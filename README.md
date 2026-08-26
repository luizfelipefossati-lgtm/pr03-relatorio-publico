# PR.03 - Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Estudos e Projetos — Relatório de Indicadores** (Engeplus Engenharia).

- **Última atualização:** 25/08/2026 22:50 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-25T22:50:50-03:00
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Publicação:** Vercel (deploy automático a cada push)

## O que é este arquivo

`index.html` é uma cópia **estática** do Live Artifact `pr03-relatorio-indicadores-epics`.
Todas as chamadas dinâmicas ao Jira foram pré-resolvidas e congeladas em `window.__SNAPSHOT__`,
que também sobrescreve `window.cowork.callMcpTool`.
A página **não consulta o Jira ao vivo** — o banner no rodapé indica a data de congelamento.

## Períodos congelados

| Aba | Período | Origem |
|---|---|---|
| Julho 2026 | 2026-07-01 a 2026-07-31 | snapshot desta execução |
| Agosto 2026 | 2026-08-01 a 2026-08-31 | snapshot desta execução |
| Visão Acumulada | Mar/2026 a Ago/2026 | Mar, Jul e Ago desta execução; Abr–Jun do histórico embutido no artifact |

## Consultas resolvidas nesta geração

- 1x `getVisibleJiraProjects` (19 projetos; tipos de nível Epic: `Fluxo de trabalho`, `Epic`)
- **Julho 2026:** planned 10 · overdue 1 · lookahead 27 · sent 5 + resolved 8 = 11 consolidados · retrabalho 5
- **Agosto 2026:** planned 14 · overdue 1 · lookahead 29 · sent 3 + resolved 5 = 5 consolidados · retrabalho 3
- **Março 2026:** planned 7 — visão acumulada
- **13 padrões JQL** mapeados no interceptador do snapshot, todos validados contra as consultas
  que o artifact emite (teste automatizado nesta geração: 13/13 OK)

## Indicadores desta geração

| Período | Epics planejados | Concluídos (statusCategory=done) | OTD bruto |
|---|---|---|---|
| Julho 2026 | 10 | 10 | 100% |
| Agosto 2026 | 14 | 2 | 14% |

O OTD de agosto é parcial: o mês ainda está em curso e a maior parte dos epics tem vencimento em 31/08.

## Observação sobre o indicador de retrabalho

A consulta de retrabalho (`status changed from "Enviado - Aguardando Análise"`) **não é limitada
ao período**, então qualquer saída histórica daquele status satisfaz o filtro. Somado aos status
homônimos com IDs distintos por projeto (`Enviado- Aguardando Análise` sem espaço,
`Enviado - Aguardando Análise1`), o conjunto de retrabalho tende a coincidir com o de envios.

Nesta geração o retrabalho ficou em 5/5 dos envios de julho e 3/3 dos de agosto — sobre os totais
consolidados (envios + resolvidos) isso equivale a 5/11 e 3/5. **O percentual de retrabalho deve
ser lido com essa ressalva** até que a consulta seja ajustada no artifact.

**Correção aplicada nesta execução:** a consulta de retrabalho de julho retornou `EG0239-27`, que
não consta do conjunto de envios do mesmo período. Como retrabalho é, por definição, subconjunto de
envios, o item foi descartado. A contagem oficial do Jira (`searchResultMode: count`) confirma 5
para ambas as consultas de julho.

## Outras particularidades preservadas verbatim

- `resolved<="2026-07-31"` é interpretado pelo Jira como `2026-07-31 00:00`, de modo que
  itens resolvidos no próprio dia 31 ficam fora do conjunto `resolved` do mês.
  Comportamento idêntico ao do dashboard ao vivo.
- Duas grafias do status de revisão: `Em Revisão` e o truncado `Em Revisã`.
- A chave de projeto `G0280` tem nome `EG0280 - DMAE` (inconsistência de origem no próprio Jira).

## Privacidade

Os JSONs congelados contêm apenas `key`, `summary`, `status.name`, `statusCategory.key`,
`project.key`, `project.name`, `duedate`, `resolutiondate` e `updated`.
Não há `accountId`, e-mails, avatares, `iconUrl` nem conteúdo de descrição/comentários
(verificado por varredura automática nesta geração).

## Publicação

O commit e o push são feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub` (a cada 30 minutos). O Vercel publica cerca de 1 minuto após o push.
