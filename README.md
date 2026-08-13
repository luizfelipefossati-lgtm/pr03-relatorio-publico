# PR.03 — Relatório Público de Indicadores de EPICs

Snapshot estático do dashboard PR.03 (Estudos e Projetos), gerado automaticamente a partir do Jira.

**Última atualização:** 12/08/2026 18:39 (2026-08-12T18:39:37-0300)

Os dados são congelados no momento da geração — a página publicada não consulta o Jira ao vivo. Um script injetado adiciona os meses corrente e anterior (Agosto e Julho/2026) mais Março/2026 ao histórico interno do artifact (`window.__HISTORY__`) e sobrescreve `window.cowork.callMcpTool` (devolvendo a lista de projetos visíveis e retornando vazio para qualquer JQL). Todas as abas e a visão acumulada padrão são servidas a partir de dados congelados, sem nenhuma chamada ao Jira ao vivo. Conteúdo do snapshot:

- **Aba mensal Agosto/2026 (mês corrente):** dados reais buscados no Jira e congelados — 15 EPICs previstos (1 entregue até a data, OTD 7%), 3 em atraso acumulado, 2 enviados/concluídos no mês (0 retrabalho), 29 no look-ahead (Set–Out/2026).
- **Aba mensal Julho/2026 (mês anterior):** congelada neste snapshot — 10 EPICs previstos (8 concluídos, OTD 80%), 1 em atraso acumulado, 11 enviados/concluídos (5 com retrabalho), 28 no look-ahead (Ago–Set/2026). Exibe dados reais em vez do aviso de período sem snapshot.
- **Visão Acumulada (padrão Março–Agosto/2026):** os seis meses ficam congelados — Março (7 previstos, 3 entregues, 43%), Abril (19 previstos, 16 entregues, 84%), Maio (15 previstos, 4 entregues, 27%), Junho (2 previstos, 1 entregue, 50%), Julho (10 previstos, 8 entregues, 80%) e Agosto (15 previstos, 1 entregue, 7%). OTD acumulado: 33/68 = 49%.

Projetos monitorados (visíveis no Jira, 19): CREA, EG0232, EG0235, EG0239, EG0240, EG0241, EG0256, EG0257, EG0272, EG0273, EG0274, EG0275, EG0285, EG0286, EG0287, EG0292, G0120, G0280, PE.

Tipos de nível Epic detectados dinamicamente: "Epic" e "Fluxo de trabalho" (este último nos projetos team-managed — CREA, EG0285, EG0286, EG0287, EG0292 — incluído na apuração).

Privacidade: os dados publicados incluem chaves e títulos de EPICs e podem conter nomes de status; accountIds, avatares e e-mails são removidos. Publicação aprovada pelo usuário.

Publicação: deploy automático via Vercel após push do repositório (tarefa do Windows `PR03-Auto-Push-GitHub`, a cada 30 min).
