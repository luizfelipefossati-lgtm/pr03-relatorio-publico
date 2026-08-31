# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 31/08/2026 03:37** (`2026-08-31T03:37:14-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **19**

### Consultas resolvidas (16)

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-03` | Epics com due date em mar/2026 | 7 |
| `planned_2026-04` | Epics com due date em abr/2026 | 15 |
| `planned_2026-05` | Epics com due date em mai/2026 | 7 |
| `planned_2026-06` | Epics com due date em jun/2026 | 1 |
| `planned_2026-07` | Epics com due date em jul/2026 | 10 |
| `planned_2026-08` | Epics com due date em ago/2026 | 8 |
| `overdue_2026-07` | Vencidos antes de jul/2026, não concluídos | 0 |
| `overdue_2026-08` | Vencidos antes de ago/2026, não concluídos | 0 |
| `lookahead_2026-07` | Due date entre ago/2026 e set/2026 | 26 |
| `lookahead_2026-08` | Due date entre set/2026 e out/2026 | 35 |
| `sent_2026-07` | Transições para "Enviado - Aguardando Análise" em jul/2026 | 5 |
| `sent_2026-08` | Transições para "Enviado - Aguardando Análise" em ago/2026 | 4 |
| `resolved_2026-07` | Concluídos em jul/2026 | 8 |
| `resolved_2026-08` | Concluídos em ago/2026 | 6 |
| `rework_2026-07` | Retrabalho (saiu de "Enviado - Aguardando Análise") em jul/2026 | 5 |
| `rework_2026-08` | Retrabalho (saiu de "Enviado - Aguardando Análise") em ago/2026 | 3 |

Mais 1 chamada a `getVisibleJiraProjects` (19 projetos, 2 tipos de nível Epic).

Nenhum conjunto mudou em relação à geração anterior — apenas o carimbo de tempo foi atualizado.

### Períodos congelados

- **Julho/2026** — período encerrado, dados travados no snapshot (10 previstos, 0 em atraso acumulado, 11 envios, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — mês corrente, atualizado a cada geração do snapshot (8 previstos, 2 entregues, 6 pendentes, 0 em atraso acumulado, OTD 25%, retrabalho 50%, 35 entregas nos próximos 60 dias).
- **Visão acumulada** — março a agosto/2026: 61 previstos, 34 entregues, OTD acumulado 56%.

## Privacidade

Os dados embutidos passam por minimização antes de serem gravados. São mantidos apenas:

`key`, `summary`, `status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`, `updated`.

**Removidos:** `accountId`, e-mails, avatares, `iconUrl`, descrições em ADF, comentários, worklogs, dados de responsável (assignee/reporter) e demais metadados da API.
Nomes de pessoas podem, eventualmente, aparecer dentro de `summary` ou `status.name` — publicação aprovada pelo responsável pelo repositório.

## Estrutura

| Arquivo | Função |
|---|---|
| `index.html` | Página publicada (artifact + dados estáticos + banner de snapshot) — 147,8 KB (151.363 bytes) |
| `snapshot-data.js` | Bloco de dados estáticos, também embutido no `index.html` |
| `_artifact_src.html` | Cópia do artifact original, sem os dados |
| `_projects_min.json` | Lista minimizada de projetos e tipos de issue |
| `_snap/` | JSONs minimais por consulta (insumo da geração) |
| `_gen_snapshot.py` | Gerador do snapshot (`_artifact_src.html` + `_snap/` → `index.html`) |
| `vercel.json` | Configuração de deploy |
| `auto-push.ps1`, `pr03-push-watchdog.ps1` | Automação de commit/push no Windows |

## Pipeline de atualização

1. A tarefa agendada **`deploy-pr03-vercel`** (Cowork) consulta o Jira, gera o snapshot e grava `index.html` + `README.md`.
2. A tarefa do Windows Task Scheduler **`PR03-Auto-Push-GitHub`** roda a cada 30 minutos, detecta alterações no working tree e faz `git add -A`, `commit` e `push`.
3. O **Vercel** publica automaticamente cerca de 1 minuto após o push.

A geração do snapshot e o push são etapas independentes: o agente nunca executa operações de git nem autentica no GitHub.

## Verificação desta geração

Executada antes de publicar:

- **Estrutura e faixas de data dos 16 conjuntos** — 16/16 OK. Cada registro validado quanto ao formato mínimo, ausência de chaves duplicadas, `statusCategory` válido e `duedate` / `resolutiondate` dentro da janela da consulta. `rework_*` confirmado como subconjunto de `sent_*` nos dois meses.
- **Renderização em navegador headless (Chromium)**, com o interceptador `window.cowork.callMcpTool` ativo, percorrendo **as três abas** (Julho/2026, Agosto/2026 e Visão Acumulada) — **nenhum aviso `JQL sem correspondencia`** e **nenhum erro de página**. Os 16 padrões casaram com todas as consultas emitidas pelo artifact.
- **Zero requisições para `api.atlassian.com`** durante a renderização completa.
- `getVisibleJiraProjects` interceptado retornando os 19 projetos e os tipos `Epic` / `Fluxo de trabalho` — OK (20 opções no filtro renderizado, incluindo "Todos").
- **KPIs renderizados a partir dos dados embutidos** — ago/2026: OTD 25%, 8 previstos, 2 entregues, 6 pendentes, 0 em atraso acumulado, retrabalho 50% (3/6). Visão acumulada: 61 previstos, 34 entregues, OTD 56%.
- **Preservação do mês congelado (`2026-07`)** contra a sobrescrita de `window.__HISTORY__` feita pelo artifact — OK.
- **Ausência de `accountId`, e-mails, avatares e `iconUrl`** nos datasets e no HTML final — OK (a única aparição da palavra "accountIds" é no comentário do próprio bloco de dados).
- **Posição do banner** de snapshot (imediatamente antes de `</body>`, não no topo do body) — OK.
- **Comentário `<!-- Snapshot gerado em ... -->`** no topo do `<head>` — OK.

**Não verificado nesta execução:** o carregamento do Chart.js (`cdn.jsdelivr.net/npm/chart.js@4.5.0`). O ambiente de verificação não tem acesso de rede a esse CDN, então os gráficos foram validados apenas quanto à ausência de erros de inicialização, com a biblioteca substituída por um stub. Os números dos KPIs, tabelas e heatmap — que não dependem do Chart.js — foram verificados normalmente.

## Observações da fonte de dados

- **Escopo de "Epic".** O artifact monta a consulta a partir dos tipos de issue com `hierarchyLevel === 1` retornados por `getVisibleJiraProjects` — hoje `Epic` e `Fluxo de trabalho`. Consultas restritas a `issuetype = Epic` subestimam todos os conjuntos, porque deixam de fora os projetos EG0285, EG0286, EG0287, EG0292 e CREA, que usam `Fluxo de trabalho`. Em ago/2026 isso corresponde a 2 de 8 previstos e 15 de 35 no lookahead.
- **Abril, maio e junho/2026 na Visão Acumulada vêm do `window.__HISTORY__` embutido no próprio artifact**, não das consultas deste snapshot — o snapshot só congela `2026-07`. Por isso o heatmap mostra 19 previstos em abr/2026 e 15 em mai/2026, enquanto uma consulta nova ao Jira hoje retorna 15 e 7. São recortes de momentos diferentes; se a intenção for realinhar, o histórico embutido no artifact precisa ser regerado.
- Existem variantes do nome do status de envio no Jira (`Enviado - Aguardando Análise`, `Enviado - Aguardando Análise1`, `Enviado- Aguardando Análise`). As consultas `sent_*` e `rework_*` usam o nome canônico, então itens com as variantes aparecem apenas em `resolved_*` — daí a diferença entre `sent` e o total de envios (jul/2026: 5 em `sent`, 11 na união com `resolved`; ago/2026: 4 e 6).
- Em jul/2026, `rework_2026-07` retornou exatamente o mesmo conjunto de `sent_2026-07`: todos os itens que entraram em "Enviado - Aguardando Análise" no período também saíram desse status em algum momento. Não é erro de consulta, mas convém validar a leitura do indicador de retrabalho. Em ago/2026 os conjuntos já divergem (3 de 4).
- `overdue_2026-07` e `overdue_2026-08` retornaram vazios: não há Epic com due date anterior ao início do mês ainda fora de `statusCategory=Done`. O último item em atraso acumulado era `EG0274-41` (Estudos Geotécnicos, due 25/03/2026), concluído em 30/08/2026 23:13.
- `EG0285-8` (due date 03/11/2026) aparece em `resolved_2026-08` por ter sido concluído em ago/2026, bem antes do prazo. `EG0274-43`, `EG0274-41` e `EG0274-38` também aparecem em `resolved_2026-08` com due date anterior (jul, mar e jul/2026) — entregas em atraso liquidadas no mês.
- O projeto "EG0280 - DMAE" tem a chave `G0280` no Jira (sem o `E` inicial); o valor é preservado como retornado pela API.
- **`_artifact_src.html` não pôde ser reconferido nesta execução**: a pasta do artifact (`Artifacts\pr03-relatorio-indicadores-epics`) não está entre as pastas conectadas à sessão. A geração usou a cópia local, de 24/08/2026. Se o Live Artifact tiver mudado depois disso, é preciso reconectar a pasta e atualizar `_artifact_src.html`.
