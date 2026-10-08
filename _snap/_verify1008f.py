# -*- coding: utf-8 -*-
import json, os, re, calendar
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
html = open(os.path.join(B,'index.html'), encoding='utf-8').read()
js   = open(os.path.join(B,'snapshot-data.js'), encoding='utf-8').read()
lines = html.split('\n')
ok = lambda c,m: print(('OK   ' if c else 'FALHA ') + m)

# 1 comentario no head
m = re.search(r'<!-- Snapshot gerado em (.+?) -->', html)
stamp = m.group(1) if m else None
ln = html[:m.start()].count('\n')+1 if m else -1
ok(m and html.find('<head>') < m.start() < html.find('<head>')+200, 'comentario de geracao no topo do <head> (linha %d): %s' % (ln, stamp))

# 2 snapshot antes do script principal
i_snap = html.find('window.__SNAPSHOT__')
i_main = max(html.find('<script>\nwindow.__HISTORY__='), html.find('/* ========== CONSTANTS ========== */'))
ok(0 < i_snap < i_main, 'bloco __SNAPSHOT__ antes do script principal (linha %d < %d)'
   % (html[:i_snap].count('\n')+1, html[:i_main].count('\n')+1))

# 3 banner como ultimo elemento do body
tail = html[html.find('Snapshot estatico - ultima atualizacao'):]
ok('Snapshot estatico - ultima atualizacao' in html and re.search(
    r'Snapshot estatico - ultima atualizacao: ([\d/ :]+)[^<]*</div>\s*</body>\s*</html>\s*$', html),
   'banner e o ultimo elemento do <body>: %s' % (re.search(r'ultima atualizacao: ([\d/ :]+)', html).group(1).strip(),))

# 4 padroes JQL
pats = [(json.loads(n), json.loads(r)) for n, r in
        re.findall(r'\{n:("(?:[^"\\]|\\.)*"),re:new RegExp\(("(?:[^"\\]|\\.)*")\)\}', js)]
SNAP = json.loads(re.search(r'var SNAP = (\{.*?\});\n', js, re.S).group(1))
DS   = json.loads(re.search(r'var DATASETS = (\{.*?\});\n\n', js, re.S).group(1))
ETQ = 'issuetype in (' + ','.join('"%s"' % n for n in SNAP['epicTypeNames']) + ')'
ld = lambda y,m: calendar.monthrange(y,m)[1]
def mk(y,m):
    s, e = '%04d-%02d-01'%(y,m), '%04d-%02d-%02d'%(y,m,ld(y,m))
    return s, e
Y, M = 2026, 10
s, e = mk(Y,M)
ly, lm = (Y, M+1) if M<12 else (Y+1,1); ey, em = (Y, M+2) if M<=10 else (Y+1, M+2-12)
ls0, le0 = '%04d-%02d-01'%(ly,lm), '%04d-%02d-%02d'%(ey,em,ld(ey,em))
queries = {
 'planned_2026-10':  ETQ+' AND duedate>="%s" AND duedate<="%s" ORDER BY project ASC, duedate ASC'%(s,e),
 'overdue_2026-10':  ETQ+' AND duedate<"%s" AND statusCategory!=Done ORDER BY duedate ASC'%s,
 'lookahead_2026-10':ETQ+' AND duedate>="%s" AND duedate<="%s" ORDER BY duedate ASC'%(ls0,le0),
 'sent_2026-10':     ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("%s","%s")'%(s,e),
 'resolved_2026-10': ETQ+' AND statusCategory=Done AND resolved>="%s" AND resolved<="%s"'%(s,e),
 'rework_2026-10':   ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("%s","%s") AND status changed from "Enviado - Aguardando Análise"'%(s,e),
}
for off in range(5,-1,-1):
    y, mm = Y, M-off
    while mm <= 0: mm += 12; y -= 1
    a, b = mk(y,mm)
    queries['planned_%04d-%02d'%(y,mm)] = ETQ+' AND duedate>="%s" AND duedate<="%s" ORDER BY project ASC, duedate ASC'%(a,b)
bad = []
for want, q in sorted(queries.items()):
    hit = next((n for n, rx in pats if re.search(rx, q)), None)
    if hit != want: bad.append('%s -> %s' % (want, hit))
ok(not bad, 'todas as %d consultas JQL resolvem para o conjunto certo %s' % (len(queries), bad or ''))
orf = [n for n,_ in pats if n not in DS]
ok(not orf, 'nenhum padrao orfao (%d padroes, %d datasets no JS)' % (len(pats), len(DS)))
ok(all(len(DS[n])>=0 for n,_ in pats), 'contagens: ' + ' '.join('%s=%d'%(n,len(DS[n])) for n,_ in pats if n.endswith('2026-10')))

# 5 privacidade
leaks = {w: html.count(w) for w in ('avatarUrls','iconUrl','emailAddress','api.atlassian.com','@engeplus','accountId')}
ok(all(v==0 for k,v in leaks.items() if k!='accountId') and leaks['accountId']<=1,
   'varredura de privacidade: ' + ', '.join('%s=%d'%kv for kv in leaks.items()))

# 6 externos
# Recursos efetivamente CARREGADOS pela pagina (src=) devem ser so o CDN do Chart.js.
# projetos-engeplus.atlassian.net aparece apenas como destino de link (href em <a
# target="_blank">) nas tabelas e no rodape - e um deep link para o issue no Jira,
# herdado do artifact; nao gera requisicao nem consulta de dados.
loaded = sorted(set(re.findall(r'src="https?://([\w.-]+)', html)))
ok(loaded == ['cdn.jsdelivr.net'], 'recursos carregados de hosts externos: %s' % loaded)
net = re.findall(r'\b(?:fetch|XMLHttpRequest|EventSource|sendBeacon)\s*\(', html)
ok(not net, 'nenhuma chamada de rede no runtime (fetch/XHR/EventSource/sendBeacon): %d' % len(net))
linked = sorted(set(re.findall(r'https?://([\w.-]+)', html)))
ok(linked == ['cdn.jsdelivr.net', 'projetos-engeplus.atlassian.net'],
   'hosts referenciados (carregados + alvos de link): %s' % linked)

print('index.html %d bytes (%.1f KB) | snapshot-data.js %d bytes (%.1f KB) | %d linhas'
      % (len(html.encode()), len(html.encode())/1024, len(js.encode()), len(js.encode())/1024, len(lines)))
