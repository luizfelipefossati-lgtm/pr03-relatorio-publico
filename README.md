# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 19/10/2026 11:35** (`2026-10-19T11:35:27-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **21**

### Consultas resolvidas (24 conjuntos + lista de projetos)

Meses encerrados — servidos pelo histórico embutido (`window.__HISTORY__`):

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-07` | Epics com due date em jul/2026 | 10 |
| `overdue_2026-07` | Vencidos antes de jul/2026, não concluídos | 0 |
| `lookahead_2026-07` | Due date entre ago/2026 e set/2026 | 26 |
| `sent_2026-07` | Transições para "Enviado - Aguardando Análise" em jul/2026 | 5 |
| `resolved_2026-07` | Concluídos em jul/2026 | 8 |
| `rework_2026-07` | Retrabalho em jul/2026 | 5 |
| `planned_2026-08` | Epics com due date em ago/2026 | 4 |
| `overdue_2026-08` | Vencidos antes de ago/2026, não concluídos | 0 |
| `lookahead_2026-08` | Due date entre set/2026 e out/2026 | 39 |
| `sent_2026-08` | Transições para "Enviado - Aguardando Análise" em ago/2026 | 4 |
| `resolved_2026-08` | Concluídos em ago/2026 | 6 |
| `rework_2026-08` | Retrabalho em ago/2026 | 3 |
| `planned_2026-09` | Epics com due date em set/2026 | 8 |
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 1 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 38 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 8 |
| `resolved_2026-09` | Concluídos em set/2026 | 4 |
| `rework_2026-09` | Retrabalho em set/2026 | 3 |

Mês corrente (out/2026) — servido pela interceptação de JQL (`window.cowork.callMcpTool`):

| Conjunto | Escopo | Registros | Geração anterior |
|---|---|---:|---:|
| `planned_2026-10` | Epics com due date em out/2026 | 15 | 15 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 0 | 0 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 | 33 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 6 | 6 |
| `resolved_2026-10` | Concluídos em out/2026 | 6 | 6 |
| `rework_2026-10` | Retrabalho em out/2026 | 4 | 4 |

Visão acumulada (`planned` por mês): mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8 · out/2026 = **15**.

Os meses de **abr/2026 a jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026, ago/2026 e set/2026** são
congelados pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Geração em 19/10/2026 11:35 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum conjunto mudou nesta rodada

Terceira geração de 19/10, cerca de **uma hora** depois da das 10:33. As **seis** consultas JQL
do mês corrente foram reexecutadas ao vivo com o predicado
`issuetype in ("Epic","Fluxo de trabalho")`, e as contagens repetem, uma a uma, as registradas
na rodada anterior:

| Conjunto | Ao vivo | Geração das 10:33 | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | vazio, sem alteração |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |

**Método desta rodada.** O `overdue_2026-10` foi consultado pela própria rotina; os outros
cinco conjuntos do mês corrente foram delegados a um **subagente**, junto das consultas
`planned` dos cinco meses anteriores, para que as respostas JQL completas não ocupassem o
contexto da rotina. O subagente devolveu apenas as contagens. A comparação com o disco foi
feita por **hash canônico**: cada arquivo novo e cada arquivo de `_snap/` foi reserializado em
JSON compacto, com os mesmos separadores e sem escapar acentos, e os MD5 resultantes batem nos
seis conjuntos — nenhuma chave nova, nenhuma chave ausente, nenhum campo alterado. Por isso
**nenhum arquivo de `_snap/` foi reescrito** nesta geração. Todas as respostas vieram completas
(`pageInfo.hasNextPage = false`), sem paginação pendente e sem erro. A projeção de seis campos
(`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`) foi aplicada em todas
as consultas.

**Meses encerrados continuam congelados.** As consultas `planned` de mai/2026 a set/2026 foram
reexecutadas ao vivo nesta rodada apenas para conferência, e **não** foram gravadas: os
arquivos de `_snap/` desses meses são o retrato do fechamento de cada período e alimentam tanto
a visão acumulada quanto os relatórios mensais congelados. A comparação mostra por que isso
importa — set/2026, por exemplo, tem **8** registros congelados contra **5** ao vivo hoje, já
que `duedate` de epics encerrados foi editado depois do fechamento. Sobrescrever esses arquivos
reescreveria retroativamente relatórios já publicados.

**Origem do HTML.** A pasta do Live Artifact
(`...\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics`) é uma área protegida e não
pode ser lida pelo shell da sessão. O HTML foi obtido pela via própria de artifacts
(`device_stage_files` com `artifact_ids`); seu MD5 (`6a2b6462a4ef…`, 87.509 bytes) é **idêntico**
ao do `_artifact_src.html` em disco, ou seja, o artifact não mudou desde a última geração.

A lista de projetos **foi reconsultada ao vivo** nesta rodada (`getVisibleJiraProjects`,
21 projetos). O hash canônico do resultado bate com o do `_projects_min.json` em disco, de modo
que o arquivo **não foi alterado** e os 21 projetos embutidos no `snapshot-data.js` seguem os
mesmos, assim como os tipos de nível Epic (`Epic`, `Fluxo de trabalho`) usados no predicado.

O subagente não executou nenhum comando `git` e não tocou em nenhum arquivo de `_snap/`.

Do lado do `git`, esta rodada não executou **nenhum** comando. A única inspeção de estado foi a
leitura dos quatro primeiros bytes de `.git/index`, que trazem a assinatura `DIRC` esperada —
o índice não está corrompido e não foi preciso recuperá-lo. Nenhum `add`, `commit` ou `push`, e
nenhuma tentativa de autenticação.

| Conjunto | SHA-256 (12 primeiros) | Bytes em disco |
|---|---|---:|
| `planned_2026-10` | `4af7adc31bc3` | 4.326 |
| `overdue_2026-10` | `37517e5f3dc6` | 3 |
| `lookahead_2026-10` | `123fdaac71a9` | 9.654 |
| `sent_2026-10` | `da81dfff54a2` | 1.909 |
| `resolved_2026-10` | `530d56710f6d` | 1.954 |
| `rework_2026-10` | `e1fb587feba0` | 1.273 |

Os hashes acima são o SHA-256 dos **bytes dos arquivos em disco** e são os mesmos das rodadas
das 09:29 e das 10:33 — os arquivos não foram tocados nesta geração. Eles usam recipiente
diferente do das tabelas de rodadas mais antigas, que normalizavam os registros antes de somar;
os valores não são comparáveis com os de lá.


### Correção de indicador (mantida da geração de 10/10 18:55)

Até a geração de 10/10 às 11:31, este README publicava o retrabalho de outubro contando apenas
os registros de `sent_2026-10` no denominador. O artifact usa outro denominador: ele monta a lista
de envios pela **união de `sent` e `resolved`** (`allSent`). O texto deste README foi corrigido na
geração das 18:55 para refletir o que a página de fato mostra, e a correção segue valendo nesta
rodada — agora com **57% (4 de 7)**, porque a união ganhou o `EG0274-38`, que também conta
como retrabalho.
O sexto item da união é o `EG0239-28`, que entra por `resolved` e não por `sent` porque seu
status chama-se `Enviado - Aguardando Análise1` — uma terceira grafia, da mesma família da
ressalva já registrada para o EG0285.

### Demais conferências

- Os seis arquivos de out/2026 **não foram regravados** nesta rodada; foram lidos e conferidos
  contra as respostas ao vivo, registro a registro. Seguem parseando como JSON, com os mesmos
  tamanhos e SHA-256 da rodada anterior, e sem nenhuma ocorrência de `accountId`,
  `avatarUrls`, `emailAddress` ou de endereço de e-mail.
- Os nomes de projeto gravados nos conjuntos são lidos do `_projects_min.json`, não digitados —
  checagem introduzida depois de um nome de projeto ter sido escrito à mão de forma incorreta na
  primeira tentativa de gravação (`EG0285`). O `EG0274 - DNIT` foi conferido contra esse arquivo.
- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026 (MD5 `6a2b6462a4ef…`). A pasta `Artifacts` é uma
  **localização protegida** (dados internos do Claude) e não pode ser lida por caminho de arquivo
  a partir de uma sessão Cowork — recusa reconfirmada nesta rodada. O HTML ao vivo foi obtido por
  *staging* de artifact (`device_stage_files` com `artifact_ids`), **refeito nesta rodada**, e
  conferido contra a cópia local: mesmos **87.509 bytes** e **MD5 idêntico**
  (`6a2b6462a4efbec1890af4494a7f0b74`). A data de modificação do artifact ao vivo continua em **27/07/2026**. A recusa de leitura da
  pasta `Artifacts` por caminho de arquivo foi reconfirmada nesta rodada, tanto em
  `device_list_dir` quanto em `ls`.
- As **12 consultas JQL** do mês corrente e da visão acumulada foram remontadas exatamente como
  o artifact as monta e testadas, uma a uma, contra os 11 padrões gravados em
  `snapshot-data.js`: cada consulta resolveu para o seu próprio conjunto, nenhuma caiu no
  *fallback* de lista vazia e nenhum padrão ficou órfão.
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.

### Quadro de outubro/2026 (19º dia do mês)

15 epics com due date em outubro — 12 em andamento/revisão (8 "Em andamento" + 4 "Em Revisão")
e 3 já enviados dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0240 = 3 · EG0274 = 2 · EG291 = 1.

Indicadores do mês na geração: **OTD 20%** (3 de 15), **retrabalho 57%** (4 de 7 envios),
**12 pendências do mês** e **nenhum em atraso acumulado**.

Os quatro indicadores repetem os da geração de 16/10 às 18:32, sem nenhuma transição nova no
intervalo:

- **OTD 20%** (3 de 15). Os três entregues — `EG0286-7`, `EG291-4` e `EG0274-38` — contam
  como **"SIM\*"** (entrega no mês, mas depois da due date), de modo que o painel marca
  **0 no prazo e 3 com pequeno atraso**.
- **Retrabalho 57%** (4 de 7 envios), no denominador do painel (união de `sent` e `resolved`).
- **Atraso acumulado** segue em **0**; as **pendências do mês**, em **12**.

O mês acumula **7 envios** no critério do painel (união de `sent` e `resolved`), sendo
**4 classificados como retrabalho**:

| EPIC | Projeto | Due date | Enviado em | Retrabalho |
|---|---|---|---|---|
| `EG0275-112` | EG0275 | 2026-09-04 | 02/10 09:27 | não |
| `EG0241-42` | EG0241 | 2026-09-10 | 02/10 09:30 | sim |
| `EG0286-7` | EG0286 | 2026-10-01 | 02/10 13:40 | sim |
| `EG0240-5` | EG0240 | 2026-10-26 | 07/10 16:01 | sim — reaberto em 13/10 09:51 |
| `EG0239-28` | EG0239 | 2026-08-10 | 09/10 09:36 | não |
| `EG291-4` | EG291 | 2026-10-07 | 15/10 13:59 | não |
| `EG0274-38` | EG0274 | 2026-10-07 | 15/10 15:30 | sim |

Quatro dos sete eram entregas que vinham em atraso de meses anteriores; `EG0286-7`, `EG291-4` e
`EG0274-38` são as únicas com due date do próprio mês de outubro — e as únicas que contam no
OTD até aqui.
`EG0239-28` aparece apenas por `resolved`: seu status (`Enviado - Aguardando Análise1`) não casa
a string exata usada pelas consultas `sent`/`rework`. O `EG0240-5` continua em `sent` e em
`rework` mesmo tendo perdido a conclusão: a transição de 07/10 está no histórico e o `DURING` a
enxerga; o que mudou em 16/10 foi apenas a sua due date.

### Lookahead nov–dez/2026

33 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 22**, dos quais 20 têm due date entre 16 e 31/12.

A composição é a mesma das gerações anteriores; nesta rodada o `lookahead` foi conferido ao
vivo em duas metades, com as mesmas 11 chaves de novembro e 22 de dezembro, e preservado em
disco sem regravação, como os outros cinco conjuntos do mês corrente. O EG0256 segue sem representante no lookahead desde a saída do
`EG0256-30`, reprogramado para 30/01/2027. **20 dos 33 registros (61%)** caem na segunda quinzena
de dezembro — o gargalo de fim de ano permanece, concentrado em EG0274 e EG0286.

### Setembro/2026, congelado

Indicadores gravados em definitivo: **8 previstos**, **1 em atraso acumulado**, **8 envios**,
**3 de retrabalho**, **4 resoluções**, OTD **63% (5 de 8)**.

Como registrado nas gerações anteriores, o fechamento carrega duas ressalvas conhecidas,
preservadas aqui sem correção porque espelham o comportamento do artifact ao vivo:

- **Corte das 00h em `resolved`.** Três EPICs resolvidos ao longo do dia 30/09 — `G0280-52`
  (11:23), `EG0285-19` (15:15) e `EG0240-4` (17:27) — ficaram fora de `resolved_2026-09`, porque
  a consulta usa `resolved<="2026-09-30"`, que o Jira lê como meia-noite do dia 30. A cláusula
  `DURING` de `sent` não sofre o mesmo corte e cobre o dia inteiro.
- **Grafia de status no EG0285.** O status do fluxo chama-se `Enviado- Aguardando Análise`
  (id `11737`, sem espaço antes do hífen), enquanto `sent`/`rework` casam a string exata
  `Enviado - Aguardando Análise`. Por isso `EG0285-19` conta como entregue no OTD mas não aparece
  entre os envios de setembro.

Corrigir qualquer das duas exige ação fora deste processo: renomear o status `11737` para a
grafia canônica no Jira e/ou ajustar o limite superior da consulta `resolved` para `23:59` no
artifact.

### Conferência estrutural

Checagens desta rodada (contagens e carimbos reconferidos após a geração):

- Comentário de geração no topo do `<head>`: presente, imediatamente após `<head>` (byte 609 do
  arquivo), com o carimbo `2026-10-19T11:35:27-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (o bloco injetado abre no byte 22.522 do `index.html` e `window.__SNAPSHOT__` é atribuído no
  byte 97.267, contra o byte 99.708 da atribuição `window.__HISTORY__=` do `<script>` próprio
  do artifact — ordem de execução confirmada). O bloco embutido é, além disso, **byte a byte
  igual** ao `snapshot-data.js` gravado ao lado.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 19/10/2026 11:35,
  seguido apenas de `</body></html>`. Ocorrência única no arquivo (abre no byte 164.840).
- Tamanhos da geração: `index.html` **164.972 bytes** (MD5 `ea3a204d5024…`) e
  `snapshot-data.js` **77.186 bytes** (MD5 `e5c17f071703…`). Os tamanhos são exatamente os da
  rodada das 10:33 — o conteúdo embutido é idêntico e o carimbo de geração tem comprimento
  fixo —, enquanto os MD5 diferem apenas por causa do carimbo.
- Contagens dos conjuntos **embutidos** lidas de volta do `snapshot-data.js` publicado e
  conferidas uma a uma contra os arquivos de `_snap/`: `planned_2026-10` 15,
  `overdue_2026-10` 0, `lookahead_2026-10` 33, `sent_2026-10` 6, `resolved_2026-10` 6,
  `rework_2026-10` 4, e a acumulada `planned` de mai a set/2026 em 7, 1, 10, 4 e 8. Os 21
  projetos, os tipos de nível Epic (`Epic`, `Fluxo de trabalho`) e os meses congelados
  (`2026-07`, `2026-08`, `2026-09`) também foram lidos de volta do arquivo publicado.
- As **12 consultas JQL** do mês corrente e da visão acumulada (6 do mês + 6 meses da
  acumulada, sendo `planned_2026-10` comum às duas) foram reconstruídas exatamente como o
  artifact as monta — inclusive o `issuetype in ("Epic","Fluxo de trabalho")` montado a partir
  dos tipos de nível Epic — e testadas contra os padrões gravados em `snapshot-data.js`: as 12
  resolvem para o conjunto correto, sem *fallback* para lista vazia, e nenhum padrão ficou
  órfão (11 padrões para 11 conjuntos embutidos).
- Esta geração **remontou o `index.html` do zero** a partir do `_artifact_src.html` com o
  `_gen_snapshot.py`, e a estrutura foi reconferida depois, item a item, como listado acima.
  Registre-se que o relógio da VM que executa os comandos no computador está em UTC: o carimbo
  foi calculado em BRT (UTC−3) e conferido no arquivo final.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudou apenas o carimbo de geração.
- Nenhuma ocorrência de `avatarUrls`, `iconUrl`, `emailAddress` ou domínio de e-mail no arquivo
  publicado, e nenhuma URL da `api.atlassian.com` — a única URL da Atlassian é a base
  `https://projetos-engeplus.atlassian.net/browse/`, usada para montar os links dos EPICs. A
  única ocorrência da palavra `accountId` é o comentário do próprio gerador
  ("Nao contem accountIds"), e a única sequência com `@` fora das regras CSS `@media` é a
  versão do pacote `chart.js@4.5.0` no endereço da CDN.

---

## Publicação

O `index.html` e este `README.md` são gravados no *working tree* por esta rotina. O
`git commit`/`push` é feito separadamente pela tarefa `PR03-Auto-Push-GitHub` do Windows Task
Scheduler — que, pelo `.push-watchdog.log`, vem rodando a cada **10 minutos** — e o deploy no
Vercel segue o push.

> **Nota de publicação (19/10/2026, 11:35).** A cadeia de publicação está íntegra: as quatro
> passagens mais recentes do watchdog — 11:04, 11:14, 11:24 e 11:34 — concluíram todas com
> sucesso, em cadência regular de 10 minutos, a última com `Commit OK: 9616e5f` e `Push OK e
> VERIFICADO: HEAD sincronizado com origin/main`. Em nenhuma delas houve lock pendente ou
> índice quebrado. Esta geração entra na passagem seguinte, prevista para ~11:44.
