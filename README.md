# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 19/10/2026 20:31** (`2026-10-19T20:31:32-03:00`)

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

Geração em 19/10/2026 20:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum indicador mudou nesta rodada

Quarta geração de 19/10, cerca de **uma hora** depois da das 13:30. As **seis** consultas JQL do
mês corrente foram reexecutadas ao vivo com o predicado
`issuetype in ("Epic","Fluxo de trabalho")` e a projeção de seis campos (`summary`, `status`,
`project`, `duedate`, `resolutiondate`, `updated`). Todas voltaram completas
(`pageInfo.hasNextPage = false`), sem paginação pendente e sem erro. As contagens repetem, uma a
uma, as da rodada anterior:

| Conjunto | Ao vivo | Geração das 13:30 | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | vazio, sem alteração |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |

**Método desta rodada.** Ao contrário das três anteriores, esta rodada **regravou** os seis
arquivos de `_snap/` do mês corrente a partir das respostas ao vivo, em vez de compará-los e
preservá-los. A regravação usa o formato canônico do pipeline (`json.dumps(..., indent=1)`,
sem escapar acentos), o mesmo de `_run1013i.py`; parte dos arquivos estava em JSON compacto,
herdado de um conversor antigo, e por isso os **tamanhos em disco cresceram sem que os dados
mudassem** — a contagem de registros é a mesma em todos os seis conjuntos, e o `index.html` e o
`snapshot-data.js` saíram com **exatamente os mesmos tamanhos em bytes** da geração anterior
(164.972 e 77.186), o único elemento variável entre as duas sendo o carimbo de geração, de
comprimento fixo. O `lookahead_2026-10`, cuja resposta estourou o limite de tokens da ferramenta,
foi reduzido aos seis campos no arquivo salvo pela própria ferramenta e transferido ao
repositório já minimizado.

**Meses encerrados continuam congelados.** As consultas dos meses ≤ set/2026 **não** foram
reconsultadas nesta rodada, por projeto: os arquivos de `_snap/` desses meses são o retrato do
fechamento de cada período e alimentam tanto a visão acumulada quanto os relatórios mensais
congelados. Como registrado nas rodadas anteriores, set/2026 tem **8** registros congelados
contra **5** que a mesma consulta devolve hoje, já que `duedate` de epics encerrados foi editado
depois do fechamento; sobrescrever esses arquivos reescreveria retroativamente relatórios já
publicados.

**Origem do HTML.** A pasta do Live Artifact
(`...\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics`) é uma área protegida e não
pode ser lida por caminho de arquivo a partir de uma sessão Cowork — recusa reconfirmada nesta
rodada, tanto em `device_list_dir` quanto em `ls`. O HTML ao vivo foi obtido pela via própria de
artifacts (`device_stage_files` com `artifact_ids`), **refeito nesta rodada**, e conferido contra
a cópia local: mesmos **87.509 bytes** e MD5 idêntico (`6a2b6462a4efbec1890af4494a7f0b74`). A
data de modificação do artifact ao vivo continua em **27/07/2026** — o artifact não mudou desde a
última geração.

A lista de projetos **foi reconsultada ao vivo** nesta rodada (`getVisibleJiraProjects`,
21 projetos, `isLast = true`). A comparação com o `_projects_min.json` em disco foi feita projeto
a projeto — mesmas 21 chaves, mesmos nomes, mesmos tipos de issue com o mesmo `hierarchyLevel` —
e **não houve diferença**, de modo que o arquivo não foi alterado e os tipos de nível Epic
(`Epic`, `Fluxo de trabalho`) usados no predicado seguem os mesmos. A cópia temporária usada na
comparação foi movida para `_to_delete/`, que o `.gitignore` já exclui.

Do lado do `git`, esta rodada não executou **nenhum** comando. A única inspeção de estado foi a
leitura dos quatro primeiros bytes de `.git/index`, que trazem a assinatura `DIRC` esperada — o
índice não está corrompido e não foi preciso recuperá-lo. Nenhum `add`, `commit` ou `push`, e
nenhuma tentativa de autenticação.

| Conjunto | SHA-256 (12 primeiros) | Bytes em disco |
|---|---|---:|
| `planned_2026-10` | `b6abc214d6c0` | 4.654 |
| `overdue_2026-10` | `4f53cda18c2b` | 2 |
| `lookahead_2026-10` | `a7915446592b` | 10.378 |
| `sent_2026-10` | `3b5f6e5baf7e` | 2.039 |
| `resolved_2026-10` | `cc1816951c1c` | 2.084 |
| `rework_2026-10` | `ef078b89c74b` | 1.359 |

Os hashes acima são o SHA-256 dos **bytes dos arquivos em disco** e **mudaram** em relação às
rodadas anteriores apenas por causa da reformatação descrita acima; não são comparáveis com os
das tabelas de rodadas passadas, nem entre recipientes diferentes.

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

### Quadro de outubro/2026 (19º dia do mês)

15 epics com due date em outubro — 12 em andamento/revisão (8 "Em andamento" + 4 "Em Revisão")
e 3 já enviados dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0240 = 3 · EG0274 = 2 · EG291 = 1.

Indicadores do mês na geração: **OTD 20%** (3 de 15), **retrabalho 57%** (4 de 7 envios),
**12 pendências do mês** e **nenhum em atraso acumulado**.

Os quatro indicadores repetem os das gerações de 16/10 às 18:32 e de 19/10, sem nenhuma
transição nova no intervalo:

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

- Comentário de geração no topo do `<head>`: presente, imediatamente após `<head>` (byte 608 do
  arquivo), com o carimbo `2026-10-19T20:31:32-03:00`.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (o bloco injetado abre no byte 22.453 do `index.html` e `window.__SNAPSHOT__` é atribuído no
  byte 96.638, contra o byte 99.088 da atribuição `window.__HISTORY__=` do `<script>` próprio
  do artifact — ordem de execução confirmada). O bloco embutido é, além disso, **byte a byte
  igual** ao `snapshot-data.js` gravado ao lado.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 19/10/2026 20:31,
  seguido apenas de `</body></html>`. Ocorrência única no arquivo (abre no byte 163.738).
- Tamanhos da geração: `index.html` **164.972 bytes** (MD5 `d7acf6b8f26c…`) e
  `snapshot-data.js` **77.186 bytes** (MD5 `86ef64004a23…`). Os tamanhos são exatamente os da
  rodada anterior — o conteúdo embutido é idêntico e o carimbo de geração tem comprimento
  fixo —, enquanto os MD5 diferem apenas por causa do carimbo.
- Contagens dos conjuntos **embutidos** lidas de volta do `snapshot-data.js` publicado e
  conferidas uma a uma contra os arquivos de `_snap/`: `planned_2026-10` 15,
  `overdue_2026-10` 0, `lookahead_2026-10` 33, `sent_2026-10` 6, `resolved_2026-10` 6,
  `rework_2026-10` 4, e a acumulada `planned` de mai a set/2026 em 7, 1, 10, 4 e 8. Os 21
  projetos, os tipos de nível Epic (`Epic`, `Fluxo de trabalho`) e os meses congelados
  (`2026-07`, `2026-08`, `2026-09`) também foram lidos de volta do arquivo publicado.
- Esta geração **remontou o `index.html` do zero** a partir do `_artifact_src.html` com o
  `_gen_snapshot.py`, e a estrutura foi reconferida depois, item a item, como listado acima.
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

> **Nota de publicação (19/10/2026, 20:31).** A cadeia de publicação está íntegra: as seis
> passagens mais recentes do watchdog — 13:44, 13:54, 14:04, 14:14, 14:24 e 14:34 — concluíram
> todas com sucesso, em cadência regular de 10 minutos, a última com
> `Commit OK: 7ed22768` e `Push OK e VERIFICADO: HEAD sincronizado com origin/main`. Em nenhuma
> delas houve lock pendente ou índice quebrado. A passagem das 14:34 já levou o `index.html`
> desta geração; este `README.md`, gravado logo em seguida, entra na passagem das ~14:44.
