# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-06 ~14:30 UTC (11:30 BRT). Mes corrente: 2026-10.
# Os 6 conjuntos de out/2026 foram RECONSULTADOS AO VIVO via MCP Atlassian:
#   planned   = 2 consultas (10-01..10-15 = 12, 10-16..10-31 = 17) -> 29
#   overdue   = 1 consulta  -> 2
#   lookahead = 2 consultas (nov = 14, dez = 7) -> 21
#   sent / resolved = 3 cada ; rework = 2
# Resultado: TODOS os conjuntos identicos a rodada das 13:30 UTC (_run1006c.py).
# getVisibleJiraProjects NAO reconsultado (chaves ja constam de _projects_min.json).
# Meses congelados (<= 2026-09) NAO sao reconsultados.
import json, os
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'

LIVE = {
 'planned': ['EG0256-28','EG0274-63','EG0274-59','EG0274-38','EG0286-7','EG0286-21',
             'EG0286-20','EG0286-17','EG0286-16','EG0286-15','EG0286-11','EG291-4',
             'EG0256-30','EG0274-64','EG0274-62','EG0274-61','EG0274-60','EG0274-21',
             'EG0274-58','EG0274-43','G0280-54','G0280-55','G0280-53','G0280-51',
             'G0280-50','EG0286-12','EG0286-23','EG0286-22','EG0286-10'],
 'overdue': ['EG0239-28','EG0240-5'],
 'lookahead': ['EG0286-19','EG0285-16','EG0285-8','EG0285-18','EG0285-14','EG0294-3',
               'EG0294-2','EG0294-1','EG0286-6','EG0274-66','EG0274-65','G0280-75',
               'EG0274-57','EG0241-45','EG0286-18','EG0286-14','EG0286-24','EG0286-9',
               'EG0275-108','EG0240-44','EG0239-54'],
 'sent': ['EG0286-7','EG0275-112','EG0241-42'],
 'resolved': ['EG0286-7','EG0275-112','EG0241-42'],
 'rework': ['EG0286-7','EG0241-42'],
}
# (key, status, duedate, updated) conferidos campo a campo na consulta ao vivo
LIVE_FIELDS = {
 'EG0256-28': ('Em andamento','2026-10-01','2026-04-07T13:44:09.762-0300'),
 'EG0274-38': ('Em Revisao','2026-10-07','2026-10-02T13:51:19.692-0300'),
 'EG291-4':   ('Em andamento','2026-10-07','2026-10-05T09:55:25.830-0300'),
 'EG0274-21': ('Tarefas pendentes','2026-10-29','2026-09-25T09:56:37.062-0300'),
 'EG0286-10': ('Em andamento','2026-10-30','2026-09-30T14:55:35.086-0300'),
 'EG0239-28': ('Em Revisao','2026-08-10','2026-09-21T10:55:55.586-0300'),
 'EG0240-5':  ('Em Revisao','2026-09-30','2026-09-21T10:07:17.904-0300'),
 'EG0286-7':  ('Enviado - Aguardando Analise','2026-10-01','2026-10-02T13:40:01.929-0300'),
 'EG0275-112':('Enviado - Aguardando Analise','2026-09-04','2026-10-02T09:27:36.111-0300'),
 'EG0241-42': ('Enviado - Aguardando Analise','2026-09-10','2026-10-02T09:30:46.892-0300'),
}

print('--- diff vs rodada anterior (13:30 UTC) ---')
alterado = False
for name, keys in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    ok = [i['key'] for i in old]
    if ok == keys:
        print('%-10s sem alteracao (%d)' % (name, len(keys)))
    else:
        alterado = True
        print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(ok), len(keys),
              sorted(set(keys)-set(ok)) or '-', sorted(set(ok)-set(keys)) or '-'))

# conferencia de campos nas amostras verificadas ao vivo
print('--- conferencia de campos (amostra ao vivo) ---')
idx = {}
for name in LIVE:
    for i in json.load(open(os.path.join(D, '%s_%s.json' % (name, K)), encoding='utf-8')):
        idx.setdefault(i['key'], i)
norm = lambda s: (s.replace('ã','a').replace('á','a').replace('é','e')
                   .replace('í','i').replace('ó','o').replace('ú','u')
                   .replace('â','a').replace('ê','e').replace('ô','o')
                   .replace('ç','c').replace('à','a'))
for k, (st, dd, up) in LIVE_FIELDS.items():
    i = idx.get(k)
    if not i:
        print('  %-12s AUSENTE nos JSONs' % k); alterado = True; continue
    f = i['fields']
    got = (norm(f['status']['name']), f['duedate'], f['updated'])
    print('  %-12s %s' % (k, 'ok' if got == (st, dd, up) else 'DIVERGENTE %r vs %r' % (got, (st, dd, up))))
    if got != (st, dd, up): alterado = True

print('RESULTADO:', 'HOUVE ALTERACAO - revisar' if alterado else 'nenhuma alteracao de dados; snapshot sera regerado apenas com novo timestamp')
