# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 25/09/2026 10:30** (`2026-09-25T10:30:59-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **20**

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
| `planned_2026-09` | Epics com due date em set/2026 | 18 |
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 2 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 29 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 5 |
| `resolved_2026-09` | Concluídos em set/2026 | 4 |
| `rework_2026-09` | Retrabalho em set/2026 | 2 |
| `planned_2026-04` | Epics com due date em abr/2026 (Visão Acumulada) | 15 |
| `planned_2026-05` | Epics com due date em mai/2026 (Visão Acumulada) | 7 |
| `planned_2026-06` | Epics com due date em jun/2026 (Visão Acumulada) | 1 |

Mais a lista de projetos (`getVisibleJiraProjects`): 20 projetos, 2 tipos de nível Epic.
Dos 21 conjuntos carregados, **11 vão embutidos** como `DATASETS` no JavaScript (apenas os alcançáveis por algum padrão de JQL: os 6 do mês corrente e os `planned` da Visão Acumulada). Os meses congelados viajam dentro de `__SNAPSHOT__.months` e nunca chegam a consultar o Jira.

### ⚠️ Cuidado ao refazer as consultas: o filtro de tipo NÃO é `issuetype=Epic`

O artifact monta o filtro dinamicamente (`ETQ`, linha ~360 do `_artifact_src.html`) a partir de **todos** os tipos de issue de `hierarchyLevel === 1` encontrados em `getVisibleJiraProjects`:

```
issuetype in ("Epic","Fluxo de trabalho")
```

Projetos *team-managed* renomeiam o Epic — hoje o **EG0286 - DNIT/AC**, o **EG0285 - EMBASA - BARREIRAS**, o **EG0287 - Dique de Camboriú**, o **EG0292 - PREFEITURA DE BLUMENAU**, o **EG0291 - Arroio Feijó** e a **GESTÃO - CREA** usam `Fluxo de trabalho`.
Rodar as consultas com `issuetype=Epic` **não gera erro**: devolve silenciosamente menos registros, e esses projetos inteiros sumiriam do relatório publicado, zerando os indicadores de envio e de atraso acumulado. O `ETQ` deve sempre ser derivado dos `epicTypeNames` correntes, nunca escrito à mão.

**A geração das 15:29 de 24/09 reconfirmou o problema na prática.** Uma rodada exploratória com `issuetype=Epic` devolveu **14** registros em `planned_2026-09` (em vez de 20 à época) e **1** em `overdue_2026-09` (em vez de 2) — faltando `EG0286-13`, `EG0286-11`, `EG0286-14`, `EG0286-10`, `EG0286-6`, `EG0285-19` e `EG0286-8`. Consultados um a um, esses itens continuam existindo no Jira, com `issuetype.name = "Fluxo de trabalho"` e `hierarchyLevel = 1`. Desde então todas as gerações usam `issuetype in ("Epic","Fluxo de trabalho")`. Nenhum dado publicado foi afetado.

### O que mudou desde a geração anterior (25/09/2026 09:30)

**Houve mudança no Jira — a primeira desde 22/09.** Dois epics do projeto **EG0274** tiveram o prazo reagendado de setembro para outubro na manhã de hoje (25/09/2026, por volta das 09:56):

| Chave | Resumo | Due date anterior | Due date atual |
|---|---|---|---|
| `EG0274-58` | Proj. Básico - Projeto de Terraplenagem | 17/09/2026 | **30/10/2026** |
| `EG0274-21` | Proj. Básico - Projeto de Pavimentação | 17/09/2026 | **29/10/2026** |

Nenhum dos dois estava concluído, e ambos venciam ainda dentro de setembro. Com o reagendamento eles saem de `planned_2026-09` e entram em `lookahead_2026-09`.

| | Geração anterior (09:30 de 25/09) | Agora (10:30 de 25/09) |
|---|---:|---:|
| `planned_2026-09` | 20 | **18** |
| `overdue_2026-09` | 2 | **2** |
| `sent_2026-09` | 5 | **5** |
| `resolved_2026-09` | 4 | **4** |
| `rework_2026-09` | 2 | **2** |
| `lookahead_2026-09` | 27 | **29** |

- Os quatro conjuntos sem alteração foram conferidos **registro a registro** (chave, resumo, status, categoria, prazo, data de resolução e `updated`), não por contagem.
- A lista de projetos foi **reconsultada ao vivo**: 20 projetos, mesmas chaves de `_projects_min.json` (`CREA` … `PE`), e os tipos de nível Epic inalterados (`Epic`, `Fluxo de trabalho`). O `_projects_min.json` do repositório foi mantido.
- Julho e agosto/2026 permanecem congelados com os mesmos números; os `planned` da Visão Acumulada de abril a junho/2026 não foram alterados.
- Indicadores de setembro após a mudança: **18 previstos**, 5 envios, 2 com retrabalho, 2 em atraso acumulado, 29 entregas nos próximos 60 dias.
- ⚠️ Atenção para a próxima geração: como os dois epics não foram concluídos e apenas mudaram de prazo, eles **não** contam como atraso — mas o `planned` de setembro fechará o mês com 18 em vez de 20, o que reduz a base do indicador de cumprimento de prazo do mês.

### Períodos cobertos

- **Julho/2026** — encerrado, congelado em 01/08/2026 (10 previstos, 0 em atraso acumulado, 11 envios na união `sent` + `resolved`, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — encerrado, congelado em 01/09/2026 (4 previstos, 0 em atraso acumulado, 6 envios, 3 com retrabalho, 39 entregas nos 60 dias seguintes).
- **Setembro/2026** — mês corrente, atualizado a cada geração do snapshot (18 previstos, 5 envios registrados, 2 com retrabalho, 2 em atraso acumulado, 29 entregas nos próximos 60 dias).
- **Visão acumulada** — abril a setembro/2026, um conjunto `planned` por mês.

## Verificação desta geração

O `index.html` gerado foi carregado em navegador headless (Chromium/Playwright), a partir de uma cópia byte a byte do arquivo publicado, percorrendo as três abas:

- **Nenhuma requisição para a Atlassian.** O navegador emitiu 2 requisições no total: o próprio `index.html` e o `chart.js@4.5.0` do CDN. 0 requisições para `atlassian.net` ou qualquer host da Atlassian.
- **Nenhum aviso `[PR03] JQL sem correspondencia no snapshot`** no console — todos os 11 padrões de JQL resolveram.
- Única mensagem de console de toda a sessão: `[PR03] Snapshot estatico carregado - gerado em 2026-09-25T10:30:59-03:00; consultas ao Jira desativadas.`
- **0 erros de JavaScript** e nenhuma mensagem em nível `warning`/`error`.
- As três abas foram percorridas — "Agosto 2026 — Encerrado", "Setembro 2026 — Ao vivo" e "Visão Acumulada — Histórico" — todas renderizando normalmente.
- `window.__SNAPSHOT__.generatedAt` = `2026-09-25T10:30:59-03:00`, 20 projetos, `epicTypeNames` = `Epic`, `Fluxo de trabalho`, e `window.__HISTORY__` com os 5 meses congelados (`2026-04` a `2026-08`) — confirmando que o merge defensivo do `__HISTORY__` preservou os meses do snapshot.
- Os 5 `canvas` do dashboard foram inicializados com dimensões não nulas (`c1` 300×160, `c3` 300×160, `c2` 494×156, `chEvo` 1190×220, `chBar` 1190×280).
- Conferência dos dados embutidos: `planned_2026-09` com 18 registros e sem `EG0274-58`/`EG0274-21`; `lookahead_2026-09` com 29 registros, contendo os dois.
- Estrutura do arquivo conferida: comentário `<!-- Snapshot gerado em ... -->` no topo do `<head>`, bloco `__SNAPSHOT__` **antes** do script principal do artifact (`window.__HISTORY__=`) e banner de aviso imediatamente antes de `</body>` (única ocorrência da tag).
- Varredura de vazamento no HTML final: 0 ocorrências de `avatarUrls`, `emailAddress` ou `iconUrl`. A única ocorrência da string `accountId` é a própria frase do cabeçalho do gerador ("Nao contem accountIds, e-mails nem avatares").
- Nenhuma operação de git foi executada nesta geração — nem `add`, `commit` ou `push`. O working tree foi deixado pronto para a tarefa agendada.

### Observação sobre a origem do HTML

A pasta `C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics` **não está montada** nesta sessão — a única pasta conectada é a do repositório. Nesta geração, como nas anteriores, o HTML do Live Artifact foi obtido **diretamente do app**, pelo identificador `pr03-relatorio-indicadores-epics`, e conferido contra o `_artifact_src.html` versionado no repositório: **idênticos** (MD5 `6a2b6462a4efbec1890af4494a7f0b74`, 87.509 bytes). O snapshot foi gerado a partir dessa cópia. O layout do artifact não muda desde 27/07/2026.

## Privacidade

Os dados embutidos passam por minimização antes de serem gravados. São mantidos apenas:

`key`, `summary`, `status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`, `updated`.

**Removidos:** `accountId`, e-mails, avatares, `iconUrl`, descrições em ADF, comentários, worklogs, dados de responsável (assignee/reporter) e demais metadados da API.
Nomes de pessoas podem, eventualmente, aparecer dentro de `summary` ou `status.name` — publicação aprovada pelo responsável pelo repositório.

## Arquivos

| Arquivo | Tamanho | Descrição |
|---|---:|---|
| `index.html` | 147.3 KB | Snapshot estático publicado (dados embutidos) |
| `snapshot-data.js` | 61.5 KB | Bloco de dados injetado (cópia avulsa, para inspeção) |
| `_artifact_src.html` | 85.5 KB | Cópia do artifact original, sem dados |
| `_projects_min.json` | 5.1 KB | Lista minimal de projetos visíveis (20) e seus tipos de issue |
| `_snap/*.json` | — | Conjuntos minimais por mês, reutilizados entre gerações |
| `_snap/_run0925b.py` | — | Carga dos dados de setembro desta geração (reagendamento de `EG0274-58` e `EG0274-21`) |
| `_snap/_verify0925a.py` | — | Conferência registro a registro da geração das 09:30 de 25/09 |
| `_snap/_run0922h.py` | — | Carga anterior dos dados de setembro (22/09/2026) |
| `_snap/_verify0924d.py` | — | Conferência da geração das 15:28 de 24/09 |
| `_snap/_verify0924c.py` | — | Conferência da geração das 15:21 de 24/09 |
| `_gen_snapshot.py` | — | Gerador do snapshot |

## Publicação

O commit e o push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que verifica o working tree a cada 30 minutos. O deploy no Vercel ocorre cerca de 1 minuto após o push.
