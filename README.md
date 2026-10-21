# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 21/10/2026 03:31** (`2026-10-21T03:31:45-03:00`)

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
| `planned_2026-07` | 10 | congelado em `__HISTORY__` |
| `planned_2026-08` | 4 | congelado em `__HISTORY__` |
| `planned_2026-09` | 8 | congelado em `__HISTORY__` |
| `planned_2026-10` | 15 | ao vivo nesta rodada |

Mais a chamada `getVisibleJiraProjects`, resolvida com os 21 projetos visíveis.

## Como foi gerado

Geração em 21/10/2026 03:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian. Foram
executadas 9 chamadas: `getVisibleJiraProjects` e 8 consultas JQL (as seis do mês corrente mais
as `planned` de mai e jun/2026, que compõem a visão acumulada e não estão congeladas em
`__HISTORY__`).

### Nenhum indicador mudou nesta rodada

Os seis conjuntos do mês corrente foram reconsultados do zero e voltaram com as mesmas
contagens e as mesmas chaves da rodada anterior (04:30 UTC / 21/10 01:30 BRT):

| Conjunto | Ao vivo nesta rodada | Rodada anterior | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | idêntico |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |

A conferência desta rodada foi feita campo a campo, e não só por contagem: cada registro
devolvido ao vivo foi comparado com o correspondente da rodada anterior (resumo, nome e
categoria de status, projeto, due date, resolution date e updated). A comparação dos oito
conjuntos reconsultados foi feita sobre a serialização canônica ordenada por chave, e todos
vieram **idênticos** — nenhum acréscimo, nenhuma remoção, nenhum campo alterado. Para
referência, o digest SHA-256 da serialização canônica do `lookahead` de 33 registros é
`fc3c7b33aa10bf9f…` e o da lista de projetos é `cc7b94d5a1583c3c…`.

A lista de projetos visíveis também foi reconsultada: **sem diferença** (mesmos 21 projetos,
mesmas chaves, mesmos tipos de issue). O gerador compara as chaves contra as da rodada
anterior e não emitiu aviso.

As `planned` de mai e jun/2026 foram conferidas ao vivo nesta rodada (7 e 1 registros, mesmas
contagens de antes). Os três meses de jul a set/2026 seguem congelados no bloco `__HISTORY__`,
como nas rodadas anteriores.

Com os dados estáveis, o `index.html` desta rodada mantém os mesmos tamanhos da anterior —
`index.html` com **164.972 bytes** e `snapshot-data.js` com **77.186 bytes** — e as únicas
diferenças observáveis são os dois carimbos de tempo (comentário no `<head>` e banner no fim
do `<body>`).

### Nota sobre a cláusula de tipo de issue

As consultas desta rodada usam `issuetype in ("Epic","Fluxo de trabalho")`, exatamente como o
artifact monta a JQL a partir dos tipos de nível 1 dos projetos visíveis. A forma reduzida
`issuetype=Epic` **não** serve: ela deixa de fora os sete projetos cujo tipo de nível 1 se chama
`Fluxo de trabalho` (CREA, EG0285, EG0286, EG0287, EG0292, EG0294 e EG291) e derrubaria, por
exemplo, o `planned_2026-10` de 15 para 10 registros. A checagem foi refeita nesta rodada e a
cláusula completa está em uso em todos os conjuntos.

### Epics com due date em out/2026 (15)

Distribuição por projeto: G0280 (DMAE) 5, EG0286 (DNIT/AC) 4, EG0240 (GOITÁ/COMPESA) 3,
EG0274 (DNIT) 2, EG291 (Arroio Feijó) 1.

Seis epics entraram em "Enviado - Aguardando Análise" ao longo de out/2026 e seis foram
concluídos no mês; quatro deles voltaram de "Enviado - Aguardando Análise" para revisão, o que
os caracteriza como retrabalho. Nenhum epic está vencido sem conclusão.

O olhar para frente registra 33 epics com due date em nov e dez/2026 — EG0274 (DNIT) 11,
EG0286 (DNIT/AC) 10, EG0285 4, EG0294 3, e um epic em cada um de EG0239, EG0240, EG0241,
EG0275 e G0280 — mesma contagem das rodadas anteriores.

## Estrutura e verificações

- Comentário `<!-- Snapshot gerado em ... -->` no início do `<head>`, com o carimbo
  `2026-10-21T03:31:45-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 21/10/2026 03:31,
  imediatamente antes do fechamento. Ocorrência única, confirmada na cauda do arquivo.
- `__HISTORY__` exposto por accessor com merge defensivo, para que a atribuição direta feita
  pelo script do artifact não apague os meses congelados.
- O bloco de dados embutido no `index.html` passou em `node --check` nesta rodada e foi
  executado em Node: carrega sem erro, expõe os 21 projetos e os 11 conjuntos, serve
  jul–set/2026 por `__HISTORY__` e preserva esses meses mesmo após uma atribuição direta a
  `window.__HISTORY__`; as 11 JQL de teste resolveram todas para os conjuntos esperados
  (15 registros de out/2026, 33 do lookahead, 21 projetos).

### Ressalvas de método

- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é o mesmo das rodadas anteriores — a última verificada em Chromium headless sem
  erros de script — e nesta rodada mudou apenas o carimbo de geração.
- A pasta de dados do Claude onde o artifact é armazenado não é legível pelo shell da sessão.
  O snapshot é reinjetado sobre o `index.html` já versionado no repositório, cuja estrutura é
  conferida a cada rodada pelos marcadores descritos acima.

## Privacidade

Os JSONs embutidos contêm apenas `key`, `summary`, nome e categoria do status, chave e nome do
projeto, due date, resolution date e updated. **Não há** `accountId`, e-mail, avatar, descrição
em ADF nem qualquer campo de pessoa.

## Publicação

- `index.html` — página estática, auto-contida.
- `snapshot-data.js` — cópia de referência do bloco de dados injetado (não é carregada pela página).
- Commit e push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 minutos.
- Deploy automático na Vercel a partir do push.
