# PR.03 — Relatório de Indicadores de EPICs

Snapshot **estático** do dashboard PR.03 (Estudos e Projetos) da Engeplus Engenharia e Consultoria.

- **Última atualização:** 23/08/2026 09:47 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-23T09:47:58-03:00
- **Fonte:** Jira — projetos-engeplus.atlassian.net (issuetype de nível Epic)
- **Artifact de origem:** `pr03-relatorio-indicadores-epics`

## Como funciona

A página é gerada a partir do Live Artifact, com todas as consultas ao Jira **pré-executadas** e
embutidas em `window.__SNAPSHOT__`. O `window.cowork.callMcpTool` é substituído por um resolvedor
local que devolve os dados congelados conforme o padrão da JQL. **A página publicada não consulta
o Jira ao vivo.**

Tipos de issue de nível Epic considerados: `Epic` e `Fluxo de trabalho` (projetos team-managed),
descobertos dinamicamente por `hierarchyLevel === 1`.

## Conteúdo deste snapshot

| Visão | Dados |
|---|---|
| Julho/2026 (encerrado) | 10 previstos, 1 em atraso acumulado, 11 enviados (5 com retrabalho), 8 resolvidos, 27 na visão prospectiva |
| Agosto/2026 (mês corrente) | 14 previstos, 2 em atraso acumulado, 2 enviados (2 com retrabalho), 4 resolvidos, 29 na visão prospectiva |
| Visão acumulada (Mar–Ago/2026) | previstos por mês; Abr/Mai/Jun vêm do histórico congelado no artifact, Jul foi congelado neste snapshot |

13 consultas JQL + 1 listagem de projetos (19 projetos) resolvidas neste snapshot.

## Notas desta geração

- Julho/2026 fechou sem congelamento prévio no artifact, então foi congelado aqui em
  `window.__HISTORY__["2026-07"]`.
- A visão prospectiva (`look`) de Julho é gravada como **array** de issues. Snapshots anteriores
  gravavam apenas a contagem, o que quebrava o filtro de pendências dessa aba.
- O conector MCP do Jira devolveu, em chamadas paralelas, respostas cruzadas com JQL diferente da
  enviada. As consultas afetadas foram refeitas sequencialmente e conferidas contra
  `searchResultMode: "count"` e o `webUrl` de retorno. Checagens de coerência aplicadas:
  `retrabalho ⊆ enviados` e `previstos do mês ⊆ visão prospectiva do mês anterior`.

## Privacidade

Os dados publicados contêm apenas: chave da issue, título (summary), projeto, status, data
prevista, data de resolução e data de atualização. **Não** há accountIds, e-mails, avatares nem
responsáveis. Nomes de pessoas podem aparecer apenas se estiverem escritos no título de alguma
issue.

## Publicação

O commit e o push são feitos automaticamente pela tarefa `PR03-Auto-Push-GitHub`
(Windows Task Scheduler, a cada 30 minutos). O deploy no Vercel ocorre cerca de 1 minuto após o push.
