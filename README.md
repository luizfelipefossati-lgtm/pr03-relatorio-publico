# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 20/10/2026 09:31** (`2026-10-20T09:31:51-03:00`)

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

Visão acumulada (últimos 6 meses) — uma consulta `planned` por mês:

| Conjunto | Registros | Origem nesta rodada |
|---|---:|---|
| `planned_2026-05` | 7 | consultado ao vivo |
| `planned_2026-06` | 1 | consultado ao vivo |
| `planned_2026-07` | 10 | congelado (`__HISTORY__`) |
| `planned_2026-08` | 4 | congelado (`__HISTORY__`) |
| `planned_2026-09` | 8 | congelado (`__HISTORY__`) |
| `planned_2026-10` | 15 | consultado ao vivo (comum ao mês corrente) |

Meses encerrados de jul a set/2026 continuam servidos pelo histórico embutido em
`window.__HISTORY__`, congelado no fechamento de cada período (`_frozen_at` 01/08, 01/09 e
01/10/2026). Alterações feitas no Jira depois do fim de cada mês não afetam esses quadros.

---

## Conferência desta geração

Geração em 20/10/2026 09:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum indicador mudou nesta rodada

As **seis** consultas do mês corrente, as duas `planned` de mai e jun/2026 e a lista de projetos
foram reexecutadas ao vivo, com o predicado `issuetype in ("Epic","Fluxo de trabalho")` e a
projeção de seis campos (`summary`, `status`, `project`, `duedate`, `resolutiondate`,
`updated`). Todas voltaram completas (`pageInfo.hasNextPage = false`), sem paginação pendente e
sem erro:

| Conjunto | Ao vivo nesta rodada | Rodada das 08:31 | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | vazio, sem alteração |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |
| `planned_2026-05` | 7 | 7 | idêntico |
| `planned_2026-06` | 1 | 1 | idêntico |
| projetos visíveis | 21 | 21 | idêntico |

A igualdade não foi inferida do total: cada conjunto recém-consultado foi **comparado registro a
registro** com o conjunto da rodada anterior (comparação de estruturas JSON já normalizadas,
campo a campo, inclusive `status`, `duedate`, `resolutiondate` e `updated`), e os onze conjuntos
voltaram idênticos. A lista de projetos foi comparada da mesma forma, após a mesma ordenação por
nome que o artifact aplica. O produto final confirma: `index.html` saiu com exatamente
**164.972 bytes** e `snapshot-data.js` com exatamente **77.186 bytes** — os mesmos números da
rodada das 08:31. Como o carimbo de geração tem comprimento fixo, mudou apenas o carimbo; os MD5
diferem por isso (`index.html` `06debc88b4f7…`, `snapshot-data.js` `42a7c99ec2ab…`).

### Quadro de outubro/2026 (20º dia do mês)

15 epics com due date em outubro — 12 em andamento/revisão (8 "Em andamento" + 4 "Em Revisão")
e 3 já enviados dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0240 = 3 · EG0274 = 2 · EG291 = 1.

Como todos os conjuntos vieram idênticos, os quatro indicadores exibidos na página repetem os
das gerações de 16/10 às 18:32 e de todas as rodadas de 19/10 e 20/10: nenhuma transição nova
no intervalo.

### Lookahead nov–dez/2026

33 epics com due date nos dois meses seguintes, mesma contagem das rodadas anteriores.

### Conferência estrutural

- Comentário de geração **no topo do `<head>`**: presente, imediatamente depois de `<head>`
  (posição 608), com o carimbo `2026-10-20T09:31:51-03:00`. Ocorrência única no arquivo.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (o bloco injetado abre na posição 22.444 e `window.__SNAPSHOT__` é atribuído na posição
  96.638, contra a posição 99.088 da atribuição `window.__HISTORY__=` do `<script>` próprio do
  artifact — ordem de execução confirmada). O bloco embutido é, além disso, **byte a byte igual**
  ao `snapshot-data.js` gravado ao lado.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 20/10/2026 09:31,
  abrindo na posição 163.738 e seguido apenas de `</body></html>`. Ocorrência única no arquivo.
- Roteamento de JQL testado de ponta a ponta: as **doze** chamadas dinâmicas que o artifact monta
  (as seis do mês corrente, as seis `planned` da visão acumulada mai–out/2026, sendo
  `planned_2026-10` comum às duas, e `getVisibleJiraProjects`) foram remontadas exatamente como
  o artifact as monta e executadas contra o `snapshot-data.js` gerado, carregado em Node. As onze
  consultas JQL resolveram para o conjunto correto, com os campos aninhados legíveis
  (`fields.status.name` presente em todas), e a de projetos devolveu os 21 registros; nenhuma
  caiu no aviso `JQL sem correspondência no snapshot` e nenhum padrão ficou órfão — ou seja, a
  página publicada não tem como consultar o Jira ao vivo.
- O acessor de `window.__HISTORY__` foi verificado depois do carregamento: devolve os três meses
  congelados (`2026-07`, `2026-08`, `2026-09`), confirmando que a atribuição direta feita pelo
  script do artifact é mesclada, e não sobrescreve o histórico do snapshot.
- Os oito arquivos de dados foram regravados em `_snap/` na forma aninhada que o artifact
  consome e relidos em seguida: todos parseiam como JSON, com as contagens da tabela acima.
- Nenhuma ocorrência de `avatarUrls`, `iconUrl`, `emailAddress` ou domínio de e-mail no arquivo
  publicado, e nenhuma URL da `api.atlassian.com` — a única URL da Atlassian é a base
  `https://projetos-engeplus.atlassian.net/browse/`, usada para montar os links dos EPICs. A
  única ocorrência da palavra `accountId` é o comentário do próprio gerador
  ("Nao contem accountIds").
- `.git/index` inspecionado somente-leitura: assinatura `DIRC`, íntegro. Nenhuma operação de
  `git` foi executada por esta rotina.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudou apenas o carimbo de geração.
- O Live Artifact de origem (`…\Artifacts\pr03-relatorio-indicadores-epics\index.html`) não é
  legível a partir de uma sessão Cowork: o caminho fica em área protegida (dados internos do
  Claude). A geração parte, como nas rodadas anteriores, do `index.html` já versionado neste
  repositório, no qual só o bloco de dados e os dois carimbos são substituídos — o HTML do
  artifact em si permanece o mesmo byte a byte.
- Registre-se que o relógio da VM que executa os comandos no computador está em UTC: o carimbo
  foi calculado em BRT (UTC−3) e conferido no arquivo final.

---

## Publicação

O `index.html` e este `README.md` são gravados no *working tree* por esta rotina. O
`git commit`/`push` é feito separadamente pela tarefa `PR03-Auto-Push-GitHub` do Windows Task
Scheduler — que, pelo `.push-watchdog.log`, vem rodando a cada **10 minutos** (última passagem
registrada às 09:24 de hoje, commit `fe762f9`, push verificado) — e o deploy no Vercel segue o
push.

> **Nota de publicação (20/10/2026, 09:31).** Esta rodada gravou no *working tree* os seis
> conjuntos de out/2026 e os dois de mai e jun/2026 em `_snap/`, a lista de projetos
> `projects_min_2026-10-20.json`, o `index.html`, o `snapshot-data.js` e este `README.md`.
> Nenhuma operação de `git` foi executada pela rotina; a próxima passagem da tarefa
> `PR03-Auto-Push-GitHub` leva tudo ao ar em até 10 minutos, com o deploy no Vercel cerca de um
> minuto depois.
