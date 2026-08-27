# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 14:16 (2026-08-27T14:16:11-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como Epic:** Epic, Fluxo de trabalho (descobertos por `hierarchyLevel === 1`)
- **Projetos visiveis no snapshot:** 19
- **Tamanho de `index.html`:** 148,6 KB (152.128 bytes, md5 `1fd71887743ab851ab541dff3c0ffac9`)

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

O bloco injetado entra **depois** do bloco nativo `window.__HISTORY__` (que congela
2026-04 a 2026-06) e **antes** do script principal, de modo que os dois conjuntos
historicos coexistem. Linhas verificadas nesta geracao: comentario `Snapshot gerado em`
na 18 -> `window.__HISTORY__=` na 282 -> shim do snapshot na 284 -> script principal
(`CONSTANTS`) na 363 -> banner na 1025 -> `</body>` na 1026.

O HTML base usado na geracao e o `_artifact_src.html` deste repositorio (947 linhas,
md5 `6a2b6462a4efbec1890af4494a7f0b74`). A pasta `Documents\Claude\Artifacts` nao e
montada no sandbox Linux, entao a equivalencia com o artifact atual foi confirmada por
duas vias: (a) removendo do `index.html` anterior as tres injecoes conhecidas, o resultado
bateu **byte a byte** (mesmo md5) com o `_artifact_src.html`; (b) contagem de linhas (947),
contagem de ocorrencias de um padrao composto (319) e comprimento da linha 281 (30.984
caracteres) conferem entre o artifact ao vivo e a copia local. Se o artifact for editado,
`_artifact_src.html` precisa ser atualizado junto.

## Politica de meses adotada nesta geracao

Diferente da geracao anterior, esta execucao **reconsultou todas as janelas** descritas na
tarefa: mes corrente (Ago/2026), mes anterior (Jul/2026) e os seis `planned` da Visao
Acumulada — 21 consultas ao Jira no total.

Os numeros agregados de Jul/2026 saem **identicos** aos do snapshot anterior
(`planned` 10, `overdue` 1, `look` 27, `sent.total` 11, `sent.rework` 5), ou seja, nao houve
deriva no periodo ja encerrado. Julho continua sendo servido por `__HISTORY__` (congelado),
com `_frozen_at` = `2026-08-27`.

Consequencia pratica: como cada execucao reconsulta o mes anterior, uma alteracao
retroativa no Jira **passa** a aparecer no relatorio ate o fim do mes seguinte. Para travar
Julho definitivamente, mova a chave `2026-07` para o `window.__HISTORY__` nativo do
artifact.

## Mes anterior congelado (`__HISTORY__["2026-07"]`)

| Campo | Valor |
|---|---|
| `planned` | 10 epics |
| `overdue` | 1 epic |
| `look` | 27 epics |
| `sent.total` | 11 |
| `sent.rework` | 5 |
| `period` | `2026-07-01` a `2026-07-31` ("Julho 2026") |
| `_frozen_at` | `2026-08-27` |

Renderizado na aba "Julho 2026 / Encerrado": OTD **80%**, 8 de 10 entregues dentro do
periodo (o artifact usa `oiAt`/`dnAt`, que so contam entregas com data de resolucao
ate 2026-07-31), retrabalho 45%.

## Indicadores do mes corrente (Ago/2026)

Valores lidos do DOM renderizado, nao recalculados a mao.

| Indicador | Valor |
|---|---|
| OTD | 15% (2 de 13) |
| Epics previstos | 13 |
| Entregues | 2 |
| No prazo | 0 |
| Pequeno atraso (mesmo mes) | 2 |
| Pendentes do mes | 11 |
| Em atraso acumulado | 1 |
| Enviados no mes (uniao sent + resolved) | 5 |
| Retrabalho | 60% (3) |

Visao Acumulada (Mar-Ago/2026, janela padrao de 6 meses): **OTD 52%**, 34 de 66 entregues.

## Chamadas dinamicas resolvidas (17)

| # | Chamada | Dataset | Itens | Origem |
|---|---|---|---|---|
| 1 | `getVisibleJiraProjects` | `projects` | 19 projetos | consulta nova |
| 2 | planned Ago/2026 | `planned_2026-08` | 13 | consulta nova |
| 3 | overdue Ago/2026 | `overdue_2026-08` | 1 | consulta nova |
| 4 | lookahead Set-Out/2026 | `lookahead_2026-08` | 30 | consulta nova |
| 5 | sent Ago/2026 | `sent_2026-08` | 3 | consulta nova |
| 6 | resolved Ago/2026 | `resolved_2026-08` | 5 | consulta nova |
| 7 | rework Ago/2026 | `rework_2026-08` | 3 | consulta nova |
| 8 | planned Jul/2026 | `planned_2026-07` | 10 | consulta nova |
| 9 | overdue Jul/2026 | `overdue_2026-07` | 1 | consulta nova |
| 10 | lookahead Ago-Set/2026 | `lookahead_2026-07` | 27 | consulta nova |
| 11 | sent Jul/2026 | `sent_2026-07` | 5 | consulta nova |
| 12 | resolved Jul/2026 | `resolved_2026-07` | 8 | consulta nova |
| 13 | rework Jul/2026 | `rework_2026-07` | 5 | consulta nova |
| 14 | planned Mar/2026 (acumulado) | `planned_2026-03` | 7 | consulta nova |
| 15 | planned Abr/2026 (fallback) | `planned_2026-04` | 15 | consulta nova |
| 16 | planned Mai/2026 (fallback) | `planned_2026-05` | 7 | consulta nova |
| 17 | planned Jun/2026 (fallback) | `planned_2026-06` | 1 | consulta nova |

Ago/2026 e o mes ao vivo. Jul/2026 e servido por `__HISTORY__` (datasets 8-13 agregados em
`months["2026-07"]`), mas os datasets seguem disponiveis como fallback de JQL.
Abr/Mai/Jun sao atendidos pelo `__HISTORY__` nativo do artifact; os datasets 15-17
existem apenas como fallback.

A Visao Acumulada abre por padrao em Mar/2026 a Ago/2026 (janela de 6 meses ancorada na
data de geracao).

## Verificacao desta geracao

**1. Casamento de JQL (19 assercoes).** A construcao de JQL do artifact foi remontada para
a data de referencia 27/08/2026 — incluindo o `ETQ` dinamico
`issuetype in ("Epic","Fluxo de trabalho")` — e cada consulta executada em Node contra o
`callMcpTool` substituido: 6 consultas do mes corrente, 6 do mes anterior, 6 `planned` da
Visao Acumulada e `getVisibleJiraProjects`. Resultado: **19/19 PASS**, cada uma devolvendo
exatamente o dataset esperado. Uma JQL fora do escopo cai no `return []` sem lancar erro.

**2. Sintaxe JS.** Os 3 blocos `<script>` inline do `index.html` publicado foram extraidos
e validados com `node --check`: todos OK (30.984 / 63.866 / 33.635 caracteres).

**3. Merge do `__HISTORY__`.** Antes do shim havia `2026-04..06`; depois, `2026-04..07`.
Simulando uma atribuicao tardia `window.__HISTORY__ = {...}` que tentava sobrescrever
`2026-07`, a entrada do snapshot sobreviveu intacta (10 epics em `planned`) e a chave nova
foi aceita.

**4. Renderizacao real em DOM (novo nesta geracao).** `jsdom` foi instalado no sandbox e o
`index.html` publicado foi executado de ponta a ponta com o Chart.js substituido por um
stub. Resultado: spinner de carregamento sumiu, `#EA` (area de erro global) vazio, **zero**
erros de console, **zero** avisos `JQL sem correspondencia`. As 3 abas foram construidas
("Julho 2026 / Encerrado", "Agosto 2026 / Ao vivo", "Visao Acumulada / Historico") com
Agosto ativa por padrao. Tabelas preenchidas: 6 linhas em OTD por projeto, 18 em
Pendencias, 4 em Entregas do Mes, 51 na Visao Acumulada. O clique na aba de Julho renderizou
os dados congelados — **sem** o aviso "periodo encerrado sem snapshot".

**5. Privacidade.** `index.html` tem 0 ocorrencias de `avatarUrls`, `emailAddress`,
`iconUrl`, `displayName`, `atlassianAccountId` e `@engeplus`. A unica ocorrencia da string
`accountId` e o proprio texto do aviso de privacidade no comentario do shim. Os JSONs
minimais guardam apenas `key`, `summary`, `duedate`, `resolutiondate`, `updated`,
`project.key`, `project.name`, `status.name` e `status.statusCategory.key`.

Nomes de epics e nomes de status sao publicados intencionalmente.

### Ressalvas levantadas nesta execucao

- **Status quase-duplicados no Jira.** Convivem `Enviado - Aguardando Analise`,
  `Enviado - Aguardando Analise1` e `Enviado- Aguardando Analise` (sem espaco antes do
  hifen). As consultas `sent` e `rework` filtram apenas a primeira grafia, entao
  **subcontam** envios reais — por exemplo, itens do EG0256 e do EG0239 que estao em
  `...Analise1` nao entram no `sent`. Isso e comportamento do artifact, nao do snapshot;
  corrigir exige padronizar os status no Jira ou ampliar a JQL do artifact.
- **Respostas inconsistentes do MCP.** Em duas ocasioes o endpoint devolveu um resultado
  cujo `webUrl` ecoava uma JQL diferente da enviada. Os resultados suspeitos foram
  descartados e as consultas refeitas ate o `webUrl` bater com a JQL. Vale conferir esse
  eco em execucoes futuras.

**Nao verificado:** os valores desenhados dentro dos graficos Chart.js (o stub nao pinta
nada) e o diff linha a linha contra a geracao anterior.

## Publicacao

O commit e o push sao feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub`, que roda a cada 30 minutos e faz `git add -A` + commit + push.
A geracao do snapshot **nao** executa nenhuma operacao git. O deploy no Vercel ocorre
cerca de 1 minuto depois do push.
