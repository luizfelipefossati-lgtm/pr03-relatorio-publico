# PR.03 — Relatório de Indicadores de EPICs

Snapshot estático público do dashboard **Estudos e Projetos — Relatório de Indicadores** (Engeplus Engenharia e Consultoria).

- **Última atualização:** 22/08/2026 19:13 (America/Sao_Paulo)
- **Fonte:** Jira — `projetos-engeplus.atlassian.net` (issuetype de nível Epic)
- **Deploy:** Vercel (publicado a partir deste repositório)

## Como funciona

O `index.html` é uma cópia estática do Live Artifact `pr03-relatorio-indicadores-epics`. Todas as chamadas ao Jira foram
pré-resolvidas e embutidas na página (`window.__SNAPSHOT__`), portanto **a página não consulta o Jira ao vivo** — os dados
ficam travados no momento da geração.

## Conteúdo deste snapshot

| Aba | Período | Dados |
|---|---|---|
| Julho 2026 | encerrado | congelado (`window.__HISTORY__["2026-07"]`) |
| Agosto 2026 | mês corrente | previstos, em atraso, look-ahead, enviados, resolvidos, retrabalho |
| Visão Acumulada | mar/2026 – ago/2026 | previstos por mês |

Chamadas dinâmicas resolvidas neste snapshot: **13 queries JQL + 1 listagem de projetos (19 projetos)**.

## Privacidade

Os dados publicados contêm apenas: chave do EPIC, título, status, projeto, data prevista, data de resolução e data de
atualização. Não são publicados responsáveis, e-mails, `accountId`, avatares ou descrições de tickets.

## Atualização automática

1. Uma tarefa agendada do Cowork regenera este `index.html` a partir do artifact e dos dados do Jira.
2. A tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler detecta mudanças a cada 30 minutos e faz `commit` + `push`.
3. O Vercel publica automaticamente cerca de 1 minuto após o push.
