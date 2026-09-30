# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~11:28 UTC (2026-09-30 08:30 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada nesta sessao (connectedFolders traz apenas
#   pr03-relatorio-publico; device_list_dir na pasta Artifacts falhou com
#   "is not inside a folder connected to Cowork on this device").
#   HTML ao vivo obtido por staging do artifact id 'pr03-relatorio-indicadores-epics':
#   md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes -> IDENTICO ao _artifact_src.html.
#
# getVisibleJiraProjects ao vivo: total=21, isLast=true.
#   Assinatura ordem-insensivel [(key,name,issueTypes(name,hierarchyLevel) ordenados)]
#   md5 = d70a089236b256be76db16acc7746931 -> IDENTICA ao _projects_min.json.
#   Tipos hierarchyLevel=1: ['Epic','Fluxo de trabalho'].
#
# Conferencia desta rodada:
#   (a) ETQ AND updated >= "2026-09-30 07:20"  -> count = 0 (sem insercoes/edicoes
#       desde a geracao anterior, carimbada em 07:31 BRT).
#   (b) counts ao vivo dos 6 conjuntos de 2026-09:
#       planned 17 | overdue 1 | lookahead 32 | sent 6 | resolved 4 | rework 3
#       -> identicos aos _snap/*.json gravados (a contagem cobre remocoes, que nao
#          mexem em `updated`).
#   (c) planned e overdue conferidos chave a chave (17 e 1 chaves), conjuntos iguais.
#
# Meses congelados (2026-07, 2026-08) nao reconsultados por design.
#
# Resultado: SEM DELTA. Nenhum _snap/*.json reescrito; nenhum comando git executado.
# index.html (151.801 bytes, md5 3a6f0fcc615b40c388487161fbc1ded2),
# snapshot-data.js (64.015 bytes, md5 930abbfd94240bbefadabe03a0282413)
# e README.md regerados apenas para o timestamp 2026-09-30T08:30:07-03:00.
#
# Render headless (Chromium/Playwright no sandbox, arquivo staged):
#   0 erros de console, 0 pageerrors, 5 canvas, unica requisicao externa cdn.jsdelivr.net,
#   banner como ultimo elemento antes de </body>.
#   Abas conferidas por clique:
#     Agosto 2026      -> OTD 50% (2 de 4), 2 pendentes
#     Setembro 2026    -> OTD 12% (2 de 17), 15 pendentes
#     Visao Acumulada  -> OTD 49% (33 de 67), 34 pendentes, heatmap OTD projeto x mes montado
#
# Observacao: 30/09 e o ultimo dia do mes corrente. Na proxima rodada apos a virada
# (01/10) o gerador passa a congelar 2026-09; os 6 conjuntos de setembro ja estao
# completos em _snap/.
