# PR.03 — Relatório de Indicadores de EPICs

Snapshot estático publicado do dashboard **Pr03 Relatorio Indicadores Epics** (Engeplus Engenharia — Estudos e Projetos).

- **Última atualização:** 24/08/2026 09:11 (America/Sao_Paulo)
- **Timestamp ISO:** `2026-08-24T09:11:04-03:00`
- **Fonte:** Jira Cloud `projetos-engeplus` (cloudId `ead785de-33f3-4746-9bdb-a2a58cf5213b`)
- **Tipos de issue tratados como EPIC:** Epic, Fluxo de trabalho
- **Projetos visíveis:** 19

## O que é isto

Cópia estática (dados congelados) do Live Artifact. A página **não** consulta o Jira ao vivo:
um bloco `<script>` injetado em `index.html` define `window.__SNAPSHOT__` e substitui
`window.cowork.callMcpTool`, devolvendo os dados pré-buscados conforme o padrão da consulta JQL.
Consultas fora do período congelado retornam vazio e registram aviso no console — nunca vão à rede.

## Dados congelados neste snapshot

| Mês | Previstos | Atrasados (acum.) | Lookahead | Enviados | Retrabalho | Origem |
|---|---|---|---|---|---|---|
| Março/2026 | 7 | — | — | — | — | snapshot desta execução |
| Abril/2026 | 19 | 1 | 36 | 20 | 18 | congelado no artifact |
| Maio/2026 | 15 | 6 | 18 | 3 | 1 | congelado no artifact |
| Junho/2026 | 2 | 2 | — | 7 | 0 | congelado no artifact |
| Julho/2026 | 10 | 1 | 27 | 11 | 5 | snapshot desta execução |
| Agosto/2026 | 14 | 2 | 29 | 4 | 2 | snapshot desta execução |

- **Julho e Agosto/2026** (abas mensais) têm o conjunto completo de indicadores: `planned`,
  `overdue`, `lookahead`, `sent`, `resolved` e `rework`.
- **Março/2026** tem apenas a série `planned`, usada pela **Visão Acumulada** (padrão: últimos 6 meses).
- **Abril a Junho/2026** são períodos encerrados cujos dados já vêm congelados no próprio artifact
  (`window.__HISTORY__`); esta execução **não** os sobrescreve, preservando o fechamento original.

## Observações sobre os dados (Jira)

- Existem **variantes do nome do status "enviado"** entre projetos — `Enviado - Aguardando Análise`,
  `Enviado - Aguardando Análise1` e `Enviado- Aguardando Análise` (sem espaço antes do hífen).
  As consultas de `sent`/`rework` filtram pelo nome exato e por isso **subcontam**: em agosto,
  `sent` retorna 2 registros contra 4 em `resolved`. A padronização dos nomes de status no Jira
  eliminaria a divergência.
- O status de `EG0275-6` está gravado como `Em Revisã` (truncado no próprio Jira).
- O projeto DMAE usa a chave `G0280` embora o nome exibido seja `EG0280 - DMAE`.

## Estrutura

- `index.html` — dashboard completo e autocontido (cópia do artifact + injeção do snapshot)
- `vercel.json` — configuração de deploy
- `snapshot-data.js` — **legado**, não é mais referenciado pelo `index.html` (dados agora inline)

## Atualização

1. A tarefa agendada `deploy-pr03-vercel` regenera `index.html` e este `README.md`.
2. A tarefa do Windows Task Scheduler `PR03-Auto-Push-GitHub` (a cada 30 min) faz `git add/commit/push`.
3. O Vercel publica automaticamente ~1 min após o push.

## Privacidade

Os dados publicados contêm chaves e resumos de EPICs, nomes de projeto, datas e status.
Verificado nesta geração: **não** contêm `accountId`, `emailAddress`, `avatarUrls`, URLs de
gravatar, `iconUrl` nem descrições de issues.
