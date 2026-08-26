# PR.03 — Relatório de Indicadores de EPICs

Publicação estática do painel **PR.03 — Estudos e Projetos / Relatório de Indicadores**, gerado a partir do Live Artifact `pr03-relatorio-indicadores-epics` e dos dados do Jira Cloud da Engeplus.

## Última atualização

- **Gerado em:** 26/08/2026 17:12 (America/São_Paulo)
- **Timestamp ISO:** `2026-08-26T17:12:12-03:00`
- **Fonte:** Jira Cloud `ead785de-33f3-4746-9bdb-a2a58cf5213b` (projetos-engeplus)
- **Projetos visíveis:** 19
- **Tipos de issue de nível Epic:** Epic, Fluxo de trabalho
- **Tamanho do `index.html`:** 140,7 KB

## O que é isto

O arquivo `index.html` é um **snapshot estático**: todas as chamadas ao Jira foram
pré-executadas no momento da geração e congeladas dentro da própria página
(`window.__SNAPSHOT__`). A página **não** consulta o Jira ao vivo — funciona
offline e pode ser publicada sem expor credenciais.

## Abas disponíveis

| Aba | Conteúdo |
|---|---|
| Julho 2026 | Mês encerrado — planejado, atrasados, enviados, retrabalho, look-ahead (congelado em `window.__HISTORY__`) |
| Agosto 2026 | Mês corrente — mesmos indicadores |
| Visão Acumulada | Histórico (padrão: últimos 6 meses, Março–Agosto 2026) |

## Conjuntos de dados congelados

| Dataset | Epics |
|---|---|
| `planned_2026-03` | 7 |
| `planned_2026-07` | 10 |
| `planned_2026-08` | 13 |
| `overdue_2026-07` | 1 |
| `overdue_2026-08` | 1 |
| `lookahead_2026-07` | 27 |
| `lookahead_2026-08` | 30 |
| `sent_2026-07` | 5 |
| `sent_2026-08` | 3 |
| `resolved_2026-07` | 8 |
| `resolved_2026-08` | 5 |
| `rework_2026-07` | 5 |
| `rework_2026-08` | 3 |

Abril, Maio e Junho de 2026 já vêm congelados dentro do próprio artifact
(`window.__HISTORY__`), com 19, 15 e 2 epics planejados respectivamente, e não
são reconsultados. Julho de 2026 foi congelado nesta geração (11 entregas
enviadas/resolvidas no período, 5 com retrabalho).

## Estrutura do repositório

| Arquivo | Descrição |
|---|---|
| `index.html` | Página publicada (snapshot estático, autocontido) |
| `snapshot-data.js` | Mesmos dados congelados em arquivo separado, para inspeção |
| `_artifact_src.html` | Cópia do Live Artifact usada como base da geração |
| `vercel.json` | Configuração de deploy |
| `*.ps1` | Scripts de automação (commit/push agendado no Windows) |

## Privacidade

Os dados publicados contêm apenas: chave da epic, resumo, nome e categoria do
status, chave e nome do projeto, data prevista, data de resolução e data de
atualização. **Não** há accountIds, e-mails, avatares ou conteúdo de comentários.

## Publicação

O commit e o push são feitos automaticamente pela tarefa `PR03-Auto-Push-GitHub`
do Windows Task Scheduler (a cada 30 minutos). O deploy no Vercel ocorre cerca de
1 minuto após o push.
