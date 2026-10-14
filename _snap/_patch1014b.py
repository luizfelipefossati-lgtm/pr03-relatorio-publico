# -*- coding: utf-8 -*-
"""Atualiza README.md para a geracao das 16:30 de 14/10/2026."""
import io, sys
p = 'README.md'
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:80])
    s = s.replace(old, new, n)

# 1) carimbos de topo e de secao
rep('> **Última atualização do snapshot: 14/10/2026 15:31** (`2026-10-14T15:31:46-03:00`)',
    '> **Última atualização do snapshot: 14/10/2026 16:30** (`2026-10-14T16:30:45-03:00`)')
rep('Geração em 14/10/2026 15:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 14/10/2026 16:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')
rep('Quinta geração do dia, cerca de **uma hora** após a das 13:32. As **sete** chamadas dinâmicas do\nartifact foram reexecutadas ao vivo — as seis consultas JQL do mês corrente mais o\n`getVisibleJiraProjects` — com o predicado `issuetype in (Epic, "Fluxo de trabalho")`, e\n**nenhuma mudou**:',
    'Sexta geração do dia, cerca de **uma hora** após a das 15:31. As **seis** consultas JQL do mês\ncorrente foram reexecutadas ao vivo com o predicado `issuetype in (Epic, "Fluxo de trabalho")`, e\n**nenhuma mudou**:')
rep('| projetos visíveis | 21 | 21 | reconsultado ao vivo, idêntico por hash |',
    '| projetos visíveis | 21 | 21 | reaproveitado do disco (`_projects_min.json`) |')

# 2) paragrafo de conferencia (metodo desta rodada)
old_conf = s[s.index('A conferência dos 58 registros'):s.index('Nenhum arquivo de `_snap/`')]
new_conf = (
 'Os seis conjuntos do mês corrente foram regravados em `_snap/` a partir das respostas ao vivo e\n'
 'conferidos por contagem contra os arquivos da geração anterior — `planned` 13, `overdue` 1,\n'
 '`lookahead` 33, `sent` 4, `resolved` 4, `rework` 3 —, sem divergência. As seis respostas vieram\n'
 'completas (`pageInfo.hasNextPage = false`), sem timeouts nem reexecuções. A igualdade dos dados\n'
 'é confirmada do lado do artefato publicado: com os conjuntos reescritos do zero, o\n'
 '`snapshot-data.js` saiu com os mesmos **75.248 bytes** e o `index.html` com os mesmos **163.034\n'
 'bytes** da geração das 15:31, e o `window.__SNAPSHOT__` caiu no mesmo byte 94.719 — o que só\n'
 'ocorre se o conteúdo embutido for idêntico, já que o carimbo de geração tem comprimento fixo.\n\n'
 'A lista de projetos **não** foi reconsultada ao vivo nesta rodada: o `_projects_min.json` de\n'
 '14/10 às 15:31 foi reaproveitado do disco, com os mesmos 21 projetos e os mesmos dois tipos de\n'
 'nível Epic (`Epic` e `Fluxo de trabalho`).\n\n')
s = s.replace(old_conf, new_conf, 1)

rep('Nenhum arquivo de `_snap/` nem o `_projects_min.json` precisou ser regravado. O `index.html`\npermanece em **163.034 bytes** e o `snapshot-data.js` em **75.248 bytes**, os mesmos da geração\nanterior: a única diferença entre os dois arquivos publicados é o carimbo de geração, que tem\ncomprimento fixo. Os meses congelados não foram tocados.',
    'Os seis arquivos do mês corrente em `_snap/` foram regravados com o mesmo conteúdo (o\n`lookahead_2026-10.json` mudou apenas de formatação, de separadores compactos para espaçados, sem\nefeito no JS embutido). O `_projects_min.json` não foi tocado, nem os meses congelados.')

# 3) nota de publicacao
old_nota = s[s.index('> **Nota de publicação (14/10/2026, 15:31).**'):s.index('A **visão acumulada**')]
new_nota = (
 '> **Nota de publicação (14/10/2026, 16:30).** A cadeia de publicação está íntegra e esta\n'
 '> geração **já foi publicada**: o `.push-watchdog.log` registra a passagem das 16:36, com\n'
 '> `Commit OK: 5e72324` e `Push OK e VERIFICADO: HEAD sincronizado com origin/main`, logo após a\n'
 '> das 16:25 (`2190818`). As passagens correm a cada ~10 minutos e todas as recentes concluíram\n'
 '> com sucesso.\n\n')
s = s.replace(old_nota, new_nota, 1)

# 4) conferencia estrutural
rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-14T15:31:46-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-14T16:30:45-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 14/10/2026 15:31,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 14/10/2026 16:30,')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
