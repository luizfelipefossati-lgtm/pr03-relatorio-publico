# -*- coding: utf-8 -*-
import io, os, sys
P = os.path.expanduser('~/mnt/pr03-relatorio-publico/README.md')
s = io.open(P, encoding='utf-8').read()
orig = s
def rep(old, new, n=1):
    global s
    if old not in s:
        sys.exit('NAO ENCONTRADO: ' + old[:140])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 13/10/2026 10:32** (`2026-10-13T10:32:27-03:00`)',
    '> **Última atualização do snapshot: 13/10/2026 11:30** (`2026-10-13T11:30:41-03:00`)')

rep('| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | **1** | 0 |',
    '| `overdue_2026-10` | Vencidos antes de out/2026, não concluídos | 1 | 1 |')
rep('| `resolved_2026-10` | Concluídos em out/2026 | **4** | 5 |',
    '| `resolved_2026-10` | Concluídos em out/2026 | 4 | 4 |')

rep('Geração em 13/10/2026 10:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 13/10/2026 11:30 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

# ---- bloco de conferencia da rodada ----
old_block = s[s.index('### Quatro conjuntos alterados: `EG0240-5` foi reaberto'):s.index('A **visão acumulada**')]
new_block = '''### Nenhum conjunto alterado nesta rodada

As seis consultas do mês corrente e o `getVisibleJiraProjects` foram reexecutados ao vivo e
comparados item a item contra a versão anterior dos mesmos arquivos (geração de 13/10, 10:32).
Os sete conjuntos vieram **idênticos**, inclusive na ordem dos registros: o Jira não registrou
movimento entre 10:32 e 11:30.

A reabertura de `EG0240-5` (*TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)*, EG0240 - GOITÁ/ COMPESA),
captada na rodada anterior, **permanece**: o EPIC segue em `Em Revisão` sem `resolutiondate`,
com `updated = 2026-10-13T09:51:44.629-0300`, e continua sendo o único EPIC em atraso acumulado
de outubro.

| Conjunto | Registros | Situação vs. 13/10 10:32 |
|---|---:|---|
| `planned_2026-10` | 13 | idêntico |
| `overdue_2026-10` | 1 | idêntico |
| `lookahead_2026-10` | 34 | idêntico |
| `sent_2026-10` | 4 | idêntico |
| `resolved_2026-10` | 4 | idêntico |
| `rework_2026-10` | 3 | idêntico |
| projetos visíveis | 21 | idêntico |

Como a coleta desta rodada reproduziu exatamente os arquivos em disco, nenhum arquivo de
`_snap/` nem o `_projects_min.json` precisou ser regravado. Entre a geração anterior e esta,
mudou apenas o carimbo de tempo do `index.html`, do `snapshot-data.js` e deste `README.md`.

'''
s = s.replace(old_block, new_block, 1)

# ---- nota de publicacao ----
old_note = s[s.index('> **Nota de publicação (13/10/2026, 10:32).**'):s.index('Outubro **volta a ter um EPIC')]
new_note = '''> **Nota de publicação (13/10/2026, 11:30).** A cadeia de publicação segue íntegra. O
> `.push-watchdog.log` registra a última passagem às 11:24:33 — `Commit OK: 2d16a35` seguido de
> `Push OK e VERIFICADO`, com `HEAD` sincronizado com `origin/main`. A geração das 10:32 foi,
> portanto, publicada. Esta geração entra na próxima passagem da tarefa.

'''
s = s.replace(old_note, new_note, 1)

rep('''Outubro **volta a ter um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e de novo
`Em Revisão`. O efeito da reprogramação dos dois EPICs do EG0256 (`EG0256-30` para
19/12/2026 e `EG0256-28` para 29/01/2027), registrada na rodada de 08/10 às 11:31, segue valendo.''',
'''Outubro segue com **um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e de novo
`Em Revisão` desde 13/10 às 09:51. O efeito da reprogramação dos dois EPICs do EG0256
(`EG0256-30` para 19/12/2026 e `EG0256-28` para 29/01/2027), registrada na rodada de 08/10
às 11:31, segue valendo.''')

# ---- demais conferencias: coleta desta rodada ----
rep('''- Cada um dos seis conjuntos de out/2026 foi coletado em **uma única consulta** nesta rodada,
  com a projeção mínima de campos (`summary`, `status`, `project`, `duedate`, `resolutiondate`,
  `updated`) e `pageInfo.hasNextPage = false` em todas. As respostas de `lookahead` e de
  `getVisibleJiraProjects` excederam o limite de tokens e foram reduzidas aos campos essenciais
  sobre o arquivo salvo pelo runtime, conforme o procedimento previsto; as demais couberam inline.
  O `getVisibleJiraProjects` desta rodada reproduziu o `_projects_min.json` em disco
  (21 projetos, mesmos tipos de nível Epic: `Epic` e `Fluxo de trabalho`), que por isso não foi
  regravado. Nesta rodada, as respostas de `lookahead` e de `getVisibleJiraProjects`
  novamente excederam o limite de tokens e foram reduzidas por `jq` sobre o arquivo salvo.''',
'''- Cada um dos seis conjuntos de out/2026 foi coletado em **uma única consulta** nesta rodada,
  com a projeção mínima de campos (`summary`, `status`, `project`, `duedate`, `resolutiondate`,
  `updated`) e `pageInfo.hasNextPage = false` em todas. O `lookahead`, por ser o maior conjunto,
  foi pedido sem o campo `project` — que não muda para uma issue já existente — e coube inline;
  a comparação com o arquivo em disco foi feita por `key`, `summary`, `status.name`,
  `status.statusCategory.key`, `duedate`, `resolutiondate` e `updated`, mais a ordem, e o
  `project` de cada registro foi preservado do arquivo. Só a resposta do
  `getVisibleJiraProjects` excedeu o limite de tokens; foi reduzida à forma mínima sobre o
  arquivo salvo pelo runtime, conforme o procedimento previsto.''')

rep('''- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026. MD5
  `6a2b6462a4efbec1890af4494a7f0b74`, o mesmo das rodadas anteriores.''',
'''- Fonte do HTML: `_artifact_src.html` (87.509 bytes), cópia do artifact
  `pr03-relatorio-indicadores-epics`, inalterado desde 27/07/2026. MD5
  `6a2b6462a4efbec1890af4494a7f0b74`, o mesmo das rodadas anteriores (conferido nesta rodada).''')

rep('''- **Filtro de tipo de item.** As consultas desta rodada usaram''',
'''- As **11 consultas JQL** do mês corrente e da visão acumulada foram remontadas exatamente como
  o artifact as monta e testadas, uma a uma, contra os 11 padrões gravados em
  `snapshot-data.js`: cada consulta resolveu para o seu próprio conjunto, nenhuma caiu no
  *fallback* de lista vazia e nenhum padrão ficou órfão.
- **Filtro de tipo de item.** As consultas desta rodada usaram''')

# ---- quadro de outubro ----
rep('### Quadro de outubro/2026 (10º dia do mês)',
    '### Quadro de outubro/2026 (13º dia do mês)')

rep('''O OTD permanece em 8%: o único envio com due date de outubro continua sendo `EG0286-7`, e o
denominador segue em 13 desde a entrada de `EG0240-4`, reprogramado para 16/10. O retrabalho
também fica em 60%: a reabertura de `EG0240-5` tirou o EPIC de `resolved`, mas ele continua em
`sent` (a transição de 07/10 está no histórico e o `DURING` a enxerga), de modo que a união
`sent` + `resolved` segue com cinco registros e três de retrabalho.''',
'''Os três indicadores repetem os da geração anterior. O OTD permanece em 8%: o único envio com
due date de outubro continua sendo `EG0286-7`, e o denominador segue em 13 desde a entrada de
`EG0240-4`, reprogramado para 16/10. O retrabalho fica em 60% porque a união `sent` + `resolved`
mantém cinco registros mesmo com `EG0240-5` reaberto — ele saiu de `resolved`, mas continua em
`sent` (a transição de 07/10 está no histórico e o `DURING` a enxerga).''')

rep('| `EG0240-5` | EG0240 | 2026-09-30 | 07/10 16:01 | sim — **reaberto em 13/10 09:51** |',
    '| `EG0240-5` | EG0240 | 2026-09-30 | 07/10 16:01 | sim — reaberto em 13/10 09:51 |')

rep('''**Um EPIC em atraso acumulado** em outubro, pela primeira vez desde 09/10: `EG0240-5`, due date
30/09, de volta a `Em Revisão`. O conjunto estava vazio porque os dois que constavam até a
rodada de 09/10 às 09:32 havíam saído — `EG0239-28` concluído em 09/10 às 09:36 e `EG0240-4`
reprogramado de 10/09 para 16/10. `EG0240-5` entra agora pelo caminho inverso: não por due date
nova, mas por ter perdido a conclusão que já tinha.''',
'''**Um EPIC em atraso acumulado** em outubro: `EG0240-5`, due date 30/09, de volta a `Em Revisão`
desde 13/10 às 09:51. O conjunto estivera vazio entre 09/10 e 13/10, porque os dois que
constavam até a rodada de 09/10 às 09:32 haviam saído — `EG0239-28` concluído em 09/10 às 09:36
e `EG0240-4` reprogramado de 10/09 para 16/10. `EG0240-5` entrou pelo caminho inverso: não por
due date nova, mas por ter perdido a conclusão que já tinha.''')

# ---- conferencia estrutural ----
rep('- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T10:32:27-03:00`.',
    '- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T11:30:41-03:00`.')
rep('- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 10:32,',
    '- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 11:30,')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode()), len(s.encode())))
