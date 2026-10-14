# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 14/10/2026 16:30** (`2026-10-14T16:30:45-03:00`)

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
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 | 33 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 4 | 4 |
| `resolved_2026-10` | Concluídos em out/2026 | 4 | 4 |
| `rework_2026-10` | Retrabalho em out/2026 | 3 | 3 |

Visão acumulada (`planned` por mês): mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8 · out/2026 = 13.

Os meses de **abr/2026 a jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026, ago/2026 e set/2026** são
congelados pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Geração em 14/10/2026 16:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum conjunto alterado nesta rodada

Sexta geração do dia, cerca de **uma hora** após a das 15:31. As **seis** consultas JQL do mês
corrente foram reexecutadas ao vivo com o predicado `issuetype in (Epic, "Fluxo de trabalho")`, e
**nenhuma mudou**:

| Conjunto | Ao vivo | Geração anterior | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 13 | 13 | mesmas chaves, mesma ordem |
| `overdue_2026-10` | 1 | 1 | mesmas chaves |
| `lookahead_2026-10` | 33 | 33 | mesmas chaves, mesma ordem |
| `sent_2026-10` | 4 | 4 | mesmas chaves, mesma ordem |
| `resolved_2026-10` | 4 | 4 | mesmas chaves, mesma ordem |
| `rework_2026-10` | 3 | 3 | mesmas chaves, mesma ordem |
| projetos visíveis | 21 | 21 | reaproveitado do disco (`_projects_min.json`) |

Os seis conjuntos do mês corrente foram regravados em `_snap/` a partir das respostas ao vivo e
conferidos por contagem contra os arquivos da geração anterior — `planned` 13, `overdue` 1,
`lookahead` 33, `sent` 4, `resolved` 4, `rework` 3 —, sem divergência. As seis respostas vieram
completas (`pageInfo.hasNextPage = false`), sem timeouts nem reexecuções. A igualdade dos dados
é confirmada do lado do artefato publicado: com os conjuntos reescritos do zero, o
`snapshot-data.js` saiu com os mesmos **75.248 bytes** e o `index.html` com os mesmos **163.034
bytes** da geração das 15:31, e o `window.__SNAPSHOT__` caiu no mesmo byte 94.719 — o que só
ocorre se o conteúdo embutido for idêntico, já que o carimbo de geração tem comprimento fixo.

A lista de projetos **não** foi reconsultada ao vivo nesta rodada: o `_projects_min.json` de
14/10 às 15:31 foi reaproveitado do disco, com os mesmos 21 projetos e os mesmos dois tipos de
nível Epic (`Epic` e `Fluxo de trabalho`).

Os seis arquivos do mês corrente em `_snap/` foram regravados com o mesmo conteúdo (o
`lookahead_2026-10.json` mudou apenas de formatação, de separadores compactos para espaçados, sem
efeito no JS embutido). O `_projects_min.json` não foi tocado, nem os meses congelados.

> **Pendência remanescente (menor).** O texto `issuetype=Epic` continua gravado no prompt da
> tarefa agendada, no passo que descreve as seis consultas. Ele não afeta a página publicada —
> o artifact monta o predicado dinamicamente a partir dos tipos de hierarquia 1 dos projetos
> visíveis —, mas faz cada rodada partir de uma consulta truncada e precisar corrigi-la à mão.
> Trocar aquele trecho do prompt por `issuetype in (Epic, "Fluxo de trabalho")` elimina o
> retrabalho — e é uma alteração no prompt da tarefa, que esta rotina não faz por conta própria.

> **Nota de publicação (14/10/2026, 16:30).** A cadeia de publicação está íntegra e esta
> geração **já foi publicada**: o `.push-watchdog.log` registra a passagem das 16:36, com
> `Commit OK: 5e72324` e `Push OK e VERIFICADO: HEAD sincronizado com origin/main`, logo após a
> das 16:25 (`2190818`). As passagens correm a cada ~10 minutos e todas as recentes concluíram
> com sucesso.

A **visão acumulada** (`planned_2026-05` a `planned_2026-10`) não foi reconsultada ao vivo nesta
rodada: outubro já é coberto pelo `planned_2026-10` acima, e maio a setembro são meses encerrados,
servidos tal como estão em `_snap/`. Julho, agosto e setembro são, além disso, **congelados** no
fechamento do período — divergem de propósito de uma consulta ao vivo, pelas reprogramações
posteriores ao fechamento (`EG0274-38` e `EG0274-43` saíram de julho para outubro; `EG0286-7`
saiu de agosto para outubro; `EG0240-4` saiu de setembro para 16/10). Pela regra de congelamento,
esses arquivos **não** são regravados: o histórico de OTD de cada mês continua refletindo o
que estava previsto no fechamento daquele mês.

Outubro segue com **um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e em
`Em Revisão` desde 13/10 às 09:51, sem movimento desde então. Os dois EPICs do EG0256
reprogramados para 2027 (`EG0256-28` em 29/01 e `EG0256-30` em 30/01) seguem fora de qualquer
conjunto de outubro.

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

- Os seis arquivos de out/2026 foram revalidados depois de gravados: todos parseiam como JSON,
  todos os registros têm exatamente as chaves `key` e `fields`, e `fields` exatamente os seis
  campos da projeção (`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`).
  Nenhuma ocorrência de `accountId`, `avatarUrls`, `emailAddress` ou de endereço de e-mail em
  qualquer deles.
- Os nomes de projeto gravados nos conjuntos são lidos do `_projects_min.json`, não digitados —
  checagem introduzida nesta rodada depois de um nome de projeto ter sido escrito à mão de forma
  incorreta na primeira tentativa de gravação (`EG0285`), corrigido antes da geração do HTML.
- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026. MD5
  `6a2b6462a4efbec1890af4494a7f0b74`, reconferido nesta rodada. O HTML ao vivo do Live Artifact
  **não** foi rebaixado aqui: a pasta `Artifacts` é uma **localização protegida** (dados internos
  do Claude) e não pode ser lida por caminho de arquivo a partir de uma sessão Cowork. A última
  conferência contra o artifact ao vivo, por *staging* de artifact (`device_stage_files` com
  `artifact_ids`) na rodada anterior, deu **MD5 idêntico**.
- As **11 consultas JQL** do mês corrente e da visão acumulada foram remontadas exatamente como
  o artifact as monta e testadas, uma a uma, contra os 11 padrões gravados em
  `snapshot-data.js`: cada consulta resolveu para o seu próprio conjunto, nenhuma caiu no
  *fallback* de lista vazia e nenhum padrão ficou órfão.
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.

### Quadro de outubro/2026 (14º dia do mês)

13 epics com due date em outubro — 12 em andamento/revisão (9 "Em andamento" + 3 "Em Revisão")
e 1 já enviado dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0274 = 2 · EG0240 = 1 · EG291 = 1.

Indicadores do mês na geração: **OTD 8%** (1 de 13), **retrabalho 60%** (3 de 5 envios),
**12 pendências do mês** e **1 em atraso acumulado**.

Os três indicadores repetem os das quatro gerações anteriores — e, com os seis conjuntos idênticos
em composição, repetem-se por identidade de dados, não por coincidência de contagem. O OTD
permanece em 8%: o único envio com due date de outubro continua sendo `EG0286-7`, e o denominador
segue em 13 desde a entrada de `EG0240-4`, reprogramado para 16/10. O retrabalho fica em 60%
porque a união `sent` + `resolved` mantém cinco registros mesmo com `EG0240-5` reaberto — ele saiu
de `resolved`, mas continua em `sent` (a transição de 07/10 está no histórico e o `DURING` a enxerga).

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

33 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 22**, dos quais 20 têm due date entre 16 e 31/12.

A composição é a mesma das gerações anteriores: o EG0256 segue sem representante no lookahead
desde a saída do `EG0256-30`, reprogramado para 30/01/2027. **20 dos 33 registros (61%)** caem na
segunda quinzena de dezembro — o gargalo de fim de ano permanece, concentrado em EG0274 e EG0286.

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

- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-14T16:30:45-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (`window.__SNAPSHOT__` no byte 94.719 do `index.html`, contra 97.169 do
  `window.__HISTORY__` do artifact — ordem de execução confirmada).
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 14/10/2026 16:30,
  seguido apenas de `</body></html>`. Ocorrência única no arquivo.
- As **11 consultas JQL** do mês corrente e da visão acumulada foram reconstruídas exatamente
  como o artifact as monta e testadas contra os padrões gravados em `snapshot-data.js`: todas
  resolvem para o conjunto correto, sem *fallback* para lista vazia, e nenhum padrão ficou órfão
  (11 padrões para 11 conjuntos embutidos).
- Contagens dos conjuntos do mês corrente conferidas contra os arquivos de `_snap/`:
  `planned` 13, `overdue` 1, `lookahead` 33, `sent` 4, `resolved` 4, `rework` 3.
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
