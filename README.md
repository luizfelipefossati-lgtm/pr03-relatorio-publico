# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 07/10/2026 17:30** (`2026-10-07T17:30:54-03:00`)

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
| `planned_2026-10` | Epics com due date em out/2026 | **14** | 15 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 2 | 2 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | **33** | 32 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 4 | 4 |
| `resolved_2026-10` | Concluídos em out/2026 | 4 | 4 |
| `rework_2026-10` | Retrabalho em out/2026 | 3 | 3 |

Visão acumulada (`planned` por mês): mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8 · out/2026 = 14.

Os meses de **abr/2026 a jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026, ago/2026 e set/2026** são
congelados pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Geração em 07/10/2026 17:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Reprogramação do `EG0286-22` — única alteração desta rodada

Às **16:39 BRT de hoje (07/10)**, depois da geração anterior (16:30 BRT), o epic
**`EG0286-22`** (projeto EG0286 - DNIT/AC), que estava em "Tarefas pendentes" com due date de
outubro, foi **reprogramado para 31/12/2026**. Com isso ele troca de conjunto:

| Conjunto | Antes | Agora | Efeito |
|---|---:|---:|---|
| `planned_2026-10` | 15 | **14** | `EG0286-22` sai do previsto de outubro |
| `lookahead_2026-10` | 32 | **33** | `EG0286-22` entra na janela nov–dez/2026 |

Os conjuntos `overdue_2026-10`, `sent_2026-10`, `resolved_2026-10`, `rework_2026-10` e a lista de
projetos ficaram **idênticos** à geração anterior, conferidos por hash canônico campo a campo.
A entrega do `EG0240-5` registrada às 16:01 segue refletida nos números de envio.

Esta é uma mudança de **planejamento**, não de entrega.

### Demais conferências

- Cada um dos seis conjuntos de out/2026 foi coletado em **uma única consulta** nesta rodada,
  com a projeção mínima de campos (`summary`, `status`, `project`, `duedate`, `resolutiondate`,
  `updated`) e `pageInfo.hasNextPage = false` em todas. As respostas de `lookahead` e de
  `getVisibleJiraProjects` excederam o limite de tokens e foram reduzidas aos campos essenciais
  sobre o arquivo salvo pelo runtime, conforme o procedimento previsto; as demais couberam inline.
- A comparação com a geração anterior usa hash canônico campo a campo (`summary`, `status.name`,
  `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`,
  `updated`), insensível à ordem dos registros.
- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026. MD5
  `6a2b6462a4efbec1890af4494a7f0b74`, o mesmo das rodadas anteriores.
  A pasta `Artifacts` segue sendo uma **localização protegida** (dados internos do Claude) e não
  pode ser lida por caminho de arquivo a partir de uma sessão Cowork. Nesta rodada, como nas
  anteriores, o HTML ao vivo do Live Artifact foi obtido pela via de *staging* de artifact
  (`device_stage_files` por `artifact_ids`, 87.509 bytes) e conferido contra a cópia versionada:
  **idêntico, byte a byte**.
- `getVisibleJiraProjects`: **reconsultado ao vivo** — `total` = 21, `isLast` = true. Reduzido à
  mesma forma mínima e comparado por hash canônico contra `_projects_min.json`: idêntico, o
  arquivo não precisou ser reescrito. Os dois tipos de nível Epic seguem sendo `Epic` e
  `Fluxo de trabalho`.
- **Filtro de tipo de item.** As consultas desta rodada usaram
  `issuetype in ("Epic","Fluxo de trabalho")`, que é o que o artifact de fato monta: ele
  parte de `epicTypes=['Epic']` apenas como padrão e substitui a lista pelos tipos de
  hierarquia 1 descobertos nos projetos visíveis. Rodar com o literal `issuetype=Epic`
  (como está escrito, de forma simplificada, no prompt da tarefa agendada) deixaria de fora
  os epics de EG0286 e EG291, que nomeiam esse nível como `Fluxo de trabalho`. **Convém alinhar
  o texto do prompt agendado ao filtro real** — a ressalva se repete desde rodadas anteriores.
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.

### Quadro de outubro/2026 (7º dia do mês)

14 epics com due date em outubro — 13 em andamento/revisão (11 "Em andamento" + 2 "Em Revisão")
e 1 já enviado dentro do próprio mês. Não há mais nenhum em "Tarefas pendentes" no mês, depois
da reprogramação do `EG0286-22`.
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0274 = 2 · EG0256 = 2 · EG291 = 1.

Indicadores do mês na geração: **OTD 7%** (1 de 14), **retrabalho 75%** (3 de 4 envios),
**13 pendências do mês** e **2 em atraso acumulado**.

O OTD permanece arredondado em 7%: o único envio com due date de outubro continua sendo
`EG0286-7`, e a saída do `EG0286-22` apenas reduz o denominador de 15 para 14. O retrabalho fica
em 75%, sem alteração nos envios.

O mês acumula **4 envios**, sendo **3 classificados como retrabalho**:

| EPIC | Projeto | Due date | Enviado em | Retrabalho |
|---|---|---|---|---|
| `EG0275-112` | EG0275 | 2026-09-04 | 02/10 09:27 | não |
| `EG0241-42` | EG0241 | 2026-09-10 | 02/10 09:30 | sim |
| `EG0286-7` | EG0286 | 2026-10-01 | 02/10 13:40 | sim |
| `EG0240-5` | EG0240 | 2026-09-30 | 07/10 16:01 | sim |

Três dos quatro eram entregas que vinham em atraso de setembro; `EG0286-7` é a única entrega com
due date do próprio mês de outubro — e a única que conta no OTD até aqui.

**2 EPICs em atraso acumulado** permanecem em outubro, sem alteração:

| EPIC | Projeto | Due date | Status |
|---|---|---|---|
| `EG0239-28` | EG0239 | 2026-08-10 | Em Revisão |
| `EG0240-4` | EG0240 | 2026-09-10 | Em Revisão |

### Lookahead nov–dez/2026

33 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 22**, dos quais 20 têm due date entre 16 e 31/12 — concentração herdada da
reprogramação registrada na rodada das 15:32 e reforçada hoje pelo `EG0286-22` (31/12).

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

- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-07T17:30:54-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (linha 283 contra linha 374 de `index.html`).
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 07/10/2026 17:30,
  seguido apenas de `</body></html>`.
- As **11 consultas JQL** do mês corrente e da visão acumulada foram reconstruídas exatamente
  como o artifact as monta e testadas contra os padrões gravados em `snapshot-data.js`: todas
  resolvem para o conjunto correto, sem *fallback* para lista vazia, e nenhum padrão ficou órfão
  (11 padrões para 11 conjuntos embutidos).
- Contagens dos conjuntos do mês corrente conferidas contra os arquivos de `_snap/`:
  `planned` 14, `overdue` 2, `lookahead` 33, `sent` 4, `resolved` 4, `rework` 3.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e apenas os dados de `planned`/`lookahead` e o carimbo mudaram.
- Nenhuma ocorrência de `avatarUrls`, `iconUrl`, `emailAddress` ou domínio de e-mail no arquivo
  publicado, e nenhuma URL da `api.atlassian.com`. A única ocorrência da palavra `accountId` é o
  comentário do próprio gerador ("Nao contem accountIds").

---

## Publicação

O `index.html` e este `README.md` são gravados no *working tree* por esta rotina. O
`git commit`/`push` é feito separadamente pela tarefa `PR03-Auto-Push-GitHub` do Windows Task
Scheduler, a cada 30 minutos, e o deploy no Vercel segue o push.
