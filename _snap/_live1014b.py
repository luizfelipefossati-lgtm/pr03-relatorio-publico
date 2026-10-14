# -*- coding: utf-8 -*-
"""Verificacao 14/10/2026 ~13:30 UTC: dados ao vivo do Jira x cache _snap/*.json.
Formato: key -> [status_name, status_cat, duedate, resolutiondate]"""
import json, io, os
S = os.path.dirname(os.path.abspath(__file__))

LIVE = {}
LIVE['planned_2026-10'] = [
 ["EG0240-4","Em Revisão","indeterminate","2026-10-16",None],
 ["EG0274-38","Em Revisão","indeterminate","2026-10-07",None],
 ["EG0274-43","Em Revisão","indeterminate","2026-10-31",None],
 ["G0280-54","Em andamento","indeterminate","2026-10-29",None],
 ["G0280-55","Em andamento","indeterminate","2026-10-30",None],
 ["G0280-53","Em andamento","indeterminate","2026-10-30",None],
 ["G0280-51","Em andamento","indeterminate","2026-10-30",None],
 ["G0280-50","Em andamento","indeterminate","2026-10-30",None],
 ["EG0286-7","Enviado - Aguardando Análise","done","2026-10-01","2026-10-02T13:40:01.911-0300"],
 ["EG0286-11","Em andamento","indeterminate","2026-10-15",None],
 ["EG0286-12","Em andamento","indeterminate","2026-10-19",None],
 ["EG0286-10","Em andamento","indeterminate","2026-10-30",None],
 ["EG291-4","Em andamento","indeterminate","2026-10-07",None],
]
LIVE['overdue_2026-10'] = [
 ["EG0240-5","Em Revisão","indeterminate","2026-09-30",None],
]
LIVE['sent_2026-10'] = [
 ["EG0286-7","Enviado - Aguardando Análise","done","2026-10-01","2026-10-02T13:40:01.911-0300"],
 ["EG0275-112","Enviado - Aguardando Análise","done","2026-09-04","2026-10-02T09:27:36.092-0300"],
 ["EG0241-42","Enviado - Aguardando Análise","done","2026-09-10","2026-10-02T09:30:29.370-0300"],
 ["EG0240-5","Em Revisão","indeterminate","2026-09-30",None],
]
LIVE['resolved_2026-10'] = [
 ["EG0286-7","Enviado - Aguardando Análise","done","2026-10-01","2026-10-02T13:40:01.911-0300"],
 ["EG0275-112","Enviado - Aguardando Análise","done","2026-09-04","2026-10-02T09:27:36.092-0300"],
 ["EG0241-42","Enviado - Aguardando Análise","done","2026-09-10","2026-10-02T09:30:29.370-0300"],
 ["EG0239-28","Enviado - Aguardando Análise1","done","2026-08-10","2026-10-09T09:36:29.171-0300"],
]
LIVE['rework_2026-10'] = [
 ["EG0286-7","Enviado - Aguardando Análise","done","2026-10-01","2026-10-02T13:40:01.911-0300"],
 ["EG0241-42","Enviado - Aguardando Análise","done","2026-09-10","2026-10-02T09:30:29.370-0300"],
 ["EG0240-5","Em Revisão","indeterminate","2026-09-30",None],
]
LIVE['lookahead_2026-10'] = [
 ["EG0286-19","Tarefas pendentes","new","2026-11-03",None],
 ["EG0285-16","Tarefas pendentes","new","2026-11-03",None],
 ["EG0285-8","Em Revisão","indeterminate","2026-11-03",None],
 ["EG0285-18","Tarefas pendentes","new","2026-11-09",None],
 ["EG0285-14","Tarefas pendentes","new","2026-11-09",None],
 ["EG0294-3","Tarefas pendentes","new","2026-11-18",None],
 ["EG0294-2","Tarefas pendentes","new","2026-11-18",None],
 ["EG0294-1","Tarefas pendentes","new","2026-11-18",None],
 ["EG0286-6","Tarefas pendentes","new","2026-11-18",None],
 ["G0280-75","Em andamento","indeterminate","2026-11-30",None],
 ["EG0241-45","Tarefas pendentes","new","2026-11-30",None],
 ["EG0286-18","Tarefas pendentes","new","2026-12-03",None],
 ["EG0286-14","Tarefas pendentes","new","2026-12-09",None],
 ["EG0274-64","Em andamento","indeterminate","2026-12-16",None],
 ["EG0286-23","Tarefas pendentes","new","2026-12-22",None],
 ["EG0274-57","Tarefas pendentes","new","2026-12-28",None],
 ["EG0286-9","Tarefas pendentes","new","2026-12-30",None],
 ["EG0274-66","Tarefas pendentes","new","2026-12-30",None],
 ["EG0274-65","Tarefas pendentes","new","2026-12-30",None],
 ["EG0274-59","Tarefas pendentes","new","2026-12-30",None],
 ["EG0274-21","Tarefas pendentes","new","2026-12-30",None],
 ["EG0286-22","Tarefas pendentes","new","2026-12-31",None],
 ["EG0286-17","Tarefas pendentes","new","2026-12-31",None],
 ["EG0286-16","Tarefas pendentes","new","2026-12-31",None],
 ["EG0286-15","Tarefas pendentes","new","2026-12-31",None],
 ["EG0275-108","Em andamento","indeterminate","2026-12-31",None],
 ["EG0274-63","Tarefas pendentes","new","2026-12-31",None],
 ["EG0274-62","Tarefas pendentes","new","2026-12-31",None],
 ["EG0274-61","Tarefas pendentes","new","2026-12-31",None],
 ["EG0274-60","Tarefas pendentes","new","2026-12-31",None],
 ["EG0274-58","Tarefas pendentes","new","2026-12-31",None],
 ["EG0240-44","Em andamento","indeterminate","2026-12-31",None],
 ["EG0239-54","Em andamento","indeterminate","2026-12-31",None],
]

FIELDS = ['status_name','status_cat','duedate','resolutiondate']
diffs = 0
for name, rows in sorted(LIVE.items()):
    cache = json.load(io.open(os.path.join(S, name + '.json'), encoding='utf-8'))
    ck = [i['key'] for i in cache]; lk = [r[0] for r in rows]
    if ck != lk:
        diffs += 1
        print('%-20s CONJUNTO/ORDEM DIFERENTE cache=%d live=%d' % (name, len(ck), len(lk)))
        print('   so cache:', sorted(set(ck)-set(lk)), '| so live:', sorted(set(lk)-set(ck)))
        continue
    bad = []
    for c, r in zip(cache, rows):
        f = c['fields']
        cf = [f['status']['name'], f['status']['statusCategory']['key'],
              f.get('duedate'), f.get('resolutiondate')]
        for j, fn in enumerate(FIELDS):
            if cf[j] != r[1+j]:
                bad.append('%s.%s cache=%r live=%r' % (c['key'], fn, cf[j], r[1+j]))
    if bad:
        diffs += 1
        print('%-20s %d divergencias' % (name, len(bad)))
        for b in bad: print('    ', b)
    else:
        print('%-20s %2d itens  IDENTICO' % (name, len(rows)))
print('\nCONJUNTOS DIVERGENTES:', diffs)
