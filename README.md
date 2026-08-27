# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 12:10 (2026-08-27T12:10:48-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como Epic:** Epic, Fluxo de trabalho (descobertos por `hierarchyLevel === 1`)
- **Projetos visiveis no snapshot:** 19
- **Tamanho de `index.html`:** 152,5 KB (156.167 bytes, md5 `249e79e0bcf1962802ebf3e050e88f1b`)

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

O bloco injetado entra **depois** do bloco nativo `window.__HISTORY__` (que congela
2026-04 a 2026-06) e **antes** do script principal, de modo que os dois conjuntos
historicos coexistem. Linhas verificadas nesta geracao: `window.__HISTORY__=` na 282 ->
shim do snapshot na 286 -> script principal (`CONSTANTS`) na 363 -> banner na 1025 ->
`</body>` na 1026.

O HTML base usado na geracao e o `_artifact_src.html` deste repositorio (947 linhas,
md5 `6a2b6462a4efbec1890af4494a7f0b74` — **inalterado** desde a geracao anterior). A pasta
`Documents\Claude\Artifacts` nao e montada no sandbox, entao a conferencia contra o
artifact atual foi feita pela ferramenta de leitura: contagem de linhas (947 em ambos) e
contagem de ocorrencias de sete padroes estruturais (`duedate>=`, `Enviado - Aguardando`,
`resolved>=`, `statusCategory!=Done`, `__HISTORY__`, `FROZEN`, `acMonths`) — 15 em ambos.
Se o artifact for editado, `_artifact_src.html` precisa ser atualizado junto.

## Politica de meses congelados adotada nesta geracao

O proprio artifact declara em `loadMonth()`: *"PREMISSA: periodo encerrado = dados
congelados; nunca consultar Jira ao vivo"*. Seguindo essa premissa, esta geracao
**reconsultou apenas o mes corrente (Ago/2026)**. Julho/2026 e os meses Mar-Jun/2026 da
Visao Acumulada foram **reaproveitados do snapshot anterior**, sem nova consulta ao Jira.

Isso e uma mudanca deliberada em relacao a geracao de 11:17, que reconsultou julho e
encontrou `resolved` = 7 contra 8 na geracao anterior a ela — exatamente o tipo de
variacao que um periodo encerrado nao deveria ter. Congelar de fato elimina essa deriva
e reduz de 21 para 7 as consultas ao Jira por execucao.

Consequencia pratica: se um mes encerrado precisar ser corrigido, a correcao tem de ser
feita explicitamente (apagando a chave correspondente do `snapshot-data.js` antes de rodar
a tarefa).

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
| 8 | planned Jul/2026 | `planned_2026-07` | 10 | congelado |
| 9 | overdue Jul/2026 | `overdue_2026-07` | 1 | congelado |
| 10 | lookahead Ago-Set/2026 | `lookahead_2026-07` | 27 | congelado |
| 11 | sent Jul/2026 | `sent_2026-07` | 5 | congelado |
| 12 | resolved Jul/2026 | `resolved_2026-07` | 7 | congelado |
| 13 | rework Jul/2026 | `rework_2026-07` | 5 | congelado |
| 14 | planned Mar/2026 (acumulado) | `planned_2026-03` | 7 | congelado |
| 15 | planned Abr/2026 (fallback) | `planned_2026-04` | 15 | congelado |
| 16 | planned Mai/2026 (fallback) | `planned_2026-05` | 7 | congelado |
| 17 | planned Jun/2026 (fallback) | `planned_2026-06` | 1 | congelado |

Ago/2026 e o mes ao vivo. Jul/2026 e servido por `__HISTORY__`, mas os datasets ficam
disponiveis como fallback. Abr/Mai/Jun sao atendidos pelo `__HISTORY__` nativo do
artifact; os datasets 15-17 existem apenas como fallback.

A Visao Acumulada abre por padrao em Mar/2026 a Ago/2026 (janela de 6 meses ancorada na
data de geracao).

## Verificacao desta geracao

**1. Casamento de JQL (21 assercoes).** A construcao de JQL do artifact foi remontada para
a data de referencia 27/08/2026 — incluindo o `ETQ` dinamico
`issuetype in ("Epic","Fluxo de trabalho")` — e cada consulta executada em Node contra o
`callMcpTool` substituido: 12 consultas mensais (Ago e Jul), 6 consultas `planned` da
Visao Acumulada, `getVisibleJiraProjects`, e o teste de merge do `__HISTORY__`.
Resultado: **21/21 PASS**, **0** avisos de `JQL sem correspondencia`, **0** datasets orfaos.

Essa verificacao pegou um defeito real: os padroes `DURING (...)` sairam com barra
invertida duplicada (`\\(` no valor da string em vez de `\(`), o que faria as regexes de
`sent` e `rework` nunca casarem e cairia no `return []` — os cartoes de Enviados e
Retrabalho apareceriam zerados. Corrigido e reverificado.

**2. Sintaxe JS.** Os 3 blocos `<script>` inline do `index.html` publicado foram extraidos
e validados com `node --check`: todos OK.

**3. Merge do `__HISTORY__`.** Apos uma atribuicao tardia `window.__HISTORY__ = {...}` com
as chaves 2026-04/05/06, as chaves resultantes sao `2026-04, 2026-05, 2026-06, 2026-07` —
a entrada do snapshot sobrevive e as nativas sao aceitas.

**4. Estrutura do HTML.** Comentario `<!-- Snapshot gerado em ... -->` na linha 18, logo
apos `<head>`; ordem nativo -> snapshot -> principal confirmada; banner amarelo na linha
1025, imediatamente antes de `</body>`.

**5. Diff minimo.** Apenas **6 linhas** diferem da geracao anterior: 18 (comentario do
head), 287 (`Gerado em` do shim), 295 (`SNAP`), 297 (`DATASETS`), 359 (`console.log`) e
1025 (banner). A linha 299 (`PATTERNS`) ficou **identica**, como esperado — a janela de
meses nao mudou.

**6. Privacidade.** `index.html` tem 0 ocorrencias de `avatarUrls`, `emailAddress`,
`iconUrl`, `displayName`, `assignee`, `atlassianAccountId`, `universal_avatar` e do prefixo
de accountId `712020:`. A unica ocorrencia da string `accountId` e o proprio texto do aviso
de privacidade no comentario do shim. Os JSONs minimais guardam apenas `key`, `summary`,
`duedate`, `resolutiondate`, `updated`, `project.key`, `project.name`, `status.name` e
`status.statusCategory.key`.

Nomes de epics e nomes de status sao publicados intencionalmente.

**Nao verificado nesta geracao:** renderizacao real em DOM (jsdom nao esta instalado no
sandbox). As checagens acima cobrem a camada de dados, a sintaxe e a estrutura do arquivo,
mas nao os numeros finais desenhados nos graficos.

## Publicacao

O commit e o push sao feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub`, que roda a cada 30 minutos e faz `git add -A` + commit + push.
A geracao do snapshot **nao** executa nenhuma operacao git. O deploy no Vercel ocorre
cerca de 1 minuto depois do push.
