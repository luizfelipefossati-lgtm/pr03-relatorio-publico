# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~14:28 UTC (11:31 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada (connectedFolders traz so pr03-relatorio-publico;
#   device_request_folder_access negado: "A requested folder can't be granted to this session").
#   HTML obtido por staging do artifact id 'pr03-relatorio-indicadores-epics':
#   md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes -> IDENTICO ao _artifact_src.html.
#
# Sonda: ETQ AND updated >= "2026-09-30 10:20" -> 10 issues. COM DELTA.
#
# Conjuntos 2026-09, ao vivo x gravado:
#   planned   17 -> 14  REESCRITO. Sairam EG0286-6 (due 2026-11-18), EG0286-13 (2027-01-01)
#                       e EG0286-14 (2026-12-09): due date empurrado para fora de setembro.
#   sent       6 ->  7  REESCRITO. Entrou G0280-52 (transicao 30/09 11:23).
#   lookahead 32 -> 32  REESCRITO. Saiu EG0286-9; entrou EG0286-6 (2026-11-18);
#                       G0280-75 mudou de 2026-10-01 para 2026-11-30 (updated 11:29).
#                       Os outros 30 registros conferidos por duedate + ausencia de `updated`
#                       posterior a 10:20 -> preservados do arquivo anterior.
#   overdue    1 ->  1  inalterado (0 do conjunto com updated >= 10:20).
#   resolved   4 ->  4  inalterado (0 do conjunto com updated >= 10:20).
#   rework     3 ->  3  inalterado; chaves conferidas (EG0240-5, EG0240-43, EG0286-7).
#
# Projetos: chaves dos conjuntos regravados todas presentes em _projects_min.json (nenhum novo).
#
# Meses congelados 2026-07 e 2026-08 nao reconsultados (design FROZEN/has_full).
# Visao acumulada planned: 04=15 05=7 06=1 07=10(congelado) 08=4(congelado) 09=14.
#
# Gerado: index.html 151.253 bytes md5 0df13f8c7ba78a4a6803452a7f4d868f
#         snapshot-data.js 63.467 bytes md5 f7704df4de84165e5ca9f1778997d287
#         carimbo 2026-09-30T11:31:49-03:00
#
# Render headless (Chromium/Playwright, arquivo staged): 0 pageerrors, 0 erros/warnings de
#   console, 5 canvas, banner como ultimo elemento do body.
#   Agosto 2026     -> OTD 50% (2 de 4)       [igual a rodada anterior]
#   Setembro 2026   -> OTD 21% (3 de 14), 11 pendentes, 1 em atraso, retrabalho 43% (3/7)
#                      [antes: 12% (2 de 17), 15 pendentes, 50% (3/6)]
#   Visao Acumulada -> OTD 53% (34 de 64)     [antes: 49% (33 de 67)]
#
# Nenhum comando git executado. Push a cargo da tarefa PR03-Auto-Push-GitHub.
