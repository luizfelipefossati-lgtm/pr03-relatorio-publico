# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-08 ~20:30 UTC (08/10 17:30 BRT). Mes corrente: 2026-10.
# Filtro: issuetype in ("Epic","Fluxo de trabalho"). pageInfo.hasNextPage=false nas 6 consultas.
# getVisibleJiraProjects: total=21, isLast=true -> md5 identico ao _projects_min.json em disco
# (441303882ffb1810eb9c6fb1337b974d); nenhuma regravacao necessaria.
# ARTIFACT_HTML (Artifacts\pr03-relatorio-indicadores-epics\index.html) continua inacessivel
# (protected location); HTML ao vivo obtido via device_stage_files(artifact_ids) e conferido
# por md5 contra _artifact_src.html => 6a2b6462a4efbec1890af4494a7f0b74 (identico).
import json, os, hashlib
D = os.path.dirname(os.path.abspath(__file__))
K = "2026-10"
def canon(items):
    return hashlib.sha256(json.dumps(sorted(items, key=lambda i: i['key']), sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:24]
changed = []
for name in ['planned','overdue','lookahead','sent','resolved','rework']:
    po = os.path.join(D, '%s_%s.json' % (name, K))
    pn = po + '.new'
    new = json.load(open(pn, encoding='utf-8'))
    old = json.load(open(po, encoding='utf-8')) if os.path.exists(po) else None
    ho = canon(old) if old is not None else '-'
    hn = canon(new)
    ok = (ho == hn)
    if not ok:
        changed.append(name)
        so, sn = {i['key'] for i in (old or [])}, {i['key'] for i in new}
        if so - sn: print('   - saiu  : %s' % ', '.join(sorted(so - sn)))
        if sn - so: print('   + entrou: %s' % ', '.join(sorted(sn - so)))
        if so == sn: print('   ~ mesmos keys, campos alterados')
    print('%-10s %2d itens (antes %s)  old=%s new=%s %s' % (
        name, len(new), len(old) if old is not None else '-', ho, hn, 'IGUAL' if ok else '*** ALTERADO ***'))
    json.dump(new, open(po, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    os.replace(pn, os.path.join(D, os.pardir, '_to_delete', '%s_%s.json.new' % (name, K)))
print('projects   21 itens  md5 identico -> IGUAL (nao regravado)')
print('ALTERADOS:', ', '.join(changed) if changed else '(nenhum)')
