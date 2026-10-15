# -*- coding: utf-8 -*-
"""Atualiza README.md para a geracao das 17:31 de 15/10/2026 (nada mudou)."""
import io, sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:90])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 15/10/2026 16:31** (`2026-10-15T16:31:29-03:00`)',
    '> **Última atualização do snapshot: 15/10/2026 17:31** (`2026-10-15T17:31:07-03:00`)')
rep('Geração em 15/10/2026 16:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 15/10/2026 17:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

# ---- bloco "o que mudou" -> nada mudou ----
i0 = s.index('### Três conjuntos mudaram nesta rodada')
i1 = s.index('> **Pendência remanescente.**')
novo = (
 '### Nenhum conjunto mudou nesta rodada\n\n'
 'Sétima geração de 15/10, uma hora após a das 16:31. As **seis** consultas JQL do mês corrente\n'
 'foram reexecutadas ao vivo com o predicado `issuetype in (Epic, "Fluxo de trabalho")`, e\n'
 '**nenhuma mudou**:\n\n'
 '| Conjunto | Ao vivo | Geração anterior | Situação |\n'
 '|---|---:|---:|---|\n'
 '| `planned_2026-10` | 15 | 15 | idêntico |\n'
 '| `overdue_2026-10` | 0 | 0 | vazio, sem alteração |\n'
 '| `lookahead_2026-10` | 33 | 33 | idêntico |\n'
 '| `sent_2026-10` | 6 | 6 | idêntico |\n'
 '| `resolved_2026-10` | 6 | 6 | idêntico |\n'
 '| `rework_2026-10` | 4 | 4 | idêntico |\n\n'
 'A comparação foi feita **item a item**, e não por contagem. Os seis conjuntos foram remontados\n'
 'do zero a partir das respostas ao vivo, no formato mínimo, e comparados aos arquivos em\n'
 '`_snap/` por **hash SHA-256 do conjunto normalizado** — chave, `summary`, `status.name`,\n'
 '`status.statusCategory.key`, `project.key`, `project.name`, `duedate`, `resolutiondate` e\n'
 '`updated` de cada registro, ordenados por chave para que a ordem de retorno do Jira não\n'
 'interfira. Os seis hashes bateram. O `EG0274-38`, entregue às 15:30 e capturado pela geração\n'
 'das 16:31, continua nos três conjuntos de envio, sem nenhuma transição nova depois dele.\n\n'
 'As seis respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts nem\n'
 'reexecuções; duas delas (`lookahead_2026-10`, com 33 registros, e a lista de projetos)\n'
 'estouraram o limite de tokens da resposta e foram extraídas com `jq` do arquivo salvo pelo\n'
 'próprio MCP, conforme a disciplina do passo 3. Como os conjuntos saíram idênticos aos de\n'
 'disco, **nenhum** arquivo de `_snap/` foi regravado nesta rodada — os hashes e tamanhos abaixo\n'
 'são os mesmos da geração anterior:\n\n'
 '| Conjunto | SHA-256 (12 primeiros) | Bytes |\n'
 '|---|---|---:|\n'
 '| `planned_2026-10` | `9e6c5f63540d` | 5.661 |\n'
 '| `overdue_2026-10` | `4f53cda18c2b` | 2 |\n'
 '| `lookahead_2026-10` | `0369f85c277b` | 12.591 |\n'
 '| `sent_2026-10` | `fde12c4e34f0` | 2.443 |\n'
 '| `resolved_2026-10` | `47039cf227fb` | 2.488 |\n'
 '| `rework_2026-10` | `8b6f50c31e86` | 1.629 |\n\n'
 'A lista de projetos **foi** reconsultada ao vivo nesta rodada: o `getVisibleJiraProjects`\n'
 'devolveu os mesmos **21 projetos** (`isLast = true`, `total = 21`) e os mesmos dois tipos de\n'
 'nível Epic (`Epic` e `Fluxo de trabalho`), usados para montar o predicado das consultas. A\n'
 'resposta foi reduzida ao formato mínimo e comparada ao `_projects_min.json` em disco por\n'
 'igualdade estrutural normalizada — chave, nome e lista de tipos de cada projeto —, com hash\n'
 'idêntico (`dc34525419c0…`). O arquivo, por isso, **não** foi regravado, e os nomes de projeto\n'
 'gravados nos conjuntos continuam batendo, um a um, com os desse arquivo. Os meses congelados\n'
 'não foram tocados.\n\n'
)
s = s[:i0] + novo + s[i1:]

rep('> Nesta rodada o efeito foi **medido**: com `issuetype=Epic`, `planned_2026-10` devolve **10**',
    '> O efeito foi **medido** na geração das 16:31: com `issuetype=Epic`, `planned_2026-10`\n'
    '> devolve **10**')

# ---- nota de publicacao ----
i0 = s.index('> **Nota de publicação (15/10/2026, 16:31).**')
i1 = s.index('A **visão acumulada**')
nota = (
 '> **Nota de publicação (15/10/2026, 17:31).** A cadeia de publicação está íntegra: o\n'
 '> `.push-watchdog.log` registra a passagem das 17:24, com `Commit OK: c1e2fac` e `Push OK e\n'
 '> VERIFICADO: HEAD sincronizado com origin/main`. As passagens correm a cada ~10 minutos e as\n'
 '> quatro mais recentes (16:54, 17:04, 17:14 e 17:24) concluíram todas com sucesso. Esta\n'
 '> geração entra na passagem seguinte, prevista para ~17:34.\n\n')
s = s[:i0] + nota + s[i1:]

# ---- indicadores ----
rep('Dois indicadores **mudaram** em relação à geração das 15:31, pela entrega do `EG0274-38`:\n\n'
    '- **OTD 13% → 20%.** O numerador subiu de 2 para 3 com a entrega do `EG0274-38` (due 07/10,\n'
    '  enviado hoje às 15:30); o denominador segue em 15. Os três entregues contam como **"SIM\\*"**\n'
    '  — entrega no mês, mas depois da due date —, de modo que o painel marca **0 no prazo e 3 com\n'
    '  pequeno atraso**.\n'
    '- **Retrabalho 50% → 57%.** Numerador e denominador subiram juntos: o `EG0274-38` entra na\n'
    '  união `sent` + `resolved` (6 → 7) e também em `rework` (3 → 4), por já ter saído antes do\n'
    '  status "Enviado - Aguardando Análise".\n'
    '- **Atraso acumulado** segue em **0**; as **pendências do mês** caem de 13 para 12.',
    'Os quatro indicadores repetem os da geração das 16:31, sem nenhuma transição nova no\n'
    'intervalo:\n\n'
    '- **OTD 20%** (3 de 15). Os três entregues — `EG0286-7`, `EG291-4` e `EG0274-38` — contam\n'
    '  como **"SIM\\*"** (entrega no mês, mas depois da due date), de modo que o painel marca\n'
    '  **0 no prazo e 3 com pequeno atraso**.\n'
    '- **Retrabalho 57%** (4 de 7 envios), no denominador do painel (união de `sent` e `resolved`).\n'
    '- **Atraso acumulado** segue em **0**; as **pendências do mês**, em **12**.')

rep('A composição é a mesma das gerações anteriores; junto com o `overdue` (vazio), foi um dos dois\n'
    'conjuntos do mês corrente que saíram idênticos nesta rodada.',
    'A composição é a mesma das gerações anteriores; nesta rodada os seis conjuntos do mês\n'
    'corrente saíram idênticos aos de disco.')

# ---- conferencia estrutural ----
rep('  `2026-10-15T16:31:29-03:00`.', '  `2026-10-15T17:31:07-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 16:31,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 15/10/2026 17:31,')
rep('  (bloco injetado abre no byte 22.611 do `index.html` e `window.__SNAPSHOT__` é atribuído no\n'
    '  byte 97.267, contra o byte 99.717 da atribuição `window.__HISTORY__=` do `<script>` próprio\n'
    '  do artifact — ordem de execução confirmada).',
    '  (bloco injetado abre no byte 22.611 do `index.html` e `window.__SNAPSHOT__` é atribuído no\n'
    '  byte 97.267, contra o byte 99.717 da atribuição `window.__HISTORY__=` do `<script>` próprio\n'
    '  do artifact — ordem de execução confirmada, com os mesmos deslocamentos da rodada anterior).')
rep('- Tamanhos da geração: `index.html` **164.972 bytes** e `snapshot-data.js` **77.186 bytes**,\n'
    '  contra 164.016 e 76.230 da rodada anterior — o crescimento corresponde ao registro novo em\n'
    '  `sent`, `resolved` e `rework`.',
    '- Tamanhos da geração: `index.html` **164.972 bytes** e `snapshot-data.js` **77.186 bytes**,\n'
    '  exatamente os da rodada anterior — o conteúdo embutido é idêntico e o carimbo de geração\n'
    '  tem comprimento fixo.')
rep('  md5 reconferido nesta rodada.', '  md5 reconferido nesta rodada (`6a2b6462a4efbec1890af4494a7f0b74`, 87.509 bytes).')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
