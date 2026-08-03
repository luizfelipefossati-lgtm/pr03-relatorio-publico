# PR.03 — Relatório de Indicadores de EPICs (snapshot público)

Snapshot **estático** do painel PR.03 (Estudos e Projetos / Engeplus), publicado via Vercel.
Os dados são congelados no momento da geração — a página **não** consulta o Jira ao vivo.

- **Última geração:** 03/08/2026 11:14 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-03T11:17:01-03:00
- **Mês corrente (capturado ao vivo):** Agosto/2026 — 16 EPICs previstos, 3 em atraso acumulado, 28 no lookahead (set–out), 0 enviados/resolvidos/retrabalho no mês até a captura
- **Mês anterior (congelado nesta geração):** Julho/2026 — 10 EPICs previstos, 1 em atraso, 10 enviados/resolvidos (4 com retrabalho), 28 no lookahead (ago–set)
- **Visão acumulada congelada:** Março–Agosto/2026 (mar, jul e ago buscados nesta geração; abr/mai/jun do histórico embutido)
- **Projetos monitorados:** 17 (Jira cloud ead785de-…)
- **Chamadas dinâmicas resolvidas:** `getVisibleJiraProjects` + 13 consultas JQL (planned/overdue/lookahead/sent/resolved/rework de jul e ago/2026 + planned de mar/2026 para o acumulado)

> Observação: tanto Agosto (ao vivo) quanto Julho (encerrado) agora exibem dados completos nas abas mensais; os EPICs previstos de mar/jul/ago também alimentam a visão acumulada.

> Atualização automática: o snapshot é regenerado periodicamente e o push para o GitHub é feito pela tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min). O deploy no Vercel ocorre ~1 min após o push.
