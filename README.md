# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 23/10/2026 22:31** (`2026-10-23T22:31:57-03:00`)

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
| `planned_2026-10` | 15 | reconsultado ao vivo (idêntico ao gravado) |

Mais a chamada `getVisibleJiraProjects`, resolvida com os 21 projetos visíveis.

Meses congelados servidos pelo `__HISTORY__` embutido: **2026-07, 2026-08, 2026-09** (além de
2026-04 a 2026-06, que já viajam no HTML-fonte do artifact).

## Como foi gerado

Geração em 23/10/2026 22:31 BRT (24/10/2026 01:31 UTC), em execução agendada e autônoma, com consulta ao
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
`<body>`. A procedência desta rodada está registrada em `_snap/_data1023k.py`. O
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

Três ressalvas de forma, sem efeito sobre os dados:

- A resposta de `getVisibleJiraProjects` excedeu o limite de tokens da ferramenta e foi entregue
  como arquivo pelo próprio conector; os campos mínimos foram extraídos desse arquivo e
  conferidos por MD5 canônico contra o `_projects_min.json` em uso — `cf7b59de6bf68fc6489470cf9018bd6e`
  dos dois lados.
- A consulta `lookahead` foi pedida com a **projeção completa** de seis campos. A
  resposta excedeu o limite e veio como arquivo; os 33 registros foram extraídos dele na mesma
  forma aninhada usada em `_snap/` e conferidos por **MD5 canônico** —
  `a38b4d9c77584b034fe2d7c2d0e61cd9` dos dois lados, registro a registro.
- As cinco `planned` da visão acumulada foram novamente pedidas com **projeção completa** de
  seis campos. As de mai e jun/2026 vieram inteiras na resposta e foram conferidas **campo a
  campo** contra `_snap/`; as de jul, ago e set/2026 foram executadas por subagente, com a mesma
  projeção e a mesma forma aninhada, e conferidas por **MD5 canônico**. Todos os 24 registros
  (7 + 1 + 8 + 3 + 5) bateram, inclusive na ordem de retorno.

### Nenhum dado mudou nesta rodada

Os **onze conjuntos** e a lista de 21 projetos visíveis voltaram do Jira **idênticos** aos
gravados em `_snap/`, inclusive na ordem de retorno — a única exceção conhecida e inofensiva é o
`resolved` do mês corrente, tratada logo abaixo. A alteração de due date das epics do EG0240,
registrada na rodada das 16:10 BRT de hoje, permanece refletida: `EG0240-43`, `EG0240-5` e `EG0240-4`
seguem com due date **26/10/2026**, em **Em Revisão**, sem resolution date, e nenhuma delas conta
como atrasada na data desta geração.

A conferência foi feita por MD5 canônico (`jq -S -c 'sort_by(.key)'`) contra os JSONs em `_snap/`,
o que neutraliza diferenças de ordem de retorno do Jira — relevante porque as JQLs de `sent`,
`resolved` e `rework` que o artifact monta não têm `ORDER BY`. Além do MD5 canônico, nesta rodada
também foi conferida a **impressão digital da ordem** de cada conjunto (MD5 da sequência de
chaves), lado a lado entre o que o Jira devolveu agora e o que está gravado:

| Conjunto | MD5 canônico | Nesta rodada |
|---|---|---|
| `planned_2026-10` | `3fe8384df0f1b8cd9245df2901c72ef6` | inalterado (conjunto e ordem) |
| `overdue_2026-10` | `58e0494c51d30eb3494f7c9198986bb9` | inalterado (vazio dos dois lados) |
| `lookahead_2026-10` | `a38b4d9c77584b034fe2d7c2d0e61cd9` | inalterado (conjunto e ordem) |
| `sent_2026-10` | `1f995242d71713c8c893953b6abdacb5` | inalterado (conjunto e ordem) |
| `resolved_2026-10` | `de830431136ac892018b47b0219897c3` | inalterado como conjunto; ordem diferente |
| `rework_2026-10` | `92ac5a1b9b202bf88b9a210c5e83dbcd` | inalterado (conjunto e ordem) |
| `planned_2026-05` | `7b561eb1414d581166c3ffb820fa6c81` | inalterado (conjunto e ordem) |
| `planned_2026-06` | `b483385522e7aba4bff7eaac7c70c70b` | inalterado (conjunto e ordem) |
| `planned_2026-07` | `89c430d7301c007c96e90c518882ae87` | inalterado (conjunto e ordem) |
| `planned_2026-08` | `4e49e617a3b2a5abc00c9a1b5f858fa6` | inalterado (conjunto e ordem) |
| `planned_2026-09` | `1b5fac7dd7a83479c00b2ef40f75e97c` | inalterado (conjunto e ordem) |
| `_projects_min` | `cf7b59de6bf68fc6489470cf9018bd6e` | inalterado |

**Nenhum JSON de `_snap/` foi reescrito.** Foram regerados apenas o `index.html`, o
`snapshot-data.js` e este README, que diferem da rodada anterior somente nos carimbos de data e
hora — os dois arquivos mantêm exatamente os mesmos tamanhos (161.380 e 73.594 bytes), porque os
carimbos trocados têm o mesmo número de caracteres.

Como nas rodadas anteriores, o `resolved` do mês corrente é consultado sem `ORDER BY` e o Jira
devolveu os **mesmos seis registros em ordem diferente** da gravada em `_snap/`. Por conjunto os
dois lados são exatamente iguais (mesmo MD5 canônico `de830431136ac892018b47b0219897c3`), e a
ordem não é carregada pelo relatório: o gerador funde `sent` e `resolved` em um mapa por chave e
ordena os detalhes pelo sinalizador de retrabalho. O arquivo foi mantido como estava.

O olhar para frente registra 33 epics com due date em nov e dez/2026 — mesma contagem das
rodadas anteriores.

## Estrutura e verificações

- Comentário `<!-- Snapshot gerado em ... -->` no início do `<head>`, com o carimbo
  `2026-10-23T22:31:57-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única,
  byte a byte idêntica ao `snapshot-data.js` publicado ao lado (73.594 bytes) — conferido
  nesta rodada.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 23/10/2026 22:31,
  imediatamente antes do fechamento. Ocorrência única, confirmada na cauda do arquivo, que
  termina íntegra em `</div>\n</body>\n</html>`.
- Bloco de dados posicionado **antes** do script principal do artifact (bloco em 22.444–95.519,
  script principal do artifact começando exatamente em 95.519), de modo que a sobrescrita de
  `callMcpTool` já esteja em vigor quando a página inicializa — confirmado nesta rodada por
  comparação de posição no arquivo.
- `__HISTORY__` exposto por accessor com merge defensivo, preservando os meses congelados
  diante de uma atribuição direta `window.__HISTORY__ = {...}` como a que o script do artifact
  faz.
- O bloco de dados foi **executado** em Node nesta rodada: as seis JQLs que o artifact monta em
  tempo de execução para out/2026 — `planned`, `overdue`, `lookahead`, `sent`, `resolved` e
  `rework` — foram submetidas ao resolvedor embutido e devolveram, respectivamente, 15, 0, 33,
  6, 6 e 4 registros; as cinco JQLs `planned` da visão acumulada devolveram 7, 1, 8, 3 e 5;
  `getVisibleJiraProjects` devolveu os 21 projetos, e `__HISTORY__` expôs 2026-07, 2026-08 e
  2026-09. Nenhum padrão testado ficou sem correspondência (nenhum aviso
  `JQL sem correspondencia no snapshot`). O conjunto `planned_2026-10` servido pelo bloco traz
  as três epics de EG0240 com due date 2026-10-26, confirmando que a alteração do Jira chegou
  à página gerada.
- Removidos do `index.html` o comentário, o bloco de dados e o banner, o restante é **idêntico
  byte a byte** ao `_artifact_src.html` — conferido nesta rodada (diferença de comprimento = 0).
- `_artifact_src.html`, base do snapshot: 87.509 bytes,
  MD5 `6a2b6462a4efbec1890af4494a7f0b74` — **reconferido ao vivo nesta rodada** contra o HTML do
  Live Artifact: idêntico.

### Ressalvas de método

- A pasta `Documents\Claude\Artifacts` segue inacessível tanto ao shell da sessão quanto a
  `device_list_dir` (área protegida). Isso não é bloqueio: o HTML do Live Artifact foi obtido
  pela via oficial de staging de artifacts (`device_stage_files` com `artifact_ids`) e comparado
  ao `_artifact_src.html` — mesmos 87.509 bytes e mesmo MD5
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

- `index.html` — página estática, auto-contida (161.380 bytes, MD5 `5ce0028343ef08143daee4bdbb9ea855`).
- `snapshot-data.js` — cópia de referência do bloco de dados injetado, não carregada pela
  página (73.594 bytes, MD5 `5b9b46f62015066fd1f6d559043143ad`).
- Commit e push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 minutos.
- Deploy automático na Vercel a partir do push.
