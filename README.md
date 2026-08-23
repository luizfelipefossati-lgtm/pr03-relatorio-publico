# PR.03 — Relatório de Indicadores de EPICs

Snapshot **estático** do dashboard PR.03 (Estudos e Projetos) da Engeplus Engenharia e Consultoria.

- **Última atualização:** 23/08/2026 (America/Sao_Paulo)
- **Fonte:** Jira — projetos-engeplus.atlassian.net (issuetype de nível Epic)
- **Artifact de origem:** `pr03-relatorio-indicadores-epics`

## Como funciona

A página é gerada a partir do Live Artifact, com todas as consultas ao Jira **pré-executadas** e
embutidas em `window.__SNAPSHOT__`. O `window.cowork.callMcpTool` é substituído por um resolvedor
local que devolve os dados congelados conforme o padrão da JQL. **A página publicada não consulta
o Jira ao vivo.**

A partir desta geração os dados ficam em um arquivo separado, `snapshot-data.js`, carregado pelo
`index.html` imediatamente antes do script principal do artifact. Ele sobrepõe `window.__SNAPSHOT__`,
`window.__HISTORY__` e `window.cowork.callMcpTool`. Vantagem: as próximas atualizações reescrevem
apenas `snapshot-data.js`, sem tocar no HTML.

Tipos de issue de nível Epic considerados: `Epic` e `Fluxo de trabalho` (projetos team-managed),
descobertos por `hierarchyLevel === 1` na listagem de projetos. 19 projetos visíveis.

## Conteúdo deste snapshot

| Visão | Dados |
|---|---|
| Julho/2026 (encerrado) | 10 previstos, 1 em atraso acumulado, 11 enviados (5 com retrabalho), 8 resolvidos, 27 na visão prospectiva |
| Agosto/2026 (mês corrente) | 14 previstos, 2 em atraso acumulado, 4 enviados consolidados (2 com retrabalho), 29 na visão prospectiva |
| Visão acumulada (Mar–Ago/2026) | previstos por mês; Mar (7) consultado nesta geração, Abr/Mai/Jun vêm do histórico congelado no artifact, Jul e Ago congelados neste snapshot |

13 consultas JQL + 1 listagem de projetos (19 projetos) embutidas neste snapshot.
Julho e Agosto também foram gravados em `window.__HISTORY__`, então as abas mensais e a visão
acumulada são resolvidas sem passar pelo resolvedor de JQL — que fica como camada de segurança.

## Notas desta geração

- Julho/2026 é período encerrado e foi congelado em `window.__HISTORY__["2026-07"]`. Sem esse
  congelamento a aba de Julho exibiria o aviso "Período encerrado sem snapshot", porque o artifact
  não consulta o Jira para meses fechados.
- O sandbox Linux da sessão não subiu (`installSdk` timeout), então não houve `jq` nem acesso a
  shell. As respostas JQL foram reduzidas ao mínimo (`key`, `summary`, `status`, `project`,
  `duedate`, `resolutiondate`, `updated`) por subagentes isolados, para não estourar o limite de
  tokens. Nenhuma operação de git foi executada.
- Sem shell também não houve relógio disponível na sessão. Por isso o carimbo desta geração tem
  precisão de **data** (23/08/2026), sem hora — preferiu-se omitir a hora a inventá-la.
- O conector MCP do Jira ignora parcialmente o parâmetro `fields` e devolve `issuetype`,
  `assignee` e `description` de qualquer forma. Esses campos foram descartados na redução; não
  chegam ao arquivo publicado.
- Checagens de coerência aplicadas nesta geração:
  - `retrabalho ⊆ enviados` — Jul: os 5 conjuntos coincidem; Ago: 2 de 2.
  - `previstos do mês ⊆ visão prospectiva do mês anterior` — as 14 issues de Ago aparecem nas 27
    de `look_2026-07`.
  - Contagens conferem com a geração anterior do mesmo dia, indicando estabilidade dos dados.
- Consolidação de "enviados" segue a regra do artifact: união de `status changed to "Enviado -
  Aguardando Análise"` com `statusCategory=Done AND resolved` no período, priorizando a primeira.
  Em Agosto: 2 enviados + 4 resolvidos → 4 distintos.
- Observações de dados do Jira, não corrigidas aqui (refletem o site): status com grafias
  divergentes — `Enviado - Aguardando Análise1` e `Em Revisã` — e o projeto `EG0280 - DMAE` cuja
  chave é `G0280`.
- `resolved<="YYYY-MM-DD"` é avaliado pelo Jira como 00:00 do último dia, então resoluções
  ocorridas ao longo do último dia do mês não entram na consulta `resolved`. Comportamento
  herdado do artifact, mantido para não divergir da versão ao vivo.

## Privacidade

Os dados publicados contêm apenas: chave da issue, título (summary), projeto, status, data
prevista, data de resolução e data de atualização. **Não** há accountIds, e-mails, avatares nem
responsáveis. Nomes de pessoas podem aparecer apenas se estiverem escritos no título de alguma
issue.

## Publicação

O commit e o push são feitos automaticamente pela tarefa `PR03-Auto-Push-GitHub`
(Windows Task Scheduler, a cada 30 minutos). O deploy no Vercel ocorre cerca de 1 minuto após o push.

> **Atenção:** `snapshot-data.js` é um arquivo novo. Se a tarefa de push usar `git add -A` ele será
> incluído normalmente; se usar uma lista fixa de arquivos, `snapshot-data.js` precisa ser
> adicionado, senão a página publicada continuará servindo os dados antigos embutidos no HTML.
