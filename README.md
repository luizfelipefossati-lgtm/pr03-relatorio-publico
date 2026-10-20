# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 20/10/2026 03:34** (`2026-10-20T03:34:40-03:00`)

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
| `planned_2026-10` | Epics com due date em out/2026 | 15 | 15 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 0 | 0 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 | 33 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 6 | 6 |
| `resolved_2026-10` | Concluídos em out/2026 | 6 | 6 |
| `rework_2026-10` | Retrabalho em out/2026 | 4 | 4 |

Visão acumulada (`planned` por mês): mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8 · out/2026 = **15**.

Os meses de **abr/2026 a jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026, ago/2026 e set/2026** são
congelados pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Geração em 20/10/2026 03:34 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum indicador mudou nesta rodada

Geração de 20/10 às 03:34, cerca de **uma hora** depois da das 02:34. As **seis** consultas JQL do
mês corrente foram reexecutadas ao vivo com o predicado
`issuetype in ("Epic","Fluxo de trabalho")` e a projeção de seis campos (`summary`, `status`,
`project`, `duedate`, `resolutiondate`, `updated`). Todas voltaram completas
(`pageInfo.hasNextPage = false`), sem paginação pendente e sem erro. As contagens repetem, uma a
uma, as da rodada anterior:

| Conjunto | Ao vivo | Geração das 02:34 | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | vazio, sem alteração |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |

**Método desta rodada.** As seis consultas do mês corrente foram reexecutadas ao vivo e os
arquivos de `_snap/` reescritos a partir do resultado. A igualdade com a rodada anterior foi
confirmada pelo **SHA-256 byte a byte** de cada arquivo regravado: os seis conjuntos do mês
corrente mantêm os mesmos digests e os mesmos tamanhos da tabela no fim desta seção. O
`lookahead_2026-10` foi conferido pelo digest do conjunto completo devolvido pela consulta, que
coincidiu com o do arquivo em disco.

As duas consultas `planned` que a visão acumulada ainda resolve ao vivo — mai/2026 e jun/2026,
que não estão em `window.__HISTORY__` — também foram reexecutadas, devolvendo **7** e **1**
registros. Os arquivos `planned_2026-05.json` (2.053 bytes, `eeb137b01b57`) e
`planned_2026-06.json` (371 bytes, `beb577eb21a8`) foram regravados em formato compacto nesta
rodada; o conteúdo é o mesmo já embutido no snapshot anterior.

**Correção mantida das rodadas anteriores.** Na primeira montagem do bloco estático, as expressões
regulares de `PATTERNS` saíram com barras duplicadas (`\\(` em vez de `\(`), o que faria
`resolveJql` não casar com nenhuma consulta e devolver listas vazias em toda a página. O defeito
foi detectado antes da entrega por um teste que roda as nove consultas que o artifact monta
contra os padrões realmente gravados no `index.html`; o gerador foi corrigido e o arquivo
refeito. Desde então os nove padrões resolvem para o conjunto correto, e o `index.html` mantém
os 164.972 bytes e o mesmo formato das gerações anteriores — reconfirmado nesta rodada.

**Ressalva sobre o predicado.** O prompt da tarefa agendada descreve as consultas de forma
abreviada, com `issuetype=Epic`. Esse predicado, tomado ao pé da letra, **perde** os projetos
cujo tipo de nível Epic se chama `Fluxo de trabalho` (EG0285, EG0286, EG0291, EG0294): a
consulta de `planned_2026-10` devolve 10 em vez de 15, e a de `lookahead_2026-10`, 15 em vez de
33. O que vale é o predicado que o próprio artifact monta — `issuetype in (...)` a partir dos
tipos com `hierarchyLevel === 1` da lista de projetos — e foi ele o usado nesta rodada, como nas
anteriores.

**Meses encerrados continuam congelados.** As consultas dos meses de jul/2026 a set/2026 **não**
foram reconsultadas nesta rodada, por projeto: os arquivos desses meses são o retrato do
fechamento de cada período e alimentam tanto a visão acumulada quanto os relatórios mensais
congelados. Como registrado nas rodadas anteriores, set/2026 tem **8** registros congelados
contra **5** que a mesma consulta devolve hoje, já que `duedate` de epics encerrados foi editado
depois do fechamento; sobrescrever esses conjuntos reescreveria retroativamente relatórios já
publicados. Os três meses foram transportados sem alteração do snapshot anterior, junto com o
bloco `months` (jul, ago e set de 2026) que alimenta `window.__HISTORY__`.

**Origem do HTML.** A pasta do Live Artifact
(`...\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics`) é uma área protegida e não
pode ser lida por caminho de arquivo a partir de uma sessão Cowork — recusa reconfirmada nesta
rodada (`Permission denied`, tanto no `ls` quanto no listador de diretórios). O registro do
artifact foi consultado pela via própria (`list_legacy_live_artifacts`) e traz
`updatedAt = 2026-07-27T17:28:22.980Z`, anterior a todas as gerações recentes: o artifact não
mudou. A cópia local `_artifact_src.html` segue com **87.509 bytes** e SHA-256 `2f09463c3e7c...`,
os mesmos valores registrados nas rodadas anteriores, e foi dela que saiu a estrutura do
`index.html` — o bloco estático é substituído por marcador, preservando o HTML do artifact
intacto.

A lista de projetos **foi reconsultada ao vivo** nesta rodada (`getVisibleJiraProjects`,
21 projetos, `isLast = true`). A comparação com a lista embutida no snapshot foi feita projeto a
projeto, por digest — mesmas 21 chaves, mesmos nomes, mesmos tipos de issue com o mesmo
`hierarchyLevel`, diferindo apenas na ordem em que a API devolveu, que o artifact reordena por
nome. Não houve diferença de conteúdo, e os tipos de nível Epic (`Epic`, `Fluxo de trabalho`)
usados no predicado seguem os mesmos.

Do lado do `git`, esta rodada não alterou nada: nenhum `add`, `commit`, `push`, `read-tree` ou
tentativa de autenticação. Houve apenas a inspeção somente-leitura dos quatro primeiros bytes de
`.git/index`, que trazem a assinatura `DIRC` esperada — índice íntegro, sem necessidade de
recuperação.

| Conjunto | SHA-256 (12 primeiros) | Bytes em disco |
|---|---|---:|
| `planned_2026-10` | `8bdfd9674ae8` | 4.325 |
| `overdue_2026-10` | `4f53cda18c2b` | 2 |
| `lookahead_2026-10` | `98812d39acd2` | 9.653 |
| `sent_2026-10` | `a019b8ae807d` | 1.908 |
| `resolved_2026-10` | `4d7b6dd4d6f1` | 1.953 |
| `rework_2026-10` | `7044e8e75f8e` | 1.272 |

### Correção de indicador (mantida da geração de 10/10 18:55)

Até a geração de 10/10 às 11:31, este README publicava o retrabalho de outubro contando apenas
os registros de `sent_2026-10` no denominador. O artifact usa outro denominador: ele monta a lista
de envios pela **união de `sent` e `resolved`** (`allSent`). O texto deste README foi corrigido na
geração das 18:55 para refletir o que a página de fato mostra, e a correção segue valendo nesta
rodada — agora com **57% (4 de 7)**, porque a união ganhou o `EG0274-38`, que também conta
como retrabalho.
O sétimo item da união é o `EG0239-28`, que entra por `resolved` e não por `sent` porque seu
status chama-se `Enviado - Aguardando Análise1` — uma terceira grafia, da mesma família da
ressalva já registrada para o EG0285.

### Demais conferências

- Os seis arquivos de out/2026 foram regravados a partir das respostas ao vivo e relidos em
  seguida: todos parseiam como JSON, com as contagens da tabela acima, e **sem nenhuma
  ocorrência** de `accountId`, `avatarUrls`, `iconUrl`, `emailAddress` ou de endereço de e-mail.
- Os nomes de projeto gravados nos conjuntos são lidos do `_projects_min.json`, não digitados —
  checagem introduzida depois de um nome de projeto ter sido escrito à mão de forma incorreta na
  primeira tentativa de gravação (`EG0285`).
- As **11 consultas JQL distintas** do mês corrente e da visão acumulada (6 do mês + 6 meses da
  acumulada, sendo `planned_2026-10` comum às duas) foram remontadas exatamente como o artifact
  as monta — inclusive o `issuetype in ("Epic","Fluxo de trabalho")` derivado dos tipos de nível
  Epic — e testadas, uma a uma, contra os 11 padrões gravados em `snapshot-data.js`: cada
  consulta resolveu para o seu próprio conjunto, nenhuma caiu no *fallback* de lista vazia e
  nenhum padrão ficou órfão.
- Meses congelados (≤ set/2026) **não** são reconsultados, por projeto.

### Quadro de outubro/2026 (20º dia do mês)

15 epics com due date em outubro — 12 em andamento/revisão (8 "Em andamento" + 4 "Em Revisão")
e 3 já enviados dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0240 = 3 · EG0274 = 2 · EG291 = 1.

Indicadores do mês na geração: **OTD 20%** (3 de 15), **retrabalho 57%** (4 de 7 envios),
**12 pendências do mês** e **nenhum em atraso acumulado**.

Os quatro indicadores repetem os das gerações de 16/10 às 18:32, das rodadas de 19/10 e da
rodada de 20/10 às 02:34, sem nenhuma transição nova no intervalo:

- **OTD 20%** (3 de 15). Os três entregues — `EG0286-7`, `EG291-4` e `EG0274-38` — contam
  como **"SIM\*"** (entrega no mês, mas depois da due date), de modo que o painel marca
  **0 no prazo e 3 com pequeno atraso**.
- **Retrabalho 57%** (4 de 7 envios), no denominador do painel (união de `sent` e `resolved`).
- **Atraso acumulado** segue em **0**; as **pendências do mês**, em **12**.

O mês acumula **7 envios** no critério do painel (união de `sent` e `resolved`), sendo
**4 classificados como retrabalho**:

| EPIC | Projeto | Due date | Enviado em | Retrabalho |
|---|---|---|---|---|
| `EG0275-112` | EG0275 | 2026-09-04 | 02/10 09:27 | não |
| `EG0241-42` | EG0241 | 2026-09-10 | 02/10 09:30 | sim |
| `EG0286-7` | EG0286 | 2026-10-01 | 02/10 13:40 | sim |
| `EG0240-5` | EG0240 | 2026-10-26 | 07/10 16:01 | sim — reaberto em 13/10 09:51 |
| `EG0239-28` | EG0239 | 2026-08-10 | 09/10 09:36 | não |
| `EG291-4` | EG291 | 2026-10-07 | 15/10 13:59 | não |
| `EG0274-38` | EG0274 | 2026-10-07 | 15/10 15:30 | sim |

Quatro dos sete eram entregas que vinham em atraso de meses anteriores; `EG0286-7`, `EG291-4` e
`EG0274-38` são as únicas com due date do próprio mês de outubro — e as únicas que contam no
OTD até aqui.
`EG0239-28` aparece apenas por `resolved`: seu status (`Enviado - Aguardando Análise1`) não casa
a string exata usada pelas consultas `sent`/`rework`. O `EG0240-5` continua em `sent` e em
`rework` mesmo tendo perdido a conclusão: a transição de 07/10 está no histórico e o `DURING` a
enxerga; o que mudou em 16/10 foi apenas a sua due date.

### Lookahead nov–dez/2026

33 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 22**, dos quais 20 têm due date entre 16 e 31/12.

A composição é a mesma das gerações anteriores. O EG0256 segue sem representante no lookahead
desde a saída do `EG0256-30`, reprogramado para 30/01/2027. **20 dos 33 registros (61%)** caem na
segunda quinzena de dezembro — o gargalo de fim de ano permanece, concentrado em EG0274 e EG0286.

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

- Comentário de geração no topo do `<head>`: presente, imediatamente após `<head>` (byte 609 do
  arquivo), com o carimbo `2026-10-20T03:34:40-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (o bloco injetado abre no byte 22.522 do `index.html` e `window.__SNAPSHOT__` é atribuído no
  byte 97.267, contra o byte 99.717 da atribuição `window.__HISTORY__=` do `<script>` próprio
  do artifact — ordem de execução confirmada). O bloco embutido é, além disso, **byte a byte
  igual** ao `snapshot-data.js` gravado ao lado.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 20/10/2026 03:34,
  seguido apenas de `</body></html>`. Ocorrência única no arquivo (abre no byte 164.733).
- Roteamento de JQL testado de ponta a ponta: as **nove** consultas que o artifact monta
  (as seis do mês corrente mais `planned` de mai, jun e set/2026) foram confrontadas com as
  expressões de `PATTERNS` lidas de volta do `index.html` publicado, e cada uma resolveu para o
  conjunto correto. Foi esse teste que pegou o defeito de escape descrito acima.
- Tamanhos da geração: `index.html` **164.972 bytes** (MD5 `2a8c54476695…`) e
  `snapshot-data.js` **77.186 bytes** (MD5 `00c08865f8d4…`). Os tamanhos são exatamente os da
  rodada anterior — o conteúdo embutido é idêntico e o carimbo de geração tem comprimento
  fixo —, enquanto os MD5 diferem apenas por causa do carimbo.
- Contagens dos conjuntos **embutidos** lidas de volta do `snapshot-data.js` publicado e
  conferidas uma a uma contra os arquivos de `_snap/`: `planned_2026-10` 15,
  `overdue_2026-10` 0, `lookahead_2026-10` 33, `sent_2026-10` 6, `resolved_2026-10` 6,
  `rework_2026-10` 4, e a acumulada `planned` de mai a set/2026 em 7, 1, 10, 4 e 8 — 94
  registros ao todo. Os 21 projetos, os tipos de nível Epic (`Epic`, `Fluxo de trabalho`) e os
  meses congelados (`2026-07`, `2026-08`, `2026-09`) também foram lidos de volta do arquivo
  publicado.
- Esta geração **reinjetou o bloco estático por marcador** no `index.html`, preservando o HTML
  do artifact intacto, e a estrutura foi reconferida depois, item a item, como listado acima.
  Registre-se que o relógio da VM que executa os comandos no computador está em UTC: o carimbo
  foi calculado em BRT (UTC−3) e conferido no arquivo final.
- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudou apenas o carimbo de geração.
- Nenhuma ocorrência de `avatarUrls`, `iconUrl`, `emailAddress` ou domínio de e-mail no arquivo
  publicado, e nenhuma URL da `api.atlassian.com` — a única URL da Atlassian é a base
  `https://projetos-engeplus.atlassian.net/browse/`, usada para montar os links dos EPICs. A
  única ocorrência da palavra `accountId` é o comentário do próprio gerador
  ("Nao contem accountIds"), e a única sequência com `@` fora das regras CSS `@media` é a
  versão do pacote `chart.js@4.5.0` no endereço da CDN.

---

## Publicação

O `index.html` e este `README.md` são gravados no *working tree* por esta rotina. O
`git commit`/`push` é feito separadamente pela tarefa `PR03-Auto-Push-GitHub` do Windows Task
Scheduler — que, pelo `.push-watchdog.log`, vem rodando a cada **10 minutos** — e o deploy no
Vercel segue o push.

> **Nota de publicação (19/10/2026, 23:35).** A cadeia de publicação está íntegra: a passagem
> das 23:34 concluiu com `Commit OK: 3a543454` e
> `Push OK e VERIFICADO: HEAD sincronizado com origin/main`, sem lock pendente nem índice
> quebrado. Essa passagem, porém, caiu **no meio desta geração** e levou ao ar a montagem
> intermediária, aquela com as expressões de `PATTERNS` escapadas em excesso — no ar, a página
> resolve as consultas para listas vazias. A correção já está no *working tree* (todos os
> arquivos desta rodada têm `mtime` posterior ao commit das 23:34) e entra na **próxima
> passagem do watchdog**, por volta das 23:44, com o deploy no Vercel cerca de um minuto depois.
