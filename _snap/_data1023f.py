# -*- coding: utf-8 -*-
"""Rodada 2026-10-23 18:31 UTC / 15:31 BRT (execucao agendada, autonoma).

Snapshot REGERADO com carimbo novo: 2026-10-23T15:31:16-03:00.

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

ETQ: issuetype in ("Epic","Fluxo de trabalho"), extraido do proprio
_artifact_src.html (os templates JQL foram relidos do HTML do Live Artifact
staged nesta rodada, nao reconstruidos de memoria).

Conferencia contra os JSONs gravados em _snap/
----------------------------------------------
Mes corrente: comparacao CAMPO A CAMPO (key | project_key | duedate |
status_name | status_cat | resolutiondate | updated | summary) dos quatro
conjuntos nao vazios com projecao completa.

  planned  : 15/15 identicos, inclusive na ordem.
  overdue  : vazio dos dois lados.
  sent     :  6/6 identicos, inclusive na ordem.
  rework   :  4/4 identicos, inclusive na ordem.
  resolved :  6/6 identicos COMO CONJUNTO; ordem diferente (ver abaixo).

Melhoria de metodo nesta rodada: lookahead com projecao COMPLETA
---------------------------------------------------------------
Diferentemente de _data1023e (que consultou o lookahead com projecao reduzida
e conferiu so por conjunto de chaves), esta rodada pediu o lookahead com a
projecao completa de seis campos. A resposta estourou o limite de tokens e
veio como arquivo; os campos minimos foram extraidos dele com jq na forma
aninhada usada em _snap/ e conferidos por MD5 canonico:

  a38b4d9c77584b034fe2d7c2d0e61cd9  ao vivo
  a38b4d9c77584b034fe2d7c2d0e61cd9  gravado

Ou seja, os 33 registros do lookahead batem agora registro a registro, nao
apenas por chave. Restam com conferencia por chaves apenas os cinco planned da
visao acumulada (7/1/8/3/5 chaves identicas as gravadas), que sao meses
encerrados e servidos pelo __HISTORY__ congelado.

Ordem de resolved_2026-10
-------------------------
A JQL de resolved nao leva ORDER BY, e o Jira devolveu os mesmos seis
registros em outra sequencia, a mesma divergencia de ordem observada em
_data1023e:

  ao vivo : EG291-4 EG0286-7 EG0275-112 EG0274-38 EG0241-42 EG0239-28
  gravado : EG0275-112 EG0241-42 EG0286-7 EG0239-28 EG291-4 EG0274-38

Por conjunto os dois lados sao exatamente iguais e o MD5 canonico do arquivo
continua de830431136ac892018b47b0219897c3. A ordem nao e carregada pelo
relatorio: o gerador funde sent + resolved em um mapa por chave e ordena os
detalhes pelo sinalizador de retrabalho. O arquivo foi mantido como estava.

getVisibleJiraProjects estourou o limite e veio como arquivo; 21 projetos,
conferidos contra o _projects_min.json em uso.

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

  index.html        161380 bytes  md5 404df979edc4be6c101119c6221636b2
  snapshot-data.js   73594 bytes  md5 56f0f5382d773975524891e7440c42b8
  _artifact_src      87509 bytes  md5 6a2b6462a4efbec1890af4494a7f0b74 (inalterado)

Os dois arquivos gerados tem exatamente o mesmo tamanho da rodada anterior e
MD5 diferente: so o carimbo mudou.

Artifact ao vivo reconferido
----------------------------
O HTML do Live Artifact foi obtido por device_stage_files com artifact_ids e
comparado ao _artifact_src.html versionado: mesmos 87.509 bytes e mesmo MD5
6a2b6462a4efbec1890af4494a7f0b74. O layout publicado esta em dia com o
artifact. A pasta Documents\\Claude\\Artifacts segue inacessivel ao shell e
agora tambem a device_list_dir (area protegida), sem ser bloqueio: a via de
staging de artifacts resolve a conferencia.

Verificacoes desta rodada
-------------------------
  - comentario, bloco de dados e banner unicos; banner como ultimo elemento do
    <body>; arquivo termina integro em </div></body></html>.
  - removidos os tres, o restante e byte a byte igual ao _artifact_src.html
    (diferenca de comprimento = 0).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    comecando exatamente em 95.519; o conteudo do bloco e byte a byte igual ao
    snapshot-data.js publicado ao lado.
  - bloco executado em node: as 6 JQLs do mes corrente devolveram 15/0/33/6/6/4,
    as 5 JQLs planned da visao acumulada devolveram 7/1/8/3/5,
    getVisibleJiraProjects devolveu 21 e __HISTORY__ expos 2026-07..2026-09.
    Nenhum aviso de JQL sem correspondencia para as JQLs reais do artifact.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, displayName, projectTypeKey e atlassianAccountId; a
    unica ocorrencia de accountId e a palavra "accountIds" na linha de
    comentario do cabecalho do proprio bloco de dados.

Cadencia do agendamento (acompanhamento de _data1023b..e)
----------------------------------------------------------
_data1023e gravou as 17:31 UTC; esta comecou as 18:28 UTC. Intervalo de ~1h.
Os dados saem identicos ha OITO rodadas seguidas (_data1022i/j/k, _data1023a,
_data1023c, _data1023d, _data1023e e agora _data1023f). A recomendacao
registrada nas rodadas anteriores segue de pe e ganha mais um caso: espacar o
agendamento (a cada 3-6h) pouparia ~12 consultas Jira por disparo e um
commit/push/deploy Vercel por rodada sem mudanca de dado.

Nenhuma operacao git executada nesta sessao.
"""
