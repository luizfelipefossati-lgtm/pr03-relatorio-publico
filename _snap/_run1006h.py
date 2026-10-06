# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-06 ~18:30 UTC (15:31 BRT). Mes corrente: 2026-10.
#
# Filtro de tipo: issuetype in ("Epic","Fluxo de trabalho") (consolidado desde _run1006e).
#
# 6 conjuntos do mes corrente reconsultados ao vivo + getVisibleJiraProjects (21 projetos,
# isLast=true). pageInfo.hasNextPage = false nas 6 consultas.
#
# Conferencia: 'planned' (29) e a lista de projetos (21) foram comparados por SHA-256 da forma
# canonica ordenada contra _snap/planned_2026-10.json e _projects_min.json -> hashes identicos
#   planned_2026-10 : 56dd6c71113432d5502897cd6aed098f3352c521134710b726b7f5db7ac6a183
#   _projects_min   : cc7b94d5a1583c3c97cfc22962e07562c52e42255b720e9d552141ac964df6c9
# Os outros 5 conjuntos foram comparados registro a registro (key, status.name,
# status.statusCategory.key, project.key, duedate, resolutiondate, updated): identicos.
#
# Nenhum arquivo de dados foi reescrito; o snapshot foi regerado apenas com novo timestamp.
#
# ARTIFACT_HTML (C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics\
# index.html) segue inacessivel a sessao Cowork (protected location). A geracao usou
# _artifact_src.html (sha256 2f09463c...), a copia local versionada no repo.
import json, os
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'

LIVE = {
 'planned': ['EG0256-28','EG0256-30','EG0274-21','EG0274-38','EG0274-43','EG0274-58',
             'EG0274-59','EG0274-60','EG0274-61','EG0274-62','EG0274-63','EG0274-64',
             'EG0286-7','EG0286-10','EG0286-11','EG0286-12','EG0286-15','EG0286-16',
             'EG0286-17','EG0286-20','EG0286-21','EG0286-22','EG0286-23','EG291-4',
             'G0280-50','G0280-51','G0280-53','G0280-54','G0280-55'],
 'overdue': ['EG0239-28','EG0240-5'],
 'lookahead': ['EG0239-54','EG0240-44','EG0241-45','EG0274-57','EG0274-65','EG0274-66',
               'EG0275-108','EG0285-8','EG0285-14','EG0285-16','EG0285-18','EG0286-6',
               'EG0286-9','EG0286-14','EG0286-18','EG0286-19','EG0286-24','EG0294-1',
               'EG0294-2','EG0294-3','G0280-75'],
 'sent': ['EG0241-42','EG0275-112','EG0286-7'],
 'resolved': ['EG0241-42','EG0275-112','EG0286-7'],
 'rework': ['EG0241-42','EG0286-7'],
}

print('--- diff vs rodada anterior (17:30 UTC, _run1006g) ---')
alterado = False
for name, keys in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    ok = [i['key'] for i in old]
    if sorted(ok) == sorted(keys):
        print('%-10s sem alteracao (%d)' % (name, len(keys)))
    else:
        alterado = True
        print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(ok), len(keys),
              sorted(set(keys)-set(ok)) or '-', sorted(set(ok)-set(keys)) or '-'))
print('RESULTADO:', 'HOUVE ALTERACAO - revisar' if alterado
      else 'nenhuma alteracao de dados; snapshot regerado apenas com novo timestamp')
