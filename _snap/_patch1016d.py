# -*- coding: utf-8 -*-
"""Atualiza o README.md para a geracao das 17:31 de 16/10/2026."""
import io, os, sys

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if s.count(old) != n:
        sys.exit('NAO ENCONTRADO (%d ocorrencias): %s' % (s.count(old), old[:140]))
    s = s.replace(old, new, n)

rep(u'> **Última atualização do snapshot: 16/10/2026 16:32** (`2026-10-16T16:32:18-03:00`)',
    u'> **Última atualização do snapshot: 16/10/2026 17:31** (`2026-10-16T17:31:26-03:00`)')

rep(u'Geração em 16/10/2026 16:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    u'Geração em 16/10/2026 17:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

rep(u'Segunda geração da tarde de 16/10, cerca de **uma hora** depois da das 15:30. As **seis**\n'
    u'consultas JQL do mês corrente foram reexecutadas ao vivo com o predicado\n'
    u'`issuetype in ("Epic","Fluxo de trabalho")`, e as contagens repetem, uma a uma, as registradas\n'
    u'na rodada anterior:',
    u'Terceira geração da tarde de 16/10, cerca de **uma hora** depois da das 16:32. As **seis**\n'
    u'consultas JQL do mês corrente foram reexecutadas ao vivo com o predicado\n'
    u'`issuetype in ("Epic","Fluxo de trabalho")`, e as contagens repetem, uma a uma, as registradas\n'
    u'na rodada anterior:')

rep(u'| Conjunto | Ao vivo | Geração das 15:30 | Situação |',
    u'| Conjunto | Ao vivo | Geração das 16:32 | Situação |')

# ---- metodo desta rodada: conferencia item a item, arquivos preservados ----
rep(u'**Diferença de método em relação à rodada das 15:30:** lá os arquivos de `_snap/` foram\n'
    u'preservados após comparação registro a registro; aqui os seis **foram regravados** com as\n'
    u'respostas ao vivo. A conferência desta rodada é, portanto, **por contagem** — as seis\n'
    u'contagens acima batem com as publicadas no README da geração anterior —, e não item a item.\n'
    u'Cinco dos seis arquivos ficaram um byte maiores (quebra de linha final acrescentada na\n'
    u'gravação) e o `lookahead_2026-10` manteve o mesmo tamanho, o que é compatível com conteúdo\n'
    u'inalterado.',
    u'**Diferença de método em relação à rodada das 16:32:** lá os seis arquivos de `_snap/` foram\n'
    u'regravados e a conferência foi por contagem; aqui eles **foram preservados** e a conferência\n'
    u'voltou a ser **registro a registro**. Os 64 registros ao vivo (15 + 0 + 33 + 6 + 6 + 4) foram\n'
    u'comparados aos de disco chave a chave e campo a campo — `duedate`, nome de status e\n'
    u'`resolutiondate` —, sem nenhuma diferença, nenhuma chave nova e nenhuma chave ausente. Os\n'
    u'seis arquivos mantêm, byte a byte, os mesmos tamanhos e os mesmos SHA-256 publicados na\n'
    u'rodada anterior.')

# ---- lookahead em metades + lista de projetos reconsultada ----
rep(u'As respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts e sem nenhum\n'
    u'`502`. O `lookahead_2026-10` foi pedido numa consulta só, em nov–dez/2026; a resposta estourou\n'
    u'o limite de tokens da ferramenta e foi gravada em arquivo pelo próprio MCP, de onde saiu\n'
    u'reduzida por `jq` aos campos mínimos — o procedimento previsto no prompt, sem precisar dividir\n'
    u'a consulta em metades. A lista de projetos **não foi reconsultada** nesta rodada: o\n'
    u'`_projects_min.json` de 14/10 (21 projetos) segue como fonte dos nomes de projeto e dos tipos\n'
    u'de nível Epic (`Epic`, `Fluxo de trabalho`) usados no predicado.',
    u'As respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts e sem nenhum\n'
    u'`502`. O `lookahead_2026-10` voltou a ser consultado em **duas metades** (`duedate` em\n'
    u'nov/2026 e em dez/2026, 11 + 22 = 33), o que manteve as duas respostas abaixo do limite de\n'
    u'tokens e dispensou a extração por arquivo. Nesta rodada a disciplina do passo 3 foi necessária\n'
    u'apenas na **lista de projetos**, que estourou o limite (62.511 caracteres) e foi reduzida aos\n'
    u'campos mínimos sobre o arquivo salvo pelo próprio MCP.\n\n'
    u'A lista de projetos **foi** reconsultada ao vivo (`getVisibleJiraProjects`, `expandIssueTypes`)\n'
    u'e saiu idêntica à embutida: os mesmos **21 projetos** — `CREA`, `EG0232`, `EG0235`, `EG0239`,\n'
    u'`EG0240`, `EG0241`, `EG0256`, `EG0257`, `EG0272`, `EG0273`, `EG0274`, `EG0275`, `EG0285`,\n'
    u'`EG0286`, `EG0287`, `EG0292`, `EG0294`, `EG291`, `G0120`, `G0280` e `PE` — e a mesma dupla de\n'
    u'tipos de nível Epic (`Epic` e `Fluxo de trabalho`). A comparação foi feita por **MD5 do\n'
    u'conjunto normalizado** (chave, nome e tipos de issue com `hierarchyLevel`, ordenado por\n'
    u'chave): `505192b9c291…` ao vivo e em `snapshot-data.js`, idênticos.')

# ---- sem subagente nesta rodada ----
rep(u'A busca e a redução dos seis conjuntos foram delegadas a um subagente, para que as respostas\n'
    u'JQL completas não ocupassem o contexto da rotina. O subagente gravou apenas os seis arquivos\n'
    u'`_snap/*_2026-10.json`, revalidou cada um quanto a parseabilidade e formato, e não executou\n'
    u'nenhum comando `git`.',
    u'Nesta rodada as consultas foram feitas pela própria rotina, sem subagente: a projeção de seis\n'
    u'campos e a divisão do `lookahead` em metades bastaram para manter as respostas dentro do\n'
    u'limite, e só a lista de projetos precisou do desvio por arquivo. Nenhum comando `git` foi\n'
    u'executado — nem `add`, nem `commit`, nem `push`.')

rep(u'| Conjunto | SHA-256 (12 primeiros) | Bytes em disco |',
    u'| Conjunto | SHA-256 (12 primeiros) | Bytes em disco |')

rep(u'Os hashes acima são o SHA-256 dos **bytes dos arquivos em disco**, recipiente diferente do\n'
    u'usado nas tabelas de rodadas anteriores, que normalizavam os registros antes de somar; os\n'
    u'valores não são comparáveis com os de lá.',
    u'Os hashes acima são o SHA-256 dos **bytes dos arquivos em disco** e são os mesmos da rodada\n'
    u'das 16:32 — os arquivos não foram tocados nesta geração. Eles usam recipiente diferente do\n'
    u'das tabelas de rodadas mais antigas, que normalizavam os registros antes de somar; os valores\n'
    u'não são comparáveis com os de lá.')

# ---- demais conferencias ----
rep(u'- Os seis arquivos de out/2026 foram revalidados depois de gravados: todos parseiam como JSON,\n'
    u'  todos os registros têm exatamente as chaves `key` e `fields`, e `fields` exatamente os seis\n'
    u'  campos da projeção (`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`).\n'
    u'  Nenhuma ocorrência de `accountId`, `avatarUrls`, `emailAddress` ou de endereço de e-mail em\n'
    u'  qualquer deles.',
    u'- Os seis arquivos de out/2026 **não foram regravados** nesta rodada; foram lidos e conferidos\n'
    u'  contra as respostas ao vivo, registro a registro. Seguem parseando como JSON, com os mesmos\n'
    u'  tamanhos e SHA-256 da rodada anterior, e sem nenhuma ocorrência de `accountId`,\n'
    u'  `avatarUrls`, `emailAddress` ou de endereço de e-mail.')

rep(u'  *staging* de artifact (`device_stage_files` com `artifact_ids`) na geração das 15:31 e conferido\n'
    u'  contra a cópia local: mesmos 87.509 bytes e **MD5 idêntico** (`6a2b6462a4efbec1890af4494a7f0b74`),\n'
    u'  md5 reconferido nesta rodada por essa mesma via (`6a2b6462a4efbec1890af4494a7f0b74`,\n'
    u'  87.509 bytes) — a origem continua sendo, byte a byte, o artifact ao vivo. A recusa de leitura\n'
    u'  da pasta `Artifacts` por caminho de arquivo foi igualmente reconfirmada nesta rodada.',
    u'  *staging* de artifact (`device_stage_files` com `artifact_ids`) na geração das 15:31 e conferido\n'
    u'  contra a cópia local: mesmos 87.509 bytes e **MD5 idêntico** (`6a2b6462a4efbec1890af4494a7f0b74`).\n'
    u'  Nesta rodada o *staging* **não** foi refeito; a cópia local foi reconferida em disco e mantém\n'
    u'  os mesmos 87.509 bytes e o mesmo MD5. A recusa de leitura da pasta `Artifacts` por caminho de\n'
    u'  arquivo foi reconfirmada nesta rodada, em `device_list_dir` e em `ls`.')

rep(u'Os quatro indicadores repetem os das gerações de 00:33 e 01:31, sem nenhuma transição nova no\n'
    u'intervalo:',
    u'Os quatro indicadores repetem os da geração das 16:32, sem nenhuma transição nova no\n'
    u'intervalo:')

rep(u'A composição é a mesma das gerações anteriores; nesta rodada os seis conjuntos do mês\n'
    u'corrente foram regravados com as mesmas contagens.',
    u'A composição é a mesma das gerações anteriores; nesta rodada os seis conjuntos do mês\n'
    u'corrente foram conferidos ao vivo e preservados em disco, sem regravação.')

# ---- conferencia estrutural ----
rep(u'  arquivo), com o carimbo `2026-10-16T16:32:18-03:00`.',
    u'  arquivo), com o carimbo `2026-10-16T17:31:26-03:00`.')

rep(u'- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado\n'
    u'  (bloco injetado abre no byte 22.611 do `index.html` e `window.__SNAPSHOT__` é atribuído no\n'
    u'  byte 97.267, contra o byte 99.717 da atribuição `window.__HISTORY__=` do `<script>` próprio\n'
    u'  do artifact — ordem de execução confirmada).',
    u'- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado\n'
    u'  (bloco injetado abre no byte 22.561 do `index.html` e `window.__SNAPSHOT__` é atribuído no\n'
    u'  byte 96.638, contra o byte 99.088 da atribuição `window.__HISTORY__=` do `<script>` próprio\n'
    u'  do artifact — ordem de execução confirmada). O bloco embutido é, além disso, **byte a byte\n'
    u'  igual** ao `snapshot-data.js` gravado ao lado.')

rep(u'- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 16/10/2026 16:32,',
    u'- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 16/10/2026 17:31,')

rep(u'- Tamanhos da geração: `index.html` **164.972 bytes** e `snapshot-data.js` **77.186 bytes**,\n'
    u'  exatamente os da rodada das 15:30 — o conteúdo embutido é idêntico e o carimbo de geração\n'
    u'  tem comprimento fixo.',
    u'- Tamanhos da geração: `index.html` **164.972 bytes** e `snapshot-data.js` **77.186 bytes**,\n'
    u'  exatamente os da rodada das 16:32 — o conteúdo embutido é idêntico e o carimbo de geração\n'
    u'  tem comprimento fixo.\n'
    u'- Como nenhum dos seis conjuntos mudou e o HTML de origem está inalterado, esta geração\n'
    u'  **reaproveitou o `index.html` da rodada anterior e trocou apenas os carimbos** (as quatro\n'
    u'  ocorrências do ISO e a data do banner), em vez de remontar um arquivo idêntico a partir do\n'
    u'  `_artifact_src.html`. A estrutura foi reconferida depois da troca, item a item, como listado\n'
    u'  acima. Registre-se que o relógio da VM que executa os comandos no computador está em UTC: o\n'
    u'  carimbo foi calculado em BRT (UTC−3) e conferido no arquivo final.')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
