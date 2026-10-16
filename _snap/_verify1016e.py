# -*- coding: utf-8 -*-
import json, io, os
SNAP = os.path.join(os.environ['HOME'], 'mnt', 'pr03-relatorio-publico', '_snap')
LIVE = {
'planned_2026-10': ['EG0240-43','EG0240-4','EG0240-5','EG0274-38','EG0274-43','G0280-54','G0280-55','G0280-53','G0280-51','G0280-50','EG0286-7','EG0286-11','EG0286-12','EG0286-10','EG291-4'],
'overdue_2026-10': [],
'sent_2026-10': ['EG291-4','EG0286-7','EG0275-112','EG0274-38','EG0241-42','EG0240-5'],
'resolved_2026-10': ['EG291-4','EG0286-7','EG0275-112','EG0274-38','EG0241-42','EG0239-28'],
'rework_2026-10': ['EG0286-7','EG0274-38','EG0241-42','EG0240-5'],
'lookahead_2026-10': ['EG0286-19','EG0285-16','EG0285-8','EG0285-18','EG0285-14','EG0294-3','EG0294-2','EG0294-1','EG0286-6','G0280-75','EG0241-45','EG0286-18','EG0286-14','EG0274-64','EG0286-23','EG0274-57','EG0286-9','EG0274-66','EG0274-65','EG0274-59','EG0274-21','EG0286-22','EG0286-17','EG0286-16','EG0286-15','EG0275-108','EG0274-63','EG0274-62','EG0274-61','EG0274-60','EG0274-58','EG0240-44','EG0239-54'],
}
allok = True
for n in sorted(LIVE):
    disk = {i['key'] for i in json.load(io.open(os.path.join(SNAP, n + '.json'), encoding='utf-8'))}
    live = set(LIVE[n])
    add, rem = live - disk, disk - live
    ok = not add and not rem
    allok &= ok
    print('%-20s disco=%2d live=%2d  %s' % (n, len(disk), len(live),
          'IDENTICO' if ok else 'DIFF +%s -%s' % (sorted(add), sorted(rem))))
print('\nRESULTADO:', 'sem mudancas no Jira desde o ultimo snapshot' if allok else 'HA MUDANCAS')
