# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 21/09/2026 09:14** (`2026-09-21T09:14:05-03:00`)

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
| `planned_2026-09` | Epics com due date em set/2026 | 21 |
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 1 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 26 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 2 |
| `resolved_2026-09` | Concluídos em set/2026 | 2 |
| `rework_2026-09` | Retrabalho em set/2026 | 0 |
| `planned_2026-04` | Epics com due date em abr/2026 (Visão Acumulada) | 15 |
| `planned_2026-05` | Epics com due date em mai/2026 (Visão Acumulada) | 7 |
| `planned_2026-06` | Epics com due date em jun/2026 (Visão Acumulada) | 1 |

Mais 1 chamada a `getVisibleJiraProjects` (19 projetos, 2 tipos de nível Epic).
Dos 21 conjuntos carregados, **11 vão embutidos** como `DATASETS` no JavaScript (apenas os alcançáveis por algum padrão de JQL: os 6 do mês corrente e os `planned` da Visão Acumulada). Os meses congelados viajam dentro de `__SNAPSHOT__.months` e nunca chegam a consultar o Jira.

### ⚠️ Cuidado ao refazer as consultas: o filtro de tipo NÃO é `issuetype=Epic`

O artifact monta o filtro dinamicamente (`ETQ`, linha ~360 do `_artifact_src.html`) a partir de **todos** os tipos de issue de `hierarchyLevel === 1` encontrados em `getVisibleJiraProjects`:

```
issuetype in ("Epic","Fluxo de trabalho")
```

Projetos *team-managed* renomeiam o Epic — hoje o **EG0286 - DNIT/AC** usa `Fluxo de trabalho`.
Rodar as consultas com `issuetype=Epic` **não gera erro**: devolve silenciosamente menos registros, e o projeto EG0286 inteiro sumiria do relatório publicado, zerando os indicadores de envio e de atraso acumulado. O `ETQ` deve sempre ser derivado dos `epicTypeNames` correntes, nunca escrito à mão.

### O que mudou desde a geração anterior (18/09/2026 14:31)

- **Nenhuma alteração nos dados do Jira.** As 6 consultas do mês corrente (`planned`, `overdue`, `lookahead`, `sent`, `resolved`, `rework` de set/2026) foram refeitas ao vivo e conferidas contra os conjuntos guardados em `_snap/`: mesmas 52 chaves, mesmos status, categorias, projetos, due dates e carimbos de `resolutiondate`/`updated`. Só o carimbo de tempo do snapshot mudou.
- Setembro/2026 segue com **21 previstos**, **2 envios** (`EG0286-30` — *Relatório Periódico*, enviado em 16/09 10:43; `EG0286-7` — *Estudo de tráfego*, enviado em 03/09), **0 retrabalho** e **26 entregas** nos 60 dias seguintes.
- O atraso acumulado segue com **um único** EPIC: `EG0286-8` — *Estudo topográfico*, due date 31/08/2026, ainda "Em andamento".
- A lista de projetos visíveis foi reconsultada: **19 projetos**, idêntica ao `_projects_min.json` do repositório, reaproveitado sem alteração. Tipos de nível Epic: `Epic` e `Fluxo de trabalho`.
- Julho e agosto/2026 permanecem congelados com os mesmos números; os `planned` da Visão Acumulada de abril a junho/2026 não foram alterados.

### Períodos cobertos

- **Julho/2026** — encerrado, congelado em 01/08/2026 (10 previstos, 0 em atraso acumulado, 11 envios na união `sent` + `resolved`, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — encerrado, congelado em 01/09/2026 (4 previstos, 0 em atraso acumulado, 6 envios, 3 com retrabalho, 39 entregas nos 60 dias seguintes).
- **Setembro/2026** — mês corrente, atualizado a cada geração do snapshot (21 previstos, 2 envios registrados, 1 em atraso acumulado, 26 entregas nos próximos 60 dias).
- **Visão acumulada** — abril a setembro/2026, um conjunto `planned` por mês.

## Verificação desta geração

O `index.html` gerado foi carregado em navegador headless (Chromium/Playwright), a partir de uma cópia byte a byte do arquivo publicado, percorrendo as três abas:

- **Nenhuma requisição para a Atlassian.** O navegador emitiu 2 requisições no total: o próprio `index.html` e o `chart.js@4.5.0` do CDN. 0 requisições para `atlassian.net` ou qualquer host da Atlassian.
- **Nenhum aviso `[PR03] JQL sem correspondencia no snapshot`** no console — todos os 11 padrões de JQL resolveram.
- Única mensagem de console de toda a sessão: `[PR03] Snapshot estatico carregado - gerado em 2026-09-21T09:14:05-03:00; consultas ao Jira desativadas.`
- **0 erros de JavaScript**, nenhuma mensagem em nível `warning`/`error` e `#EA` (área de erro de inicialização) vazia.
- As três abas foram percorridas — "Agosto 2026 — Encerrado", "Setembro 2026 — Ao vivo" e "Visão Acumulada — Histórico" — todas renderizando normalmente; 80 `option` no total da página (seletores de projeto com 20 opções cada: "Todos" + os 19 projetos).
- `window.__SNAPSHOT__.generatedAt` = `2026-09-21T09:14:05-03:00`, 19 projetos, e `window.__HISTORY__` com os 5 meses congelados (`2026-04` a `2026-08`) — confirmando que o merge defensivo do `__HISTORY__` preservou os meses do snapshot.
- Os 5 `canvas` do dashboard (`c1` 300×160, `c2` 494×182, `c3` 300×160 nas abas mensais; `chEvo` 1190×220 e `chBar` 1190×280 na Visão Acumulada) foram inicializados e desenhados com dimensões não nulas.
- Estrutura do arquivo conferida: comentário `<!-- Snapshot gerado em ... -->` no topo do `<head>`, bloco `__SNAPSHOT__` **antes** do script principal do artifact e banner de aviso imediatamente antes de `</body>`.
- Nenhuma operação de git foi executada — commit e push são da tarefa agendada.

### Observação sobre a origem do HTML

A pasta do Live Artifact (`C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics`) **não estava montada nesta sessão** e, por ser uma execução automática sem usuário presente, não pôde ser concedida. O snapshot foi gerado a partir do `_artifact_src.html` versionado no repositório, que na geração de 18/09/2026 foi confirmado idêntico (SHA-256 `2f09463c3e7c98cd03ce4bdf773e6160576a13b74387cd0518efd5279eec2419`, 87.509 bytes) ao HTML do Live Artifact. **Nesta geração essa comparação não foi refeita**: se o artifact ao vivo tiver mudado de layout desde 18/09, a mudança ainda não está refletida aqui. Os dados, esses sim, são de hoje.

## Privacidade

Os dados embutidos passam por minimização antes de serem gravados. São mantidos apenas:

`key`, `summary`, `status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`, `updated`.

**Removidos:** `accountId`, e-mails, avatares, `iconUrl`, descrições em ADF, comentários, worklogs, dados de responsável (assignee/reporter) e demais metadados da API.
Nomes de pessoas podem, eventualmente, aparecer dentro de `summary` ou `status.name` — publicação aprovada pelo responsável pelo repositório.

## Arquivos

| Arquivo | Tamanho | Descrição |
|---|---:|---|
| `index.html` | 144.5 KB | Snapshot estático publicado (dados embutidos) |
| `snapshot-data.js` | 58.8 KB | Bloco de dados injetado (cópia avulsa, para inspeção) |
| `_artifact_src.html` | 85.5 KB | Cópia do artifact original, sem dados |
| `_snap/*.json` | — | Conjuntos minimais por mês, reutilizados entre gerações |
| `_gen_snapshot.py` | — | Gerador do snapshot |

## Publicação

O commit e o push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que verifica o working tree a cada 30 minutos. O deploy no Vercel ocorre cerca de 1 minuto após o push.
