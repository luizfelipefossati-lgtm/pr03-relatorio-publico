# -*- coding: utf-8 -*-
"""Atualiza README.md para a geracao das 20:31 de 14/10/2026."""
import io, sys
p = 'README.md'
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:90])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 14/10/2026 20:25** (`2026-10-14T20:25:14-03:00`)',
    '> **Última atualização do snapshot: 14/10/2026 20:31** (`2026-10-14T20:31:52-03:00`)')
rep('Geração em 14/10/2026 20:25 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 14/10/2026 20:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')
rep('Oitava geração do dia, cerca de **uma hora** após a das 17:31. As **seis** consultas JQL do mês\n'
    'corrente foram reexecutadas ao vivo com o predicado `issuetype in (Epic, "Fluxo de trabalho")`, e\n'
    '**nenhuma mudou**:',
    'Nona geração do dia, **seis minutos** após a das 20:25 — o agendador disparou duas rodadas em\n'
    'sequência, e não com o intervalo habitual de uma hora. As **seis** consultas JQL do mês corrente\n'
    'foram reexecutadas ao vivo com o predicado `issuetype in (Epic, "Fluxo de trabalho")`, e\n'
    '**nenhuma mudou**:')

old_conf = s[s.index('Os seis conjuntos do mês corrente foram regravados'):s.index('> **Pendência remanescente (menor).**')]
new_conf = (
 'Os seis conjuntos do mês corrente foram regravados em `_snap/` a partir das respostas ao vivo e\n'
 'conferidos **item a item** — e não só por contagem — contra os arquivos da geração anterior:\n'
 '`planned` 13, `overdue` 1, `lookahead` 33, `sent` 4, `resolved` 4, `rework` 3, com igualdade\n'
 'exata de JSON nos seis conjuntos, campo a campo (`summary`, `status`, `statusCategory`,\n'
 '`project`, `duedate`, `resolutiondate`, `updated`). As seis respostas vieram completas\n'
 '(`pageInfo.hasNextPage = false`), sem timeouts nem reexecuções; duas delas\n'
 '(`lookahead_2026-10` e a lista de projetos) estouraram o limite de tokens da resposta e foram\n'
 'extraídas com `jq` do arquivo salvo pelo próprio MCP, conforme a disciplina do passo 3. A\n'
 'igualdade dos dados é confirmada do lado do artefato publicado: com os conjuntos reescritos do\n'
 'zero, o `snapshot-data.js` saiu com os mesmos **75.248 bytes** e o `index.html` com os mesmos\n'
 '**163.034 bytes** das gerações das 15:31, 16:30, 17:31 e 20:25, e o `window.__SNAPSHOT__` caiu no\n'
 'mesmo byte 94.719 — o que só ocorre se o conteúdo embutido for idêntico, já que o carimbo de\n'
 'geração tem comprimento fixo.\n\n'
 'A lista de projetos **foi** reconsultada ao vivo nesta rodada: o `getVisibleJiraProjects`\n'
 'devolveu os mesmos **21 projetos** e os mesmos dois tipos de nível Epic (`Epic` e\n'
 '`Fluxo de trabalho`). A resposta ao vivo foi reduzida ao formato mínimo e comparada ao\n'
 '`_projects_min.json` em disco por igualdade estrutural — chave, nome e lista de tipos de cada\n'
 'projeto, normalizados: **idênticos**. O arquivo, por isso, **não** foi regravado — os nomes de\n'
 'projeto gravados nos conjuntos continuam batendo, um a um, com os desse arquivo.\n\n'
 'Os seis arquivos do mês corrente em `_snap/` foram regravados com o mesmo conteúdo. Os meses\n'
 'congelados não foram tocados.\n\n')
s = s.replace(old_conf, new_conf, 1)

old_nota = s[s.index('> **Nota de publicação (14/10/2026, 20:25).**'):s.index('A **visão acumulada**')]
new_nota = (
 '> **Nota de publicação (14/10/2026, 20:31).** A cadeia de publicação está íntegra: o\n'
 '> `.push-watchdog.log` registra a passagem das 20:24, com `Commit OK: 12e3abe` e `Push OK e\n'
 '> VERIFICADO: HEAD sincronizado com origin/main`, logo após a das 20:14 (`3f5ed33`) e a das\n'
 '> 20:04. As passagens correm a cada ~10 minutos e todas as recentes concluíram com sucesso.\n'
 '> Esta geração entra na passagem seguinte, prevista para ~20:34.\n\n')
s = s.replace(old_nota, new_nota, 1)

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-14T20:25:14-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, logo após `<head>`, com o carimbo\n'
    '  `2026-10-14T20:31:52-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 14/10/2026 20:25,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 14/10/2026 20:31,')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
