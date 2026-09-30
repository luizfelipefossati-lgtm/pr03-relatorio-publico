# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 29/09/2026 21:30** (`2026-09-29T21:30:49-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **21**

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
| `planned_2026-09` | Epics com due date em set/2026 | 17 |
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 1 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 32 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 6 |
| `resolved_2026-09` | Concluídos em set/2026 | 4 |
| `rework_2026-09` | Retrabalho em set/2026 | 3 |
| `planned_2026-04` | Epics com due date em abr/2026 (Visão Acumulada) | 15 |
| `planned_2026-05` | Epics com due date em mai/2026 (Visão Acumulada) | 7 |
| `planned_2026-06` | Epics com due date em jun/2026 (Visão Acumulada) | 1 |

Mais a lista de projetos (`getVisibleJiraProjects`): 21 projetos, 2 tipos de nível Epic.
Dos 21 conjuntos carregados, **11 vão embutidos** como `DATASETS` no JavaScript (apenas os alcançáveis por algum padrão de JQL: os 6 do mês corrente e os `planned` da Visão Acumulada). Os meses congelados viajam dentro de `__SNAPSHOT__.months` e nunca chegam a consultar o Jira.

### ⚠️ Cuidado ao refazer as consultas: o filtro de tipo NÃO é `issuetype=Epic`

O artifact monta o filtro dinamicamente (`ETQ`, linha ~360 do `_artifact_src.html`) a partir de **todos** os tipos de issue de `hierarchyLevel === 1` encontrados em `getVisibleJiraProjects`:

```
issuetype in ("Epic","Fluxo de trabalho")
```

Projetos *team-managed* renomeiam o Epic — hoje o **EG0286 - DNIT/AC**, o **EG0285 - EMBASA - BARREIRAS**, o **EG0287 - Dique de Camboriú**, o **EG0292 - PREFEITURA DE BLUMENAU**, o **EG0291 - Arroio Feijó** e a **GESTÃO - CREA** usam `Fluxo de trabalho`.
Rodar as consultas com `issuetype=Epic` **não gera erro**: devolve silenciosamente menos registros, e esses projetos inteiros sumiriam do relatório publicado, zerando os indicadores de envio e de atraso acumulado. O `ETQ` deve sempre ser derivado dos `epicTypeNames` correntes, nunca escrito à mão.

**A geração das 15:29 de 24/09 reconfirmou o problema na prática.** Uma rodada exploratória com `issuetype=Epic` devolveu **14** registros em `planned_2026-09` (em vez de 20 à época) e **1** em `overdue_2026-09` (em vez de 2) — faltando `EG0286-13`, `EG0286-11`, `EG0286-14`, `EG0286-10`, `EG0286-6`, `EG0285-19` e `EG0286-8`. Consultados um a um, esses itens continuam existindo no Jira, com `issuetype.name = "Fluxo de trabalho"` e `hierarchyLevel = 1`. Desde então todas as gerações usam `issuetype in ("Epic","Fluxo de trabalho")`.

### O que mudou desde a geração anterior (29/09/2026 19:30)

**Nada nos dados; um projeto novo na lista.** As seis consultas de setembro foram refeitas ao vivo e vieram idênticas registro a registro. A mudança desta geração está na lista de projetos: `getVisibleJiraProjects` passou de 20 para **21** entradas, com a entrada do **`EG0294` — ARTLOT - Topografia**. Como os 3 epics/fluxos desse projeto estão sem prazo, ele não altera nenhum indicador — aparece apenas na relação de projetos do relatório.

| | Geração anterior (19:30 de 29/09) | Agora (20:30 de 29/09) |
|---|---:|---:|
| `planned_2026-09` | 17 | **17** |
| `overdue_2026-09` | 1 | **1** |
| `sent_2026-09` | 6 | **6** |
| `resolved_2026-09` | 4 | **4** |
| `rework_2026-09` | 3 | **3** |
| `lookahead_2026-09` | 32 | **32** |

- Cinco dos seis conjuntos de setembro (`planned`, `overdue`, `sent`, `resolved`, `rework`) foram trazidos por inteiro e conferidos **registro a registro** contra os arquivos gravados — chave, resumo, status, categoria, projeto, prazo, data de resolução e `updated` — todos idênticos. Nenhum arquivo em `_snap/` foi reescrito (`_snap/_run0929o.py` registra a conferência: sem delta nos dados, delta apenas na lista de projetos).
- O `lookahead_2026-09` foi conferido por duas consultas de contagem (`searchResultMode: "count"`), que não trazem registro algum e custam poucos tokens: a faixa out/2026–nov/2026 devolveu **32**, igual ao `lookahead_2026-09.json` gravado, e a mesma faixa com `updated >= "2026-09-28 12:00"` devolveu **0**. Como qualquer inserção, remoção ou edição nessa faixa — inclusive a mudança de prazo que tiraria ou traria uma issue para dentro dela — atualiza o campo `updated`, as duas contagens juntas excluem qualquer alteração desde a captura dos 32 registros em 28/09 às 13:31.
- A lista de projetos **foi reconsultada ao vivo** nesta geração e houve **delta**: `getVisibleJiraProjects` devolveu **21** projetos (antes 20), com o projeto novo **`EG0294` — ARTLOT - Topografia** (id 10630). O `_projects_min.json` foi atualizado de 20 para 21 entradas (backup em `_projects_min.json.bak`). Os tipos de issue do EG0294 são `Fluxo de trabalho` (nível 1), `Tarefa` e `Subtarefa`, de modo que os `epicTypeNames` continuam `Epic` e `Fluxo de trabalho` e o `ETQ` das consultas permanece inalterado. O EG0294 tem 3 epics/fluxos, **todos sem prazo (`duedate`)**, e por isso nenhum dos conjuntos de dados mudou — o projeto entra apenas na lista do relatório.
- A pasta `Artifacts` **não estava montada** nesta sessão (a única pasta conectada é a do próprio repositório), mas o HTML ao vivo do artifact **foi reconferido**: o artifact `pr03-relatorio-indicadores-epics` foi trazido por staging e seu md5 é `6a2b6462a4efbec1890af4494a7f0b74` (87.509 bytes), **idêntico** ao `_artifact_src.html` versionado no repositório. O `updatedAt` do artifact segue em 27/07/2026, sem alteração.
- A **Visão Acumulada não foi reconsultada** nesta geração: os meses de abril a agosto/2026 estão congelados e seus arquivos em `_snap/` foram reaproveitados sem alteração (abril 15, maio 7, junho 1, julho 10, agosto 4). Por desenho, o relatório preserva o retrato do fechamento de cada mês.
- Julho e agosto/2026 permanecem **congelados** com os mesmos números. Os dois meses não foram reconsultados: por desenho, alterações no Jira após o fechamento do período não afetam os meses congelados.
- Indicadores de setembro: **17 previstos**, 6 envios, 3 com retrabalho, 1 em atraso acumulado, 32 entregas nos próximos 60 dias. OTD do mês corrente: **12%** (agosto fechou em 50%).

### Períodos cobertos

- **Julho/2026** — encerrado, congelado em 01/08/2026 (10 previstos, 0 em atraso acumulado, 11 envios na união `sent` + `resolved`, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — encerrado, congelado em 01/09/2026 (4 previstos, 0 em atraso acumulado, 6 envios, 3 com retrabalho, 39 entregas nos 60 dias seguintes).
- **Setembro/2026** — mês corrente, atualizado a cada geração do snapshot (17 previstos, 6 envios registrados, 3 com retrabalho, 1 em atraso acumulado, 32 entregas nos próximos 60 dias).
- **Visão acumulada** — abril a setembro/2026, um conjunto `planned` por mês.

## Verificação desta geração

O `index.html` gerado foi carregado em navegador headless (Chromium/Playwright), a partir de uma cópia byte a byte do arquivo publicado (`md5 c6684e5ef6fa138975beea75d7d42048`, 151.801 bytes), percorrendo as três abas:

- **Nenhuma requisição para a Atlassian.** Além do próprio `index.html`, o navegador emitiu uma única requisição externa: o `chart.js@4.5.0` do CDN (`cdn.jsdelivr.net`). 0 requisições para `atlassian.net` ou qualquer host da Atlassian.
- **Nenhum aviso `[PR03] JQL sem correspondencia no snapshot`** no console — todos os 11 padrões de JQL resolveram.
- Única mensagem de console de toda a sessão: `[PR03] Snapshot estatico carregado - gerado em 2026-09-29T20:30:27-03:00; consultas ao Jira desativadas.`
- **0 erros de JavaScript** e nenhuma mensagem em nível `warning`/`error`.
- As três abas foram percorridas uma a uma — "Agosto 2026 — Encerrado", "Setembro 2026 — Ao vivo" e "Visão Acumulada — Histórico" — todas renderizando normalmente, sem nenhum erro de página após os cliques.
- `window.__SNAPSHOT__.generatedAt` = `2026-09-29T20:30:27-03:00`, 21 projetos (incluindo o novo `EG0294`), `epicTypeNames` = `Epic`, `Fluxo de trabalho`, e `window.__HISTORY__` com os 5 meses congelados (`2026-04` a `2026-08`) — confirmando que o merge defensivo do `__HISTORY__` preservou os meses do snapshot (`2026-07` e `2026-08` vêm do snapshot; `2026-04` a `2026-06` vêm do próprio artifact).
- Conferência dos dados embutidos: os 11 `DATASETS` com as contagens esperadas — `planned_2026-09` com 17 registros, `lookahead_2026-09` com 32, `sent_2026-09` com 6, `resolved_2026-09` com 4, `rework_2026-09` com 3, `overdue_2026-09` com 1 e os `planned` acumulados com 15 / 7 / 1 / 10 / 4.
- Estrutura do arquivo conferida: comentário `<!-- Snapshot gerado em ... -->` no topo do `<head>` (posição 608, logo após a abertura da tag), bloco `__SNAPSHOT__` **antes** do script principal do artifact (posições 83.576 e 86.019) e banner de aviso imediatamente antes de `</body>` (única ocorrência da tag, ao final do arquivo).
- Varredura de vazamento no HTML final: 0 ocorrências de `avatarUrls`, `emailAddress`, `iconUrl` ou `api.atlassian.com`. A única ocorrência da string `accountId` é a própria frase do cabeçalho do gerador ("Nao contem accountIds, e-mails nem avatares").
- Nenhum `git add`, `commit` ou `push` foi executado por esta sessão. O working tree foi deixado pronto para a tarefa agendada.

## Privacidade

Os dados embutidos passam por minimização antes de serem gravados. São mantidos apenas:

`key`, `summary`, `status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`, `updated`.

**Removidos:** `accountId`, e-mails, avatares, `iconUrl`, descrições em ADF, comentários, worklogs, dados de responsável (assignee/reporter) e demais metadados da API.
Nomes de pessoas podem, eventualmente, aparecer dentro de `summary` ou `status.name` — publicação aprovada pelo responsável pelo repositório.

## Arquivos

| Arquivo | Tamanho | Descrição |
|---|---:|---|
| `index.html` | 148.2 KB | Snapshot estático publicado (dados embutidos) |
| `snapshot-data.js` | 62.5 KB | Bloco de dados injetado (cópia avulsa, para inspeção) |
| `_artifact_src.html` | 85.5 KB | Cópia do artifact original, sem dados (md5 `6a2b6462a4efbec1890af4494a7f0b74`, conferido contra o artifact ao vivo na geração das 21:30 de 29/09) |
| `_projects_min.json` | 5.4 KB | Lista minimal de projetos visíveis (21) e seus tipos de issue |
| `_snap/*.json` | — | Conjuntos minimais por mês, reutilizados entre gerações |
| `_snap/_run0930a.py` | — | Conferência ao vivo desta geração (21:30 de 29/09), registro a registro (sem delta) |
| `_snap/_run0929o.py` | — | Conferência ao vivo da geração das 20:30 de 29/09, delta na lista de projetos |
| `_snap/_run0929n.py` | — | Conferência ao vivo da geração das 19:30 de 29/09, sem delta |
| `_snap/_run0929m.py` | — | Conferência ao vivo da geração das 16:30 de 29/09, sem delta |
| `_snap/_run0929j.py` | — | Conferência ao vivo da geração das 13:31 de 29/09, registro a registro (sem delta) |
| `_snap/_run0929h.py` | — | Conferência ao vivo da geração das 12:22 de 29/09, registro a registro (sem delta) |
| `_gen_snapshot.py` | — | Gerador do snapshot |

## Publicação

O commit e o push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que verifica o working tree periodicamente (ciclos de ~10 min observados no `.push-watchdog.log`). O deploy no Vercel ocorre cerca de 1 minuto após o push.
