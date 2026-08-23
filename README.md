# PR.03 — Relatório de Indicadores de EPICs

Snapshot **estático** do dashboard PR.03 (Estudos e Projetos) da Engeplus Engenharia e Consultoria.

- **Última atualização:** 22/08/2026 23:11 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-22T23:11:14-03:00
- **Fonte:** Jira — projetos-engeplus.atlassian.net (issuetype de nível Epic)
- **Artifact de origem:** `pr03-relatorio-indicadores-epics`

## Como funciona

A página é gerada a partir do Live Artifact, com todas as consultas ao Jira **pré-executadas** e
embutidas em `window.__SNAPSHOT__`. O `window.cowork.callMcpTool` é substituído por um resolvedor
local que devolve os dados congelados conforme o padrão da JQL. **A página publicada não consulta
o Jira ao vivo.**

Tipos de issue de nível Epic considerados: `Epic` e `Fluxo de trabalho` (projetos team-managed).

## Conteúdo deste snapshot

| Visão | Dados |
|---|---|
| Julho/2026 (encerrado) | 10 previstos, 1 em atraso acumulado, 11 enviados (5 com retrabalho), 8 resolvidos, 27 na visão prospectiva |
| Agosto/2026 (mês corrente) | 14 previstos, 2 em atraso acumulado, 2 enviados, 4 resolvidos, 29 na visão prospectiva |
| Visão acumulada (Mar–Ago/2026) | previstos por mês; Abr/Mai/Jun vêm do histórico congelado no artifact |

13 consultas JQL + 1 listagem de projetos (19 projetos) resolvidas neste snapshot.

## Privacidade

Os dados publicados contêm apenas: chave da issue, título (summary), projeto, status, data
prevista, data de resolução e data de atualização. **Não** há accountIds, e-mails, avatares nem
responsáveis. Nomes de pessoas podem aparecer apenas se estiverem escritos no título de alguma
issue.

## Publicação

O commit e o push são feitos automaticamente pela tarefa `PR03-Auto-Push-GitHub`
(Windows Task Scheduler, a cada 30 minutos). O deploy no Vercel ocorre cerca de 1 minuto após o push.
