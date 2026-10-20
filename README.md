# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 20/10/2026 15:32** (`2026-10-20T15:32:46-03:00`)

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
| `planned_2026-05` | 7 | reaproveitado de `_snap/` (rodada das 15:31) |
| `planned_2026-06` | 1 | reaproveitado de `_snap/` (rodada das 15:31) |
| `planned_2026-07` | 10 | congelado (mês encerrado, servido por `__HISTORY__`) |
| `planned_2026-08` | 4 | congelado (mês encerrado, servido por `__HISTORY__`) |
| `planned_2026-09` | 8 | congelado (mês encerrado, servido por `__HISTORY__`) |
| `planned_2026-10` | 15 | ao vivo nesta rodada |

Mais a chamada `getVisibleJiraProjects`, resolvida com os 21 projetos visíveis.

## Como foi gerado

Geração em 20/10/2026 15:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum indicador mudou nesta rodada

Os seis conjuntos do mês corrente foram reconsultados do zero e voltaram idênticos aos da
rodada anterior (17:3x UTC / 14:34 BRT):

| Conjunto | Ao vivo nesta rodada | Rodada anterior | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | idêntico |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |

A lista de projetos visíveis também foi reconsultada e conferida por hash contra a da rodada
anterior: **sem diferença** (mesmos 21 projetos, mesmos nomes, mesmos tipos de issue).

As duas `planned` de mai e jun/2026 **não** foram reconsultadas nesta rodada: são meses
encerrados, e os arquivos de `_snap/` reaproveitados vêm da rodada das 15:31 de hoje. Os três
meses de jul a set/2026 seguem congelados no bloco `__HISTORY__`, como nas rodadas anteriores.

Com os dados iguais, o `index.html` desta rodada difere do anterior **apenas nos dois carimbos
de tempo** (comentário no `<head>` e banner no fim do `<body>`), e mantém os mesmos tamanhos —
`index.html` com **164.972 bytes** e `snapshot-data.js` com **77.186 bytes**.

### Epics com due date em out/2026 (15)

Distribuição por projeto: EG0286 (DNIT/AC) 4, G0280 (DMAE) 5, EG0240 (GOITÁ/COMPESA) 3,
EG0274 (DNIT) 2, EG291 (Arroio Feijó) 1.

Seis epics entraram em "Enviado - Aguardando Análise" ao longo de out/2026 e seis foram
concluídos no mês; quatro deles voltaram de "Enviado - Aguardando Análise" para revisão, o que
os caracteriza como retrabalho. Nenhum epic está vencido sem conclusão.

O olhar para frente registra 33 epics com due date em nov e dez/2026, mesma contagem das
rodadas anteriores.

## Estrutura e verificações

- Comentário `<!-- Snapshot gerado em ... -->` no início do `<head>` (posição 608), com o
  carimbo `2026-10-20T15:32:46-03:00`. Ocorrência única no arquivo.
- Bloco `<script>` com `window.__SNAPSHOT__` e a sobrescrita de `window.cowork.callMcpTool`,
  que devolve os dados pré-buscados conforme o padrão da JQL recebida. Ocorrência única.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 20/10/2026 15:32,
  imediatamente antes do fechamento. Ocorrência única.
- `__HISTORY__` exposto por accessor com merge defensivo, para que a atribuição direta feita
  pelo script do artifact não apague os meses congelados.

### Ressalvas de método

- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudou apenas o carimbo de geração.
- O HTML-fonte do Live Artifact não é acessível a partir de uma sessão Cowork (fica em área
  protegida de dados do Claude). A geração parte, como nas rodadas anteriores, do `index.html`
  já versionado neste repositório, com o bloco de dados substituído.

## Privacidade

Os conjuntos gravados contêm apenas `key`, `summary`, `status` (nome e categoria), `project`
(chave e nome), `duedate`, `resolutiondate` e `updated`. **Não** há `accountId`, e-mail, avatar
nem qualquer identificador de pessoa. Dois status de fluxo trazem sufixo numérico no fim do
nome, herdado do Jira.

## Publicação

O commit e o push são feitos pela tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, que
roda a cada 30 minutos e detecta mudanças no working tree. Esta geração não executa git. O
deploy no Vercel acompanha o push, normalmente em cerca de um minuto.

> **Nota de publicação (20/10/2026, 15:32).** Esta rodada regravou os seis conjuntos do mês
> corrente com consulta ao vivo, reconferiu a lista de projetos e regerou `index.html`,
> `snapshot-data.js` e este `README.md`. Os dados vieram idênticos aos da rodada anterior: o
> `index.html` novo é byte a byte o mesmo, exceto pelos dois carimbos de tempo.
