# PR.03 - Relatório de Indicadores de EPICs (Snapshot Público)

Snapshot estático do dashboard PR.03 (Estudos e Projetos) gerado a partir do Live Artifact
**Pr03 Relatorio Indicadores Epics**, com dados do Jira (projetos-engeplus.atlassian.net) travados no momento da geração.

- **Última atualização:** 17/07/2026 17:09 (horário local da geração)
- **Timestamp ISO:** 2026-07-17T20:09:20Z
- **Fonte:** JIRA — issuetype = Epic (todos os projetos, sem filtro por chave)
- **Abas:** Junho 2026 (encerrado), Julho 2026 (mês corrente na geração) e Visão Acumulada (Fev–Jul 2026)

As consultas JQL não filtram por projeto (só `issuetype = Epic` + `duedate`), portanto todos os projetos são sempre baixados e novos projetos entram automaticamente. O seletor de projetos é populado dinamicamente por `getVisibleJiraProjects` (17 projetos nesta geração). Um projeto só não aparece nos dados de um mês quando não possui epic com `duedate` naquele período.

A página não consulta o Jira ao vivo — todos os dados estão embutidos em `window.__HISTORY__` (Abr, Mai e Jun/2026 já congelados no fechamento de cada período) e `window.__SNAPSHOT__` (Julho corrente + Fev/Mar do acumulado); `window.cowork.callMcpTool` é sobrescrito para devolvê-los offline. Consultas ao vivo resolvidas nesta geração: 1× `getVisibleJiraProjects` + 8 JQL. Julho (corrente): planned 17, overdue 4, lookahead 6, sent 2, resolved 5 (união dedup = 5), rework 2. Visão acumulada ao vivo: Fev 1, Mar 5 (Abr 15, Mai 9 e Jun 2 vêm do `window.__HISTORY__`).

Atualização automática do repositório a cada 30 min via tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler.

_Publicação de nomes de epics e responsáveis autorizada pelo usuário._
