# PR.03 - Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Estudos e Projetos — Relatório de Indicadores** (Engeplus Engenharia).

- **Última atualização:** 26/08/2026 00:16 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-26T00:16:29-03:00
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Publicação:** Vercel (deploy automático a cada push)

## O que é este arquivo

`index.html` é uma cópia **estática** do Live Artifact `pr03-relatorio-indicadores-epics`.
Todas as chamadas dinâmicas ao Jira foram pré-resolvidas e congeladas em `SNAP`/`DATASETS`,
que também sobrescrevem `window.cowork.callMcpTool`.
A página **não consulta o Jira ao vivo** — o banner no rodapé indica a data de congelamento.

## Períodos congelados

| Aba | Período | Origem |
|---|---|---|
| Julho 2026 | 2026-07-01 a 2026-07-31 | snapshot desta execução (mesclado em `window.__HISTORY__`) |
| Agosto 2026 | 2026-08-01 a 2026-08-31 | snapshot desta execução (servido pelo interceptador de JQL) |
| Visão Acumulada | Mar/2026 a Ago/2026 | Mar e Ago desta execução; Abr–Jul do `window.__HISTORY__` |

## Consultas resolvidas nesta geração

- 1x `getVisibleJiraProjects` (19 projetos; tipos de nível Epic: `Epic`, `Fluxo de trabalho`)
- **Julho 2026:** planned 10 · overdue 1 · lookahead 27 · sent 5 + resolved 8 = 11 consolidados · retrabalho 5
- **Agosto 2026:** planned 14 · overdue 1 · lookahead 29 · sent 3 + resolved 5 = 5 consolidados · retrabalho 3
- **Março–Junho 2026:** 1 consulta `planned` por mês, para a Visão Acumulada
- **16 padrões JQL** mapeados no interceptador.
  Teste automatizado nesta geração: **16/16 casos de roteamento OK, 16/16 datasets íntegros,
  nenhum aviso de "JQL sem correspondência"**.

## Indicadores desta geração

| Período | Epics planejados | Entregues no período¹ | OTD |
|---|---|---|---|
| Março 2026 | 7 | 3 | 43% |
| Abril 2026 | 19 | 16 | 84% |
| Maio 2026 | 15 | 4 | 27% |
| Junho 2026 | 2 | 1 | 50% |
| Julho 2026 | 10 | 8 | 80% |
| Agosto 2026 | 14 | 2 | 14% |

¹ Contagem com corte por `resolutiondate <= último dia do período` (função `dnAt` do dashboard),
e não pelo `statusCategory` atual. É por isso que a coluna pode ficar abaixo do total de epics
hoje marcados como concluídos.

O OTD de agosto é parcial: o mês ainda está em curso e a maior parte dos epics tem vencimento em 31/08.

Julho fechou em 8/10 (e não 10/10) porque `EG0274-43` e `EG0274-38`, com vencimento em julho,
só foram resolvidos em 21/08 e 24/08. Como julho é período encerrado, o corte por
`resolutiondate <= 2026-07-31` não os conta como entregues no mês.

## Divergência entre histórico congelado e o Jira atual

Os `planned` de Abr–Jun consultados agora retornam 15, 7 e 1 epics, contra 19, 15 e 2 no
`window.__HISTORY__` congelado. A diferença é de **datas de vencimento alteradas no Jira após o
fechamento** desses meses. A Visão Acumulada usa o histórico congelado (19/15/2), que é a fonte
autoritativa para períodos encerrados; os datasets recém-consultados ficam apenas como fallback
offline caso o usuário selecione uma faixa que o histórico não cubra.

## Observação sobre o indicador de retrabalho

A consulta de retrabalho (`status changed from "Enviado - Aguardando Análise"`) **não é limitada
ao período**, então qualquer saída histórica daquele status satisfaz o filtro. Somado aos status
homônimos com IDs distintos por projeto (`Enviado - Aguardando Análise1`), o conjunto de
retrabalho tende a coincidir com o de envios.

Nesta geração o retrabalho ficou em 5/5 dos envios de julho e 3/3 dos de agosto — sobre os totais
consolidados (envios + resolvidos) isso equivale a 5/11 e 3/5. **O percentual de retrabalho deve
ser lido com essa ressalva** até que a consulta seja ajustada no artifact.

Em ambos os meses o conjunto de retrabalho é subconjunto exato do conjunto de envios
(verificado nesta geração) — nenhum item precisou ser descartado.

## Outras particularidades preservadas verbatim

- `resolved<="2026-08-31"` é interpretado pelo Jira como `2026-08-31 00:00`, de modo que
  itens resolvidos no próprio dia 31 ficam fora do conjunto `resolved` do mês.
  Comportamento idêntico ao do dashboard ao vivo.
- Três grafias do status de envio nos dados desta geração: `Enviado - Aguardando Análise`,
  `Enviado - Aguardando Análise1` e `Enviado- Aguardando Análise` (sem espaço antes do hífen).
- Duas grafias do status de revisão: `Em Revisão` e o truncado `Em Revisã`.
- A chave de projeto `G0280` tem nome `EG0280 - DMAE` (inconsistência de origem no próprio Jira).
- Nomes com espaço final preservados (`EG0286 - DNIT/AC `, `Estudos Hidrológicos `).

## Privacidade

Os JSONs congelados contêm apenas `key`, `summary`, `status.name`, `statusCategory.key`,
`project.key`, `project.name`, `duedate`, `resolutiondate` e `updated`.
Não há `accountId`, e-mails, avatares, `iconUrl` nem conteúdo de descrição/comentários
(verificado por varredura automática nesta geração: 0 ocorrências de `accountId`, `avatarUrls`,
`iconUrl`, `emailAddress` e `displayName` nos dados).

## Publicação

O commit e o push são feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub` (a cada 30 minutos). O Vercel publica cerca de 1 minuto após o push.
