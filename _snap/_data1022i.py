# -*- coding: utf-8 -*-
"""Rodada 2026-10-22 23:31 UTC / 20:31 BRT (execucao agendada, autonoma).

As 7 chamadas dinamicas do artifact foram refeitas ao vivo contra o Jira
(cloud ead785de-33f3-4746-9bdb-a2a58cf5213b) pelo conector MCP Atlassian:
getVisibleJiraProjects + as 6 consultas JQL do mes corrente (out/2026), com
ETQ = issuetype in ("Epic","Fluxo de trabalho") e projecao minima de campos
(summary, status, project, duedate, resolutiondate, updated).

planned=15 overdue=0 lookahead=33 sent=6 resolved=6 rework=4 | projects=21

Conferencia contra os JSONs ja gravados em _snap/: os 7 conjuntos sairam
IDENTICOS aos das rodadas _data1022b/_1022d..._1022h.

  - getVisibleJiraProjects e lookahead_2026-10 estouraram o limite de tokens da
    ferramenta e vieram como arquivo; campos minimos extraidos com jq e
    conferidos por MD5 canonico (jq -S -c 'sort_by(.key // .name)'):
        lookahead_2026-10  a38b4d9c77584b034fe2d7c2d0e61cd9
        _projects_min      cf7b59de6bf68fc6489470cf9018bd6e
  - planned/overdue/sent/resolved/rework vieram inline e foram conferidos
    campo a campo (key, project.key, duedate, status.name,
    status.statusCategory.key, updated, resolutiondate, summary) contra os
    JSONs gravados: coincidencia integral, inclusive na ordem de retorno.
        planned_2026-10    beb20fe094f4f249b43b20e9becc072f
        overdue_2026-10    58e0494c51d30eb3494f7c9198986bb9
        sent_2026-10       1f995242d71713c8c893953b6abdacb5
        resolved_2026-10   de830431136ac892018b47b0219897c3
        rework_2026-10     92ac5a1b9b202bf88b9a210c5e83dbcd

Nenhum JSON precisou ser reescrito; apenas index.html e snapshot-data.js foram
regerados com carimbo novo (2026-10-22T20:31:13-03:00).

  index.html        161380 bytes  md5 c004d7de4b2113261ca6b22e77098fee
  snapshot-data.js   73594 bytes  md5 f1a816c4af1b94818f0d84dd4e9c200e
  _artifact_src      87509 bytes  md5 6a2b6462a4efbec1890af4494a7f0b74 (inalterado)

Verificacoes desta rodada:
  - comentario, bloco de dados e banner unicos; banner como ultimo elemento do
    <body>; removidos os tres, o restante e byte a byte igual ao
    _artifact_src.html (diff de comprimento = 0).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    comecando exatamente em 95.519; o conteudo do bloco (com as tags <script>)
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
