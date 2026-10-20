# -*- coding: utf-8 -*-
"""Converte os conjuntos planos (key/status_name/project_key...) para a forma
aninhada que o script do artifact consome (key/fields/status/project)."""
import json, io

FILES = ['planned_2026-10','overdue_2026-10','lookahead_2026-10',
         'sent_2026-10','resolved_2026-10','rework_2026-10']

def nest(r):
    if 'fields' in r:            # ja aninhado
        return r
    return {
        'key': r['key'],
        'fields': {
            'summary': r.get('summary'),
            'status': {'name': r.get('status_name'),
                       'statusCategory': {'key': r.get('status_cat')}},
            'project': {'key': r.get('project_key'), 'name': r.get('project_name')},
            'duedate': r.get('duedate'),
            'resolutiondate': r.get('resolutiondate'),
            'updated': r.get('updated'),
        },
    }

for name in FILES:
    p = name + '.json'
    data = json.load(io.open(p, encoding='utf-8'))
    conv = [nest(r) for r in data]
    with io.open(p, 'w', encoding='utf-8') as f:
        json.dump(conv, f, ensure_ascii=False)
    print(name, len(conv), 'convertido' if data and 'fields' not in data[0] else 'ja ok')
