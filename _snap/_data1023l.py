# -*- coding: utf-8 -*-
"""Rodada 2026-10-24 02:33 UTC / 2026-10-23 23:33 BRT (execucao agendada, autonoma).

NENHUMA MUDANCA DE DADO. Snapshot regerado com carimbo 2026-10-23T23:33:30-03:00.

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
Dois metodos, conforme a forma em que cada resposta chegou:

  - planned_2026-10, overdue_2026-10, sent_2026-10, resolved_2026-10 e
    rework_2026-10 vieram inteiros na resposta e foram conferidos CAMPO A
    CAMPO contra _snap/ (key, summary, status.name, statusCategory.key,
    project.key, project.name, duedate, resolutiondate), registro a registro.
  - getVisibleJiraProjects, lookahead_2026-10 e planned_2026-05..09 foram
    executados por subagente (lookahead estourou o limite de tokens) e
    conferidos por MD5 canonico calculado em python sobre a projecao minima
    (sorted by key, json.dumps sort_keys, separators=(',',':')), com o mesmo
    calculo aplicado aos arquivos gravados.

  conjunto            md5 canonico (python)             veredito
  planned_2026-05     157ad827b2d9223d37c121a83295838f  igual
  planned_2026-06     5e26c475b986a90fe739243f91db6d86  igual
  planned_2026-07     99e4f5b92c1e42d607f9c33be40cde74  igual
  planned_2026-08     6b203fddbfaa5a4c2507d46fdd6c384b  igual
  planned_2026-09     ec11caaa3805975bceb76d087921f530  igual
  lookahead_2026-10   1fb0148e00e02f85ce94c5b39e3f03f5  igual
  planned_2026-10     6803139f8cb2d2c3a01336257249650a  igual (campo a campo)
  overdue_2026-10     d751713988987e9331980363e24189ce  igual (vazio dos dois lados)
  sent_2026-10        6e09d9b97ce39b02e08476277592df10  igual (campo a campo)
  resolved_2026-10    891d3e1f95bc3e11ab19d063c0687deb  conjunto igual, ORDEM
                                                        diferente - JQL sem
                                                        ORDER BY, como em
                                                        _data1023e..k.
                                                        Arquivo mantido.
  rework_2026-10      d0024c38510614f87769c0c7bac80cdb  igual (campo a campo)
  _projects_min       505192b9c2912c176357e055e44f085a  igual

  Os MD5 desta tabela usam a canonicalizacao em python descrita acima; nao sao
  comparaveis aos de _data1023a..k, que usavam `jq -S -c 'sort_by(.key)'`.
  Ambos os lados (ao vivo e gravado) foram medidos com o mesmo metodo nesta
  rodada, entao a comparacao e valida.

Arquivos gerados
----------------
  index.html        161380 bytes  md5 706f565525a346673e93ce09c23155f6
  snapshot-data.js   73594 bytes  md5 3cccafb8c70f89b7951542fc9365a645
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
    (diferenca de comprimento = 0, comparacao de igualdade True).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    comecando exatamente em 95.519; conteudo byte a byte igual ao
    snapshot-data.js publicado ao lado.
  - bloco executado em node: as 6 JQLs do mes corrente devolveram
    15/0/33/6/6/4, as 5 planned da visao acumulada devolveram 7/1/8/3/5,
    getVisibleJiraProjects devolveu 21 e __HISTORY__ expos 2026-07..2026-09.
    Nenhum aviso de JQL sem correspondencia. epicTypeNames no bloco:
    ["Epic","Fluxo de trabalho"].
  - planned_2026-10 servido pelo bloco traz EG0240-43, EG0240-5 e EG0240-4
    todos com duedate 2026-10-26.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, displayName, projectTypeKey e atlassianAccountId;
    a unica ocorrencia de accountId e a palavra "accountIds" na linha de
    comentario do cabecalho do proprio bloco de dados. Varredura por regex de
    e-mail no arquivo inteiro: nenhuma ocorrencia.

Cadencia do agendamento
-----------------------
_data1023k gravou as 01:33 UTC de 24/10; esta gravou as 02:33 UTC - intervalo
de 1h, cadencia horaria mantida. Em treze das quatorze ultimas rodadas nada
mudou; a unica mudanca (16:10 BRT de 23/10) chegou a pagina em 20 minutos.
Segue valendo a observacao de _data1023h..k: uma faixa de 3-6h gastaria bem
menos para praticamente o mesmo frescor. A escolha e do usuario.

Nenhuma operacao git executada nesta sessao.
"""
