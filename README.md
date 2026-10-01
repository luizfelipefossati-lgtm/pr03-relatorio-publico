# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 01/10/2026 11:30** (`2026-10-01T11:30:14-03:00`)

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
| `planned_2026-10` | Epics com due date em out/2026 | 27 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 4 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 18 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 0 |
| `resolved_2026-10` | Concluídos em out/2026 | 0 |
| `rework_2026-10` | Retrabalho em out/2026 | 0 |

Visão acumulada (`planned` por mês): mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8 · out/2026 = 27.

Os meses de **abr/2026 a jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026, ago/2026 e set/2026** são
congelados pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Geração em 01/10/2026 11:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

- **Virada de mês concluída.** Set/2026 está congelado (os 6 conjuntos foram gravados em
  30/09 às 23:29) e out/2026 é o mês ao vivo, com os 6 conjuntos reconsultados nesta rodada.
  Nenhuma alteração em relação à geração anterior (01/10 às 09:31): os números de outubro
  permanecem idênticos.
- Fonte do HTML: `_artifact_src.html` (87.509 bytes, md5 `6a2b6462a4efbec1890af4494a7f0b74`),
  cópia do artifact `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026.
  A pasta `Artifacts` **não** está montada nesta sessão — `connectedFolders` traz apenas
  `pr03-relatorio-publico` —, de modo que a cópia local é a fonte usada.
- Os **seis conjuntos de out/2026** foram consultados ao vivo, individualmente, com a projeção
  mínima de campos (`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`).
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.
- `getVisibleJiraProjects`: `_projects_min.json` de 30/09 reaproveitado — **21 projetos**,
  todas as chaves presentes nos conjuntos de outubro conferidas contra esse arquivo.

### Quadro de outubro/2026 (1º dia do mês)

27 epics com due date em outubro, nenhum ainda concluído — 14 em "Tarefas pendentes" e 13 em
andamento/revisão. Distribuição por projeto: EG0286 = 11 · EG0274 = 9 · G0280 = 5 · EG0256 = 2.
Como o mês acabou de começar, `sent`, `resolved` e `rework` estão vazios; é o esperado e eles se
preenchem ao longo do mês.

**4 EPICs em atraso acumulado** entram em outubro (eram 1 em setembro):

| EPIC | Projeto | Due date | Status |
|---|---|---|---|
| `EG0239-28` | EG0239 | 2026-08-10 | Em Revisão |
| `EG0275-112` | EG0275 | 2026-09-04 | Em Revisã |
| `EG0241-42` | EG0241 | 2026-09-10 | Em Revisão |
| `EG0240-5` | EG0240 | 2026-09-30 | Em Revisão |

Os três últimos venceram em setembro sem conclusão e migraram para o atraso acumulado na virada.

### Setembro/2026, agora congelado

Indicadores gravados em definitivo: **8 previstos**, **1 em atraso acumulado**, **8 envios**,
**3 de retrabalho**, **4 resoluções**, OTD **63% (5 de 8)**.

Como registrado na geração anterior, o fechamento carrega duas ressalvas conhecidas, preservadas
aqui sem correção porque espelham o comportamento do artifact ao vivo:

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

- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-01T11:30:14-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact (offsets 91.887
  contra 94.330): confirmado.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 01/10/2026 11:30.
- As **12 chamadas dinâmicas** do mês corrente e da visão acumulada foram testadas contra os
  padrões de JQL gravados em `snapshot-data.js`, reconstruindo as consultas exatamente como o
  artifact as monta: todas resolvem para o conjunto correto, sem *fallback* para lista vazia.
- Nenhuma ocorrência de `avatarUrls`, `iconUrl` ou e-mail no arquivo publicado. A única
  ocorrência da palavra `accountId` é o comentário do próprio gerador ("Nao contem accountIds").

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
