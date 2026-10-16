# -*- coding: utf-8 -*-
"""Confere os datasets do mes corrente no snapshot-data.js contra a consulta ao vivo
do Jira feita em 16/10/2026 (madrugada). Nao altera nada - so compara e reporta."""
import io, json, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
s = io.open(os.path.join(BASE, 'snapshot-data.js'), encoding='utf-8').read()
i = s.index('var DATASETS = ') + len('var DATASETS = ')
j = s.index('\n', i)
DISK = json.loads(s[i:j].rstrip().rstrip(';'))

# (key, duedate, status, resolutiondate, updated)
LIVE = {
 'planned_2026-10': [
  ('EG0286-7','2026-10-01','Enviado - Aguardando Análise','2026-10-02T13:40:01.911-0300','2026-10-02T13:40:01.929-0300'),
  ('EG291-4','2026-10-07','Enviado - Aguardando Análise','2026-10-15T13:59:49.573-0300','2026-10-15T14:05:50.668-0300'),
  ('EG0274-38','2026-10-07','Enviado - Aguardando Análise','2026-10-15T15:30:49.463-0300','2026-10-15T15:30:49.471-0300'),
  ('EG0286-11','2026-10-15','Em andamento',None,'2026-09-28T09:29:27.853-0300'),
  ('EG0286-12','2026-10-19','Em andamento',None,'2026-09-28T09:31:11.033-0300'),
  ('EG0240-43','2026-10-23','Em Revisão',None,'2026-10-15T14:50:41.722-0300'),
  ('EG0240-4','2026-10-23','Em Revisão',None,'2026-10-15T13:58:30.870-0300'),
  ('EG0240-5','2026-10-26','Em Revisão',None,'2026-10-15T13:58:00.568-0300'),
  ('G0280-54','2026-10-29','Em andamento',None,'2026-09-30T14:59:57.634-0300'),
  ('G0280-55','2026-10-30','Em andamento',None,'2026-09-30T14:59:43.601-0300'),
  ('G0280-53','2026-10-30','Em andamento',None,'2026-09-30T14:59:30.308-0300'),
  ('G0280-51','2026-10-30','Em andamento',None,'2026-09-30T15:00:04.232-0300'),
  ('G0280-50','2026-10-30','Em andamento',None,'2026-09-30T14:59:50.045-0300'),
  ('EG0286-10','2026-10-30','Em andamento',None,'2026-09-30T14:55:35.086-0300'),
  ('EG0274-43','2026-10-31','Em Revisão',None,'2026-09-28T09:26:55.035-0300')],
 'overdue_2026-10': [],
 'sent_2026-10': [
  ('EG291-4',None,None,None,None),('EG0286-7',None,None,None,None),
  ('EG0275-112',None,None,None,None),('EG0274-38',None,None,None,None),
  ('EG0241-42',None,None,None,None),('EG0240-5',None,None,None,None)],
 'resolved_2026-10': [
  ('EG291-4',None,None,None,None),('EG0286-7',None,None,None,None),
  ('EG0275-112',None,None,None,None),('EG0274-38',None,None,None,None),
  ('EG0241-42',None,None,None,None),('EG0239-28',None,None,None,None)],
 'rework_2026-10': [
  ('EG0286-7',None,None,None,None),('EG0274-38',None,None,None,None),
  ('EG0241-42',None,None,None,None),('EG0240-5',None,None,None,None)],
 'lookahead_2026-10': [
  ('EG0286-19','2026-11-03','Tarefas pendentes',None,'2026-06-17T17:38:40.836-0300'),
  ('EG0285-16','2026-11-03','Tarefas pendentes',None,'2026-05-14T11:31:20.526-0300'),
  ('EG0285-8','2026-11-03','Em Revisão',None,'2026-09-30T11:46:00.212-0300'),
  ('EG0285-18','2026-11-09','Tarefas pendentes',None,'2026-05-14T11:31:30.030-0300'),
  ('EG0285-14','2026-11-09','Tarefas pendentes',None,'2026-05-14T11:31:11.610-0300'),
  ('EG0294-3','2026-11-18','Tarefas pendentes',None,'2026-10-02T13:45:46.124-0300'),
  ('EG0294-2','2026-11-18','Tarefas pendentes',None,'2026-10-02T13:45:37.682-0300'),
  ('EG0294-1','2026-11-18','Tarefas pendentes',None,'2026-10-02T13:45:29.242-0300'),
  ('EG0286-6','2026-11-18','Tarefas pendentes',None,'2026-09-30T11:08:02.268-0300'),
  ('G0280-75','2026-11-30','Em andamento',None,'2026-09-30T11:29:49.398-0300'),
  ('EG0241-45','2026-11-30','Tarefas pendentes',None,'2026-09-21T14:45:40.371-0300'),
  ('EG0286-18','2026-12-03','Tarefas pendentes',None,'2026-06-17T17:38:36.976-0300'),
  ('EG0286-14','2026-12-09','Tarefas pendentes',None,'2026-09-30T11:08:32.515-0300'),
  ('EG0274-64','2026-12-16','Em andamento',None,'2026-10-07T15:10:38.615-0300'),
  ('EG0286-23','2026-12-22','Tarefas pendentes',None,'2026-10-07T15:14:52.336-0300'),
  ('EG0274-57','2026-12-28','Tarefas pendentes',None,'2026-10-07T15:12:37.179-0300'),
  ('EG0286-9','2026-12-30','Tarefas pendentes',None,'2026-09-30T11:08:11.622-0300'),
  ('EG0274-66','2026-12-30','Tarefas pendentes',None,'2026-10-07T15:12:55.017-0300'),
  ('EG0274-65','2026-12-30','Tarefas pendentes',None,'2026-10-07T15:12:50.939-0300'),
  ('EG0274-59','2026-12-30','Tarefas pendentes',None,'2026-10-07T15:12:39.174-0300'),
  ('EG0274-21','2026-12-30','Tarefas pendentes',None,'2026-10-07T15:10:59.297-0300'),
  ('EG0286-22','2026-12-31','Tarefas pendentes',None,'2026-10-07T16:39:37.820-0300'),
  ('EG0286-17','2026-12-31','Tarefas pendentes',None,'2026-10-07T15:14:36.171-0300'),
  ('EG0286-16','2026-12-31','Tarefas pendentes',None,'2026-10-07T15:14:39.402-0300'),
  ('EG0286-15','2026-12-31','Tarefas pendentes',None,'2026-10-07T15:14:41.891-0300'),
  ('EG0275-108','2026-12-31','Em andamento',None,'2026-05-05T09:21:58.639-0300'),
  ('EG0274-63','2026-12-31','Tarefas pendentes',None,'2026-10-07T15:12:47.131-0300'),
  ('EG0274-62','2026-12-31','Tarefas pendentes',None,'2026-10-07T15:12:42.729-0300'),
  ('EG0274-61','2026-12-31','Tarefas pendentes',None,'2026-10-07T15:10:17.792-0300'),
  ('EG0274-60','2026-12-31','Tarefas pendentes',None,'2026-10-07T15:11:13.308-0300'),
  ('EG0274-58','2026-12-31','Tarefas pendentes',None,'2026-10-07T15:10:03.315-0300'),
  ('EG0240-44','2026-12-31','Em andamento',None,'2026-05-05T09:21:36.085-0300'),
  ('EG0239-54','2026-12-31','Em andamento',None,'2026-05-11T16:20:36.026-0300')],
}

ok = True
for name in sorted(LIVE):
    disk = DISK.get(name, [])
    dmap = {}
    for it in disk:
        f = it['fields']
        dmap[it['key']] = (f.get('duedate'), f.get('status', {}).get('name'),
                           f.get('resolutiondate'), f.get('updated'))
    live_keys = [k for k, _, _, _, _ in LIVE[name]]
    diffs = []
    for k, du, st, rd, up in LIVE[name]:
        if k not in dmap:
            diffs.append('+%s (novo no Jira)' % k); continue
        ddu, dst, drd, dup = dmap[k]
        if du is not None and du != ddu: diffs.append('%s duedate %s->%s' % (k, ddu, du))
        if st is not None and st != dst: diffs.append('%s status %s->%s' % (k, dst, st))
        if rd is not None and rd != drd: diffs.append('%s resolvido %s->%s' % (k, drd, rd))
        if up is not None and up != dup: diffs.append('%s updated %s->%s' % (k, dup, up))
    for k in dmap:
        if k not in live_keys: diffs.append('-%s (saiu do conjunto)' % k)
    if diffs: ok = False
    print('%-20s disco=%2d  live=%2d  %s' % (name, len(disk), len(LIVE[name]),
          'IDENTICO' if not diffs else 'DIFERENCAS: ' + '; '.join(diffs)))
print('\nRESULTADO:', 'todos os conjuntos identicos' if ok else 'HA DIFERENCAS - regenerar DATASETS')
