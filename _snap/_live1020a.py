# -*- coding: utf-8 -*-
"""Gera o snapshot estatico PR.03 (execucao 2026-10-19/20 BRT)."""
import json, os, re, io, datetime

REPO = os.path.join(os.environ['HOME'], 'mnt', 'pr03-relatorio-publico')
SNAPDIR = os.path.join(REPO, '_snap')

PJ = {
 'EG0239': 'EG0239 - CARPINA/ COMPESA',
 'EG0240': 'EG0240 - GOITÁ/ COMPESA',
 'EG0241': 'EG0241 - XARÉU/ COMPESA',
 'EG0256': 'EG0256 - SOPS_RS - EIA RIMA',
 'EG0274': 'EG0274 - DNIT',
 'EG0275': 'EG0275 - CODEVASF',
 'EG0286': 'EG0286 - DNIT/AC ',
 'EG291':  'EG0291 - Arroio Feijó',
 'G0280':  'EG0280 - DMAE',
}

def it(key, summary, st, cat, pj, due, res, upd):
    return {"key": key, "fields": {
        "summary": summary,
        "status": {"name": st, "statusCategory": {"key": cat}},
        "project": {"key": pj, "name": PJ[pj]},
        "duedate": due, "resolutiondate": res, "updated": upd}}

IND, DONE = 'indeterminate', 'done'
EAA = 'Enviado - Aguardando Análise'

EG291_4   = it('EG291-4', 'PEB - Plano de Execução BIM', EAA, DONE, 'EG291', '2026-10-07', '2026-10-15T13:59:49.573-0300', '2026-10-15T14:05:50.668-0300')
EG0286_7  = it('EG0286-7', 'Estudo de tráfego', EAA, DONE, 'EG0286', '2026-10-01', '2026-10-02T13:40:01.911-0300', '2026-10-02T13:40:01.929-0300')
EG0274_38 = it('EG0274-38', 'Estudos de Tráfego', EAA, DONE, 'EG0274', '2026-10-07', '2026-10-15T15:30:49.463-0300', '2026-10-15T15:30:49.471-0300')
EG0241_42 = it('EG0241-42', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', EAA, DONE, 'EG0241', '2026-09-10', '2026-10-02T09:30:29.370-0300', '2026-10-02T09:30:46.892-0300')
EG0275_112= it('EG0275-112', 'Licenças Ambientais', EAA, DONE, 'EG0275', '2026-09-04', '2026-10-02T09:27:36.092-0300', '2026-10-02T09:27:36.111-0300')
EG0240_5  = it('EG0240-5', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'Em Revisão', IND, 'EG0240', '2026-10-26', None, '2026-10-15T13:58:00.568-0300')
EG0239_28 = it('EG0239-28', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'Enviado - Aguardando Análise1', DONE, 'EG0239', '2026-08-10', '2026-10-09T09:36:29.171-0300', '2026-10-09T09:36:29.198-0300')

FRESH = {}

FRESH['planned_2026-10'] = [
 it('EG0240-43', 'TOMO IV - PROJETO DE INSTRUMENTAÇÃO', 'Em Revisão', IND, 'EG0240', '2026-10-23', None, '2026-10-15T14:50:41.722-0300'),
 it('EG0240-4', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'Em Revisão', IND, 'EG0240', '2026-10-23', None, '2026-10-15T13:58:30.870-0300'),
 EG0240_5,
 EG0274_38,
 it('EG0274-43', 'Estudos Hidrológicos ', 'Em Revisão', IND, 'EG0274', '2026-10-31', None, '2026-09-28T09:26:55.035-0300'),
 it('G0280-54', 'EBE Asa Branca', 'Em andamento', IND, 'G0280', '2026-10-29', None, '2026-09-30T14:59:57.634-0300'),
 it('G0280-55', 'EBE Nova Brasília', 'Em andamento', IND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:43.601-0300'),
 it('G0280-53', 'EBE Gaspar Martins', 'Em andamento', IND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:30.308-0300'),
 it('G0280-51', 'EBE Baronesa do Gravataí', 'Em andamento', IND, 'G0280', '2026-10-30', None, '2026-09-30T15:00:04.232-0300'),
 it('G0280-50', 'EBE Ponta da Cadeia', 'Em andamento', IND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:50.045-0300'),
 EG0286_7,
 it('EG0286-11', 'Estudos hidrológicos', 'Em andamento', IND, 'EG0286', '2026-10-15', None, '2026-09-28T09:29:27.853-0300'),
 it('EG0286-12', 'Levantamento ambiental', 'Em andamento', IND, 'EG0286', '2026-10-19', None, '2026-09-28T09:31:11.033-0300'),
 it('EG0286-10', 'Estudos geológicos', 'Em andamento', IND, 'EG0286', '2026-10-30', None, '2026-09-30T14:55:35.086-0300'),
 EG291_4,
]
FRESH['overdue_2026-10']  = []
FRESH['sent_2026-10']     = [EG291_4, EG0286_7, EG0275_112, EG0274_38, EG0241_42, EG0240_5]
FRESH['resolved_2026-10'] = [EG291_4, EG0286_7, EG0275_112, EG0274_38, EG0241_42, EG0239_28]
FRESH['rework_2026-10']   = [EG0286_7, EG0274_38, EG0241_42, EG0240_5]
FRESH['planned_2026-05'] = [
 it('EG0239-26', 'TOMO IV -  PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', 'Concluído', DONE, 'EG0239', '2026-05-15', '2026-07-13T16:10:44.098-0300', '2026-07-14T15:00:07.129-0300'),
 it('EG0274-39', 'Estudo de Concepção e Traçado', 'Concluído', DONE, 'EG0274', '2026-05-15', '2026-06-29T19:25:06.525-0300', '2026-09-28T09:26:14.228-0300'),
 it('G0280-49', 'EBE 5S', 'Medido e Faturado', DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:08.021-0300', '2026-09-30T11:24:05.018-0300'),
 it('G0280-48', 'EBE 4S', 'Medido e Faturado', DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:06.542-0300', '2026-09-30T11:24:03.760-0300'),
 it('G0280-47', 'EBE 3S', 'Medido e Faturado', DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:05.132-0300', '2026-09-30T11:24:02.649-0300'),
 it('G0280-46', 'EBE 2S', 'Medido e Faturado', DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:03.281-0300', '2026-09-30T11:24:01.415-0300'),
 it('G0280-45', 'EBE 1S', 'Medido e Faturado', DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:01.173-0300', '2026-09-30T11:23:59.909-0300'),
]
FRESH['planned_2026-06'] = [
 it('EG0256-24', 'Diagnóstico Ambiental - Meio Físico - Condições Meteorológicas', 'Enviado - Aguardando Análise1', DONE, 'EG0256', '2026-06-30', '2026-06-29T11:06:29.534-0300', '2026-06-29T11:06:39.573-0300'),
]

# ---- dados reaproveitados do snapshot anterior (inalterados nesta execucao) ----
prev = io.open(os.path.join(REPO, 'snapshot-data.js'), encoding='utf-8').read()
i = prev.index('var SNAP = ') + len('var SNAP = '); j = prev.index('var DATASETS')
PREV_SNAP = json.loads(prev[i:j].rstrip().rstrip(';'))
i2 = prev.index('var DATASETS = ') + len('var DATASETS = '); j2 = prev.index('var PATTERNS')
PREV_DS = json.loads(prev[i2:j2].rstrip().rstrip(';'))

DATASETS = {}
DATASETS['rework_2026-10']   = FRESH['rework_2026-10']
DATASETS['sent_2026-10']     = FRESH['sent_2026-10']
DATASETS['resolved_2026-10'] = FRESH['resolved_2026-10']
DATASETS['overdue_2026-10']  = FRESH['overdue_2026-10']
DATASETS['lookahead_2026-10'] = json.load(io.open(os.path.join(SNAPDIR, 'lookahead_2026-10.json'), encoding='utf-8'))
DATASETS['planned_2026-05'] = FRESH['planned_2026-05']
DATASETS['planned_2026-06'] = FRESH['planned_2026-06']
for k in ('planned_2026-07', 'planned_2026-08', 'planned_2026-09'):
    DATASETS[k] = PREV_DS[k]
DATASETS['planned_2026-10'] = FRESH['planned_2026-10']

# grava JSONs minimais para reuso
for name, data in list(FRESH.items()):
    with io.open(os.path.join(SNAPDIR, name + '.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
ISO = now.strftime('%Y-%m-%dT%H:%M:%S-03:00')
BR  = now.strftime('%d/%m/%Y %H:%M')

SNAP = {
    'generated': now.strftime('%Y-%m-%d'),
    'generatedAt': ISO,
    'epicTypeNames': ['Epic', 'Fluxo de trabalho'],
    'projects': PREV_SNAP['projects'],
    'months': PREV_SNAP['months'],
}

PATTERNS = [
 ('rework_2026-10',    r'DURING \\("2026-10-01","2026-10-31"\\)[\\s\\S]*changed from'),
 ('sent_2026-10',      r'DURING \\("2026-10-01","2026-10-31"\\)'),
 ('resolved_2026-10',  r'resolved>="2026-10-01"[\\s\\S]*resolved<="2026-10-31"'),
 ('overdue_2026-10',   r'duedate<"2026-10-01"[\\s\\S]*statusCategory!=Done'),
 ('lookahead_2026-10', r'duedate>="2026-11-01"[\\s\\S]*duedate<="2026-12-31"'),
 ('planned_2026-05',   r'duedate>="2026-05-01"[\\s\\S]*duedate<="2026-05-31"'),
 ('planned_2026-06',   r'duedate>="2026-06-01"[\\s\\S]*duedate<="2026-06-30"'),
 ('planned_2026-07',   r'duedate>="2026-07-01"[\\s\\S]*duedate<="2026-07-31"'),
 ('planned_2026-08',   r'duedate>="2026-08-01"[\\s\\S]*duedate<="2026-08-31"'),
 ('planned_2026-09',   r'duedate>="2026-09-01"[\\s\\S]*duedate<="2026-09-30"'),
 ('planned_2026-10',   r'duedate>="2026-10-01"[\\s\\S]*duedate<="2026-10-31"'),
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

  // __HISTORY__ com merge defensivo: o script do artifact faz
  // "window.__HISTORY__ = {{...}}" (atribuicao direta), o que apagaria os meses
  // congelados do snapshot. O accessor abaixo mescla em vez de sobrescrever,
  // e o snapshot tem precedencia sobre as chaves proprias.
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

# ---------- reinjeta no index.html ----------
html = io.open(os.path.join(REPO, 'index.html'), encoding='utf-8').read()

# 1) comentario no topo do <head>
html, n1 = re.subn(r'<!-- Snapshot gerado em [^>]*-->',
                   '<!-- Snapshot gerado em %s -->' % ISO, html, count=1)
assert n1 == 1, 'comentario de snapshot nao encontrado'

# 2) bloco de dados estaticos
start = html.index('<script>\n/* ====')
assert 'DADOS ESTATICOS DO SNAPSHOT' in html[start:start + 400], 'bloco de snapshot nao localizado'
end = html.index('</script>', start) + len('</script>\n')
html = html[:start] + block + html[end:]

# 3) banner antes de </body>
BANNER = ('<div style="background:#fef3c7;padding:8px;text-align:center;font-size:12px;'
          'color:#92400e;margin-top:24px">Snapshot estatico - ultima atualizacao: %s '
          '(dados travados, pagina nao consulta o Jira ao vivo)</div>' % BR)
html = re.sub(r'<div style="background:#fef3c7;[^>]*>Snapshot estatico[^<]*</div>\n?', '', html)
html = html.replace('</body>', BANNER + '\n</body>', 1)

with io.open(os.path.join(REPO, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print('ISO', ISO, '| BR', BR)
print('snapshot-data.js', os.path.getsize(os.path.join(REPO, 'snapshot-data.js')))
print('index.html', os.path.getsize(os.path.join(REPO, 'index.html')))
for k, v in DATASETS.items():
    print('  ', k, len(v))
