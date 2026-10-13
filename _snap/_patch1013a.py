# -*- coding: utf-8 -*-
import io, os, sys
P = os.path.expanduser('~/mnt/pr03-relatorio-publico/README.md')
s = io.open(P, encoding='utf-8').read()
orig = s
def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:120])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 10/10/2026 21:29** (`2026-10-10T21:29:49-03:00`)',
    '> **Última atualização do snapshot: 13/10/2026 09:31** (`2026-10-13T09:31:21-03:00`)')

rep('Geração em 10/10/2026 21:29 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 13/10/2026 09:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

rep('''comparados por hash canônico contra a versão anterior dos mesmos arquivos (geração de 10/10,
20:32, já versionada). **Todos os sete vieram idênticos** — décima segunda rodada consecutiva
sem movimento no Jira, depois das três mudanças registradas em 09/10 às 11:32 (`EG0239-28`
concluído e `EG0240-4` reprogramado para 16/10).

| Conjunto | Registros | Situação vs. 10/10 20:32 |''',
'''comparados item a item contra a versão anterior dos mesmos arquivos (geração de 10/10,
21:29, ainda **não** publicada — ver nota de publicação abaixo). **Todos os sete vieram
idênticos** — décima terceira rodada consecutiva sem movimento no Jira, depois das três
mudanças registradas em 09/10 às 11:32 (`EG0239-28` concluído e `EG0240-4` reprogramado
para 16/10). Esta rodada cobre uma lacuna de agendamento: a geração anterior foi em 10/10
às 21:29, quase três dias atrás.

| Conjunto | Registros | Situação vs. 10/10 21:29 |''')

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-10T21:29:49-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T09:31:21-03:00`.')

rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 10/10/2026 21:29,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 09:31,')

# nota nova sobre a cadeia de publicacao parada
rep('''Como a coleta desta rodada reproduziu exatamente os arquivos em disco, nenhum arquivo de
`_snap/` nem o `_projects_min.json` precisou ser regravado.''',
'''> **Nota de publicação (13/10/2026).** O `PR03-Auto-Push-GitHub` parou em 10/10 às 23:57: a
> última linha de `.push-watchdog.log` é `Empurrando para origin/main...` sem confirmação, e o
> commit `ed2f177` segue **1 commit à frente** de `origin/main` (`6e7a43e`). O site publicado
> portanto ainda serve a geração de 10/10 às 22:24. Enquanto a tarefa do Windows Task Scheduler
> não voltar a rodar com sucesso, este `index.html` fica apenas no working tree local.

Como a coleta desta rodada reproduziu exatamente os arquivos em disco, nenhum arquivo de
`_snap/` nem o `_projects_min.json` precisou ser regravado.''')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
