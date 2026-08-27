# -*- coding: utf-8 -*-
"""Gera index.html estatico (snapshot) a partir de _artifact_src.html + _snap/*.json."""
import json, os, re, sys, datetime, calendar

BASE = os.path.dirname(os.path.abspath(__file__))
SNAPDIR = os.path.join(BASE, '_snap')
MO = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

TZ = datetime.timezone(datetime.timedelta(hours=-3))
NOW = datetime.datetime.now(TZ)
STAMP_ISO = NOW.strftime('%Y-%m-%dT%H:%M:%S-03:00')
STAMP_BR  = NOW.strftime('%d/%m/%Y %H:%M')
TODAY = NOW.strftime('%Y-%m-%d')

CUR = (NOW.year, NOW.month)
PREV = (NOW.year, NOW.month - 1) if NOW.month > 1 else (NOW.year - 1, 12)
def mk(t): return '%04d-%02d' % t
CURK, PREVK = mk(CUR), mk(PREV)

def ds(name):
    p = os.path.join(SNAPDIR, name + '.json')
    if not os.path.exists(p): return None
    return json.load(open(p, encoding='utf-8'))

def last_day(y, m): return calendar.monthrange(y, m)[1]

# ---------- datasets ----------
DATASETS, missing = {}, []
acum_months = []
for off in range(5, -1, -1):
    y, m = NOW.year, NOW.month - off
    while m <= 0: m += 12; y -= 1
    acum_months.append((y, m))

names = []
for (y, m) in [PREV, CUR]:
    k = '%04d-%02d' % (y, m)
    names += ['planned_'+k, 'overdue_'+k, 'lookahead_'+k, 'sent_'+k, 'resolved_'+k, 'rework_'+k]
for (y, m) in acum_months:
    n = 'planned_%04d-%02d' % (y, m)
    if n not in names: names.append(n)

for n in names:
    d = ds(n)
    if d is None: missing.append(n)
    else: DATASETS[n] = d
if missing:
    sys.exit('ERRO: datasets ausentes em _snap/: ' + ', '.join(missing))

# ---------- meses congelados (mes anterior) ----------
def build_month(y, m):
    k = '%04d-%02d' % (y, m)
    s = '%s-01' % k
    e = '%s-%02d' % (k, last_day(y, m))
    sent = DATASETS['sent_'+k]
    res  = DATASETS['resolved_'+k]
    rw   = {i['key'] for i in DATASETS['rework_'+k]}
    seen, allsent = set(), []
    for i in sent + res:
        if i['key'] in seen: continue
        seen.add(i['key']); allsent.append(i)
    det = [{'key': i['key'], 'sm': i['fields'].get('summary') or '',
            'pj': i['fields']['project']['key'], 'rw': i['key'] in rw} for i in allsent]
    det.sort(key=lambda d: 0 if d['rw'] else 1)
    return {
        'planned': DATASETS['planned_'+k],
        'overdue': DATASETS['overdue_'+k],
        'sent': {'total': len(allsent), 'rework': len(rw & seen), 'details': det},
        'look': DATASETS['lookahead_'+k],
        'period': {'s': s, 'e': e, 'l': MO[m-1] + ' ' + str(y), 'm': m-1, 'y': y},
        '_frozen_at': TODAY,
        '_note': 'Dados congelados no fechamento do período. Alterações no Jira após %s não afetam este relatório.' % e,
    }

MONTHS = {PREVK: build_month(*PREV)}

projects = json.load(open(os.path.join(BASE, '_projects_min.json'), encoding='utf-8'))
projects.sort(key=lambda p: p.get('name') or '')
epic_types = sorted({it['name'] for p in projects for it in p.get('issueTypes', [])
                     if it.get('hierarchyLevel') == 1})

SNAP = {'generated': TODAY, 'generatedAt': STAMP_ISO, 'epicTypeNames': epic_types,
        'projects': projects, 'months': MONTHS}

# ---------- patterns (ordem importa: mais especifico primeiro) ----------
pats = []
# Os padroes sao montados como regex "cru" em Python e serializados com json.dumps,
# que cuida de escapar barras e aspas para o literal de string do JavaScript.
for (y, m) in [PREV, CUR]:
    k = '%04d-%02d' % (y, m); ld = last_day(y, m)
    pats.append(('rework_'+k, r'DURING \("{k}-01","{k}-{ld:02d}"\)[\s\S]*changed from'.format(k=k, ld=ld)))
for (y, m) in [PREV, CUR]:
    k = '%04d-%02d' % (y, m); ld = last_day(y, m)
    pats.append(('sent_'+k, r'DURING \("{k}-01","{k}-{ld:02d}"\)'.format(k=k, ld=ld)))
    pats.append(('resolved_'+k, r'resolved>="{k}-01"[\s\S]*resolved<="{k}-{ld:02d}"'.format(k=k, ld=ld)))
    pats.append(('overdue_'+k, r'duedate<"{k}-01"[\s\S]*statusCategory!=Done'.format(k=k)))
    # lookahead do artifact: do 1o dia do mes seguinte ao ultimo dia de (mes + 2)
    ly, lm = (y, m + 1) if m < 12 else (y + 1, 1)
    ey, em = (y, m + 2) if m <= 10 else (y + 1, m + 2 - 12)
    pats.append(('lookahead_'+k,
                 r'duedate>="{ly:04d}-{lm:02d}-01"[\s\S]*duedate<="{ey:04d}-{em:02d}-{eld:02d}"'.format(
                     ly=ly, lm=lm, ey=ey, em=em, eld=last_day(ey, em))))
for (y, m) in acum_months:
    k = '%04d-%02d' % (y, m); ld = last_day(y, m)
    pats.append(('planned_'+k, r'duedate>="{k}-01"[\s\S]*duedate<="{k}-{ld:02d}"'.format(k=k, ld=ld)))

J = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))

script = '''<script>
/* =========================================================================
   PR.03 - Relatorio de Indicadores de EPICs - DADOS ESTATICOS DO SNAPSHOT
   Gerado em: %(stamp)s
   Fonte: Jira Cloud ead785de-33f3-4746-9bdb-a2a58cf5213b (projetos-engeplus)
   Dados pre-buscados do Jira. A pagina NAO consulta o Jira ao vivo.
   Nao contem accountIds, e-mails nem avatares.
   ========================================================================= */
(function () {
  'use strict';

  var SNAP = %(snap)s;

  var DATASETS = %(datasets)s;

  var PATTERNS = [%(patterns)s];

  window.__SNAPSHOT__ = SNAP;
  SNAP.datasets = DATASETS;

  // __HISTORY__ com merge defensivo: o script do artifact faz
  // "window.__HISTORY__ = {...}" (atribuicao direta), o que apagaria os meses
  // congelados do snapshot. O accessor abaixo mescla em vez de sobrescrever,
  // e o snapshot tem precedencia sobre as chaves proprias.
  var _hist = {};
  (window.__HISTORY__ && typeof window.__HISTORY__ === 'object') &&
    Object.keys(window.__HISTORY__).forEach(function (k) { _hist[k] = window.__HISTORY__[k]; });
  Object.keys(SNAP.months).forEach(function (k) { _hist[k] = SNAP.months[k]; });
  try {
    Object.defineProperty(window, '__HISTORY__', {
      configurable: true,
      enumerable: true,
      get: function () { return _hist; },
      set: function (v) {
        if (v && typeof v === 'object') {
          Object.keys(v).forEach(function (k) {
            if (!Object.prototype.hasOwnProperty.call(SNAP.months, k)) _hist[k] = v[k];
          });
        }
      }
    });
  } catch (e) {
    window.__HISTORY__ = _hist;
    console.warn('[PR03] defineProperty indisponivel; __HISTORY__ pode ser sobrescrito.', e);
  }

  function wrap(o) {
    return { content: [{ type: 'text', text: JSON.stringify(o) }], structuredContent: o, isError: false };
  }
  function issues(list) {
    return wrap({ issues: { nodes: list || [], pageInfo: { hasNextPage: false, endCursor: null } } });
  }
  function resolveJql(jql) {
    var q = String(jql || '');
    for (var i = 0; i < PATTERNS.length; i++) {
      if (PATTERNS[i].re.test(q)) return DATASETS[PATTERNS[i].n] || [];
    }
    console.warn('[PR03] JQL sem correspondencia no snapshot:', q);
    return [];
  }

  window.cowork = window.cowork || {};
  window.cowork.callMcpTool = function (name, args) {
    var n = String(name || '');
    if (n.indexOf('getVisibleJiraProjects') !== -1) {
      return Promise.resolve(wrap({ values: SNAP.projects, total: SNAP.projects.length, isLast: true }));
    }
    if (n.indexOf('searchJiraIssuesUsingJql') !== -1) {
      return Promise.resolve(issues(resolveJql(args && args.jql)));
    }
    return Promise.resolve(wrap({}));
  };
  window.cowork.askClaude = function () { return Promise.resolve(''); };
  window.cowork.runScheduledTask = function () { return Promise.resolve(null); };

  console.log('[PR03] Snapshot estatico carregado - gerado em %(stamp)s; consultas ao Jira desativadas.');
})();
</script>
''' % {
    'stamp': STAMP_ISO,
    'snap': J(SNAP),
    'datasets': J(DATASETS),
    'patterns': ','.join('{n:%s,re:new RegExp(%s)}' % (J(n), J(rx)) for n, rx in pats),
}

open(os.path.join(BASE, 'snapshot-data.js'), 'w', encoding='utf-8').write(script)

# ---------- injecao no HTML ----------
src = open(os.path.join(BASE, '_artifact_src.html'), encoding='utf-8').read()
if '__SNAPSHOT__' in src:
    sys.exit('ERRO: _artifact_src.html ja contem snapshot; use o artifact limpo.')

out = src.replace('<head>', '<head>\n<!-- Snapshot gerado em %s -->' % STAMP_ISO, 1)

# o snapshot precisa rodar ANTES do script principal do artifact
anchor = '<script>\nwindow.__HISTORY__='
idx = out.find(anchor)
if idx == -1:
    idx = out.find('<script>\n/* ========== CONSTANTS ========== */')
if idx == -1:
    sys.exit('ERRO: nao encontrei o ponto de injecao do script principal.')
out = out[:idx] + script + out[idx:]

banner = ('<div style="background:#fef3c7;padding:8px;text-align:center;font-size:12px;'
          'color:#92400e;margin-top:24px">Snapshot estatico - ultima atualizacao: %s '
          '(dados travados, pagina nao consulta o Jira ao vivo)</div>\n</body>' % STAMP_BR)
if '</body>' not in out:
    sys.exit('ERRO: </body> nao encontrado.')
out = out.replace('</body>', banner, 1)

open(os.path.join(BASE, 'index.html'), 'w', encoding='utf-8').write(out)

print('OK  index.html %.1f KB | snapshot-data.js %.1f KB' % (
    len(out.encode('utf-8'))/1024, len(script.encode('utf-8'))/1024))
print('gerado:', STAMP_ISO)
print('meses congelados:', list(MONTHS.keys()), '| mes ao vivo (via DATASETS):', CURK)
print('datasets:', len(DATASETS), '| patterns:', len(pats))
for n in names: print('   %-22s %d' % (n, len(DATASETS[n])))
mj = MONTHS[PREVK]
print('%s: previstos=%d atraso=%d envios=%d retrabalho=%d lookahead=%d' % (
    PREVK, len(mj['planned']), len(mj['overdue']), mj['sent']['total'],
    mj['sent']['rework'], len(mj['look'])))
