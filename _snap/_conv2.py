# -*- coding: utf-8 -*-
"""Converte um arquivo bruto de tool-result do MCP Atlassian em JSON minimal.
Uso: python3 _conv2.py <arquivo_bruto> <nome_dataset>
Grava _snap/<nome_dataset>.json
"""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src, name = sys.argv[1], sys.argv[2]
raw = json.load(open(src, encoding='utf-8'))
nodes = raw.get('issues', {}).get('nodes', []) or []
out = []
for i in nodes:
    f = i.get('fields', {}) or {}
    st = f.get('status') or {}
    pj = f.get('project') or {}
    out.append({'key': i['key'], 'fields': {
        'summary': f.get('summary') or '',
        'status': {'name': st.get('name'),
                   'statusCategory': {'key': (st.get('statusCategory') or {}).get('key')}},
        'project': {'key': pj.get('key'), 'name': pj.get('name')},
        'duedate': f.get('duedate'),
        'resolutiondate': f.get('resolutiondate'),
        'updated': f.get('updated')}})
p = os.path.join(BASE, name + '.json')
json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('OK %-24s %d issues  %d bytes' % (name, len(out), os.path.getsize(p)))
