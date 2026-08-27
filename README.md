# PR.03 — Relatório de Indicadores de EPICs

Publicação estática do painel **PR.03 — Estudos e Projetos / Relatório de Indicadores**, gerado a partir do Live Artifact `pr03-relatorio-indicadores-epics` e dos dados do Jira Cloud da Engeplus.

## Última atualização

- **Gerado em:** 26/08/2026 23:33 (America/São_Paulo)
- **Timestamp ISO:** `2026-08-26T23:33:35-03:00`
- **Fonte:** Jira Cloud `ead785de-33f3-4746-9bdb-a2a58cf5213b` (projetos-engeplus)
- **Projetos visíveis:** 19
- **Tipos de issue de nível Epic:** Epic, Fluxo de trabalho
- **Tamanho do `index.html`:** 128,1 KB
- **Chamadas dinâmicas resolvidas:** 14 (1× `getVisibleJiraProjects` + 13 consultas JQL)

## O que é isto

O arquivo `index.html` é um **snapshot estático**: todas as chamadas ao Jira foram
pré-executadas no momento da geração e congeladas dentro da própria página
(`window.__SNAPSHOT__`). A página **não** consulta o Jira ao vivo — funciona
offline e pode ser publicada sem expor credenciais.

## Abas disponíveis

| Aba | Conteúdo |
|---|---|
| Julho 2026 | Mês encerrado — planejado, atrasados, enviados, retrabalho, look-ahead |
| Agosto 2026 | Mês corrente — mesmos indicadores |
| Visão Acumulada | Histórico (padrão: últimos 6 meses, Março–Agosto 2026) |

## Conjuntos de dados congelados

| Dataset | Epics |
|---|---|
| `planned_2026-03` | 7 |
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

Abril, Maio e Junho de 2026 já vêm congelados dentro do próprio artifact
(`window.__HISTORY__`) e não são reconsultados. Julho e Agosto de 2026 são
resolvidos pelo stub de snapshot a partir dos datasets acima, exatamente com a
mesma lógica de agregação do painel ao vivo.

## Observação sobre o indicador de retrabalho

A consulta de "enviados" usa a string literal `"Enviado - Aguardando Análise"`.
Alguns projetos usam variantes do nome do status — `Enviado - Aguardando Análise1`
(EG0239, EG0256, EG0273) e `Enviado- Aguardando Análise` (EG0285, sem espaço antes
do hífen). Esses itens entram em `resolved_*` mas não em `sent_*`, o que pode
subcontar as entregas enviadas e, por consequência, o retrabalho. Nesta geração:

- **Agosto/2026:** 2 de 5 entregas resolvidas ficaram fora de `sent` (EG0285-8, EG0239-28).
- **Julho/2026:** 6 de 8 entregas resolvidas ficaram fora de `sent` (3 por variante de nome no EG0256; 3 fechadas direto em `Concluído`).

Padronizar os nomes de status no Jira corrigiria a distorção.

## Estrutura do repositório

| Arquivo | Descrição |
|---|---|
| `index.html` | Página publicada (snapshot estático, autocontido) |
| `snapshot-data.js` | Mesmos dados congelados em arquivo separado, para inspeção |
| `_artifact_src.html` | Cópia do Live Artifact usada como base da geração |
| `vercel.json` | Configuração de deploy |
| `*.ps1` | Scripts de automação (commit/push agendado no Windows) |

## Privacidade

Os dados publicados contêm apenas: chave da epic, resumo, nome e categoria do
status, chave e nome do projeto, data prevista, data de resolução e data de
atualização. **Não** há accountIds, e-mails, avatares, iconUrls ou conteúdo de
comentários (verificado por varredura no `index.html` gerado).

## Publicação

O commit e o push são feitos automaticamente pela tarefa `PR03-Auto-Push-GitHub`
do Windows Task Scheduler (a cada 30 minutos). O deploy no Vercel ocorre cerca de
1 minuto após o push.
