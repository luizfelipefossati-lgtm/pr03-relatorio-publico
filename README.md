# PR.03 - Relatório de Indicadores de EPICs (Snapshot Público)

Página estática publicada automaticamente a partir do Live Artifact **"Pr03 Relatorio Indicadores Epics"** (dashboard Jira da Engeplus Engenharia).

- **Última atualização (snapshot):** 22/08/2026 10:15
- **Origem dos dados:** Jira Cloud (projetos de Estudos e Projetos)
- **Natureza:** dados **travados** no momento da geração — a página não consulta o Jira ao vivo.

## Como funciona a automação

1. Uma tarefa agendada gera este snapshot estático, pré-buscando via MCP os dados do mês corrente, mês anterior e visão acumulada. Os meses são injetados em `window.__HISTORY__` por `window.__SNAPSHOT__`, e a sobrescrita de `window.cowork.callMcpTool` serve `getVisibleJiraProjects` e qualquer consulta JQL residual offline (roteamento por padrão de JQL: planned, overdue, lookahead, sent/rework e resolved; vazio quando não houver dado pré-buscado).
2. A tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min) detecta as mudanças no working tree e faz `git commit + push` automaticamente.
3. O Vercel publica o novo `index.html` cerca de 1 minuto após o push.

## Conteúdo capturado neste snapshot

- Aba mensal **Agosto 2026** (mês corrente): 14 epics previstos, 2 entregues, 12 pendentes, 2 em atraso acumulado, 3 enviados/resolvidos no período (2 com retrabalho). OTD 14% — mês em curso, 7 dos 14 vencem em 31/08.
- Aba mensal **Julho 2026** (mês anterior, encerrado): 10 epics previstos, 8 entregues (5 no prazo, 3 com pequeno atraso), 1 em atraso acumulado, 11 enviados/resolvidos no período (7 com retrabalho), 27 no lookahead. OTD 80%.
- Próximos 2 meses (**Set–Out 2026**): 29 epics com vencimento previsto (lookahead de agosto).
- Visão **Acumulada** dos últimos 6 meses (Março–Agosto 2026): Mar 7 (OTD 43%), Abr 19 (84%), Mai 15 (27%), Jun 2 (50%), Jul 10 (80%) e Ago 14 (14%) epics previstos — 67 previstos e 34 entregues no período (OTD acumulado 51%).
- Projetos com epics previstos em agosto: EG0239, EG0240, EG0241, EG0275, EG0286 e EG0280 (`G0280`).
- Indicadores: OTD, previstos/entregues/pendentes, retrabalho e lookahead.
- Tipos de issue de nível Epic detectados no Jira: `Epic` e `Fluxo de trabalho` (19 projetos visíveis).

## Notas deste ciclo

- Os meses encerrados **Abril, Maio e Junho de 2026** são preservados congelados do artifact de origem (Abr 19, Mai 15 e Jun 2 epics previstos) e **não** são re-consultados ao vivo — períodos fechados não devem mudar.
- **Março 2026**, **Julho 2026** e **Agosto 2026** foram consultados nesta execução. Julho é reconsultado com corte histórico em 31/07 (`resolutiondate <= 31/07`), de modo que alterações posteriores no Jira não deslocam o OTD já fechado.
- A sobrescrita de `callMcpTool` foi ampliada para distinguir consultas de mês único (planned) de consultas de faixa de dois meses (lookahead), evitando que um lookahead receba dados de planned por engano.

## Privacidade

Os dados publicados incluem chaves e títulos de epics e nomes de status. Os JSONs de origem já excluem `accountId`, e-mails e avatares — verificado neste ciclo (0 ocorrências no payload). Publicação aprovada pelo usuário.

> Nota de qualidade de dado: o status `Em Revisã` (EG0275-6) é o nome real cadastrado no Jira — não é truncamento do snapshot.

_Gerado automaticamente. Não editar manualmente — as alterações são sobrescritas no próximo ciclo._
