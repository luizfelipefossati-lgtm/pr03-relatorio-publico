# -*- coding: utf-8 -*-
"""Rodada 2026-10-22 19:31 UTC / 16:31 BRT (execucao agendada, autonoma).

As 7 chamadas dinamicas do artifact foram refeitas ao vivo contra o Jira
(cloud ead785de-33f3-4746-9bdb-a2a58cf5213b) pelo conector MCP Atlassian:
getVisibleJiraProjects + as 6 consultas JQL do mes corrente (out/2026).

planned=15 overdue=0 lookahead=33 sent=6 resolved=6 rework=4 | projects=21

Conferencia por MD5 canonico (jq -S -c 'sort_by(.key)') contra os JSONs ja
gravados em _snap/: os 7 conjuntos IDENTICOS aos da rodada _data1022b/_1022d.

  planned_2026-10    beb20fe094f4f249b43b20e9becc072f
  overdue_2026-10    58e0494c51d30eb3494f7c9198986bb9
  lookahead_2026-10  a38b4d9c77584b034fe2d7c2d0e61cd9
  sent_2026-10       1f995242d71713c8c893953b6abdacb5
  resolved_2026-10   de830431136ac892018b47b0219897c3
  rework_2026-10     92ac5a1b9b202bf88b9a210c5e83dbcd
  _projects_min      cf7b59de6bf68fc6489470cf9018bd6e

Nenhum JSON precisou ser reescrito; apenas index.html e snapshot-data.js foram
regerados com carimbo novo (2026-10-22T16:31:25-03:00).

Observacao operacional: as respostas de getVisibleJiraProjects e da consulta
`lookahead` estouraram o limite de tokens da ferramenta e foram processadas a
partir dos arquivos salvos pelo proprio conector, com extracao via jq dos campos
minimos. As outras 5 consultas vieram inline, na primeira tentativa, sem erro
HTTP e sem paginacao (hasNextPage falso em todas).
"""
