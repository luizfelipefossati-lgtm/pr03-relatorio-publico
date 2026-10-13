# -*- coding: utf-8 -*-
import io, os, sys
P = os.path.expanduser('~/mnt/pr03-relatorio-publico/README.md')
s = io.open(P, encoding='utf-8').read()
orig = s
def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:160])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 13/10/2026 16:30** (`2026-10-13T16:30:09-03:00`)',
    '> **Última atualização do snapshot: 13/10/2026 17:31** (`2026-10-13T17:31:37-03:00`)')

rep('| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 34 | 34 |',
    '| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 | 34 |')

rep('Geração em 13/10/2026 16:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 13/10/2026 17:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

old_block = s[s.index('### Nenhum conjunto alterado nesta rodada'):s.index('A **visão acumulada**')]
new_block = '''### Movimento real no lookahead: `EG0256-30` reprogramado para 2027

Depois de seis rodadas sem movimento, o Jira mexeu. As sete chamadas dinâmicas foram
reexecutadas ao vivo com o predicado `issuetype in (Epic, "Fluxo de trabalho")`, e **um único
conjunto mudou**:

| Conjunto | Ao vivo | Cache em disco | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 13 | 13 | idêntico ao cache |
| `overdue_2026-10` | 1 | 1 | idêntico ao cache |
| `lookahead_2026-10` | **33** | 34 | **alterado — saiu `EG0256-30`** |
| `sent_2026-10` | 4 | 4 | idêntico ao cache |
| `resolved_2026-10` | 4 | 4 | idêntico ao cache |
| `rework_2026-10` | 3 | 3 | idêntico ao cache |
| projetos visíveis | 21 | 21 | idêntico ao cache |

O EPIC `EG0256-30` ("Diagnóstico Ambiental - Meio Antrópico", EG0256 - SOPS_RS - EIA RIMA)
teve o **due date movido de 19/12/2026 para 30/01/2027**, alteração registrada no Jira hoje
às **17:04:26 BRT** — ou seja, depois da geração das 16:30 e antes desta. Com isso ele sai da
janela de lookahead (nov–dez/2026), que cai de 34 para 33 registros. Os outros 32 registros do
conjunto reproduziram o cache campo a campo, e os outros cinco conjuntos do mês, mais a lista
de 21 projetos, foram conferidos por `sha256` do JSON canônico e por comparação item a item:
nada mais se moveu.

Só o `_snap/lookahead_2026-10.json` foi regravado (34 → 33 itens); `_projects_min.json` e os
demais arquivos de `_snap/` ficaram intactos. O `index.html` passou de 163.342 para
**163.034 bytes** e o `snapshot-data.js` de 75.556 para **75.248 bytes** — a diferença é
exatamente o registro removido. Os meses congelados **não** foram tocados: `EG0256-30` segue
presente nos lookaheads de ago/2026 e set/2026, como era no fechamento daqueles meses, e isso
foi conferido no `window.__SNAPSHOT__` gerado.

> **Pendência remanescente (menor).** O texto `issuetype=Epic` continua gravado no prompt da
> tarefa agendada, no passo que descreve as seis consultas. Ele não afeta a página publicada —
> o artifact monta o predicado dinamicamente a partir dos tipos de hierarquia 1 dos projetos
> visíveis —, mas faz cada rodada partir de uma consulta truncada e precisar corrigi-la à mão.
> Trocar aquele trecho do prompt por `issuetype in (Epic, "Fluxo de trabalho")` elimina o
> retrabalho — e é uma alteração no prompt da tarefa, que esta rotina não faz por conta própria.

'''
s = s.replace(old_block, new_block, 1)

old_note = s[s.index('> **Nota de publicação (13/10/2026, 16:30).**'):s.index('Outubro segue com')]
new_note = '''> **Nota de publicação (13/10/2026, 17:31).** A cadeia de publicação segue íntegra. O
> `.push-watchdog.log` registra seis passagens desde a geração anterior — 16:34:34, 16:44:34,
> 16:54:34, 17:04:34, 17:14:35 e 17:24:34 — todas com `Commit OK` seguido de
> `Push OK e VERIFICADO` e `HEAD` sincronizado com `origin/main`; a última foi o commit
> `0435d1c`. A geração das 16:30 foi, portanto, publicada. Esta geração entra na próxima
> passagem da tarefa.

'''
s = s.replace(old_note, new_note, 1)

rep('''Outubro segue com **um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e de novo
`Em Revisão` desde 13/10 às 09:51. O efeito da reprogramação dos dois EPICs do EG0256
(`EG0256-30` para 19/12/2026 e `EG0256-28` para 29/01/2027), registrada na rodada de 08/10
às 11:31, segue valendo.''',
'''Outubro segue com **um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e de novo
`Em Revisão` desde 13/10 às 09:51. Os dois EPICs do EG0256 reprogramados em 08/10 às 11:31
seguiram caminhos diferentes: `EG0256-28` continua em 29/01/2027, e `EG0256-30`, que fora
movido para 19/12/2026, foi **empurrado de novo hoje às 17:04 para 30/01/2027** — saindo do
lookahead desta geração.''')

rep('''34 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0256, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 23**, dos quais 21 têm due date entre 16 e 31/12.

A concentração de dezembro **mantém-se** no patamar alcançado na rodada de 08/10 às 11:31, com a chegada
do `EG0256-30` (19/12): dois terços do lookahead caem na segunda quinzena de dezembro.''',
'''33 epics, concentrados em **EG0274 = 11** e **EG0286 = 10**, seguidos de EG0285 = 4, EG0294 = 3 e
um cada em G0280, EG0275, EG0241, EG0240 e EG0239. Por mês: **nov/2026 = 11** e
**dez/2026 = 22**, dos quais 20 têm due date entre 16 e 31/12.

A concentração de dezembro **recua um ponto** com a saída do `EG0256-30`, reprogramado de
19/12/2026 para 30/01/2027 nesta rodada — o EG0256 deixa de ter representante no lookahead.
Ainda assim, 20 dos 33 registros (**61%**) caem na segunda quinzena de dezembro: o gargalo de
fim de ano permanece, concentrado em EG0274 e EG0286.''')

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T16:30:09-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T17:31:37-03:00`.')
rep('''  (`window.__SNAPSHOT__` na posição 95.025 do `index.html`, contra 97.475 do
  `window.__HISTORY__` do artifact — ordem de execução confirmada).''',
'''  (`window.__SNAPSHOT__` na posição 94.719 do `index.html`, contra 97.169 do
  `window.__HISTORY__` do artifact — ordem de execução confirmada).''')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 16:30,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 17:31,')
rep('  `planned` 13, `overdue` 1, `lookahead` 34, `sent` 4, `resolved` 4, `rework` 3.',
    '  `planned` 13, `overdue` 1, `lookahead` 33, `sent` 4, `resolved` 4, `rework` 3.')
rep('''- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudou apenas o carimbo de geração.''',
'''- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudaram apenas o carimbo de geração e um registro do
  `lookahead_2026-10`, dentro da estrutura de dados já existente.''')

rep('''  `updated`) e `pageInfo.hasNextPage = false` em todas. O `lookahead`, por ser o maior conjunto,
  foi pedido sem o campo `project` — que não muda para uma issue já existente — e coube inline;
  a comparação com o arquivo em disco foi feita por `key`, `summary`, `status.name`,
  `status.statusCategory.key`, `duedate`, `resolutiondate` e `updated`, mais a ordem, e o
  `project` de cada registro foi preservado do arquivo. Só a resposta do
  `getVisibleJiraProjects` excedeu o limite de tokens; foi reduzida à forma mínima sobre o
  arquivo salvo pelo runtime, conforme o procedimento previsto.''',
'''  `updated`) e `pageInfo.hasNextPage = false` em todas. Duas respostas excederam o limite de
  tokens — o `lookahead`, por ser o maior conjunto, e o `getVisibleJiraProjects` — e ambas foram
  reduzidas à forma mínima sobre o arquivo salvo pelo runtime, conforme o procedimento previsto.
  A comparação com o arquivo em disco foi feita por `key`, `summary`, `status.name`,
  `status.statusCategory.key`, `duedate`, `resolutiondate` e `updated`; o `project` de cada
  registro mantido foi preservado do arquivo.''')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
