# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-07 ~16:30 UTC (07/10 13:30 BRT). Mes corrente: 2026-10.
# Filtro: issuetype in ("Epic","Fluxo de trabalho"). pageInfo.hasNextPage=false em todas as 6.
# getVisibleJiraProjects: total=21, isLast=true (identico a _projects_min.json, nao regravado).
# ARTIFACT_HTML (Artifacts\pr03-relatorio-indicadores-epics\index.html) segue inacessivel
# (protected location); base de geracao = _artifact_src.html versionado no repo.
# Datasets gerados no container via MCP+jq e trazidos como *.json.new; aqui so comparo e instalo.
import json, os, hashlib
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'
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
    if not ok: changed.append(name)
    print('%-10s %2d itens  old=%s new=%s %s' % (name, len(new), ho, hn, 'IGUAL' if ok else '*** ALTERADO ***'))
    json.dump(new, open(po, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    os.replace(pn, os.path.join(D, os.pardir, '_to_delete', '%s_%s.json.new' % (name, K)))
print('ALTERADOS:', ', '.join(changed) if changed else '(nenhum)')
