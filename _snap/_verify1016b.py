# -*- coding: utf-8 -*-
"""Conferencia estrutural do index.html gerado."""
import io, os, re, sys, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
R = lambda n: io.open(os.path.join(BASE, n), encoding='utf-8').read()
idx, snap, src = R('index.html'), R('snapshot-data.js'), R('_artifact_src.html')
fail = []
def chk(cond, msg):
    print(('  OK  ' if cond else ' FALHA ') + msg)
    if not cond: fail.append(msg)

iso = re.search(r'<!-- Snapshot gerado em ([0-9T:\-]+) -->', idx)
chk(bool(iso), 'comentario "Snapshot gerado em" presente no topo do head')
ISO = iso.group(1) if iso else ''
chk(idx.index('<!-- Snapshot gerado em') < 2000, 'comentario esta no inicio do documento')

chk(snap in idx, 'conteudo de snapshot-data.js embutido no index.html, integro')
chk(idx.count(ISO) == 4, 'carimbo ISO %s aparece 4x (comentario, SNAP, generatedAt, console.log) -> %d' % (ISO, idx.count(ISO)))

BAN = re.search(r'<div style="background:#fef3c7[^>]*>Snapshot estatico - ultima atualizacao: ([0-9/ :]+) \(dados travados[^<]*</div>', idx)
chk(bool(BAN), 'banner de snapshot presente')
tail = idx[idx.rindex('</div>'):]
chk(tail.strip() == '</div>\n</body>\n</html>' or re.match(r'^</div>\s*</body>\s*</html>\s*$', tail), 'banner e o ultimo elemento do <body> (nao no topo)')

br = BAN.group(1) if BAN else ''
chk(br[:10] == ISO[8:10] + '/' + ISO[5:7] + '/' + ISO[0:4] and br[11:16] == ISO[11:16],
    'carimbo do banner (%s) bate com o ISO (%s)' % (br, ISO))

# index.html == artifact original + script do snapshot + banner
rebuilt = idx.replace(snap, '', 1)
rebuilt = re.sub(r'<!-- Snapshot gerado em [0-9T:\-]+ -->\n?', '', rebuilt, count=1)
rebuilt = re.sub(r'<div style="background:#fef3c7.*?</div>\n?', '', rebuilt, count=1, flags=re.S)
chk(rebuilt == src, 'index.html = artifact original (_artifact_src.html) + snapshot + banner, sem outras alteracoes')

# privacidade -- ignora o cabecalho de comentario, que cita 'accountIds' em texto
seg = snap[snap.index('(function ()'):]
for termo in ['accountId', 'avatarUrl', 'emailAddress', '@engeplus', 'displayName']:
    chk(termo not in seg, 'sem "%s" nos dados do snapshot' % termo)

# dados
i = seg.index('var DATASETS = ') + len('var DATASETS = ')
ds = json.loads(seg[i:seg.index('\n', i)].rstrip().rstrip(';'))
i = seg.index('var SNAP = ') + len('var SNAP = ')
sn = json.loads(seg[i:seg.index('\n', i)].rstrip().rstrip(';'))
chk(len(sn['projects']) == 21, 'lista de projetos com 21 entradas -> %d' % len(sn['projects']))
chk(sorted(sn['months']) == ['2026-07', '2026-08', '2026-09'], 'meses congelados: %s' % sorted(sn['months']))
chk(sn['generatedAt'] == ISO, 'SNAP.generatedAt == carimbo do comentario')
for k in ['planned_2026-10','overdue_2026-10','lookahead_2026-10','sent_2026-10','resolved_2026-10','rework_2026-10']:
    print('       %-20s %d registros' % (k, len(ds[k])))
chk('window.cowork.callMcpTool' in seg, 'callMcpTool sobrescrito (pagina nao consulta o Jira)')

print('\nRESULTADO:', 'tudo conferido' if not fail else '%d FALHA(S)' % len(fail))
sys.exit(1 if fail else 0)
