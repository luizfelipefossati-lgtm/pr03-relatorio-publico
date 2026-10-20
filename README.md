# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 20/10/2026 13:31** (`2026-10-20T13:31:39-03:00`)

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
| `planned_2026-05` | 7 | reaproveitado de `_snap/` (rodada das 12:31) |
| `planned_2026-06` | 1 | reaproveitado de `_snap/` (rodada das 12:31) |
| `planned_2026-07` | 10 | congelado (`__HISTORY__`) |
| `planned_2026-08` | 4 | congelado (`__HISTORY__`) |
| `planned_2026-09` | 8 | congelado (`__HISTORY__`) |
| `planned_2026-10` | 15 | consultado ao vivo (comum ao mês corrente) |

Meses encerrados de jul a set/2026 continuam servidos pelo histórico embutido em
`window.__HISTORY__`, congelado no fechamento de cada período (`_frozen_at` 01/08, 01/09 e
01/10/2026). Alterações feitas no Jira depois do fim de cada mês não afetam esses quadros.

---

## Conferência desta geração

Geração em 20/10/2026 13:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.

### Nenhum indicador mudou nesta rodada

As **seis** consultas do mês corrente e a lista de projetos foram reexecutadas ao vivo, com o
predicado `issuetype in ("Epic","Fluxo de trabalho")` e a projeção de seis campos (`summary`,
`status`, `project`, `duedate`, `resolutiondate`, `updated`). Todas voltaram completas
(`pageInfo.hasNextPage = false`), sem paginação pendente, sem atingir o teto de 100 resultados
e sem erro:

| Conjunto | Ao vivo nesta rodada | Rodada das 12:33 | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 15 | 15 | idêntico |
| `overdue_2026-10` | 0 | 0 | vazio, sem alteração |
| `lookahead_2026-10` | 33 | 33 | idêntico |
| `sent_2026-10` | 6 | 6 | idêntico |
| `resolved_2026-10` | 6 | 6 | idêntico |
| `rework_2026-10` | 4 | 4 | idêntico |
| projetos visíveis | 21 | 21 | idêntico |

As duas `planned` de mai e jun/2026 **não** foram reconsultadas nesta rodada: são meses
encerrados, e os arquivos de `_snap/` reaproveitados vêm da rodada das 12:31 de hoje. Os três
meses seguintes (jul a set) continuam servidos pelo histórico congelado. Isso está anotado na
tabela da visão acumulada acima.

Duas evidências sustentam a igualdade dos conjuntos do mês corrente, além das contagens. A lista
de projetos recém-consultada foi comparada campo a campo com a do dia anterior
(`projects_min_2026-10-19.json`): mesmas 21 chaves, mesmos nomes e mesmos tipos de nível Epic
(`Epic` e `Fluxo de trabalho`) — conteúdo idêntico. E o produto final saiu com exatamente os
mesmos tamanhos da rodada anterior — `index.html` com **164.972 bytes** e `snapshot-data.js`
com **77.186 bytes**; como os conjuntos são reserializados em forma compacta e o carimbo de
geração tem comprimento fixo, qualquer alteração de conteúdo nos onze conjuntos teria mudado
esses tamanhos. Os MD5 diferem apenas por causa do carimbo (`index.html` `16becdc75b08…`,
`snapshot-data.js` `de5c330b589b…`).

Ressalva de método: os arquivos de `_snap/` do mês corrente foram regravados nesta rodada com o
separador JSON padrão (com espaço após `:` e `,`), enquanto os da rodada anterior estavam em
forma compacta. Os tamanhos em bytes de `_snap/*.json` portanto **não** são comparáveis entre as
duas rodadas — a comparação válida é a do arquivo final, acima. O `_projects_min.json` mudou de
MD5 (`aff35de4c56a…`) pela mesma razão de serialização, com o conteúdo conferido como idêntico.

### Quadro de outubro/2026 (20º dia do mês)

15 epics com due date em outubro — 12 em andamento/revisão (8 "Em andamento" + 4 "Em Revisão")
e 3 já enviados dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0240 = 3 · EG0274 = 2 · EG291 = 1.

Como todos os conjuntos vieram idênticos, os quatro indicadores exibidos na página repetem os
das gerações de 16/10 às 18:32 e de todas as rodadas de 19/10 e 20/10: nenhuma transição nova
no intervalo.

### Lookahead nov–dez/2026

33 epics com due date nos dois meses seguintes, mesma contagem das rodadas anteriores.

### Ponto de atenção nos dados de origem (não é falha desta rotina)

Dois epics carregam no Jira o status `Enviado - Aguardando Análise**1**` — com um `1` sobrando no
fim do nome: `EG0239-28` (aparece em `resolved_2026-10`) e `EG0256-24` (em `planned_2026-06`).
A categoria de status dos dois é `done`, então eles contam normalmente como concluídos; mas a
consulta de envios casa com o nome exato `"Enviado - Aguardando Análise"` e, por isso, **não**
captura a transição desses dois. Nos meses congelados o efeito é neutralizado, porque o gerador
une `sent` e `resolved` ao montar o total de envios; no mês corrente, quem é contado como
enviado pela via da transição fica de fora. Parece um status renomeado por engano em dois fluxos
de trabalho — vale corrigir o nome no Jira, que é mais seguro do que normalizar no relatório.
O dado foi preservado verbatim no snapshot.

### Conferência estrutural

- Comentário de geração **no topo do `<head>`**: presente, imediatamente depois de `<head>`
  (posição 608), com o carimbo `2026-10-20T13:31:39-03:00`. Ocorrência única no arquivo.
- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado
  (o bloco injetado abre na posição 22.444 e `window.__SNAPSHOT__` é atribuído na posição
  96.638, contra a posição 99.088 da atribuição `window.__HISTORY__=` do `<script>` próprio do
  artifact — ordem de execução confirmada). O bloco embutido é, além disso, **byte a byte igual**
  ao `snapshot-data.js` gravado ao lado.
- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 20/10/2026 13:31,
  abrindo na posição 163.845 e seguido apenas de `</body></html>`. Ocorrência única no arquivo.
- Roteamento de JQL testado de ponta a ponta: as **doze** chamadas dinâmicas que o artifact monta
  (as seis do mês corrente, as seis `planned` da visão acumulada mai–out/2026, sendo
  `planned_2026-10` comum às duas, e `getVisibleJiraProjects`) foram remontadas exatamente como
  o artifact as monta e executadas contra o `snapshot-data.js` gerado, carregado em Node. As onze
  consultas JQL resolveram para o conjunto correto, com os campos aninhados legíveis
  (`fields.status.name` presente em todas), e a de projetos devolveu os 21 registros; nenhuma
  caiu no aviso `JQL sem correspondência no snapshot` e nenhum padrão ficou órfão — ou seja, a
  página publicada não tem como consultar o Jira ao vivo.
- O acessor de `window.__HISTORY__` foi verificado depois do carregamento, inclusive com uma
  atribuição direta simulada (`window.__HISTORY__ = {'2026-04': …, '2026-09': …}`): devolveu
  `2026-04` **mais** os três meses congelados (`2026-07`, `2026-08`, `2026-09`), a chave
  `2026-09` da atribuição foi rejeitada em favor da do snapshot, e `period`, `planned`, `sent` e
  `rework` vieram íntegros — a atribuição do script do artifact é mesclada, não sobrescreve.
- Os conjuntos de dados em `_snap/` foram regravados na forma aninhada que o artifact consome,
  relidos em seguida e validados elemento a elemento: todos parseiam como JSON, todos os
  registros têm exatamente as chaves `key` e `fields`, e cada `fields` tem exatamente `summary`,
  `status`, `project`, `duedate`, `resolutiondate` e `updated`. Contagens conforme a tabela
  acima.
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
registrada às 13:24 de hoje, push verificado contra `origin/main`) — e o deploy no Vercel segue o
push.

> **Nota de publicação (20/10/2026, 13:31).** Esta rodada regravou os seis conjuntos do mês
> corrente em `_snap/` com o retorno ao vivo do Jira, reaproveitou as duas `planned` de mai e
> jun/2026 já em disco, e gravou no *working tree* o `index.html`, o `snapshot-data.js` e este
> `README.md`. Os dados vieram idênticos aos da rodada das 12:33: o `index.html` novo é byte a
> byte igual ao anterior fora os dois carimbos de geração. A lista de projetos foi reconsultada
> e conferida como idêntica. Nenhuma operação de `git` foi executada pela rotina; a próxima
> passagem da tarefa `PR03-Auto-Push-GitHub` leva tudo ao ar em até 10 minutos, com o deploy no
> Vercel cerca de um minuto depois.
