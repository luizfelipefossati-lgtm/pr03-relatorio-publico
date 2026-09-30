# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~03:30 UTC (2026-09-30 00:30 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada nesta sessao (apenas pr03-relatorio-publico).
#   HTML ao vivo obtido por staging do artifact id 'pr03-relatorio-indicadores-epics':
#   md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes -> IDENTICO ao _artifact_src.html
#   do repo. Sem alteracao.
#
# getVisibleJiraProjects ao vivo: total=21, isLast=true.
#   Assinatura md5 (key,name,issueTypes+hierarchyLevel) = aca1bab21c39a6dafd8d8b0bfd212527
#   -> IDENTICA ao _projects_min.json. epicTypeNames = ['Epic','Fluxo de trabalho'].
#
# Estrategia de conferencia desta rodada (duas checagens que se complementam):
#   (a) ETQ AND updated >= "2026-09-29 23:30"  -> count = 0
#       Exclui insercoes e edicoes desde a conferencia da rodada anterior (_run0930c).
#   (b) count dos 6 conjuntos de 2026-09, ao vivo:
#       planned 17 | overdue 1 | lookahead 32 | sent 6 | resolved 4 | rework 3
#       -> identicos aos _snap/*.json gravados. Exclui remocoes (que nao mexem em updated).
#   (c) planned_2026-09 trazido por inteiro (17 registros, hasNextPage=false);
#       as 17 chaves conferem com o arquivo gravado.
#
# Meses congelados (2026-04..2026-08) nao sao reconsultados por design.
# FROZEN = [2026-07, 2026-08]; mes ao vivo = 2026-09.
#
# Resultado: SEM DELTA. Nenhum _snap/*.json reescrito; nenhum git executado.
# index.html (151.801 bytes, md5 9da3fffe940f07b6b5a86a1fe5b6db51),
# snapshot-data.js (64.015 bytes) e README.md regerados apenas para o timestamp.
# .git/index integro; nao foi preciso 'git read-tree HEAD'.
