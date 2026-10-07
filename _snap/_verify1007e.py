# -*- coding: utf-8 -*-
import re, json, calendar, os
BASE = os.path.expanduser('~/mnt/pr03-relatorio-publico')
h = open(os.path.join(BASE,'index.html'), encoding='utf-8').read()
L = h.split('\n')
for i,l in enumerate(L,1):
    if 'Snapshot gerado em' in l: print('head comment linha', i, '->', l.strip())
for i,l in enumerate(L,1):
    if '__SNAPSHOT__ = SNAP' in l or 'window.__SNAPSHOT__' in l: print('SNAPSHOT linha', i); break
for i,l in enumerate(L,1):
    if l.startswith('window.__HISTORY__='): print('script principal (__HISTORY__=) linha', i); break
tail = h[-400:]
print('--- tail ---'); print(tail[-260:])
print('banner e ultimo?', h.rstrip().endswith('</html>'), '| banner idx', h.find('Snapshot estatico - ultima atualizacao'), '| body idx', h.rfind('</body>'))
# patterns
js = open(os.path.join(BASE,'snapshot-data.js'), encoding='utf-8').read()
pats = re.search(r'var PATTERNS = \[(.*?)\];', js, re.S).group(1)
names = re.findall(r'\{n:"([^"]+)",re:new RegExp\((".*?[^\\]")\)\}', pats)
print('patterns:', len(names), [n for n,_ in names])
ds = re.search(r'var DATASETS = (\{.*?\});\n', js, re.S).group(1)
print('datasets embutidos:', len(json.loads(ds)))
# monta as 11 JQL como o artifact e testa
K='2026-10'; ld=calendar.monthrange(2026,10)[1]
Q = {
 'rework_2026-10': 'issuetype=Epic AND status changed to "Enviado - Aguardando Análise" DURING ("2026-10-01","2026-10-%d") AND status changed from "Enviado - Aguardando Análise"'%ld,
 'sent_2026-10': 'issuetype=Epic AND status changed to "Enviado - Aguardando Análise" DURING ("2026-10-01","2026-10-%d")'%ld,
 'resolved_2026-10': 'issuetype=Epic AND statusCategory=Done AND resolved>="2026-10-01" AND resolved<="2026-10-%d"'%ld,
 'overdue_2026-10': 'issuetype=Epic AND duedate<"2026-10-01" AND statusCategory!=Done',
 'lookahead_2026-10': 'issuetype=Epic AND duedate>="2026-11-01" AND duedate<="2026-12-31"',
}
for (y,m) in [(2026,5),(2026,6),(2026,7),(2026,8),(2026,9),(2026,10)]:
    k='%04d-%02d'%(y,m); d=calendar.monthrange(y,m)[1]
    Q['planned_'+k]='issuetype=Epic AND duedate>="%s-01" AND duedate<="%s-%02d"'%(k,k,d)
import json as _j
PY=[(n,_j.loads(rx)) for n,rx in names]
ok=0; used=set()
for want,q in Q.items():
    hit=None
    for n,rx in PY:
        if re.search(rx,q): hit=n; break
    used.add(hit)
    status='OK' if hit==want else 'FALHA (%s)'%hit
    if hit==want: ok+=1
    print('%-20s %s'%(want,status))
print('resolvidas %d/%d | padroes orfaos: %s'%(ok,len(Q), sorted(set(n for n,_ in PY)-used) or '(nenhum)'))
