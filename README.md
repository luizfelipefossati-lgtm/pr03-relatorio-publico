# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 31/08/2026 12:38** (`2026-08-31T12:38:40-03:00`)

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
| `planned_2026-08` | Epics com due date em ago/2026 | 8 |
| `overdue_2026-07` | Vencidos antes de jul/2026, não concluídos | 0 |
| `overdue_2026-08` | Vencidos antes de ago/2026, não concluídos | 0 |
| `lookahead_2026-07` | Due date entre ago/2026 e set/2026 | 26 |
| `lookahead_2026-08` | Due date entre set/2026 e out/2026 | 35 |
| `sent_2026-07` | Transições para "Enviado - Aguardando Análise" em jul/2026 | 5 |
| `sent_2026-08` | Transições para "Enviado - Aguardando Análise" em ago/2026 | 4 |
| `resolved_2026-07` | Concluídos em jul/2026 | 8 |
| `resolved_2026-08` | Concluídos em ago/2026 | 6 |
| `rework_2026-07` | Retrabalho (saiu de "Enviado - Aguardando Análise") em jul/2026 | 5 |
| `rework_2026-08` | Retrabalho (saiu de "Enviado - Aguardando Análise") em ago/2026 | 3 |

Mais 1 chamada a `getVisibleJiraProjects` (19 projetos, 2 tipos de nível Epic).

**Nenhum conjunto mudou em relação às gerações anteriores de hoje (07:35, 08:35, 09:30, 09:40, 10:35, 11:30 e 12:38)** — nesta geração os **16 conjuntos foram integralmente reexecutados** contra o Jira (sem atalho de verificação por `updated`) e comparados campo a campo com os dados da geração anterior: **16/16 idênticos**, mesmas chaves de issue e mesmos valores de `status`, `duedate`, `resolutiondate` e `updated`. A lista de projetos (`getVisibleJiraProjects`) também foi reexecutada e conferida por hash canônico — idêntica (19 projetos, `md5 e7a0d8e010f894459f7a584a734d868f`). Apenas o carimbo de tempo mudou, e o `index.html` resultante mantém 151.363 bytes.

### Períodos cobertos

- **Julho/2026** — período encerrado, dados travados no snapshot (10 previstos, 0 em atraso acumulado, 11 envios na união `sent` + `resolved`, 5 com retrabalho, 26 entregas nos 60 dias seguintes).
- **Agosto/2026** — mês corrente, atualizado a cada geração do snapshot (8 previstos, 0 em atraso acumulado, 6 concluídos no mês, 3 com retrabalho, 35 entregas nos próximos 60 dias).
- **Visão acumulada** — março a agosto/2026, um conjunto `planned` por mês.

## Privacidade

Os dados embutidos passam por minimização antes de serem gravados. São mantidos apenas:

`key`, `summary`, `status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate`, `updated`.

**Removidos:** `accountId`, e-mails, avatares, `iconUrl`, descrições em ADF, comentários, worklogs, dados de responsável (assignee/reporter) e demais metadados da API.
Nomes de pessoas podem, eventualmente, aparecer dentro de `summary` ou `status.name` — publicação aprovada pelo responsável pelo repositório.

## Estrutura

| Arquivo | Função |
|---|---|
| `index.html` | Página publicada (artifact + dados estáticos + banner de snapshot) — 147,8 KB (151.363 bytes) |
| `snapshot-data.js` | Bloco de dados estáticos, também embutido no `index.html` |
| `_artifact_src.html` | Cópia do artifact original, sem os dados (não versionado) |
| `_projects_min.json` | Lista minimizada de projetos e tipos de issue |
| `_snap/` | JSONs minimais por consulta (insumo da geração) |
| `_gen_snapshot.py` | Gerador do snapshot (`_artifact_src.html` + `_snap/` → `index.html`) |
| `vercel.json` | Configuração de deploy |
| `auto-push.ps1`, `pr03-push-watchdog.ps1` | Automação de commit/push no Windows |

## Pipeline de atualização

1. A tarefa agendada **`deploy-pr03-vercel`** (Cowork) consulta o Jira, gera o snapshot e grava `index.html` + `README.md`.
2. A tarefa do Windows Task Scheduler **`PR03-Auto-Push-GitHub`** roda a cada 30 minutos, detecta alterações no working tree e faz `git add -A`, `commit` e `push`.
3. O **Vercel** publica automaticamente cerca de 1 minuto após o push.

A geração do snapshot e o push são etapas independentes: o agente nunca executa operações de git nem autentica no GitHub.

## Verificação desta geração

- **16 consultas reexecutadas no Jira** (mais `getVisibleJiraProjects`) via MCP, com `fields` restrito a `summary, status, project, duedate, resolutiondate, updated`. Nenhuma consulta falhou; nenhuma exigiu paginação (todas com `hasNextPage: false`, abaixo do limite de 100 resultados).
- **`_artifact_src.html` NÃO pôde ser reconferido contra o Live Artifact nesta geração.** A pasta `Artifacts\pr03-relatorio-indicadores-epics` não estava montada na sessão (apenas `pr03-relatorio-publico`), então a fonte usada foi a cópia local do repositório. As duas cópias locais — `_artifact_src.html` e `_artifact_live_check.html`, esta última extraída do Live Artifact às 12:39 de hoje — são byte a byte idênticas: 87.509 bytes, `md5 6a2b6462a4efbec1890af4494a7f0b74`, o mesmo hash confirmado na geração das 11:30. Alterações feitas no Live Artifact após aquela extração não estariam refletidas aqui.
- **16 JQLs emitidas pelo artifact conferidas por script contra os 16 padrões do snapshot** (mês anterior, mês corrente e os meses da visão acumulada) — **16/16 casaram** com o conjunto esperado, 0 falhas.
- **Estrutura dos 16 conjuntos validada por script** — chaves exatas em todos os níveis, `statusCategory.key` sempre em `new | indeterminate | done`, `project.key` coerente com o prefixo da `key` da issue e presente em `_projects_min.json`. **0 problemas.**
- **Contagens comparadas com a geração anterior** — 16/16 idênticas, incluindo os dois conjuntos vazios (`overdue_*`).
- **Ausência de `accountId`, e-mails, `avatarUrls` e `iconUrl`** no HTML final — OK. A única ocorrência da string `accountId` é na frase "Nao contem accountIds, e-mails nem avatares" do cabeçalho de comentário do próprio bloco de dados.
- **Ordem de injeção** — o bloco do snapshot aparece antes do script principal do artifact (offset 83.126 contra 85.576).
- **Posição do banner** de snapshot (imediatamente antes de `</body>`, não no topo do body) — OK.
- **Comentário `<!-- Snapshot gerado em ... -->`** no topo do `<head>` — OK.
- **Nenhuma operação de git executada** pelo agente (sem `add`, `commit`, `push` ou autenticação).

**Renderização verificada nesta geração** (Chromium/Playwright headless, sobre o `index.html` que está no disco):

| Aba | Linhas de tabela | Chaves de issue | OTD | Retrabalho |
|---|---:|---:|---:|---:|
| Julho 2026 (encerrado) | 78 | 45 | 80% (8 de 10) | 45% (5/11) |
| Agosto 2026 (ao vivo) | 85 | 49 | 25% (2 de 8) | 50% (3/6) |
| Visão Acumulada | 133 | 27 | 56% acumulado (34 de 61) | 34 entregues / 27 pendentes |

Também confirmado em execução: `[PR03] Snapshot estatico carregado - gerado em 2026-08-31T12:38:40-03:00` no console, **0 avisos de "JQL sem correspondencia"** (os 16 padrões cobrem todas as consultas que o artifact emite) e **0 requisições de rede para `atlassian.com`**. A única requisição externa da página é o `chart.js@4.5.0` do jsDelivr, necessário para os gráficos; no sandbox de verificação esse CDN é bloqueado, então o teste rodou com um stub do `Chart` — em produção (Vercel) o script carrega normalmente.

**Execuções repetidas:** a tarefa `deploy-pr03-vercel` já rodou sete vezes hoje (07:35, 08:35, 09:30, 09:40, 10:35, 11:30 e 12:38). Todas produziram `index.html` e `snapshot-data.js` de tamanho idêntico (151.363 e 63.577 bytes), diferindo apenas no carimbo de tempo. Este README descreve o arquivo que está no disco, com carimbo `2026-08-31T12:38:40-03:00`.

## Observações da fonte de dados

- **Escopo de "Epic".** O artifact monta a consulta a partir dos tipos de issue com `hierarchyLevel === 1` retornados por `getVisibleJiraProjects` — hoje `Epic` e `Fluxo de trabalho`. Consultas restritas a `issuetype = Epic` subestimam todos os conjuntos, porque deixam de fora os projetos EG0285, EG0286, EG0287, EG0292 e CREA, que usam `Fluxo de trabalho`.
- **Abril, maio e junho/2026 na Visão Acumulada vêm do `window.__HISTORY__` embutido no próprio artifact**, não das consultas deste snapshot — o snapshot só congela `2026-07`. Por isso o heatmap mostra 19 previstos em abr/2026, 15 em mai/2026 e 2 em jun/2026, enquanto uma consulta nova ao Jira hoje retorna 15, 7 e 1. São recortes de momentos diferentes; para realinhar, o histórico embutido no artifact precisa ser regerado.
- Existem variantes do nome do status de envio no Jira (`Enviado - Aguardando Análise`, `Enviado - Aguardando Análise1`, `Enviado- Aguardando Análise` — esta última sem espaço antes do hífen). As consultas `sent_*` e `rework_*` usam o nome canônico, então itens com as variantes aparecem apenas em `resolved_*` — daí a diferença entre `sent` e o total de envios (jul/2026: 5 em `sent`, 11 na união com `resolved`; ago/2026: 4 e 6). Essa quase-duplicidade de nomes é uma armadilha real: qualquer filtro por igualdade exata com o nome canônico ignora silenciosamente os itens com as variantes.
- Em jul/2026, `rework_2026-07` retornou exatamente o mesmo conjunto de `sent_2026-07`: todos os itens que entraram em "Enviado - Aguardando Análise" no período também saíram desse status em algum momento. Não é erro de consulta, mas convém validar a leitura do indicador de retrabalho — a cláusula `status changed from` não tem recorte temporal, então casa também com a transição normal para "Medido e Faturado". Em ago/2026 os conjuntos já divergem (3 de 4).
- `overdue_2026-07` e `overdue_2026-08` retornaram vazios: não há Epic com due date anterior ao início do mês ainda fora de `statusCategory=Done`. Vale notar que várias situações de "aguardando análise do cliente" estão mapeadas na categoria `Done` do Jira, então `statusCategory!=Done` não equivale a "trabalho em aberto".
- O projeto "EG0280 - DMAE" tem a chave `G0280` no Jira (sem o `E` inicial); o valor é preservado como retornado pela API.
- Peculiaridades do cadastro original foram preservadas literalmente: espaços à direita (`EG0286 - DNIT/AC `, `Estudos Hidrológicos `), espaço duplo (`TOMO IV -  PLANO...`) e nomes de status com erro de digitação (`Em Revisã`).
