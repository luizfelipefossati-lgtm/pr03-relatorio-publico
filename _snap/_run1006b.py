# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-06 ~12:30 UTC (09:30 BRT). Mes corrente: 2026-10.
# Os 6 conjuntos de out/2026 foram reconsultados ao vivo via MCP Atlassian.
# ETQ = issuetype in ("Epic","Fluxo de trabalho"); cloudId ead785de-...
# planned em 2 consultas (10-01..10-15 = 12, 10-16..10-31 = 17) -> 29.
# lookahead em 2 consultas (nov = 14, dez = 7) -> 21.
# getVisibleJiraProjects NAO reconsultado (chaves ja constam de _projects_min.json).
# Meses congelados (<= 2026-09) NAO sao reconsultados.
# SEM NOVIDADES vs _run1006a: os 6 conjuntos seguem identicos (29/2/21/3/3/2),
#   mesmas chaves e mesmos campos; nenhum JSON de _snap/ precisou ser reescrito.
# OBS: ARTIFACT_HTML (Documents\Claude\Artifacts\...) e local protegido e nao e
#      legivel desta sessao; usado o template versionado _artifact_src.html.
import json, os
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'
LIVE = {
 'planned': ["EG0256-28","EG0274-63","EG0274-59","EG0274-38","EG0286-7","EG0286-21","EG0286-20",
             "EG0286-17","EG0286-16","EG0286-15","EG0286-11","EG291-4","EG0256-30","EG0274-64",
             "EG0274-62","EG0274-61","EG0274-60","EG0274-21","EG0274-58","EG0274-43","G0280-54",
             "G0280-55","G0280-53","G0280-51","G0280-50","EG0286-12","EG0286-23","EG0286-22","EG0286-10"],
 'overdue': ["EG0239-28","EG0240-5"],
 'lookahead': ["EG0286-19","EG0285-16","EG0285-8","EG0285-18","EG0285-14","EG0294-3","EG0294-2",
               "EG0294-1","EG0286-6","EG0274-66","EG0274-65","G0280-75","EG0274-57","EG0241-45",
               "EG0286-18","EG0286-14","EG0286-24","EG0286-9","EG0275-108","EG0240-44","EG0239-54"],
 'sent': ["EG0286-7","EG0275-112","EG0241-42"],
 'resolved': ["EG0286-7","EG0275-112","EG0241-42"],
 'rework': ["EG0286-7","EG0241-42"],
}
print('--- diff vs rodada anterior ---')
for name, keys in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    cur = [i['key'] for i in json.load(open(p, encoding='utf-8'))]
    if set(cur) == set(keys):
        print('%-10s sem alteracao (%d)' % (name, len(cur)))
    else:
        print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(cur), len(keys),
              sorted(set(keys)-set(cur)) or '-', sorted(set(cur)-set(keys)) or '-'))
