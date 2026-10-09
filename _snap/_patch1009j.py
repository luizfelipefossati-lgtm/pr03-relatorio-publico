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

rep('> **Última atualização do snapshot: 09/10/2026 18:31** (`2026-10-09T18:31:44-03:00`)',
    '> **Última atualização do snapshot: 09/10/2026 19:30** (`2026-10-09T19:30:36-03:00`)')

rep('Geração em 09/10/2026 18:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 09/10/2026 19:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

rep('''(geração de 09/10, 17:31, já versionada). **Todos os sete vieram idênticos** — sétima rodada
consecutiva sem movimento no Jira, depois das três mudanças registradas às 11:32 (`EG0239-28`
concluído e `EG0240-4` reprogramado para 16/10).

| Conjunto | Registros | Situação vs. 09/10 17:31 |''',
'''(geração de 09/10, 18:31, já versionada). **Todos os sete vieram idênticos** — oitava rodada
consecutiva sem movimento no Jira, depois das três mudanças registradas às 11:32 (`EG0239-28`
concluído e `EG0240-4` reprogramado para 16/10).

| Conjunto | Registros | Situação vs. 09/10 18:31 |''')

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-09T18:31:44-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-09T19:30:36-03:00`.')

rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 09/10/2026 18:31,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 09/10/2026 19:30,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
