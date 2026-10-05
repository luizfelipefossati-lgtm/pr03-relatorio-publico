# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 05/10/2026 14:30** (`2026-10-05T14:30:11-03:00`)

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

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-10` | Epics com due date em out/2026 | 29 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 2 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 21 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 3 |
| `resolved_2026-10` | Concluídos em out/2026 | 3 |
| `rework_2026-10` | Retrabalho em out/2026 | 2 |

Visão acumulada (`planned` por mês): mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8 · out/2026 = 29.

Os meses de **abr/2026 a jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026, ago/2026 e set/2026** são
congelados pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Geração em 05/10/2026 14:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

- **Nenhuma mudança nos dados desde a geração anterior (05/10, 12:30 BRT).** Os seis conjuntos
  de out/2026 foram reconsultados ao vivo e vieram com exatamente as mesmas chaves e contagens:
  `planned` 29, `overdue` 2, `lookahead` 21, `sent` 3, `resolved` 3, `rework` 2. Nenhuma chave
  entrou ou saiu de nenhum conjunto. O epic `EG291-4` — "PEB - Plano de Execução BIM", que
  entrou na rodada das 09:59 — segue sendo a movimentação mais recente registrada no Jira.
  A saída desta rodada, portanto, difere da anterior apenas nos carimbos de data.
- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026.
  A pasta `Artifacts` consta entre as pastas conectadas, mas é uma **localização protegida**
  (dados internos do Claude): não pode ser listada nem lida a partir de uma sessão Cowork. Nesta
  rodada o HTML do Live Artifact foi obtido pela via própria de artifacts, e seu SHA-256
  (`2f09463c…ec2419`) confere com o de `_artifact_src.html` — confirmando que a cópia local
  continua idêntica ao artifact publicado.
- Os **seis conjuntos de out/2026** foram consultados ao vivo, individualmente, com a projeção
  mínima de campos (`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`).
  As respostas de `planned` e `lookahead` excederam o limite de tokens e foram reduzidas aos
  campos essenciais com `jq` sobre o arquivo salvo, conforme o procedimento previsto. Nenhuma
  consulta paginou (`hasNextPage` = false em todas). `resolved` retornou exatamente as mesmas
  três issues de `sent`, todas na categoria `done` com `resolutiondate` dentro de outubro.
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.
- `getVisibleJiraProjects`: **reconsultado ao vivo** nesta rodada — `total` = 21, `isLast` = true.
  O resultado foi reduzido à forma mínima e regravado em `_projects_min.json`: o arquivo saiu
  com os mesmos 5.536 bytes da versão anterior, ou seja, nenhuma mudança no cadastro de projetos. As 11 chaves que aparecem nos conjuntos de outubro
  (EG0239, EG0240, EG0241, EG0256, EG0274, EG0275, EG0285, EG0286, EG0294, EG291, G0280) constam
  todas nele — `EG291` já estava mapeado, de modo que o epic novo herda o nome correto do projeto
  sem necessidade de atualizar o arquivo. Os dois tipos de nível Epic seguem sendo `Epic` e
  `Fluxo de trabalho`.

### Quadro de outubro/2026 (5º dia do mês)

29 epics com due date em outubro — 14 em "Tarefas pendentes", 14 em andamento/revisão
(12 "Em andamento" + 2 "Em Revisão") e 1 já enviado dentro do próprio mês.
Distribuição por projeto: EG0286 = 11 · EG0274 = 10 · G0280 = 5 · EG0256 = 2 · EG291 = 1.

Indicadores do mês na geração: **OTD 3%** (1 de 29), **retrabalho 67%** (2 de 3 envios),
**28 pendências do mês** e **2 em atraso acumulado**. A queda do OTD de 4% para 3% é efeito
apenas do denominador — o epic novo aumenta a base de previstos sem alterar o numerador.

O mês acumula **3 envios**, sendo **2 classificados como retrabalho**:

| EPIC | Projeto | Due date | Enviado em | Retrabalho |
|---|---|---|---|---|
| `EG0275-112` | EG0275 | 2026-09-04 | 02/10 09:27 | não |
| `EG0241-42` | EG0241 | 2026-09-10 | 02/10 09:30 | sim |
| `EG0286-7` | EG0286 | 2026-10-01 | 02/10 13:40 | sim |

Os dois primeiros eram entregas que vinham em atraso de setembro; `EG0286-7` é a primeira
entrega com due date do próprio mês de outubro — e a única que conta no OTD até aqui.

**2 EPICs em atraso acumulado** permanecem em outubro:

| EPIC | Projeto | Due date | Status |
|---|---|---|---|
| `EG0239-28` | EG0239 | 2026-08-10 | Em Revisão |
| `EG0240-5` | EG0240 | 2026-09-30 | Em Revisão |

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

Checagens automatizadas desta rodada (`_snap/_verify1005f.py`), todas aprovadas:

- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-05T14:30:11-03:00` (linha 18).
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (linha 298 contra linha 363 de `index.html`).
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 05/10/2026 14:30,
  seguido apenas de `</body></html>`.
- As **12 consultas JQL** do mês corrente e da visão acumulada foram reconstruídas exatamente
  como o artifact as monta e testadas contra os padrões gravados em `snapshot-data.js`: todas
  resolvem para o conjunto correto, sem *fallback* para lista vazia, e nenhum padrão ficou órfão
  (11 padrões para 11 conjuntos embutidos).
- Contagens dos conjuntos do mês corrente conferidas contra os arquivos de `_snap/`:
  `planned` 29, `overdue` 2, `lookahead` 21, `sent` 3, `resolved` 3, `rework` 2.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e os dados vieram iguais aos da rodada anterior, de modo que a saída
  desta rodada difere daquela apenas nos carimbos de data.
- Nenhuma ocorrência de `avatarUrls`, `iconUrl`, `emailAddress` ou domínio de e-mail no arquivo
  publicado, e nenhuma URL da `api.atlassian.com`. A única ocorrência da palavra `accountId` é o
  comentário do próprio gerador ("Nao contem accountIds").
- **Recursos carregados** de host externo: apenas `cdn.jsdelivr.net` (Chart.js). A varredura de
  `src="http…"` não encontra nenhum outro.
- **Nenhuma chamada de rede no runtime**: zero ocorrências de `fetch(`, `XMLHttpRequest`,
  `EventSource` ou `sendBeacon` em todo o `index.html` — não há como a página consultar o Jira.
  As três menções a `projetos-engeplus.atlassian.net` vêm do artifact original e são inertes:
  o rótulo da fonte no rodapé, um comentário do gerador e a base `…/browse/` usada para montar
  os links clicáveis das chaves dos epics (`<a target="_blank">`, destino de clique, não
  requisição). A verificação estrutural foi ajustada nesta rodada para separar *recursos
  carregados* de *alvos de link*, que antes eram tratados como a mesma coisa e faziam a checagem
  acusar falha indevidamente sobre esses links herdados.
- `index.html` com 163.602 bytes (159,8 KB) em 1.028 linhas; `snapshot-data.js` com 75.816 bytes (74,0 KB).

## Abas disponíveis

- **Setembro 2026** — período encerrado, dados congelados no fechamento do período.
- **Outubro 2026** — mês corrente; os dados são os do instante da geração do snapshot.
- **Visão Acumulada** — mai/2026 a out/2026 (padrão: últimos 6 meses).

## Estrutura

| Arquivo | Função |
|---|---|
| `index.html` | Página publicada, auto-contida (HTML + dados + lógica). |
| `snapshot-data.js` | Cópia avulsa do bloco de dados embutido, para inspeção. |
| `_gen_snapshot.py`, `_snap/`, `_projects_min.json` | Insumos e gerador de execuções anteriores. |
| `auto-push.ps1`, `install-task.ps1` e afins | Automação local de commit/push no Windows. |

A única dependência externa da página é o Chart.js via CDN (`cdn.jsdelivr.net`), usado para os gráficos.

## Publicação

O commit e o push são feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub`, que verifica o working tree a cada 30 minutos.
O deploy no Vercel ocorre cerca de 1 minuto após o push.

## Privacidade

Os conjuntos de dados embutidos contêm apenas: chave do epic, resumo, status (nome e categoria),
projeto (chave e nome), due date, data de resolução e data de atualização.
**Não** incluem `accountId`, e-mails, avatares, descrições em ADF nem `iconUrl`.

## Observação sobre os status de envio

As consultas `sent` e `rework` casam exatamente a string `Enviado - Aguardando Análise`.
O Jira da organização possui variantes distintas desse status em alguns projetos
(`Enviado- Aguardando Análise`, `Enviado - Aguardando Análise1`), que **não** são contabilizadas
nessas consultas. Esse comportamento é o mesmo do artifact ao vivo e foi preservado no snapshot.
