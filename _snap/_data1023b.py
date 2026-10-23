# -*- coding: utf-8 -*-
"""Rodada 2026-10-23 12:29 UTC / 09:29 BRT (execucao agendada, autonoma).

RODADA DE VERIFICACAO - NENHUM ARQUIVO REGERADO. Motivo abaixo.

Situacao encontrada
-------------------
Ao iniciar (disparo 12:28:58 UTC), o snapshot no working tree JA estava
recem-gerado e completo:

  index.html        161380 bytes  mtime 12:27 UTC  (carimbo 2026-10-23T09:27:38-03:00)
  snapshot-data.js   73594 bytes  mtime 12:27 UTC
  README.md                       mtime 12:29 UTC
  _snap/_data1023a.py             mtime 12:30 UTC  <- escrito DEPOIS deste disparo

Ou seja: a rodada anterior (disparo das 11:27 UTC / 08:27 BRT) ainda estava
terminando de gravar quando esta comecou. As duas execucoes se sobrepuseram.
A rodada _data1023a levou ~1h (08:27 -> 09:30 BRT), estourando o intervalo
horario do proprio agendamento (cron `27 * * * *`).

Conferencia independente contra o Jira ao vivo
----------------------------------------------
Em vez de refazer as 12 consultas e sobrescrever arquivos de uma sessao que
ainda escrevia, esta rodada reconsultou ao vivo os 5 conjuntos do mes corrente
(cloud ead785de-33f3-4746-9bdb-a2a58cf5213b, conector MCP Atlassian, projecao
minima `duedate`, ORDER BY key, hasNextPage falso em todas) e comparou o
conjunto de chaves com os JSONs publicados em _snap/:

  planned_2026-10   15  IDENTICO
  overdue_2026-10    0  IDENTICO (vazio)
  sent_2026-10       6  IDENTICO
  resolved_2026-10   6  IDENTICO
  rework_2026-10     4  IDENTICO

  planned : EG0240-4 EG0240-5 EG0240-43 EG0274-38 EG0274-43 EG0286-7
            EG0286-10 EG0286-11 EG0286-12 EG291-4 G0280-50 G0280-51
            G0280-53 G0280-54 G0280-55
  sent    : EG0240-5 EG0241-42 EG0274-38 EG0275-112 EG0286-7 EG291-4
  resolved: EG0239-28 EG0241-42 EG0274-38 EG0275-112 EG0286-7 EG291-4
  rework  : EG0240-5 EG0241-42 EG0274-38 EG0286-7

Zero divergencias. O snapshot publicado reflete o Jira ao vivo neste momento.

Integridade do arquivo publicado (conferida nesta rodada)
---------------------------------------------------------
  - bloco de dados do snapshot inline no index.html (161380 = 87509 do
    _artifact_src + 73594 do bloco), uma unica ocorrencia de __SNAPSHOT__;
  - banner amarelo presente como ULTIMO elemento antes de </body>, com o texto
    "Snapshot estatico - ultima atualizacao: 23/10/2026 09:27";
  - index.html termina em </body></html> integro (sem escrita truncada).

Decisao
-------
Nao regerar. Regerar produziria conteudo identico com carimbo novo, gerando um
commit/push/deploy Vercel sem mudanca de dado, e havia risco de intercalar
escrita com a sessao anterior ainda ativa. O working tree ja tem
index.html/snapshot-data.js/README.md modificados aguardando o
PR03-Auto-Push-GitHub.

Ponto de atencao para o usuario
-------------------------------
As rodadas passaram a durar ~1h contra um agendamento horario, entao estao se
sobrepondo e duplicando ~12 consultas Jira por hora para um conjunto de dados
que sai identico ha varias rodadas (_data1022i/j/k e _data1023a). Vale espacar
o agendamento (a cada 3-6h) ou enxugar a etapa de reconferencia acumulada.

Nenhuma operacao git executada nesta sessao.
