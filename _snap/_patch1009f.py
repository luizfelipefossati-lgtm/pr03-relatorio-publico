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

rep('> **Última atualização do snapshot: 09/10/2026 13:30** (`2026-10-09T13:30:20-03:00`)',
    '> **Última atualização do snapshot: 09/10/2026 14:30** (`2026-10-09T14:30:50-03:00`)')

rep('Geração em 09/10/2026 13:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 09/10/2026 14:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

rep('''As seis consultas do mês corrente e o `getVisibleJiraProjects` foram reexecutados ao vivo e
comparados por assinatura canônica (`key` + `updated` + `duedate` + `status`) contra a geração
anterior (09/10, 12:30). **Todos os sete vieram idênticos** — segunda rodada consecutiva sem
movimento no Jira, depois das três mudanças registradas às 11:32 (`EG0239-28` concluído e
`EG0240-4` reprogramado para 16/10).

| Conjunto | Registros | Situação vs. 09/10 12:30 |''',
'''As seis consultas do mês corrente e o `getVisibleJiraProjects` foram reexecutados ao vivo e
comparados por hash canônico do conjunto completo contra a geração anterior (09/10, 13:30).
**Todos os sete vieram idênticos** — terceira rodada consecutiva sem movimento no Jira, depois
das três mudanças registradas às 11:32 (`EG0239-28` concluído e `EG0240-4` reprogramado para
16/10).

| Conjunto | Registros | Situação vs. 09/10 13:30 |''')

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-09T13:30:20-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-09T14:30:50-03:00`.')
rep('''  (posição 95.138 do arquivo, contra 97.572 do `window.__HISTORY__` do artifact).''',
    '''  (`window.__SNAPSHOT__` na posição 95.131 do `index.html`, contra 95.257 do
  `window.__HISTORY__` do artifact — ordem de execução confirmada).''')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 09/10/2026 13:30,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 09/10/2026 14:30,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
