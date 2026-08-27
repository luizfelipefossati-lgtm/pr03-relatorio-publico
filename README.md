# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 15:13 (2026-08-27T15:13:28-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como Epic:** Epic, Fluxo de trabalho (descobertos por `hierarchyLevel === 1`)
- **Projetos visiveis no snapshot:** 19
- **Tamanho de `index.html`:** 148,5 KB (152.126 bytes, md5 `07784f239c290cff7dd17a3445fda89b`, 1.025 linhas)

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

O bloco injetado entra **depois** do bloco nativo `window.__HISTORY__` (que congela
2026-04 a 2026-06) e **antes** do script principal, de modo que os dois conjuntos
historicos coexistem. Linhas verificadas nesta geracao: comentario `Snapshot gerado em`
na 18 -> `window.__HISTORY__=` na 282 -> shim do snapshot na 286 -> script principal
na 404 -> banner na 1023 -> `</body>` na 1024.

O HTML base usado na geracao e o `_artifact_src.html` deste repositorio (947 linhas,
md5 `6a2b6462a4efbec1890af4494a7f0b74`). A pasta `Documents\Claude\Artifacts` nao e
montada no sandbox Linux, entao a equivalencia com o artifact ao vivo foi conferida por
amostragem: contagem total de linhas (947), o bloco construtor de JQL (linhas 430-459,
que define as seis consultas do mes) e o fechamento do arquivo (linhas 940-947) batem
exatamente. **Ressalva honesta:** isso e uma verificacao por amostragem, nao byte a byte —
uma edicao do artifact fora dessas faixas passaria despercebida. Se o artifact for
editado, `_artifact_src.html` precisa ser atualizado junto.

Em contrapartida, a integridade do gerador **foi** confirmada byte a byte: removendo do
`index.html` recem-gerado as tres injecoes conhecidas (comentario, shim e banner), o
resultado tem md5 `6a2b6462a4efbec1890af4494a7f0b74` — identico ao `_artifact_src.html`.
Ou seja, as injecoes sao as unicas diferencas introduzidas.

## Politica de meses adotada nesta geracao

Esta execucao reconsultou todas as janelas descritas na tarefa: mes corrente (Ago/2026),
mes anterior (Jul/2026) e os seis `planned` da Visao Acumulada — **17 consultas** ao Jira
(16 JQL + `getVisibleJiraProjects`).

Os numeros agregados de Jul/2026 saem **identicos** aos das duas geracoes anteriores
(`planned` 10, `overdue` 1, `look` 27, `sent.total` 11, `sent.rework` 5): nao houve deriva
no periodo ja encerrado. Julho continua sendo servido por `__HISTORY__` (congelado), com
`_frozen_at` = `2026-08-27`.

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

Renderizado na aba "Julho 2026 / Encerrado": OTD **80%**, 8 de 10 entregues (5 no prazo,
3 com pequeno atraso), 2 pendentes, retrabalho 45% (5/11).

## Indicadores do mes corrente (Ago/2026)

Valores lidos do DOM renderizado, nao recalculados a mao.

| Indicador | Valor |
|---|---|
| OTD | 15% (2 de 13) |
| Epics previstos | 13 |
| Entregues | 2 (0 no prazo · 2 pequeno atraso) |
| Pendentes do mes | 11 |
| Em atraso acumulado | 1 |
| Enviados no mes (uniao sent + resolved) | 5 |
| Retrabalho | 60% (3/5) |

Visao Acumulada (Mar-Ago/2026, janela padrao de 6 meses): **OTD 52%**, 34 de 66 entregues,
32 pendentes (48% do total).

## Chamadas dinamicas resolvidas (17)

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

Ago/2026 e o mes ao vivo. Jul/2026 e servido por `__HISTORY__` (datasets 8-13 agregados em
`months["2026-07"]`), mas os datasets seguem disponiveis como fallback de JQL.
Abr/Mai/Jun sao atendidos pelo `__HISTORY__` nativo do artifact; os datasets 15-17
existem apenas como fallback.

A Visao Acumulada abre por padrao em Mar/2026 a Ago/2026 (janela de 6 meses ancorada na
data de geracao).

## Verificacao desta geracao

**1. Casamento de JQL (16 assercoes, no gerador).** A construcao de JQL do artifact foi
remontada para a data de referencia 27/08/2026 — incluindo o `ETQ` dinamico
`issuetype in ("Epic","Fluxo de trabalho")` — e cada JQL testada contra a lista de
`PATTERNS` antes de gravar o arquivo. Resultado: **16/16**, cada consulta resolvendo para o
dataset correto. O gerador aborta se algum padrao divergir.

**2. Validacao dos dados na origem.** Cada um dos 16 JSONs minimais foi conferido com `jq`
antes da montagem: `planned_*` sem nenhuma `duedate` fora do mes; `overdue_*` com
`duedate` maxima 2026-03-25 e zero itens com `statusCategory=done`; `lookahead_2026-07`
em 2026-08-07..2026-09-30 e `lookahead_2026-08` em 2026-09-04..2026-10-31;
`resolved_*` com todas as `resolutiondate` dentro do mes; `rework_*` subconjunto de
`sent_*` em ambos os meses. Schema conferido em todos os arquivos.

**3. Simulacao das chamadas (26 assercoes, no artefato publicado).** O bloco do snapshot foi
extraido do `index.html` final e executado em Node; as 12 consultas dos dois meses, os 6
`planned` do acumulado e o `getVisibleJiraProjects` foram disparados contra o
`callMcpTool` substituido. Todas devolveram exatamente as contagens esperadas.

**4. Sintaxe.** Os 4 blocos inline do `index.html` foram validados: o `application/json` de
metadados faz parse, e os 3 blocos JS compilam com `vm.Script` (30.986 / 63.866 / 33.637
caracteres).

**5. Merge do `__HISTORY__`.** Simulando a atribuicao tardia `window.__HISTORY__ = {...}`
que tentava sobrescrever `2026-07`, a entrada do snapshot sobreviveu intacta e uma chave
nova (`2026-01`) foi aceita normalmente.

**6. Renderizacao real em DOM.** `jsdom` executou o `index.html` publicado de ponta a ponta
com o Chart.js substituido por stub. Resultado: spinner sumiu, `#EA` (area de erro global)
vazio, **zero** erros de console, **zero** avisos `JQL sem correspondencia`, log
`Snapshot estatico carregado` presente, 3 graficos instanciados. As 3 abas foram
construidas ("Julho 2026 / Encerrado", "Agosto 2026 / Ao vivo", "Visao Acumulada /
Historico") com Agosto ativa por padrao. Tabelas de Agosto: 6 linhas em OTD por Projeto,
18 em Pendencias, 4 em Entregas do Mes, 9 em Retrabalho. Os cliques nas abas de Julho
(6 tabelas) e da Visao Acumulada (10 + 41 linhas) renderizaram sem erro.

Uma checagem inicial acusou o texto "sem snapshot" na pagina; a investigacao mostrou que a
unica ocorrencia esta **dentro do codigo-fonte** do `<script>` do artifact (o literal do
ramo de fallback), nunca renderizada no DOM. Falso positivo — a aba de Julho exibe os dados
congelados normalmente.

**7. Privacidade.** `index.html` tem 0 ocorrencias de `avatarUrls`, `emailAddress`,
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
- **`rework` igual a `sent` nos dois meses.** Em Jul (5/5) e Ago (3/3), todo item enviado
  tambem casou com `status changed from "Enviado - Aguardando Analise"`, o que empurra o
  indicador de retrabalho para perto do teto. Vale confirmar com a equipe se isso reflete
  o processo real ou se e efeito das transicoes de status duplicadas acima.
- **Respostas inconsistentes do MCP.** Novamente uma consulta devolveu um resultado cujo
  `webUrl` ecoava uma JQL diferente da enviada (no `lookahead_2026-07`). O resultado
  suspeito foi descartado e a consulta refeita ate o `webUrl` bater com a JQL; o intervalo
  final foi validado com `jq`. Vale conferir esse eco em execucoes futuras.
- **Equivalencia do `_artifact_src.html`** verificada por amostragem, nao byte a byte
  (ver secao "Como funciona").

**Nao verificado:** os valores desenhados dentro dos graficos Chart.js (o stub nao pinta
nada) e o diff linha a linha contra a geracao anterior.

## Publicacao

O commit e o push sao feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub`, que roda a cada 30 minutos e faz `git add -A` + commit + push.
A geracao do snapshot **nao** executa nenhuma operacao git. O deploy no Vercel ocorre
cerca de 1 minuto depois do push.
