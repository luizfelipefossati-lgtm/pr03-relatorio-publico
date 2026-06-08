# PR03 - Relatório de Indicadores de EPICs

Snapshot estático do dashboard PR.03 (Processo de Estudos e Projetos) da Engeplus, publicado automaticamente via Vercel.

## Última atualização

Gerado em **05/06/2026 15:48** (horário de Brasília).

Os dados são travados no momento da geração e **não** consultam o Jira em tempo real. Para visualizar a versão ao vivo, abra o artifact original em Cowork:
`pr03-relatorio-indicadores-epics`.

## Como funciona

- Uma tarefa agendada do Cowork (`deploy-pr03-vercel`) executa a cada 30 minutos:
  - Lê o artifact ao vivo (`%USERPROFILE%\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics\index.html`).
  - Pré-busca os dados do Jira via MCP (mês corrente + mês anterior + últimos 6 meses).
  - Gera um HTML estático com `window.__HISTORY__` e `window.__SNAPSHOT__`, sobrescrevendo `window.cowork.callMcpTool` para não fazer chamadas externas.
  - Salva em `index.html` (este diretório).
- Em seguida, uma tarefa do Windows Task Scheduler (`PR03-Auto-Push-GitHub`) detecta mudanças e faz `git commit + push` para o repositório.
- O Vercel detecta o push e publica a nova versão em ~1 min.

## Período coberto no snapshot

- **Visão mensal:** mês anterior (Maio 2026, encerrado) e mês corrente (Junho 2026).
- **Visão acumulada:** Janeiro a Junho 2026.

## Privacidade

Os dados publicados incluem nomes de Epics, números de issue, datas de vencimento, status e nomes de projetos. Aprovado pelo usuário para publicação.
