# PR.03 - Relatório de Indicadores de EPICs (snapshot público)

Snapshot **estático** do dashboard PR.03 (Processo de Estudos e Projetos), gerado
automaticamente a partir do Live Artifact "Pr03 Relatorio Indicadores Epics".

- **Última geração:** 18/06/2026 14:31 (America/Sao_Paulo)
- **Fonte:** Jira (projetos-engeplus.atlassian.net), issuetype = Epic
- **Conteúdo:** os dados estão *travados* no momento da geração — a página publicada
  não consulta o Jira ao vivo. As chamadas dinâmicas (`searchJiraIssuesUsingJql` e
  `getVisibleJiraProjects`) foram substituídas por dados pré-buscados em
  `window.__SNAPSHOT__`, com `window.cowork.callMcpTool` sobrescrito.
- **Abas incluídas:** mês corrente (Junho/2026), mês anterior (Maio/2026 — congelado em
  `window.__HISTORY__`) e Visão Acumulada (Jan–Jun 2026).

## Privacidade
Os dados publicados incluem nomes de epics e podem incluir nome de responsáveis via
status. accountIds, avatares e e-mails foram removidos.

## Deploy
O push para o GitHub é feito automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub` (a cada 30 min). O deploy no Vercel ocorre ~1 min após o push.
