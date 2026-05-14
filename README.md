# Relatorio PR03 - Indicadores Epicos

Snapshot publico do dashboard de OTD por EPICs do Jira (projetos Engeplus).
Atualizado automaticamente pelo scheduled task "deploy-pr03-vercel".

- **Ultima geracao:** 2026-05-14T12:10:46Z (14/05/2026 09:10 -03)
- **Periodo coberto:** Visao Mensal (Abr/Mai 2026) + Acumulado (Dez/2025 - Mai/2026)
- **Fonte:** projetos-engeplus.atlassian.net (issuetype = Epic)
- **Hospedagem:** Vercel (auto-deploy a partir deste repo)

## Como funciona

Os dados sao buscados via MCP do Jira no momento da geracao do snapshot, embutidos
no HTML como variavel `window.__SNAPSHOT__`, e o JavaScript original do artifact
`callMcpTool` foi monkey-patched para devolver esses dados em vez de fazer
requisicao ao vivo. Isso permite que a pagina rode em dominio publico sem
acesso ao Jira.


---
*Última atualização: 14/05/2026 09:10 (BRT)*
