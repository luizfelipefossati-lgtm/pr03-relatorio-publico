# PR.03 - Relatório de Indicadores de EPICs (Snapshot Público)

Snapshot estático do dashboard PR.03 (Estudos e Projetos) gerado a partir do Live Artifact
**Pr03 Relatorio Indicadores Epics**, com dados do Jira (projetos-engeplus.atlassian.net) travados no momento da geração.

- **Última atualização:** 14/07/2026 12:14 (horário local da geração)
- **Timestamp ISO:** 2026-07-14T12:14
- **Fonte:** JIRA — issuetype = Epic (todos os projetos, sem filtro por chave)
- **Abas:** Junho 2026 (encerrado), Julho 2026 (mês corrente na geração) e Visão Acumulada (Fev–Jul 2026)

As consultas JQL não filtram por projeto (só `issuetype = Epic` + `duedate`), portanto todos os projetos são sempre baixados e novos projetos entram automaticamente. O seletor de projetos é populado dinamicamente por `getVisibleJiraProjects` (17 projetos nesta geração). Um projeto só não aparece nos dados de um mês quando não possui epic com `duedate` naquele período.

A página não consulta o Jira ao vivo — todos os dados estão embutidos em `window.__SNAPSHOT__` e `window.cowork.callMcpTool` é sobrescrito para devolvê-los offline. Consultas congeladas nesta geração: 1× `getVisibleJiraProjects` + 8 JQL do mês corrente/acumulado (Julho: planned 17, overdue 4, lookahead 6, sent 2, resolved 4, rework 2; acumulado planned Fev 1, Mar 5).
Os meses encerrados (abr/mai/jun) permanecem congelados em `window.__HISTORY__` (mantido do artifact original); o mês corrente (julho) e os demais meses da visão acumulada são servidos pelo snapshot.
Atualização automática do repositório a cada 30 min via tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler.

_Publicação de nomes de epics e responsáveis autorizada pelo usuário._
