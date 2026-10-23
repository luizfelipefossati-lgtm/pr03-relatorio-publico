# -*- coding: utf-8 -*-
"""Rodada 2026-10-23 19:31 UTC / 16:31 BRT (execucao agendada, autonoma).

PRIMEIRA MUDANCA DE DADO EM NOVE RODADAS.

Snapshot regerado com carimbo 2026-10-23T16:31:04-03:00.

Chamadas dinamicas refeitas ao vivo (12 no total, conector MCP Atlassian,
cloud ead785de-33f3-4746-9bdb-a2a58cf5213b, todas na primeira tentativa,
hasNextPage falso em todas):

  getVisibleJiraProjects                 21 projetos
  planned_2026-10                        15   <-- MUDOU
  overdue_2026-10                         0
  lookahead_2026-10                      33
  sent_2026-10                            6
  resolved_2026-10                        6
  rework_2026-10                          4
  planned_2026-05 .. planned_2026-09      7 / 1 / 8 / 3 / 5

ETQ: issuetype in ("Epic","Fluxo de trabalho"), relido do _artifact_src.html
nesta rodada (tipos de hierarchyLevel==1 dos 21 projetos visiveis).

O QUE MUDOU
-----------
Duas epics do EG0240 - GOITA/ COMPESA tiveram o due date adiado hoje, por
volta das 16:10 BRT, cerca de 20 minutos antes desta geracao:

  EG0240-43  TOMO IV - PROJETO DE INSTRUMENTACAO
             duedate 2026-10-23 -> 2026-10-26
             updated 2026-10-15T14:50:41.722-0300 -> 2026-10-23T16:10:52.572-0300

  EG0240-4   TOMO V - PROJETO DE RECUPERACAO ESTRUTURAL (PRE)
             duedate 2026-10-23 -> 2026-10-26
             updated 2026-10-15T13:58:30.870-0300 -> 2026-10-23T16:10:22.646-0300

Ambas seguem em "Em Revisao" (indeterminate), sem resolutiondate. O conjunto
de 15 chaves nao mudou. A ordem de retorno dentro do bloco EG0240 mudou de
[43, 4, 5] para [43, 5, 4] porque as tres epics passaram a compartilhar o
mesmo duedate (2026-10-26) e o ORDER BY project, duedate deixa o desempate
livre. O arquivo gravado segue a ordem devolvida ao vivo.

Efeito no relatorio: as tres epics de EG0240 em outubro vencem agora no dia
26; na data desta geracao (23/10) nenhuma delas esta atrasada. Antes, 43 e 4
venciam no proprio dia 23.

_snap/planned_2026-10.json foi reescrito (backup em
planned_2026-10.json.bak-20261023). Nenhum outro JSON foi tocado.

  md5 canonico planned_2026-10  beb20fe094f4f249b43b20e9becc072f (antes)
                                3fe8384df0f1b8cd9245df2901c72ef6 (agora)

Conferencia dos demais conjuntos
--------------------------------
Mes corrente, comparacao CAMPO A CAMPO (key | project_key | duedate |
status_name | status_cat | resolutiondate | updated | summary):

  overdue  : vazio dos dois lados.
  sent     :  6/6 identicos, inclusive na ordem.
  rework   :  4/4 identicos, inclusive na ordem.
  resolved :  6/6 identicos COMO CONJUNTO; ordem diferente, como em
              _data1023e/f (JQL sem ORDER BY). Arquivo mantido.
  lookahead: projecao completa; resposta estourou o limite e veio como
             arquivo; extraida com jq e conferida por MD5 canonico
             a38b4d9c77584b034fe2d7c2d0e61cd9 dos dois lados.

Melhoria de metodo nesta rodada: visao acumulada com projecao COMPLETA
---------------------------------------------------------------------
Diferentemente das rodadas anteriores, as cinco planned da visao acumulada
foram pedidas com a projecao completa de seis campos. Os 24 registros
(7 + 1 + 8 + 3 + 5) foram conferidos CAMPO A CAMPO contra os JSONs gravados,
e nao apenas por conjunto de chaves: todos identicos, inclusive na ordem.
Com isso, nesta rodada, TODOS os onze conjuntos tiveram conferencia campo a
campo, nao restando nenhum conferido apenas por chave.

MD5 canonicos (jq -S -c 'sort_by(.key)') dos JSONs em uso:

  planned_2026-10    3fe8384df0f1b8cd9245df2901c72ef6  (novo)
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

getVisibleJiraProjects estourou o limite e veio como arquivo; 21 projetos,
MD5 canonico identico ao _projects_min.json em uso.

Arquivos gerados
----------------
  index.html        161380 bytes  md5 ad940a3f454333c0cb41aa14299d9c5a
  snapshot-data.js   73594 bytes  md5 1fe7504f3bf46643577a27e9771086ab
  _artifact_src      87509 bytes  md5 6a2b6462a4efbec1890af4494a7f0b74 (inalterado)

Mesmo tamanho da rodada anterior: as duas datas trocadas tem o mesmo numero
de caracteres, assim como os carimbos.

Artifact ao vivo reconferido
----------------------------
HTML do Live Artifact obtido por device_stage_files com artifact_ids e
comparado ao _artifact_src.html versionado: mesmos 87.509 bytes e mesmo MD5
6a2b6462a4efbec1890af4494a7f0b74. Documents\\Claude\\Artifacts segue como
area protegida, inacessivel ao shell e a device_list_dir; a via de staging
resolve a conferencia.

Verificacoes desta rodada
-------------------------
  - comentario, bloco de dados e banner unicos; banner como ultimo elemento
    do <body>; arquivo termina integro em </div></body></html>.
  - removidos os tres, o restante e byte a byte igual ao _artifact_src.html
    (diferenca de comprimento = 0).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    comecando exatamente em 95.519; conteudo do bloco byte a byte igual ao
    snapshot-data.js publicado ao lado.
  - bloco executado em node (assinatura real callMcpTool(TJ, params), com
    TJ = mcp__6387c33d-...__searchJiraIssuesUsingJql): as 6 JQLs do mes
    corrente devolveram 15/0/33/6/6/4, as 5 planned da visao acumulada
    devolveram 7/1/8/3/5, getVisibleJiraProjects devolveu 21 e __HISTORY__
    expos 2026-07..2026-09. Nenhum aviso de JQL sem correspondencia.
  - planned_2026-10 servido pelo bloco traz EG0240-43, EG0240-5 e EG0240-4
    todos com duedate 2026-10-26: a alteracao do Jira chegou a pagina.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, displayName, projectTypeKey e atlassianAccountId;
    a unica ocorrencia de accountId e a palavra "accountIds" na linha de
    comentario do cabecalho do proprio bloco de dados.

Cadencia do agendamento
-----------------------
_data1023f gravou as 18:31 UTC; esta comecou as 19:27 UTC. Intervalo de ~1h.
A recomendacao das rodadas anteriores (espacar para 3-6h) continua valendo em
termos de custo, mas esta rodada mostra o outro lado: a mudanca de due date
entrou no Jira as 16:10 BRT e chegou a pagina publicada 20 minutos depois.
Com cadencia de 6h, a pagina teria ficado desatualizada por ate meio dia. A
escolha e do usuario; o registro fica.

Nenhuma operacao git executada nesta sessao.
"""
