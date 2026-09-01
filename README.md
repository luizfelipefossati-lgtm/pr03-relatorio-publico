# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 01/09/2026 09:48** (`2026-09-01T09:48:33-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Virada de mês (setembro/2026)

Esta é a primeira geração após a virada de mês:

- **Agosto/2026 encerrou** e passou a ser o período congelado da aba "Encerrado".
- **Setembro/2026** é agora o mês corrente ("Ao vivo" no artifact, servido pelos dados do snapshot aqui).
- O gerador (`_gen_snapshot.py`) foi ajustado para congelar **todos** os meses anteriores que tenham os 6 conjuntos completos em `_snap/`, e não apenas o mês imediatamente anterior. Sem esse ajuste, julho/2026 sairia do `__HISTORY__` na virada e desapareceria da Visão Acumulada, porque o artifact traz embutidos apenas abr–jun/2026.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **19**

### Consultas resolvidas (18 conjuntos + lista de projetos)

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-07` | Epics com due date em jul/2026 | 10 |
| `overdue_2026-07` | Vencidos antes de jul/2026, não concluídos | 0 |
| `lookahead_2026-07` | Due date entre ago/2026 e set/2026 | 26 |
| `sent_2026-07` | Transições para "Enviado - Aguardando Análise" em jul/2026 | 5 |
| `resolved_2026-07` | Concluídos em jul/2026 | 8 |
| `rework_2026-07` | Retrabalho (saiu de "Enviado - Aguardando Análise") em jul/2026 | 5 |
| `planned_2026-08` | Epics com due date em ago/2026 | 4 |
| `overdue_2026-08` | Vencidos antes de ago/2026, não concluídos | 0 |
| `lookahead_2026-08` | Due date entre set/2026 e out/2026 | 39 |
| `sent_2026-08` | Transições para "Enviado - Aguardando Análise" em ago/2026 | 4 |
| `resolved_2026-08` | Concluídos em ago/2026 | 6 |
| `rework_2026-08` | Retrabalho em ago/2026 | 3 |
| `planned_2026-09` | Epics com due date em set/2026 | 22 |
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 2 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 25 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 0 |
| `resolved_2026-09` | Concluídos em set/2026 | 0 |
| `rework_2026-09` | Retrabalho em set/2026 | 0 |
| `planned_2026-04` | Epics com due date em abr/2026 (Visão Acumulada) | 15 |
| `planned_2026-05` | Epics com due date em mai/2026 (Visão Acumulada) | 7 |
| `planned_2026-06` | Epics com due date em jun/2026 (Visão Acumulada) | 1 |

Mais 1 chamada a `getVisibleJiraProjects` (19 projetos, 2 tipos de nível Epic).
Dos 21 conjuntos carregados, **11 vão embutidos** como `DATASETS` no JavaScript (apenas os alcançáveis por algum padrão de JQL: os 6 do mês corrente e os `planned` da Visão Acumulada). Os meses congelados viajam dentro de `__SNAPSHOT__.months` e nunca chegam a consultar o Jira.

### O que mudou desde a geração anterior (31/08/2026 14:36)

- **`planned_2026-08` caiu de 8 para 4 registros.** Quatro EPICs com due date 31/08 foram reprogramados para setembro e agora aparecem em `planned_2026-09`: `EG0240-43` (TOMO IV — Projeto de Instrumentação), `EG0240-4` (TOMO V — PRE), `EG0241-42` (TOMO V — PRE) e `EG0275-112` (Licenças Ambientais). Como agosto foi congelado nesta geração, o mês fecha com **4 previstos e OTD de 50%** (2 entregues, ambos com pequeno atraso) em vez dos 8 previstos que a versão anterior mostrava.
- **`overdue_2026-09` = 2**: `EG0286-8` (Estudo topográfico) e `EG0286-7` (Estudo de tráfego), ambos com due date 31/08/2026 e ainda em andamento — são as pendências acumuladas que setembro herda.
- `lookahead_2026-08` subiu de 35 para 39 registros; `lookahead_2026-09` (out–nov/2026) tem 25.
- `sent`, `resolved` e `rework` de setembro estão vazios: o mês tem um dia. Os conjuntos de agosto (4 / 6 / 3) foram reexecutados e conferem com o baseline anterior.
- Julho/2026 foi mantido congelado com os mesmos números da geração anterior (10 previstos, 11 envios, 5 com retrabalho).

### Períodos cobertos

- **Julho/2026** — encerrado, congelado em 01/08/2026 (10 previstos, 0 em atraso acumulado, 11 envios na união `sent` + `resolved`, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — encerrado, congelado em 01/09/2026 (4 previstos, 0 em atraso acumulado, 6 envios, 3 com retrabalho, 39 entregas nos 60 dias seguintes).
- **Setembro/2026** — mês corrente, atualizado a cada geração do snapshot (22 previstos, 2 em atraso acumulado, 0 concluídos até agora, 25 entregas nos próximos 60 dias).
- **Visão acumulada** — abril a setembro/2026, um conjunto `planned` por mês (72 previstos, 31 entregues, OTD acumulado 43%).

## Verificação desta geração

O `index.html` gerado foi carregado em navegador headless antes da publicação:

- Nenhuma requisição para `atlassian.net` ou qualquer host da Atlassian — a única chamada externa é o Chart.js em `cdn.jsdelivr.net`, que já faz parte do artifact.
- Nenhum aviso `[PR03] JQL sem correspondencia no snapshot` no console: todos os padrões resolveram.
- `__HISTORY__` com abr, mai, jun, jul e ago/2026; abas "Agosto 2026 — Encerrado" e "Setembro 2026 — Ao vivo" renderizando; Visão Acumulada abr–set/2026 carregando sem erro.

## Privacidade

Os dados embutidos passam por minimização antes de serem gravados. São mantidos apenas:

`key`, `summary`, `status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`, `updated`.

**Removidos:** `accountId`, e-mails, avatares, `iconUrl`, descrições em ADF, comentários, worklogs, dados de responsável (assignee/reporter) e demais metadados da API.
Nomes de pessoas podem, eventualmente, aparecer dentro de `summary` ou `status.name` — publicação aprovada pelo responsável pelo repositório.

## Arquivos

| Arquivo | Tamanho | Descrição |
|---|---:|---|
| `index.html` | 143,6 KB | Snapshot estático publicado (dados embutidos) |
| `snapshot-data.js` | 57,8 KB | Bloco de dados injetado (cópia avulsa, para inspeção) |
| `_artifact_src.html` | 85,5 KB | Cópia do artifact original, sem dados |
| `_snap/*.json` | — | Conjuntos minimais por mês, reutilizados entre gerações |
| `_gen_snapshot.py` | — | Gerador do snapshot |

## Publicação

O commit e o push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que verifica o working tree a cada 30 minutos. O deploy no Vercel ocorre cerca de 1 minuto após o push.
