# PR.03 — Relatório de Indicadores de EPICs (Snapshot Público)

Página estática publicada a partir do Live Artifact **Pr03 Relatorio Indicadores Epics**.
Os dados são um *snapshot* congelado do Jira: a página publicada **não** consulta o Jira ao vivo.

- **Última geração do snapshot:** 04/08/2026 13:15 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-04T13:15:03
- **Meses congelados neste build:** Março, Julho e Agosto/2026 (Abril–Junho/2026 já vinham congelados no artifact).
- **Projetos monitorados:** EG0239, EG0240, EG0241, EG0256, EG0273, EG0274, EG0275, EG0285, EG0286, EG0287, G0280 e demais visíveis no board.

## Como é gerado
Uma tarefa agendada regenera este `index.html` a partir do artifact, injetando os dados pré-buscados (`window.__SNAPSHOT__` / `window.__HISTORY__`) e substituindo as chamadas MCP por respostas locais. O commit/push para o GitHub é feito automaticamente pela tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min); o deploy é feito pela Vercel.
