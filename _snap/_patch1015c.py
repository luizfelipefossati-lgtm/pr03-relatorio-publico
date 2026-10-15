# -*- coding: utf-8 -*-
"""Atualiza README.md para a geracao das 12:30 de 15/10/2026."""
import io, sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:90])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 15/10/2026 10:30** (`2026-10-15T10:30:35-03:00`)',
    '> **Última atualização do snapshot: 15/10/2026 12:30** (`2026-10-15T12:30:22-03:00`)')
rep('Geração em 15/10/2026 10:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 15/10/2026 12:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')
rep('Segunda geração de 15/10, cerca de **uma hora** após a das 09:31. As **seis**\n'
    'consultas JQL do mês corrente foram reexecutadas ao vivo com o predicado\n'
    '`issuetype in (Epic, "Fluxo de trabalho")`, e **nenhuma mudou**:',
    'Terceira geração de 15/10, cerca de **duas horas** após a das 10:30. As **seis**\n'
    'consultas JQL do mês corrente foram reexecutadas ao vivo com o predicado\n'
    '`issuetype in (Epic, "Fluxo de trabalho")`, e **nenhuma mudou**:')

i0 = s.index('A comparação foi feita por dois caminhos')
i1 = s.index('> **Pendência remanescente (menor).**')
novo = (
 'A comparação foi feita **item a item**, e não por contagem. Os seis conjuntos do mês corrente\n'
 'foram remontados do zero a partir das respostas ao vivo, no formato mínimo, e comparados por\n'
 'igualdade estrutural de JSON aos arquivos em `_snap/` — chave, `summary`, `status.name`,\n'
 '`status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate` e\n'
 '`updated`, **na mesma ordem**: os seis saíram idênticos, sem uma única divergência de campo. As\n'
 'seis respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts nem\n'
 'reexecuções; duas delas (`lookahead_2026-10`, com 33 registros, e a lista de projetos)\n'
 'estouraram o limite de tokens da resposta e foram extraídas com `jq` do arquivo salvo pelo\n'
 'próprio MCP, conforme a disciplina do passo 3. A igualdade dos dados é confirmada do lado do\n'
 'artefato publicado: com os seis conjuntos regravados a partir do resultado ao vivo, o\n'
 '`snapshot-data.js` saiu com os mesmos **75.248 bytes** e o `index.html` com os mesmos\n'
 '**163.034 bytes** das gerações anteriores, e o `window.__SNAPSHOT__` caiu no mesmo byte\n'
 '**95.329** — o que só ocorre se o conteúdo embutido for idêntico, já que o carimbo de geração\n'
 'tem comprimento fixo.\n\n'
 'A lista de projetos **foi** reconsultada ao vivo nesta rodada: o `getVisibleJiraProjects`\n'
 'devolveu os mesmos **21 projetos** (`isLast = true`, `total = 21`) e os mesmos dois tipos de\n'
 'nível Epic (`Epic` e `Fluxo de trabalho`). A resposta foi reduzida ao formato mínimo e\n'
 'comparada ao `_projects_min.json` em disco por igualdade estrutural — chave, nome e lista de\n'
 'tipos de cada projeto, normalizados: **idênticos**, e os dois arquivos têm os mesmos 6.657\n'
 'bytes. O arquivo, por isso, **não** foi regravado — os nomes de projeto gravados nos conjuntos\n'
 'continuam batendo, um a um, com os desse arquivo.\n\n'
 'Os seis arquivos do mês corrente em `_snap/` foram regravados com o mesmo conteúdo. Os meses\n'
 'congelados não foram tocados.\n\n')
s = s[:i0] + novo + s[i1:]

i0 = s.index('> **Nota de publicação (15/10/2026, 10:30).**')
i1 = s.index('A **visão acumulada**')
nota = (
 '> **Nota de publicação (15/10/2026, 12:30).** A cadeia de publicação está íntegra: o\n'
 '> `.push-watchdog.log` registra a passagem das 12:24, com `Commit OK: a4e4d5f` e `Push OK e\n'
 '> VERIFICADO: HEAD sincronizado com origin/main`. As passagens correm a cada ~10 minutos e\n'
 '> todas as recentes concluíram com sucesso. Esta geração entra na passagem seguinte, prevista\n'
 '> para ~12:34.\n\n')
s = s[:i0] + nota + s[i1:]

rep('  `2026-10-15T10:30:35-03:00`.', '  `2026-10-15T12:30:22-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 10:30,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 12:30,')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
