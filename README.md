# PR.03 — Relatório de Indicadores de EPICs

Snapshot **estático** do Live Artifact "Pr03 Relatorio Indicadores Epics" (dashboard de OTD / indicadores de EPICs do Jira da Engeplus).

- **Última geração:** 05/08/2026 16:10 (BRT)
- **Origem dos dados:** Jira Cloud (projetos-engeplus.atlassian.net)
- **Natureza:** página offline — os dados estão congelados no momento da geração e **não** consultam o Jira ao vivo.

## Meses incluídos
- **Agosto/2026** (mês corrente / "ao vivo") — dados pré-buscados e congelados neste snapshot (16 previstos, 3 em atraso acumulado, 0 enviados no mês)
- **Julho/2026** (mês anterior / "encerrado") — dados pré-buscados e congelados neste snapshot (10 previstos, 1 em atraso, 11 enviados / 4 retrabalho)
- **Visão Acumulada** — Março a Agosto/2026 (Mar/Jul/Ago pré-buscados neste snapshot; Abr/Mai/Jun já congelados no próprio artifact)

## Como é atualizado
Um snapshot novo é gerado periodicamente por uma tarefa automatizada, que injeta os dados
pré-buscados no HTML (`window.__HISTORY__` + `window.__SNAPSHOT__`) e sobrescreve
`window.cowork.callMcpTool` para nunca consultar o Jira ao vivo. O `git commit + push` é feito
separadamente pela tarefa do Windows Task Scheduler `PR03-Auto-Push-GitHub` (a cada 30 min),
e o deploy é publicado pelo Vercel.

## Privacidade
Os dados publicados incluem apenas: chave do epic, título, status, projeto, due date, data de
resolução e data de atualização. `accountId`, e-mails e avatares dos responsáveis são removidos
na geração do snapshot.
