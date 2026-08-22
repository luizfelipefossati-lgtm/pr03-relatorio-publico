# PR.03 - Relatório de Indicadores de EPICs (Snapshot Público)

Página estática publicada automaticamente a partir do Live Artifact **"Pr03 Relatorio Indicadores Epics"** (dashboard Jira da Engeplus Engenharia).

- **Última atualização (snapshot):** 22/08/2026 12:20
- **Origem dos dados:** Jira Cloud (projetos de Estudos e Projetos)
- **Natureza:** dados **travados** no momento da geração — a página não consulta o Jira ao vivo.

## Como funciona a automação

1. Uma tarefa agendada gera este snapshot estático, pré-buscando via MCP os dados do mês corrente, do mês anterior e da visão acumulada. Os meses são injetados em `window.__HISTORY__` por `window.__SNAPSHOT__`, e a sobrescrita de `window.cowork.callMcpTool` serve `getVisibleJiraProjects` e qualquer consulta JQL residual offline (roteamento por padrão de JQL: planned, overdue, lookahead, sent/rework e resolved; vazio quando não houver dado pré-buscado).
2. O relógio da página é **congelado** no instante da geração. Sem isso, o navegador de quem abre a página recalcularia as abas e o lookahead pela data atual do visitante e, ao virar o mês, o relatório apareceria vazio. As abas ficam fixas em Julho/Agosto 2026 e o acumulado em Março–Agosto 2026.
3. A tarefa `PR03-Auto-Push-GitHub` (Windows Task Scheduler, a cada 30 min) detecta as mudanças no working tree e faz `git commit + push` automaticamente.
4. O Vercel publica o novo `index.html` cerca de 1 minuto após o push.

## Conteúdo capturado neste snapshot

- Aba mensal **Agosto 2026** (mês corrente): 14 epics previstos, 2 entregues (ambos com pequeno atraso), 12 pendentes, 2 em atraso acumulado, 4 enviados/resolvidos no período (2 com retrabalho), 29 no lookahead. **OTD 14%** — mês em curso, 7 dos 14 vencem em 31/08.
- Aba mensal **Julho 2026** (mês anterior, encerrado): 10 epics previstos, 8 entregues (5 no prazo, 3 com pequeno atraso), 2 pendentes, 1 em atraso acumulado, 11 enviados/resolvidos no período (5 com retrabalho), 27 no lookahead. **OTD 80%**.
- Próximos 2 meses (**Set–Out 2026**): 29 epics com vencimento previsto (lookahead de agosto).
- Visão **Acumulada** dos últimos 6 meses (Março–Agosto 2026): Mar 7 (OTD 43%), Abr 19 (84%), Mai 15 (27%), Jun 2 (50%), Jul 10 (80%) e Ago 14 (14%) epics previstos — **67 previstos e 34 entregues** no período (OTD acumulado **51%**).
- Projetos com epics previstos em agosto: EG0239, EG0240, EG0241, EG0275, EG0286 e EG0280 (`G0280`).
- Indicadores: OTD, previstos/entregues/pendentes, retrabalho e lookahead.
- Tipos de issue de nível Epic detectados no Jira: `Epic` e `Fluxo de trabalho` (19 projetos visíveis).

## Notas deste ciclo

- Os meses encerrados **Abril, Maio e Junho de 2026** são preservados congelados do artifact de origem (Abr 19, Mai 15 e Jun 2 epics previstos) e **não** são re-consultados ao vivo — períodos fechados não devem mudar.
- Correção em relação ao ciclo anterior: o snapshot de 11:14 havia **sobrescrito** o bloco `window.__HISTORY__` do artifact, descartando Abril/Maio/Junho e deixando a visão acumulada dependente de re-consulta. Este ciclo reconstrói a página a partir do artifact de origem, mantendo os três meses congelados intactos e verificados (contagens e `_frozen_at` conferidos item a item).
- **Julho 2026** e **Agosto 2026** foram consultados nesta execução (12 queries JQL) mais 8 queries `planned` de apoio ao acumulado e 1 `getVisibleJiraProjects`. Julho usa corte histórico em 31/07 (`resolutiondate <= 31/07`), de modo que alterações posteriores no Jira não deslocam o OTD já fechado.
- Verificação pós-geração: as 24 chamadas dinâmicas da página foram reexecutadas contra o snapshot e todas resolveram offline, com as contagens esperadas — nenhuma requisição ao Jira permanece na página publicada.
- `EG0274-38` ("Estudos de Tráfego") teve a due date reprogramada de 11/08/2025 para 17/07/2026 e por isso passa a figurar no atraso acumulado de agosto.

## Limitações herdadas do artifact (não alteradas aqui)

- As consultas de enviados/retrabalho filtram pela grafia exata `Enviado - Aguardando Análise`. Existem no Jira as variantes `Enviado- Aguardando Análise` (EG0285) e `Enviado - Aguardando Análise1` (EG0239, EG0256, EG0273), que ficam fora dessas duas métricas — os epics correspondentes ainda são contados como entregues via `statusCategory=Done`. Padronizar os nomes de status no Jira resolveria a divergência.
- Nos dois meses consultados, a consulta de retrabalho retornou **exatamente o mesmo conjunto** da consulta de enviados (5/5 em julho, 2/2 em agosto). A cláusula `status changed from "Enviado - Aguardando Análise"` não discrimina nada nesses períodos, porque todo epic que entrou nesse status também registrou saída dele no histórico. A taxa de retrabalho, portanto, está superestimada e deve ser lida com reserva até que a regra seja revista no artifact.
- O status `Enviado - Aguardando Análise` tem `statusCategory = done`, ou seja, epics aguardando análise do cliente são contados como entregues no OTD.

## Privacidade

Os dados publicados incluem chaves e títulos de epics e nomes de status. Os JSONs de origem já excluem `accountId`, e-mails e avatares — verificado neste ciclo (0 ocorrências de `accountId`, `avatarUrl`, `emailAddress`, `displayName`, `self` e URLs de avatar no payload). Publicação aprovada pelo usuário.

> Nota de qualidade de dado: os status `Em Revisã` (EG0275-6) e `Enviado - Aguardando Análise1` são os nomes reais cadastrados no Jira — não são truncamentos nem erros do snapshot.

_Gerado automaticamente. Não editar manualmente — as alterações são sobrescritas no próximo ciclo._
