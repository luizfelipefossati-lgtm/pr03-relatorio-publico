# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~15:27 UTC (12:31 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Artifact: pasta Artifacts NAO montada (connectedFolders traz so pr03-relatorio-publico;
#   device_list_dir na pasta Artifacts falhou com "is not inside a folder connected to
#   Cowork on this device"). HTML obtido por staging do artifact id
#   'pr03-relatorio-indicadores-epics': md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes
#   -> IDENTICO ao _artifact_src.html.
#
# Sonda: ETQ AND updated >= "2026-09-30 11:20" -> 10 issues. COM DELTA (de conteudo, nao de
#   tamanho). Oito delas (11:23-11:29) ja estavam no snapshot anterior (carimbo 11:31:49).
#
# Conjuntos 2026-09, ao vivo x gravado (contagens identicas, conferidas chave a chave):
#   planned   14 -> 14  REESCRITO (conteudo). EG0285-19 "Em andamento" -> "Em Revisao"
#                       (11:46:18). Categoria segue indeterminate; sem efeito no OTD.
#   lookahead 32 -> 32  REESCRITO (conteudo). EG0285-8 REABERTO as 11:46:00:
#                       "Enviado- Aguardando Analise"/done + resolucao 2026-08-11
#                       -> "Em Revisao"/indeterminate + resolutiondate null.
#   overdue    1 ->  1  inalterado (EG0239-28).
#   sent       7 ->  7  inalterado; chaves conferidas (EG0240-5, EG0240-43, EG0275-6,
#                       EG0286-7, EG0286-8, EG0286-30, G0280-52).
#   resolved   4 ->  4  inalterado (EG0240-43, EG0275-6, EG0286-8, EG0286-30).
#   rework     3 ->  3  inalterado (EG0240-5, EG0240-43, EG0286-7).
#
# Visao acumulada, planned ao vivo x gravado:
#   04: 15/15 ok | 05: 7/7 ok | 06: 1/1 ok | 07: 9/10 DIVERGE | 08: 3/4 DIVERGE | 09: 14/14 ok
#   Jul e ago: divergencia ESPERADA (meses congelados, has_full -> FROZEN).
#   planned_2026-05 REESCRITO (conteudo): G0280-45..49 (EBE 1S-5S) passaram de
#   "Enviado - Aguardando Analise" para "Medido e Faturado" as 11:24. Ambos os status sao
#   statusCategory=done -> sem efeito no OTD acumulado. Esse conjunto nao era regravado
#   desde 28/08 e estava com o rotulo antigo.
#
# Nota: G0280-52 foi resolvido as 11:23 de 30/09 e entra em sent_2026-09, mas NAO em
#   resolved_2026-09: a query do artifact usa resolved<="2026-09-30", que o Jira le como
#   meia-noite do dia 30. Comportamento do artifact ao vivo, preservado.
#
# Projetos: chaves dos conjuntos regravados (EG0285, G0280) ja presentes em
#   _projects_min.json; nenhum projeto novo. getVisibleJiraProjects nao reconsultado
#   (nenhum epic de projeto novo apareceu na sonda).
#
# Gerado: index.html 151.158 bytes md5 2d16e4799feddf8827840f8561f786c9
#         snapshot-data.js 63.372 bytes md5 1643bc9961176c8b670f45c61ec9e2c6
#         carimbo 2026-09-30T12:31:10-03:00
#
# Render headless (Chromium/Playwright no sandbox, arquivo staged): 0 pageerrors,
#   0 erros/warnings de console, 5 canvas, unica requisicao externa cdn.jsdelivr.net,
#   banner como ultimo elemento do body.
#     Agosto 2026     -> OTD 50% (2 de 4), retrabalho 50%
#     Setembro 2026   -> OTD 21% (3 de 14), 11 pendentes, 1 em atraso, retrabalho 43% (3/7)
#     Visao Acumulada -> OTD 53% (34 de 64), 30 pendentes, heatmap montado
#   IDENTICOS a rodada 0930l: as tres alteracoes foram de rotulo dentro da mesma categoria
#   de status ou em epic fora da janela de apuracao do mes.
#
# INCIDENTE (resolvido): um `git status` de diagnostico deixou .git/index.lock orfao
#   (rm nao e permitido no mount). Movido para _to_delete/index.lock.stale-20260930-1233,
#   liberando a tarefa PR03-Auto-Push-GitHub. Mesmo problema da rodada das 09:33
#   (_to_delete/index.lock.stale-20260930-0933).
#   LICAO: NAO rodar `git status` aqui. O prompt ja restringe git a `read-tree HEAD`;
#   para inspecionar o working tree use ls/md5sum.
#
# Nenhum commit ou push executado. Push a cargo da tarefa PR03-Auto-Push-GitHub.
#
# Virada de mes: 30/09 e o ultimo dia do mes corrente. Na proxima rodada apos 01/10 o
# gerador passa a congelar 2026-09; os 6 conjuntos de setembro ja estao completos.
