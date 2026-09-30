# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 30/09/2026 00:30** (`2026-09-30T00:30:53-03:00`)

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

### O que mudou desde a geração anterior (29/09/2026 23:30)

**Nada.** As seis consultas de setembro e a lista de projetos foram refeitas ao vivo e vieram idênticas. Esta geração apenas renova o carimbo de tempo do snapshot.

| | Geração anterior (23:30 de 29/09) | Agora (00:30 de 30/09) |
|---|---:|---:|
| `planned_2026-09` | 17 | **17** |
| `overdue_2026-09` | 1 | **1** |
| `sent_2026-09` | 6 | **6** |
| `resolved_2026-09` | 4 | **4** |
| `rework_2026-09` | 3 | **3** |
| `lookahead_2026-09` | 32 | **32** |
| projetos visíveis | 21 | **21** |

- **Varredura global de alterações:** `ETQ AND updated >= "2026-09-29 23:30"` devolveu **0** registros. Nenhum epic ou fluxo de trabalho do site foi criado ou editado desde a conferência da geração anterior — o que exclui, de uma só vez, inserções e edições em qualquer um dos conjuntos.
- **Contagem dos seis conjuntos de setembro** reconsultada ao vivo (`searchResultMode: count`): 17 / 1 / 32 / 6 / 4 / 3, idênticas às dos arquivos gravados em `_snap/`. A contagem cobre o que a varredura de `updated` não alcança — uma exclusão de issue não atualiza carimbo nenhum, mas reduz o total. Somadas, as duas checagens excluem inserção, remoção e edição.
- O `planned_2026-09` foi ainda trazido **por inteiro** (17 registros, `hasNextPage: false`) e as 17 chaves conferidas contra o arquivo gravado: as mesmas, na mesma ordem de projeto e prazo.
- Nenhum arquivo em `_snap/` foi reescrito.
- A lista de projetos **foi reconsultada ao vivo** (`getVisibleJiraProjects`, `total: 21`, `isLast: true`) e normalizada da mesma forma que o `_projects_min.json` gravado: a **assinatura md5 das duas versões é a mesma** (`aca1bab21c39a6dafd8d8b0bfd212527`, sobre chave, nome e tipos de issue com nível de hierarquia). Os `epicTypeNames` continuam `Epic` e `Fluxo de trabalho`, e o `ETQ` das consultas permanece inalterado. O `_projects_min.json` não foi reescrito.
- A pasta `Artifacts` **não estava montada** nesta sessão — a única pasta conectada é a do próprio repositório. O HTML ao vivo foi obtido por *staging* do artifact `pr03-relatorio-indicadores-epics` e conferido contra o `_artifact_src.html` versionado no repo: **md5 `6a2b6462a4efbec1890af4494a7f0b74`, 87.509 bytes, idêntico**. O artifact não mudou desde a última geração.
- A **Visão Acumulada não foi reconsultada**: os meses de abril a agosto/2026 estão congelados e seus arquivos em `_snap/` foram reaproveitados sem alteração (abril 15, maio 7, junho 1, julho 10, agosto 4). Por desenho, o relatório preserva o retrato do fechamento de cada mês.
- Julho e agosto/2026 permanecem **congelados** com os mesmos números, e não foram reconsultados.
- Indicadores de setembro: **17 previstos**, 6 envios, 3 com retrabalho, 1 em atraso acumulado, 32 entregas nos próximos 60 dias. OTD do mês corrente: **12%** (agosto fechou em 50%).

### Períodos cobertos

- **Julho/2026** — encerrado, congelado em 01/08/2026 (10 previstos, 0 em atraso acumulado, 11 envios na união `sent` + `resolved`, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — encerrado, congelado em 01/09/2026 (4 previstos, 0 em atraso acumulado, 6 envios, 3 com retrabalho, 39 entregas nos 60 dias seguintes).
- **Setembro/2026** — mês corrente, atualizado a cada geração do snapshot (17 previstos, 6 envios registrados, 3 com retrabalho, 1 em atraso acumulado, 32 entregas nos próximos 60 dias).
- **Visão acumulada** — abril a setembro/2026, um conjunto `planned` por mês.

## Verificação desta geração

O `index.html` gerado (151.801 bytes, md5 `9da3fffe940f07b6b5a86a1fe5b6db51`) foi conferido **estruturalmente** sobre o arquivo em disco:

- Comentário `<!-- Snapshot gerado em 2026-09-30T00:30:53-03:00 -->` no topo do `<head>` (posição 608, logo após a abertura da tag, que começa em 601).
- Bloco `window.__SNAPSHOT__` na posição 83.569, **antes** do script principal do artifact (`<script>\nwindow.__HISTORY__=`, posição 86.010) — a ordem que garante que o `callMcpTool` já esteja substituído quando o artifact rodar.
- Banner de aviso imediatamente antes de `</body>` (única ocorrência da tag, ao final do arquivo, posição 150.892), com o texto `Snapshot estatico - ultima atualizacao: 30/09/2026 00:30`.
- Os **11 padrões de JQL** foram gerados e conferidos no `snapshot-data.js`: os 6 do mês corrente (`rework`, `sent`, `resolved`, `overdue`, `lookahead`, `planned` de 2026-09) e os `planned` de abril a agosto/2026 da Visão Acumulada. Os meses congelados (jul e ago/2026) viajam em `__SNAPSHOT__.months` e não dependem de padrão.
- Contagens embutidas conferidas na geração: `planned_2026-09` 17, `lookahead_2026-09` 32, `sent_2026-09` 6, `resolved_2026-09` 4, `rework_2026-09` 3, `overdue_2026-09` 1, e os `planned` acumulados 15 / 7 / 1 / 10 / 4.
- Varredura de vazamento no HTML final: **0** ocorrências de `avatarUrls`, `emailAddress`, `iconUrl` ou `api.atlassian.com`. A única ocorrência de `accountId` é a frase do cabeçalho do gerador ("Nao contem accountIds, e-mails nem avatares"). As 2 ocorrências de `atlassian.net` vêm do próprio artifact e não geram requisição: o rótulo de rodapé "Fonte: JIRA (projetos-engeplus.atlassian.net)" e a constante `JB`, base dos links `browse/` para as issues.
- **Nesta geração não houve carregamento em navegador headless.** A verificação foi estrutural, sobre o arquivo em disco. A última checagem em navegador foi a da geração das 20:30 de 29/09, sobre um `index.html` de mesma estrutura, que registrou 0 requisições para a Atlassian, 0 erros de JavaScript e nenhum aviso `[PR03] JQL sem correspondencia no snapshot`.
- O `.git/index` estava **íntegro** (`git status` limpo, sem erro de assinatura); não foi preciso recuperá-lo.
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
| `_snap/_run0930b.py` | — | Conferência ao vivo desta geração (22:31 de 29/09), registro a registro (sem delta) |
| `_snap/_run0930a.py` | — | Conferência ao vivo da geração das 21:30 de 29/09, registro a registro (sem delta) |
| `_snap/_run0929o.py` | — | Conferência ao vivo da geração das 20:30 de 29/09, delta na lista de projetos |
| `_snap/_run0929n.py` | — | Conferência ao vivo da geração das 19:30 de 29/09, sem delta |
| `_snap/_run0929m.py` | — | Conferência ao vivo da geração das 16:30 de 29/09, sem delta |
| `_snap/_run0929j.py` | — | Conferência ao vivo da geração das 13:31 de 29/09, registro a registro (sem delta) |
| `_gen_snapshot.py` | — | Gerador do snapshot |

## Publicação

O commit e o push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que verifica o working tree periodicamente (ciclos de ~10 min observados no `.push-watchdog.log`). O deploy no Vercel ocorre cerca de 1 minuto após o push.
