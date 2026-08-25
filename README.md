# PR.03 - Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Estudos e Projetos — Relatório de Indicadores** (Engeplus Engenharia).

- **Última atualização:** 25/08/2026 13:14 (America/Sao_Paulo)
- **Timestamp ISO:** 2026-08-25T13:14:22-03:00
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Publicação:** Vercel (deploy automático a cada push)

## O que é este arquivo

`index.html` é uma cópia **estática** do Live Artifact `pr03-relatorio-indicadores-epics`.
Todas as chamadas dinâmicas ao Jira foram pré-resolvidas e congeladas em `window.__SNAPSHOT__`,
que também sobrescreve `window.cowork.callMcpTool`.
A página **não consulta o Jira ao vivo** — o banner no rodapé indica a data de congelamento.

## Períodos congelados

| Aba | Período | Origem |
|---|---|---|
| Julho 2026 | 2026-07-01 a 2026-07-31 | snapshot desta execução |
| Agosto 2026 | 2026-08-01 a 2026-08-31 | snapshot desta execução |
| Visão Acumulada | Mar/2026 a Ago/2026 | Mar, Jul e Ago desta execução; Abr–Jun do histórico embutido no artifact |

## Consultas resolvidas nesta geração

- 1x `getVisibleJiraProjects` (19 projetos; tipos de nível Epic: `Fluxo de trabalho`, `Epic`)
- **Julho 2026:** planned 10 · overdue 1 · lookahead 27 · sent 5 + resolved 8 = 11 consolidados · retrabalho 5
- **Agosto 2026:** planned 14 · overdue 1 · lookahead 29 · sent 3 + resolved 5 = 5 consolidados · retrabalho 3
- **Março 2026:** planned 7 — visão acumulada
- Total de **13 padrões JQL** mapeados em `window.__SNAPSHOT__.jql`

## Observação sobre variantes de status

O site possui variantes do status de envio (`Enviado - Aguardando Análise`,
`Enviado- Aguardando Análise`, `Enviado - Aguardando Análise1`) com IDs distintos.
O JQL agrupa essas variantes. O indicador de retrabalho deve ser lido considerando
essa particularidade da configuração de workflow do site.

## Privacidade

Os JSONs congelados contêm apenas: chave do epic, resumo, nome/categoria do status,
chave e nome do projeto, due date, data de resolução e data de atualização.
**Não** contêm accountIds, e-mails, avatares nem corpo de descrição/comentários.

## Automação

| Etapa | Responsável | Frequência |
|---|---|---|
| Gerar `index.html` + `README.md` | tarefa agendada `deploy-pr03-vercel` (Cowork) | conforme agendamento |
| `git add/commit/push` | Windows Task Scheduler `PR03-Auto-Push-GitHub` | a cada 30 min |
| Deploy | Vercel (hook de push) | ~1 min após o push |
