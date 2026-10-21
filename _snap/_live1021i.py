# -*- coding: utf-8 -*-
"""Gera o snapshot estatico PR.03 (rodada 2026-10-21 ~09:3x UTC / 06:3x BRT)."""
import json, os, re, io, datetime

REPO = os.path.join(os.environ['HOME'], 'mnt', 'pr03-relatorio-publico')
SNAPDIR = os.path.join(REPO, '_snap')
PAY = json.load(io.open(os.path.join(SNAPDIR, '_payload_2026-10-21i.json'), encoding='utf-8'))

# grava os JSONs minimais individuais (reuso em retries)
for name, rows in PAY['datasets'].items():
    with io.open(os.path.join(SNAPDIR, name + '.json'), 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)
with io.open(os.path.join(SNAPDIR, 'projects_min_2026-10-21i.json'), 'w', encoding='utf-8') as f:
    json.dump(PAY['projects'], f, ensure_ascii=False)

prev = io.open(os.path.join(REPO, 'snapshot-data.js'), encoding='utf-8').read()
i = prev.index('var SNAP = ') + len('var SNAP = '); j = prev.index('var DATASETS')
PREV_SNAP = json.loads(prev[i:j].rstrip().rstrip(';'))
i2 = prev.index('var DATASETS = ') + len('var DATASETS = '); j2 = prev.index('var PATTERNS')
PREV_DS = json.loads(prev[i2:j2].rstrip().rstrip(';'))

PROJECTS = PAY['projects']
prev_keys = sorted(p['key'] for p in PREV_SNAP['projects'])
new_keys = sorted(p['key'] for p in PROJECTS)
if prev_keys != new_keys:
    print('AVISO: lista de projetos mudou. +%s  -%s' % (
        sorted(set(new_keys) - set(prev_keys)), sorted(set(prev_keys) - set(new_keys))))
PROJECTS.sort(key=lambda p: p.get('name') or '')

epic_types = sorted({t['name'] for p in PROJECTS for t in p.get('issueTypes', [])
                     if t.get('hierarchyLevel') == 1})

DATASETS = {}
for k in ('rework_2026-10', 'sent_2026-10', 'resolved_2026-10', 'overdue_2026-10',
          'lookahead_2026-10', 'planned_2026-05', 'planned_2026-06', 'planned_2026-10'):
    DATASETS[k] = PAY['datasets'][k]
for k in ('planned_2026-07', 'planned_2026-08', 'planned_2026-09'):
    DATASETS[k] = PREV_DS[k]

# diff vs rodada anterior
for k in sorted(DATASETS):
    a = sorted(x['key'] for x in PREV_DS.get(k, []))
    b = sorted(x['key'] for x in DATASETS[k])
    if a != b:
        print('MUDOU %s: +%s -%s' % (k, sorted(set(b)-set(a)), sorted(set(a)-set(b))))

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
ISO = now.strftime('%Y-%m-%dT%H:%M:%S-03:00')
BR  = now.strftime('%d/%m/%Y %H:%M')

SNAP = {
    'generated': now.strftime('%Y-%m-%d'),
    'generatedAt': ISO,
    'epicTypeNames': epic_types,
    'projects': PROJECTS,
    'months': PREV_SNAP['months'],
}

PATTERNS = [
 ('rework_2026-10',    r'DURING \("2026-10-01","2026-10-31"\)[\s\S]*changed from'),
 ('sent_2026-10',      r'DURING \("2026-10-01","2026-10-31"\)'),
 ('resolved_2026-10',  r'resolved>="2026-10-01"[\s\S]*resolved<="2026-10-31"'),
 ('overdue_2026-10',   r'duedate<"2026-10-01"[\s\S]*statusCategory!=Done'),
 ('lookahead_2026-10', r'duedate>="2026-11-01"[\s\S]*duedate<="2026-12-31"'),
 ('planned_2026-05',   r'duedate>="2026-05-01"[\s\S]*duedate<="2026-05-31"'),
 ('planned_2026-06',   r'duedate>="2026-06-01"[\s\S]*duedate<="2026-06-30"'),
 ('planned_2026-07',   r'duedate>="2026-07-01"[\s\S]*duedate<="2026-07-31"'),
 ('planned_2026-08',   r'duedate>="2026-08-01"[\s\S]*duedate<="2026-08-31"'),
 ('planned_2026-09',   r'duedate>="2026-09-01"[\s\S]*duedate<="2026-09-30"'),
 ('planned_2026-10',   r'duedate>="2026-10-01"[\s\S]*duedate<="2026-10-31"'),
]
pat_js = '[' + ','.join('{n:%s,re:new RegExp(%s)}' % (json.dumps(n), json.dumps(r)) for n, r in PATTERNS) + ']'

TPL = u'''<script>
/* =========================================================================
   PR.03 - Relatorio de Indicadores de EPICs - DADOS ESTATICOS DO SNAPSHOT
   Gerado em: {ISO}
   Fonte: Jira Cloud ead785de-33f3-4746-9bdb-a2a58cf5213b (projetos-engeplus)
   Dados pre-buscados do Jira. A pagina NAO consulta o Jira ao vivo.
   Nao contem accountIds, e-mails nem avatares.
   ========================================================================= */
(function () {{
  'use strict';

  var SNAP = {SNAP};

  var DATASETS = {DS};

  var PATTERNS = {PAT};

  window.__SNAPSHOT__ = SNAP;
  SNAP.datasets = DATASETS;

  var _hist = {{}};
  (window.__HISTORY__ && typeof window.__HISTORY__ === 'object') &&
    Object.keys(window.__HISTORY__).forEach(function (k) {{ _hist[k] = window.__HISTORY__[k]; }});
  Object.keys(SNAP.months).forEach(function (k) {{ _hist[k] = SNAP.months[k]; }});
  try {{
    Object.defineProperty(window, '__HISTORY__', {{
      configurable: true,
      enumerable: true,
      get: function () {{ return _hist; }},
      set: function (v) {{
        if (v && typeof v === 'object') {{
          Object.keys(v).forEach(function (k) {{
            if (!Object.prototype.hasOwnProperty.call(SNAP.months, k)) _hist[k] = v[k];
          }});
        }}
      }}
    }});
  }} catch (e) {{
    window.__HISTORY__ = _hist;
    console.warn('[PR03] defineProperty indisponivel; __HISTORY__ pode ser sobrescrito.', e);
  }}

  function wrap(o) {{
    return {{ content: [{{ type: 'text', text: JSON.stringify(o) }}], structuredContent: o, isError: false }};
  }}
  function issues(list) {{
    return wrap({{ issues: {{ nodes: list || [], pageInfo: {{ hasNextPage: false, endCursor: null }} }} }});
  }}
  function resolveJql(jql) {{
    var q = String(jql || '');
    for (var i = 0; i < PATTERNS.length; i++) {{
      if (PATTERNS[i].re.test(q)) return DATASETS[PATTERNS[i].n] || [];
    }}
    console.warn('[PR03] JQL sem correspondencia no snapshot:', q);
    return [];
  }}

  window.cowork = window.cowork || {{}};
  window.cowork.callMcpTool = function (name, args) {{
    var n = String(name || '');
    if (n.indexOf('getVisibleJiraProjects') !== -1) {{
      return Promise.resolve(wrap({{ values: SNAP.projects, total: SNAP.projects.length, isLast: true }}));
    }}
    if (n.indexOf('searchJiraIssuesUsingJql') !== -1) {{
      return Promise.resolve(issues(resolveJql(args && args.jql)));
    }}
    return Promise.resolve(wrap({{}}));
  }};
  window.cowork.askClaude = function () {{ return Promise.resolve(''); }};
  window.cowork.runScheduledTask = function () {{ return Promise.resolve(null); }};

  console.log('[PR03] Snapshot estatico carregado - gerado em {ISO}; consultas ao Jira desativadas.');
}})();
</script>
'''

block = TPL.format(
    ISO=ISO,
    SNAP=json.dumps(SNAP, ensure_ascii=False, separators=(',', ':')),
    DS=json.dumps(DATASETS, ensure_ascii=False, separators=(',', ':')),
    PAT=pat_js,
)

with io.open(os.path.join(REPO, 'snapshot-data.js'), 'w', encoding='utf-8') as f:
    f.write(block)

html = io.open(os.path.join(REPO, 'index.html'), encoding='utf-8').read()
html, n1 = re.subn(r'<!-- Snapshot gerado em [^>]*-->',
                   '<!-- Snapshot gerado em %s -->' % ISO, html, count=1)
assert n1 == 1, 'comentario de snapshot nao encontrado'
start = html.index('<script>\n/* ====')
assert 'DADOS ESTATICOS DO SNAPSHOT' in html[start:start + 400], 'bloco de snapshot nao localizado'
end = html.index('</script>', start) + len('</script>\n')
html = html[:start] + block + html[end:]

BANNER = ('<div style="background:#fef3c7;padding:8px;text-align:center;font-size:12px;'
          'color:#92400e;margin-top:24px">Snapshot estatico - ultima atualizacao: %s '
          '(dados travados, pagina nao consulta o Jira ao vivo)</div>' % BR)
html = re.sub(r'<div style="background:#fef3c7;[^>]*>Snapshot estatico[^<]*</div>\n?', '', html)
html = html.replace('</body>', BANNER + '\n</body>', 1)

with io.open(os.path.join(REPO, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print('ISO', ISO, '| BR', BR)
print('epicTypes', epic_types, '| projects', len(PROJECTS))
print('snapshot-data.js', os.path.getsize(os.path.join(REPO, 'snapshot-data.js')))
print('index.html', os.path.getsize(os.path.join(REPO, 'index.html')))
for k in sorted(DATASETS):
    print('  ', k, len(DATASETS[k]))
