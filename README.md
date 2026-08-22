# PR.03 - Relatório de Indicadores de EPICs (Snapshot Público)

Página estática publicada automaticamente a partir do Live Artifact **"Pr03 Relatorio Indicadores Epics"** (dashboard Jira da Engeplus Engenharia).

- **Última atualização (snapshot):** 22/08/2026 09:33
- **Origem dos dados:** Jira Cloud (projetos de Estudos e Projetos)
- **Natureza:** dados **travados** no momento da geração — a página não consulta o Jira ao vivo.

## Como funciona a automação

1. Uma tarefa agendada gera este snapshot estático, pré-buscando via MCP os dados do mês corrente, mês anterior e visão acumulada. Os meses são injetados em `window.__HISTORY__` por `window.__SNAPSHOT__`, e a sobrescrita de `window.cowork.callMcpTool` serve `getVisibleJiraProjects` e qualquer consulta JQL residual offline (fallback por mês; vazio quando não houver dado pré-buscado).
2. A tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min) detecta as mudanças no working tree e faz `git commit + push` automaticamente.
3. O Vercel publica o novo `index.html` cerca de 1 minuto após o push.

## Conteúdo capturado neste snapshot

- Aba mensal **Agosto 2026** (mês corrente, ao vivo → congelado): 14 epics previstos, 2 entregues, 12 pendentes, 2 em atraso acumulado, 4 enviados/resolvidos no período (2 com retrabalho). OTD 14% — mês em curso, 8 dos 14 vencem em 31/08.
- Aba mensal **Julho 2026** (mês anterior, encerrado): 10 epics previstos, 8 entregues, 1 em atraso acumulado, 11 enviados/resolvidos no período (5 com retrabalho), 27 no lookahead. OTD 80%.
- Próximos 2 meses (**Set–Out 2026**): 29 epics com vencimento previsto (lookahead de agosto).
- Visão **Acumulada** dos últimos 6 meses (Março–Agosto 2026): Mar 7 (OTD 43%), Abr 19 (84%), Mai 15 (27%), Jun 2 (50%), Jul 10 (80%) e Ago 14 (14%) epics previstos.
- Indicadores: OTD, previstos/entregues/pendentes, retrabalho e lookahead.
- Tipos de issue de nível Epic detectados no Jira: `Epic` e `Fluxo de trabalho` (19 projetos visíveis).

## Correção aplicada neste ciclo

Os meses encerrados **Abril, Maio e Junho de 2026** haviam sido sobrescritos em ciclos anteriores por consultas ao vivo, o que alterava indicadores já fechados (epics reagendados saem do mês). Este ciclo restaurou os valores **congelados** do artifact de origem: Abr 19, Mai 15 e Jun 2 epics previstos (antes: 15, 7 e 1). Períodos encerrados não devem ser re-consultados ao vivo.

## Privacidade

Os dados publicados incluem chaves e títulos de epics e nomes de status. Os JSONs de origem já excluem `accountId`, e-mails e avatares — verificado neste ciclo (0 ocorrências no HTML final). Publicação aprovada pelo usuário.

> Nota de qualidade de dado: o status `Em Revisã` (EG0275-6) é o nome real cadastrado no Jira — não é truncamento do snapshot.

_Gerado automaticamente. Não editar manualmente — as alterações são sobrescritas no próximo ciclo._
