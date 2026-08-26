# PR.03 — Relatório de Indicadores de EPICs

Publicação estática do painel **PR.03 — Estudos e Projetos / Relatório de Indicadores**, gerado a partir do Live Artifact `pr03-relatorio-indicadores-epics` e dos dados do Jira Cloud da Engeplus.

## Última atualização

- **Gerado em:** 26/08/2026 14:13 (America/São_Paulo)
- **Timestamp ISO:** `2026-08-26T14:13:13-03:00`
- **Fonte:** Jira Cloud `ead785de-33f3-4746-9bdb-a2a58cf5213b` (projetos-engeplus)
- **Projetos visíveis:** 19
- **Tipos de issue de nível Epic:** Epic, Fluxo de trabalho

## O que é isto

O arquivo `index.html` é um **snapshot estático**: todas as chamadas ao Jira foram
pré-executadas no momento da geração e congeladas dentro da própria página
(`window.__SNAPSHOT__`). A página **não** consulta o Jira ao vivo — funciona
offline e pode ser publicada sem expor credenciais.

## Abas disponíveis

| Aba | Conteúdo |
|---|---|
| Julho 2026 | Mês encerrado — planejado, atrasados, enviados, retrabalho, look-ahead (congelado em `window.__HISTORY__`) |
| Agosto 2026 | Mês corrente — mesmos indicadores |
| Visão Acumulada | Histórico (padrão: últimos 6 meses, Março–Agosto 2026) |

## Conjuntos de dados congelados

```
lookahead_2026-07=27, lookahead_2026-08=30, overdue_2026-07=1, overdue_2026-08=1,
planned_2026-03=7, planned_2026-04=15, planned_2026-05=7, planned_2026-06=1,
planned_2026-07=10, planned_2026-08=13, resolved_2026-07=8, resolved_2026-08=5,
rework_2026-07=5, rework_2026-08=3, sent_2026-07=5, sent_2026-08=3
```

16 conjuntos de dados / 16 padrões de consulta resolvidos + 1 chamada de projetos
(17 chamadas dinâmicas do artifact no total).

Totais de "enviados" exibidos no painel (união de `sent` + `resolved`, sem duplicatas):
**Julho 2026 = 11** (5 em retrabalho) e **Agosto 2026 = 5** (3 em retrabalho).

## Verificação desta geração

Antes da publicação, o snapshot passou por teste funcional automatizado que
reexecuta em Node.js **todas** as consultas JQL que o artifact monta em tempo de
execução (2 abas mensais × 6 consultas + 4 meses adicionais da visão acumulada + projetos):

```
17/17 checks OK, 0 falhas, 0 JQL sem correspondência no snapshot
```

Também verificado: sintaxe JavaScript válida (`node --check`), execução limpa do
shim embutido, integridade do HTML (5 blocos `<script>` abertos e fechados, banner
antes de `</body>`, bloco do snapshot antes do script principal) e ordem correta dos
padrões (`rework` é avaliado antes de `sent`, caso contrário a consulta de retrabalho
cairia no conjunto de enviados).

## Observações sobre os dados desta geração

- **Julho encerrado e congelado.** Os dados de julho foram preservados exatamente
  como no fechamento do período e receberam a marcação `_frozen_at`. Alterações
  feitas no Jira após 31/07/2026 não afetam a aba de julho — apenas os meses
  abertos são reconsultados a cada geração.
- **Março a junho reconsultados nesta geração.** Nesta versão apenas julho entra em
  `window.__HISTORY__`; os meses de março a junho da Visão Acumulada são servidos
  pelos conjuntos `planned_*` recém-buscados, então os valores acima são exatamente
  os que o painel exibe.
- **EG0286 - DNIT/AC no relatório.** O projeto tem epics do tipo "Fluxo de trabalho"
  e responde por parte relevante dos 13 epics previstos em agosto e dos 30 itens do
  look-ahead.
- **Variações no nome do status.** O site possui status quase homônimos —
  `Enviado - Aguardando Análise`, `Enviado- Aguardando Análise` (sem espaço antes do
  hífen, em EG0285-8) e `Enviado - Aguardando Análise1` (em EG0239-28 e EG0256-25/26/27).
  As consultas `sent` / `rework` usam o nome literal, então itens com as variantes
  aparecem apenas em `resolved`. O painel une `sent` + `resolved` para o total de
  enviados, o que compensa a diferença.
- **Retrabalho superestimado.** Em julho o conjunto `rework` coincide integralmente
  com o `sent` (5 de 5) e em agosto também (3 de 3). A cláusula `status changed from`
  não carrega janela `DURING`, portanto casa com qualquer transição histórica de saída
  daquele status — o indicador tende a superestimar o retrabalho.
- **Atrasos acumulados.** Há 1 epic não concluído com vencimento anterior a
  01/08/2026 (`overdue_2026-08=1`).
- **Chave de projeto `G0280`.** O projeto exibido como `EG0280 - DMAE` tem chave real
  `G0280` (sem o "E"), portanto suas issues aparecem como `G0280-51` etc. O mesmo vale
  para `EG0120 - DAER`, cuja chave é `G0120`.
- **Sem epics.** `EG0232 - EMBASA` e `Projetos - Engenharia` (PE) não possuem tipo de
  issue de nível Epic e por isso não aparecem nos indicadores.
- **Fora da faixa congelada.** Se o seletor da Visão Acumulada for movido para meses
  anteriores a Março/2026 ou posteriores a Agosto/2026, o painel exibirá zero — esses
  períodos não foram pré-buscados neste snapshot.

## Privacidade

Os JSONs embutidos passam por uma limpeza que remove `accountId`, e-mails,
avatares, ícones, URLs internas (`self`) e conteúdo ADF. Permanecem apenas: chave
da issue, resumo, status, projeto, data de vencimento, data de resolução e data de
atualização. Verificado nesta geração no `index.html`: **0 ocorrências** de
`avatarUrl`, `emailAddress`, `iconUrl` e `displayName`; a única correspondência de
`accountId` é a própria nota do cabeçalho do script.

## Publicação

- Commit e push são automáticos (tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 min).
- O deploy no Vercel ocorre cerca de 1 minuto após o push.
