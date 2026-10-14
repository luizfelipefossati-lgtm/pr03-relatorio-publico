# -*- coding: utf-8 -*-
import io, os, sys
P = os.path.expanduser('~/mnt/pr03-relatorio-publico/README.md')
s = io.open(P, encoding='utf-8').read(); orig = s
def rep(old, new, n=1):
    global s
    if old not in s: sys.exit('NAO ENCONTRADO: ' + old[:160])
    s = s.replace(old, new, n)

rep('> **Última atualização do snapshot: 13/10/2026 17:31** (`2026-10-13T17:31:37-03:00`)',
    '> **Última atualização do snapshot: 14/10/2026 09:32** (`2026-10-14T09:32:25-03:00`)')

rep('| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 | 34 |',
    '| `lookahead_2026-10` | Due date entre nov/2026 e dez/2026 | 33 | 33 |')

rep('Geração em 13/10/2026 17:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    'Geração em 14/10/2026 09:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

old_block = s[s.index('### Movimento real no lookahead'):s.index('A **visão acumulada**')]
new_block = u'''### Nenhum conjunto alterado nesta rodada

Primeira geração desde a tarde de ontem — o intervalo entre as duas é de cerca de 16 horas,
atravessando a madrugada. As sete chamadas dinâmicas foram reexecutadas ao vivo com o predicado
`issuetype in (Epic, "Fluxo de trabalho")` e **nenhum conjunto mudou**:

| Conjunto | Ao vivo | Cache em disco | Situação |
|---|---:|---:|---|
| `planned_2026-10` | 13 | 13 | idêntico ao cache |
| `overdue_2026-10` | 1 | 1 | idêntico ao cache |
| `lookahead_2026-10` | 33 | 33 | idêntico ao cache |
| `sent_2026-10` | 4 | 4 | idêntico ao cache |
| `resolved_2026-10` | 4 | 4 | idêntico ao cache |
| `rework_2026-10` | 3 | 3 | idêntico ao cache |
| projetos visíveis | 21 | 21 | idêntico ao cache |

A conferência foi item a item, na ordem, por `key`, `summary`, `status.name`,
`status.statusCategory.key`, `project.key`, `duedate`, `resolutiondate` e `updated` — zero campos
divergentes nos 58 registros dos seis conjuntos. A lista de projetos foi comparada por `sha256`
do JSON canônico com `issueTypes` ordenados: idêntica, os mesmos 21 projetos e os mesmos dois
tipos de nível Epic. O `EG0256-30`, que saiu do lookahead na rodada de ontem às 17:31 ao ser
reprogramado para 30/01/2027, continua fora — a mudança de ontem se manteve.

Nenhum arquivo de `_snap/` nem o `_projects_min.json` precisou ser regravado. O `index.html`
permanece em **163.034 bytes** e o `snapshot-data.js` em **75.248 bytes**, os mesmos da geração
anterior: a única diferença entre os dois arquivos publicados é o carimbo de geração, que tem
comprimento fixo. Os meses congelados não foram tocados.

> **Pendência remanescente (menor).** O texto `issuetype=Epic` continua gravado no prompt da
> tarefa agendada, no passo que descreve as seis consultas. Ele não afeta a página publicada —
> o artifact monta o predicado dinamicamente a partir dos tipos de hierarquia 1 dos projetos
> visíveis —, mas faz cada rodada partir de uma consulta truncada e precisar corrigi-la à mão.
> Trocar aquele trecho do prompt por `issuetype in (Epic, "Fluxo de trabalho")` elimina o
> retrabalho — e é uma alteração no prompt da tarefa, que esta rotina não faz por conta própria.

'''
s = s.replace(old_block, new_block, 1)

old_note = s[s.index(u'> **Nota de publicação (13/10/2026, 17:31).**'):s.index('Outubro segue com')]
new_note = u'''> **Nota de publicação (14/10/2026, 09:32).** A cadeia de publicação está íntegra, mas o
> `.push-watchdog.log` registra um episódio digno de nota na virada da noite: a passagem das
> **13/10 22:40** fez `Commit OK` (`8b4c3e8`) e ficou presa no push por **10h26min**, só
> concluindo com `Push OK e VERIFICADO` às **14/10 09:06:59** — compatível com a máquina ter
> hibernado com o push em andamento. Depois disso as passagens voltaram ao ritmo normal:
> 09:14:37 (`e19fc8e`) e 09:24:35 (`80d70f0`), ambas com `HEAD` sincronizado com `origin/main`.
> A geração de ontem às 17:31 foi publicada. Esta geração entra na próxima passagem da tarefa.

'''
s = s.replace(old_note, new_note, 1)

rep(u'''Outubro segue com **um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e de novo
`Em Revisão` desde 13/10 às 09:51. Os dois EPICs do EG0256 reprogramados em 08/10 às 11:31
seguiram caminhos diferentes: `EG0256-28` continua em 29/01/2027, e `EG0256-30`, que fora
movido para 19/12/2026, foi **empurrado de novo hoje às 17:04 para 30/01/2027** — saindo do
lookahead desta geração.''',
u'''Outubro segue com **um EPIC em atraso acumulado** — `EG0240-5`, vencido em 30/09 e em
`Em Revisão` desde 13/10 às 09:51, sem movimento desde então. Os dois EPICs do EG0256
reprogramados para 2027 (`EG0256-28` em 29/01 e `EG0256-30` em 30/01) seguem fora de qualquer
conjunto de outubro.''')

rep(u'### Quadro de outubro/2026 (13º dia do mês)', u'### Quadro de outubro/2026 (14º dia do mês)')

rep(u'''Os três indicadores repetem os da geração anterior. O OTD permanece em 8%: o único envio com''',
    u'''Os três indicadores repetem os da geração anterior — e, com os seis conjuntos idênticos ao
cache, repetem-se por identidade de dados, não por coincidência de contagem. O OTD permanece em 8%: o único envio com''')

rep(u'''A concentração de dezembro **recua um ponto** com a saída do `EG0256-30`, reprogramado de
19/12/2026 para 30/01/2027 nesta rodada — o EG0256 deixa de ter representante no lookahead.
Ainda assim, 20 dos 33 registros (**61%**) caem na segunda quinzena de dezembro: o gargalo de
fim de ano permanece, concentrado em EG0274 e EG0286.''',
u'''A composição é a mesma da geração anterior: o EG0256 segue sem representante no lookahead
desde a saída do `EG0256-30`, reprogramado para 30/01/2027 ontem às 17:04. **20 dos 33
registros (61%)** caem na segunda quinzena de dezembro — o gargalo de fim de ano permanece,
concentrado em EG0274 e EG0286.''')

rep(u'- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-13T17:31:37-03:00`.',
    u'- Comentário de geração no topo do `<head>`: presente, com o carimbo `2026-10-14T09:32:25-03:00`.')
rep(u'- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 13/10/2026 17:31,',
    u'- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 14/10/2026 09:32,')
rep(u'''- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudaram apenas o carimbo de geração e um registro do
  `lookahead_2026-10`, dentro da estrutura de dados já existente.''',
u'''- Renderização não reexecutada em navegador nesta rodada (execução agendada e autônoma). O
  HTML-fonte é idêntico ao das rodadas anteriores — a última verificada em Chromium headless
  sem erros de script — e nesta rodada mudou apenas o carimbo de geração; os dados embutidos
  são byte a byte os mesmos.''')
rep(u'''  `updated`) e `pageInfo.hasNextPage = false` em todas. Duas respostas excederam o limite de
  tokens — o `lookahead`, por ser o maior conjunto, e o `getVisibleJiraProjects` — e ambas foram
  reduzidas à forma mínima sobre o arquivo salvo pelo runtime, conforme o procedimento previsto.
  A comparação com o arquivo em disco foi feita por `key`, `summary`, `status.name`,
  `status.statusCategory.key`, `duedate`, `resolutiondate` e `updated`; o `project` de cada
  registro mantido foi preservado do arquivo.''',
u'''  `updated`) e `pageInfo.hasNextPage = false` em todas. O `lookahead`, por ser o maior conjunto,
  foi pedido sem o campo `project` — que não muda para uma issue já existente — e coube inline;
  os outros cinco couberam com a projeção completa. Só a resposta do `getVisibleJiraProjects`
  excedeu o limite de tokens, e foi reduzida à forma mínima sobre o arquivo salvo pelo runtime,
  conforme o procedimento previsto. A comparação com o arquivo em disco foi feita por `key`,
  `summary`, `status.name`, `status.statusCategory.key`, `duedate`, `resolutiondate` e `updated`,
  mais a ordem; o `project` de cada registro foi preservado do arquivo.''')

io.open(P, 'w', encoding='utf-8').write(s)
print('README atualizado: %d -> %d bytes' % (len(orig.encode('utf-8')), len(s.encode('utf-8'))))
