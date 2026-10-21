# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 21/10/2026 08:30** (`2026-10-21T08:30:39-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho` (derivados dos tipos de nível 1 dos projetos visíveis)
Projetos visíveis mapeados: **21**

### Consultas resolvidas (11 consultas JQL + lista de projetos)

Mês corrente — **out/2026**, reconsultado ao vivo nesta rodada:

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
| `planned_2026-05` | 7 | conferido ao vivo nesta rodada |
| `planned_2026-06` | 1 | conferido ao vivo nesta rodada |
| `planned_2026-07` | 8 | congelado em `__HISTORY__` |
| `planned_2026-08` | 3 | congelado em `__HISTORY__` |
| `planned_2026-09` | 5 | conferido ao vivo nesta rodada |
| `planned_2026-10` | 15 | ao vivo nesta rodada |

Mais a chamada `getVisibleJiraProjects`, resolvida com os 21 projetos visíveis.

## Como foi gerado

Geração em 21/10/2026 08:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian. Foram
executadas 10 chamadas: `getVisibleJiraProjects` e 9 consultas JQL (as seis do mês corrente
mais as `planned` de mai, jun e set/2026). Jul e ago/2026 seguem congelados em `__HISTORY__`.

### Nenhum indicador mudou nesta rodada

Os seis conjuntos do mês corrente foram reconsultados do zero e voltaram com as mesmas
contagens e as mesmas chaves da rodada anterior (10:33 UTC / 21/10 07:33 BRT):

| Conjunto | Ao vivo nesta rodada | Rodada anterior | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | idêntico |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |

A conferência foi feita por chave: o conjunto de chaves devolvido ao vivo em cada um dos nove
conjuntos reconsultados foi comparado com o da rodada anterior, extraído do `snapshot-data.js`
então publicado. O gerador não emitiu nenhuma linha `MUDOU` — não houve acréscimo nem remoção
em nenhum deles. O `lookahead_2026-10` reconsultado tem a mesma forma canônica (mesmo hash MD5)
do JSON mínimo da rodada anterior.

A lista de projetos visíveis também foi reconsultada: **sem diferença** (mesmos 21 projetos,
mesmas chaves, mesmos tipos de issue, conferido por hash da forma canônica). O gerador compara
as chaves contra as da rodada anterior e não emitiu aviso.

Com os dados estáveis, o `index.html` desta rodada mantém os mesmos tamanhos da anterior —
`index.html` com **161.100 bytes** e `snapshot-data.js` com **73.314 bytes** — e as únicas
diferenças observáveis são os dois carimbos de tempo (comentário no `<head>` e banner no fim
do `<body>`).

### Nota sobre a cláusula de tipo de issue

As consultas desta rodada usam `issuetype in ("Epic","Fluxo de trabalho")`, exatamente como o
artifact monta a JQL a partir dos tipos de nível 1 dos projetos visíveis. A forma reduzida
`issuetype=Epic` **não** serve: ela deixa de fora os projetos cujo tipo de nível 1 se chama
`Fluxo de trabalho` e derrubaria, por exemplo, o `planned_2026-10` de 15 para 10 registros.
A cláusula completa está em uso em todos os conjuntos desta rodada.

### Epics com due date em out/2026 (15)

Distribuição por projeto: G0280 (DMAE) 5, EG0286 (DNIT/AC) 4, EG0240 (GOITÁ/COMPESA) 3,
EG0274 (DNIT) 2, EG291 (Arroio Feijó) 1.

Seis epics entraram em "Enviado - Aguardando Análise" ao longo de out/2026 e seis foram
concluídos no mês; quatro deles voltaram de "Enviado - Aguardando Análise" para revisão, o que
os caracteriza como retrabalho. Nenhum epic está vencido sem conclusão.

O olhar para frente registra 33 epics com due date em nov e dez/2026 — mesma contagem das
rodadas anteriores.

## Estrutura e verificações

- Comentário `<!-- Snapshot gerado em ... -->` no início do `<head>`, com o carimbo
  `2026-10-21T08:30:39-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única,
  byte a byte idêntica ao `snapshot-data.js` publicado ao lado (73.314 bytes) — conferido
  nesta rodada.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 21/10/2026 08:30,
  imediatamente antes do fechamento. Ocorrência única, confirmada na cauda do arquivo.
- `__HISTORY__` exposto por accessor com merge defensivo, para que a atribuição direta feita
  pelo script do artifact não apague os meses congelados.
- O bloco de dados foi executado em Node nesta rodada: carrega sem erro, expõe os 21 projetos
  e os 11 conjuntos, serve jul e ago/2026 por `__HISTORY__`, e as 11 JQL de teste resolveram
  todas para os conjuntos esperados (15 registros de out/2026, 33 do lookahead, 21 projetos).
- **Fonte conferida contra o artifact ao vivo nesta rodada.** O HTML atual do Live Artifact
  `pr03-relatorio-indicadores-epics` foi obtido diretamente do desktop e é **byte a byte
  idêntico** (MD5 `6a2b6462a4efbec1890af4494a7f0b74`, 87.509 bytes) ao `_artifact_src.html`
  versionado neste repositório, que é a base sobre a qual o snapshot é reinjetado.

### Ressalvas de método

- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é o mesmo das rodadas anteriores — a última verificada em Chromium headless sem
  erros de script — e nesta rodada mudou apenas o carimbo de geração.
- A pasta de dados do Claude onde o artifact é armazenado não é legível pelo shell da sessão.
  Nesta rodada o HTML do artifact foi obtido pelo canal de artifacts do desktop e conferido
  por hash contra a cópia versionada (ver acima); o snapshot é reinjetado sobre o `index.html`
  já versionado no repositório, cuja estrutura é conferida a cada rodada pelos marcadores
  descritos acima.

## Privacidade

Os JSONs embutidos contêm apenas `key`, `summary`, nome e categoria do status, chave e nome do
projeto, due date, resolution date e updated. **Não há** `accountId`, e-mail, avatar, descrição
em ADF nem qualquer campo de pessoa. A conferência desta rodada no `index.html` gerado não
encontrou nenhuma ocorrência de `avatarUrls`, `emailAddress` ou de endereço de e-mail
corporativo (a única ocorrência da string `accountId` é a linha de comentário do próprio
cabeçalho do bloco de dados).

## Publicação

- `index.html` — página estática, auto-contida.
- `snapshot-data.js` — cópia de referência do bloco de dados injetado (não é carregada pela página).
- Commit e push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 minutos.
- Deploy automático na Vercel a partir do push.
