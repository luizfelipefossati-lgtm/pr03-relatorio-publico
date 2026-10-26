# -*- coding: utf-8 -*-
"""Rodada 2026-10-26 14:35 UTC / 2026-10-26 11:35 BRT (execucao agendada, autonoma).

NENHUMA MUDANCA DE DADO. Snapshot regerado com carimbo 2026-10-26T11:35:12-03:00.

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

ETQ: issuetype in ("Epic","Fluxo de trabalho").

INTERVALO DESDE A RODADA ANTERIOR
---------------------------------
_data1026a gravou as 13:40 UTC de 26/10; esta gravou as 14:35 UTC do mesmo dia
- cerca de 55 min, cadencia normal da tarefa agendada. Nada a investigar.

O QUE MUDOU
-----------
Nada. Os onze conjuntos e a lista de projetos voltaram identicos aos gravados
em _snap/. As tres epics do EG0240 - GOITA/ COMPESA (EG0240-43, EG0240-5 e
EG0240-4) seguem com duedate 2026-10-26, em "Em Revisao" (indeterminate), sem
resolutiondate. Como a geracao e de 26/10, nenhuma conta como atrasada e
overdue_2026-10 segue vazio.

Nenhum JSON de _snap/ foi reescrito.

Execucao
--------
As doze chamadas foram feitas por DOIS SUBAGENTES em paralelo, para nao estourar
o contexto da sessao principal:
  - subagente 1: os seis conjuntos de out/2026 -> $HOME/snapshot_data/
  - subagente 2: as cinco planned de mai..set/2026 e getVisibleJiraProjects
    -> $HOME/snapshot_data2/
Os dois gravaram fora de mnt/ (nada tocou o repositorio antes da conferencia),
com fields=["summary","status","project","duedate","resolutiondate","updated"]
e projecao ANINHADA identica a de _snap/.

getVisibleJiraProjects (62.513 chars) e lookahead_2026-10 (60.761 chars)
estouraram o limite de tokens da ferramenta; as respostas foram salvas em
arquivo pela propria ferramenta e processadas a partir do arquivo, sem
redigitar conteudo truncado.

Conferencia
-----------
Os doze conjuntos foram comparados REGISTRO A REGISTRO contra _snap/ e
_projects_min.json por MD5 canonico em python (json.dumps sort_keys=True,
separators=(',',':'), ensure_ascii=False), em duas formas: preservando a ordem
de retorno e reordenando por key. Todos bateram nas duas formas, exceto
resolved_2026-10, que bateu apenas na forma reordenada (ver abaixo).

Tabela no README (convencao jq -S -c 'sort_by(.key)', comparavel entre
rodadas): os doze valores sao identicos aos de _data1026a.

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

Ordem de retorno
----------------
Dez conjuntos voltaram na MESMA ordem gravada. resolved_2026-10 voltou em ordem
diferente, como em todas as rodadas anteriores - e consultado sem ORDER BY:
  agora    EG291-4, EG0286-7, EG0275-112, EG0274-38, EG0241-42, EG0239-28
  gravado  EG0275-112, EG0241-42, EG0286-7, EG0239-28, EG291-4, EG0274-38
Conjunto e valores identicos; a ordem nao e carregada pelo relatorio (o gerador
funde sent+resolved num mapa por chave e ordena pelo sinalizador de
retrabalho). Arquivo mantido.

Arquivos gerados
----------------
  index.html        161380 bytes  md5 f8a8f0aa10a5c9713759dad0bcbcc5f0
  snapshot-data.js   73594 bytes  md5 7c23993de4400fc4634f5fa04c1c3dfc
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
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, displayName, projectTypeKey, atlassianAccountId e
    'self":'. A unica ocorrencia de accountId e a palavra "accountIds" na
    linha de comentario do cabecalho do proprio bloco de dados. Varredura por
    regex de e-mail: zero ocorrencias.

Nenhuma operacao git executada nesta sessao.
"""
