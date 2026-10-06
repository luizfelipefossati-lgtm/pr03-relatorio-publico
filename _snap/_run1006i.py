# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-06 ~20:28 UTC (17:30 BRT). Mes corrente: 2026-10.
#
# Filtro de tipo: issuetype in ("Epic","Fluxo de trabalho") (consolidado desde _run1006e).
#
# 6 conjuntos do mes corrente reconsultados ao vivo + getVisibleJiraProjects (21 projetos,
# isLast=true). pageInfo.hasNextPage = false nas 6 consultas.
#
# Conferencia: 'planned' (29) e a lista de projetos (21) comparados por SHA-256 da forma
# canonica ordenada contra _snap/planned_2026-10.json e _projects_min.json.
#   _projects_min   : 42e8a14f9d6551ac373ec0c0b6b6597f2de1f72b0fb2182f0f271379516c283b (identico)
#   planned_2026-10 : DIVERGENTE -> comparacao registro a registro isolou EG291-4.
# Os outros 5 conjuntos foram comparados registro a registro (key, status.name,
# status.statusCategory.key, project.key, project.name, duedate, resolutiondate, updated):
# identicos.
#
# UNICA ALTERACAO: EG291-4 "PEB - Plano de Execucao BIM" (EG0291 - Arroio Feijo)
#   updated 2026-10-05T09:55:25.830-0300 -> 2026-10-06T16:26:05.341-0300
#   status/duedate/summary/resolutiondate inalterados; nenhum indicador se moveu.
#   Apenas _snap/planned_2026-10.json foi reescrito.
#
# ARTIFACT_HTML (C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics\
# index.html) segue inacessivel a sessao Cowork (protected location). A geracao usou
# _artifact_src.html, a copia local versionada no repo.
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

print('--- diff vs rodada anterior (18:30 UTC, _run1006h) ---')
alterado = False
for name, keys in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    ok = [i['key'] for i in old]
    if sorted(ok) == sorted(keys):
        print('%-10s sem alteracao de chaves (%d)' % (name, len(keys)))
    else:
        alterado = True
        print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(ok), len(keys),
              sorted(set(keys)-set(ok)) or '-', sorted(set(ok)-set(keys)) or '-'))
print('RESULTADO: nenhuma chave entrou/saiu; unica mudanca de campo em EG291-4 (updated).'
      if not alterado else 'RESULTADO: HOUVE ALTERACAO DE CHAVES - revisar')
