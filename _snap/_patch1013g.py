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

rep('> **Última atualização do snapshot: 13/10/2026 14:33** (`2026-10-13T14:33:49-03:00`)',
    '> **Última atualização do snapshot: 13/10/2026 15:30** (`2026-10-13T15:30:56-03:00`)')

rep('Geração em 13/10/2026 14:33 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 13/10/2026 15:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

old_block = s[s.index('### Nenhum conjunto alterado nesta rodada'):s.index('A **visão acumulada**')]
new_block = '''### Mudança de tipo de item no Jira — JQL do relatório corrigida nesta rodada

Esta rodada começou com uma anomalia. As seis consultas do mês corrente, executadas com o
predicado histórico `issuetype=Epic`, vieram **truncadas**: `planned` caiu de 13 para 8 itens,
`lookahead` de 34 para 16, `sent` de 4 para 3, `resolved` de 4 para 3 e `rework` de 3 para 2.
Todos os itens ausentes pertenciam a quatro projetos — **EG0285, EG0286, EG0294 e EG291**.

A investigação descartou perda de dados e descartou perda de acesso:

- `getVisibleJiraProjects` continua retornando **21 projetos**, os quatro inclusive, todos
  navegáveis — ou seja, não houve mudança de permissão.
- `project = EG0286` retorna **37 itens** normalmente, e `EG0286-7` é recuperável pelo
  endpoint de issue com todos os campos íntegros.

A causa é outra: nesses quatro projetos o **tipo de item deixou de se chamar `Epic` e passou a
se chamar `Fluxo de trabalho`** (`issuetype` id 10737, `hierarchyLevel` 1). Os itens são os
mesmos, com os mesmos campos; apenas não casam mais com o predicado `issuetype=Epic`. O
relatório não perdeu dado nenhum — a consulta é que deixou de alcançá-lo.

Com o predicado corrigido para `issuetype in (Epic, "Fluxo de trabalho")`, os seis conjuntos
voltaram a reproduzir **exatamente** o cache em disco, item a item — chave, resumo, status,
categoria, due date, data de resolução e `updated`:

| Conjunto | Com `issuetype=Epic` | Com predicado corrigido | Cache em disco | Situação |
|---|---:|---:|---:|---|
| `planned_2026-10` | 8 | 13 | 13 | idêntico ao cache |
| `overdue_2026-10` | 1 | 1 | 1 | idêntico ao cache |
| `lookahead_2026-10` | 16 | 34 | 34 | idêntico ao cache |
| `sent_2026-10` | 3 | 4 | 4 | idêntico ao cache |
| `resolved_2026-10` | 3 | 4 | 4 | idêntico ao cache |
| `rework_2026-10` | 2 | 3 | 3 | idêntico ao cache |
| projetos visíveis | 21 | 21 | 21 | idêntico ao cache |

Portanto **não houve movimento no Jira entre 14:33 e 15:30** — é a quinta rodada consecutiva
sem movimento real. Nenhum arquivo de `_snap/` nem o `_projects_min.json` precisou ser
regravado, e `index.html` e `snapshot-data.js` mantiveram o mesmo tamanho em bytes (163.342 e
75.556), mudando apenas o carimbo de tempo. O snapshot publicado está **completo**: os 13
EPICs previstos de outubro, os quatro projetos inclusive, seguem na página.

A reabertura de `EG0240-5` (*TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)*, EG0240 - GOITÁ/
COMPESA), captada na rodada das 10:32, **permanece**: segue em `Em Revisão` sem
`resolutiondate`, com `updated = 2026-10-13T09:51:44.629-0300`.

> **Pendência para o responsável.** O predicado `issuetype=Epic` está gravado no prompt da
> tarefa agendada e continuará truncando os quatro projetos nas próximas rodadas. A troca por
> `issuetype in (Epic, "Fluxo de trabalho")` nas seis consultas precisa ser feita no prompt da
> tarefa — esta rodada aplicou a correção manualmente, mas ela não persiste sozinha. Enquanto
> não for aplicada, uma rodada que confie no resultado bruto publicaria um relatório sem
> EG0285, EG0286, EG0294 e EG291, inflando artificialmente o OTD.

'''
s = s.replace(old_block, new_block, 1)

old_note = s[s.index('> **Nota de publicação (13/10/2026, 14:33).**'):s.index('Outubro segue com')]
new_note = '''> **Nota de publicação (13/10/2026, 15:30).** A cadeia de publicação segue íntegra. O
> `.push-watchdog.log` registra seis passagens desde a geração anterior — 14:34:34, 14:44:34,
> 14:54:34, 15:04:38, 15:14:38 e 15:24:34 — todas com `Commit OK` seguido de
> `Push OK e VERIFICADO` e `HEAD` sincronizado com `origin/main`; a última foi o commit
> `625c1e1`. A geração das 14:33 foi, portanto, publicada. Esta geração entra na próxima
> passagem da tarefa.

'''
s = s.replace(old_note, new_note, 1)

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T14:33:49-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T15:30:56-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 14:33,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 15:30,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
