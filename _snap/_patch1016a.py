# -*- coding: utf-8 -*-
"""Atualiza README.md para a geracao das 21:32 de 15/10/2026 (nada mudou nos dados)."""
import io, sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:110])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 15/10/2026 19:29** (`2026-10-15T19:29:45-03:00`)',
    '> **Última atualização do snapshot: 15/10/2026 21:32** (`2026-10-15T21:32:20-03:00`)')
rep('Geração em 15/10/2026 19:29 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 15/10/2026 21:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

# ---- coluna "Geracao anterior" do quadro de conjuntos do mes corrente ----
rep('| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | **6** | 5 |\n'
    '| `resolved_2026-10` | Concluídos em out/2026 | **6** | 5 |\n'
    '| `rework_2026-10` | Retrabalho em out/2026 | **4** | 3 |',
    '| `sent_2026-10` | Transições para "Enviado - Aguardando Análise" em out/2026 | 6 | 6 |\n'
    '| `resolved_2026-10` | Concluídos em out/2026 | 6 | 6 |\n'
    '| `rework_2026-10` | Retrabalho em out/2026 | 4 | 4 |')

rep('Nona geração de 15/10, uma hora após a das 18:30.',
    'Décima geração de 15/10, pouco mais de duas horas após a das 19:29.')

# ---- disciplina do passo 3: nesta rodada quem estourou foi a lista de projetos ----
rep('As seis respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts nem\n'
    'reexecuções; uma delas (`lookahead_2026-10`, com 33 registros) estourou o limite de tokens da\n'
    'resposta e foi extraída com `jq` do arquivo salvo pelo próprio MCP, conforme a disciplina do\n'
    'passo 3. Como os conjuntos saíram idênticos aos de',
    'As seis respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts nem\n'
    'reexecuções. Nesta rodada o `lookahead_2026-10` foi consultado em **duas metades**\n'
    '(`duedate` em nov/2026 e em dez/2026, 11 + 22 = 33), o que manteve as duas respostas abaixo\n'
    'do limite de tokens e dispensou a extração por arquivo — a disciplina do passo 3 foi\n'
    'necessária apenas na lista de projetos. Como os conjuntos saíram idênticos aos de')

rep('`_projects_min.json` em disco — `42e8a14f9d65…` —, de modo que a dupla de tipos de nível Epic',
    '`_projects_min.json` em disco — `f938b6c2df9a…` —, de modo que a dupla de tipos de nível Epic')

# ---- nota de publicacao ----
i0 = s.index('> **Nota de publicação (15/10/2026, 19:29).**')
i1 = s.index('A **visão acumulada**')
nota = (
 '> **Nota de publicação (15/10/2026, 21:32).** A cadeia de publicação está íntegra: o\n'
 '> `.push-watchdog.log` registra a passagem das 21:24, com `Commit OK: e6a25e9` e `Push OK e\n'
 '> VERIFICADO: HEAD sincronizado com origin/main`. As quatro passagens mais recentes (20:54,\n'
 '> 21:04, 21:14 e 21:24) concluíram todas com sucesso. Houve, porém, uma **lacuna de 67\n'
 '> minutos** entre as passagens das 19:44 e das 20:51, fora do intervalo de ~10 minutos\n'
 '> observado no resto do log. A publicação não foi afetada — a passagem das 20:51 commitou e\n'
 '> empurrou normalmente —, mas convém olhar o agendamento da tarefa se a lacuna se repetir.\n'
 '> Esta geração entra na passagem seguinte, prevista para ~21:34.\n\n')
s = s[:i0] + nota + s[i1:]

rep('Os quatro indicadores repetem os da geração das 18:30, sem nenhuma transição nova no',
    'Os quatro indicadores repetem os da geração das 19:29, sem nenhuma transição nova no')

# ---- conferencia estrutural ----
rep('  `2026-10-15T19:29:45-03:00`.', '  `2026-10-15T21:32:20-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 19:29,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 21:32,')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
