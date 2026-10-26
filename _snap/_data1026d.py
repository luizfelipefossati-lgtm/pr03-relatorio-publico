# -*- coding: utf-8 -*-
"""Rodada 2026-10-26 17:32 UTC / 2026-10-26 14:32 BRT (execucao agendada, autonoma).

NENHUMA MUDANCA DE DADO. Snapshot regerado com carimbo 2026-10-26T14:32:33-03:00.

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

ETQ: issuetype in ("Epic","Fluxo de trabalho"), confirmado ao vivo a partir dos
tipos de nivel 1 dos 21 projetos visiveis.

INTERVALO DESDE A RODADA ANTERIOR
---------------------------------
_data1026c gravou as 16:33 UTC (13:33 BRT); esta gravou as 17:32 UTC de 26/10 -
cerca de 59 min depois, cadencia normal da tarefa agendada.

O QUE MUDOU
-----------
Nada. Os onze conjuntos e a lista de projetos voltaram identicos aos gravados
em _snap/, tanto por MD5 canonico (jq -S -c 'sort_by(.key)') quanto na ORDEM DE
RETORNO (jq -c '[.[].key]'), inclusive sent/resolved/rework, consultados sem
ORDER BY.

As tres epics do EG0240 - GOITA/ COMPESA (EG0240-43, EG0240-5 e EG0240-4)
seguem com duedate 2026-10-26, em "Em Revisao" (indeterminate), sem
resolutiondate. Como a geracao e de 26/10, nenhuma conta como atrasada e
overdue_2026-10 segue vazio.

Nenhum JSON de _snap/ foi reescrito.

Execucao
--------
As doze chamadas foram feitas por DOIS SUBAGENTES em paralelo, para nao estourar
o contexto da sessao principal:
  - subagente 1: os seis conjuntos de out/2026
  - subagente 2: as cinco planned de mai..set/2026 e getVisibleJiraProjects
Os dois gravaram os JSONs minimos na area de trabalho da sessao, FORA da arvore
do repositorio (nada tocou o repositorio antes da conferencia), com
fields=["summary","status","project","duedate","resolutiondate","updated"]
e projecao ANINHADA identica a de _snap/.

Tabela de MD5 canonico (convencao jq -S -c 'sort_by(.key)', comparavel entre
rodadas): os doze valores sao identicos aos de _data1026c.

  planned_2026-10    3fe8384df0f1b8cd9245df2901c72ef6
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
  _projects_min      cf7b59de6bf68fc6489470cf9018bd6e

Arquivos gerados
----------------
  index.html        161380 bytes  md5 9cc2d3223298b1d5c760750ff4cf2d03
  snapshot-data.js   73594 bytes  md5 22e797ce9f62c98ac849f713baa71938
  _artifact_src      87509 bytes  md5 6a2b6462a4efbec1890af4494a7f0b74 (inalterado)

Mesmos tamanhos da rodada anterior: so os carimbos mudaram, e tem o mesmo
numero de caracteres.

Artifact ao vivo reconferido
----------------------------
HTML do Live Artifact obtido por device_stage_files com artifact_ids: 87.509
bytes, md5 6a2b6462a4efbec1890af4494a7f0b74, identico ao _artifact_src.html
versionado. Documents\\Claude\\Artifacts segue inacessivel ao shell e a
device_list_dir (Permission denied, area protegida); a via de staging resolve
a conferencia.

Verificacoes desta rodada
-------------------------
  - comentario, bloco de dados e banner unicos; banner como ultimo elemento
    do <body>; arquivo termina integro em </div></body></html>.
  - removidos os tres, o restante e byte a byte igual ao _artifact_src.html
    (igualdade True, diferenca de comprimento 0).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    comecando exatamente em 95.519; conteudo byte a byte igual ao
    snapshot-data.js publicado ao lado.
  - bloco executado em node: as 6 JQLs do mes corrente devolveram
    15/0/33/6/6/4, as 5 planned da visao acumulada devolveram 7/1/8/3/5,
    getVisibleJiraProjects devolveu 21 e __HISTORY__ expos 2026-07..2026-09.
    Nenhum aviso de JQL sem correspondencia. epicTypeNames no bloco:
    ["Epic","Fluxo de trabalho"].
  - merge defensivo do __HISTORY__ testado: apos window.__HISTORY__ = {...}
    com uma chave 2026-09 falsa e uma chave nova 2026-11, os meses congelados
    seguiram intactos e a chave nova foi aceita.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, displayName, projectTypeKey, atlassianAccountId e
    'self":'. A unica ocorrencia de accountId e a palavra "accountIds" na
    linha 287, comentario do cabecalho do proprio bloco de dados. A varredura
    por regex de e-mail nao acusou nenhuma correspondencia.

Observacao de dados (ja conhecida, sem acao)
--------------------------------------------
EG0239-28 esta em "Enviado - Aguardando Analise1" (com "1" ao final), status
distinto do consultado por sent_2026-10; por isso aparece em resolved_2026-10 e
nao em sent_2026-10. Variacoes de grafia semelhantes existem em outros projetos
("Enviado- Aguardando Analise", sem espaco, em EG0285-19).

Nenhuma operacao git executada nesta sessao.
"""
