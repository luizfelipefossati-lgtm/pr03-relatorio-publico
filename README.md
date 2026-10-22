# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 22/10/2026 08:34** (`2026-10-22T08:34:15-03:00`)

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

Mês corrente — **out/2026**:

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-10` | Epics com due date em out/2026 | 15 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 0 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 6 |
| `resolved_2026-10` | Concluídos em out/2026 | 6 |
| `rework_2026-10` | Enviados em out/2026 que voltaram de "Enviado - Aguardando Análise" | 4 |

Visão acumulada (últimos 6 meses) — **todos os seis meses reconsultados ao vivo nesta rodada**:

| Conjunto | Registros | Origem nesta rodada |
|---|---:|---|
| `planned_2026-05` | 7 | consultado ao vivo |
| `planned_2026-06` | 1 | consultado ao vivo |
| `planned_2026-07` | 8 | consultado ao vivo |
| `planned_2026-08` | 3 | consultado ao vivo |
| `planned_2026-09` | 5 | consultado ao vivo |
| `planned_2026-10` | 15 | consultado ao vivo |

Mais a chamada `getVisibleJiraProjects`, resolvida com os 21 projetos visíveis.

Meses congelados servidos pelo `__HISTORY__` embutido: **2026-07, 2026-08, 2026-09** (além de
2026-04 a 2026-06, que já viajam no HTML-fonte do artifact).

## Como foi gerado

Geração em 22/10/2026 08:34 BRT, com consulta ao vivo ao Jira. Foram feitas **10 chamadas** ao
conector MCP Atlassian: `getVisibleJiraProjects` e 9 consultas JQL — `planned`, `overdue`,
`lookahead`, `sent`, `resolved` e `rework` do mês corrente, mais uma consulta cobrindo
`duedate` de 01/05/2026 a 30/06/2026 (dividida por mês na montagem) e duas sondagens de
contagem para mai/2026 e jun/2026.

Os conjuntos `planned_2026-07`, `planned_2026-08` e `planned_2026-09` foram mantidos da rodada
anterior: são meses encerrados, servidos pelo `__HISTORY__` congelado, de modo que rebuscá-los
só poderia introduzir divergência em relação ao fechamento. A lista de projetos e o conjunto
`lookahead_2026-10` foram rebuscados e conferidos por hash contra a rodada anterior — idênticos,
e por isso reaproveitados byte a byte. Os demais nove conjuntos foram buscados do zero.

A montagem usou o gerador da rodada `_snap/_live1022a.py`, que reescreve o carimbo no início do
`<head>`, substitui o bloco `<script>` do snapshot — que vem **antes** do script principal do
artifact — e regrava o banner como último elemento do `<body>`. O `snapshot-data.js` publicado
ao lado é a cópia de referência do mesmo bloco, e foi conferido como idêntico ao embutido no
`index.html`. O HTML-fonte do Live Artifact fica em local protegido e não é legível pela sessão
Cowork; a base usada é o `index.html` já publicado, cuja estrutura corresponde ao artifact
(sem alterações no artifact desde 27/07/2026).

### Filtro de tipo de issue

A JQL usada é a **mesma que o artifact monta em tempo de execução**:
`issuetype in ("Epic","Fluxo de trabalho")`, derivada dos tipos de nível 1 (`hierarchyLevel === 1`)
dos projetos visíveis. O filtro simplificado `issuetype=Epic` **não** reproduz o relatório: os
projetos EG0285, EG0286 e EG0291 nomeiam seu tipo de nível Epic como `Fluxo de trabalho` e ficariam
de fora. Conferido nesta rodada: com `issuetype=Epic` o mês corrente cairia de 15 para 10 epics
previstos, de 6 para 4 envios e de 6 para 4 concluídos.

### Via de acesso ao Jira nesta rodada

O conector **MCP Atlassian respondeu normalmente** — todas as chamadas foram feitas por ele, com
projeção mínima de campos (`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`),
sem necessidade de recorrer à CLI local `Documents\Claude\jira-cli\jira_query.py`. Nenhuma
credencial passou pela sessão nem aparece em log. Nenhuma tentativa de login web em Jira, GitHub
ou Vercel foi feita.

### Nenhum indicador mudou nesta rodada

Os onze conjuntos voltaram com a **mesma composição** da rodada anterior (21/10 16:34 BRT) —
mesmas chaves de epic em cada conjunto, mesmas datas e mesmos status; a comparação chave a chave
contra a versão em `HEAD` não acusou inclusão nem remoção em nenhum dos seis `planned`. O conjunto
de 21 projetos visíveis e seus tipos de issue também permanecem os mesmos.

O olhar para frente registra 33 epics com due date em nov e dez/2026 — mesma contagem das
rodadas anteriores.

## Estrutura e verificações

- Comentário `<!-- Snapshot gerado em ... -->` no início do `<head>`, com o carimbo
  `2026-10-22T08:34:15-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única,
  byte a byte idêntica ao `snapshot-data.js` publicado ao lado (73.594 bytes) — conferido
  nesta rodada.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 22/10/2026 08:34,
  imediatamente antes do fechamento. Ocorrência única, confirmada na cauda do arquivo.
- Bloco de dados posicionado **antes** do script principal do artifact, de modo que a
  sobrescrita de `callMcpTool` já esteja em vigor quando a página inicializa — confirmado
  nesta rodada (bloco no byte 22.522; próximo `<script>` no byte 96.116).
- `__HISTORY__` exposto por accessor com merge defensivo, para que a atribuição direta feita
  pelo script do artifact não apague os meses congelados.
- O bloco de dados passou por `node --check` (v22) nesta rodada: sintaxe válida, com os 21
  projetos, os 3 meses congelados e os 11 conjuntos presentes no `SNAP`/`DATASETS` lidos de
  volta do arquivo gerado.
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
encontrou nenhuma ocorrência de `avatarUrls`, `emailAddress`, `iconUrl` ou `self` (a única
ocorrência da string `accountId` é a linha de comentário do próprio cabeçalho do bloco de dados).

## Publicação

- `index.html` — página estática, auto-contida (161.380 bytes, MD5 `24666af19e566296cdd992d5440cf4cb`).
- `snapshot-data.js` — cópia de referência do bloco de dados injetado, não carregada pela
  página (73.594 bytes, MD5 `7669996a23f9193c33c56b1b71254bd6`).
- Commit e push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 minutos.
- Deploy automático na Vercel a partir do push.
