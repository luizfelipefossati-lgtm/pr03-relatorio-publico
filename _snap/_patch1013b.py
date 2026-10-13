# -*- coding: utf-8 -*-
import io, os, sys
P = os.path.expanduser('~/mnt/pr03-relatorio-publico/README.md')
s = io.open(P, encoding='utf-8').read()
orig = s
def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:140])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 13/10/2026 09:31** (`2026-10-13T09:31:21-03:00`)',
    '> **Última atualização do snapshot: 13/10/2026 10:32** (`2026-10-13T10:32:27-03:00`)')

rep('| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 0 | 0 |',
    '| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | **1** | 0 |')
rep('| `resolved_2026-10` | Concluídos em out/2026 | 5 | 5 |',
    '| `resolved_2026-10` | Concluídos em out/2026 | **4** | 5 |')

rep('Geração em 13/10/2026 09:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 13/10/2026 10:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

# ---- bloco de conferencia da rodada ----
old_block = s[s.index('### Nenhum conjunto alterado nesta rodada'):s.index('A **visão acumulada**')]
new_block = '''### Quatro conjuntos alterados: `EG0240-5` foi reaberto

As seis consultas do mês corrente e o `getVisibleJiraProjects` foram reexecutados ao vivo e
comparados item a item contra a versão anterior dos mesmos arquivos (geração de 13/10, 09:31).
Depois de treze rodadas consecutivas sem movimento, **o Jira mudou**: o EPIC `EG0240-5`
(*TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)*, EG0240 - GOITÁ/ COMPESA) **saiu de
`Enviado - Aguardando Análise` e voltou para `Em Revisão`** em 13/10 às 09:51 BRT
(`updated = 2026-10-13T09:51:44.629-0300`), perdendo a `resolutiondate` que tinha desde
07/10 às 16:01.

Como a due date dele é 30/09, a reabertura **reintroduz o primeiro EPIC em atraso acumulado de
outubro**, depois de o conjunto ter ficado vazio desde a rodada de 09/10 às 11:32.

| Conjunto | Registros | Situação vs. 13/10 09:31 |
|---|---:|---|
| `planned_2026-10` | 13 | idêntico |
| `overdue_2026-10` | 1 | **alterado** — entra `EG0240-5` (lista estava vazia) |
| `lookahead_2026-10` | 34 | idêntico |
| `sent_2026-10` | 4 | **alterado** — mesmos quatro keys; `EG0240-5` com novo status e sem `resolutiondate` |
| `resolved_2026-10` | 4 | **alterado** — sai `EG0240-5` (era 5) |
| `rework_2026-10` | 3 | **alterado** — mesmos três keys; `EG0240-5` com novo status |
| projetos visíveis | 21 | idêntico |

Os quatro arquivos alterados foram regravados em `_snap/`; `planned_2026-10`,
`lookahead_2026-10` e `_projects_min.json` vieram idênticos e não foram tocados.

'''
s = s.replace(old_block, new_block, 1)

# ---- nota de publicacao: cadeia restabelecida ----
old_note = s[s.index('> **Nota de publicação (13/10/2026).**'):s.index('Como a coleta desta rodada reproduziu')]
new_note = '''> **Nota de publicação (13/10/2026, 10:32).** A parada do `PR03-Auto-Push-GitHub` registrada
> na geração anterior **foi superada**. O `.push-watchdog.log` mostra commits e pushes
> verificados de dez em dez minutos ao longo de toda a manhã de 13/10 — o último às 10:24:35,
> com `Push OK e VERIFICADO`. `HEAD` e `origin/main` apontam ambos para `173e253`, sem commits
> locais pendentes. Esta geração deve ser publicada na próxima passagem da tarefa.

'''
s = s.replace(old_note, new_note, 1)

rep('''Como a coleta desta rodada reproduziu exatamente os arquivos em disco, nenhum arquivo de
`_snap/` nem o `_projects_min.json` precisou ser regravado. Entre a geração anterior e esta,
mudou apenas o carimbo de tempo do `index.html`, do `snapshot-data.js` e deste `README.md`.

Outubro segue **sem nenhum EPIC em atraso acumulado** — `overdue_2026-10` continua vazio desde a
rodada de 09/10 às 11:32. O efeito da reprogramação dos dois EPICs do EG0256 (`EG0256-30` para
19/12/2026 e `EG0256-28` para 29/01/2027), registrada na rodada de 08/10 às 11:31, segue valendo.''',
'''Outubro **volta a ter um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e de novo
`Em Revisão`. O efeito da reprogramação dos dois EPICs do EG0256 (`EG0256-30` para
19/12/2026 e `EG0256-28` para 29/01/2027), registrada na rodada de 08/10 às 11:31, segue valendo.''')

# ---- quadro de outubro ----
rep('Indicadores do mês na geração: **OTD 8%** (1 de 13), **retrabalho 60%** (3 de 5 envios),\n**12 pendências do mês** e **nenhum em atraso acumulado**.',
    'Indicadores do mês na geração: **OTD 8%** (1 de 13), **retrabalho 60%** (3 de 5 envios),\n**12 pendências do mês** e **1 em atraso acumulado**.')

rep('''O OTD permanece em 8%: o único envio com due date de outubro continua sendo `EG0286-7`, e o
denominador segue em 13 desde a entrada de `EG0240-4`, reprogramado para 16/10. O retrabalho
fica em 60%, sem alteração nos envios.''',
'''O OTD permanece em 8%: o único envio com due date de outubro continua sendo `EG0286-7`, e o
denominador segue em 13 desde a entrada de `EG0240-4`, reprogramado para 16/10. O retrabalho
também fica em 60%: a reabertura de `EG0240-5` tirou o EPIC de `resolved`, mas ele continua em
`sent` (a transição de 07/10 está no histórico e o `DURING` a enxerga), de modo que a união
`sent` + `resolved` segue com cinco registros e três de retrabalho.''')

rep('| `EG0240-5` | EG0240 | 2026-09-30 | 07/10 16:01 | sim |',
    '| `EG0240-5` | EG0240 | 2026-09-30 | 07/10 16:01 | sim — **reaberto em 13/10 09:51** |')

rep('''**Nenhum EPIC em atraso acumulado** em outubro: `overdue_2026-10` é uma lista vazia. Os dois que
constavam até a rodada de 09/10 às 09:32 saíram do conjunto — `EG0239-28` foi concluído em
09/10 às 09:36
e `EG0240-4` teve a due date reprogramada de 10/09 para 16/10, passando a contar como previsto do
próprio mês.''',
'''**Um EPIC em atraso acumulado** em outubro, pela primeira vez desde 09/10: `EG0240-5`, due date
30/09, de volta a `Em Revisão`. O conjunto estava vazio porque os dois que constavam até a
rodada de 09/10 às 09:32 havíam saído — `EG0239-28` concluído em 09/10 às 09:36 e `EG0240-4`
reprogramado de 10/09 para 16/10. `EG0240-5` entra agora pelo caminho inverso: não por due date
nova, mas por ter perdido a conclusão que já tinha.''')

# ---- conferencia estrutural ----
rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T09:31:21-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T10:32:27-03:00`.')
rep('''  (`window.__SNAPSHOT__` na posição 95.138 do `index.html`, contra 97.581 do
  `window.__HISTORY__` do artifact — ordem de execução confirmada).''',
'''  (`window.__SNAPSHOT__` na posição 95.025 do `index.html`, contra 97.475 do
  `window.__HISTORY__` do artifact — ordem de execução confirmada).''')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 09:31,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 10:32,')
rep('  `planned` 13, `overdue` 0 (lista vazia), `lookahead` 34, `sent` 4, `resolved` 5, `rework` 3.',
    '  `planned` 13, `overdue` 1, `lookahead` 34, `sent` 4, `resolved` 4, `rework` 3.')

rep('''Scheduler, a cada 30 minutos, e o deploy no Vercel segue o push.''',
'''Scheduler — que, pelo `.push-watchdog.log`, vem rodando a cada **10 minutos** — e o deploy no
Vercel segue o push.''')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
