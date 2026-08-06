# PR.03 — Relatório de Indicadores de EPICs (snapshot público)

Snapshot **estático** do dashboard PR.03 (indicadores de EPICs do Jira Engeplus), publicado via Vercel.

- **Última geração:** 06/08/2026 13:17 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-06T13:17:25-03:00
- **Origem:** Live Artifact `pr03-relatorio-indicadores-epics`
- **Dados:** travados no momento da geração — a página **não** consulta o Jira ao vivo.

## Cobertura de dados

- Meses já congelados no artifact (`__HISTORY__`): Abril, Maio e Junho/2026.
- Congelados neste snapshot: **Agosto/2026** (mês corrente) e **Julho/2026** (mês anterior), ambos com o conjunto completo — previstos, atrasados, próximos (lookahead), enviados, resolvidos e retrabalho — além dos **previstos de Março/2026** (necessários para a visão acumulada dos últimos 6 meses).
- Julho/2026 é injetado em `__HISTORY__` como período fechado; Agosto/2026 é servido por um override de `callMcpTool` que devolve os dados pré-buscados conforme o padrão da consulta JQL. A lista de 18 projetos vem embutida. Nenhuma consulta ao Jira ao vivo é feita.

## Indicadores (no momento da geração)

- **Julho/2026:** 10 previstos, OTD 80% · 1 em atraso · 11 enviados (4 retrabalho).
- **Agosto/2026:** 16 previstos, OTD 0% (mês em curso) · 3 em atraso acumulado · 28 próximos (set–out).
- **Acumulado Mar–Ago/2026:** 56 previstos, 26 entregues, OTD 46%.

## Atualização

Gerado automaticamente por tarefa agendada. O push para o GitHub é feito pela tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min). O deploy no Vercel ocorre ~1 min após o push.

> Privacidade: os dados publicados incluem chaves e títulos de epics e nomes de status. Aprovado pelo usuário para publicação.
