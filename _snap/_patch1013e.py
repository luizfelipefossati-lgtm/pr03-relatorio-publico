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

rep('> **Última atualização do snapshot: 13/10/2026 12:29** (`2026-10-13T12:29:50-03:00`)',
    '> **Última atualização do snapshot: 13/10/2026 13:31** (`2026-10-13T13:31:49-03:00`)')

rep('Geração em 13/10/2026 12:29 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 13/10/2026 13:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

old_block = s[s.index('### Nenhum conjunto alterado nesta rodada'):s.index('A **visão acumulada**')]
new_block = '''### Nenhum conjunto alterado nesta rodada

As seis consultas do mês corrente e o `getVisibleJiraProjects` foram reexecutados ao vivo e
comparados item a item — chave, resumo, status, categoria, due date, data de resolução e
`updated`, na ordem em que o Jira devolve — contra a versão anterior dos mesmos arquivos
(geração de 13/10, 12:29). Os sete conjuntos vieram **idênticos**: o Jira não registrou
movimento entre 12:29 e 13:31. É a terceira rodada consecutiva sem movimento — o último evento
captado continua sendo a reabertura de `EG0240-5`, das 09:51.

Essa reabertura (`EG0240-5`, *TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)*, EG0240 - GOITÁ/ COMPESA),
captada na rodada das 10:32, **permanece**: o EPIC segue em `Em Revisão` sem `resolutiondate`,
com `updated = 2026-10-13T09:51:44.629-0300`, e continua sendo o único EPIC em atraso acumulado
de outubro.

| Conjunto | Registros | Situação vs. 13/10 12:29 |
|---|---:|---|
| `planned_2026-10` | 13 | idêntico |
| `overdue_2026-10` | 1 | idêntico |
| `lookahead_2026-10` | 34 | idêntico |
| `sent_2026-10` | 4 | idêntico |
| `resolved_2026-10` | 4 | idêntico |
| `rework_2026-10` | 3 | idêntico |
| projetos visíveis | 21 | idêntico (hash `cc7b94d5a1583c3c97cfc229`) |

Como a coleta desta rodada reproduziu exatamente os arquivos em disco, nenhum arquivo de
`_snap/` nem o `_projects_min.json` precisou ser regravado. Entre a geração anterior e esta,
mudou apenas o carimbo de tempo do `index.html`, do `snapshot-data.js` e deste `README.md` —
os dois primeiros, inclusive, mantiveram o mesmo tamanho em bytes (163.342 e 75.556).

'''
s = s.replace(old_block, new_block, 1)

old_note = s[s.index('> **Nota de publicação (13/10/2026, 12:29).**'):s.index('Outubro segue com')]
new_note = '''> **Nota de publicação (13/10/2026, 13:31).** A cadeia de publicação segue íntegra. O
> `.push-watchdog.log` registra seis passagens desde a geração anterior — 12:34:34, 12:44:33,
> 12:54:34, 13:04:33, 13:14:33 e 13:24:33 — todas com `Commit OK` seguido de
> `Push OK e VERIFICADO` e `HEAD` sincronizado com `origin/main`; a última foi o commit
> `2ae8809`. A geração das 12:29 foi, portanto, publicada. Esta geração entra na próxima
> passagem da tarefa.

'''
s = s.replace(old_note, new_note, 1)

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T12:29:50-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T13:31:49-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 12:29,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 13:31,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
