# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 13/10/2026 16:30** (`2026-10-13T16:30:09-03:00`)

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
| `planned_2026-10` | Epics com due date em out/2026 | 13 | 13 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 1 | 1 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 34 | 34 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 4 | 4 |
| `resolved_2026-10` | Concluídos em out/2026 | 4 | 4 |
| `rework_2026-10` | Retrabalho em out/2026 | 3 | 3 |

Visão acumulada (`planned` por mês): mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8 · out/2026 = 13.

Os meses de **abr/2026 a jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026, ago/2026 e set/2026** são
congelados pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Geração em 13/10/2026 16:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum conjunto alterado nesta rodada — e onde o predicado corrigido realmente mora

As sete chamadas dinâmicas foram reexecutadas ao vivo, já com o predicado corrigido
`issuetype in (Epic, "Fluxo de trabalho")`, e **reproduziram o cache de `_snap/` item a item** —
chave, resumo, status, categoria, due date, data de resolução e `updated`:

| Conjunto | Ao vivo | Cache em disco | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 13 | 13 | idêntico ao cache |
| `overdue_2026-10` | 1 | 1 | idêntico ao cache |
| `lookahead_2026-10` | 34 | 34 | idêntico ao cache |
| `sent_2026-10` | 4 | 4 | idêntico ao cache |
| `resolved_2026-10` | 4 | 4 | idêntico ao cache |
| `rework_2026-10` | 3 | 3 | idêntico ao cache |
| projetos visíveis | 21 | 21 | idêntico ao cache |

Os conjuntos `lookahead_2026-10` e a lista de projetos foram conferidos por `sha256` do JSON
canônico, e os cinco demais item a item. **Não houve movimento no Jira entre 15:30 e 16:30** —
é a sexta rodada consecutiva sem movimento real. Nenhum arquivo de `_snap/` nem o
`_projects_min.json` precisou ser regravado, e `index.html` e `snapshot-data.js` mantiveram o
mesmo tamanho em bytes (163.342 e 75.556), mudando apenas o carimbo de tempo. As posições do
`window.__SNAPSHOT__` (95.025) e do `window.__HISTORY__` do artifact (97.475) também não se
moveram, o que confirma que o HTML-fonte é byte a byte o mesmo fora dos carimbos.

**Correção da pendência registrada na rodada das 15:30.** Aquela nota concluía que o predicado
`issuetype=Epic` precisava ser trocado *no relatório*. A leitura do `_artifact_src.html` nesta
rodada mostra que **a página não tem esse predicado fixo**: em `LP()` ela varre os tipos de item
de todos os projetos visíveis, seleciona os de `hierarchyLevel === 1` e monta o predicado
dinamicamente em `ETQ` — hoje, `issuetype in ("Epic","Fluxo de trabalho")`. Ou seja, o relatório
publicado **já alcança** EG0285, EG0286, EG0294 e EG291; o truncamento observado às 15:30 foi um
artefato da consulta manual, não do dashboard. A verificação de padrões abaixo confirma: as 11
consultas que a página monta com o `ETQ` dinâmico casam com os 11 padrões gravados em
`snapshot-data.js`, sem sobra nem órfão.

> **Pendência remanescente (menor).** O texto `issuetype=Epic` continua gravado no prompt da
> tarefa agendada, no passo que descreve as seis consultas. Ele não afeta a página publicada,
> mas faz cada rodada partir de uma consulta truncada e precisar corrigi-la à mão. Trocar
> aquele trecho do prompt por `issuetype in (Epic, "Fluxo de trabalho")` elimina o retrabalho —
> e é uma alteração no prompt da tarefa, que esta rotina não faz por conta própria.

A **visão acumulada** (`planned_2026-05` a `planned_2026-10`) não foi reconsultada ao vivo nesta
rodada: outubro já é coberto pelo `planned_2026-10` acima, e maio a setembro são meses encerrados,
servidos tal como estão em `_snap/`. Julho, agosto e setembro são, além disso, **congelados** no
fechamento do período — divergem de propósito de uma consulta ao vivo, pelas reprogramações
posteriores ao fechamento (`EG0274-38` e `EG0274-43` saíram de julho para outubro; `EG0286-7`
saiu de agosto para outubro; `EG0240-4` saiu de setembro para 16/10). Pela regra de congelamento,
esses arquivos **não** são regravados: o histórico de OTD de cada mês continua refletindo o
que estava previsto no fechamento daquele mês.

> **Nota de publicação (13/10/2026, 16:30).** A cadeia de publicação segue íntegra. O
> `.push-watchdog.log` registra seis passagens desde a geração anterior — 15:34:34, 15:44:34,
> 15:54:34, 16:04:34, 16:14:34 e 16:24:34 — todas com `Commit OK` seguido de
> `Push OK e VERIFICADO` e `HEAD` sincronizado com `origin/main`; a última foi o commit
> `189d7e4`. A geração das 15:30 foi, portanto, publicada. Esta geração entra na próxima
> passagem da tarefa.

Outubro segue com **um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e de novo
`Em Revisão` desde 13/10 às 09:51. O efeito da reprogramação dos dois EPICs do EG0256
(`EG0256-30` para 19/12/2026 e `EG0256-28` para 29/01/2027), registrada na rodada de 08/10
às 11:31, segue valendo.

### Correção de indicador (mantida da geração de 10/10 18:55)

Até a geração de 10/10 às 11:31, este README publicava o retrabalho de outubro como **75% (3 de 4)**, contando apenas
os registros de `sent_2026-10` no denominador. O artifact usa outro denominador: ele monta a lista
de envios pela **união de `sent` e `resolved`** (`allSent`), de modo que o painel exibe
**60% (3 de 5)**. O texto deste README foi corrigido na geração das 18:55 para refletir o que a
página de fato mostra, e a correção segue valendo nesta rodada.
O quinto item da união é o `EG0239-28`, que entra por `resolved` e não por `sent` porque seu
status chama-se `Enviado - Aguardando Análise1` — uma terceira grafia, da mesma família da
ressalva já registrada para o EG0285.

### Demais conferências

- Cada um dos seis conjuntos de out/2026 foi coletado em **uma única consulta** nesta rodada,
  com a projeção mínima de campos (`summary`, `status`, `project`, `duedate`, `resolutiondate`,
  `updated`) e `pageInfo.hasNextPage = false` em todas. O `lookahead`, por ser o maior conjunto,
  foi pedido sem o campo `project` — que não muda para uma issue já existente — e coube inline;
  a comparação com o arquivo em disco foi feita por `key`, `summary`, `status.name`,
  `status.statusCategory.key`, `duedate`, `resolutiondate` e `updated`, mais a ordem, e o
  `project` de cada registro foi preservado do arquivo. Só a resposta do
  `getVisibleJiraProjects` excedeu o limite de tokens; foi reduzida à forma mínima sobre o
  arquivo salvo pelo runtime, conforme o procedimento previsto.
- A comparação com a geração anterior usa hash canônico campo a campo (`summary`, `status.name`,
  `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`,
  `updated`), insensível à ordem dos registros.
- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026. MD5
  `6a2b6462a4efbec1890af4494a7f0b74`, o mesmo das rodadas anteriores (conferido nesta rodada).
  A pasta `Artifacts` segue sendo uma **localização protegida** (dados internos do Claude) e não
  pode ser lida por caminho de arquivo a partir de uma sessão Cowork. Nesta rodada, como nas
  anteriores, o HTML ao vivo do Live Artifact foi obtido pela via de *staging* de artifact
  (`device_stage_files` por `artifact_ids`, 87.509 bytes) e conferido contra a cópia versionada:
  **idêntico, byte a byte**.
- `getVisibleJiraProjects`: **reconsultado ao vivo** — `total` = 21, `isLast` = true. Reduzido à
  mesma forma mínima e comparado por hash canônico contra `_projects_min.json`: idêntico, o
  arquivo não precisou ser reescrito. Os dois tipos de nível Epic seguem sendo `Epic` e
  `Fluxo de trabalho`.
- As **11 consultas JQL** do mês corrente e da visão acumulada foram remontadas exatamente como
  o artifact as monta e testadas, uma a uma, contra os 11 padrões gravados em
  `snapshot-data.js`: cada consulta resolveu para o seu próprio conjunto, nenhuma caiu no
  *fallback* de lista vazia e nenhum padrão ficou órfão.
- **Filtro de tipo de item.** As consultas desta rodada usaram
  `issuetype in ("Epic","Fluxo de trabalho")`, que é o que o artifact de fato monta: ele
  parte de `epicTypes=['Epic']` apenas como padrão e substitui a lista pelos tipos de
  hierarquia 1 descobertos nos projetos visíveis. Rodar com o literal `issuetype=Epic`
  (como está escrito, de forma simplificada, no prompt da tarefa agendada) deixaria de fora
  os epics de EG0286 e EG291, que nomeiam esse nível como `Fluxo de trabalho`. **Convém alinhar
  o texto do prompt agendado ao filtro real** — a ressalva se repete desde rodadas anteriores.
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.

### Quadro de outubro/2026 (13º dia do mês)

13 epics com due date em outubro — 12 em andamento/revisão (9 "Em andamento" + 3 "Em Revisão")
e 1 já enviado dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0274 = 2 · EG0240 = 1 · EG291 = 1.

Indicadores do mês na geração: **OTD 8%** (1 de 13), **retrabalho 60%** (3 de 5 envios),
**12 pendências do mês** e **1 em atraso acumulado**.

Os três indicadores repetem os da geração anterior. O OTD permanece em 8%: o único envio com
due date de outubro continua sendo `EG0286-7`, e o denominador segue em 13 desde a entrada de
`EG0240-4`, reprogramado para 16/10. O retrabalho fica em 60% porque a união `sent` + `resolved`
mantém cinco registros mesmo com `EG0240-5` reaberto — ele saiu de `resolved`, mas continua em
`sent` (a transição de 07/10 está no histórico e o `DURING` a enxerga).

O mês acumula **5 envios** no critério do painel (união de `sent` e `resolved`), sendo
**3 classificados como retrabalho**:

| EPIC | Projeto | Due date | Enviado em | Retrabalho |
|---|---|---|---|---|
| `EG0275-112` | EG0275 | 2026-09-04 | 02/10 09:27 | não |
| `EG0241-42` | EG0241 | 2026-09-10 | 02/10 09:30 | sim |
| `EG0286-7` | EG0286 | 2026-10-01 | 02/10 13:40 | sim |
| `EG0240-5` | EG0240 | 2026-09-30 | 07/10 16:01 | sim — reaberto em 13/10 09:51 |
| `EG0239-28` | EG0239 | 2026-08-10 | 09/10 09:36 | não |

Quatro dos cinco eram entregas que vinham em atraso de meses anteriores; `EG0286-7` é a única
entrega com due date do próprio mês de outubro — e a única que conta no OTD até aqui.
`EG0239-28` aparece apenas por `resolved`: seu status (`Enviado - Aguardando Análise1`) não casa
a string exata usada pelas consultas `sent`/`rework`.

**Um EPIC em atraso acumulado** em outubro: `EG0240-5`, due date 30/09, de volta a `Em Revisão`
desde 13/10 às 09:51. O conjunto estivera vazio entre 09/10 e 13/10, porque os dois que
constavam até a rodada de 09/10 às 09:32 haviam saído — `EG0239-28` concluído em 09/10 às 09:36
e `EG0240-4` reprogramado de 10/09 para 16/10. `EG0240-5` entrou pelo caminho inverso: não por
due date nova, mas por ter perdido a conclusão que já tinha.

### Lookahead nov–dez/2026

34 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0256, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 23**, dos quais 21 têm due date entre 16 e 31/12.

A concentração de dezembro **mantém-se** no patamar alcançado na rodada de 08/10 às 11:31, com a chegada
do `EG0256-30` (19/12): dois terços do lookahead caem na segunda quinzena de dezembro.

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

- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T16:30:09-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (`window.__SNAPSHOT__` na posição 95.025 do `index.html`, contra 97.475 do
  `window.__HISTORY__` do artifact — ordem de execução confirmada).
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 16:30,
  seguido apenas de `</body></html>`.
- As **11 consultas JQL** do mês corrente e da visão acumulada foram reconstruídas exatamente
  como o artifact as monta e testadas contra os padrões gravados em `snapshot-data.js`: todas
  resolvem para o conjunto correto, sem *fallback* para lista vazia, e nenhum padrão ficou órfão
  (11 padrões para 11 conjuntos embutidos).
- Contagens dos conjuntos do mês corrente conferidas contra os arquivos de `_snap/`:
  `planned` 13, `overdue` 1, `lookahead` 34, `sent` 4, `resolved` 4, `rework` 3.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudou apenas o carimbo de geração.
- Nenhuma ocorrência de `avatarUrls`, `iconUrl`, `emailAddress` ou domínio de e-mail no arquivo
  publicado, e nenhuma URL da `api.atlassian.com` — a única URL da Atlassian é a base
  `https://projetos-engeplus.atlassian.net/browse/`, usada para montar os links dos EPICs. A
  única ocorrência da palavra `accountId` é o comentário do próprio gerador
  ("Nao contem accountIds").

---

## Publicação

O `index.html` e este `README.md` são gravados no *working tree* por esta rotina. O
`git commit`/`push` é feito separadamente pela tarefa `PR03-Auto-Push-GitHub` do Windows Task
Scheduler — que, pelo `.push-watchdog.log`, vem rodando a cada **10 minutos** — e o deploy no
Vercel segue o push.
