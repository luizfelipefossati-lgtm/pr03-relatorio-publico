# PR.03 - Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Estudos e Projetos — Relatório de Indicadores** (Engeplus Engenharia).

- **Última atualização:** 25/08/2026 10:13 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-25T10:13:35-03:00
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Publicação:** Vercel (deploy automático a cada push)

## O que é este arquivo

`index.html` é uma cópia **estática** do Live Artifact `pr03-relatorio-indicadores-epics`.
Todas as chamadas dinâmicas ao Jira foram pré-resolvidas e congeladas em `window.__SNAPSHOT__`,
que também sobrescreve `window.cowork.callMcpTool`.
A página **não consulta o Jira ao vivo** — o banner no rodapé indica a data de congelamento.

## Períodos congelados

| Aba | Período | Origem |
|---|---|---|
| Julho 2026 | 01/07 a 31/07/2026 | snapshot desta execução |
| Agosto 2026 | 01/08 a 31/08/2026 | snapshot desta execução |
| Visão Acumulada | Mar/2026 a Ago/2026 | Mar, Jul e Ago desta execução; Abr–Jun do histórico embutido no artifact |

## Consultas resolvidas nesta geração

- 1x `getVisibleJiraProjects` (19 projetos; tipos de nível Epic: `Epic`, `Fluxo de trabalho`)
- **Julho/2026:** planned 10 · overdue 1 · lookahead 27 (ago–set) · sent 11 consolidados · retrabalho 5 · resolved 8
- **Agosto/2026:** planned 14 · overdue 1 · lookahead 29 (set–out) · sent 5 consolidados · retrabalho 3 · resolved 5
- **Março/2026:** planned 7 — visão acumulada
- Total de **13 padrões JQL** mapeados em `window.__SNAPSHOT__.jql`

## Privacidade

Os dados publicados contêm apenas chave do epic, resumo, status, projeto e datas.
Não há `accountId`, e-mail, avatar ou qualquer identificador pessoal de usuário do Jira
(verificado programaticamente na geração).

## Pipeline

1. Tarefa agendada do Cowork gera o snapshot e grava `index.html` + `README.md`.
2. Tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min) faz `git add/commit/push`.
3. Vercel publica automaticamente ~1 min após o push.
