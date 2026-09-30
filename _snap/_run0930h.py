# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~09:31 UTC (2026-09-30 06:31 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada nesta sessao (apenas pr03-relatorio-publico).
#   device_request_folder_access para a pasta Artifacts foi RECUSADO pelo host
#   ("A requested folder can't be granted to this session").
#   HTML ao vivo obtido por staging do artifact id 'pr03-relatorio-indicadores-epics':
#   md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes -> IDENTICO ao _artifact_src.html.
#
# getVisibleJiraProjects ao vivo: total=21, isLast=true.
#   Comparacao ordem-insensivel, agora com issueTypes TAMBEM ordenados dentro de cada
#   projeto: md5 = 9acfbae31b248a7099db00ade880a981 -> IDENTICA ao _projects_min.json.
#   (Sem normalizar a ordem dos issueTypes as assinaturas divergem — 3e2210d9... ao vivo
#    contra 980defcc... gravado — porque a API e o arquivo gravado listam os tipos em
#    ordens diferentes. O conteudo e o mesmo; so a ordem difere. Foi tambem conferida a
#    igualdade linha a linha de (key | name | issueTypes) dos 21 projetos.)
#   Tipos hierarchyLevel=1: ['Epic','Fluxo de trabalho'].
#
# Conferencia desta rodada:
#   (a) ETQ AND updated >= "2026-09-30 05:20"  -> count = 0 (sem insercoes/edicoes
#       desde a geracao anterior, carimbada em 05:30 BRT).
#   (b) counts ao vivo dos 6 conjuntos de 2026-09:
#       planned 17 | overdue 1 | lookahead 32 | sent 6 | resolved 4 | rework 3
#       -> identicos aos _snap/*.json gravados (exclui remocoes, que nao mexem em `updated`).
#
# Meses congelados (2026-07, 2026-08) nao reconsultados por design.
#
# Resultado: SEM DELTA. Nenhum _snap/*.json reescrito; nenhum comando git executado.
# index.html (151.801 bytes, md5 b5a9edcd5484f262a7d2a5afc7b429b4),
# snapshot-data.js (64.015 bytes, md5 971301009c0ac872af5ef89ee17b0231)
# e README.md regerados apenas para o timestamp 2026-09-30T06:31:19-03:00.
#
# Render headless (Chromium/Playwright no sandbox, arquivo staged):
#   0 erros de console, 0 warnings, 5 canvas, unica requisicao externa cdn.jsdelivr.net,
#   banner como ultimo elemento antes de </body>.
#   Abas conferidas por clique:
#     Agosto 2026      -> OTD 50% (2 de 4), 2 pendentes, 0 acumuladas, retrabalho 50% (3/6)
#     Setembro 2026    -> OTD 12% (2 de 17), 15 pendentes, 1 acumulada, retrabalho 50% (3/6)
#     Visao Acumulada  -> OTD 49% (33 de 67), heatmap OTD por projeto x mes montado
#
# Observacao: 30/09 e o ultimo dia do mes corrente. Na proxima virada (01/10) o gerador
# passa a congelar 2026-09; os 6 conjuntos de setembro ja estao completos em _snap/.
