# -*- coding: utf-8 -*-
"""Conferencia estrutural da geracao de 15/10/2026 17:31 BRT."""
import io, os, re, json, hashlib, calendar
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
h = io.open(os.path.join(B,'index.html'), encoding='utf-8').read()
hb = h.encode('utf-8')
js = io.open(os.path.join(B,'snapshot-data.js'), encoding='utf-8').read()

print('== tamanhos ==')
print('index.html      ', len(hb))
print('snapshot-data.js', len(js.encode('utf-8')))

print('== carimbos ==')
print('head comment  :', re.search(r'<!-- Snapshot gerado em (.*?) -->', h).group(1))
print('head logo apos:', h.index('<!-- Snapshot') - h.index('<head>') == len('<head>\n'))
bn = re.findall(r'ultima atualizacao: ([0-9/]+ [0-9:]+)', h)
print('banner        :', bn, 'ocorrencias:', len(bn))
print('banner no fim :', h.rstrip().endswith('</html>') and
      h.rstrip()[:-len('</html>')].rstrip().endswith('</body>') and
      '<div style="background:#fef3c7' in h.rsplit('</body>',1)[0][-400:])

print('== ordem de execucao (bytes) ==')
p_inj = len(h[:h.index('PR.03 - Relatorio de Indicadores de EPICs - DADOS ESTATICOS')].encode('utf-8'))
p_sn  = len(h[:h.index('window.__SNAPSHOT__ = SNAP')].encode('utf-8'))
p_hi  = len(h[:h.index('window.__HISTORY__={')].encode('utf-8'))
print('bloco injetado abre em    ', p_inj)
print('window.__SNAPSHOT__ =     ', p_sn)
print('window.__HISTORY__= (orig)', p_hi, '| ordem OK:', p_inj < p_sn < p_hi)

print('== hashes dos conjuntos em _snap/ ==')
SD = os.path.join(B,'_snap')
for n in ['planned_2026-10','overdue_2026-10','lookahead_2026-10','sent_2026-10','resolved_2026-10','rework_2026-10']:
    raw = io.open(os.path.join(SD,n+'.json'),'rb').read()
    print('%-18s %s %6d bytes' % (n, hashlib.sha256(raw).hexdigest()[:12], len(raw)))
raw = io.open(os.path.join(B,'_projects_min.json'),'rb').read()
print('%-18s %s %6d bytes' % ('_projects_min', hashlib.sha256(raw).hexdigest()[:12], len(raw)))

print('== 12 JQL vs padroes do snapshot-data.js ==')
pats = [(m.group(1), m.group(2)) for m in
        re.finditer(r'\{n:"([^"]+)",re:new RegExp\("((?:[^"\\]|\\.)*)"\)\}', js)]
pats = [(n, json.loads('"'+rx+'"')) for n, rx in pats]
ETQ = 'issuetype in ("Epic","Fluxo de trabalho")'
F = ''
def ld(y,m): return calendar.monthrange(y,m)[1]
Q = []
y, m = 2026, 10
k = '%04d-%02d' % (y,m); e = '%s-%02d' % (k, ld(y,m))
Q.append(('planned_'+k,  ETQ+' AND duedate>="%s-01" AND duedate<="%s" ORDER BY project ASC, duedate ASC' % (k,e)))
Q.append(('overdue_'+k,  ETQ+' AND duedate<"%s-01" AND statusCategory!=Done ORDER BY duedate ASC' % k))
Q.append(('lookahead_'+k,ETQ+' AND duedate>="2026-11-01" AND duedate<="2026-12-31" ORDER BY duedate ASC'))
Q.append(('sent_'+k,     ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("%s-01","%s")' % (k,e)))
Q.append(('resolved_'+k, ETQ+' AND statusCategory=Done AND resolved>="%s-01" AND resolved<="%s"' % (k,e)))
Q.append(('rework_'+k,   ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("%s-01","%s") AND status changed from "Enviado - Aguardando Análise"' % (k,e)))
for mm in range(5, 11):
    kk = '2026-%02d' % mm; ee = '%s-%02d' % (kk, ld(2026,mm))
    Q.append(('planned_'+kk, ETQ+' AND duedate>="%s-01" AND duedate<="%s" ORDER BY project ASC, duedate ASC' % (kk,ee)))
hit = set(); bad = 0
for want, q in Q:
    got = None
    for n, rx in pats:
        if re.search(rx, q): got = n; break
    ok = (got == want)
    if not ok: bad += 1
    hit.add(got)
    print('  %-18s -> %-18s %s' % (want, got, 'OK' if ok else '*** ERRO ***'))
print('consultas:', len(Q), '| erros:', bad, '| padroes:', len(pats),
      '| orfaos:', [n for n,_ in pats if n not in hit])

print('== privacidade ==')
for t in ['accountId','avatarUrls','iconUrl','emailAddress','api.atlassian.com','@']:
    print('  %-18s %d' % (t, h.count(t)))
print('  regex e-mail      ', len(re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', h)))
