# -*- coding: utf-8 -*-
import io, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'README.md')
s = io.open(P, encoding='utf-8').read()
orig = s
def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:90])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 09/10/2026 11:32** (`2026-10-09T11:32:36-03:00`)',
    '> **Última atualização do snapshot: 09/10/2026 12:30** (`2026-10-09T12:30:29-03:00`)')

rep('''| `planned_2026-10` | Epics com due date em out/2026 | 13 | 12 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 0 | 2 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 34 | 34 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 4 | 4 |
| `resolved_2026-10` | Concluídos em out/2026 | 5 | 4 |
| `rework_2026-10` | Retrabalho em out/2026 | 3 | 3 |''',
'''| `planned_2026-10` | Epics com due date em out/2026 | 13 | 13 |
| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 0 | 0 |
| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 34 | 34 |
| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 4 | 4 |
| `resolved_2026-10` | Concluídos em out/2026 | 5 | 5 |
| `rework_2026-10` | Retrabalho em out/2026 | 3 | 3 |''')

rep('Geração em 09/10/2026 11:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 09/10/2026 12:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

# ---- substitui a secao "Tres conjuntos alterados" pela desta rodada ----
i = s.index('### Três conjuntos alterados nesta rodada')
j = s.index('### Demais conferências')
s = s[:i] + '''### Nenhum conjunto alterado nesta rodada

As seis consultas do mês corrente e o `getVisibleJiraProjects` foram reexecutados ao vivo e
comparados por hash canônico contra a geração anterior (09/10, 11:32). **Todos os sete vieram
idênticos** — o Jira não registrou movimento no intervalo, depois das três mudanças da rodada
anterior (`EG0239-28` concluído e `EG0240-4` reprogramado para 16/10).

| Conjunto | Registros | Situação vs. 09/10 11:32 |
|---|---:|---|
| `planned_2026-10` | 13 | idêntico |
| `overdue_2026-10` | 0 | idêntico (lista vazia) |
| `lookahead_2026-10` | 34 | idêntico |
| `sent_2026-10` | 4 | idêntico |
| `resolved_2026-10` | 5 | idêntico |
| `rework_2026-10` | 3 | idêntico |
| projetos visíveis | 21 | idêntico |

Os arquivos de `_snap/` e o `_projects_min.json` não precisaram ser regravados. Entre a geração
anterior e esta, mudou apenas o carimbo de tempo do `index.html` e deste `README.md`.

Outubro segue **sem nenhum EPIC em atraso acumulado** — `overdue_2026-10` continua vazio desde a
rodada das 11:32. O efeito da reprogramação dos dois EPICs do EG0256 (`EG0256-30` para 19/12/2026
e `EG0256-28` para 29/01/2027), registrada na rodada de 08/10 às 11:31, segue valendo.

''' + s[j:]

# ---- quadro de outubro ----
rep('''12 epics com due date em outubro — 11 em andamento/revisão (9 "Em andamento" + 2 "Em Revisão")
e 1 já enviado dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0274 = 2 · EG291 = 1.

Indicadores do mês na geração: **OTD 8%** (1 de 12), **retrabalho 75%** (3 de 4 envios),
**11 pendências do mês** e **2 em atraso acumulado**.

O OTD segue em 8%, estável desde a geração das 11:31: o único envio com due date de outubro
continua sendo `EG0286-7`, e o denominador permanece em 12 após a saída dos dois EPICs do EG0256.
O retrabalho fica em 75%, sem alteração nos envios.''',
'''13 epics com due date em outubro — 12 em andamento/revisão (9 "Em andamento" + 3 "Em Revisão")
e 1 já enviado dentro do próprio mês. Nenhum em "Tarefas pendentes".
Distribuição por projeto: G0280 = 5 · EG0286 = 4 · EG0274 = 2 · EG0240 = 1 · EG291 = 1.

Indicadores do mês na geração: **OTD 8%** (1 de 13), **retrabalho 75%** (3 de 4 envios),
**12 pendências do mês** e **nenhum em atraso acumulado**.

O OTD permanece em 8%: o único envio com due date de outubro continua sendo `EG0286-7`, e o
denominador subiu para 13 com a entrada de `EG0240-4`, reprogramado para 16/10. O retrabalho
fica em 75%, sem alteração nos envios.''')

rep('''**2 EPICs em atraso acumulado** permanecem em outubro, sem alteração:

| EPIC | Projeto | Due date | Status |
|---|---|---|---|
| `EG0239-28` | EG0239 | 2026-08-10 | Em Revisão |
| `EG0240-4` | EG0240 | 2026-09-10 | Em Revisão |''',
'''**Nenhum EPIC em atraso acumulado** em outubro: `overdue_2026-10` é uma lista vazia. Os dois que
constavam até a rodada das 09:32 saíram do conjunto — `EG0239-28` foi concluído em 09/10 às 09:36
e `EG0240-4` teve a due date reprogramada de 10/09 para 16/10, passando a contar como previsto do
próprio mês.''')

rep('A concentração de dezembro **mantém-se** no patamar alcançado na rodada das 11:31, com a chegada',
    'A concentração de dezembro **mantém-se** no patamar alcançado na rodada de 08/10 às 11:31, com a chegada')

# ---- conferencia estrutural ----
rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-09T11:32:36-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-09T12:30:29-03:00`.')
rep('  (posição 95.138 do arquivo, contra 97.581 do `window.__HISTORY__` do artifact).',
    '  (posição 95.131 do arquivo, contra 97.581 do `window.__HISTORY__` do artifact).')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 09/10/2026 11:32,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 09/10/2026 12:30,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
