# PR.03 — Relatório de Indicadores de EPICs

Publicação estática do painel **PR.03 — Estudos e Projetos / Relatório de Indicadores**, gerado a partir do Live Artifact `pr03-relatorio-indicadores-epics` e dos dados do Jira Cloud da Engeplus.

## Última atualização

- **Gerado em:** 26/08/2026 16:12 (America/São_Paulo)
- **Timestamp ISO:** `2026-08-26T16:12:42-03:00`
- **Fonte:** Jira Cloud `ead785de-33f3-4746-9bdb-a2a58cf5213b` (projetos-engeplus)
- **Projetos visíveis:** 19
- **Tipos de issue de nível Epic:** Epic, Fluxo de trabalho
- **Tamanho do `index.html`:** 150,1 KB

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

| Dataset | Epics |
|---|---|
| `planned_2026-03` | 7 |
| `planned_2026-04` | 15 |
| `planned_2026-05` | 7 |
| `planned_2026-06` | 1 |
| `planned_2026-07` | 10 |
| `planned_2026-08` | 13 |
| `overdue_2026-07` | 1 |
| `overdue_2026-08` | 1 |
| `lookahead_2026-07` | 27 |
| `lookahead_2026-08` | 30 |
| `sent_2026-07` | 5 |
| `sent_2026-08` | 3 |
| `resolved_2026-07` | 8 |
| `resolved_2026-08` | 5 |
| `rework_2026-07` | 5 |
| `rework_2026-08` | 3 |

Total: 16 conjuntos + 1 listagem de projetos = **17 chamadas dinâmicas resolvidas**.

## Ressalvas de leitura dos indicadores

- **Retrabalho:** o site possui variantes de nome de status muito próximas
  (`Enviado - Aguardando Análise`, `Enviado - Aguardando Análise1`,
  `Enviado- Aguardando Análise`), com IDs distintos por workflow de projeto. Como o
  JQL casa status por *nome* em todos os workflows, a cláusula
  `status changed from "Enviado - Aguardando Análise"` acaba sendo satisfeita por
  transições entre essas variantes. Nos dois meses o conjunto de retrabalho
  coincide com o de enviados, o que produz taxa de 100% — o número deve ser lido
  como **indicativo, não conclusivo**.
- **Enviados / concluídos:** itens em variantes de "Enviado - Aguardando Análise"
  carregam `statusCategory = done`, portanto entram na contagem de concluídos
  mesmo quando ainda estão em análise do cliente.
- **Atrasados:** o número baixo (1 por mês) é real — a maioria dos epics antigos
  já está em `statusCategory = Done`.
- **Espaços em branco:** alguns `summary` e nomes de projeto vêm do Jira com
  espaço à direita (ex.: `EG0286 - DNIT/AC `), preservados como estão.

## Privacidade

Os dados congelados contêm apenas: chave do issue, resumo, nome e categoria do
status, chave e nome do projeto, data de entrega, data de resolução e data de
atualização. **Não** há `accountId`, e-mail, avatar ou responsável.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `index.html` | Página publicada (snapshot completo, autocontido) |
| `snapshot-data.js` | Mesmo bloco de dados em arquivo separado, para inspeção |
| `_artifact_src.html` | Cópia do Live Artifact usada como base da geração |
| `auto-push.ps1`, `pr03-push-watchdog.ps1`, `install-*.ps1` | Automação de commit/push no Windows |
| `vercel.json` | Configuração de deploy |

## Pipeline

1. A tarefa agendada `deploy-pr03-vercel` (Cowork) lê o Live Artifact, executa as
   consultas no Jira via MCP e regrava `index.html` + `README.md`.
2. A tarefa `PR03-Auto-Push-GitHub` do Windows Task Scheduler roda a cada 30
   minutos, detecta mudanças no working tree e faz `git add -A`, commit e push.
3. O Vercel publica automaticamente cerca de 1 minuto após o push.
