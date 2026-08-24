# PR.03 — Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Pr03 Relatorio Indicadores Epics** (Engeplus Engenharia — Estudos e Projetos).

- **Última atualização:** 24/08/2026 15:13 (America/Sao_Paulo)
- **Timestamp ISO:** `2026-08-24T15:13:34-03:00`
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como EPIC:** `Epic`, `Fluxo de trabalho` (hierarchyLevel = 1)
- **Projetos visíveis:** 19
- **Filtro base (ETQ):** `issuetype in ("Epic","Fluxo de trabalho")`

## O que é isto

Cópia estática (dados congelados) do Live Artifact. A página **não** consulta o Jira ao vivo:
um bloco `<script>` injetado antes do script principal define `window.__SNAPSHOT__` e substitui
`window.cowork.callMcpTool` por um resolvedor local que devolve os dados pré-buscados a partir do
texto exato da consulta JQL. Consultas fora do período congelado retornam vazio e registram aviso
no console — nunca vão à rede.

Além disso, o snapshot faz `Object.assign` em `window.__HISTORY__`, **preservando** os períodos que
já estavam congelados dentro do próprio artifact (Abril, Maio e Junho/2026) e acrescentando os meses
coletados nesta execução.

## Dados congelados neste snapshot

| Mês | Previstos | Entregues | OTD | Atrasados (acum.) | Lookahead | Enviados | Retrabalho | Origem |
|---|---|---|---|---|---|---|---|---|
| Março/2026 | 7 | — | — | — | — | — | — | `planned` desta execução |
| Abril/2026 | 19 | — | — | 1 | 36 | 20 | 18 | congelado no artifact |
| Maio/2026 | 15 | — | — | 6 | 18 | 3 | 1 | congelado no artifact |
| Junho/2026 | 2 | — | — | 2 | — | 7 | 0 | congelado no artifact |
| Julho/2026 | 10 | 8 | 80% | 1 | 27 | 11 | 5 (45%) | snapshot desta execução |
| Agosto/2026 | 14 | 2 | 14% | 1 | 29 | 5 | 3 (60%) | snapshot desta execução |

- **Julho e Agosto/2026** (abas mensais) têm o conjunto completo de indicadores: `planned`,
  `overdue`, `lookahead`, `sent`, `resolved` e `rework`.
- **Março/2026** tem apenas `planned`, usado pela Visão Acumulada.
- **Abril, Maio e Junho/2026** vêm do `__HISTORY__` embutido no artifact (premissa do relatório:
  período encerrado = dado congelado, nunca reconsultado).

### Visão Acumulada (Março/2026 a Agosto/2026 — padrão)

| Indicador | Valor |
|---|---|
| OTD Acumulado | 51% (34 de 67) |
| Total Previstos | 67 (6 meses) |
| Total Entregues | 34 |
| Total Pendentes | 33 |

## Consultas resolvidas offline

16 consultas JQL + 1 `getVisibleJiraProjects` estão congeladas no snapshot:

- `planned` — 6 meses (2026-03 a 2026-08)
- `overdue`, `lookahead`, `sent`, `resolved`, `rework` — Julho e Agosto/2026

## Verificação desta geração

O arquivo foi renderizado num DOM headless antes da publicação:

- 0 requisições de rede (`fetch` / `XMLHttpRequest` interceptados e não chamados)
- 0 erros e 0 avisos de console; nenhum aviso do resolver (todo JQL emitido pela página estava no snapshot)
- As 3 visões renderizam: aba Julho/2026, aba Agosto/2026 e Visão Acumulada
- Varredura de privacidade sem ocorrências de `accountId`, `avatarUrl`, `emailAddress`, `iconUrl` ou `self`
- Único recurso externo: CDN do Chart.js (`cdn.jsdelivr.net`, com `integrity`)

## Observação sobre a métrica "Enviados"

Existem variantes de grafia do status no Jira que o filtro exato
`status changed to "Enviado - Aguardando Análise"` não captura:

- `Enviado - Aguardando Análise1` (ex.: EG0239, EG0256)
- `Enviado- Aguardando Análise` — sem espaço antes do hífen (ex.: EG0285)

Por isso a consulta `sent` isolada fica abaixo do real, e o dashboard compensa unindo `sent` com
`resolved` (`statusCategory=Done`). A métrica de `rework` usa `status changed from
"Enviado - Aguardando Análise"` sem restrição de período, então conta também progressões normais do
fluxo (ex.: para "Medido e Faturado") — não apenas retrabalho de fato. Padronizar os nomes de status
no Jira resolveria as duas distorções.

## Privacidade

Os JSONs de origem foram reduzidos a `key`, `summary`, `status`, `project`, `duedate`,
`resolutiondate` e `updated`. Não há accountIds, e-mails, avatares nem descrições (ADF). Nomes de
epics e de projetos são publicados por opção do responsável.

## Publicação

`index.html` é servido pelo Vercel. O commit e o push são feitos pela tarefa
`PR03-Auto-Push-GitHub` do Windows Task Scheduler, que roda a cada 30 minutos e detecta mudanças no
working tree. Esta geração **não** executa git.
