# -*- coding: utf-8 -*-
import io, os, re, json, hashlib, calendar
B = os.path.expanduser('~/mnt/pr03-relatorio-publico')
js = io.open(os.path.join(B,'snapshot-data.js'), encoding='utf-8').read()
html = io.open(os.path.join(B,'index.html'), encoding='utf-8').read()

print('md5 _artifact_src.html:', hashlib.md5(io.open(os.path.join(B,'_artifact_src.html'),'rb').read()).hexdigest())
print('bytes index.html=%d snapshot-data.js=%d' % (
    len(html.encode('utf-8')), len(js.encode('utf-8'))))

# --- padroes gravados ---
m = re.search(r'var PATTERNS = \[(.*?)\];', js, re.S)
raw = m.group(1)
pats = re.findall(r'\{n:("(?:[^"\\]|\\.)*"),re:new RegExp\(("(?:[^"\\]|\\.)*")\)\}', raw)
pats = [(json.loads(n), json.loads(r)) for n, r in pats]
print('padroes:', len(pats))

ETQ = 'issuetype in ("Epic","Fluxo de trabalho")'
def ld(y,mn): return calendar.monthrange(y,mn)[1]
queries = {}
y, mn = 2026, 10
s='%04d-%02d-01'%(y,mn); e='%04d-%02d-%02d'%(y,mn,ld(y,mn))
queries['planned_2026-10'] = ETQ+' AND duedate>="%s" AND duedate<="%s" ORDER BY project ASC, duedate ASC'%(s,e)
queries['overdue_2026-10'] = ETQ+' AND duedate<"%s" AND statusCategory!=Done ORDER BY duedate ASC'%s
queries['lookahead_2026-10'] = ETQ+' AND duedate>="2026-11-01" AND duedate<="2026-12-31" ORDER BY duedate ASC'
queries['sent_2026-10'] = ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("%s","%s")'%(s,e)
queries['resolved_2026-10'] = ETQ+' AND statusCategory=Done AND resolved>="%s" AND resolved<="%s"'%(s,e)
queries['rework_2026-10'] = ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("%s","%s") AND status changed from "Enviado - Aguardando Análise"'%(s,e)
for off in range(5,-1,-1):
    yy, mm = 2026, 10-off
    while mm<=0: mm+=12; yy-=1
    k='%04d-%02d'%(yy,mm)
    queries.setdefault('planned_'+k, ETQ+' AND duedate>="%s-01" AND duedate<="%s-%02d" ORDER BY project ASC, duedate ASC'%(k,k,ld(yy,mm)))

def resolve(q):
    for n, rx in pats:
        if re.search(rx, q): return n
    return None

orph = set(n for n,_ in pats)
ok = True
for name, q in sorted(queries.items()):
    r = resolve(q)
    orph.discard(r)
    flag = 'OK ' if r == name else 'ERRO'
    if r != name: ok = False
    print('  %s %-20s -> %s' % (flag, name, r))
print('padroes orfaos:', sorted(orph) or 'nenhum')
print('TODAS AS CONSULTAS RESOLVEM CORRETAMENTE:', ok and not orph)

# --- privacidade ---
print('--- privacidade ---')
for t in ['avatarUrls','iconUrl','emailAddress','@engeplus','api.atlassian.com']:
    print('  %-20s ocorrencias: %d' % (t, html.count(t)))
print('  accountId ocorrencias: %d' % html.count('accountId'),
      '(contexto:', [l.strip()[:60] for l in html.split('\n') if 'accountId' in l][:3], ')')
print('  atlassian.net:', sorted(set(re.findall(r'https://[a-z0-9.-]*atlassian[a-z0-9.-]*/[^\s"\'<>]*', html)))[:3])

# --- indicadores de outubro ---
snap = json.loads(re.search(r'var SNAP = (\{.*?\});\n', js, re.S).group(1))
D = snap['datasets']
pl = D['planned_2026-10']; sent = D['sent_2026-10']; res = D['resolved_2026-10']; rw = D['rework_2026-10']
look = D['lookahead_2026-10']; ovd = D['overdue_2026-10']
def cat(i): return i['fields']['status']['statusCategory']['key']
union = {i['key']: i for i in sent}
for i in res: union.setdefault(i['key'], i)
rwk = {i['key'] for i in rw}
done_pl = [i for i in pl if cat(i)=='done']
print('--- outubro/2026 ---')
print('  previstos=%d concluidos=%d OTD=%d%%' % (len(pl), len(done_pl), round(100.0*len(done_pl)/len(pl))))
print('  envios(uniao)=%d retrabalho=%d -> %d%%' % (len(union), len(rwk & set(union)), round(100.0*len(rwk & set(union))/len(union))))
print('  pendencias do mes=%d  atraso acumulado=%d' % (len(pl)-len(done_pl), len(ovd)))
from collections import Counter
print('  por projeto:', dict(Counter(i['fields']['project']['key'] for i in pl)))
print('  por status :', dict(Counter(i['fields']['status']['name'] for i in pl)))
print('--- lookahead ---')
print('  total=%d por projeto=%s' % (len(look), dict(Counter(i['fields']['project']['key'] for i in look))))
print('  nov=%d dez=%d  dez 2a quinzena=%d' % (
    sum(1 for i in look if i['fields']['duedate'][:7]=='2026-11'),
    sum(1 for i in look if i['fields']['duedate'][:7]=='2026-12'),
    sum(1 for i in look if i['fields']['duedate'][:7]=='2026-12' and int(i['fields']['duedate'][8:])>=16)))
print('--- meses congelados: EG0256-30 presente? ---')
for k, mo in sorted(snap['months'].items()):
    print('  %s lookahead=%d EG0256-30=%s' % (k, len(mo['look']), any(i['key']=='EG0256-30' for i in mo['look'])))
