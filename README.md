# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 30/09/2026 15:13** (`2026-09-30T15:13:00-03:00`)

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

Verificação ao vivo no Jira em 30/09/2026 15:13 (BRT):

- HTML do artifact ao vivo: md5 `6a2b6462a4efbec1890af4494a7f0b74`, 87.509 bytes — idêntico a
  `_artifact_src.html`, confirmando que o fonte usado na geração está atualizado.
- Sonda de alterações `ETQ AND updated >= "2026-09-30 14:28"` → **6 issues**. Houve delta desde a
  geração anterior; os 6 conjuntos de set/2026 foram integralmente reconsultados ao vivo.
- Projetos: nenhuma chave nova apareceu nos conjuntos consultados; `_projects_min.json` inalterado.

### Delta desta rodada

Entre 14:55 e 15:00 de 30/09, **seis EPICs tiveram o due date empurrado de setembro para outubro**:
`G0280-50` (EBE Ponta da Cadeia), `G0280-51` (EBE Baronesa do Gravataí), `G0280-53` (EBE Gaspar
Martins), `G0280-54` (EBE Asa Branca), `G0280-55` (EBE Nova Brasília) e `EG0286-10` (Estudos
geológicos). Eles saíram de `planned_2026-09` e entraram em `lookahead_2026-09`.

| Conjunto | Registros | Situação |
|---|---:|---|
| `planned_2026-09` | 8 | era 14; −6 (repactuação de prazo para out/2026). |
| `overdue_2026-09` | 1 | sem alteração (`EG0239-28`). |
| `lookahead_2026-09` | 38 | era 32; +6 (os mesmos EPICs, agora com due date em out/2026). |
| `sent_2026-09` | 7 | sem alteração; chaves conferidas. |
| `resolved_2026-09` | 4 | sem alteração (`EG0240-43`, `EG0275-6`, `EG0286-8`, `EG0286-30`). |
| `rework_2026-09` | 3 | sem alteração (`EG0240-5`, `EG0240-43`, `EG0286-7`). |

Efeito nos indicadores de **Setembro/2026**: a base de previstos caiu de 14 para 8 sem mudança no
numerador de entregas, então o OTD do mês **subiu de 21% (3 de 14) para 38% (3 de 8)** e as
pendências do mês caíram de 11 para 5. Em atraso acumulado segue 1 EPIC e o retrabalho segue em
43% (3/7). Na visão acumulada, o OTD passou de 53% (34 de 64) para **59% (34 de 58)**, com 24
pendentes. A melhora é efeito de repactuação de prazo, **não** de entrega adicional.

> `G0280-52` (EBE Barros Cassal) foi resolvido às 11:23 de 30/09 e aparece em `sent_2026-09`, mas
> **não** em `resolved_2026-09`: a consulta do artifact usa `resolved<="2026-09-30"`, que o Jira
> interpreta como meia-noite do dia 30. É o comportamento do artifact ao vivo, preservado aqui.

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

Renderização conferida em navegador headless (Chromium): sem erros de página nem de console,
5 gráficos montados, única dependência externa `cdn.jsdelivr.net` (Chart.js), banner como último
elemento do `<body>`, e as três abas abrem normalmente —
**Agosto 2026** OTD 50% (2 de 4), **Setembro 2026** OTD 38% (3 de 8), 5 pendentes do mês, 1 em
atraso acumulado e 43% de retrabalho (3/7), **Visão Acumulada** OTD 59% (34 de 58), 24 pendentes,
heatmap OTD por projeto × mês montado.

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
