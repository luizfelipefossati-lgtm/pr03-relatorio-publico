# PR.03 — Relatório de Indicadores de EPICs

Snapshot **estático** do dashboard PR.03 (Estudos e Projetos) da Engeplus Engenharia e Consultoria.

- **Última atualização:** 23/08/2026 10:19 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-23T10:19:59-03:00
- **Fonte:** Jira — projetos-engeplus.atlassian.net (issuetype de nível Epic)
- **Artifact de origem:** `pr03-relatorio-indicadores-epics`

## Como funciona

A página é gerada a partir do Live Artifact, com todas as consultas ao Jira **pré-executadas** e
embutidas em `window.__SNAPSHOT__`. O `window.cowork.callMcpTool` é substituído por um resolvedor
local que devolve os dados congelados conforme o padrão da JQL. **A página publicada não consulta
o Jira ao vivo.**

Tipos de issue de nível Epic considerados: `Epic` e `Fluxo de trabalho` (projetos team-managed),
descobertos dinamicamente por `hierarchyLevel === 1`. Dos 19 projetos visíveis, 12 usam `Epic`,
5 usam `Fluxo de trabalho` e 2 (`EG0232`, `PE`) não possuem tipo de nível 1.

## Conteúdo deste snapshot

| Visão | Dados |
|---|---|
| Julho/2026 (encerrado) | 10 previstos, 1 em atraso acumulado, 11 enviados (5 com retrabalho), 8 resolvidos, 27 na visão prospectiva |
| Agosto/2026 (mês corrente) | 14 previstos, 2 em atraso acumulado, 2 enviados (2 com retrabalho), 4 resolvidos, 29 na visão prospectiva |
| Visão acumulada (Mar–Ago/2026) | previstos por mês; Mar (7) consultado nesta geração, Abr/Mai/Jun vêm do histórico congelado no artifact, Jul congelado neste snapshot, Ago do mês corrente |

13 consultas JQL + 1 listagem de projetos (19 projetos) embutidas neste snapshot.
Das 13, 8 correspondem às chamadas que a página realmente dispara ao abrir (1 listagem de
projetos + 6 de Agosto + 1 de Março no acumulado); as 6 de Julho ficam como fallback, já que
Julho é resolvido por `window.__HISTORY__["2026-07"]`.

## Notas desta geração

- Julho/2026 é período encerrado e foi congelado em `window.__HISTORY__["2026-07"]`
  (`_frozen_at: 2026-08-23`). Alterações no Jira após 2026-07-31 não afetam essa aba.
- As consultas prospectivas (`look`) de Julho e Agosto estouraram o limite de tokens do conector
  MCP em chamada única. Foram fatiadas em janelas de quinzena, cada fatia conferida pelo `webUrl`
  de retorno, e reconcatenadas em ordem de `duedate`. Como `ORDER BY duedate ASC` não define
  critério de desempate, a ordem entre issues com a mesma data pode diferir da consulta única —
  sem efeito sobre os indicadores.
- Todas as chamadas ao Jira foram feitas **sequencialmente** (nunca em paralelo) e validadas pelo
  `webUrl` da resposta, para evitar o problema conhecido de respostas cruzadas do conector.
- Checagens de coerência aplicadas: `retrabalho ⊆ enviados` (Jul: os 5 conjuntos coincidem) e
  `previstos do mês ⊆ visão prospectiva do mês anterior` (as 14 de Ago estão nas 27 de `look_2026-08`).
- Observações de dados do Jira, não corrigidas aqui (refletem o site): status com grafias
  divergentes — `Enviado - Aguardando Análise1`, `Enviado- Aguardando Análise` e `Em Revisã` —
  e o projeto `EG0280 - DMAE` cuja chave é `G0280`.
- `resolved<="YYYY-MM-DD"` é avaliado pelo Jira como 00:00 do último dia, então resoluções
  ocorridas ao longo do último dia do mês não entram na consulta `resolved`. Comportamento
  herdado do artifact, mantido para não divergir da versão ao vivo.

## Privacidade

Os dados publicados contêm apenas: chave da issue, título (summary), projeto, status, data
prevista, data de resolução e data de atualização. **Não** há accountIds, e-mails, avatares nem
responsáveis — verificado no HTML gerado. Nomes de pessoas podem aparecer apenas se estiverem
escritos no título de alguma issue.

## Publicação

O commit e o push são feitos automaticamente pela tarefa `PR03-Auto-Push-GitHub`
(Windows Task Scheduler, a cada 30 minutos). O deploy no Vercel ocorre cerca de 1 minuto após o push.
