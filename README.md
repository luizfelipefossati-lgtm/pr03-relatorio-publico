# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 22/10/2026 13:02** (`2026-10-22T13:02:03-03:00`)

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

Geração em 22/10/2026 13:02 BRT, com consulta ao vivo ao Jira. Foram feitas **8 chamadas
bem-sucedidas** ao conector MCP Atlassian: `getVisibleJiraProjects` e sete consultas JQL —
`planned`, `overdue`, `lookahead`, `resolved` e `rework` do mês corrente, mais `sent` em duas
janelas quinzenais (ver ressalva abaixo).

Os conjuntos de 2026-07, 2026-08 e 2026-09, e os `planned` de mai e jun/2026, foram mantidos das
rodadas de fechamento: são meses encerrados, servidos pelo `__HISTORY__` congelado, de modo que
rebuscá-los só poderia introduzir divergência em relação ao fechamento.

A montagem usou o gerador versionado na raiz, `_gen_snapshot.py`, que parte do
`_artifact_src.html` limpo, insere o carimbo no início do `<head>`, injeta o bloco `<script>` do
snapshot **antes** do script principal do artifact e acrescenta o banner como último elemento do
`<body>`. Os dados desta rodada estão em `_snap/_data1022b.py`, que grava os seis JSONs do mês
corrente em `_snap/`. O `snapshot-data.js` publicado ao lado é a cópia de referência do mesmo
bloco, e foi conferido como idêntico ao embutido no `index.html`.

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

O conector esteve **instável nesta rodada**: várias chamadas estouraram o limite de 180 s e duas
voltaram com HTTP 502 do gateway, exigindo repetição. A consulta `sent` do mês cheio não
completou em nenhuma tentativa e foi dividida em duas janelas — `("2026-10-01","2026-10-16")`,
com 6 resultados, e `("2026-10-16","2026-10-31")`, vazia —, cuja união é o conjunto publicado.
Como a segunda janela não teve nenhuma transição, o `rework` foi apurado apenas sobre a primeira,
sem perda de cobertura.

### Nenhum indicador mudou nesta rodada

Os onze conjuntos voltaram com a **mesma composição** da rodada anterior (22/10 09:35 BRT) —
mesmas chaves de epic em cada conjunto, mesmas datas e mesmos status. A comparação chave a chave
contra a versão em `HEAD` não acusou inclusão, remoção nem alteração de campo em nenhum conjunto;
`_snap/resolved_2026-10.json` e `_snap/lookahead_2026-10.json` aparecem como modificados apenas
por ordenação e serialização. O conjunto de 21 projetos visíveis e seus tipos de issue também
permanecem os mesmos.

O olhar para frente registra 33 epics com due date em nov e dez/2026 — mesma contagem das
rodadas anteriores.

## Estrutura e verificações

- Comentário `<!-- Snapshot gerado em ... -->` no início do `<head>`, com o carimbo
  `2026-10-22T13:02:03-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única,
  byte a byte idêntica ao `snapshot-data.js` publicado ao lado (73.594 bytes) — conferido
  nesta rodada.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 22/10/2026 13:02,
  imediatamente antes do fechamento. Ocorrência única, confirmada na cauda do arquivo.
- Bloco de dados posicionado **antes** do script principal do artifact, de modo que a
  sobrescrita de `callMcpTool` já esteja em vigor quando a página inicializa — confirmado
  nesta rodada (bloco no byte 93.078; script principal no byte 95.528).
- `__HISTORY__` exposto por accessor com merge defensivo, para que a atribuição direta feita
  pelo script do artifact não apague os meses congelados.
- O bloco de dados passou por `node --check` (v22) e foi **executado** em Node nesta rodada:
  quatro das JQLs que o artifact monta em tempo de execução para out/2026 — `planned`,
  `lookahead`, `sent` e `rework` — foram submetidas ao resolvedor embutido e devolveram,
  respectivamente, 15, 33, 6 e 4 registros, e `getVisibleJiraProjects` devolveu os 21 projetos
  — ou seja, nenhum padrão testado ficou sem correspondência.
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

- `index.html` — página estática, auto-contida (161.380 bytes, MD5 `edc8b95a04c0d235f5de3950c248424d`).
- `snapshot-data.js` — cópia de referência do bloco de dados injetado, não carregada pela
  página (73.594 bytes, MD5 `080237a10abf41856446b9b0d22982af`).
- Commit e push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 minutos.
- Deploy automático na Vercel a partir do push.
