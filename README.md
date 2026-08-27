# PR.03 - Relatorio de Indicadores de EPICs (snapshot publico)

Pagina estatica publicada a partir do artifact **Pr03 Relatorio Indicadores Epics**.

- **Ultima atualizacao:** 27/08/2026 09:12 (2026-08-27T09:12:20-03:00)
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como Epic:** Epic, Fluxo de trabalho
- **Projetos visiveis no snapshot:** 19
- **Tamanho de `index.html`:** 138.5 KB

## Como funciona

O `index.html` e uma copia do artifact com todos os dados do Jira **pre-buscados e embutidos**.
Um script injetado define `window.__SNAPSHOT__` e substitui `window.cowork.callMcpTool`,
devolvendo os dados congelados conforme o padrao da consulta JQL. A pagina publicada
**nao consulta o Jira ao vivo** e nao precisa de credenciais.

O script injetado entra **depois** do bloco `window.__HISTORY__` proprio do artifact
(que congela 2026-04 a 2026-06) e **antes** do script principal, de modo que os dois
conjuntos historicos coexistem em vez de um sobrescrever o outro. Na pagina carregada,
`window.__HISTORY__` fica com as chaves `2026-04`, `2026-05`, `2026-06` (nativas) e
`2026-07` (do snapshot). Ordem verificada nesta geracao: bloco nativo (offset 22.453)
-> bloco do snapshot (53.537) -> script principal (107.146).

O HTML base usado na geracao e o `_artifact_src.html` deste repositorio (947 linhas,
md5 `6a2b6462a4efbec1890af4494a7f0b74`), verificado contra o artifact atual
(`Artifacts\pr03-relatorio-indicadores-epics\index.html`) por contagem de linhas,
posicao dos blocos `<script>` (1, 21, 280, 283) e comparacao de linhas-ancora
(500-502, 700, 944-947), todas identicas. Se o artifact for editado,
`_artifact_src.html` precisa ser atualizado junto.

## Verificacao desta geracao

As 17 chamadas dinamicas do artifact (1x `getVisibleJiraProjects` + 16 consultas JQL)
foram reproduzidas contra o `index.html` gerado, remontando a construcao de JQL do
artifact para a data de referencia 27/08/2026:

- **16** consultas JQL casaram com o padrao correto, cada uma apontando para o dataset
  esperado (nenhum `JQL sem correspondencia`);
- **1** `getVisibleJiraProjects`, devolvendo os 19 projetos;
- meses 2026-04 a 2026-07 continuam sendo servidos por `window.__HISTORY__` sem gerar
  JQL na visao acumulada; os datasets equivalentes ficam embutidos como fallback.

Tambem verificado: comentario de timestamp no topo do `<head>`, banner de aviso
imediatamente antes de `</body>` (depois do `go();`), 5 tags `<script>` abertas e 5
fechadas, `</html>` no final do arquivo, um unico override de `callMcpTool`, e ausencia
de `accountId` / `emailAddress` / `avatarUrls` / `712020:` nos dados embutidos (a unica
ocorrencia da string `accountIds` esta no comentario de privacidade do proprio bloco).

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
| `planned_2026-07` | 10 | ativo (aba de Julho) |
| `overdue_2026-07` | 1 | ativo (aba de Julho) |
| `lookahead_2026-07` | 27 | ativo (aba de Julho) |
| `sent_2026-07` | 5 | ativo (aba de Julho) |
| `resolved_2026-07` | 8 | ativo (aba de Julho) |
| `rework_2026-07` | 5 | ativo (aba de Julho) |
| `planned_2026-03` | 7 | ativo |
| `planned_2026-04` | 15 | fallback |
| `planned_2026-05` | 7 | fallback |
| `planned_2026-06` | 1 | fallback |

Todos os 16 conjuntos foram reconsultados no Jira nesta geracao e os totais coincidiram
com a geracao anterior (27/08/2026 08:14), sem alteracao de volume.

Mes encerrado de **Julho/2026** congelado em `window.__SNAPSHOT__.months` (que alimenta
`window.__HISTORY__`) para exibir os dados reais do periodo em vez do aviso de "sem
snapshot": 11 enviados e 5 com retrabalho (5 de `sent_2026-07` unidos a
8 de `resolved_2026-07`, sem duplicatas).

Visao acumulada padrao: **Marco a Agosto/2026** (ultimos 6 meses). Marco e Agosto sao
resolvidos via JQL embutida; Abril a Julho vem congelados de `window.__HISTORY__`.

## Observacao sobre status

O site usa variantes de nome quase identicas que caem na categoria `done`:
`Enviado - Aguardando Analise`, `Enviado - Aguardando Analise1` e `Enviado- Aguardando Analise`
(IDs distintos por projeto). A clausula JQL `status changed to "Enviado - Aguardando Analise"`
depende do nome exato, por isso `resolved_*` pode ser maior que `sent_*` — em Agosto,
5 contra 3. O relatorio une os dois conjuntos.

Ha tambem nomes com ruido preservado fielmente do Jira: status truncado `Em Revisa`
(EG0275-6), projeto com chave `G0280` e nome `EG0280 - DMAE`, e nomes com espaco final
(`EG0286 - DNIT/AC `). Nada foi normalizado.

## Ressalvas conhecidas

**`rework_*` superestima o retrabalho.** A clausula `status changed from "Enviado -
Aguardando Analise"` nao tem janela temporal e casa com qualquer saida daquele status,
inclusive a transicao normal rumo ao encerramento (ex.: "Medido e Faturado"). Nesta
geracao os conjuntos `sent` e `rework` coincidiram integralmente nos dois meses
(Agosto 3 e 3, Julho 5 e 5). Para medir devolucao real, a consulta precisaria
restringir o destino da transicao (ex.: `... to "Em Revisao"`) e/ou limitar a janela.

**Limite superior de `resolved_*`.** O Jira interpreta `resolved<="AAAA-MM-DD"` como
meia-noite daquele dia, entao itens resolvidos ao longo do ultimo dia do mes ficam de fora
do conjunto `resolved_*`. Corrigir exigiria alterar o artifact para
`resolved<"primeiro-dia-do-mes-seguinte"`.

**Congelamento de Julho nao e uma foto de 31/07.** O mes encerrado e reconsultado a cada
geracao do snapshot, portanto reflete o estado **atual** das issues com vencimento em
Julho. Alteracoes retroativas no Jira ainda afetam os numeros de Julho.

**Abril a Junho vem do artifact, nao desta geracao.** Na visao acumulada esses tres meses
sao servidos pelo bloco `window.__HISTORY__` embutido no proprio artifact; os datasets
`planned_2026-04/05/06` reconsultados aqui ficam apenas como fallback.

## Privacidade

Os dados embutidos contem apenas: chave da issue, resumo, status, projeto, data de
entrega, data de resolucao e data de atualizacao. **Nao ha** accountIds, e-mails,
avatares, URLs internas da API nem descricoes. Nomes de pessoas podem aparecer apenas se
estiverem escritos no resumo de alguma issue — publicacao aprovada pelo usuario.

## Publicacao

O commit e o push para o GitHub sao feitos automaticamente pela tarefa do Windows
Task Scheduler `PR03-Auto-Push-GitHub` (a cada 30 minutos). O deploy no Vercel ocorre
cerca de 1 minuto apos o push. A geracao do snapshot nao executa nenhuma operacao git.
