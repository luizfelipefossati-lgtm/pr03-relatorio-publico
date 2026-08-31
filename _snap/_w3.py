# -*- coding: utf-8 -*-
"""Expande tuplas compactas em issues no formato do artifact e grava _snap/<name>.json
Uso: python3 _w3.py <name> <<< '[[key,summary,statusName,statusCat,duedate,resdate,updated], ...]'
"""
import json, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
PROJ = {p['key']: p['name'] for p in json.load(open(os.path.join(BASE, '..', '_projects_min.json'), encoding='utf-8'))}
name = sys.argv[1]
rows = json.load(sys.stdin)
out = []
for r in rows:
    k, sm, st, sc, du, rd, up = r
    pk = k.rsplit('-', 1)[0]
    if pk not in PROJ:
        sys.exit('ERRO: projeto desconhecido para %s (%s)' % (k, pk))
    out.append({'key': k, 'fields': {'summary': sm,
        'status': {'name': st, 'statusCategory': {'key': sc}},
        'project': {'key': pk, 'name': PROJ[pk]},
        'duedate': du, 'resolutiondate': rd, 'updated': up}})
p = os.path.join(BASE, name + '.json')
json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('OK %-24s %d issues  %d bytes' % (name, len(out), os.path.getsize(p)))
