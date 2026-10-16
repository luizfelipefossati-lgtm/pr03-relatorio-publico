# -*- coding: utf-8 -*-
import json, os, io
SNAP = os.path.join(os.environ['HOME'], 'mnt', 'pr03-relatorio-publico', '_snap')

def load(n):
    return json.load(io.open(os.path.join(SNAP, n + '.json'), encoding='utf-8'))

# live: key -> (duedate, status_name, resolutiondate)  (None = nao conferido)
LIVE = {
'planned_2026-10': {
 'EG0240-43':('2026-10-23','Em Revisão',None),
 'EG0240-4':('2026-10-23','Em Revisão',None),
 'EG0240-5':('2026-10-26','Em Revisão',None),
 'EG0274-38':('2026-10-07','Enviado - Aguardando Análise','2026-10-15T15:30:49.463-0300'),
 'EG0274-43':('2026-10-31','Em Revisão',None),
 'G0280-54':('2026-10-29','Em andamento',None),
 'G0280-55':('2026-10-30','Em andamento',None),
 'G0280-53':('2026-10-30','Em andamento',None),
 'G0280-51':('2026-10-30','Em andamento',None),
 'G0280-50':('2026-10-30','Em andamento',None),
 'EG0286-7':('2026-10-01','Enviado - Aguardando Análise','2026-10-02T13:40:01.911-0300'),
 'EG0286-11':('2026-10-15','Em andamento',None),
 'EG0286-12':('2026-10-19','Em andamento',None),
 'EG0286-10':('2026-10-30','Em andamento',None),
 'EG291-4':('2026-10-07','Enviado - Aguardando Análise','2026-10-15T13:59:49.573-0300'),
},
'overdue_2026-10': {},
'sent_2026-10': {
 'EG291-4':('2026-10-07','Enviado - Aguardando Análise','2026-10-15T13:59:49.573-0300'),
 'EG0286-7':('2026-10-01','Enviado - Aguardando Análise','2026-10-02T13:40:01.911-0300'),
 'EG0275-112':('2026-09-04','Enviado - Aguardando Análise','2026-10-02T09:27:36.092-0300'),
 'EG0274-38':('2026-10-07','Enviado - Aguardando Análise','2026-10-15T15:30:49.463-0300'),
 'EG0241-42':('2026-09-10','Enviado - Aguardando Análise','2026-10-02T09:30:29.370-0300'),
 'EG0240-5':('2026-10-26','Em Revisão',None),
},
'resolved_2026-10': {
 'EG291-4':('2026-10-07',None,'2026-10-15T13:59:49.573-0300'),
 'EG0286-7':('2026-10-01',None,'2026-10-02T13:40:01.911-0300'),
 'EG0275-112':('2026-09-04',None,'2026-10-02T09:27:36.092-0300'),
 'EG0274-38':('2026-10-07',None,'2026-10-15T15:30:49.463-0300'),
 'EG0241-42':('2026-09-10',None,'2026-10-02T09:30:29.370-0300'),
 'EG0239-28':('2026-08-10',None,'2026-10-09T09:36:29.171-0300'),
},
'rework_2026-10': {
 'EG0286-7':(None,None,None),'EG0274-38':(None,None,None),
 'EG0241-42':(None,None,None),'EG0240-5':(None,None,None),
},
'lookahead_2026-10': {
 'EG0286-19':('2026-11-03','Tarefas pendentes',None),
 'EG0285-16':('2026-11-03','Tarefas pendentes',None),
 'EG0285-8':('2026-11-03','Em Revisão',None),
 'EG0285-18':('2026-11-09','Tarefas pendentes',None),
 'EG0285-14':('2026-11-09','Tarefas pendentes',None),
 'EG0294-3':('2026-11-18','Tarefas pendentes',None),
 'EG0294-2':('2026-11-18','Tarefas pendentes',None),
 'EG0294-1':('2026-11-18','Tarefas pendentes',None),
 'EG0286-6':('2026-11-18','Tarefas pendentes',None),
 'G0280-75':('2026-11-30','Em andamento',None),
 'EG0241-45':('2026-11-30','Tarefas pendentes',None),
 'EG0286-18':('2026-12-03','Tarefas pendentes',None),
 'EG0286-14':('2026-12-09','Tarefas pendentes',None),
 'EG0274-64':('2026-12-16','Em andamento',None),
 'EG0286-23':('2026-12-22','Tarefas pendentes',None),
 'EG0274-57':('2026-12-28','Tarefas pendentes',None),
 'EG0286-9':('2026-12-30','Tarefas pendentes',None),
 'EG0274-66':('2026-12-30','Tarefas pendentes',None),
 'EG0274-65':('2026-12-30','Tarefas pendentes',None),
 'EG0274-59':('2026-12-30','Tarefas pendentes',None),
 'EG0274-21':('2026-12-30','Tarefas pendentes',None),
 'EG0286-22':('2026-12-31','Tarefas pendentes',None),
 'EG0286-17':('2026-12-31','Tarefas pendentes',None),
 'EG0286-16':('2026-12-31','Tarefas pendentes',None),
 'EG0286-15':('2026-12-31','Tarefas pendentes',None),
 'EG0275-108':('2026-12-31','Em andamento',None),
 'EG0274-63':('2026-12-31','Tarefas pendentes',None),
 'EG0274-62':('2026-12-31','Tarefas pendentes',None),
 'EG0274-61':('2026-12-31','Tarefas pendentes',None),
 'EG0274-60':('2026-12-31','Tarefas pendentes',None),
 'EG0274-58':('2026-12-31','Tarefas pendentes',None),
 'EG0240-44':('2026-12-31','Em andamento',None),
 'EG0239-54':('2026-12-31','Em andamento',None),
},
}

allok = True
for name in sorted(LIVE):
    disk = load(name)
    dmap = {}
    for it in disk:
        f = it['fields']
        dmap[it['key']] = (f.get('duedate'), (f.get('status') or {}).get('name'), f.get('resolutiondate'))
    live = LIVE[name]
    diffs = []
    for k, (du, st, rd) in live.items():
        if k not in dmap:
            diffs.append('+%s novo' % k); continue
        ddu, dst, drd = dmap[k]
        if du is not None and du != ddu: diffs.append('%s duedate %s->%s' % (k, ddu, du))
        if st is not None and st != dst: diffs.append('%s status %s->%s' % (k, dst, st))
        if rd is not None and rd != drd: diffs.append('%s resolv %s->%s' % (k, drd, rd))
    for k in dmap:
        if k not in live: diffs.append('-%s saiu' % k)
    if diffs: allok = False
    print('%-20s disco=%2d live=%2d  %s' % (name, len(disk), len(live),
          'IDENTICO' if not diffs else 'DIFF: ' + '; '.join(diffs)))
print('\nRESULTADO:', 'sem mudancas no Jira' if allok else 'HA MUDANCAS')
