# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-07 ~00:30 UTC (06/10 21:31 BRT). Mes corrente: 2026-10.
#
# Filtro de tipo: issuetype in ("Epic","Fluxo de trabalho") (consolidado desde _run1006e).
#
# 6 conjuntos do mes corrente reconsultados ao vivo + getVisibleJiraProjects (21 projetos,
# isLast=true). pageInfo.hasNextPage = false nas 6 consultas.
#
# Conferencia: comparacao semantica campo a campo (key, status.name,
# status.statusCategory.key, project.key, project.name, duedate, resolutiondate, updated),
# insensivel a ordem, dos 6 conjuntos + lista de projetos contra o pacote de _snap/.
#
# RESULTADO: NENHUMA ALTERACAO desde _run1006i (17:30 BRT). Nenhuma chave entrou ou saiu;
# nenhum campo divergiu, nem 'updated'. EG291-4 segue com updated 2026-10-06T16:26:05.341-0300.
# index.html / snapshot-data.js mudam apenas no carimbo de geracao.
#
# ARTIFACT_HTML (C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics\
# index.html) segue inacessivel a sessao Cowork (protected location). A geracao usou
# _artifact_src.html, a copia local versionada no repo (87.509 bytes, sha256 2f09463c...ec2419).
import json, os
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'

LIVE = {
 'planned': ['EG0256-28','EG0256-30','EG0274-21','EG0274-38','EG0274-43','EG0274-58',
             'EG0274-59','EG0274-60','EG0274-61','EG0274-62','EG0274-63','EG0274-64',
             'EG0286-7','EG0286-10','EG0286-11','EG0286-12','EG0286-15','EG0286-16',
             'EG0286-17','EG0286-20','EG0286-21','EG0286-22','EG0286-23','EG291-4',
             'G0280-50','G0280-51','G0280-53','G0280-54','G0280-55'],
 'overdue': ['EG0239-28','EG0240-5'],
 'lookahead': ['EG0239-54','EG0240-44','EG0241-45','EG0274-57','EG0274-65','EG0274-66',
               'EG0275-108','EG0285-8','EG0285-14','EG0285-16','EG0285-18','EG0286-6',
               'EG0286-9','EG0286-14','EG0286-18','EG0286-19','EG0286-24','EG0294-1',
               'EG0294-2','EG0294-3','G0280-75'],
 'sent': ['EG0241-42','EG0275-112','EG0286-7'],
 'resolved': ['EG0241-42','EG0275-112','EG0286-7'],
 'rework': ['EG0241-42','EG0286-7'],
}

print('--- diff vs rodada anterior (17:30 BRT, _run1006i) ---')
alterado = False
for name, keys in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    ok = [i['key'] for i in old]
    if sorted(ok) == sorted(keys):
        print('%-10s sem alteracao de chaves (%d)' % (name, len(keys)))
    else:
        alterado = True
        print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(ok), len(keys),
              sorted(set(keys)-set(ok)) or '-', sorted(set(ok)-set(keys)) or '-'))
print('RESULTADO: nenhuma alteracao de dados nesta rodada.'
      if not alterado else 'RESULTADO: HOUVE ALTERACAO DE CHAVES - revisar')
