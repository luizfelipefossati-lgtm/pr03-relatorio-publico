# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 11:17 (2026-08-27T11:17:07-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como Epic:** Fluxo de trabalho, Epic (descobertos por `hierarchyLevel === 1`)
- **Projetos visiveis no snapshot:** 19
- **Tamanho de `index.html`:** 148,2 KB (151.784 bytes, md5 `6c8bfc662ac09dd8bc2a5eb6ededf938`)

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

O artifact tem cinco blocos `<script>`. O bloco injetado entra **depois** do bloco nativo
`window.__HISTORY__` (que congela 2026-04 a 2026-06) e **antes** do script principal, de
modo que os dois conjuntos historicos coexistem. Offsets verificados nesta geracao:
bloco nativo 22.453 -> bloco do snapshot 53.581 -> script principal 117.606.

O HTML base usado na geracao e o `_artifact_src.html` deste repositorio (947 linhas,
md5 `6a2b6462a4efbec1890af4494a7f0b74`). A pasta `Documents\Claude\Artifacts` e uma
localizacao protegida e **nao pode ser montada** no sandbox, entao a comparacao com o
artifact atual foi feita pela ferramenta de leitura de arquivos: contagem de linhas (947
em ambos) e conferencia das linhas-ancora finais (935-947), identicas. Se o artifact for
editado, `_artifact_src.html` precisa ser atualizado junto.

## Correcao aplicada nesta geracao

O script principal do artifact executa `window.__HISTORY__ = { ... }` — uma **atribuicao
direta**, nao um merge. Qualquer chave gravada pelo snapshot antes desse ponto seria
apagada, e a aba mensal do mes anterior cairia no ramo `info.lock` de `loadMonth()`,
exibindo "Periodo encerrado sem snapshot" em vez dos dados.

Ate agora isso funcionava apenas porque o bloco injetado ficava posicionado depois da
atribuicao nativa — uma dependencia fragil da ordem dos blocos `<script>` do artifact.
Nesta geracao `window.__HISTORY__` passou a ser definido com `Object.defineProperty`, com
um setter que **mescla** em vez de sobrescrever e da precedencia as chaves do snapshot.
O posicionamento correto foi mantido; o accessor e a garantia caso a ordem mude.

Teste de regressao executado: apos uma atribuicao tardia `window.__HISTORY__ = {...}`
contendo uma chave conflitante (`2026-07`) e uma nova (`2026-01`), a entrada do snapshot
permanece intacta e a chave nova e aceita.

## Mes anterior congelado (`__HISTORY__["2026-07"]`)

Montado com a mesma logica de `loadMonth()` (uniao de `sent` + `resolved` por chave,
`rework` marcando `rw:true`, ordenacao com retrabalho primeiro):

| Campo | Valor |
|---|---|
| `planned` | 10 epics |
| `overdue` | 1 epic |
| `look` | 27 epics |
| `sent.total` | 11 |
| `sent.rework` | 5 |
| `period` | `2026-07-01` a `2026-07-31` ("Julho 2026") |

**Observacao:** julho foi reconsultado nesta geracao (as 5 consultas mensais foram
executadas para o mes corrente e o anterior). A consulta `resolved` de julho retornou
**7** epics, contra **8** na geracao anterior. `sent.total` permaneceu 11 porque o epic
a menos ja entrava na uniao pela consulta `sent`. Nao ha indicio de perda de dado, mas a
divergencia fica registrada — periodo encerrado nao deveria variar.

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
| 12 | resolved Jul/2026 | `resolved_2026-07` | 7 |
| 13 | rework Jul/2026 | `rework_2026-07` | 5 |
| 14 | planned Mar/2026 (acumulado) | `planned_2026-03` | 7 |
| 15 | planned Abr/2026 (fallback) | `planned_2026-04` | 15 |
| 16 | planned Mai/2026 (fallback) | `planned_2026-05` | 7 |
| 17 | planned Jun/2026 (fallback) | `planned_2026-06` | 1 |

Ago/2026 e o mes ao vivo. Jul/2026 e servido por `__HISTORY__`, mas os datasets ficam
disponiveis como fallback. Abr/Mai/Jun sao atendidos pelo `__HISTORY__` nativo do
artifact; os datasets 15-17 existem apenas como fallback.

A Visao Acumulada abre por padrao em Mar/2026 a Ago/2026 (janela de 6 meses ancorada na
data de geracao).

## Verificacao desta geracao

**1. Casamento de JQL (16 consultas reproduzidas):** a construcao de JQL do artifact foi
remontada para a data de referencia 27/08/2026 — incluindo o `ETQ` dinamico
`issuetype in ("Fluxo de trabalho","Epic")` — e cada consulta foi executada contra o
`callMcpTool` substituido. Resultado: **16/16** devolveram exatamente o dataset esperado
(comparacao por igualdade profunda, nao so por contagem), **0** avisos de
`JQL sem correspondencia`, **0** datasets orfaos.

Essa verificacao pegou um defeito real: as aspas internas dos padroes `DURING (...)`
nao estavam escapadas para o literal JavaScript, o que gerava `SyntaxError` e derrubaria
o script inteiro do snapshot na pagina publicada. Corrigido e reverificado.

**2. `__HISTORY__` apos a execucao real dos blocos:** `2026-04` (planned 19), `2026-05`
(15), `2026-06` (2) e `2026-07` (10), todos com `overdue`, `look`, `sent` e `period`
presentes.

**3. Estrutura do HTML:** comentario `<!-- Snapshot gerado em ... -->` no inicio do
`<head>`; ordem nativo -> snapshot -> principal confirmada; banner amarelo depois do
ultimo `</script>` e antes de `</body>`.

**4. Privacidade:** `index.html` nao contem `avatarUrls`, `emailAddress`, `accountId`
nem `iconUrl` (0 ocorrencias de cada). Os JSONs minimais guardam apenas `key`, `summary`,
`duedate`, `resolutiondate`, `updated`, `project.key`, `project.name`, `status.name` e
`status.statusCategory.key` — validado campo a campo nos 16 arquivos.

Nomes de epics e nomes de status sao publicados intencionalmente.

**Nao verificado nesta geracao:** renderizacao real em DOM (jsdom). A instalacao do pacote
travou no sandbox e foi abandonada para nao estourar o tempo da tarefa. As checagens
acima cobrem a camada de dados e a estrutura do arquivo, mas nao os numeros finais
exibidos nos graficos.

## Publicacao

O commit e o push sao feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub`, que roda a cada 30 minutos e faz `git add -A` + commit + push.
A geracao do snapshot **nao** executa nenhuma operacao git. O deploy no Vercel ocorre
cerca de 1 minuto depois do push.
