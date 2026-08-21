# PR.03 - Relatório de Indicadores de EPICs (Snapshot Público)

Página estática publicada automaticamente a partir do Live Artifact **"Pr03 Relatorio Indicadores Epics"** (dashboard Jira da Engeplus Engenharia).

- **Última atualização (snapshot):** 21/08/2026 14:18
- **Origem dos dados:** Jira Cloud (projetos de Estudos e Projetos)
- **Natureza:** dados **travados** no momento da geração — a página não consulta o Jira ao vivo.

## Como funciona a automação

1. Uma tarefa agendada gera este snapshot estático, pré-buscando via MCP os dados do mês corrente, mês anterior e visão acumulada. As entradas completas dos dois meses recentes e os meses acumulados são congelados em `window.__HISTORY__`, e `window.__SNAPSHOT__` + a sobrescrita de `window.cowork.callMcpTool` servem `getVisibleJiraProjects` e qualquer consulta residual offline.
2. A tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min) detecta as mudanças no working tree e faz `git commit + push` automaticamente.
3. O Vercel publica o novo `index.html` cerca de 1 minuto após o push.

## Conteúdo capturado neste snapshot

- Aba mensal **Agosto 2026** (mês corrente, ao vivo → congelado): 14 epics previstos, 2 em atraso acumulado, 4 enviados/resolvidos para análise no período (2 com retrabalho).
- Aba mensal **Julho 2026** (mês anterior): congelado como entrada completa em `window.__HISTORY__` — 10 epics previstos, 1 em atraso acumulado, 11 enviados/resolvidos no período (5 com retrabalho), 27 no lookahead.
- Próximos 2 meses (**Set–Out 2026**): 29 epics com vencimento previsto (lookahead de agosto).
- Visão **Acumulada** dos últimos 6 meses (Março–Agosto 2026): Mar 7, Abr 15, Mai 7, Jun 1, Jul 10 e Ago 14 epics previstos.
- Indicadores: OTD, previstos/entregues/pendentes, retrabalho e lookahead.

## Privacidade

Os dados publicados incluem chaves e títulos de epics e nomes de status. Os JSONs de origem já excluem `accountId`, e-mails e avatares. Publicação aprovada pelo usuário.

_Gerado automaticamente. Não editar manualmente — as alterações são sobrescritas no próximo ciclo._
