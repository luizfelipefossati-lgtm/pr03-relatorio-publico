# -*- coding: utf-8 -*-
"""Rodada 2026-10-23 12:24 UTC / 09:27 BRT (execucao agendada, autonoma).

As 7 chamadas dinamicas do artifact foram refeitas ao vivo contra o Jira
(cloud ead785de-33f3-4746-9bdb-a2a58cf5213b) pelo conector MCP Atlassian:
getVisibleJiraProjects + as 6 consultas JQL do mes corrente (out/2026). Alem
delas, as 5 consultas `planned` da visao acumulada (mai a set/2026) tambem
foram reconsultadas ao vivo - 12 chamadas no total, todas na primeira
tentativa, sem paginacao (hasNextPage falso em todas). ETQ confirmado ao vivo
como issuetype in ("Epic","Fluxo de trabalho") a partir dos issueTypes de
hierarchyLevel 1 dos 21 projetos visiveis; projecao minima de campos
(summary, status, project, duedate, resolutiondate, updated).

planned=15 overdue=0 lookahead=33 sent=6 resolved=6 rework=4 | projects=21
planned acumulado: 2026-05=7 2026-06=1 2026-07=8 2026-08=3 2026-09=5

Conferencia contra os JSONs ja gravados em _snap/: os 12 conjuntos sairam
IDENTICOS aos das rodadas _data1022i / _data1022j / _data1022k.

  - getVisibleJiraProjects estourou o limite de tokens da ferramenta e veio
    como arquivo; campos minimos extraidos do arquivo.
  - lookahead_2026-10 foi consultado com projecao reduzida (duedate) para nao
    estourar o limite; conferido por comparacao do conjunto de chaves (33
    chaves identicas), nao por MD5 de registro completo.
  - conferencia por MD5 canonico (ordenacao por .key + chaves ordenadas),
    que neutraliza diferencas de ordem de retorno do Jira:
        _projects_min      505192b9c2912c176357e055e44f085a
        planned_2026-10    6e647aa5b49e5a5ffbdb9a6d01ee248f
        overdue_2026-10    d751713988987e9331980363e24189ce (vazio)
        sent_2026-10       6e09d9b97ce39b02e08476277592df10
        resolved_2026-10   891d3e1f95bc3e11ab19d063c0687deb
        rework_2026-10     d0024c38510614f87769c0c7bac80cdb
    Os MD5 no formato historico do README (jq -S -c 'sort_by(.key)') tambem
    foram recalculados e batem com a tabela publicada:
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
  - os 5 `planned` acumulados foram conferidos por conjunto de chaves contra
    os JSONs gravados: zero divergencias.

Nenhum JSON precisou ser reescrito; apenas index.html e snapshot-data.js foram
regerados com carimbo novo (2026-10-23T09:27:38-03:00).

  index.html        161380 bytes  md5 ed1ecc3434eaa60b5ad6683bcef32990
  snapshot-data.js   73594 bytes  md5 433d4bfe50a736c9357b1ac3040c97ee
  _artifact_src      87509 bytes  md5 6a2b6462a4efbec1890af4494a7f0b74 (inalterado)

NOVIDADE DESTA RODADA: o HTML do Live Artifact foi obtido pela via oficial de
staging de artifacts (device_stage_files com artifact_ids) e comparado ao
_artifact_src.html versionado - mesmos 87.509 bytes e mesmo MD5. E a primeira
rodada desde a serie de outubro em que a ressalva "artifact nao reconferido"
pode ser levantada: o layout publicado esta em dia com o artifact ao vivo.
A pasta Documents\\Claude\\Artifacts continua inacessivel ao shell (area
protegida), mas isso deixou de ser bloqueio para a conferencia.

Verificacoes desta rodada:
  - comentario, bloco de dados e banner unicos; banner como ultimo elemento do
    <body>; removidos os tres, o restante e byte a byte igual ao
    _artifact_src.html (diff de comprimento = 0).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    (window.__HISTORY__=) comecando exatamente em 95.519; o conteudo do bloco
    e igual ao snapshot-data.js publicado ao lado.
  - bloco executado em node v22.23.4: as 6 JQLs do mes corrente devolveram
    15/0/33/6/6/4, as 5 JQLs `planned` da visao acumulada devolveram 7/1/8/3/5,
    getVisibleJiraProjects devolveu 21 e __HISTORY__ expos 2026-07..2026-09,
    sobrevivendo intacto a uma atribuicao direta que tentava sobrescrever
    2026-09. Nenhum aviso de JQL sem correspondencia.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, projectTypeKey, atlassianAccountId e "self"; a unica
    ocorrencia de accountId e a palavra "accountIds" na linha de comentario do
    cabecalho do proprio bloco de dados (linha 287).

Nenhuma operacao git foi executada nesta sessao; commit e push ficam a cargo da
tarefa PR03-Auto-Push-GitHub do Windows Task Scheduler.
"""
