# -*- coding: utf-8 -*-
# Verificacao pos-geracao da rodada 2026-10-09 ~17:30 UTC (14:30 BRT).
import re, json, os
D = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(D, os.pardir)
s = open(os.path.join(B, 'index.html'), encoding='utf-8').read()
print('tamanho index.html: %.1f KB' % (len(s.encode())/1024))
# privacidade
for t in ['avatarUrls','iconUrl','emailAddress','@engeplus','api.atlassian.com','accountId']:
    print('  %-20s %d' % (t, s.count(t)))
print('  base atlassian browse:', s.count('https://projetos-engeplus.atlassian.net/browse/'))
# padroes x JQL reconstruidas como o artifact monta
js = open(os.path.join(B, 'snapshot-data.js'), encoding='utf-8').read()
pats = re.findall(r'\{n:"([^"]+)",re:new RegExp\("((?:[^"\\]|\\.)*)"\)\}', js)
print('padroes:', len(pats))
ETQ = 'issuetype in ("Epic","Fluxo de trabalho")'
F = ' ORDER BY project ASC, duedate ASC'
Q = []
Q.append(('planned_2026-10', ETQ+' AND duedate>="2026-10-01" AND duedate<="2026-10-31"'+F))
Q.append(('overdue_2026-10', ETQ+' AND duedate<"2026-10-01" AND statusCategory!=Done ORDER BY duedate ASC'))
Q.append(('lookahead_2026-10', ETQ+' AND duedate>="2026-11-01" AND duedate<="2026-12-31" ORDER BY duedate ASC'))
Q.append(('sent_2026-10', ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("2026-10-01","2026-10-31")'))
Q.append(('resolved_2026-10', ETQ+' AND statusCategory=Done AND resolved>="2026-10-01" AND resolved<="2026-10-31"'))
Q.append(('rework_2026-10', ETQ+' AND status changed to "Enviado - Aguardando Análise" DURING ("2026-10-01","2026-10-31") AND status changed from "Enviado - Aguardando Análise"'))
for k in ['2026-05','2026-06','2026-07','2026-08','2026-09','2026-10']:
    ld = {'2026-05':31,'2026-06':30,'2026-07':31,'2026-08':31,'2026-09':30,'2026-10':31}[k]
    Q.append(('planned_'+k, ETQ+' AND duedate>="%s-01" AND duedate<="%s-%02d"%s' % (k,k,ld,F)))
used, bad = set(), 0
for want, jql in Q:
    hit = None
    for n, rx in pats:
        if re.search(rx.encode().decode('unicode_escape'), jql): hit = n; break
    ok = (hit == want) or (want.startswith('planned_2026-10') and hit == want)
    if not ok: bad += 1
    if hit: used.add(hit)
    print('  %-20s -> %-20s %s' % (want, hit, 'OK' if ok else '*** DIVERGENTE ***'))
orf = [n for n, _ in pats if n not in used]
print('divergentes:', bad, '| padroes orfaos:', orf)
