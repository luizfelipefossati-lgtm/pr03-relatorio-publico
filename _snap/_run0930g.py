# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~08:30 UTC (2026-09-30 05:30 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada nesta sessao (apenas pr03-relatorio-publico).
#   HTML ao vivo obtido por staging do artifact id 'pr03-relatorio-indicadores-epics':
#   md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes -> IDENTICO ao _artifact_src.html.
#
# getVisibleJiraProjects ao vivo: total=21, isLast=true.
#   Comparacao ordem-insensivel (key,name,issueTypes+hierarchyLevel) md5
#   = d6a2527e62d01b629ae9fd827d2989e7 -> IDENTICA ao _projects_min.json.
#   (A API devolve os projetos ordenados por key; _projects_min.json preserva a ordem
#    original de gravacao. Somente a ordem difere; o conteudo e o mesmo.)
#   Tipos hierarchyLevel=1: ['Epic','Fluxo de trabalho'].
#
# Conferencia desta rodada:
#   (a) ETQ AND updated >= "2026-09-30 04:20"  -> count = 0 (sem insercoes/edicoes
#       desde a geracao anterior, carimbada em 04:29 BRT).
#   (b) counts ao vivo dos 6 conjuntos de 2026-09:
#       planned 17 | overdue 1 | lookahead 32 | sent 6 | resolved 4 | rework 3
#       -> identicos aos _snap/*.json gravados (exclui remocoes, que nao mexem em `updated`).
#
# Meses congelados (2026-07, 2026-08) nao reconsultados por design.
#
# Resultado: SEM DELTA. Nenhum _snap/*.json reescrito; nenhum comando git executado.
# index.html (151.801 bytes, md5 86a45d93483cb4b085042f0bd59b6578),
# snapshot-data.js (64.015 bytes, md5 97e3fdf2136255919e55c6998aed80b6)
# e README.md regerados apenas para o timestamp 2026-09-30T05:30:27-03:00.
#
# Render headless (Chromium/Playwright no sandbox, arquivo staged):
#   0 erros de console, 5 canvas, abas "Agosto 2026 / Setembro 2026 / Visao Acumulada" OK,
#   banner antes de </body>, resumo set/2026: OTD 12% (2 de 17), 15 pendentes,
#   1 acumulada, retrabalho 50% (3/6).
#
# Observacao: 30/09 e o ultimo dia do mes corrente. Na proxima virada (01/10) o gerador
# passa a congelar 2026-09; os 6 conjuntos de setembro ja estao completos em _snap/.
