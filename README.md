# PR.03 - Relatório de Indicadores de EPICs (Snapshot Público)

Snapshot estático do dashboard PR.03 (Estudos e Projetos) gerado a partir do Live Artifact
**Pr03 Relatorio Indicadores Epics**, com dados do Jira (projetos-engeplus.atlassian.net) travados no momento da geração.

- **Última atualização:** 13/07/2026 17:07 (horário de Brasília)
- **Timestamp ISO:** 2026-07-13T17:07:34-03:00
- **Fonte:** JIRA — issuetype = Epic (todos os projetos, sem filtro por chave)
- **Abas:** Junho 2026 (encerrado), Julho 2026 (mês corrente na geração) e Visão Acumulada (Fev–Jul 2026)

As consultas JQL não filtram por projeto (só `issuetype = Epic` + `duedate`), portanto todos os projetos são sempre baixados e novos projetos entram automaticamente. O seletor de projetos é populado dinamicamente por `getVisibleJiraProjects` (17 projetos nesta geração). Um projeto só não aparece nos dados de um mês quando não possui epic com `duedate` naquele período.

A página não consulta o Jira ao vivo — todos os dados estão embutidos em `window.__SNAPSHOT__`.
Os meses encerrados (abr/mai/jun) permanecem congelados em `window.__HISTORY__` (mantido do artifact original); o mês corrente e demais meses da visão acumulada são servidos pelo snapshot.
Atualização automática do repositório a cada 30 min via tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler.

_Publicação de nomes de epics e responsáveis autorizada pelo usuário._
