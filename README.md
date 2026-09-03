# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 03/09/2026 17:30** (`2026-09-03T17:30:17-03:00`)

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
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 1 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 25 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 1 |
| `resolved_2026-09` | Concluídos em set/2026 | 1 |
| `rework_2026-09` | Retrabalho em set/2026 | 0 |
| `planned_2026-04` | Epics com due date em abr/2026 (Visão Acumulada) | 15 |
| `planned_2026-05` | Epics com due date em mai/2026 (Visão Acumulada) | 7 |
| `planned_2026-06` | Epics com due date em jun/2026 (Visão Acumulada) | 1 |

Mais 1 chamada a `getVisibleJiraProjects` (19 projetos, 2 tipos de nível Epic).
Dos 21 conjuntos carregados, **11 vão embutidos** como `DATASETS` no JavaScript (apenas os alcançáveis por algum padrão de JQL: os 6 do mês corrente e os `planned` da Visão Acumulada). Os meses congelados viajam dentro de `__SNAPSHOT__.months` e nunca chegam a consultar o Jira.

### O que mudou desde a geração anterior (03/09/2026 16:30)

- **Primeira entrega de setembro/2026 registrada.** O EPIC `EG0286-7` — *Estudo de tráfego* (EG0286 - DNIT/AC) — passou para **"Enviado - Aguardando Análise"** em **03/09/2026 16:50**, com `resolutiondate` na mesma data. Era um dos dois EPICs em atraso acumulado.
- Consequências nos conjuntos de setembro: `sent_2026-09` **0 → 1**, `resolved_2026-09` **0 → 1**, `overdue_2026-09` **2 → 1**. `rework_2026-09` segue em **0** (o EPIC não saiu do status de envio).
- O atraso acumulado agora tem **um único** EPIC: `EG0286-8` — *Estudo topográfico*, due date 31/08/2026, ainda "Em andamento".
- `planned_2026-09` (22) e `lookahead_2026-09` (25) foram reconsultados e conferiram **chave por chave** com os JSONs de `_snap/` — mesmos status, categorias, due dates, `resolutiondate` e `updated`. Reaproveitados sem alteração.
- Como `EG0286-7` tem due date em 31/08/2026, ele **não entra** no "Previstos" de setembro: o OTD do mês segue em 0% sobre os 22 previstos, e a entrega aparece no painel de envios.
- A lista de projetos visíveis foi reconsultada (`getVisibleJiraProjects`, 19 projetos) e confere chave por chave com o `_projects_min.json` do repositório, reaproveitado sem alteração. Tipos de nível Epic: `Epic` e `Fluxo de trabalho`.
- Julho e agosto/2026 permanecem congelados com os mesmos números; os `planned` da Visão Acumulada (abr–set/2026) não foram alterados.
- A pasta do Live Artifact (`Artifacts\pr03-relatorio-indicadores-epics`) **não estava montada** nesta sessão; o snapshot foi gerado a partir do `_artifact_src.html` versionado no repositório, portanto sem revalidação contra o artifact ao vivo.

### Períodos cobertos

- **Julho/2026** — encerrado, congelado em 01/08/2026 (10 previstos, 0 em atraso acumulado, 11 envios na união `sent` + `resolved`, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — encerrado, congelado em 01/09/2026 (4 previstos, 0 em atraso acumulado, 6 envios, 3 com retrabalho, 39 entregas nos 60 dias seguintes).
- **Setembro/2026** — mês corrente, atualizado a cada geração do snapshot (22 previstos, 1 envio registrado, 1 em atraso acumulado, 25 entregas nos próximos 60 dias).
- **Visão acumulada** — abril a setembro/2026, um conjunto `planned` por mês.

## Verificação desta geração

O `index.html` gerado foi carregado em navegador headless (Chromium/Playwright), sem qualquer alteração no arquivo publicado, percorrendo as três abas:

- **Nenhuma requisição para a Atlassian.** O navegador emitiu 2 requisições no total: o próprio `index.html` e o `chart.js` do CDN. 0 requisições para `atlassian.net` ou qualquer host da Atlassian.
- **Nenhum aviso `[PR03] JQL sem correspondencia no snapshot`** no console — todos os 11 padrões de JQL resolveram.
- Única mensagem de console de toda a sessão: `[PR03] Snapshot estatico carregado - gerado em 2026-09-03T17:30:17-03:00; consultas ao Jira desativadas.`
- **0 erros de JavaScript**, nenhuma mensagem em nível `warning`/`error`, nenhum recurso 404 e `#EA` (área de erro de inicialização) vazia.
- As três abas foram clicadas em sequência — "Agosto 2026 — Encerrado", "Setembro 2026 — Ao vivo" e "Visão Acumulada — Histórico" — todas renderizando normalmente; seletores de projeto `sP` e `fP` com 20 `option` cada ("Todos" + os 19 projetos), 80 `option` no total da página contando os seletores de mês/ano da Visão Acumulada.
- `window.__SNAPSHOT__.generatedAt` = `2026-09-03T17:30:17-03:00`, 19 projetos, e `window.__HISTORY__` com os 5 meses congelados (`2026-04` a `2026-08`) — confirmando que o merge defensivo do `__HISTORY__` preservou os meses do snapshot.
- Os 5 `canvas` do dashboard (`c1`, `c2`, `c3` nas abas mensais e `chEvo`/`chBar` na Visão Acumulada) foram inicializados e desenhados com dimensões não nulas.
- Observação sobre o ambiente de verificação: a requisição do `chart.js@4.5.0` foi respondida com o arquivo real obtido do pacote `chart.js@4.5.0` do npm, cujo SHA-384 (`iU8HYtnGQ8Cy4zl7gbNMOhsDTTKX02BTXptVP/vqAWIaTfM7isw76iyZCsjL2eVi`) confere com o `integrity` (SRI) declarado na tag. No Vercel a tag carrega do CDN normalmente.
- As duas únicas menções a `atlassian.net` no HTML vêm do próprio artifact e não são requisições: o texto do rodapé ("Fonte: JIRA (projetos-engeplus.atlassian.net)") e a base dos links `browse/` usada quando se clica em um EPIC.
- Nenhuma operação de git foi executada — commit e push são da tarefa agendada.

### Observação sobre a origem do HTML

Nesta execução a pasta do Live Artifact (`C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics`) **não estava montada na sessão** — a sessão só tinha acesso a este repositório. O snapshot foi gerado a partir de `_artifact_src.html`, cópia limpa do artifact, ainda idêntica (mesmo MD5) à `_artifact_live_check.html` conferida com o artifact ao vivo em 31/08/2026. Enquanto a pasta do artifact seguir desconectada, alterações de layout feitas no Live Artifact não entram no snapshot — apenas os dados do Jira são atualizados.

## Privacidade

Os dados embutidos passam por minimização antes de serem gravados. São mantidos apenas:

`key`, `summary`, `status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`, `updated`.

**Removidos:** `accountId`, e-mails, avatares, `iconUrl`, descrições em ADF, comentários, worklogs, dados de responsável (assignee/reporter) e demais metadados da API.
Nomes de pessoas podem, eventualmente, aparecer dentro de `summary` ou `status.name` — publicação aprovada pelo responsável pelo repositório.

## Arquivos

| Arquivo | Tamanho | Descrição |
|---|---:|---|
| `index.html` | 143.9 KB | Snapshot estático publicado (dados embutidos) |
| `snapshot-data.js` | 58.2 KB | Bloco de dados injetado (cópia avulsa, para inspeção) |
| `_artifact_src.html` | 85.5 KB | Cópia do artifact original, sem dados |
| `_snap/*.json` | — | Conjuntos minimais por mês, reutilizados entre gerações |
| `_gen_snapshot.py` | — | Gerador do snapshot |

## Publicação

O commit e o push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que verifica o working tree a cada 30 minutos. O deploy no Vercel ocorre cerca de 1 minuto após o push.
