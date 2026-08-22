# PR.03 - Relatorio de Indicadores de EPICs

Publicacao estatica do dashboard **Estudos e Projetos - Relatorio de Indicadores**
(Engeplus Engenharia), gerado a partir do Live Artifact `pr03-relatorio-indicadores-epics`.

- **Ultima atualizacao:** 22/08/2026 17:11
- **Fonte:** Jira Cloud (projetos EG####) - dados congelados no momento da geracao
- **Abas:** Julho 2026 (encerrado), Agosto 2026 (mes corrente), Visao Acumulada (Mar-Ago/2026)

## Como funciona

O `index.html` e uma copia do artifact com um bloco `window.__SNAPSHOT__` injetado.
Esse bloco substitui `window.cowork.callMcpTool`, devolvendo os resultados JQL
pre-buscados em vez de consultar o Jira. A pagina, portanto, **nao acessa o Jira
ao vivo** e pode ser publicada sem credenciais.

## Dados consolidados neste snapshot

| Consulta | Registros |
|---|---|
| Previstos Ago/2026 | 14 |
| Em atraso acumulado (< Ago/2026) | 2 |
| Enviados Ago/2026 | 2 |
| Resolvidos Ago/2026 | 4 |
| Retrabalho Ago/2026 | 2 |
| Look-ahead Set-Out/2026 | 29 |
| Previstos Jul/2026 (congelado) | 10 |
| Em atraso acumulado (< Jul/2026) | 1 |
| Enviados + Resolvidos Jul/2026 | 11 |
| Retrabalho Jul/2026 | 5 |
| Look-ahead Ago-Set/2026 (aba Jul) | 27 |
| Previstos Mar/2026 (acumulado) | 7 |

Abr/2026, Mai/2026 e Jun/2026 da Visao Acumulada vem do bloco `window.__HISTORY__`
ja embutido no artifact de origem.

## Publicacao

Commit e push sao feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub` (a cada 30 minutos). O deploy no Vercel ocorre cerca de
1 minuto apos o push.
