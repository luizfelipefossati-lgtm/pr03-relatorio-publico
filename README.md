# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 05:11 (2026-08-27T05:11:29-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue considerados como Epic:** Epic, Fluxo de trabalho
- **Projetos visiveis no snapshot:** 19

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

O script injetado entra **depois** do bloco `window.__HISTORY__` proprio do artifact
(que congela 2026-04 a 2026-06) e **antes** do script principal, de modo que os dois
conjuntos historicos coexistem em vez de um sobrescrever o outro.

As 17 chamadas dinamicas do artifact (1x `getVisibleJiraProjects` + 16 consultas JQL)
foram resolvidas e validadas uma a uma: cada JQL foi roteada para o dataset correto,
sem colisao de padroes e sem dataset orfao.

## Conteudo do snapshot

| Conjunto | Registros |
|---|---|
| `planned_2026-08` | 13 |
| `overdue_2026-08` | 1 |
| `lookahead_2026-08` | 30 |
| `sent_2026-08` | 3 |
| `resolved_2026-08` | 5 |
| `rework_2026-08` | 3 |
| `planned_2026-07` | 10 |
| `overdue_2026-07` | 1 |
| `lookahead_2026-07` | 27 |
| `sent_2026-07` | 5 |
| `resolved_2026-07` | 8 |
| `rework_2026-07` | 5 |
| `planned_2026-03` | 7 |
| `planned_2026-04` | 15 |
| `planned_2026-05` | 7 |
| `planned_2026-06` | 1 |

Mes encerrado de **Julho/2026** congelado em `window.__HISTORY__` para exibir os dados
reais do periodo em vez do aviso de "sem snapshot" (11 enviados, 5 com retrabalho —
`sent` e a uniao de `sent_2026-07` com `resolved_2026-07`, sem duplicatas).

Visao acumulada padrao: **Marco a Agosto/2026** (ultimos 6 meses). Marco e Agosto sao
resolvidos via JQL embutida; Abril a Julho vem congelados de `window.__HISTORY__`.

## Observacao sobre status

O site usa variantes de nome quase identicas que caem na categoria `done`:
`Enviado - Aguardando Analise`, `Enviado - Aguardando Analise1` e `Enviado- Aguardando Analise`.
A clausula JQL `status changed to "Enviado - Aguardando Analise"` so casa com o nome exato,
por isso `resolved_*` pode ser maior que `sent_*`. O relatorio une os dois conjuntos.

Ressalva conhecida sobre `rework_*`: a clausula `status changed from "Enviado - Aguardando
Analise"` nao tem janela temporal e casa com qualquer saida daquele status, inclusive a
transicao normal rumo ao encerramento (ex.: "Medido e Faturado"). O indicador de retrabalho
tende portanto a ser superestimado — nesta geracao os conjuntos `sent` e `rework`
coincidiram integralmente nos dois meses (Agosto 3 e 3, Julho 5 e 5). Para medir devolucao
real, a consulta precisaria restringir o destino da transicao (ex.: `... to "Em Revisao"`)
e/ou limitar a janela.

Ressalva sobre o congelamento de Julho: o mes encerrado e reconsultado a cada geracao do
snapshot, portanto reflete o estado **atual** das issues com vencimento em Julho, e nao uma
foto tirada em 31/07. Alteracoes retroativas no Jira ainda afetam os numeros de Julho.

## Privacidade

Os dados embutidos contem apenas: chave da issue, resumo, status, projeto, data de
entrega, data de resolucao e data de atualizacao. **Nao ha** accountIds, e-mails,
avatares, URLs internas da API nem descricoes.

## Publicacao

O commit e o push para o GitHub sao feitos automaticamente pela tarefa do Windows
Task Scheduler `PR03-Auto-Push-GitHub` (a cada 30 minutos). O deploy no Vercel ocorre
cerca de 1 minuto apos o push.
