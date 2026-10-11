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

rep('> **Última atualização do snapshot: 10/10/2026 20:32** (`2026-10-10T20:32:15-03:00`)',
    '> **Última atualização do snapshot: 10/10/2026 21:29** (`2026-10-10T21:29:49-03:00`)')

rep('Geração em 10/10/2026 20:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 10/10/2026 21:29 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

rep('''comparados por hash canônico contra a versão anterior dos mesmos arquivos (geração de 10/10,
19:30, já versionada). **Todos os sete vieram idênticos** — décima primeira rodada consecutiva
sem movimento no Jira, depois das três mudanças registradas em 09/10 às 11:32 (`EG0239-28`
concluído e `EG0240-4` reprogramado para 16/10).

| Conjunto | Registros | Situação vs. 10/10 19:30 |''',
'''comparados por hash canônico contra a versão anterior dos mesmos arquivos (geração de 10/10,
20:32, já versionada). **Todos os sete vieram idênticos** — décima segunda rodada consecutiva
sem movimento no Jira, depois das três mudanças registradas em 09/10 às 11:32 (`EG0239-28`
concluído e `EG0240-4` reprogramado para 16/10).

| Conjunto | Registros | Situação vs. 10/10 20:32 |''')

rep('''Além dos sete conjuntos acima, esta rodada reconsultou ao vivo os seis meses da **visão
acumulada** (`planned_2026-05` a `planned_2026-10`). Maio, junho e outubro vieram idênticos aos
arquivos em disco. Julho, agosto e setembro divergem da consulta ao vivo — e **devem divergir**:
são meses congelados no fechamento do período, e as diferenças são exatamente as reprogramações
posteriores ao fechamento (`EG0274-38` e `EG0274-43` saíram de julho para outubro; `EG0286-7`
saiu de agosto para outubro; `EG0240-4` saiu de setembro para 16/10). Pela regra de congelamento,
esses arquivos **não** foram regravados: o histórico de OTD de cada mês continua refletindo o
que estava previsto no fechamento daquele mês.''',
'''A **visão acumulada** (`planned_2026-05` a `planned_2026-10`) não foi reconsultada ao vivo nesta
rodada: outubro já é coberto pelo `planned_2026-10` acima, e maio a setembro são meses encerrados,
servidos tal como estão em `_snap/`. Julho, agosto e setembro são, além disso, **congelados** no
fechamento do período — divergem de propósito de uma consulta ao vivo, pelas reprogramações
posteriores ao fechamento (`EG0274-38` e `EG0274-43` saíram de julho para outubro; `EG0286-7`
saiu de agosto para outubro; `EG0240-4` saiu de setembro para 16/10). Pela regra de congelamento,
esses arquivos **não** são regravados: o histórico de OTD de cada mês continua refletindo o
que estava previsto no fechamento daquele mês.''')

rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-10T20:32:15-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-10T21:29:49-03:00`.')

rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 10/10/2026 20:32,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 10/10/2026 21:29,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
