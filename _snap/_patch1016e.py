# -*- coding: utf-8 -*-
"""Atualiza o README.md para a geracao das 18:32 de 16/10/2026."""
import io, os, sys

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()
orig = s

def rep(old, new, n=1):
    global s
    if s.count(old) != n:
        sys.exit('NAO ENCONTRADO (%d ocorrencias): %s' % (s.count(old), old[:140]))
    s = s.replace(old, new, n)

rep(u'> **Última atualização do snapshot: 16/10/2026 17:31** (`2026-10-16T17:31:26-03:00`)',
    u'> **Última atualização do snapshot: 16/10/2026 18:32** (`2026-10-16T18:32:17-03:00`)')

rep(u'Geração em 16/10/2026 17:31 BRT, com consulta ao vivo ao Jira via MCP Atlassian.',
    u'Geração em 16/10/2026 18:32 BRT, com consulta ao vivo ao Jira via MCP Atlassian.')

rep(u'Terceira geração da tarde de 16/10, cerca de **uma hora** depois da das 16:32. As **seis**',
    u'Quarta geração da tarde de 16/10, cerca de **uma hora** depois da das 17:31. As **seis**')

rep(u'| Conjunto | Ao vivo | Geração das 16:32 | Situação |',
    u'| Conjunto | Ao vivo | Geração das 17:31 | Situação |')

# ---- metodo desta rodada ----
rep(u'**Diferença de método em relação à rodada das 16:32:** lá os seis arquivos de `_snap/` foram\n'
    u'regravados e a conferência foi por contagem; aqui eles **foram preservados** e a conferência\n'
    u'voltou a ser **registro a registro**. Os 64 registros ao vivo (15 + 0 + 33 + 6 + 6 + 4) foram\n'
    u'comparados aos de disco chave a chave e campo a campo — `duedate`, nome de status e\n'
    u'`resolutiondate` —, sem nenhuma diferença, nenhuma chave nova e nenhuma chave ausente. Os\n'
    u'seis arquivos mantêm, byte a byte, os mesmos tamanhos e os mesmos SHA-256 publicados na\n'
    u'rodada anterior.',
    u'**Diferença de método em relação à rodada das 17:31:** o método de conferência é o mesmo —\n'
    u'arquivos **preservados** e comparação **registro a registro** —, mas a divisão do trabalho\n'
    u'mudou. O `planned_2026-10` foi consultado pela própria rotina; os outros cinco conjuntos\n'
    u'foram delegados a um **subagente**, para que as respostas JQL completas não ocupassem o\n'
    u'contexto da rotina. Os 64 registros ao vivo (15 + 0 + 33 + 6 + 6 + 4) foram comparados aos de\n'
    u'disco chave a chave e campo a campo — `duedate`, nome de status, categoria de status,\n'
    u'`resolutiondate`, `summary`, projeto e `updated` —, sem nenhuma diferença, nenhuma chave nova\n'
    u'e nenhuma chave ausente. Os seis arquivos mantêm, byte a byte, os mesmos tamanhos e os mesmos\n'
    u'SHA-256 publicados na rodada anterior.')

# ---- lookahead em metades + lista de projetos nao reconsultada ----
rep(u'As respostas vieram completas (`pageInfo.hasNextPage = false`), sem timeouts e sem nenhum\n'
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
    u'chave): `505192b9c291…` ao vivo e em `snapshot-data.js`, idênticos.',
    u'As seis respostas vieram completas (`pageInfo.hasNextPage = false`), sem paginação pendente,\n'
    u'sem timeouts e sem nenhum `502`. O `lookahead_2026-10` foi novamente consultado em **duas\n'
    u'metades** (`duedate` em nov/2026 e em dez/2026, 11 + 22 = 33), o que manteve as respostas\n'
    u'abaixo do limite de tokens e dispensou a extração por arquivo. A projeção de seis campos\n'
    u'(`summary`, `status`, `project`, `duedate`, `resolutiondate`, `updated`) foi aplicada em todas\n'
    u'as consultas.\n\n'
    u'A lista de projetos **não foi reconsultada** nesta rodada: o `_projects_min.json` de 14/10\n'
    u'(21 projetos) segue como fonte dos nomes de projeto e dos tipos de nível Epic (`Epic`,\n'
    u'`Fluxo de trabalho`) usados no predicado, e os 21 projetos embutidos no `snapshot-data.js`\n'
    u'não foram alterados. A reconsulta ao vivo da rodada das 17:31, que os confirmou um a um,\n'
    u'continua valendo como última verificação dessa lista.')

# ---- subagente + git ----
rep(u'Nesta rodada as consultas foram feitas pela própria rotina, sem subagente: a projeção de seis\n'
    u'campos e a divisão do `lookahead` em metades bastaram para manter as respostas dentro do\n'
    u'limite, e só a lista de projetos precisou do desvio por arquivo. Do lado do `git`, a rotina\n'
    u'executou apenas leituras de estado (`git status`, `git log`) para confirmar a integridade do\n'
    u'repositório: nenhum `add`, `commit` ou `push`, e nenhuma tentativa de autenticação.',
    u'A busca e a redução de cinco dos seis conjuntos foram delegadas a um subagente, que gravou\n'
    u'apenas o seu relatório de comparação — nenhum arquivo de `_snap/` foi tocado, porque não\n'
    u'houve diferença a registrar — e não executou nenhum comando `git`. Do lado do `git`, esta\n'
    u'rodada não executou **nenhum** comando, nem de leitura: a única inspeção de estado foi a\n'
    u'leitura do `.push-watchdog.log`. Nenhum `add`, `commit` ou `push`, e nenhuma tentativa de\n'
    u'autenticação.')

rep(u'Os hashes acima são o SHA-256 dos **bytes dos arquivos em disco** e são os mesmos da rodada\n'
    u'das 16:32 — os arquivos não foram tocados nesta geração.',
    u'Os hashes acima são o SHA-256 dos **bytes dos arquivos em disco** e são os mesmos da rodada\n'
    u'das 17:31 — os arquivos não foram tocados nesta geração.')

# ---- fonte do HTML: staging refeito nesta rodada ----
rep(u'  *staging* de artifact (`device_stage_files` com `artifact_ids`) na geração das 15:31 e conferido\n'
    u'  contra a cópia local: mesmos 87.509 bytes e **MD5 idêntico** (`6a2b6462a4efbec1890af4494a7f0b74`).\n'
    u'  Nesta rodada o *staging* **não** foi refeito; a cópia local foi reconferida em disco e mantém\n'
    u'  os mesmos 87.509 bytes e o mesmo MD5. A recusa de leitura da pasta `Artifacts` por caminho de\n'
    u'  arquivo foi reconfirmada nesta rodada, em `device_list_dir` e em `ls`.',
    u'  *staging* de artifact (`device_stage_files` com `artifact_ids`), **refeito nesta rodada**, e\n'
    u'  conferido contra a cópia local: mesmos **87.509 bytes** e **MD5 idêntico**\n'
    u'  (`6a2b6462a4efbec1890af4494a7f0b74`). O inventário de artifacts confirma que o\n'
    u'  `pr03-relatorio-indicadores-epics` continua com `updatedAt` de **27/07/2026**. A recusa de\n'
    u'  leitura da pasta `Artifacts` por caminho de arquivo foi reconfirmada nesta rodada, em `ls`.')

rep(u'Os quatro indicadores repetem os da geração das 16:32, sem nenhuma transição nova no\n'
    u'intervalo:',
    u'Os quatro indicadores repetem os da geração das 17:31, sem nenhuma transição nova no\n'
    u'intervalo:')

# ---- conferencia estrutural ----
rep(u'  arquivo), com o carimbo `2026-10-16T17:31:26-03:00`.',
    u'  arquivo), com o carimbo `2026-10-16T18:32:17-03:00`.')

rep(u'- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado\n'
    u'  (bloco injetado abre no byte 22.561 do `index.html` e `window.__SNAPSHOT__` é atribuído no\n'
    u'  byte 96.638, contra o byte 99.088 da atribuição `window.__HISTORY__=` do `<script>` próprio\n'
    u'  do artifact — ordem de execução confirmada). O bloco embutido é, além disso, **byte a byte\n'
    u'  igual** ao `snapshot-data.js` gravado ao lado.',
    u'- Bloco `window.__SNAPSHOT__` injetado **antes** do script principal do artifact: confirmado\n'
    u'  (o comentário de cabeçalho do bloco injetado começa no byte 22.531 do `index.html` e\n'
    u'  `window.__SNAPSHOT__` é atribuído no byte 97.267, contra o byte 99.717 da atribuição\n'
    u'  `window.__HISTORY__=` do `<script>` próprio do artifact — ordem de execução confirmada).\n'
    u'  O bloco embutido é, além disso, **byte a byte igual** ao `snapshot-data.js` gravado ao lado\n'
    u'  (MD5 `b1ad41bc1819…` nos dois).')

rep(u'- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 16/10/2026 17:31,',
    u'- Banner de snapshot como **último elemento do `<body>`**, com o carimbo 16/10/2026 18:32,')

rep(u'- Tamanhos da geração: `index.html` **164.972 bytes** e `snapshot-data.js` **77.186 bytes**,\n'
    u'  exatamente os da rodada das 16:32 — o conteúdo embutido é idêntico e o carimbo de geração\n'
    u'  tem comprimento fixo.',
    u'- Tamanhos da geração: `index.html` **164.972 bytes** e `snapshot-data.js` **77.186 bytes**,\n'
    u'  exatamente os da rodada das 17:31 — o conteúdo embutido é idêntico e o carimbo de geração\n'
    u'  tem comprimento fixo.\n'
    u'- Contagens dos conjuntos **embutidos** no `snapshot-data.js` lidas de volta do arquivo\n'
    u'  publicado e conferidas uma a uma contra as de `_snap/`: `planned_2026-10` 15,\n'
    u'  `overdue_2026-10` 0, `lookahead_2026-10` 33, `sent_2026-10` 6, `resolved_2026-10` 6,\n'
    u'  `rework_2026-10` 4, e a acumulada `planned` de mai a set/2026 em 7, 1, 10, 4 e 8.')

# ---- nota de publicacao ----
rep(u'> **Nota de publicação (16/10/2026, 17:31).** A cadeia de publicação está íntegra: as três\n'
    u'> passagens mais recentes do watchdog — 17:04, 17:14 e 17:24 — concluíram todas com\n'
    u'> sucesso, em cadência regular de 10 minutos, a última com `Commit OK: 1bcabf9` e `Push OK e\n'
    u'> VERIFICADO: HEAD sincronizado com origin/main`. Esta geração entra na passagem seguinte,\n'
    u'> prevista para ~17:34.',
    u'> **Nota de publicação (16/10/2026, 18:32).** A cadeia de publicação está íntegra: as três\n'
    u'> passagens mais recentes do watchdog — 18:04, 18:14 e 18:24 — concluíram todas com\n'
    u'> sucesso, em cadência regular de 10 minutos, a última com `Commit OK: 2728daf` e `Push OK e\n'
    u'> VERIFICADO: HEAD sincronizado com origin/main`. Esta geração entra na passagem seguinte,\n'
    u'> prevista para ~18:34.')

if s == orig:
    sys.exit('ERRO: nada mudou.')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('README atualizado:', len(s.encode('utf-8')), 'bytes')
