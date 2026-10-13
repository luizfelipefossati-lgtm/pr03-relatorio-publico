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

rep('> **Última atualização do snapshot: 13/10/2026 15:30** (`2026-10-13T15:30:56-03:00`)',
    '> **Última atualização do snapshot: 13/10/2026 16:30** (`2026-10-13T16:30:09-03:00`)')

rep('Geração em 13/10/2026 15:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 13/10/2026 16:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

old_block = s[s.index('### Mudança de tipo de item no Jira'):s.index('A **visão acumulada**')]
new_block = '''### Nenhum conjunto alterado nesta rodada — e onde o predicado corrigido realmente mora

As sete chamadas dinâmicas foram reexecutadas ao vivo, já com o predicado corrigido
`issuetype in (Epic, "Fluxo de trabalho")`, e **reproduziram o cache de `_snap/` item a item** —
chave, resumo, status, categoria, due date, data de resolução e `updated`:

| Conjunto | Ao vivo | Cache em disco | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 13 | 13 | idêntico ao cache |
| `overdue_2026-10` | 1 | 1 | idêntico ao cache |
| `lookahead_2026-10` | 34 | 34 | idêntico ao cache |
| `sent_2026-10` | 4 | 4 | idêntico ao cache |
| `resolved_2026-10` | 4 | 4 | idêntico ao cache |
| `rework_2026-10` | 3 | 3 | idêntico ao cache |
| projetos visíveis | 21 | 21 | idêntico ao cache |

Os conjuntos `lookahead_2026-10` e a lista de projetos foram conferidos por `sha256` do JSON
canônico, e os cinco demais item a item. **Não houve movimento no Jira entre 15:30 e 16:30** —
é a sexta rodada consecutiva sem movimento real. Nenhum arquivo de `_snap/` nem o
`_projects_min.json` precisou ser regravado, e `index.html` e `snapshot-data.js` mantiveram o
mesmo tamanho em bytes (163.342 e 75.556), mudando apenas o carimbo de tempo. As posições do
`window.__SNAPSHOT__` (95.025) e do `window.__HISTORY__` do artifact (97.475) também não se
moveram, o que confirma que o HTML-fonte é byte a byte o mesmo fora dos carimbos.

**Correção da pendência registrada na rodada das 15:30.** Aquela nota concluía que o predicado
`issuetype=Epic` precisava ser trocado *no relatório*. A leitura do `_artifact_src.html` nesta
rodada mostra que **a página não tem esse predicado fixo**: em `LP()` ela varre os tipos de item
de todos os projetos visíveis, seleciona os de `hierarchyLevel === 1` e monta o predicado
dinamicamente em `ETQ` — hoje, `issuetype in ("Epic","Fluxo de trabalho")`. Ou seja, o relatório
publicado **já alcança** EG0285, EG0286, EG0294 e EG291; o truncamento observado às 15:30 foi um
artefato da consulta manual, não do dashboard. A verificação de padrões abaixo confirma: as 11
consultas que a página monta com o `ETQ` dinâmico casam com os 11 padrões gravados em
`snapshot-data.js`, sem sobra nem órfão.

> **Pendência remanescente (menor).** O texto `issuetype=Epic` continua gravado no prompt da
> tarefa agendada, no passo que descreve as seis consultas. Ele não afeta a página publicada,
> mas faz cada rodada partir de uma consulta truncada e precisar corrigi-la à mão. Trocar
> aquele trecho do prompt por `issuetype in (Epic, "Fluxo de trabalho")` elimina o retrabalho —
> e é uma alteração no prompt da tarefa, que esta rotina não faz por conta própria.

'''
s = s.replace(old_block, new_block, 1)

old_note = s[s.index('> **Nota de publicação (13/10/2026, 15:30).**'):s.index('Outubro segue com')]
new_note = '''> **Nota de publicação (13/10/2026, 16:30).** A cadeia de publicação segue íntegra. O
> `.push-watchdog.log` registra seis passagens desde a geração anterior — 15:34:34, 15:44:34,
> 15:54:34, 16:04:34, 16:14:34 e 16:24:34 — todas com `Commit OK` seguido de
> `Push OK e VERIFICADO` e `HEAD` sincronizado com `origin/main`; a última foi o commit
> `189d7e4`. A geração das 15:30 foi, portanto, publicada. Esta geração entra na próxima
> passagem da tarefa.

'''
s = s.replace(old_note, new_note, 1)

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T15:30:56-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T16:30:09-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 15:30,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 16:30,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
