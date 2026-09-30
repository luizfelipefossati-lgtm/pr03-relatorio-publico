# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 30/09/2026 20:30** (`2026-09-30T20:30:20-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **21**

### Consultas resolvidas (18 conjuntos + lista de projetos)

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

Mês corrente — servido pela interceptação de JQL (`window.cowork.callMcpTool`):

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-09` | Epics com due date em set/2026 | 8 |
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 1 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 38 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 8 |
| `resolved_2026-09` | Concluídos em set/2026 | 4 |
| `rework_2026-09` | Retrabalho em set/2026 | 3 |

Visão acumulada (`planned` por mês): abr/2026 = 15 · mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8.

Os meses de **abr/2026, mai/2026 e jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026 e ago/2026** são congelados
pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Verificação ao vivo no Jira em 30/09/2026 20:28–20:30 (BRT):

- Fonte do HTML: o artifact `pr03-relatorio-indicadores-epics` foi obtido por staging pelo id e
  confere **byte a byte** com o `_artifact_src.html` local — 87.509 bytes, md5
  `6a2b6462a4efbec1890af4494a7f0b74` nos dois. (O artifact não é alterado desde 27/07/2026.)
  A pasta `Artifacts` **não** está montada nesta sessão — `connectedFolders` traz apenas
  `pr03-relatorio-publico`, e o pedido de acesso à pasta foi recusado pelo ambiente —, mas o
  staging por id dispensou a montagem.
- Os **seis conjuntos de set/2026** foram reconsultados individualmente ao vivo (não por sonda):
  `planned`, `overdue`, `sent`, `resolved`, `rework` e `lookahead`. Todos **idênticos** ao
  gravado em `_snap/` (o `lookahead`, de 38 linhas, conferido campo a campo por digest).
- `getVisibleJiraProjects` reconsultado: **21 projetos**, idênticos a `_projects_min.json`
  (digest por projeto conferido, incluindo `issueTypes` e `hierarchyLevel`).

### Delta desta rodada

**Sem delta.** Nenhuma alteração no Jira entre a geração das 19:30 e esta das 20:30 BRT. Esta
geração reescreve `index.html` e `snapshot-data.js` somente para atualizar o carimbo de data.

Indicadores de **Setembro/2026** mantidos: OTD **63% (5 de 8)**, **3** pendências do mês,
**1** EPIC em atraso acumulado, retrabalho **38% (3/8)**. Visão acumulada: OTD **62% (36 de 58)**,
22 pendentes.

### ⚠ Ressalva de fechamento — o corte das 00h em `resolved`

Hoje é **o último dia de set/2026**, e três EPICs foram resolvidos ao longo do dia 30:
`G0280-52` (11:23), `EG0285-19` (15:15) e `EG0240-4` (17:27). Nenhum deles entra em
`resolved_2026-09`, porque a consulta do artifact usa `resolved<="2026-09-30"`, que o Jira
interpreta como **meia-noite** do dia 30. Reexecutando a mesma consulta com
`resolved<="2026-09-30 23:59"` o resultado passa de **4 para 7** registros — reconfirmado ao vivo
nesta rodada.

A cláusula `DURING ("2026-09-01","2026-09-30")` de `sent` **não** sofre o mesmo corte: ela cobre o
dia 30 inteiro, e por isso `EG0240-4` foi contabilizado como envio. O painel de OTD também não
sofre, porque deriva de `planned` + categoria de status.

Persiste, além disso, a divergência de **grafia de status** no projeto EG0285: o status do fluxo
chama-se `Enviado- Aguardando Análise` (id `11737`, **sem espaço antes do hífen**), enquanto as
consultas `sent` e `rework` casam a string exata `Enviado - Aguardando Análise`. Por isso
`EG0285-19` conta como entregue no OTD mas não aparece em `sent_2026-09`.

Consequência do fechamento: quando set/2026 for congelado (primeira geração após 01/10), o mês
ficará gravado com **8 envios e 4 resoluções**, sem `EG0285-19` entre os envios e sem os três
EPICs do dia 30 entre as resoluções. O mesmo mecanismo já afeta silenciosamente os últimos dias
de meses anteriores.

Esse é o comportamento do artifact ao vivo, preservado aqui sem correção: o snapshot espelha o
que a página publicada mostraria. Corrigir exige ação fora deste processo — renomear o status
`11737` para a grafia canônica no Jira, e/ou ajustar o limite superior da consulta `resolved` no
artifact para `23:59`.

Conferência dos meses da visão acumulada (`planned` de abr/2026 a set/2026),
comparando o valor ao vivo com o gravado em `_snap/`:

| Mês | Ao vivo | Gravado | |
|---|---:|---:|---|
| abr/2026 | 15 | 15 | igual |
| mai/2026 | 7 | 7 | igual |
| jun/2026 | 1 | 1 | igual |
| jul/2026 | 9 | 10 | divergência esperada (mês congelado) |
| ago/2026 | 3 | 4 | divergência esperada (mês congelado) |
| set/2026 | 8 | 8 | igual |

As divergências de jul e ago são o comportamento pretendido, não um erro: os meses encerrados
são **congelados no fechamento do período** e, por projeto, não voltam a ser consultados. Uma
alteração de due date (ou a remoção de um epic) feita no Jira depois do fechamento muda a
contagem ao vivo, mas não pode alterar um indicador já publicado para aquele mês. Os meses em
aberto na acumulada (abr–jun, que ainda não têm os 6 conjuntos completos) continuam batendo com
o Jira.

Conferência estrutural do `index.html` gerado: comentário de geração no topo do `<head>`, bloco
`window.__SNAPSHOT__` injetado antes do script principal do artifact, banner de snapshot como
**último elemento do `<body>`** com o carimbo 30/09/2026 20:30, e nenhuma ocorrência de
`accountId`, `avatarUrls`, `iconUrl` ou e-mail no arquivo publicado.

> Nota de virada de mês: 30/09 é o último dia do mês corrente. Na próxima geração após a virada
> (01/10) o gerador passa a congelar 2026-09 — os 6 conjuntos de setembro já estão completos em
> `_snap/` — e 2026-10 vira o mês ao vivo, com os 6 conjuntos de outubro a serem criados naquela
> rodada.

## Abas disponíveis

- **Agosto 2026** — período encerrado, dados congelados no fechamento do período.
- **Setembro 2026** — mês corrente; os dados são os do instante da geração do snapshot.
- **Visão Acumulada** — abr/2026 a set/2026 (padrão: últimos 6 meses).

## Estrutura

| Arquivo | Função |
|---|---|
| `index.html` | Página publicada, auto-contida (HTML + dados + lógica). |
| `snapshot-data.js` | Cópia avulsa do bloco de dados embutido, para inspeção. |
| `_gen_snapshot.py`, `_snap/`, `_projects_min.json` | Insumos e gerador de execuções anteriores. |
| `auto-push.ps1`, `install-task.ps1` e afins | Automação local de commit/push no Windows. |

A única dependência externa da página é o Chart.js via CDN (`cdn.jsdelivr.net`), usado para os gráficos.

## Publicação

O commit e o push são feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub`, que verifica o working tree a cada 30 minutos.
O deploy no Vercel ocorre cerca de 1 minuto após o push.

## Privacidade

Os conjuntos de dados embutidos contêm apenas: chave do epic, resumo, status (nome e categoria),
projeto (chave e nome), due date, data de resolução e data de atualização.
**Não** incluem `accountId`, e-mails, avatares, descrições em ADF nem `iconUrl`.

## Observação sobre os status de envio

As consultas `sent` e `rework` casam exatamente a string `Enviado - Aguardando Análise`.
O Jira da organização possui variantes distintas desse status em alguns projetos
(`Enviado- Aguardando Análise`, `Enviado - Aguardando Análise1`), que **não** são contabilizadas
nessas consultas. Esse comportamento é o mesmo do artifact ao vivo e foi preservado no snapshot.
