# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~13:27 UTC (2026-09-30 10:29 BRT). Mes corrente 2026-09.
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
#   md5 = aca1bab21c39a6dafd8d8b0bfd212527 -> IDENTICA ao _projects_min.json.
#   Tipos hierarchyLevel=1: ['Epic','Fluxo de trabalho'].
#   (Resposta estourou o limite de tokens do MCP; assinatura extraida do arquivo salvo.)
#
# Conferencia desta rodada:
#   (a) ETQ AND updated >= "2026-09-30 09:20"  -> count = 0 (sem insercoes/edicoes
#       desde a geracao anterior, carimbada em 09:29 BRT).
#   (b) counts ao vivo dos 6 conjuntos de 2026-09:
#       planned 17 | overdue 1 | lookahead 32 | sent 6 | resolved 4 | rework 3
#       -> identicos aos _snap/*.json gravados (a contagem cobre remocoes, que nao
#          mexem em `updated`).
#   (c) planned e overdue conferidos chave a chave (17 e 1 chaves), conjuntos iguais.
#   (d) meses `planned` da visao acumulada, ao vivo x gravado:
#          04: 15/15 ok | 05: 7/7 ok | 06: 1/1 ok |
#          07: 9/10 DIVERGE | 08: 3/4 DIVERGE | 09: 17/17 ok
#       Divergencias de jul e ago ESPERADAS e nao corrigidas: meses congelados
#       (has_full -> FROZEN no _gen_snapshot.py), por design nao voltam a ser
#       consultados. Reescrever planned_2026-07/08.json quebraria o congelamento.
#       Mesmo resultado da rodada 0930j; documentado no README.
#
# Resultado: SEM DELTA. Nenhum _snap/*.json reescrito; nenhum comando git executado.
# index.html (151.801 bytes, md5 30e18336fc8f38dc64a22d9ed1b69271),
# snapshot-data.js (64.015 bytes, md5 24be656425314ef8ad9e199f206c53f7)
# e README.md regerados apenas para o timestamp 2026-09-30T10:29:34-03:00.
#
# Render headless (Chromium/Playwright no sandbox, arquivo staged):
#   0 pageerrors, 0 erros/warnings de console, 5 canvas, unica requisicao externa
#   cdn.jsdelivr.net, banner como ultimo elemento do body antes de </body>.
#   Abas conferidas por clique:
#     Agosto 2026      -> OTD 50% (2 de 4)
#     Setembro 2026    -> OTD 12% (2 de 17)
#     Visao Acumulada  -> OTD 49% (33 de 67), 34 pendentes, heatmap projeto x mes montado
#   Identicos a rodada 0930j.
#
# Observacao: 30/09 e o ultimo dia do mes corrente. Na proxima rodada apos a virada
# (01/10) o gerador passa a congelar 2026-09; os 6 conjuntos de setembro ja estao
# completos em _snap/.
