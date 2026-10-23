# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 23/10/2026 13:31** (`2026-10-23T13:31:57-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho` (derivados dos tipos de nível 1 dos projetos visíveis)
Projetos visíveis mapeados: **21**

### Consultas resolvidas (11 conjuntos + lista de projetos)

Mês corrente — **out/2026**, todos reconsultados ao vivo nesta rodada:

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-10` | Epics com due date em out/2026 | 15 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 0 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 6 |
| `resolved_2026-10` | Concluídos em out/2026 | 6 |
| `rework_2026-10` | Enviados em out/2026 que voltaram de "Enviado - Aguardando Análise" | 4 |

Visão acumulada (últimos 6 meses) — as cinco consultas de meses encerrados também foram refeitas
ao vivo nesta rodada, como reconferência:

| Conjunto | Registros | Origem nesta rodada |
|---|---:|---|
| `planned_2026-05` | 7 | reconsultado ao vivo (idêntico ao congelado) |
| `planned_2026-06` | 1 | reconsultado ao vivo (idêntico ao congelado) |
| `planned_2026-07` | 8 | reconsultado ao vivo (idêntico ao congelado) |
| `planned_2026-08` | 3 | reconsultado ao vivo (idêntico ao congelado) |
| `planned_2026-09` | 5 | reconsultado ao vivo (idêntico ao congelado) |
| `planned_2026-10` | 15 | consultado ao vivo |

Mais a chamada `getVisibleJiraProjects`, resolvida com os 21 projetos visíveis.

Meses congelados servidos pelo `__HISTORY__` embutido: **2026-07, 2026-08, 2026-09** (além de
2026-04 a 2026-06, que já viajam no HTML-fonte do artifact).

## Como foi gerado

Geração em 23/10/2026 13:31 BRT (16:31 UTC), em execução agendada e autônoma, com consulta ao
vivo ao Jira. Foram feitas **12 chamadas bem-sucedidas** ao conector MCP Atlassian:
`getVisibleJiraProjects`, as seis consultas JQL do mês corrente — `planned`, `overdue`,
`lookahead`, `sent`, `resolved` e `rework` — e as cinco consultas `planned` da visão acumulada
(mai a set/2026). Cada uma em uma única janela de mês cheio, sem paginação (`hasNextPage` falso
em todas) e sem nenhuma tentativa malsucedida.

Os demais conjuntos de 2026-07, 2026-08 e 2026-09 (`overdue`, `lookahead`, `sent`, `resolved` e
`rework`) foram mantidos das rodadas de fechamento: são meses encerrados, servidos pelo
`__HISTORY__` congelado, de modo que rebuscá-los só poderia introduzir divergência em relação ao
fechamento.

A montagem usou o gerador versionado na raiz, `_gen_snapshot.py`, que parte do
`_artifact_src.html` limpo, insere o carimbo no início do `<head>`, injeta o bloco `<script>` do
snapshot **antes** do script principal do artifact e acrescenta o banner como último elemento do
`<body>`. A procedência desta rodada está registrada em `_snap/_data1023d.py`. O
`snapshot-data.js` publicado ao lado é a cópia de referência do mesmo bloco, e foi conferido como
idêntico ao embutido no `index.html`.

### Filtro de tipo de issue

A JQL usada é a **mesma que o artifact monta em tempo de execução**:
`issuetype in ("Epic","Fluxo de trabalho")`, derivada dos tipos de nível 1 (`hierarchyLevel === 1`)
dos projetos visíveis — confirmados ao vivo nesta rodada a partir dos 21 projetos. O filtro
simplificado `issuetype=Epic` **não** reproduz o relatório: os projetos EG0285, EG0286, EG0291,
EG0292, EG0294, EG0287 e CREA nomeiam seu tipo de nível Epic como `Fluxo de trabalho` e ficariam
de fora.

### Via de acesso ao Jira nesta rodada

Todas as chamadas foram feitas pelo conector **MCP Atlassian**, com projeção mínima de campos
(`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`). Nenhuma credencial
passou pela sessão nem aparece em log. Nenhuma tentativa de login web em Jira, GitHub ou Vercel
foi feita.

O conector esteve estável: as doze consultas completaram na primeira tentativa, sem HTTP 502, sem
estouro de tempo e sem necessidade de backoff ou de dividir o período.

Duas ressalvas de forma, sem efeito sobre os dados:

- A resposta de `getVisibleJiraProjects` excedeu o limite de tokens da ferramenta e foi entregue
  como arquivo pelo próprio conector; os campos mínimos foram extraídos desse arquivo e
  conferidos por MD5 canônico contra o `_projects_min.json` em uso — `cf7b59de6bf68fc6489470cf9018bd6e`
  dos dois lados.
- A consulta `lookahead` e as cinco `planned` da visão acumulada foram executadas com projeção
  reduzida (`duedate`) justamente para não estourar o limite; a conferência desses conjuntos foi
  feita por **comparação do conjunto de chaves** (33 chaves no `lookahead`; 7, 1, 8, 3 e 5 nos
  acumulados), e não por MD5 de registro completo. Como os seis conjuntos do mês corrente foram
  conferidos **campo a campo** (chave, projeto, due date, status, categoria, resolution date e
  updated), a verificação por chaves é suficiente para os conjuntos de meses encerrados.

### Nenhum indicador mudou nesta rodada

Os doze conjuntos reconsultados voltaram com a **mesma composição** da rodada anterior (23/10
09:27 BRT), tanto no mês corrente quanto nos cinco `planned` da visão acumulada. Além da
comparação campo a campo do mês corrente, a conferência foi feita por MD5 canônico
(`jq -S -c 'sort_by(.key)'`) contra os JSONs já gravados em `_snap/`, o que neutraliza diferenças
de ordem de retorno do Jira — relevante porque as JQLs de `sent`, `resolved` e `rework` que o
artifact monta não têm `ORDER BY`. Todos os conjuntos e a lista de 21 projetos visíveis bateram
integralmente:

| Conjunto | MD5 canônico |
|---|---|
| `planned_2026-10` | `beb20fe094f4f249b43b20e9becc072f` |
| `overdue_2026-10` | `58e0494c51d30eb3494f7c9198986bb9` |
| `lookahead_2026-10` | `a38b4d9c77584b034fe2d7c2d0e61cd9` |
| `sent_2026-10` | `1f995242d71713c8c893953b6abdacb5` |
| `resolved_2026-10` | `de830431136ac892018b47b0219897c3` |
| `rework_2026-10` | `92ac5a1b9b202bf88b9a210c5e83dbcd` |
| `planned_2026-05` | `7b561eb1414d581166c3ffb820fa6c81` |
| `planned_2026-06` | `b483385522e7aba4bff7eaac7c70c70b` |
| `planned_2026-07` | `89c430d7301c007c96e90c518882ae87` |
| `planned_2026-08` | `4e49e617a3b2a5abc00c9a1b5f858fa6` |
| `planned_2026-09` | `1b5fac7dd7a83479c00b2ef40f75e97c` |
| `_projects_min` | `cf7b59de6bf68fc6489470cf9018bd6e` |

Como nada mudou, **nenhum JSON em `_snap/` foi reescrito**; o `index.html` foi regerado apenas
para renovar o carimbo.

O olhar para frente registra 33 epics com due date em nov e dez/2026 — mesma contagem das
rodadas anteriores.

## Estrutura e verificações

- Comentário `<!-- Snapshot gerado em ... -->` no início do `<head>`, com o carimbo
  `2026-10-23T13:31:57-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única,
  byte a byte idêntica ao `snapshot-data.js` publicado ao lado (73.594 bytes) — conferido
  nesta rodada.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 23/10/2026 13:31,
  imediatamente antes do fechamento. Ocorrência única, confirmada na cauda do arquivo, que
  termina íntegra em `</div>\n</body>\n</html>`.
- Bloco de dados posicionado **antes** do script principal do artifact (bloco em 22.444–95.519,
  script principal do artifact começando exatamente em 95.519), de modo que a sobrescrita de
  `callMcpTool` já esteja em vigor quando a página inicializa — confirmado nesta rodada por
  comparação de posição no arquivo.
- `__HISTORY__` exposto por accessor com merge defensivo. Testado nesta rodada: após uma
  atribuição direta `window.__HISTORY__ = {...}` tentando sobrescrever 2026-09, como a que o
  script do artifact faz, os meses congelados continuam presentes e intactos, e uma chave nova
  (2026-04) é aceita normalmente.
- O bloco de dados foi **executado** em Node nesta rodada: as seis JQLs que o artifact monta em
  tempo de execução para out/2026 — `planned`, `overdue`, `lookahead`, `sent`, `resolved` e
  `rework` — foram submetidas ao resolvedor embutido e devolveram, respectivamente, 15, 0, 33,
  6, 6 e 4 registros; as cinco JQLs `planned` da visão acumulada devolveram 7, 1, 8, 3 e 5;
  `getVisibleJiraProjects` devolveu os 21 projetos, e `__HISTORY__` expôs 2026-07, 2026-08 e
  2026-09. Nenhum padrão testado ficou sem correspondência (nenhum aviso
  `JQL sem correspondencia no snapshot`).
- Removidos do `index.html` o comentário, o bloco de dados e o banner, o restante é **idêntico
  byte a byte** ao `_artifact_src.html` — conferido nesta rodada (diferença de comprimento = 0).
- `_artifact_src.html`, base do snapshot: 87.509 bytes,
  MD5 `6a2b6462a4efbec1890af4494a7f0b74` — **reconferido ao vivo nesta rodada** contra o HTML do
  Live Artifact: idêntico.

### Ressalvas de método

- A pasta `Documents\Claude\Artifacts` continua inacessível ao shell da sessão (área protegida).
  Nesta rodada, porém, o HTML do Live Artifact foi obtido pela via oficial de staging de
  artifacts e comparado ao `_artifact_src.html`: mesmos 87.509 bytes e mesmo MD5
  `6a2b6462a4efbec1890af4494a7f0b74`. O layout publicado está, portanto, em dia com o artifact.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é o mesmo das rodadas anteriores — a última verificada em Chromium headless sem
  erros de script — e a validação desta rodada foi feita em Node sobre o bloco de dados
  extraído do `index.html` gerado.

## Privacidade

Os JSONs embutidos contêm apenas `key`, `summary`, nome e categoria do status, chave e nome do
projeto, due date, resolution date e updated. **Não há** `accountId`, e-mail, avatar, descrição
em ADF nem qualquer campo de pessoa. A conferência desta rodada no `index.html` gerado não
encontrou nenhuma ocorrência de `avatarUrls`, `emailAddress`, `iconUrl`, `displayName`,
`atlassianAccountId` ou `projectTypeKey` (a única ocorrência da string `accountId` é a linha de
comentário do próprio cabeçalho do bloco de dados).

## Publicação

- `index.html` — página estática, auto-contida (161.380 bytes, MD5 `ae6d91b4fd3d7a8426520e20d6ee09dd`).
- `snapshot-data.js` — cópia de referência do bloco de dados injetado, não carregada pela
  página (73.594 bytes, MD5 `70050a602d3970fb3d1eef0f938145b8`).
- Commit e push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 minutos.
- Deploy automático na Vercel a partir do push.
