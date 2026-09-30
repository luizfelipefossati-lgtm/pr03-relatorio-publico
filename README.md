# PR.03 — Relatório de Indicadores de EPICs

Publicação estática (snapshot) do dashboard **Estudos e Projetos — Relatório de Indicadores** da Engeplus Engenharia e Consultoria.

> **Última atualização do snapshot: 30/09/2026 01:34** (`2026-09-30T01:34:28-03:00`)

---

## O que é

Esta página é uma **cópia congelada** do Live Artifact `pr03-relatorio-indicadores-epics`.
Os dados do Jira são pré-buscados no momento da geração e embutidos no próprio `index.html`.
A página publicada **não consulta o Jira ao vivo** — não há credenciais, tokens nem chamadas de rede para a Atlassian.

## Conteúdo do snapshot

Fonte: Jira Cloud `projetos-engeplus` (`ead785de-33f3-4746-9bdb-a2a58cf5213b`)
Tipos de issue considerados como Epic: `Epic`, `Fluxo de trabalho`
Projetos visíveis mapeados: **21**

### Consultas resolvidas (13 conjuntos + lista de projetos)

| Conjunto | Escopo | Registros |
|---|---|---:|
| `planned_2026-07` | Epics com due date em jul/2026 (visão acumulada) | 9 |
| `planned_2026-08` | Epics com due date em ago/2026 | 3 |
| `overdue_2026-08` | Vencidos antes de ago/2026, não concluídos | 0 |
| `lookahead_2026-08` | Due date entre set/2026 e out/2026 | 40 |
| `sent_2026-08` | Transições para "Enviado - Aguardando Análise" em ago/2026 | 4 |
| `resolved_2026-08` | Concluídos em ago/2026 | 4 |
| `rework_2026-08` | Retrabalho (saiu de "Enviado - Aguardando Análise") em ago/2026 | 3 |
| `planned_2026-09` | Epics com due date em set/2026 | 17 |
| `overdue_2026-09` | Vencidos antes de set/2026, não concluídos | 1 |
| `lookahead_2026-09` | Due date entre out/2026 e nov/2026 | 32 |
| `sent_2026-09` | Transições para "Enviado - Aguardando Análise" em set/2026 | 6 |
| `resolved_2026-09` | Concluídos em set/2026 | 4 |
| `rework_2026-09` | Retrabalho em set/2026 | 3 |

Os meses de **abr/2026, mai/2026 e jun/2026** continuam vindo do histórico já congelado dentro do
artifact (`window.__HISTORY__`), preservado sem alteração.

## Abas disponíveis

- **Agosto 2026** — período encerrado, dados congelados no snapshot.
- **Setembro 2026** — mês corrente na data de geração, congelado no snapshot.
- **Visão Acumulada** — abr/2026 a set/2026 (padrão: últimos 6 meses).

## Estrutura

| Arquivo | Função |
|---|---|
| `index.html` | Página publicada, auto-contida (HTML + dados + lógica). |
| `snapshot-data.js` | Cópia avulsa do bloco de dados embutido, para inspeção. |
| `_gen_snapshot.py`, `_snap/`, `_projects_min.json` | Insumos e gerador de execuções anteriores. |
| `auto-push.ps1`, `install-task.ps1` e afins | Automação local de commit/push no Windows. |

A única dependência externa da página é o Chart.js via CDN (`cdn.jsdelivr.net`), usado para os gráficos.

## Publicação

O commit e o push são feitos automaticamente pela tarefa do Windows Task Scheduler
`PR03-Auto-Push-GitHub`, que verifica o working tree a cada 30 minutos.
O deploy no Vercel ocorre cerca de 1 minuto após o push.

## Privacidade

Os conjuntos de dados embutidos contêm apenas: chave do epic, resumo, status (nome e categoria),
projeto (chave e nome), due date, data de resolução e data de atualização.
**Não** incluem `accountId`, e-mails, avatares, descrições em ADF nem `iconUrl`.

## Observação sobre os status de envio

As consultas `sent` e `rework` casam exatamente a string `Enviado - Aguardando Análise`.
O Jira da organização possui variantes distintas desse status em alguns projetos
(`Enviado- Aguardando Análise`, `Enviado - Aguardando Análise1`), que **não** são contabilizadas
nessas consultas. Esse comportamento é o mesmo do artifact ao vivo e foi preservado no snapshot.
