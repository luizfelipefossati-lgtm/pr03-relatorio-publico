# PR.03 - Relatorio de Indicadores de EPICs (Engeplus)

Snapshot estatico publico do dashboard **PR.03 - Estudos e Projetos / Relatorio de Indicadores**,
gerado a partir do Live Artifact `pr03-relatorio-indicadores-epics` com dados do Jira
(`projetos-engeplus.atlassian.net`).

**Ultima atualizacao: 22/08/2026 15:11 (America/Sao_Paulo)**

## O que e

`index.html` e uma pagina autocontida. Todos os dados do Jira foram pre-buscados no
momento da geracao e injetados em `window.__SNAPSHOT__` / `window.__HISTORY__`.
A pagina **nao** consulta o Jira ao vivo - `window.cowork.callMcpTool` e substituido
por um stub que devolve os dados congelados conforme o padrao da query JQL.

## Conteudo do snapshot

| Aba | Periodo | Origem dos dados |
|---|---|---|
| Julho 2026 (Encerrado) | 01-31/07/2026 | congelado em `__HISTORY__["2026-07"]` |
| Agosto 2026 | 01-31/08/2026 | congelado via `__SNAPSHOT__.queries` |
| Visao Acumulada | Mar-Ago/2026 | `__HISTORY__` (04,05,06,07) + `__SNAPSHOT__` (03,08) |

Volumes desta geracao: julho/2026 - 10 previstos, 1 em atraso acumulado, 11 enviados
(5 com retrabalho), 27 no lookahead; agosto/2026 - 14 previstos, 2 em atraso acumulado,
2 enviados, 4 resolvidos, 29 no lookahead; marco/2026 - 7 previstos (serie acumulada).

Metricas: OTD (On Time Delivery), previstos/entregues/pendentes, atrasos acumulados,
retrabalho (reenvios), heatmap por projeto e lookahead de 2 meses.

## Publicacao

- Repositorio local: `C:\\Users\\DELL\\Documents\\Claude\\pr03-relatorio-publico`
- `git commit + push` automatico pela tarefa do Windows Task Scheduler `PR03-Auto-Push-GitHub` (a cada 30 min)
- Deploy no Vercel disparado pelo push (~1 min)

## Privacidade

Os dados publicados contem chaves e titulos de epics, nomes de projetos, datas e status.
Nao contem accountIds, e-mails, avatares nem descricoes/comentarios das issues.
Nomes de pessoas podem aparecer apenas se estiverem escritos no titulo de um epic.

---
Gerado automaticamente pela tarefa agendada `deploy-pr03-vercel`. Nao editar `index.html` a mao.
