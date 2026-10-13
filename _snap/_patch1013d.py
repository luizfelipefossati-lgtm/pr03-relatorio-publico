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

rep('> **Última atualização do snapshot: 13/10/2026 11:30** (`2026-10-13T11:30:41-03:00`)',
    '> **Última atualização do snapshot: 13/10/2026 12:29** (`2026-10-13T12:29:50-03:00`)')

rep('Geração em 13/10/2026 11:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 13/10/2026 12:29 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

# ---- bloco de conferencia da rodada ----
old_block = s[s.index('### Nenhum conjunto alterado nesta rodada'):s.index('A **visão acumulada**')]
new_block = '''### Nenhum conjunto alterado nesta rodada

As seis consultas do mês corrente e o `getVisibleJiraProjects` foram reexecutados ao vivo e
comparados item a item contra a versão anterior dos mesmos arquivos (geração de 13/10, 11:30).
Os sete conjuntos vieram **idênticos**, inclusive na ordem dos registros: o Jira não registrou
movimento entre 11:30 e 12:29. É a segunda rodada consecutiva sem movimento — o último evento
captado continua sendo a reabertura de `EG0240-5`, das 09:51.

Essa reabertura (`EG0240-5`, *TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)*, EG0240 - GOITÁ/ COMPESA),
captada na rodada das 10:32, **permanece**: o EPIC segue em `Em Revisão` sem `resolutiondate`,
com `updated = 2026-10-13T09:51:44.629-0300`, e continua sendo o único EPIC em atraso acumulado
de outubro.

| Conjunto | Registros | Situação vs. 13/10 11:30 |
|---|---:|---|
| `planned_2026-10` | 13 | idêntico |
| `overdue_2026-10` | 1 | idêntico |
| `lookahead_2026-10` | 34 | idêntico |
| `sent_2026-10` | 4 | idêntico |
| `resolved_2026-10` | 4 | idêntico |
| `rework_2026-10` | 3 | idêntico |
| projetos visíveis | 21 | idêntico |

Como a coleta desta rodada reproduziu exatamente os arquivos em disco, nenhum arquivo de
`_snap/` nem o `_projects_min.json` precisou ser regravado. Entre a geração anterior e esta,
mudou apenas o carimbo de tempo do `index.html`, do `snapshot-data.js` e deste `README.md` —
os dois primeiros, inclusive, mantiveram o mesmo tamanho em bytes (163.342 e 75.556).

'''
s = s.replace(old_block, new_block, 1)

# ---- nota de publicacao ----
old_note = s[s.index('> **Nota de publicação (13/10/2026, 11:30).**'):s.index('Outubro segue com')]
new_note = '''> **Nota de publicação (13/10/2026, 12:29).** A cadeia de publicação segue íntegra. O
> `.push-watchdog.log` registra três passagens desde a geração anterior — 12:04:34, 12:14:34 e
> 12:24:34 — todas com `Commit OK` seguido de `Push OK e VERIFICADO` e `HEAD` sincronizado com
> `origin/main`; a última foi o commit `3196def`. A geração das 11:30 foi, portanto, publicada.
> Esta geração entra na próxima passagem da tarefa.

'''
s = s.replace(old_note, new_note, 1)

# ---- conferencia estrutural ----
rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T11:30:41-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T12:29:50-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 11:30,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 12:29,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
