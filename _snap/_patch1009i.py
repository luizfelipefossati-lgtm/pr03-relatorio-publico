# -*- coding: utf-8 -*-
import io, os, sys
P = os.path.expanduser('~/mnt/pr03-relatorio-publico/README.md')
s = io.open(P, encoding='utf-8').read()
orig = s
def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:90])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 09/10/2026 16:30** (`2026-10-09T16:30:33-03:00`)',
    '> **Última atualização do snapshot: 09/10/2026 17:31** (`2026-10-09T17:31:00-03:00`)')

rep('Geração em 09/10/2026 16:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 09/10/2026 17:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

rep('''comparados por hash canônico do conjunto completo contra a geração anterior (09/10, 15:31).
**Todos os sete vieram idênticos** — quinta rodada consecutiva sem movimento no Jira, depois
das três mudanças registradas às 11:32 (`EG0239-28` concluído e `EG0240-4` reprogramado para
16/10).

| Conjunto | Registros | Situação vs. 09/10 15:31 |''',
'''comparados por hash canônico do conjunto completo contra a geração anterior (09/10, 16:30).
**Todos os sete vieram idênticos** — sexta rodada consecutiva sem movimento no Jira, depois
das três mudanças registradas às 11:32 (`EG0239-28` concluído e `EG0240-4` reprogramado para
16/10).

| Conjunto | Registros | Situação vs. 09/10 16:30 |''')

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-09T16:30:33-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-09T17:31:00-03:00`.')

rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 09/10/2026 16:30,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 09/10/2026 17:31,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
