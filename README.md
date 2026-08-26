# PR.03 — Relatório de Indicadores de EPICs

Publicação estática do painel **PR.03 — Estudos e Projetos / Relatório de Indicadores**, gerado a partir do Live Artifact `pr03-relatorio-indicadores-epics` e dos dados do Jira Cloud da Engeplus.

## Última atualização

- **Gerado em:** 26/08/2026 02:15 (America/São_Paulo)
- **Timestamp ISO:** `2026-08-26T02:15:46-03:00`
- **Fonte:** Jira Cloud `ead785de-33f3-4746-9bdb-a2a58cf5213b` (projetos-engeplus)
- **Projetos visíveis:** 19
- **Tipos de issue de nível Epic:** Fluxo de trabalho, Epic

## O que é isto

O arquivo `index.html` é um **snapshot estático**: todas as chamadas ao Jira foram
pré-executadas no momento da geração e congeladas dentro da própria página
(`window.__SNAPSHOT__`). A página **não** consulta o Jira ao vivo — funciona
offline e pode ser publicada sem expor credenciais.

## Abas disponíveis

| Aba | Conteúdo |
|---|---|
| 2026-07 | Mês encerrado — planejado, atrasados, enviados, retrabalho, look-ahead |
| 2026-08 | Mês corrente — mesmos indicadores |
| Visão Acumulada | Histórico (padrão: últimos 6 meses) |

## Conjuntos de dados congelados

```
look_2026-08_2026-09=27, look_2026-09_2026-10=29, overdue_2026-07=1, overdue_2026-08=1, planned_2026-03=7, planned_2026-04=15, planned_2026-05=7, planned_2026-06=1, planned_2026-07=10, planned_2026-08=14, resolved_2026-07=8, resolved_2026-08=5, rework_2026-07=5, rework_2026-08=3, sent_2026-07=5, sent_2026-08=3
```

## Privacidade

Os JSONs embutidos passam por uma limpeza que remove `accountId`, e-mails,
avatares, ícones e conteúdo ADF. Permanecem apenas: chave da issue, resumo,
status, projeto, data de vencimento, data de resolução e data de atualização.

## Publicação

- Commit e push são automáticos (tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler, a cada 30 min).
- O deploy no Vercel ocorre cerca de 1 minuto após o push.
