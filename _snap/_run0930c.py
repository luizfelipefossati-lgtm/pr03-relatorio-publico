# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~02:30 UTC (2026-09-29 23:30 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada nesta sessao (apenas pr03-relatorio-publico).
#   HTML ao vivo obtido por staging do artifact id 'pr03-relatorio-indicadores-epics':
#   md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes -> IDENTICO ao _artifact_src.html
#   do repo. Artifact updatedAt 2026-07-27, sem alteracao.
#
# getVisibleJiraProjects ao vivo: total=21, isLast=true.
#   Conjunto (key,name) identico ao _projects_min.json (21 projetos). Sem delta.
#
# Conjuntos 2026-09 reconsultados ao vivo e conferidos registro a registro
# (key, summary, status, statusCategory, project, duedate, resolutiondate, updated):
#   planned    17 identicos
#   overdue     1 identico  (EG0239-28)
#   sent        6 identicos
#   resolved    4 identicos
#   rework      3 identicos
#   lookahead  32 identicos, conferido por contagem (32, searchResultMode=count)
#              + count de 2026-10-01..2026-11-30 com updated>="2026-09-28 12:00" = 0,
#              o que exclui insercoes, remocoes e edicoes desde a captura dos JSONs.
#
# Verificacao global adicional: ETQ AND updated>="2026-09-30 01:30" -> count=0,
#   ou seja, nenhum epic/fluxo foi tocado desde a rodada anterior (_run0930b).
#
# Meses congelados (2026-04..2026-08) nao sao reconsultados por design.
# Resultado: SEM DELTA. Nenhum _snap/*.json reescrito; nenhum git executado.
# index.html/snapshot-data.js/README regerados apenas para atualizar o timestamp.
