# -*- coding: utf-8 -*-
import json, re, os, calendar, datetime
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H=open(os.path.join(B,'index.html'),encoding='utf-8').read()
JS=open(os.path.join(B,'snapshot-data.js'),encoding='utf-8').read()
ok=lambda c,m:print(('OK  ' if c else 'FALHA ')+m)

m=re.search(r'<!-- Snapshot gerado em (\S+) -->',H); ok(bool(m),'carimbo head: %s'%(m.group(1) if m else '-'))
i=H.find('window.__SNAPSHOT__'); j=H.find('/* ========== CONSTANTS ========== */'); h=H.find('window.__HISTORY__=')
ok(i>0 and i<h and i<j,'__SNAPSHOT__ antes do script do artifact (%d < %d/%d)'%(i,h,j))
b=H.rfind('Snapshot estatico - ultima'); e=H.rfind('</body>')
ok(b>0 and b<e and len(H[e:].strip())<=len('</body>\n</html>')+2,'banner como ultimo elemento do body')

# padroes do snapshot-data.js x JQL que o artifact monta
pats=json.loads('['+re.search(r'var PATTERNS = \[(.*?)\];',JS,re.S).group(1).replace('n:','"n":').replace('re:new RegExp(','"re":(')+']') if False else None
raw=re.search(r'var PATTERNS = \[(.*?)\];',JS,re.S).group(1)
P=[(json.loads(a),json.loads(bb)) for a,bb in re.findall(r'\{n:("(?:[^"\\]|\\.)*"),re:new RegExp\(("(?:[^"\\]|\\.)*")\)\}',raw)]
ETQ='issuetype in ("Epic","Fluxo de trabalho")'
NOW=datetime.date(2026,10,7); ld=lambda y,m:calendar.monthrange(y,m)[1]
Q=[]
y,m=2026,10; s='%04d-%02d-01'%(y,m); en='%04d-%02d-%02d'%(y,m,ld(y,m))
Q+=[('planned_2026-10',ETQ+' AND duedate>="%s" AND duedate<="%s" ORDER BY project ASC, duedate ASC'%(s,en)),
    ('overdue_2026-10',ETQ+' AND duedate<"%s" AND statusCategory!=Done ORDER BY duedate ASC'%s),
    ('lookahead_2026-10',ETQ+' AND duedate>="2026-11-01" AND duedate<="2026-12-31" ORDER BY duedate ASC'),
    ('sent_2026-10',ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("%s","%s")'%(s,en)),
    ('resolved_2026-10',ETQ+' AND statusCategory=Done AND resolved>="%s" AND resolved<="%s"'%(s,en)),
    ('rework_2026-10',ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("%s","%s") AND status changed from "Enviado - Aguardando Análise"'%(s,en))]
for off in range(5,-1,-1):
    yy,mm=2026,10-off
    while mm<=0: mm+=12; yy-=1
    k='%04d-%02d'%(yy,mm)
    Q.append(('planned_'+k,ETQ+' AND duedate>="%s-01" AND duedate<="%s-%02d" ORDER BY project ASC, duedate ASC'%(k,k,ld(yy,mm))))
seen=set(); bad=0
for name,jql in Q:
    hit=next((n for n,rx in P if re.search(rx,jql)),None)
    if hit!=name: print('   FALHA %-20s -> %s'%(name,hit)); bad+=1
    else: seen.add(hit)
ok(bad==0,'%d consultas JQL resolvem para o conjunto correto'%len(Q))
ok(seen=={n for n,_ in P},'nenhum padrao orfao (%d padroes / %d usados)'%(len(P),len(seen)))

for n in ['planned','overdue','lookahead','sent','resolved','rework']:
    d=json.load(open(os.path.join(B,'_snap','%s_2026-10.json'%n),encoding='utf-8'))
    print('   %-10s %d'%(n,len(d)))

for t in ['avatarUrls','iconUrl','emailAddress','api.atlassian.com','@engeplus','fetch(','XMLHttpRequest','EventSource','sendBeacon']:
    ok(t not in H,'ausente: %s'%t)
ok(H.count('accountId')==1,'accountId apenas no comentario do gerador (%d)'%H.count('accountId'))
ext=sorted(set(re.findall(r'src="https?://([^/"]+)',H))); ok(ext==['cdn.jsdelivr.net'],'hosts externos: %s'%ext)
print('index.html %d bytes / %d linhas | snapshot-data.js %d bytes'%(len(H.encode()),H.count('\n')+1,len(JS.encode())))
