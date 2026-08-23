# PR.03 — Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Pr03 Relatorio Indicadores Epics** (Engeplus Engenharia — Estudos e Projetos).

- **Última atualização:** 23/08/2026 20:14 (America/Sao_Paulo)
- **Timestamp ISO:** `2026-08-23T20:14:25-03:00`
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como EPIC:** Epic, Fluxo de trabalho
- **Projetos visíveis:** 19

## O que é isto

Cópia estática (dados congelados) do Live Artifact. A página **não** consulta o Jira ao vivo:
`snapshot-data.js` substitui `window.cowork.callMcpTool` e devolve os dados pré-buscados
conforme o padrão da consulta JQL.

## Dados congelados neste snapshot

| Mês | Previstos | Atrasados (acum.) | Lookahead | Enviados | Resolvidos | Retrabalho |
|---|---|---|---|---|---|---|
| Março/2026 | 7 | 0 | 0 | 0 | 0 | 0 |
| Abril/2026 | 15 | 0 | 0 | 0 | 0 | 0 |
| Maio/2026 | 7 | 0 | 0 | 0 | 0 | 0 |
| Junho/2026 | 1 | 0 | 0 | 0 | 0 | 0 |
| Julho/2026 | 10 | 1 | 27 | 5 | 8 | 5 |
| Agosto/2026 | 14 | 2 | 29 | 2 | 4 | 2 |

Meses de março a junho/2026 têm apenas a série `planned`, usada pela **Visão Acumulada**.
Julho e agosto/2026 têm o conjunto completo de indicadores (abas mensais).

## Estrutura

- `index.html` — dashboard (cópia do artifact + injeção do snapshot)
- `snapshot-data.js` — dados congelados e desligamento das consultas ao vivo
- `vercel.json` — configuração de deploy

## Atualização

1. A tarefa agendada `deploy-pr03-vercel` regenera `index.html` e `snapshot-data.js`.
2. A tarefa do Windows Task Scheduler `PR03-Auto-Push-GitHub` (a cada 30 min) faz `git add/commit/push`.
3. O Vercel publica automaticamente ~1 min após o push.

## Privacidade

Os dados publicados contêm chaves e resumos de EPICs, nomes de projeto, datas e status.
Não contêm `accountId`, e-mails, avatares nem descrições de issues.
