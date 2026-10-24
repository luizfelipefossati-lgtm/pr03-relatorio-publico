# -*- coding: utf-8 -*-
"""Rodada 2026-10-24 00:33 UTC / 2026-10-23 21:33 BRT (execucao agendada, autonoma).

NENHUMA MUDANCA DE DADO. Snapshot regerado com carimbo 2026-10-23T21:33:32-03:00.

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

ETQ: issuetype in ("Epic","Fluxo de trabalho"), reconfirmado nesta rodada a
partir dos tipos de hierarchyLevel==1 dos 21 projetos visiveis.

O QUE MUDOU
-----------
Nada. Os onze conjuntos e a lista de projetos voltaram identicos aos gravados
em _snap/. As tres epics do EG0240 - GOITA/ COMPESA (EG0240-43, EG0240-5 e
EG0240-4) seguem com duedate 2026-10-26, em "Em Revisao" (indeterminate), sem
resolutiondate. Nenhuma atrasada em 23/10.

Nenhum JSON de _snap/ foi reescrito.

Conferencia
-----------
Dupla: primeiro por MD5 canonico calculado em Python
(json.dumps(sorted(d, key=key), sort_keys=True, separators=(',',':'))) sobre os
dados recem-devolvidos pelo Jira, lado a lado com os gravados; depois pelo MD5
canonico historico (jq -S -c 'sort_by(.key)'), para manter continuidade com as
rodadas anteriores. Os dois metodos concordam.

  conjunto            jq -S -c canonico                  veredito
  planned_2026-05     7b561eb1414d581166c3ffb820fa6c81   igual (conjunto e ordem)
  planned_2026-06     b483385522e7aba4bff7eaac7c70c70b   igual (conjunto e ordem)
  planned_2026-07     89c430d7301c007c96e90c518882ae87   igual (conjunto e ordem)
  planned_2026-08     4e49e617a3b2a5abc00c9a1b5f858fa6   igual (conjunto e ordem)
  planned_2026-09     1b5fac7dd7a83479c00b2ef40f75e97c   igual (conjunto e ordem)
  planned_2026-10     3fe8384df0f1b8cd9245df2901c72ef6   igual (conjunto e ordem)
  overdue_2026-10     58e0494c51d30eb3494f7c9198986bb9   igual (vazio dos dois lados)
  lookahead_2026-10   a38b4d9c77584b034fe2d7c2d0e61cd9   igual (conjunto e ordem)
  sent_2026-10        1f995242d71713c8c893953b6abdacb5   igual (conjunto e ordem)
  resolved_2026-10    de830431136ac892018b47b0219897c3   conjunto igual, ORDEM
                                                         diferente - JQL sem
                                                         ORDER BY, como em
                                                         _data1023e/f/g/h/i.
                                                         Arquivo mantido.
  rework_2026-10      92ac5a1b9b202bf88b9a210c5e83dbcd   igual (conjunto e ordem)
  _projects_min       cf7b59de6bf68fc6489470cf9018bd6e   igual

getVisibleJiraProjects e lookahead_2026-10 estouraram o limite de tokens e
vieram como arquivo; extraidos com jq na forma minima e conferidos por MD5.

As cinco planned da visao acumulada foram executadas por subagente, com a
mesma projecao completa de seis campos e a mesma forma aninhada; os MD5
canonicos e as contagens devolvidos conferem com os gravados.

Arquivos gerados
----------------
  index.html        161380 bytes  md5 ff15f4b95c2333775d171c40fad365c7
  snapshot-data.js   73594 bytes  md5 cd3c2e58a62baa71067da0c5762c9ea6
  _artifact_src      87509 bytes  md5 6a2b6462a4efbec1890af4494a7f0b74 (inalterado)

Mesmos tamanhos da rodada anterior: so os carimbos mudaram, e tem o mesmo
numero de caracteres.

Artifact ao vivo reconferido
----------------------------
HTML do Live Artifact obtido por device_stage_files com artifact_ids: 87.509
bytes, md5 6a2b6462a4efbec1890af4494a7f0b74, identico ao _artifact_src.html
versionado. Documents\\Claude\\Artifacts segue inacessivel ao shell e a
device_list_dir (area protegida); a via de staging resolve a conferencia.

Verificacoes desta rodada
-------------------------
  - comentario, bloco de dados e banner unicos; banner como ultimo elemento
    do <body>; arquivo termina integro em </div></body></html>.
  - removidos os tres, o restante e byte a byte igual ao _artifact_src.html
    (diferenca de comprimento = 0).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    comecando exatamente em 95.519; conteudo byte a byte igual ao
    snapshot-data.js publicado ao lado.
  - bloco executado em node: as 6 JQLs do mes corrente devolveram
    15/0/33/6/6/4, as 5 planned da visao acumulada devolveram 7/1/8/3/5,
    getVisibleJiraProjects devolveu 21 e __HISTORY__ expos 2026-07..2026-09.
    Nenhum aviso de JQL sem correspondencia.
  - planned_2026-10 servido pelo bloco traz EG0240-43, EG0240-5 e EG0240-4
    todos com duedate 2026-10-26.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, displayName, projectTypeKey e atlassianAccountId;
    a unica ocorrencia de accountId e a palavra "accountIds" na linha de
    comentario do cabecalho do proprio bloco de dados. Varredura por regex de
    e-mail no arquivo inteiro: nenhuma ocorrencia. As 7 ocorrencias de "@" sao
    da URL do CDN do chart.js e de regras @media/@keyframes do CSS.

Cadencia do agendamento
-----------------------
_data1023i gravou as 23:34 UTC de 23/10; esta comecou as 00:28 UTC de 24/10 -
intervalo de ~1h, cadencia horaria mantida. Em onze das doze ultimas rodadas
nada mudou; a unica mudanca (16:10 BRT de 23/10) chegou a pagina em 20 minutos.
Segue valendo a observacao de _data1023h/i: uma faixa de 3-6h gastaria bem
menos para praticamente o mesmo frescor. A escolha e do usuario.

Nenhuma operacao git executada nesta sessao.
"""
