# PR.03 — Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Pr03 Relatorio Indicadores Epics** (Engeplus Engenharia — Estudos e Projetos).

- **Última atualização:** 24/08/2026 16:09 (America/Sao_Paulo)
- **Timestamp ISO:** `2026-08-24T16:09:20-03:00`
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

| Mês | Previstos | Entregues | No prazo | Peq. atraso | Pendentes | Atrasados (acum.) | Lookahead | Enviados | Retrabalho | Origem |
|---|---|---|---|---|---|---|---|---|---|---|
| Março/2026 | 7 | — | — | — | — | — | — | — | — | `planned` desta execução |
| Abril/2026 | 19 | — | — | — | — | 1 | 36 | 20 | 18 | congelado no artifact |
| Maio/2026 | 15 | — | — | — | — | 6 | 18 | 3 | 1 | congelado no artifact |
| Junho/2026 | 2 | — | — | — | — | 2 | — | 7 | 0 | congelado no artifact |
| Julho/2026 | 10 | 10 | 7 | 3 | 0 | 1 | 27 | 11 | 7 | snapshot desta execução |
| Agosto/2026 | 14 | 2 | 0 | 2 | 12 | 1 | 29 | 5 | 2 | snapshot desta execução |

- **Julho e Agosto/2026** (abas mensais) têm o conjunto completo de indicadores: `planned`,
  `overdue`, `lookahead`, `sent`, `resolved` e `rework`.
- **Março/2026** tem apenas `planned`, usado pela Visão Acumulada.
- **Abril, Maio e Junho/2026** vêm do `__HISTORY__` embutido no artifact (premissa do relatório:
  período encerrado = dado congelado, nunca reconsultado).
- Os percentuais de OTD e de retrabalho são calculados na própria página a partir destes números.

## Consultas resolvidas offline

13 entradas JQL no índice de `window.__SNAPSHOT__.jql`:

- Julho/2026 — `planned` (10), `overdue` (1), `lookahead` ago–set (27), `sent` (5), `resolved` (8), `rework` (7)
- Agosto/2026 — `planned` (14), `overdue` (1), `lookahead` set–out (29), `sent` (3), `resolved` (5), `rework` (2)
- Março/2026 — `planned` (7)

Mais 1 chamada de `getVisibleJiraProjects` (19 projetos), também resolvida pelo bloco estático.

## Privacidade

Os JSONs embutidos foram reduzidos aos campos `key`, `summary`, `status`, `project`, `duedate`,
`resolutiondate` e `updated`. Não há `accountId`, e-mail, avatar, descrição de issue nem qualquer
outro metadado do Jira. Nomes de pessoas só apareceriam se estivessem escritos no título do epic ou
no nome do status.

## Publicação

O arquivo `index.html` é servido pela Vercel. O commit e o push são feitos automaticamente pela
tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que roda a cada 30 minutos e detecta
mudanças no working tree. O deploy sai cerca de 1 minuto depois do push.
