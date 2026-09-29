# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-29 ~23:30 UTC (20:30 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada nesta sessao (apenas pr03-relatorio-publico).
#   HTML ao vivo obtido por staging do artifact id 'pr03-relatorio-indicadores-epics':
#   md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes -> IDENTICO ao _artifact_src.html
#   do repo. Artifact updatedAt 2026-07-27, sem alteracao.
#
# getVisibleJiraProjects ao vivo: total=21, isLast=true.
#   *** DELTA: projeto NOVO 'EG0294 - ARTLOT - Topografia' (key EG0294, id 10630). ***
#   _projects_min.json atualizado de 20 -> 21 projetos (backup em _projects_min.json.bak).
#   issueTypes do EG0294: Fluxo de trabalho (h1), Tarefa (h0), Subtarefa (h-1).
#   => epicTypeNames permanece ['Epic','Fluxo de trabalho']; ETQ e todos os JQL inalterados.
#   EG0294 tem 3 epics/fluxos, TODOS sem duedate -> nenhum conjunto de dados afetado.
#
# Conjuntos 2026-09 reconsultados ao vivo e conferidos registro a registro:
#   planned    17 identicos
#   overdue     1 identico  (EG0239-28)
#   sent        6 identicos
#   resolved    4 identicos
#   rework      3 identicos
#   lookahead  32 identicos, conferido por contagem (32, via searchResultMode=count)
#              + verificacao de que nenhuma issue da faixa 2026-10-01..2026-11-30 teve
#              'updated' >= 2026-09-28 12:00 (count=0), o que exclui insercoes,
#              remocoes e edicoes desde a captura dos JSONs em 2026-09-28 13:31.
#
# Meses congelados (2026-04..2026-08) nao sao reconsultados por design.
# Resultado: DELTA apenas na lista de projetos. Nenhum _snap/*.json reescrito;
# index.html/snapshot-data.js/README regerados (novo projeto + timestamp).
