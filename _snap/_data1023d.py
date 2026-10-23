# -*- coding: utf-8 -*-
"""Rodada 2026-10-23 16:31 UTC / 13:31 BRT (execucao agendada, autonoma).

Snapshot REGERADO com carimbo novo: 2026-10-23T13:31:57-03:00.

Chamadas dinamicas refeitas ao vivo (12 no total, conector MCP Atlassian,
cloud ead785de-33f3-4746-9bdb-a2a58cf5213b, todas na primeira tentativa,
hasNextPage falso em todas):

  getVisibleJiraProjects                 21 projetos
  planned_2026-10                        15
  overdue_2026-10                         0
  lookahead_2026-10                      33
  sent_2026-10                            6
  resolved_2026-10                        6
  rework_2026-10                          4
  planned_2026-05 .. planned_2026-09      7 / 1 / 8 / 3 / 5

ETQ confirmado ao vivo como issuetype in ("Epic","Fluxo de trabalho") a partir
dos issueTypes de hierarchyLevel 1 dos 21 projetos visiveis.

Conferencia contra os JSONs gravados em _snap/
----------------------------------------------
Mes corrente: comparacao CAMPO A CAMPO (key | project_key | duedate |
status_name | status_cat | resolutiondate | updated) dos 31 registros dos
cinco conjuntos com projecao completa. Zero divergencias.

  planned  : EG0240-4 EG0240-5 EG0240-43 EG0274-38 EG0274-43 EG0286-7
             EG0286-10 EG0286-11 EG0286-12 EG291-4 G0280-50 G0280-51
             G0280-53 G0280-54 G0280-55
  overdue  : (vazio)
  sent     : EG0240-5 EG0241-42 EG0274-38 EG0275-112 EG0286-7 EG291-4
  resolved : EG0239-28 EG0241-42 EG0274-38 EG0275-112 EG0286-7 EG291-4
  rework   : EG0240-5 EG0241-42 EG0274-38 EG0286-7

lookahead_2026-10 e os cinco planned acumulados foram consultados com projecao
reduzida (duedate) para nao estourar o limite de tokens da ferramenta, e
conferidos por conjunto de chaves: 33 / 7 / 1 / 8 / 3 / 5 chaves identicas as
gravadas. Zero divergencias.

getVisibleJiraProjects estourou o limite e veio como arquivo; campos minimos
extraidos dele e conferidos por MD5 canonico contra _projects_min.json:
cf7b59de6bf68fc6489470cf9018bd6e dos dois lados (jq -S -c 'sort_by(.key)').

MD5 canonicos (jq -S -c 'sort_by(.key)') dos JSONs em uso, recalculados nesta
rodada e batendo com a tabela publicada no README:

  planned_2026-10    beb20fe094f4f249b43b20e9becc072f
  overdue_2026-10    58e0494c51d30eb3494f7c9198986bb9
  lookahead_2026-10  a38b4d9c77584b034fe2d7c2d0e61cd9
  sent_2026-10       1f995242d71713c8c893953b6abdacb5
  resolved_2026-10   de830431136ac892018b47b0219897c3
  rework_2026-10     92ac5a1b9b202bf88b9a210c5e83dbcd
  planned_2026-05    7b561eb1414d581166c3ffb820fa6c81
  planned_2026-06    b483385522e7aba4bff7eaac7c70c70b
  planned_2026-07    89c430d7301c007c96e90c518882ae87
  planned_2026-08    4e49e617a3b2a5abc00c9a1b5f858fa6
  planned_2026-09    1b5fac7dd7a83479c00b2ef40f75e97c

Nenhum JSON precisou ser reescrito. Apenas index.html, snapshot-data.js e
README.md foram regerados.

  index.html        161380 bytes  md5 ae6d91b4fd3d7a8426520e20d6ee09dd
  snapshot-data.js   73594 bytes  md5 70050a602d3970fb3d1eef0f938145b8
  _artifact_src      87509 bytes  md5 6a2b6462a4efbec1890af4494a7f0b74 (inalterado)

Artifact ao vivo reconferido
----------------------------
O HTML do Live Artifact foi obtido por device_stage_files com artifact_ids e
comparado ao _artifact_src.html versionado: mesmos 87.509 bytes e mesmo MD5
6a2b6462a4efbec1890af4494a7f0b74. O layout publicado esta em dia com o
artifact. A pasta Documents\\Claude\\Artifacts segue inacessivel ao shell
(area protegida), sem ser bloqueio para a conferencia.

Verificacoes desta rodada
-------------------------
  - comentario, bloco de dados e banner unicos; banner como ultimo elemento do
    <body>; arquivo termina integro em </div></body></html>.
  - removidos os tres, o restante e byte a byte igual ao _artifact_src.html
    (diferenca de comprimento = 0).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    (window.__HISTORY__=) comecando exatamente em 95.519; o conteudo do bloco
    e igual ao snapshot-data.js publicado ao lado.
  - bloco executado em node: as 6 JQLs do mes corrente devolveram 15/0/33/6/6/4,
    as 5 JQLs planned da visao acumulada devolveram 7/1/8/3/5,
    getVisibleJiraProjects devolveu 21 e __HISTORY__ expos 2026-07..2026-09,
    sobrevivendo a uma atribuicao direta que tentava sobrescrever 2026-09 e
    aceitando normalmente uma chave nova (2026-04). Nenhum aviso de JQL sem
    correspondencia.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, displayName, projectTypeKey e atlassianAccountId; a
    unica ocorrencia de accountId e a palavra "accountIds" na linha de
    comentario do cabecalho do proprio bloco de dados.

Cadencia do agendamento (acompanhamento de _data1023b/c)
--------------------------------------------------------
A rodada anterior (_data1023c) gravou as 14:30 UTC; esta comecou as 16:28 UTC.
Novo intervalo de ~2h, repetindo o observado na rodada passada: a serie nao
esta saindo de hora em hora. O ponto de _data1023b/c continua valido e ganha
mais um caso: os dados saem identicos ha seis rodadas seguidas (_data1022i/j/k,
_data1023a, _data1023c e agora _data1023d). Espacar o agendamento (a cada 3-6h)
reduziria ~12 consultas Jira por disparo e um commit/push/deploy Vercel por
rodada sem mudanca de dado.

Nenhuma operacao git executada nesta sessao.
"""
