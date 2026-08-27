# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 10:12 (2026-08-27T10:12:34-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como Epic:** Fluxo de trabalho, Epic (descobertos por `hierarchyLevel === 1`)
- **Projetos visiveis no snapshot:** 19
- **Tamanho de `index.html`:** 147.6 KB (151.150 bytes, md5 `18e3596809796bf6a8ce30300f120af2`)

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

O script injetado entra **depois** do bloco `window.__HISTORY__` proprio do artifact
(que congela 2026-04 a 2026-06) e **antes** do script principal, de modo que os dois
conjuntos historicos coexistem em vez de um sobrescrever o outro. Na pagina carregada,
`window.__HISTORY__` fica com as chaves `2026-04`, `2026-05`, `2026-06` (nativas) e
`2026-07` (do snapshot). Ordem verificada nesta geracao: bloco nativo (offset 22.453)
-> bloco do snapshot (53.581) -> script principal (116.409).

O HTML base usado na geracao e o `_artifact_src.html` deste repositorio (947 linhas,
md5 `6a2b6462a4efbec1890af4494a7f0b74`), verificado contra o artifact atual
(`Artifacts\pr03-relatorio-indicadores-epics\index.html`) por contagem de linhas,
posicao dos blocos `<script>` (1, 21, 280, 283) e comparacao de linhas-ancora
(1, 21, 280, 283-302, 500-502, 700, 944-947), todas identicas. Se o artifact for
editado, `_artifact_src.html` precisa ser atualizado junto.

## Correcao aplicada nesta geracao

Na geracao anterior (09:12), a entrada `2026-07` de `window.__HISTORY__` continha
**apenas** a lista `planned`. Isso atendia a Visao Acumulada (que le
`__HISTORY__[key].planned`), mas quebrava a aba mensal **Julho 2026**, porque
`loadMonth()` devolve o objeto inteiro e `renderMonthly()` espera tambem
`overdue`, `sent`, `look` e `period`.

A entrada `2026-07` agora e um objeto de mes completo, montado com a mesma logica de
`loadMonth()` (uniao de `sent` + `resolved` por chave, `rework` marcando `rw:true`,
ordenacao com retrabalho primeiro), no mesmo formato das entradas nativas
`2026-04`/`2026-05`/`2026-06`:

| Campo | Valor |
|---|---|
| `planned` | 10 epics |
| `overdue` | 1 epic |
| `look` | 27 epics |
| `sent.total` | 11 |
| `sent.rework` | 5 |
| `period` | `2026-07-01` a `2026-07-31` ("Julho 2026") |

Os dados de julho foram **preservados** da geracao anterior (periodo encerrado =
dados congelados, conforme a premissa do artifact); nenhuma reconsulta foi feita
para julho.

## Chamadas dinamicas resolvidas

| # | Chamada | Dataset | Itens |
|---|---|---|---|
| 1 | `getVisibleJiraProjects` | `projects` | 19 projetos |
| 2 | planned Ago/2026 | `planned_2026-08` | 13 |
| 3 | overdue Ago/2026 | `overdue_2026-08` | 1 |
| 4 | lookahead Set-Out/2026 | `lookahead_2026-08` | 30 |
| 5 | sent Ago/2026 | `sent_2026-08` | 3 |
| 6 | resolved Ago/2026 | `resolved_2026-08` | 5 |
| 7 | rework Ago/2026 | `rework_2026-08` | 3 |
| 8 | planned Jul/2026 | `planned_2026-07` | 10 |
| 9 | overdue Jul/2026 | `overdue_2026-07` | 1 |
| 10 | lookahead Ago-Set/2026 | `lookahead_2026-07` | 27 |
| 11 | sent Jul/2026 | `sent_2026-07` | 5 |
| 12 | resolved Jul/2026 | `resolved_2026-07` | 8 |
| 13 | rework Jul/2026 | `rework_2026-07` | 5 |
| 14 | planned Mar/2026 (acumulado) | `planned_2026-03` | 7 |
| 15 | planned Abr/2026 (fallback) | `planned_2026-04` | 15 |
| 16 | planned Mai/2026 (fallback) | `planned_2026-05` | 7 |
| 17 | planned Jun/2026 (fallback) | `planned_2026-06` | 1 |

Ago/2026 e o mes ao vivo (reconsultado agora). Jul/2026 e servido por
`__HISTORY__`, mas os datasets ficam disponiveis como fallback caso a ordem dos
scripts mude. Abr/Mai/Jun sao atendidos pelo `__HISTORY__` nativo do artifact;
os datasets 15-17 existem apenas como fallback e nunca sao usados na pagina.

## Verificacao desta geracao

**1. Casamento de JQL (18 consultas reproduzidas):** a construcao de JQL do artifact
foi remontada para a data de referencia 27/08/2026 e cada consulta foi testada contra
a tabela de padroes embutida. Resultado: **18/18 casaram** com o dataset esperado,
**0** `JQL sem correspondencia`, **0** datasets orfaos.

**2. Renderizacao real (jsdom):** o `index.html` gerado foi carregado num DOM e os
tres scripts inline foram executados na ordem, com o Chart.js stubado.

- Abas montadas: `Julho 2026 (Encerrado)`, `Agosto 2026 (Ao vivo)`, `Visao Acumulada`
- **Agosto 2026:** OTD 15% | Previstos 13 | Entregues 2 | Pendentes do mes 11 |
  Em atraso (acum.) 1 | Retrabalho 60% | 6 linhas em "OTD por Projeto" |
  18 linhas em "Pendencias"
- **Julho 2026:** OTD 80% | Previstos 10 | Entregues 8 | Retrabalho 45% |
  **sem** o aviso "Periodo encerrado sem snapshot"
- **Visao Acumulada** (Mar/2026 a Ago/2026, padrao de 6 meses): OTD acumulado 52%
  (34 de 66 entregues), 32 pendentes, heatmap OTD por projeto x mes renderizado
- `window.__HISTORY__` = `2026-04, 2026-05, 2026-06, 2026-07`
- Banner de snapshot presente no fim do `<body>`
- **0** `console.error`, **0** `console.warn`, **0** excecoes em todas as tres abas

**3. Privacidade:** `index.html` nao contem `avatarUrls`, `emailAddress` nem nenhum
`accountId` (a unica ocorrencia da string "accountId" e o comentario
"Nao contem accountIds..."). Os JSONs minimais guardam apenas
`key`, `summary`, `duedate`, `resolutiondate`, `updated`, `project.key`,
`project.name`, `status.name` e `status.statusCategory.key`.

Nomes de epics e nomes de status sao publicados intencionalmente.

## Publicacao

O commit e o push sao feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub`, que roda a cada 30 minutos e faz `git add -A` + commit + push.
A geracao do snapshot **nao** executa nenhuma operacao git. O deploy no Vercel ocorre
cerca de 1 minuto depois do push.
