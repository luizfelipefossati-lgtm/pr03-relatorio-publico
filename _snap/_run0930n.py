# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~16:28 UTC (13:29 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada (connectedFolders traz so pr03-relatorio-publico;
#   device_list_dir na pasta Artifacts falhou com "is not inside a folder connected to
#   Cowork on this device"). HTML obtido por staging do artifact id
#   'pr03-relatorio-indicadores-epics': md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes
#   -> IDENTICO ao _artifact_src.html.
#
# Sonda: ETQ AND updated >= "2026-09-30 12:25" -> 0 issues. SEM DELTA de edicao desde a
#   geracao anterior (carimbo 12:31:10).
#
# Conjuntos 2026-09, ao vivo x gravado -- contagens identicas:
#   planned   14 -> 14  chaves conferidas (EG0240-4, EG0240-5, EG0240-43, EG0241-42,
#                       EG0275-6, EG0275-112, EG0285-19, EG0286-10, G0280-50..55)
#   overdue    1 ->  1  EG0239-28
#   lookahead 32 -> 32  contagem via searchResultMode=count
#   sent       7 ->  7  EG0240-5, EG0240-43, EG0275-6, EG0286-7, EG0286-8, EG0286-30, G0280-52
#   resolved   4 ->  4  EG0240-43, EG0275-6, EG0286-8, EG0286-30
#   rework     3 ->  3  EG0240-5, EG0240-43, EG0286-7
#   Nenhum _snap/*.json reescrito.
#
# Visao acumulada, planned ao vivo x gravado (counts):
#   04: 15/15 ok | 05: 7/7 ok | 06: 1/1 ok | 07: 9/10 DIVERGE | 08: 3/4 DIVERGE | 09: 14/14 ok
#   Jul e ago: divergencia ESPERADA (meses congelados, has_full -> FROZEN).
#
# Projetos: nenhuma chave nova nos conjuntos consultados. getVisibleJiraProjects nao
#   reconsultado; _projects_min.json inalterado.
#
# Gerado: index.html 151.158 bytes md5 ccbb1e94da296f96dc6ab1ec846f97f8
#         snapshot-data.js 63.372 bytes md5 28ddffe10d6e359016bf5e507a3bdbb7
#         carimbo 2026-09-30T13:29:49-03:00
#   Mesmo tamanho da rodada 0930m; md5 difere apenas pelo carimbo.
#
# Render headless (Chromium/Playwright no sandbox, arquivo staged): 0 pageerrors,
#   0 erros/warnings de console, 5 canvas, unica requisicao externa cdn.jsdelivr.net,
#   banner como ultimo elemento do body com o carimbo 30/09/2026 13:29.
#     Agosto 2026     -> OTD 50% (2 de 4)
#     Setembro 2026   -> OTD 21% (3 de 14), 11 pendentes, 1 em atraso, retrabalho 43% (3/7)
#     Visao Acumulada -> OTD 53% (34 de 64), 30 pendentes, heatmap montado
#   IDENTICOS a rodada 0930m, como esperado numa rodada sem delta.
#
# Nenhum comando git executado (nem `git status` -- ver LICAO da rodada 0930m).
# .git/index.lock ausente no inicio desta rodada. Push a cargo de PR03-Auto-Push-GitHub.
#
# Virada de mes: 30/09 e o ultimo dia do mes corrente. Na proxima rodada apos 01/10 o
# gerador passa a congelar 2026-09; os 6 conjuntos de setembro ja estao completos.
