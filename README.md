# PR.03 - Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Estudos e Projetos — Relatório de Indicadores** (Engeplus Engenharia).

- **Última atualização:** 25/08/2026 09:15 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-25T09:15:00-03:00
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Publicação:** Vercel (deploy automático a cada push)

## O que é este arquivo

`index.html` é uma cópia **estática** do Live Artifact `pr03-relatorio-indicadores-epics`.
Todas as chamadas dinâmicas ao Jira foram pré-resolvidas e congeladas em `window.__SNAPSHOT__`.
A página **não consulta o Jira ao vivo** — o banner no rodapé indica a data de congelamento.

## Períodos congelados

| Aba | Período | Origem |
|---|---|---|
| Julho 2026 | 01/07 a 31/07/2026 | snapshot desta execução |
| Agosto 2026 | 01/08 a 31/08/2026 | snapshot desta execução |
| Visão Acumulada | Mar/2026 a Ago/2026 | Mar, Jul e Ago desta execução; Abr–Jun do histórico embutido |

## Consultas resolvidas nesta geração

- 1x `getVisibleJiraProjects` (19 projetos)
- Julho/2026: planned, overdue, lookahead, sent, resolved, rework
- Agosto/2026: planned, overdue, lookahead, sent, resolved, rework
- Março/2026: planned (visão acumulada)

## Privacidade

Os dados publicados contêm apenas chave do epic, resumo, status, projeto e datas.
Não há `accountId`, e-mail, avatar ou qualquer identificador pessoal de usuário do Jira.

## Pipeline

1. Tarefa agendada do Cowork gera o snapshot e grava `index.html` + `README.md`.
2. Tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min) faz `git add/commit/push`.
3. Vercel publica automaticamente ~1 min após o push.
