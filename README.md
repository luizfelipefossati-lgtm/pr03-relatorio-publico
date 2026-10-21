# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 21/10/2026 00:30** (`2026-10-21T00:30:47-03:00`)

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
| `rework_2026-10` | Retrabalho em out/2026 | 4 |

Visão acumulada (últimos 6 meses):

| Conjunto | Registros | Origem nesta rodada |
|---|---:|---|
| `planned_2026-05` | 7 | consultado ao vivo nesta rodada |
| `planned_2026-06` | 1 | consultado ao vivo nesta rodada |
| `planned_2026-07` | 10 | congelado (mês encerrado, servido por `__HISTORY__`) |
| `planned_2026-08` | 4 | congelado (mês encerrado, servido por `__HISTORY__`) |
| `planned_2026-09` | 8 | congelado (mês encerrado, servido por `__HISTORY__`) |
| `planned_2026-10` | 15 | ao vivo nesta rodada |

Mais a chamada `getVisibleJiraProjects`, resolvida com os 21 projetos visíveis.

## Como foi gerado

Geração em 21/10/2026 00:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian. Foram
executadas 9 chamadas: `getVisibleJiraProjects` e 8 consultas JQL (as seis do mês corrente mais
as `planned` de mai e jun/2026, que compõem a visão acumulada e não estão congeladas em
`__HISTORY__`).

### Nenhum indicador mudou nesta rodada

Os seis conjuntos do mês corrente foram reconsultados do zero e voltaram com as mesmas
contagens e as mesmas chaves da rodada anterior (03:27 UTC / 20/10 23:31 BRT):

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
categoria de status, projeto, due date, resolution date e updated). Para o `lookahead` de 33
registros e para a lista de projetos a comparação foi feita por digest SHA-256 da serialização
canônica — `e84f25daa972ace9…` e `42e8a14f9d6551ac…`, ambos iguais aos da rodada anterior.
Todos os oito conjuntos reconsultados vieram **idênticos**.

A lista de projetos visíveis também foi reconsultada: **sem diferença** (mesmos 21 projetos,
mesmas chaves). O gerador compara as chaves contra as da rodada anterior e não emitiu aviso.

As `planned` de mai e jun/2026 foram reconsultadas ao vivo nesta rodada (7 e 1 registros,
mesmas contagens de antes). Os três meses de jul a set/2026 seguem congelados no bloco
`__HISTORY__`, como nas rodadas anteriores.

Com os dados estáveis, o `index.html` desta rodada mantém os mesmos tamanhos da anterior —
`index.html` com **164.972 bytes** e `snapshot-data.js` com **77.186 bytes** — e as únicas
diferenças observáveis são os dois carimbos de tempo (comentário no `<head>` e banner no fim
do `<body>`).

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
  `2026-10-21T00:30:47-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 21/10/2026 00:30,
  imediatamente antes do fechamento. Ocorrência única, confirmada na cauda do arquivo.
- `__HISTORY__` exposto por accessor com merge defensivo, para que a atribuição direta feita
  pelo script do artifact não apague os meses congelados.
- O bloco de dados foi executado em Node nesta rodada: carrega sem erro, expõe os 21 projetos
  e os 11 conjuntos, serve jul–set/2026 por `__HISTORY__` e preserva esses meses mesmo após
  uma atribuição direta a `window.__HISTORY__`; as JQL de teste resolvem para os 15 registros
  de out/2026, os 33 do lookahead e os 21 projetos.
- O HTML-fonte do Live Artifact foi obtido nesta rodada pelo staging de artifacts e conferido
  contra a cópia versionada `_artifact_src.html`: **idênticos**
  (MD5 `6a2b6462a4efbec1890af4494a7f0b74`, 87.509 bytes; artifact com `updatedAt` de
  27/07/2026). O artifact não mudou desde a última conferência, de modo que a estrutura do
  `index.html` publicado continua correspondendo à do artifact de origem.

### Ressalvas de método

- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é o mesmo das rodadas anteriores — a última verificada em Chromium headless sem
  erros de script — e nesta rodada mudou apenas o bloco de dados e o carimbo de geração.
- A pasta de dados do Claude onde o artifact é armazenado não é legível pelo shell da sessão;
  o HTML-fonte é obtido pelo mecanismo de staging de artifacts. A geração parte, como nas
  rodadas anteriores, do `index.html` já versionado neste repositório, com o bloco de dados
  substituído.

## Privacidade

Os conjuntos gravados contêm apenas `key`, `summary`, `status` (nome e categoria), `project`
(chave e nome), `duedate`, `resolutiondate` e `updated`. **Não** há `accountId`, e-mail, avatar
nem qualquer identificador de pessoa — a varredura desta rodada não encontrou nenhuma dessas
chaves nos arquivos gerados (a única ocorrência da palavra `accountIds` é a própria nota de
privacidade no cabeçalho do bloco de dados). Dois status de fluxo trazem sufixo numérico no fim
do nome, herdado do Jira.

## Publicação

O commit e o push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que
roda a cada 30 minutos e detecta mudanças no working tree. Esta geração não executa git. O
deploy no Vercel acompanha o push, normalmente em cerca de um minuto.

> **Nota de publicação (21/10/2026, 00:30).** Esta rodada regravou os seis conjuntos do mês
> corrente e as duas `planned` da visão acumulada com consulta ao vivo, reconferiu a lista de
> projetos e regerou `index.html`, `snapshot-data.js` e este `README.md`. A comparação campo a
> campo contra a rodada anterior não acusou nenhuma diferença nos oito conjuntos reconsultados
> nem na lista de projetos; os dois arquivos gerados mantêm os mesmos tamanhos (164.972 e
> 77.186 bytes). O HTML-fonte do artifact permanece o de 27/07/2026, conferido por MD5 nesta
> rodada.
