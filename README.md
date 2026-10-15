# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 15/10/2026 15:31** (`2026-10-15T15:31:23-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **21**

### Consultas resolvidas (24 conjuntos + lista de projetos)

Meses encerrados — servidos pelo histórico embutido (`window.__HISTORY__`):

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-07` | Epics com due date em jul/2026 | 10 |
| `overdue_2026-07` | Vencidos antes de jul/2026, não concluídos | 0 |
| `lookahead_2026-07` | Due date entre ago/2026 e set/2026 | 26 |
| `sent_2026-07` | Transições para "Enviado - Aguardando Análise" em jul/2026 | 5 |
| `resolved_2026-07` | Concluídos em jul/2026 | 8 |
| `rework_2026-07` | Retrabalho em jul/2026 | 5 |
| `planned_2026-08` | Epics com due date em ago/2026 | 4 |
| `overdue_2026-08` | Vencidos antes de ago/2026, não concluídos | 0 |
| `lookahead_2026-08` | Due date entre set/2026 e out/2026 | 39 |
| `sent_2026-08` | Transições para "Enviado - Aguardando Análise" em ago/2026 | 4 |
| `resolved_2026-08` | Concluídos em ago/2026 | 6 |
| `rework_2026-08` | Retrabalho em ago/2026 | 3 |
| `planned_2026-09` | Epics com due date em set/2026 | 8 |
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 1 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 38 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 8 |
| `resolved_2026-09` | Concluídos em set/2026 | 4 |
| `rework_2026-09` | Retrabalho em set/2026 | 3 |

Mês corrente (out/2026) — servido pela interceptação de JQL (`window.cowork.callMcpTool`):

| Conjunto | Escopo | Registros | Geração anterior |
|---|---|---:|---:|
| `planned_2026-10` | Epics com due date em out/2026 | **15** | 13 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | **0** | 1 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 | 33 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | **5** | 4 |
| `resolved_2026-10` | Concluídos em out/2026 | **5** | 4 |
| `rework_2026-10` | Retrabalho em out/2026 | 3 | 3 |

Visão acumulada (`planned` por mês): mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8 · out/2026 = **15**.

Os meses de **abr/2026 a jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026, ago/2026 e set/2026** são
congelados pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Geração em 15/10/2026 15:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Cinco dos seis conjuntos mudaram nesta rodada

Quinta geração de 15/10, cerca de **duas horas** após a das 13:31 — e a primeira do dia com
movimento real no Jira. As **seis** consultas JQL do mês corrente foram reexecutadas ao vivo com
o predicado `issuetype in (Epic, "Fluxo de trabalho")`:

| Conjunto | Ao vivo | Geração anterior | Situação |
|---|---:|---:|---|
| `planned_2026-10` | **15** | 13 | **+2 chaves**, 1 reprogramação, 1 mudança de status |
| `overdue_2026-10` | **0** | 1 | **−1 chave** (ficou vazio) |
| `lookahead_2026-10` | 33 | 33 | mesmas chaves, mesma ordem |
| `sent_2026-10` | **5** | 4 | **+1 chave**, 1 registro com campos alterados |
| `resolved_2026-10` | **5** | 4 | **+1 chave** |
| `rework_2026-10` | 3 | 3 | mesmas chaves; 1 registro com campos alterados |
| projetos visíveis | 21 | 21 | **reconsultada ao vivo**, sem alteração |

A comparação foi feita **item a item**, e não por contagem: os seis conjuntos foram remontados do
zero a partir das respostas ao vivo, no formato mínimo, e comparados aos arquivos em `_snap/` por
igualdade estrutural completa — chave, `summary`, `status.name`, `status.statusCategory.key`,
`project.key`, `project.name`, `duedate`, `resolutiondate`, `updated` e a ordem dos registros.
As diferenças apuradas, uma a uma:

| EPIC | O que mudou | Antes | Agora |
|---|---|---|---|
| `EG0240-43` | **novo** em `planned` | — | TOMO IV - PROJETO DE INSTRUMENTAÇÃO, `Em Revisão`, due 23/10 |
| `EG0240-4` | due date reprogramada | 16/10 | **23/10** (atualizado 15/10 13:58) |
| `EG0240-5` | due date reprogramada — sai de `overdue`, entra em `planned` | 30/09 | **26/10** (atualizado 15/10 13:58) |
| `EG291-4` | **entregue** — entra em `sent` e `resolved` | `Em andamento` | **`Enviado - Aguardando Análise`**, resolvido 15/10 13:59 |

As três alterações do EG0240 e a entrega do EG291-4 foram registradas no Jira entre **13:58 e
14:50 de hoje**, ou seja, depois da geração das 13:31 — o que explica por que aquela rodada ainda
encontrou tudo idêntico. Os seis conjuntos de `_snap/` foram **regravados** com os dados ao vivo;
os meses congelados não foram tocados.

As seis respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts nem
reexecuções; duas delas (`lookahead_2026-10`, com 33 registros, e a lista de projetos)
estouraram o limite de tokens da resposta e foram extraídas do arquivo salvo pelo próprio MCP,
conforme a disciplina do passo 3. Estado dos arquivos depois da gravação:

| Conjunto | SHA-256 (12 primeiros) | Bytes |
|---|---|---:|
| `planned_2026-10` | `7bd37aa49eba` | 5.626 |
| `overdue_2026-10` | `4f53cda18c2b` | 2 |
| `lookahead_2026-10` | `a7915446592b` | 12.591 |
| `sent_2026-10` | `bfb6746a723d` | 2.047 |
| `resolved_2026-10` | `3c8279fe3d9c` | 2.092 |
| `rework_2026-10` | `39eacb6e104d` | 1.233 |

O `lookahead_2026-10` manteve o hash e os 12.591 bytes das gerações anteriores — é o único dos
seis que saiu idêntico.

A lista de projetos **foi** reconsultada ao vivo nesta rodada: o `getVisibleJiraProjects`
devolveu os mesmos **21 projetos** (`isLast = true`, `total = 21`) e os mesmos dois tipos de
nível Epic (`Epic` e `Fluxo de trabalho`). A resposta foi reduzida ao formato mínimo e
comparada ao `_projects_min.json` em disco por igualdade estrutural normalizada — chave, nome
e lista de tipos de cada projeto. Idênticos; o arquivo, por isso, **não** foi regravado, e os
nomes de projeto gravados nos conjuntos continuam batendo, um a um, com os desse arquivo.

> **Pendência remanescente (menor).** O texto `issuetype=Epic` continua gravado no prompt da
> tarefa agendada, no passo que descreve as seis consultas. Ele não afeta a página publicada —
> o artifact monta o predicado dinamicamente a partir dos tipos de hierarquia 1 dos projetos
> visíveis —, mas faz cada rodada partir de uma consulta truncada e precisar corrigi-la à mão.
> Trocar aquele trecho do prompt por `issuetype in (Epic, "Fluxo de trabalho")` elimina o
> retrabalho — e é uma alteração no prompt da tarefa, que esta rotina não faz por conta própria.

> **Pendência (operacional), confirmada de novo.** O passo 1 do prompt manda abrir o
> `ARTIFACT_HTML` por caminho (`...\Claude\Artifacts\pr03-relatorio-indicadores-epics\index.html`)
> e **parar** com "Artifact PR03 não encontrado" se a leitura falhar. Nesta rodada tanto o
> `device_bash` quanto o `device_list_dir` recusaram o caminho com *"inside a protected location
> (system, credential or Claude-internal data)"* — uma rodada que siga o passo ao pé da letra
> aborta sem gerar nada. A origem usada foi o `_artifact_src.html` versionado no repositório,
> que é o que o `_gen_snapshot.py` já consome. Convém trocar aquele passo por
> `list_legacy_live_artifacts` + `device_stage_files(artifact_ids=[...])`, com o
> `_artifact_src.html` como alternativa declarada — alteração no prompt da tarefa, que esta
> rotina não faz por conta própria. A equivalência foi **verificada** nesta rodada: o
> `list_legacy_live_artifacts` + `device_stage_files(artifact_ids=[...])` trouxe o artifact ao
> vivo (87.509 bytes, `updatedAt` 27/07/2026) e o `md5` bate com o do `_artifact_src.html` em
> disco (`6a2b6462a4efbec1890af4494a7f0b74`) — a origem em cache é byte a byte o artifact atual,
> sem defasagem.

> **Nota de publicação (15/10/2026, 15:31).** A cadeia de publicação está íntegra: o
> `.push-watchdog.log` registra a passagem das 15:24, com `Commit OK: 8202e3e` e `Push OK e
> VERIFICADO: HEAD sincronizado com origin/main`. As passagens correm a cada ~10 minutos e as
> quatro mais recentes (14:54, 15:04, 15:14 e 15:24) concluíram todas com sucesso. Esta
> geração entra na passagem seguinte, prevista para ~15:34.

A **visão acumulada** (`planned_2026-05` a `planned_2026-10`) não foi reconsultada ao vivo nesta
rodada: outubro já é coberto pelo `planned_2026-10` acima, e maio a setembro são meses encerrados,
servidos tal como estão em `_snap/`. Julho, agosto e setembro são, além disso, **congelados** no
fechamento do período — divergem de propósito de uma consulta ao vivo, pelas reprogramações
posteriores ao fechamento (`EG0274-38` e `EG0274-43` saíram de julho para outubro; `EG0286-7`
saiu de agosto para outubro; `EG0240-4` saiu de setembro para 23/10). Pela regra de congelamento,
esses arquivos **não** são regravados: o histórico de OTD de cada mês continua refletindo o
que estava previsto no fechamento daquele mês.

Outubro passa a **não ter nenhum EPIC em atraso acumulado**: o `EG0240-5`, que ocupava sozinho
esse conjunto desde 13/10, teve a due date movida de 30/09 para 26/10 e migrou para os previstos
do próprio mês. Os dois EPICs do EG0256 reprogramados para 2027 (`EG0256-28` em 29/01 e
`EG0256-30` em 30/01) seguem fora de qualquer conjunto de outubro.

### Correção de indicador (mantida da geração de 10/10 18:55)

Até a geração de 10/10 às 11:31, este README publicava o retrabalho de outubro contando apenas
os registros de `sent_2026-10` no denominador. O artifact usa outro denominador: ele monta a lista
de envios pela **união de `sent` e `resolved`** (`allSent`). O texto deste README foi corrigido na
geração das 18:55 para refletir o que a página de fato mostra, e a correção segue valendo nesta
rodada — agora com **50% (3 de 6)**, porque a união ganhou o `EG291-4`.
O sexto item da união é o `EG0239-28`, que entra por `resolved` e não por `sent` porque seu
status chama-se `Enviado - Aguardando Análise1` — uma terceira grafia, da mesma família da
ressalva já registrada para o EG0285.

### Demais conferências

- Os seis arquivos de out/2026 foram revalidados depois de gravados: todos parseiam como JSON,
  todos os registros têm exatamente as chaves `key` e `fields`, e `fields` exatamente os seis
  campos da projeção (`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`).
  Nenhuma ocorrência de `accountId`, `avatarUrls`, `emailAddress` ou de endereço de e-mail em
  qualquer deles.
- Os nomes de projeto gravados nos conjuntos são lidos do `_projects_min.json`, não digitados —
  checagem introduzida depois de um nome de projeto ter sido escrito à mão de forma incorreta na
  primeira tentativa de gravação (`EG0285`). O `EG0291 - Arroio Feijó`, projeto do EPIC entregue
  hoje, foi conferido contra esse arquivo.
- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026. A pasta `Artifacts` é uma
  **localização protegida** (dados internos do Claude) e não pode ser lida por caminho de arquivo
  a partir de uma sessão Cowork; por isso o HTML ao vivo foi obtido **nesta rodada** por *staging*
  de artifact (`device_stage_files` com `artifact_ids`) e conferido contra a cópia local: mesmos
  87.509 bytes e **MD5 idêntico** (`6a2b6462a4efbec1890af4494a7f0b74`).
- As **12 consultas JQL** do mês corrente e da visão acumulada foram remontadas exatamente como
  o artifact as monta e testadas, uma a uma, contra os 11 padrões gravados em
  `snapshot-data.js`: cada consulta resolveu para o seu próprio conjunto, nenhuma caiu no
  *fallback* de lista vazia e nenhum padrão ficou órfão.
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.

### Quadro de outubro/2026 (15º dia do mês)

15 epics com due date em outubro — 13 em andamento/revisão (8 "Em andamento" + 5 "Em Revisão")
e 2 já enviados dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0240 = 3 · EG0274 = 2 · EG291 = 1.

Indicadores do mês na geração: **OTD 13%** (2 de 15), **retrabalho 50%** (3 de 6 envios),
**13 pendências do mês** e **nenhum em atraso acumulado**.

Os três indicadores **mudaram** em relação às sete gerações anteriores, que vinham repetindo
OTD 8% (1 de 13) e retrabalho 60% (3 de 5):

- **OTD 8% → 13%.** O numerador subiu de 1 para 2 com a entrega do `EG291-4` (due 07/10,
  enviado hoje às 13:59) e o denominador, de 13 para 15, com a entrada de `EG0240-43` (novo) e
  `EG0240-5` (reprogramado para 26/10). Os dois entregues contam como **"SIM\*"** — entrega no
  mês, mas depois da due date —, de modo que o painel marca **0 no prazo e 2 com pequeno atraso**.
- **Retrabalho 60% → 50%.** O numerador segue em 3; o denominador passou de 5 para 6 com a
  entrada do `EG291-4` na união `sent` + `resolved`.
- **Atraso acumulado 1 → 0.** Pela reprogramação do `EG0240-5`, descrita acima.
- **Pendências do mês 12 → 13**: 15 previstos menos 2 entregues.

O mês acumula **6 envios** no critério do painel (união de `sent` e `resolved`), sendo
**3 classificados como retrabalho**:

| EPIC | Projeto | Due date | Enviado em | Retrabalho |
|---|---|---|---|---|
| `EG0275-112` | EG0275 | 2026-09-04 | 02/10 09:27 | não |
| `EG0241-42` | EG0241 | 2026-09-10 | 02/10 09:30 | sim |
| `EG0286-7` | EG0286 | 2026-10-01 | 02/10 13:40 | sim |
| `EG0240-5` | EG0240 | 2026-10-26 | 07/10 16:01 | sim — reaberto em 13/10 09:51 |
| `EG0239-28` | EG0239 | 2026-08-10 | 09/10 09:36 | não |
| `EG291-4` | EG291 | 2026-10-07 | 15/10 13:59 | não |

Quatro dos seis eram entregas que vinham em atraso de meses anteriores; `EG0286-7` e `EG291-4`
são as únicas com due date do próprio mês de outubro — e as únicas que contam no OTD até aqui.
`EG0239-28` aparece apenas por `resolved`: seu status (`Enviado - Aguardando Análise1`) não casa
a string exata usada pelas consultas `sent`/`rework`. O `EG0240-5` continua em `sent` e em
`rework` mesmo tendo perdido a conclusão: a transição de 07/10 está no histórico e o `DURING` a
enxerga; o que mudou hoje foi apenas a sua due date.

### Lookahead nov–dez/2026

33 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 22**, dos quais 20 têm due date entre 16 e 31/12.

A composição é a mesma das gerações anteriores — este foi o único conjunto do mês corrente que
saiu idêntico nesta rodada. O EG0256 segue sem representante no lookahead desde a saída do
`EG0256-30`, reprogramado para 30/01/2027. **20 dos 33 registros (61%)** caem na segunda quinzena
de dezembro — o gargalo de fim de ano permanece, concentrado em EG0274 e EG0286.

### Setembro/2026, congelado

Indicadores gravados em definitivo: **8 previstos**, **1 em atraso acumulado**, **8 envios**,
**3 de retrabalho**, **4 resoluções**, OTD **63% (5 de 8)**.

Como registrado nas gerações anteriores, o fechamento carrega duas ressalvas conhecidas,
preservadas aqui sem correção porque espelham o comportamento do artifact ao vivo:

- **Corte das 00h em `resolved`.** Três EPICs resolvidos ao longo do dia 30/09 — `G0280-52`
  (11:23), `EG0285-19` (15:15) e `EG0240-4` (17:27) — ficaram fora de `resolved_2026-09`, porque
  a consulta usa `resolved<="2026-09-30"`, que o Jira lê como meia-noite do dia 30. A cláusula
  `DURING` de `sent` não sofre o mesmo corte e cobre o dia inteiro.
- **Grafia de status no EG0285.** O status do fluxo chama-se `Enviado- Aguardando Análise`
  (id `11737`, sem espaço antes do hífen), enquanto `sent`/`rework` casam a string exata
  `Enviado - Aguardando Análise`. Por isso `EG0285-19` conta como entregue no OTD mas não aparece
  entre os envios de setembro.

Corrigir qualquer das duas exige ação fora deste processo: renomear o status `11737` para a
grafia canônica no Jira e/ou ajustar o limite superior da consulta `resolved` para `23:59` no
artifact.

### Conferência estrutural

Checagens desta rodada (contagens e carimbos reconferidos após a geração):

- Comentário de geração no topo do `<head>`: presente, logo após `<head>`, com o carimbo
  `2026-10-15T15:31:23-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (bloco injetado abre no byte 22.533 do `index.html` e `window.__SNAPSHOT__` é atribuído no
  byte 95.688, contra o byte 98.129 da atribuição `window.__HISTORY__=` do `<script>` próprio
  do artifact — ordem de execução confirmada).
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 15:31,
  seguido apenas de `</body></html>`. Ocorrência única no arquivo.
- As **12 consultas JQL** do mês corrente e da visão acumulada (6 do mês + 6 meses da
  acumulada, sendo `planned_2026-10` comum às duas) foram reconstruídas exatamente como o
  artifact as monta — inclusive o `issuetype in ("Epic","Fluxo de trabalho")` montado a partir
  dos tipos de nível Epic — e testadas contra os padrões gravados em `snapshot-data.js`: as 12
  resolvem para o conjunto correto, sem *fallback* para lista vazia, e nenhum padrão ficou
  órfão (11 padrões para 11 conjuntos embutidos).
- Contagens dos conjuntos do mês corrente conferidas contra os arquivos de `_snap/`:
  `planned` 15, `overdue` 0, `lookahead` 33, `sent` 5, `resolved` 5, `rework` 3.
- Tamanhos da geração: `index.html` **164.016 bytes** e `snapshot-data.js` **76.230 bytes**,
  contra 163.034 e 75.248 da rodada anterior — o crescimento corresponde aos dois registros
  novos de `planned` e ao registro novo de `sent`/`resolved`.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudaram apenas o carimbo de geração e os dados embutidos.
- Nenhuma ocorrência de `avatarUrls`, `iconUrl`, `emailAddress` ou domínio de e-mail no arquivo
  publicado, e nenhuma URL da `api.atlassian.com` — a única URL da Atlassian é a base
  `https://projetos-engeplus.atlassian.net/browse/`, usada para montar os links dos EPICs. A
  única ocorrência da palavra `accountId` é o comentário do próprio gerador
  ("Nao contem accountIds"), e a única sequência com `@` é a versão do pacote
  `chart.js@4.5.0` no endereço da CDN.

---

## Publicação

O `index.html` e este `README.md` são gravados no *working tree* por esta rotina. O
`git commit`/`push` é feito separadamente pela tarefa `PR03-Auto-Push-GitHub` do Windows Task
Scheduler — que, pelo `.push-watchdog.log`, vem rodando a cada **10 minutos** — e o deploy no
Vercel segue o push.
