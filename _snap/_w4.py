# -*- coding: utf-8 -*-
"""Le TSV do stdin e grava _snap/<dataset>.json no formato minimal.
Colunas: key<TAB>summary<TAB>status_name<TAB>status_cat<TAB>proj_key<TAB>proj_name<TAB>duedate<TAB>resolutiondate<TAB>updated
Use '-' para null. Linhas vazias ignoradas."""
import json, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
name = sys.argv[1]
out = []
for line in sys.stdin.read().split('\n'):
    if not line.strip():
        continue
    c = line.split('\t')
    assert len(c) == 9, (len(c), c)
    n = lambda v: None if v == '-' else v
    out.append({'key': c[0], 'fields': {
        'summary': c[1],
        'status': {'name': c[2], 'statusCategory': {'key': c[3]}},
        'project': {'key': c[4], 'name': c[5]},
        'duedate': n(c[6]), 'resolutiondate': n(c[7]), 'updated': n(c[8])}})
p = os.path.join(BASE, name + '.json')
json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('OK %-22s %d issues %d bytes' % (name, len(out), os.path.getsize(p)))
