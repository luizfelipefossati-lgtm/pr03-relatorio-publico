# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 01/09/2026 19:29** (`2026-09-01T19:29:15-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **19**

### Consultas resolvidas (21 conjuntos + lista de projetos)

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

### O que mudou desde a geração anterior (01/09/2026 18:30)

- **Nenhuma alteração nos números.** Os 6 conjuntos de setembro/2026 foram reconsultados no Jira nesta geração e voltaram idênticos aos da geração das 18:30 — mesmas chaves, mesma ordem e mesmos carimbos `updated`: 22 previstos, 2 em atraso acumulado, 25 no lookahead, 0 envios, 0 concluídos, 0 com retrabalho.
- `sent_2026-09`, `resolved_2026-09` e `rework_2026-09` voltaram vazios do Jira (setembro acabou de começar).
- A lista de projetos visíveis **foi reconsultada** nesta geração via `getVisibleJiraProjects` e conferiu com o `_projects_min.json` existente (19 projetos; tipos de nível Epic `Epic` e `Fluxo de trabalho`), que por isso não precisou ser reescrito.
- Julho e agosto/2026 permanecem congelados com os mesmos números; os `planned` da Visão Acumulada (abr–set/2026) não foram alterados.
- Em relação ao arquivo anterior, mudaram apenas os carimbos de geração (comentário do `<head>`, cabeçalho do script, `generatedAt`, `console.log` e banner).

### Períodos cobertos

- **Julho/2026** — encerrado, congelado em 01/08/2026 (10 previstos, 0 em atraso acumulado, 11 envios na união `sent` + `resolved`, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — encerrado, congelado em 01/09/2026 (4 previstos, 0 em atraso acumulado, 6 envios, 3 com retrabalho, 39 entregas nos 60 dias seguintes).
- **Setembro/2026** — mês corrente, atualizado a cada geração do snapshot (22 previstos, 0 entregues até agora, 2 em atraso acumulado, 25 entregas nos próximos 60 dias).
- **Visão acumulada** — abril a setembro/2026, um conjunto `planned` por mês.

## Verificação desta geração

O `index.html` gerado foi carregado em navegador headless (Chromium/Playwright) antes da publicação:

- **Nenhuma requisição para a Atlassian** — percorrendo as três abas, o navegador emitiu 2 requisições no total: o próprio `index.html` e o `chart.js` do CDN (interceptado localmente). 0 requisições para `atlassian.net` ou qualquer host da Atlassian.
- **Nenhum aviso `[PR03] JQL sem correspondencia no snapshot`** no console — todos os 11 padrões de JQL resolveram.
- Console registra `[PR03] Snapshot estatico carregado - gerado em 2026-09-01T18:30:31-03:00; consultas ao Jira desativadas.`
- **0 erros de JavaScript** e nenhum recurso 404. Abas "Agosto 2026 — Encerrado", "Setembro 2026 — Ao vivo" e "Visão Acumulada — Histórico" presentes; nenhuma mensagem "Erro na inicialização"; seletor de projeto com "Todos" + os 19 projetos.
- Os `canvas` do dashboard (`c1`, `c2`, `c3` nas abas mensais e `chEvo`/`chBar` na Visão Acumulada) estão presentes e inicializados após o carregamento.
- Observação sobre o ambiente de verificação: o CDN do Chart.js não é alcançável pelo navegador do sandbox. O teste roda sobre o **`index.html` publicado, sem qualquer alteração**: a requisição do `chart.js@4.5.0` é interceptada e respondida com o arquivo real baixado do mesmo CDN, de modo que o `integrity` (SRI) da tag continua sendo validado pelo navegador e passa. No Vercel a tag carrega do CDN normalmente.
- As duas únicas menções a `atlassian.net` no HTML vêm do próprio artifact e não são requisições: o texto do rodapé ("Fonte: JIRA (projetos-engeplus.atlassian.net)") e a base dos links `browse/` usada quando se clica em um EPIC.

### Observação sobre a origem do HTML

Nesta execução a pasta do Live Artifact (`C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics`) **não estava montada na sessão** — a sessão só tinha acesso a este repositório. O snapshot foi gerado a partir de `_artifact_src.html`, cópia limpa do artifact idêntica (`diff` byte a byte) à última conferência com o artifact ao vivo em 31/08/2026. Enquanto a pasta do artifact seguir desconectada, alterações de layout feitas no Live Artifact não entram no snapshot — apenas os dados do Jira são atualizados.

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
