# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 00:13 (2026-08-27T00:13:11-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue considerados como Epic:** Epic, Fluxo de trabalho
- **Projetos visiveis no snapshot:** 19

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

## Conteudo do snapshot

| Conjunto | Registros |
|---|---|
| `planned_2026-08` | 13 |
| `overdue_2026-08` | 1 |
| `lookahead_2026-08` | 30 |
| `sent_2026-08` | 3 |
| `resolved_2026-08` | 5 |
| `rework_2026-08` | 3 |
| `planned_2026-07` | 10 |
| `overdue_2026-07` | 1 |
| `lookahead_2026-07` | 27 |
| `sent_2026-07` | 5 |
| `resolved_2026-07` | 8 |
| `rework_2026-07` | 5 |
| `planned_2026-03` | 7 |
| `planned_2026-04` | 15 |
| `planned_2026-05` | 7 |
| `planned_2026-06` | 1 |

Mes encerrado de **Julho/2026** congelado em `window.__HISTORY__` para exibir os dados
reais do periodo em vez do aviso de "sem snapshot".

## Privacidade

Os dados embutidos contem apenas: chave da issue, resumo, status, projeto, data de
entrega, data de resolucao e data de atualizacao. **Nao ha** accountIds, e-mails,
avatares nem descricoes.

## Publicacao

O commit e o push para o GitHub sao feitos automaticamente pela tarefa do Windows
Task Scheduler `PR03-Auto-Push-GitHub` (a cada 30 minutos). O deploy no Vercel ocorre
cerca de 1 minuto apos o push.
