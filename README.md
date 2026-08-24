# PR.03 — Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Pr03 Relatorio Indicadores Epics** (Engeplus Engenharia — Estudos e Projetos).

- **Última atualização:** 24/08/2026 12:15 (America/Sao_Paulo)
- **Timestamp ISO:** `2026-08-24T12:15:03-03:00`
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como EPIC:** `Epic`, `Fluxo de trabalho` (hierarchyLevel = 1)
- **Projetos visíveis:** 19

## O que é isto

Cópia estática (dados congelados) do Live Artifact. A página **não** consulta o Jira ao vivo:
um bloco `<script>` injetado em `index.html` define `window.__SNAPSHOT__` e substitui
`window.cowork.callMcpTool`, devolvendo os dados pré-buscados conforme o padrão da consulta JQL.
Consultas fora do período congelado retornam vazio e registram aviso no console — nunca vão à rede.

## Dados congelados neste snapshot

| Mês | Previstos | Entregues | OTD | Atrasados (acum.) | Lookahead | Enviados | Retrabalho | Origem |
|---|---|---|---|---|---|---|---|---|
| Março/2026 | 7 | — | — | — | — | — | — | snapshot desta execução |
| Abril/2026 | 19 | — | — | 1 | 36 | 20 | 18 | congelado no artifact |
| Maio/2026 | 15 | — | — | 6 | 18 | 3 | 1 | congelado no artifact |
| Junho/2026 | 2 | — | — | 2 | — | 7 | 0 | congelado no artifact |
| Julho/2026 | 10 | 8 | 80% | 1 | 27 | 11 | 5 | snapshot desta execução |
| Agosto/2026 | 14 | 2 | 14% | 2 | 29 | 4 | 2 | snapshot desta execução |

- **Julho e Agosto/2026** (abas mensais) têm o conjunto completo de indicadores: `planned`,
  `overdue`, `lookahead`, `sent`, `resolved` e `rework`.
- **Março/2026** é o mês inicial da **Visão Acumulada** (padrão: últimos 6 meses); a visão
  acumulada usa apenas a série `planned`, que foi buscada nesta execução.
- **Abril a Junho/2026** são períodos encerrados cujos dados já vêm congelados no próprio
  artifact (`window.__HISTORY__`) e não são reconsultados.
- "Enviados" combina as séries `sent` e `resolved` do mês, deduplicadas por chave de issue —
  mesma regra usada pelo dashboard ao vivo.

## Consultas resolvidas nesta execução

| Chave | Registros |
|---|---|
| `planned\|2026-03` | 7 |
| `planned\|2026-07` | 10 |
| `overdue\|2026-07` | 1 |
| `look\|2026-07` | 27 |
| `sent\|2026-07` | 5 |
| `resolved\|2026-07` | 8 |
| `rework\|2026-07` | 5 |
| `planned\|2026-08` | 14 |
| `overdue\|2026-08` | 2 |
| `look\|2026-08` | 29 |
| `sent\|2026-08` | 2 |
| `resolved\|2026-08` | 4 |
| `rework\|2026-08` | 2 |

Mais 1 chamada `getVisibleJiraProjects` (19 projetos) — total de **14 chamadas MCP** resolvidas.

## Privacidade

Os JSONs embutidos contêm apenas `key`, `summary`, `status.name`, `status.statusCategory.key`,
`project.key`, `project.name`, `duedate`, `resolutiondate` e `updated`. Não há `accountId`,
avatares, e-mails, descrições (ADF) nem comentários. A publicação deste conteúdo foi
aprovada pelo responsável pelo repositório.

## Publicação

- `index.html` é servido estaticamente (Vercel, config em `vercel.json`).
- O commit e o push são feitos automaticamente pela tarefa do Windows Task Scheduler
  `PR03-Auto-Push-GitHub`, que roda a cada 30 minutos. A geração do snapshot **não** executa
  operações de git.
