# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 08:14 (2026-08-27T08:14:05-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como Epic:** Epic, Fluxo de trabalho
- **Projetos visiveis no snapshot:** 19
- **Tamanho de `index.html`:** 147.7 KB

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

O script injetado entra **depois** do bloco `window.__HISTORY__` proprio do artifact
(que congela 2026-04 a 2026-06) e **antes** do script principal, de modo que os dois
conjuntos historicos coexistem em vez de um sobrescrever o outro. Na pagina carregada,
`window.__HISTORY__` fica com as chaves `2026-04`, `2026-05`, `2026-06` (nativas) e
`2026-07` (do snapshot).

O HTML base usado na geracao e o `_artifact_src.html` deste repositorio (948 linhas,
md5 `6a2b6462a4efbec1890af4494a7f0b74`), verificado contra o artifact atual
(`Artifacts\pr03-relatorio-indicadores-epics\index.html`) por contagem de linhas e
comparacao de ancoras. Se o artifact for editado, `_artifact_src.html` precisa ser
atualizado junto. Os pontos de injecao sao validados por assercao no gerador: `<head>`
na linha 17, `window.__HISTORY__=` na 281, `</script>` na 282 e `<script>` na 283 —
se o artifact mudar de forma a deslocar essas linhas, a geracao falha em vez de
produzir um HTML corrompido.

## Verificacao desta geracao

As 18 chamadas dinamicas do artifact (1x `getVisibleJiraProjects` + 17 consultas JQL)
foram simuladas em Node contra o `index.html` gerado, reproduzindo a montagem de JQL do
artifact para a data de referencia 27/08/2026:

- **8** resolvidas via padrao JQL -> dataset embutido, todas para o dataset correto;
- **10** servidas diretamente por `window.__HISTORY__`, sem gerar JQL;
- **1** `getVisibleJiraProjects`, devolvendo os 19 projetos;
- **0** consultas sem correspondencia (nenhum aviso `JQL sem correspondencia`).

Tambem verificado: comentario de timestamp no topo do `<head>`, banner de aviso
imediatamente antes de `</body>`, um unico override de `callMcpTool`, `<body>`/`<html>`
bem formados, bloco do snapshot posicionado entre o `__HISTORY__` nativo e o script
principal, e ausencia de `accountId` / `emailAddress` / `avatarUrls` nos dados embutidos.

## Conteudo do snapshot

`ativo` = acionado por alguma consulta JQL nesta geracao.
`fallback` = presente no arquivo mas nao acionado, porque o mes correspondente e servido
por `window.__HISTORY__`. Os fallbacks sao mantidos de proposito: se a data de referencia
virar o mes e o artifact passar a consultar esses periodos por JQL, os dados ja estao la.

| Conjunto | Registros | Uso |
|---|---:|---|
| `planned_2026-08` | 13 | ativo |
| `overdue_2026-08` | 1 | ativo |
| `lookahead_2026-08` | 30 | ativo |
| `sent_2026-08` | 3 | ativo |
| `resolved_2026-08` | 5 | ativo |
| `rework_2026-08` | 3 | ativo |
| `planned_2026-07` | 10 | fallback |
| `overdue_2026-07` | 1 | fallback |
| `lookahead_2026-07` | 27 | fallback |
| `sent_2026-07` | 5 | fallback |
| `resolved_2026-07` | 8 | fallback |
| `rework_2026-07` | 5 | fallback |
| `planned_2026-03` | 7 | ativo |
| `planned_2026-04` | 15 | fallback |
| `planned_2026-05` | 7 | fallback |
| `planned_2026-06` | 1 | fallback |

Mes encerrado de **Julho/2026** congelado em `window.__SNAPSHOT__.months` (que alimenta
`window.__HISTORY__`) para exibir os dados reais do periodo em vez do aviso de "sem
snapshot": 11 enviados e 5 com retrabalho (5 de `sent_2026-07` unidos a
8 de `resolved_2026-07`, sem duplicatas).

Visao acumulada padrao: **Marco a Agosto/2026** (ultimos 6 meses). Marco e Agosto sao
resolvidos via JQL embutida; Abril a Julho vem congelados de `window.__HISTORY__`.

## Observacao sobre status

O site usa variantes de nome quase identicas que caem na categoria `done`:
`Enviado - Aguardando Analise`, `Enviado - Aguardando Analise1` e `Enviado- Aguardando Analise`.
A clausula JQL `status changed to "Enviado - Aguardando Analise"` so casa com o nome exato,
por isso `resolved_*` pode ser maior que `sent_*`. O relatorio une os dois conjuntos.

Ha tambem um nome de status truncado no Jira, `Em Revisa` (EG0275-6), preservado como esta.

## Ressalvas conhecidas

**`rework_*` superestima o retrabalho.** A clausula `status changed from "Enviado -
Aguardando Analise"` nao tem janela temporal e casa com qualquer saida daquele status,
inclusive a transicao normal rumo ao encerramento (ex.: "Medido e Faturado"). Nesta
geracao os conjuntos `sent` e `rework` coincidiram integralmente nos dois meses
(Agosto 3 e 3, Julho 5 e 5). Para medir devolucao real, a consulta precisaria
restringir o destino da transicao (ex.: `... to "Em Revisao"`) e/ou limitar a janela.

**Limite superior de `resolved_*`.** O Jira interpreta `resolved<="AAAA-MM-DD"` como
meia-noite daquele dia, entao itens resolvidos ao longo do ultimo dia do mes ficam de fora
do conjunto `resolved_*` (ex.: EG0274-44, resolvido em 31/07/2026 09:31, nao aparece em
`resolved_2026-07`; ele entra no total de julho apenas porque tambem consta em
`sent_2026-07`). Corrigir exigiria alterar o artifact para
`resolved<"primeiro-dia-do-mes-seguinte"`.

**Congelamento de Julho nao e uma foto de 31/07.** O mes encerrado e reconsultado a cada
geracao do snapshot, portanto reflete o estado **atual** das issues com vencimento em
Julho. Alteracoes retroativas no Jira ainda afetam os numeros de Julho.

**Abril a Junho vem do artifact, nao desta geracao.** Esses tres meses sao servidos pelo
bloco `window.__HISTORY__` embutido no proprio artifact e nao sao atualizados aqui.

## Privacidade

Os dados embutidos contem apenas: chave da issue, resumo, status, projeto, data de
entrega, data de resolucao e data de atualizacao. **Nao ha** accountIds, e-mails,
avatares, URLs internas da API nem descricoes. Nomes de pessoas podem aparecer apenas se
estiverem escritos no resumo de alguma issue — publicacao aprovada pelo usuario.

## Publicacao

O commit e o push para o GitHub sao feitos automaticamente pela tarefa do Windows
Task Scheduler `PR03-Auto-Push-GitHub` (a cada 30 minutos). O deploy no Vercel ocorre
cerca de 1 minuto apos o push. A geracao do snapshot nao executa nenhuma operacao git.
