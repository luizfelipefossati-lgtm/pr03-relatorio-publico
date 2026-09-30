# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 30/09/2026 15:30** (`2026-09-30T15:30:40-03:00`)

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
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 7 |
| `resolved_2026-09` | Concluídos em set/2026 | 4 |
| `rework_2026-09` | Retrabalho em set/2026 | 3 |

Visão acumulada (`planned` por mês): abr/2026 = 15 · mai/2026 = 7 · jun/2026 = 1 · jul/2026 = 10 · ago/2026 = 4 · set/2026 = 8.

Os meses de **abr/2026, mai/2026 e jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração. **Jul/2026 e ago/2026** são congelados
pelo snapshot e mesclados a esse histórico.

## Conferência desta geração

Verificação ao vivo no Jira em 30/09/2026 15:30 (BRT):

- Fonte do HTML: `_artifact_src.html` (87.509 bytes). A pasta `Artifacts` **não** está montada
  nesta sessão (`connectedFolders` traz apenas `pr03-relatorio-publico`), então o fonte local foi
  usado diretamente; ele é idêntico ao artifact conferido na rodada anterior.
- Sonda de alterações `ETQ AND updated >= "2026-09-30 15:05"` → **1 issue**. Houve delta desde a
  geração anterior; os 6 conjuntos de set/2026 foram reconsultados ao vivo.
- Projetos: nenhuma chave nova nos conjuntos consultados; `_projects_min.json` inalterado.

### Delta desta rodada

Às **15:15 de 30/09**, `EG0285-19` (SERVIÇOS TOPOGRÁFICOS, EG0285 - EMBASA - BARREIRAS, due date
18/09) saiu de "Em Revisão" para **"Enviado- Aguardando Análise"** (categoria `done`,
`resolutiondate` 30/09 15:15).

| Conjunto | Registros | Situação |
|---|---:|---|
| `planned_2026-09` | 8 | mesmas chaves; `EG0285-19` passou a `done`. |
| `overdue_2026-09` | 1 | sem alteração (`EG0239-28`). |
| `lookahead_2026-09` | 38 | sem alteração (md5 idêntico ao vivo). |
| `sent_2026-09` | 7 | sem alteração — ver ressalva abaixo. |
| `resolved_2026-09` | 4 | sem alteração — ver ressalva abaixo. |
| `rework_2026-09` | 3 | sem alteração (`EG0240-5`, `EG0240-43`, `EG0286-7`). |

Efeito nos indicadores de **Setembro/2026**: o OTD subiu de 38% (3 de 8) para **50% (4 de 8)** e as
pendências do mês caíram de 5 para 4. Em atraso acumulado segue 1 EPIC; o retrabalho segue em
43% (3/7). Desta vez a melhora é **entrega real**, não repactuação de prazo.

### ⚠ Ressalva de fechamento — `EG0285-19` não entra em `sent_2026-09`

`EG0285-19` é contabilizado como **entregue** no painel de OTD (que deriva de `planned` +
categoria de status), mas **não** aparece em `sent_2026-09` nem em `resolved_2026-09`. São duas
causas independentes, ambas confirmadas ao vivo nesta rodada:

1. **Nome de status divergente.** O status do fluxo do projeto EG0285 chama-se
   `Enviado- Aguardando Análise` (id `11737`, **sem espaço antes do hífen**). As consultas `sent` e
   `rework` do artifact casam a string exata `Enviado - Aguardando Análise`, então nenhuma
   transição de EPIC do EG0285 é registrada como envio ou retrabalho.
2. **Limite de data às 00h.** A consulta `resolved` do artifact usa `resolved<="2026-09-30"`, que o
   Jira interpreta como **meia-noite** do dia 30. Reexecutando a mesma consulta com
   `resolved<="2026-09-30 23:59"` o resultado passa de **4 para 6** registros, incluindo
   `G0280-52` (resolvido 30/09 11:23) e `EG0285-19` (30/09 15:15).

Consequência: **30/09 é o último dia do mês**. Na primeira geração após a virada, set/2026 será
congelado e o total de envios do mês ficará gravado como **7 em vez de 8**, com `EG0285-19`
permanentemente ausente do fechamento — e o denominador do retrabalho fixado em 7. O mesmo
mecanismo já afeta silenciosamente qualquer EPIC resolvido no último dia de meses anteriores.

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

Renderização conferida em navegador headless (Chromium): **0 erros de página e 0 erros/avisos de
console**, 5 gráficos montados, única dependência externa `cdn.jsdelivr.net` (Chart.js), banner
como último elemento do `<body>` com o carimbo 30/09/2026 15:30, e as três abas abrem
normalmente — **Agosto 2026** OTD 50% (2 de 4), **Setembro 2026** OTD 50% (4 de 8), 4 pendentes do
mês, 1 em atraso acumulado e 43% de retrabalho (3/7), **Visão Acumulada** com heatmap de OTD por
projeto × mês montado.

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
