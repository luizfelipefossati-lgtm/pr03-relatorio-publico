# -*- coding: utf-8 -*-
"""Rodada 2026-10-26 13:40 UTC / 2026-10-26 10:40 BRT (execucao agendada, autonoma).

NENHUMA MUDANCA DE DADO. Snapshot regerado com carimbo 2026-10-26T10:40:55-03:00.

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
_data1024a gravou as 03:33 UTC de 24/10 (sabado); esta gravou as 13:40 UTC de
26/10 (segunda) - cerca de 58h sem geracao. O .watch.log mostra o watcher
reiniciando as 09:18 de 26/10, compativel com a estacao desligada no fim de
semana. Nenhum dado do Jira mudou no intervalo, entao a pagina publicada nao
ficou defasada em conteudo, so no carimbo. Nao ha falha a investigar.

O QUE MUDOU
-----------
Nada. Os onze conjuntos e a lista de projetos voltaram identicos aos gravados
em _snap/. As tres epics do EG0240 - GOITA/ COMPESA (EG0240-43, EG0240-5 e
EG0240-4) seguem com duedate 2026-10-26, em "Em Revisao" (indeterminate), sem
resolutiondate. Como a geracao e de 26/10, nenhuma conta como atrasada e
overdue_2026-10 segue vazio.

Nenhum JSON de _snap/ foi reescrito.

Conferencia
-----------
Dois metodos, conforme a forma em que cada resposta chegou:

  - Nove conjuntos (planned_2026-05..10, overdue, sent, resolved, rework do mes
    corrente) vieram inteiros na resposta e foram conferidos CAMPO A CAMPO: os
    registros foram remontados na projecao ANINHADA de _snap/ e comparados por
    MD5 canonico em python (sorted by key, json.dumps sort_keys,
    separators=(',',':'), ensure_ascii=False), com o mesmo calculo aplicado aos
    arquivos gravados. Os dez MD5 bateram (inclui overdue vazio).

      planned_2026-05  157ad827b2d9223d37c121a83295838f  igual
      planned_2026-06  5e26c475b986a90fe739243f91db6d86  igual
      planned_2026-07  99e4f5b92c1e42d607f9c33be40cde74  igual
      planned_2026-08  6b203fddbfaa5a4c2507d46fdd6c384b  igual
      planned_2026-09  ec11caaa3805975bceb76d087921f530  igual
      planned_2026-10  6803139f8cb2d2c3a01336257249650a  igual
      overdue_2026-10  d751713988987e9331980363e24189ce  igual (vazio)
      sent_2026-10     6e09d9b97ce39b02e08476277592df10  igual
      resolved_2026-10 891d3e1f95bc3e11ab19d063c0687deb  igual
      rework_2026-10   d0024c38510614f87769c0c7bac80cdb  igual

  - getVisibleJiraProjects e lookahead_2026-10 estouram o limite de tokens da
    ferramenta e foram executados por subagente, que projetou os campos minimos
    e gravou os arquivos em $HOME/snapshot_data/ (fora de mnt/). Resultado:
    BYTE A BYTE identicos aos em uso (3.836 e 10.378 bytes), com MD5 canonico
    505192b9c2912c176357e055e44f085a e 1fb0148e00e02f85ce94c5b39e3f03f5 dos
    dois lados.

Tabela no README (convencao jq -S -c 'sort_by(.key)', comparavel entre
rodadas): os doze valores sao identicos aos de _data1024a.

Ordem de retorno
----------------
planned_2026-10, sent_2026-10 e rework_2026-10 voltaram na MESMA ordem gravada.
resolved_2026-10 voltou em ordem diferente, como nas rodadas anteriores - e
consultado sem ORDER BY:
  agora    EG291-4, EG0286-7, EG0275-112, EG0274-38, EG0241-42, EG0239-28
  gravado  EG0275-112, EG0241-42, EG0286-7, EG0239-28, EG291-4, EG0274-38
Conjunto e valores identicos; a ordem nao e carregada pelo relatorio (o gerador
funde sent+resolved num mapa por chave e ordena pelo sinalizador de
retrabalho). Arquivo mantido.

Arquivos gerados
----------------
  index.html        161380 bytes  md5 69f781af4582ceb0111dccfcdad6dc20
  snapshot-data.js   73594 bytes  md5 8da4fb22d4ae67b1aff183fbf7e02989
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
    (igualdade True, diferenca de comprimento 0).
  - bloco do snapshot em 22.444-95.519, com o script principal do artifact
    comecando exatamente em 95.519; conteudo byte a byte igual ao
    snapshot-data.js publicado ao lado.
  - bloco executado em node: as 6 JQLs do mes corrente devolveram
    15/0/33/6/6/4, as 5 planned da visao acumulada devolveram 7/1/8/3/5,
    getVisibleJiraProjects devolveu 21 e __HISTORY__ expos 2026-07..2026-09.
    Nenhum aviso de JQL sem correspondencia. epicTypeNames no bloco:
    ["Epic","Fluxo de trabalho"]. planned_2026-10 servido pelo bloco traz
    EG0240-43, EG0240-5 e EG0240-4 todos com duedate 2026-10-26.
  - varredura de privacidade no index.html: zero ocorrencias de avatarUrls,
    emailAddress, iconUrl, displayName, projectTypeKey, atlassianAccountId e
    'self":'. A unica ocorrencia de accountId e a palavra "accountIds" na
    linha de comentario do cabecalho do proprio bloco de dados. A varredura
    por regex de e-mail acusou UMA ocorrencia, inspecionada: e a versao do
    CDN "chart.js@4.5.0" no <head>, presente tambem no _artifact_src.html.
    Nao e e-mail. (Rodadas anteriores reportaram zero porque usavam um regex
    que exigia TLD alfabetico puro.)

Nenhuma operacao git executada nesta sessao.
"""
