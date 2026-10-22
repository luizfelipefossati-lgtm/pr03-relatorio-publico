# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 22/10/2026 15:33** (`2026-10-22T15:33:57-03:00`)

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

Visão acumulada (últimos 6 meses):

| Conjunto | Registros | Origem nesta rodada |
|---|---:|---|
| `planned_2026-05` | 7 | reaproveitado (mês encerrado) |
| `planned_2026-06` | 1 | reaproveitado (mês encerrado) |
| `planned_2026-07` | 8 | reaproveitado (mês encerrado) |
| `planned_2026-08` | 3 | reaproveitado (mês encerrado) |
| `planned_2026-09` | 5 | reaproveitado (mês encerrado) |
| `planned_2026-10` | 15 | consultado ao vivo |

Mais a chamada `getVisibleJiraProjects`, resolvida com os 21 projetos visíveis.

Meses congelados servidos pelo `__HISTORY__` embutido: **2026-07, 2026-08, 2026-09** (além de
2026-04 a 2026-06, que já viajam no HTML-fonte do artifact).

## Como foi gerado

Geração em 22/10/2026 15:33 BRT, em execução agendada e autônoma, com consulta ao vivo ao Jira.
Foram feitas **7 chamadas bem-sucedidas** ao conector MCP Atlassian: `getVisibleJiraProjects` e as
seis consultas JQL do mês corrente — `planned`, `overdue`, `lookahead`, `sent`, `resolved` e
`rework` —, cada uma em uma única janela de mês cheio, sem paginação (`hasNextPage` falso em
todas) e sem nenhuma tentativa malsucedida.

Os conjuntos de 2026-07, 2026-08 e 2026-09, e os `planned` de mai e jun/2026, foram mantidos das
rodadas de fechamento: são meses encerrados, servidos pelo `__HISTORY__` congelado, de modo que
rebuscá-los só poderia introduzir divergência em relação ao fechamento.

A montagem usou o gerador versionado na raiz, `_gen_snapshot.py`, que parte do
`_artifact_src.html` limpo, insere o carimbo no início do `<head>`, injeta o bloco `<script>` do
snapshot **antes** do script principal do artifact e acrescenta o banner como último elemento do
`<body>`. A procedência desta rodada está registrada em `_snap/_data1022d.py`. O
`snapshot-data.js` publicado ao lado é a cópia de referência do mesmo bloco, e foi conferido como
idêntico ao embutido no `index.html`.

### Filtro de tipo de issue

A JQL usada é a **mesma que o artifact monta em tempo de execução**:
`issuetype in ("Epic","Fluxo de trabalho")`, derivada dos tipos de nível 1 (`hierarchyLevel === 1`)
dos projetos visíveis. O filtro simplificado `issuetype=Epic` **não** reproduz o relatório: os
projetos EG0285, EG0286, EG0291, EG0292, EG0294, EG0287 e CREA nomeiam seu tipo de nível Epic como
`Fluxo de trabalho` e ficariam de fora.

### Via de acesso ao Jira nesta rodada

Todas as chamadas foram feitas pelo conector **MCP Atlassian**, com projeção mínima de campos
(`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`). Nenhuma credencial
passou pela sessão nem aparece em log. Nenhuma tentativa de login web em Jira, GitHub ou Vercel
foi feita.

Ao contrário da rodada anterior, **o conector esteve estável**: as sete consultas completaram na
primeira tentativa, sem HTTP 502, sem estouro de tempo e sem necessidade de backoff ou de dividir
o período.

Uma ressalva de forma, sem efeito sobre os dados: a resposta de `getVisibleJiraProjects` excedeu o
limite de tokens da ferramenta e foi entregue como arquivo pelo próprio conector. Os campos
mínimos (`key`, `name`, `issueTypes[name, hierarchyLevel]`) foram extraídos desse arquivo e
conferidos por MD5 canônico contra o `_projects_min.json` em uso
(`c5873d9e86471ebc97cc091448095b42` dos dois lados).

### Nenhum indicador mudou nesta rodada

Os sete conjuntos reconsultados voltaram com a **mesma composição** da rodada anterior (22/10
14:53 BRT). A conferência foi feita comparando os JSONs mínimos recém-extraídos contra os já
gravados em `_snap/`: `planned`, `overdue`, `lookahead`, `sent` e `rework` bateram integralmente,
e `resolved` traz o mesmo conjunto de seis epics apenas em outra ordem de retorno do Jira — a JQL
que o artifact monta para esse conjunto não tem `ORDER BY`, então a ordem devolvida não é estável
entre rodadas e não indica alteração de dado. A lista de 21 projetos visíveis e seus tipos de
issue também permanece a mesma. Como nada mudou, **nenhum JSON em `_snap/` foi reescrito**; o
`index.html` foi regerado apenas para renovar o carimbo.

O olhar para frente registra 33 epics com due date em nov e dez/2026 — mesma contagem das
rodadas anteriores.

## Estrutura e verificações

- Comentário `<!-- Snapshot gerado em ... -->` no início do `<head>`, com o carimbo
  `2026-10-22T15:33:57-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única,
  byte a byte idêntica ao `snapshot-data.js` publicado ao lado (73.594 bytes) — conferido
  nesta rodada.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 22/10/2026 15:33,
  imediatamente antes do fechamento. Ocorrência única, confirmada na cauda do arquivo.
- Bloco de dados posicionado **antes** do script principal do artifact, de modo que a
  sobrescrita de `callMcpTool` já esteja em vigor quando a página inicializa — confirmado
  nesta rodada por comparação de posição no arquivo.
- `__HISTORY__` exposto por accessor com merge defensivo. Testado nesta rodada: após uma
  atribuição direta `window.__HISTORY__ = {...}`, como a que o script do artifact faz, os meses
  congelados continuam presentes.
- O bloco de dados passou por `node --check` (v22.23.4) e foi **executado** em Node nesta rodada:
  as seis JQLs que o artifact monta em tempo de execução para out/2026 — `planned`, `overdue`,
  `lookahead`, `sent`, `resolved` e `rework` — foram submetidas ao resolvedor embutido e
  devolveram, respectivamente, 15, 0, 33, 6, 6 e 4 registros; `getVisibleJiraProjects` devolveu
  os 21 projetos, e `__HISTORY__` expôs 2026-07, 2026-08 e 2026-09. Nenhum padrão testado ficou
  sem correspondência (nenhum aviso `JQL sem correspondencia no snapshot`).
- Removidos do `index.html` o comentário, o bloco de dados e o banner, o restante é **idêntico
  byte a byte** ao `_artifact_src.html` — conferido nesta rodada.
- `_artifact_src.html`, base do snapshot: 87.509 bytes,
  MD5 `6a2b6462a4efbec1890af4494a7f0b74` — inalterado em relação à última rodada em que foi
  conferido contra o artifact ao vivo.

### Ressalvas de método

- **O HTML do Live Artifact não pôde ser reconferido nesta rodada.** A pasta
  `Documents\Claude\Artifacts` é uma área protegida para sessões Cowork e não é legível nem
  pelo shell da sessão nem pelas ferramentas de arquivo. O snapshot foi gerado sobre o
  `_artifact_src.html` versionado (hash acima, igual ao da última conferência bem-sucedida).
  Se o artifact ao vivo tiver sido editado desde então, esta página não refletirá a alteração
  de layout — apenas os dados são novos.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é o mesmo das rodadas anteriores — a última verificada em Chromium headless sem
  erros de script — e a validação desta rodada foi feita em Node sobre o bloco de dados
  extraído do `index.html` gerado.

## Privacidade

Os JSONs embutidos contêm apenas `key`, `summary`, nome e categoria do status, chave e nome do
projeto, due date, resolution date e updated. **Não há** `accountId`, e-mail, avatar, descrição
em ADF nem qualquer campo de pessoa. A conferência desta rodada no `index.html` gerado não
encontrou nenhuma ocorrência de `avatarUrls`, `emailAddress`, `iconUrl`, `"self"` ou
`projectTypeKey` (a única ocorrência da string `accountId` é a linha de comentário do próprio
cabeçalho do bloco de dados).

## Publicação

- `index.html` — página estática, auto-contida (161.380 bytes, MD5 `4f4ae3ed0144f8fc4c9d8c23df00c3a4`).
- `snapshot-data.js` — cópia de referência do bloco de dados injetado, não carregada pela
  página (73.594 bytes, MD5 `1739adf76128bbfcfdf7f1cc21c41ebe`).
- Commit e push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 minutos.
- Deploy automático na Vercel a partir do push.
