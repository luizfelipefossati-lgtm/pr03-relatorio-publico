# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 27/08/2026 16:14** (`2026-08-27T16:14:35-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **19**

### Consultas resolvidas (16)

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-03` | Epics com due date em mar/2026 | 7 |
| `planned_2026-04` | Epics com due date em abr/2026 | 15 |
| `planned_2026-05` | Epics com due date em mai/2026 | 7 |
| `planned_2026-06` | Epics com due date em jun/2026 | 1 |
| `planned_2026-07` | Epics com due date em jul/2026 | 10 |
| `planned_2026-08` | Epics com due date em ago/2026 | 13 |
| `overdue_2026-07` | Vencidos antes de jul/2026, não concluídos | 1 |
| `overdue_2026-08` | Vencidos antes de ago/2026, não concluídos | 1 |
| `lookahead_2026-07` | Due date entre ago/2026 e set/2026 | 27 |
| `lookahead_2026-08` | Due date entre set/2026 e out/2026 | 30 |
| `sent_2026-07` | Transições para "Enviado - Aguardando Análise" em jul/2026 | 5 |
| `sent_2026-08` | Transições para "Enviado - Aguardando Análise" em ago/2026 | 3 |
| `resolved_2026-07` | Concluídos em jul/2026 | 8 |
| `resolved_2026-08` | Concluídos em ago/2026 | 5 |
| `rework_2026-07` | Retrabalho (saiu de "Enviado - Aguardando Análise") em jul/2026 | 5 |
| `rework_2026-08` | Retrabalho (saiu de "Enviado - Aguardando Análise") em ago/2026 | 3 |

### Períodos congelados

- **Julho/2026** — período encerrado, dados travados no snapshot (10 previstos, 1 em atraso acumulado, 11 envios, 5 com retrabalho).
- **Agosto/2026** — mês corrente, atualizado a cada geração do snapshot.
- **Visão acumulada** — março a agosto/2026.

## Privacidade

Os dados embutidos passam por minimização antes de serem gravados. São mantidos apenas:

`key`, `summary`, `status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`, `updated`.

**Removidos:** `accountId`, e-mails, avatares, `iconUrl`, descrições em ADF, dados de responsável (assignee/reporter) e demais metadados da API.
Nomes de pessoas podem, eventualmente, aparecer dentro de `summary` ou `status.name` — publicação aprovada pelo responsável pelo repositório.

## Estrutura

| Arquivo | Função |
|---|---|
| `index.html` | Página publicada (artifact + dados estáticos + banner de snapshot) |
| `snapshot-data.js` | Bloco de dados estáticos, também embutido no `index.html` |
| `_artifact_src.html` | Cópia do artifact original, sem os dados |
| `_projects_min.json` | Lista minimizada de projetos e tipos de issue |
| `_snap/` | JSONs minimais por consulta (insumo da geração) |
| `vercel.json` | Configuração de deploy |
| `auto-push.ps1`, `pr03-push-watchdog.ps1` | Automação de commit/push no Windows |

## Pipeline de atualização

1. A tarefa agendada **`deploy-pr03-vercel`** (Cowork) consulta o Jira, gera o snapshot e grava `index.html` + `README.md`.
2. A tarefa do Windows Task Scheduler **`PR03-Auto-Push-GitHub`** roda a cada 30 minutos, detecta alterações no working tree e faz `git add -A`, `commit` e `push`.
3. O **Vercel** publica automaticamente cerca de 1 minuto após o push.

A geração do snapshot e o push são etapas independentes: o agente nunca executa operações de git nem autentica no GitHub.
