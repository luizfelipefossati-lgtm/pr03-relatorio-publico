# -*- coding: utf-8 -*-
"""Atualiza README.md para a geracao das 13:31 de 15/10/2026."""
import io, sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:90])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 15/10/2026 12:30** (`2026-10-15T12:30:22-03:00`)',
    '> **Última atualização do snapshot: 15/10/2026 13:31** (`2026-10-15T13:31:02-03:00`)')
rep('Geração em 15/10/2026 12:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 15/10/2026 13:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')
rep('Terceira geração de 15/10, cerca de **duas horas** após a das 10:30. As **seis**\n'
    'consultas JQL do mês corrente foram reexecutadas ao vivo com o predicado\n'
    '`issuetype in (Epic, "Fluxo de trabalho")`, e **nenhuma mudou**:',
    'Quarta geração de 15/10, cerca de **uma hora** após a das 12:30. As **seis**\n'
    'consultas JQL do mês corrente foram reexecutadas ao vivo com o predicado\n'
    '`issuetype in (Epic, "Fluxo de trabalho")`, e **nenhuma mudou**:')

i0 = s.index('A comparação foi feita **item a item**')
i1 = s.index('> **Pendência remanescente (menor).**')
novo = (
 'A comparação foi feita **item a item**, e não por contagem. Os seis conjuntos do mês corrente\n'
 'foram remontados do zero a partir das respostas ao vivo, no formato mínimo, e comparados aos\n'
 'arquivos em `_snap/` por **hash SHA-256 do JSON serializado** — o que cobre chave, `summary`,\n'
 '`status.name`, `status.statusCategory.key`, `project.key`, `project.name`, `duedate`,\n'
 '`resolutiondate`, `updated` **e a ordem dos registros** de uma só vez. Os seis hashes bateram,\n'
 'byte a byte, com os dos arquivos em disco:\n\n'
 '| Conjunto | SHA-256 (12 primeiros) | Bytes |\n'
 '|---|---|---:|\n'
 '| `planned_2026-10` | `b4f847fc1f0c` | 4.807 |\n'
 '| `overdue_2026-10` | `fc714b77d49c` | 397 |\n'
 '| `lookahead_2026-10` | `0369f85c277b` | 12.591 |\n'
 '| `sent_2026-10` | `bdd875dd58e3` | 1.635 |\n'
 '| `resolved_2026-10` | `b81f03dcbbdf` | 1.680 |\n'
 '| `rework_2026-10` | `d1016bb331c0` | 1.233 |\n\n'
 'As seis respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts nem\n'
 'reexecuções; duas delas (`lookahead_2026-10`, com 33 registros, e a lista de projetos)\n'
 'estouraram o limite de tokens da resposta e foram extraídas do arquivo salvo pelo próprio MCP,\n'
 'conforme a disciplina do passo 3. A igualdade dos dados é confirmada do lado do artefato\n'
 'publicado: o `snapshot-data.js` saiu com os mesmos **75.248 bytes** e o `index.html` com os\n'
 'mesmos **163.034 bytes** das gerações anteriores, e o `window.__SNAPSHOT__` caiu no mesmo byte\n'
 '**95.329** — o que só ocorre se o conteúdo embutido for idêntico, já que o carimbo de geração\n'
 'tem comprimento fixo.\n\n'
 'A lista de projetos **foi** reconsultada ao vivo nesta rodada: o `getVisibleJiraProjects`\n'
 'devolveu os mesmos **21 projetos** (`isLast = true`, `total = 21`) e os mesmos dois tipos de\n'
 'nível Epic (`Epic` e `Fluxo de trabalho`). A resposta foi reduzida ao formato mínimo e\n'
 'comparada ao `_projects_min.json` em disco por igualdade estrutural normalizada — chave, nome\n'
 'e lista de tipos de cada projeto —, com hash idêntico (`81c3eeb3b263…`). O arquivo, por isso,\n'
 '**não** foi regravado, e os nomes de projeto gravados nos conjuntos continuam batendo, um a\n'
 'um, com os desse arquivo.\n\n'
 'Como os seis conjuntos saíram idênticos aos de disco, os arquivos de `_snap/` **não**\n'
 'precisaram ser regravados nesta rodada. Os meses congelados não foram tocados.\n\n')
s = s[:i0] + novo + s[i1:]

i0 = s.index('> **Nota de publicação (15/10/2026, 12:30).**')
i1 = s.index('A **visão acumulada**')
nota = (
 '> **Nota de publicação (15/10/2026, 13:31).** A cadeia de publicação está íntegra: o\n'
 '> `.push-watchdog.log` registra a passagem das 13:24, com `Commit OK: 2a2db94` e `Push OK e\n'
 '> VERIFICADO: HEAD sincronizado com origin/main`. As passagens correm a cada ~10 minutos e as\n'
 '> quatro mais recentes (12:54, 13:04, 13:14 e 13:24) concluíram todas com sucesso. Esta\n'
 '> geração entra na passagem seguinte, prevista para ~13:34.\n\n')
s = s[:i0] + nota + s[i1:]

rep('Os três indicadores repetem os das seis gerações anteriores',
    'Os três indicadores repetem os das sete gerações anteriores')
rep('  `2026-10-15T12:30:22-03:00`.', '  `2026-10-15T13:31:02-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 12:30,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 13:31,')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
