# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 31/08/2026 02:32** (`2026-08-31T02:32:06-03:00`)

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

### Períodos congelados

- **Julho/2026** — período encerrado, dados travados no snapshot (10 previstos, 0 em atraso acumulado, 11 envios, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — mês corrente, atualizado a cada geração do snapshot (8 previstos, 0 em atraso acumulado, 6 envios, 3 com retrabalho, 35 entregas nos próximos 60 dias).
- **Visão acumulada** — março a agosto/2026.

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
| `_snap/` | JSONs minimais por consulta (insumo da geração) + `_load_all.py` (carga desta execução) e `_w.py` (minimização) |
| `_gen_snapshot.py` | Gerador do snapshot (`_artifact_src.html` + `_snap/` → `index.html`) |
| `vercel.json` | Configuração de deploy |
| `auto-push.ps1`, `pr03-push-watchdog.ps1` | Automação de commit/push no Windows |

## Pipeline de atualização

1. A tarefa agendada **`deploy-pr03-vercel`** (Cowork) consulta o Jira, gera o snapshot e grava `index.html` + `README.md`.
2. A tarefa do Windows Task Scheduler **`PR03-Auto-Push-GitHub`** roda a cada 30 minutos, detecta alterações no working tree e faz `git add -A`, `commit` e `push`.
3. O **Vercel** publica automaticamente cerca de 1 minuto após o push.

A geração do snapshot e o push são etapas independentes: o agente nunca executa operações de git nem autentica no GitHub.

## Verificação da geração

Esta execução validou, antes de publicar:

- as 16 consultas JQL retornaram registros dentro das faixas de data esperadas (`duedate` / `resolved`) — **16/16 OK**;
- renderização da página em navegador headless (Chromium), com o interceptador `window.cowork.callMcpTool` ativo — **sem nenhum aviso `JQL sem correspondencia`**, ou seja, os 16 padrões casaram com as consultas emitidas pelo artifact;
- `getVisibleJiraProjects` interceptado retornando os 19 projetos e os tipos `Epic` / `Fluxo de trabalho` — **OK** (os 19 projetos aparecem no filtro renderizado);
- KPIs renderizados a partir dos dados embutidos (ago/2026: OTD 25%, 8 previstos, 2 entregues, 6 pendentes, 0 em atraso acumulado, retrabalho 50%) — **OK**;
- preservação do mês congelado (`2026-07`) contra a sobrescrita de `window.__HISTORY__` feita pelo artifact — **OK**;
- ausência de `accountId`, e-mails, avatares e `iconUrl` nos datasets e no HTML final — **OK** (nenhuma ocorrência; a única aparição da palavra "accountIds" é no comentário do próprio bloco de dados);
- nenhuma referência a `api.atlassian.com` no HTML publicado — **OK** (0 ocorrências);
- posição do banner de snapshot (imediatamente antes de `</body>`, não no topo do body) — **OK** (linha 1025 de 1028);
- comentário `<!-- Snapshot gerado em ... -->` no topo do `<head>` — **OK** (1 ocorrência, linha 18).

## Observações da fonte de dados

- **Escopo de "Epic".** O artifact monta a consulta a partir dos tipos de issue com `hierarchyLevel === 1` retornados por `getVisibleJiraProjects` — hoje `Epic` e `Fluxo de trabalho`. Consultas restritas a `issuetype = Epic` subestimam todos os conjuntos, porque deixam de fora os projetos EG0285, EG0286, EG0287, EG0292 e CREA, que usam `Fluxo de trabalho`. Em ago/2026 isso corresponde a 2 de 8 previstos e 15 de 35 no lookahead.
- Existem variantes do nome do status de envio no Jira (`Enviado - Aguardando Análise`, `Enviado - Aguardando Análise1`, `Enviado- Aguardando Análise`). As consultas `sent_*` e `rework_*` usam o nome canônico, então itens com as variantes aparecem apenas em `resolved_*` — daí a diferença entre `sent` e o total de envios (jul/2026: 5 em `sent`, 11 na união com `resolved`; ago/2026: 4 e 6).
- Em jul/2026, `rework_2026-07` retornou exatamente o mesmo conjunto de `sent_2026-07`: todos os itens que entraram em "Enviado - Aguardando Análise" no período também saíram desse status em algum momento. Não é erro de consulta, mas convém validar a leitura do indicador de retrabalho. Em ago/2026 os conjuntos já divergem (3 de 4).
- `overdue_2026-07` e `overdue_2026-08` retornaram vazios: não há Epic com due date anterior ao início do mês ainda fora de `statusCategory=Done`. O último item em atraso acumulado era `EG0274-41` (Estudos Geotécnicos, due 25/03/2026), concluído em 30/08/2026 23:13.
- `EG0285-8` (due date 03/11/2026) aparece em `resolved_2026-08` por ter sido concluído em ago/2026, bem antes do prazo. `EG0274-43`, `EG0274-41` e `EG0274-38` também aparecem em `resolved_2026-08` com due date anterior (jul, mar e jul/2026) — entregas em atraso liquidadas no mês.
- O projeto "EG0280 - DMAE" tem a chave `G0280` no Jira (sem o `E` inicial); o valor é preservado como retornado pela API.
