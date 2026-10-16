# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 16/10/2026 18:32** (`2026-10-16T18:32:17-03:00`)

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

Geração em 16/10/2026 18:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum conjunto mudou nesta rodada

Quarta geração da tarde de 16/10, cerca de **uma hora** depois da das 17:31. As **seis**
consultas JQL do mês corrente foram reexecutadas ao vivo com o predicado
`issuetype in ("Epic","Fluxo de trabalho")`, e as contagens repetem, uma a uma, as registradas
na rodada anterior:

| Conjunto | Ao vivo | Geração das 17:31 | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | vazio, sem alteração |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |

**Diferença de método em relação à rodada das 17:31:** o método de conferência é o mesmo —
arquivos **preservados** e comparação **registro a registro** —, mas a divisão do trabalho
mudou. O `planned_2026-10` foi consultado pela própria rotina; os outros cinco conjuntos
foram delegados a um **subagente**, para que as respostas JQL completas não ocupassem o
contexto da rotina. Os 64 registros ao vivo (15 + 0 + 33 + 6 + 6 + 4) foram comparados aos de
disco chave a chave e campo a campo — `duedate`, nome de status, categoria de status,
`resolutiondate`, `summary`, projeto e `updated` —, sem nenhuma diferença, nenhuma chave nova
e nenhuma chave ausente. Os seis arquivos mantêm, byte a byte, os mesmos tamanhos e os mesmos
SHA-256 publicados na rodada anterior.

As seis respostas vieram completas (`pageInfo.hasNextPage = false`), sem paginação pendente,
sem timeouts e sem nenhum `502`. O `lookahead_2026-10` foi novamente consultado em **duas
metades** (`duedate` em nov/2026 e em dez/2026, 11 + 22 = 33), o que manteve as respostas
abaixo do limite de tokens e dispensou a extração por arquivo. A projeção de seis campos
(`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`) foi aplicada em todas
as consultas.

A lista de projetos **não foi reconsultada** nesta rodada: o `_projects_min.json` de 14/10
(21 projetos) segue como fonte dos nomes de projeto e dos tipos de nível Epic (`Epic`,
`Fluxo de trabalho`) usados no predicado, e os 21 projetos embutidos no `snapshot-data.js`
não foram alterados. A reconsulta ao vivo da rodada das 17:31, que os confirmou um a um,
continua valendo como última verificação dessa lista.

A busca e a redução de cinco dos seis conjuntos foram delegadas a um subagente, que gravou
apenas o seu relatório de comparação — nenhum arquivo de `_snap/` foi tocado, porque não
houve diferença a registrar — e não executou nenhum comando `git`. Do lado do `git`, esta
rodada não executou **nenhum** comando, nem de leitura: a única inspeção de estado foi a
leitura do `.push-watchdog.log`. Nenhum `add`, `commit` ou `push`, e nenhuma tentativa de
autenticação.

| Conjunto | SHA-256 (12 primeiros) | Bytes em disco |
|---|---|---:|
| `planned_2026-10` | `4af7adc31bc3` | 4.326 |
| `overdue_2026-10` | `37517e5f3dc6` | 3 |
| `lookahead_2026-10` | `123fdaac71a9` | 9.654 |
| `sent_2026-10` | `da81dfff54a2` | 1.909 |
| `resolved_2026-10` | `530d56710f6d` | 1.954 |
| `rework_2026-10` | `e1fb587feba0` | 1.273 |

Os hashes acima são o SHA-256 dos **bytes dos arquivos em disco** e são os mesmos da rodada
das 17:31 — os arquivos não foram tocados nesta geração. Eles usam recipiente diferente do
das tabelas de rodadas mais antigas, que normalizavam os registros antes de somar; os valores
não são comparáveis com os de lá.


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
  primeira tentativa de gravação (`EG0285`). O `EG0274 - DNIT`, projeto do EPIC entregue nesta
  rodada, foi conferido contra esse arquivo.
- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026. A pasta `Artifacts` é uma
  **localização protegida** (dados internos do Claude) e não pode ser lida por caminho de arquivo
  a partir de uma sessão Cowork — recusa reconfirmada nesta rodada. O HTML ao vivo foi obtido por
  *staging* de artifact (`device_stage_files` com `artifact_ids`), **refeito nesta rodada**, e
  conferido contra a cópia local: mesmos **87.509 bytes** e **MD5 idêntico**
  (`6a2b6462a4efbec1890af4494a7f0b74`). O inventário de artifacts confirma que o
  `pr03-relatorio-indicadores-epics` continua com `updatedAt` de **27/07/2026**. A recusa de
  leitura da pasta `Artifacts` por caminho de arquivo foi reconfirmada nesta rodada, em `ls`.
- As **12 consultas JQL** do mês corrente e da visão acumulada foram remontadas exatamente como
  o artifact as monta e testadas, uma a uma, contra os 11 padrões gravados em
  `snapshot-data.js`: cada consulta resolveu para o seu próprio conjunto, nenhuma caiu no
  *fallback* de lista vazia e nenhum padrão ficou órfão.
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.

### Quadro de outubro/2026 (16º dia do mês)

15 epics com due date em outubro — 12 em andamento/revisão (8 "Em andamento" + 4 "Em Revisão")
e 3 já enviados dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0240 = 3 · EG0274 = 2 · EG291 = 1.

Indicadores do mês na geração: **OTD 20%** (3 de 15), **retrabalho 57%** (4 de 7 envios),
**12 pendências do mês** e **nenhum em atraso acumulado**.

Os quatro indicadores repetem os da geração das 17:31, sem nenhuma transição nova no
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
enxerga; o que mudou hoje foi apenas a sua due date.

### Lookahead nov–dez/2026

33 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 22**, dos quais 20 têm due date entre 16 e 31/12.

A composição é a mesma das gerações anteriores; nesta rodada os seis conjuntos do mês
corrente foram conferidos ao vivo e preservados em disco, sem regravação. O EG0256 segue sem representante no lookahead desde a saída do
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

- Comentário de geração no topo do `<head>`: presente, imediatamente após `<head>` (byte 608 do
  arquivo), com o carimbo `2026-10-16T18:32:17-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (o comentário de cabeçalho do bloco injetado começa no byte 22.531 do `index.html` e
  `window.__SNAPSHOT__` é atribuído no byte 97.267, contra o byte 99.717 da atribuição
  `window.__HISTORY__=` do `<script>` próprio do artifact — ordem de execução confirmada).
  O bloco embutido é, além disso, **byte a byte igual** ao `snapshot-data.js` gravado ao lado
  (MD5 `b1ad41bc1819…` nos dois).
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 16/10/2026 18:32,
  seguido apenas de `</body></html>`. Ocorrência única no arquivo.
- As **12 consultas JQL** do mês corrente e da visão acumulada (6 do mês + 6 meses da
  acumulada, sendo `planned_2026-10` comum às duas) foram reconstruídas exatamente como o
  artifact as monta — inclusive o `issuetype in ("Epic","Fluxo de trabalho")` montado a partir
  dos tipos de nível Epic — e testadas contra os padrões gravados em `snapshot-data.js`: as 12
  resolvem para o conjunto correto, sem *fallback* para lista vazia, e nenhum padrão ficou
  órfão (11 padrões para 11 conjuntos embutidos).
- Contagens dos conjuntos do mês corrente conferidas contra os arquivos de `_snap/`:
  `planned` 15, `overdue` 0, `lookahead` 33, `sent` 6, `resolved` 6, `rework` 4.
- Tamanhos da geração: `index.html` **164.972 bytes** e `snapshot-data.js` **77.186 bytes**,
  exatamente os da rodada das 17:31 — o conteúdo embutido é idêntico e o carimbo de geração
  tem comprimento fixo.
- Contagens dos conjuntos **embutidos** no `snapshot-data.js` lidas de volta do arquivo
  publicado e conferidas uma a uma contra as de `_snap/`: `planned_2026-10` 15,
  `overdue_2026-10` 0, `lookahead_2026-10` 33, `sent_2026-10` 6, `resolved_2026-10` 6,
  `rework_2026-10` 4, e a acumulada `planned` de mai a set/2026 em 7, 1, 10, 4 e 8.
- Como nenhum dos seis conjuntos mudou e o HTML de origem está inalterado, esta geração
  **reaproveitou o `index.html` da rodada anterior e trocou apenas os carimbos** (as quatro
  ocorrências do ISO e a data do banner), em vez de remontar um arquivo idêntico a partir do
  `_artifact_src.html`. A estrutura foi reconferida depois da troca, item a item, como listado
  acima. Registre-se que o relógio da VM que executa os comandos no computador está em UTC: o
  carimbo foi calculado em BRT (UTC−3) e conferido no arquivo final.
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

> **Nota de publicação (16/10/2026, 18:32).** A cadeia de publicação está íntegra: as três
> passagens mais recentes do watchdog — 18:04, 18:14 e 18:24 — concluíram todas com
> sucesso, em cadência regular de 10 minutos, a última com `Commit OK: 2728daf` e `Push OK e
> VERIFICADO: HEAD sincronizado com origin/main`. Esta geração entra na passagem seguinte,
> prevista para ~18:34.
