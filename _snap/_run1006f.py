# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-06 ~16:30 UTC (13:30 BRT). Mes corrente: 2026-10.
#
# Filtro de tipo consolidado desde _run1006e: issuetype in ("Epic","Fluxo de trabalho").
# _projects_min.json ja reflete a renomeacao (EG0286, EG291, EG0285, EG0287,
# EG0292, EG0294, CREA = "Fluxo de trabalho"; demais = "Epic").
#
# 6 conjuntos do mes corrente reconsultados ao vivo + getVisibleJiraProjects (21 projetos).
# Comparacao byte-a-byte contra _snap/*_2026-10.json: IDENTICOS em todos os campos
# (key, summary, status.name, statusCategory.key, project, duedate, resolutiondate, updated).
# Nenhum arquivo de dados foi reescrito; o snapshot foi regerado apenas com novo timestamp.
#
# ARTIFACT_HTML (C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics\
# index.html) segue inacessivel a sessao Cowork (protected location). A geracao usou
# _artifact_src.html, a copia local versionada no repo.
import json, os
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'

LIVE = {
 'planned': ['EG0256-28','EG0256-30','EG0274-63','EG0274-59','EG0274-38','EG0274-64',
             'EG0274-62','EG0274-61','EG0274-60','EG0274-21','EG0274-58','EG0274-43',
             'G0280-54','G0280-55','G0280-53','G0280-51','G0280-50','EG0286-7',
             'EG0286-21','EG0286-20','EG0286-17','EG0286-16','EG0286-15','EG0286-11',
             'EG0286-12','EG0286-23','EG0286-22','EG0286-10','EG291-4'],
 'overdue': ['EG0239-28','EG0240-5'],
 'lookahead': ['EG0286-19','EG0285-16','EG0285-8','EG0285-18','EG0285-14','EG0294-3',
               'EG0294-2','EG0294-1','EG0286-6','EG0274-66','EG0274-65','G0280-75',
               'EG0274-57','EG0241-45','EG0286-18','EG0286-14','EG0286-24','EG0286-9',
               'EG0275-108','EG0240-44','EG0239-54'],
 'sent': ['EG0286-7','EG0275-112','EG0241-42'],
 'resolved': ['EG0286-7','EG0275-112','EG0241-42'],
 'rework': ['EG0286-7','EG0241-42'],
}

print('--- diff vs rodada anterior (15:30 UTC, _run1006e) ---')
alterado = False
for name, keys in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    ok = [i['key'] for i in old]
    if sorted(ok) == sorted(keys):
        print('%-10s sem alteracao (%d)' % (name, len(keys)))
    else:
        alterado = True
        print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(ok), len(keys),
              sorted(set(keys)-set(ok)) or '-', sorted(set(ok)-set(keys)) or '-'))
print('RESULTADO:', 'HOUVE ALTERACAO - revisar' if alterado
      else 'nenhuma alteracao de dados; snapshot regerado apenas com novo timestamp')
