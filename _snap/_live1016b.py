# -*- coding: utf-8 -*-
import json, io, os
S = os.path.dirname(os.path.abspath('/mnt/x'))
S = os.environ['SNAPDIR']
LIVE = {
 'planned_2026-10': [
  ('EG0240-43','2026-10-23','Em Revisão'),('EG0240-4','2026-10-23','Em Revisão'),
  ('EG0240-5','2026-10-26','Em Revisão'),('EG0274-38','2026-10-07','Enviado - Aguardando Análise'),
  ('EG0274-43','2026-10-31','Em Revisão'),('G0280-54','2026-10-29','Em andamento'),
  ('G0280-55','2026-10-30','Em andamento'),('G0280-53','2026-10-30','Em andamento'),
  ('G0280-51','2026-10-30','Em andamento'),('G0280-50','2026-10-30','Em andamento'),
  ('EG0286-7','2026-10-01','Enviado - Aguardando Análise'),('EG0286-11','2026-10-15','Em andamento'),
  ('EG0286-12','2026-10-19','Em andamento'),('EG0286-10','2026-10-30','Em andamento'),
  ('EG291-4','2026-10-07','Enviado - Aguardando Análise')],
 'overdue_2026-10': [],
 'sent_2026-10': [('EG291-4',None,None),('EG0286-7',None,None),('EG0275-112',None,None),
  ('EG0274-38',None,None),('EG0241-42',None,None),('EG0240-5',None,None)],
 'resolved_2026-10': [('EG291-4',None,None),('EG0286-7',None,None),('EG0275-112',None,None),
  ('EG0274-38',None,None),('EG0241-42',None,None),('EG0239-28',None,None)],
 'rework_2026-10': [('EG0286-7',None,None),('EG0274-38',None,None),('EG0241-42',None,None),('EG0240-5',None,None)],
 'lookahead_2026-10': [
  ('EG0286-19','2026-11-03','Tarefas pendentes'),('EG0285-16','2026-11-03','Tarefas pendentes'),
  ('EG0285-8','2026-11-03','Em Revisão'),('EG0285-18','2026-11-09','Tarefas pendentes'),
  ('EG0285-14','2026-11-09','Tarefas pendentes'),('EG0294-3','2026-11-18','Tarefas pendentes'),
  ('EG0294-2','2026-11-18','Tarefas pendentes'),('EG0294-1','2026-11-18','Tarefas pendentes'),
  ('EG0286-6','2026-11-18','Tarefas pendentes'),('G0280-75','2026-11-30','Em andamento'),
  ('EG0241-45','2026-11-30','Tarefas pendentes'),
  ('EG0286-18','2026-12-03','Tarefas pendentes'),('EG0286-14','2026-12-09','Tarefas pendentes'),
  ('EG0274-64','2026-12-16','Em andamento'),('EG0286-23','2026-12-22','Tarefas pendentes'),
  ('EG0274-57','2026-12-28','Tarefas pendentes'),('EG0286-9','2026-12-30','Tarefas pendentes'),
  ('EG0274-66','2026-12-30','Tarefas pendentes'),('EG0274-65','2026-12-30','Tarefas pendentes'),
  ('EG0274-59','2026-12-30','Tarefas pendentes'),('EG0274-21','2026-12-30','Tarefas pendentes'),
  ('EG0286-22','2026-12-31','Tarefas pendentes'),('EG0286-17','2026-12-31','Tarefas pendentes'),
  ('EG0286-16','2026-12-31','Tarefas pendentes'),('EG0286-15','2026-12-31','Tarefas pendentes'),
  ('EG0275-108','2026-12-31','Em andamento'),('EG0274-63','2026-12-31','Tarefas pendentes'),
  ('EG0274-62','2026-12-31','Tarefas pendentes'),('EG0274-61','2026-12-31','Tarefas pendentes'),
  ('EG0274-60','2026-12-31','Tarefas pendentes'),('EG0274-58','2026-12-31','Tarefas pendentes'),
  ('EG0240-44','2026-12-31','Em andamento'),('EG0239-54','2026-12-31','Em andamento')],
}
for name in sorted(LIVE):
    p = os.path.join(S, name + '.json')
    disk = json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else []
    dmap = {}
    for i in disk:
        f = i['fields']
        dmap[i['key']] = (f.get('duedate'), f.get('status',{}).get('name'))
    lkeys = [k for k,_,_ in LIVE[name]]
    diffs = []
    for k, du, st in LIVE[name]:
        if k not in dmap: diffs.append('+%s' % k); continue
        ddu, dst = dmap[k]
        if du is not None and du != ddu: diffs.append('%s due %s->%s' % (k, ddu, du))
        if st is not None and st != dst: diffs.append('%s st %s->%s' % (k, dst, st))
    for k in dmap:
        if k not in lkeys: diffs.append('-%s' % k)
    print('%-20s disco=%2d live=%2d  %s' % (name, len(disk), len(LIVE[name]),
          'IDENTICO' if not diffs else 'DIFERENCAS: ' + '; '.join(diffs)))
