# -*- coding: utf-8 -*-
"""Rodada 2026-10-23 00:31 UTC / 2026-10-22 21:31 BRT (execucao agendada, autonoma).

As 7 chamadas dinamicas do artifact foram refeitas ao vivo contra o Jira
(cloud ead785de-33f3-4746-9bdb-a2a58cf5213b) pelo conector MCP Atlassian:
getVisibleJiraProjects + as 6 consultas JQL do mes corrente (out/2026). Alem
delas, as 5 consultas `planned` da visao acumulada (mai a set/2026) tambem
foram reconsultadas ao vivo nesta rodada. ETQ confirmado ao vivo como
issuetype in ("Epic","Fluxo de trabalho") a partir dos issueTypes de
hierarchyLevel 1 dos 21 projetos visiveis; projecao minima de campos
(summary, status, project, duedate, resolutiondate, updated).

planned=15 overdue=0 lookahead=33 sent=6 resolved=6 rework=4 | projects=21
planned acumulado: 2026-05=7 2026-06=1 2026-07=8 2026-08=3 2026-09=5

Conferencia contra os JSONs ja gravados em _snap/: os 12 conjuntos sairam
IDENTICOS aos da rodada _data1022i.

  - getVisibleJiraProjects e lookahead_2026-10 estouraram o limite de tokens
    da ferramenta e vieram como arquivo; campos minimos extraidos com jq.
  - conferencia por MD5 canonico (ordenacao por .key/.name + chaves ordenadas),
    que neutraliza diferencas de ordem de retorno do Jira:
        lookahead_2026-10  1fb0148e00e02f85ce94c5b39e3f03f5
        _projects_min      505192b9c2912c176357e055e44f085a
        planned_2026-10    6e647aa5b49e5a5ffbdb9a6d01ee248f
        overdue_2026-10    d751713988987e9331980363e24189ce (vazio)
        sent_2026-10       6e09d9b97ce39b02e08476277592df10
        resolved_2026-10   891d3e1f95bc3e11ab19d063c0687deb
        rework_2026-10     d0024c38510614f87769c0c7bac80cdb
        planned_2026-05    157ad827b2d9223d37c121a83295838f
        planned_2026-06    5e26c475b986a90fe739243f91db6d86
        planned_2026-07    99e4f5b92c1e42d607f9c33be40cde74
        planned_2026-08    6b203fddbfaa5a4c2507d46fdd6c384b
        planned_2026-09    ec11caaa3805975bceb76d087921f530
    Os MD5 no formato historico do README (jq -S -c 'sort_by(.key)') tambem
    foram reconferidos e batem com a tabela ja publicada.

Nenhum JSON precisou ser reescrito; apenas index.html e snapshot-data.js foram
regerados com carimbo novo (2026-10-22T21:31:44-03:00).

  index.html        161380 bytes  md5 9317f454ad7178fb416f2020fd08ceeb
  snapshot-data.js   73594 bytes  md5 3cc45472a7dede02ea5a05d5355e8150
  _artifact_src      87509 bytes  md5 6a2b6462a4efbec1890af4494a7f0b74 (inalterado)

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
    sobrevivendo intacto a uma atribuicao direta. Nenhum aviso de JQL sem
    correspondencia.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, projectTypeKey, atlassianAccountId e "self"; a unica
    ocorrencia de accountId e a palavra "accountIds" na linha de comentario do
    cabecalho do proprio bloco de dados.

Nenhuma operacao git foi executada nesta sessao; commit e push ficam a cargo da
tarefa PR03-Auto-Push-GitHub do Windows Task Scheduler.

Ressalva mantida: a pasta Documents\\Claude\\Artifacts continua inacessivel
(area protegida para sessoes Cowork; o shell responde "Permission denied" e ela
nao aparece em connectedFolders), entao o HTML do Live Artifact nao pode ser
reconferido; o snapshot foi gerado sobre o _artifact_src.html versionado.
"""
