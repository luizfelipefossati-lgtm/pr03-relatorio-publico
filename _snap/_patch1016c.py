# -*- coding: utf-8 -*-
"""Atualiza o README.md para a geracao das 23:32 de 15/10/2026."""
import io, os, sys

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if s.count(old) != n:
        sys.exit('NAO ENCONTRADO (%d ocorrencias): %s' % (s.count(old), old[:120]))
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 15/10/2026 22:30** (`2026-10-15T22:30:19-03:00`)',
    '> **Última atualização do snapshot: 15/10/2026 23:32** (`2026-10-15T23:32:07-03:00`)')

rep('Geração em 15/10/2026 22:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 15/10/2026 23:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

rep('Décima primeira geração de 15/10, cerca de uma hora após a das 21:32.',
    'Décima segunda geração de 15/10, cerca de uma hora após a das 22:30.')

rep('O `EG0274-38`, entregue às 15:30, continua nos três conjuntos de envio,',
    'O `EG0274-38`, entregue às 15:30, continua nos três conjuntos de envio,')

# ---- disciplina do passo 3: nesta rodada quem estourou foi a lista de projetos ----
rep('As respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts nem reexecuções.\n'
    'Como nas rodadas anteriores, o `lookahead_2026-10` foi consultado em **duas metades**\n'
    '(`duedate` em nov/2026 e em dez/2026, 11 + 22 = 33), o que manteve as duas respostas abaixo do\n'
    'limite de tokens e dispensou a extração por arquivo. Como os conjuntos saíram idênticos aos de',
    'As respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts nem reexecuções.\n'
    'Como nas rodadas anteriores, o `lookahead_2026-10` foi consultado em **duas metades**\n'
    '(`duedate` em nov/2026 e em dez/2026, 11 + 22 = 33), o que manteve as duas respostas abaixo do\n'
    'limite de tokens. Nesta rodada a disciplina do passo 3 foi necessária apenas na **lista de\n'
    'projetos**, que voltou a estourar o limite (62.513 caracteres) e foi reduzida com `jq` sobre o\n'
    'arquivo salvo pelo próprio MCP. Como os conjuntos saíram idênticos aos de')

# ---- lista de projetos: nesta rodada foi reconsultada ao vivo ----
rep('A lista de projetos **não** foi reconsultada ao vivo nesta rodada: o `_projects_min.json` em\n'
    'disco, reconferido ao vivo na geração das 21:32, traz os mesmos **21 projetos** e a mesma dupla\n'
    'de tipos de nível Epic (`Epic` e `Fluxo de trabalho`). A conferência desta rodada foi de\n'
    'consistência interna — todos os projetos que aparecem nos conjuntos de outubro e no lookahead,\n'
    'inclusive o `EG0294`, constam do arquivo, e os tipos de nível Epic derivados dele são\n'
    'exatamente os dois usados no predicado das consultas. Os meses congelados não foram tocados.',
    'A lista de projetos **foi** reconsultada ao vivo nesta rodada (`getVisibleJiraProjects`,\n'
    '`expandIssueTypes`), e saiu idêntica à embutida: os mesmos **21 projetos** — `CREA`, `EG0232`,\n'
    '`EG0235`, `EG0239`, `EG0240`, `EG0241`, `EG0256`, `EG0257`, `EG0272`, `EG0273`, `EG0274`,\n'
    '`EG0275`, `EG0285`, `EG0286`, `EG0287`, `EG0292`, `EG0294`, `EG291`, `G0120`, `G0280` e `PE`\n'
    '— e a mesma dupla de tipos de nível Epic (`Epic` e `Fluxo de trabalho`). A comparação foi feita\n'
    'por **md5 do conjunto normalizado** (chave, nome e tipos de issue com `hierarchyLevel`,\n'
    'ordenado por chave): `1da60355ea01…` ao vivo e em `snapshot-data.js`, idênticos. Todos os\n'
    'projetos que aparecem nos conjuntos de outubro e no lookahead, inclusive o `EG0294`, constam da\n'
    'lista. Os meses congelados não foram tocados.')

# ---- origem do artifact: nesta rodada foi conferida ao vivo de novo ----
rep('rotina não faz por conta própria. A equivalência foi **verificada na geração das 15:31**: o',
    'rotina não faz por conta própria. A equivalência foi **reverificada nesta geração**: o')
rep('> `list_legacy_live_artifacts` + `device_stage_files(artifact_ids=[...])` trouxe o artifact ao\n'
    '> vivo (87.509 bytes, `updatedAt` 27/07/2026) e o `md5` bateu com o do `_artifact_src.html` em\n'
    '> disco (`6a2b6462a4efbec1890af4494a7f0b74`). Nesta rodada a cópia local foi reaproveitada, com\n'
    '> o mesmo md5 reconferido — a origem em cache é byte a byte o artifact atual, sem defasagem.',
    '> `list_legacy_live_artifacts` + `device_stage_files(artifact_ids=[...])` trouxe o artifact ao\n'
    '> vivo (87.509 bytes, `updatedAt` 27/07/2026) e o `md5` bateu com o do `_artifact_src.html` em\n'
    '> disco (`6a2b6462a4efbec1890af4494a7f0b74`). O caminho continua recusado, mas a origem em\n'
    '> cache é, nesta rodada também, byte a byte o artifact atual — sem defasagem.')

# ---- nota de publicacao ----
i0 = s.index('> **Nota de publicação (15/10/2026, 22:30).**')
i1 = s.index('A **visão acumulada**')
nota = (
 '> **Nota de publicação (15/10/2026, 23:32).** A cadeia de publicação está íntegra: o\n'
 '> `.push-watchdog.log` registra a passagem das 23:24, com `Commit OK: 2e98244` e `Push OK e\n'
 '> VERIFICADO: HEAD sincronizado com origin/main`. As cinco passagens mais recentes (22:44,\n'
 '> 22:54, 23:04, 23:14 e 23:24) concluíram todas com sucesso, em cadência regular de **10\n'
 '> minutos** — sem o espaçamento de 21 minutos observado por volta das 22:04 e sem repetir a\n'
 '> lacuna de 67 minutos registrada mais cedo no dia. Esta geração entra na passagem seguinte,\n'
 '> prevista para ~23:34.\n\n')
s = s[:i0] + nota + s[i1:]

rep('Os quatro indicadores repetem os da geração das 19:29, sem nenhuma transição nova no',
    'Os quatro indicadores repetem os da geração das 22:30, sem nenhuma transição nova no')

# ---- conferencia estrutural ----
rep('  `2026-10-15T22:30:19-03:00`.', '  `2026-10-15T23:32:07-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 22:30,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 23:32,')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
