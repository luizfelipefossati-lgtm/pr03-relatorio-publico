# -*- coding: utf-8 -*-
"""Geracao 15/10/2026 ~12:30 BRT: dados ao vivo do Jira (MCP Atlassian) x cache _snap/*.json."""
import json, io, os
S = os.path.dirname(os.path.abspath(__file__))

def I(key, summary, st, cat, pk, pn, due, res, upd):
    return {"key": key, "fields": {"summary": summary,
            "status": {"name": st, "statusCategory": {"key": cat}},
            "project": {"key": pk, "name": pn},
            "duedate": due, "resolutiondate": res, "updated": upd}}

G240 = ("EG0240", "EG0240 - GOITÁ/ COMPESA")
G274 = ("EG0274", "EG0274 - DNIT")
G280 = ("G0280", "EG0280 - DMAE")
G286 = ("EG0286", "EG0286 - DNIT/AC ")
G291 = ("EG291", "EG0291 - Arroio Feijó")
G275 = ("EG0275", "EG0275 - CODEVASF")
G241 = ("EG0241", "EG0241 - XARÉU/ COMPESA")
G239 = ("EG0239", "EG0239 - CARPINA/ COMPESA")

EG0286_7  = I("EG0286-7", "Estudo de tráfego", "Enviado - Aguardando Análise", "done", *G286,
              due="2026-10-01", res="2026-10-02T13:40:01.911-0300", upd="2026-10-02T13:40:01.929-0300")
EG0241_42 = I("EG0241-42", "TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)", "Enviado - Aguardando Análise", "done", *G241,
              due="2026-09-10", res="2026-10-02T09:30:29.370-0300", upd="2026-10-02T09:30:46.892-0300")
EG0275_112= I("EG0275-112", "Licenças Ambientais", "Enviado - Aguardando Análise", "done", *G275,
              due="2026-09-04", res="2026-10-02T09:27:36.092-0300", upd="2026-10-02T09:27:36.111-0300")
EG0240_5  = I("EG0240-5", "TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)", "Em Revisão", "indeterminate", *G240,
              due="2026-09-30", res=None, upd="2026-10-13T09:51:44.629-0300")
EG0239_28 = I("EG0239-28", "TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)", "Enviado - Aguardando Análise1", "done", *G239,
              due="2026-08-10", res="2026-10-09T09:36:29.171-0300", upd="2026-10-09T09:36:29.198-0300")

LIVE = {}
LIVE['planned_2026-10'] = [
 I("EG0240-4", "TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)", "Em Revisão", "indeterminate", *G240,
   due="2026-10-16", res=None, upd="2026-10-09T09:35:08.823-0300"),
 I("EG0274-38", "Estudos de Tráfego", "Em Revisão", "indeterminate", *G274,
   due="2026-10-07", res=None, upd="2026-10-02T13:51:19.692-0300"),
 I("EG0274-43", "Estudos Hidrológicos ", "Em Revisão", "indeterminate", *G274,
   due="2026-10-31", res=None, upd="2026-09-28T09:26:55.035-0300"),
 I("G0280-54", "EBE Asa Branca", "Em andamento", "indeterminate", *G280,
   due="2026-10-29", res=None, upd="2026-09-30T14:59:57.634-0300"),
 I("G0280-55", "EBE Nova Brasília", "Em andamento", "indeterminate", *G280,
   due="2026-10-30", res=None, upd="2026-09-30T14:59:43.601-0300"),
 I("G0280-53", "EBE Gaspar Martins", "Em andamento", "indeterminate", *G280,
   due="2026-10-30", res=None, upd="2026-09-30T14:59:30.308-0300"),
 I("G0280-51", "EBE Baronesa do Gravataí", "Em andamento", "indeterminate", *G280,
   due="2026-10-30", res=None, upd="2026-09-30T15:00:04.232-0300"),
 I("G0280-50", "EBE Ponta da Cadeia", "Em andamento", "indeterminate", *G280,
   due="2026-10-30", res=None, upd="2026-09-30T14:59:50.045-0300"),
 EG0286_7,
 I("EG0286-11", "Estudos hidrológicos", "Em andamento", "indeterminate", *G286,
   due="2026-10-15", res=None, upd="2026-09-28T09:29:27.853-0300"),
 I("EG0286-12", "Levantamento ambiental", "Em andamento", "indeterminate", *G286,
   due="2026-10-19", res=None, upd="2026-09-28T09:31:11.033-0300"),
 I("EG0286-10", "Estudos geológicos", "Em andamento", "indeterminate", *G286,
   due="2026-10-30", res=None, upd="2026-09-30T14:55:35.086-0300"),
 I("EG291-4", "PEB - Plano de Execução BIM", "Em andamento", "indeterminate", *G291,
   due="2026-10-07", res=None, upd="2026-10-07T15:27:45.699-0300"),
]
LIVE['overdue_2026-10']  = [EG0240_5]
LIVE['sent_2026-10']     = [EG0286_7, EG0275_112, EG0241_42, EG0240_5]
LIVE['resolved_2026-10'] = [EG0286_7, EG0275_112, EG0241_42, EG0239_28]
LIVE['rework_2026-10']   = [EG0286_7, EG0241_42, EG0240_5]
LIVE['lookahead_2026-10'] = json.load(io.open(os.path.join(S, '_new_lookahead_2026-10.json'), encoding='utf-8'))

diffs = 0
for name in sorted(LIVE):
    p = os.path.join(S, name + '.json')
    old = json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else None
    new = LIVE[name]
    if old == new:
        print('%-20s %2d itens  IDENTICO' % (name, len(new)))
    else:
        diffs += 1
        ok = [i['key'] for i in (old or [])]; nk = [i['key'] for i in new]
        print('%-20s DIFERENTE cache=%d live=%d' % (name, len(ok), len(nk)))
        if ok != nk:
            print('   so cache:', sorted(set(ok) - set(nk)), '| so live:', sorted(set(nk) - set(ok)))
        else:
            for a, b in zip(old, new):
                if a != b:
                    for k in b['fields']:
                        if a['fields'].get(k) != b['fields'][k]:
                            print('   %s.%s cache=%r live=%r' % (b['key'], k, a['fields'].get(k), b['fields'][k]))
    io.open(p, 'w', encoding='utf-8').write(json.dumps(new, ensure_ascii=False, indent=1))

print('\nCONJUNTOS COM MUDANCA:', diffs)

# projetos
a = json.load(io.open(os.path.join(S, '..', '_projects_min.json'), encoding='utf-8'))
b = json.load(io.open(os.path.join(S, '..', '_new_projects_min.json'), encoding='utf-8'))
def norm(ps):
    return sorted([(p['key'], p.get('name'), sorted((t['name'], t.get('hierarchyLevel')) for t in p.get('issueTypes', []))) for p in ps])
print('PROJETOS cache=%d live=%d  %s' % (len(a), len(b), 'IDENTICOS' if norm(a) == norm(b) else 'DIFERENTES'))
if norm(a) != norm(b):
    io.open(os.path.join(S, '..', '_projects_min.json'), 'w', encoding='utf-8').write(json.dumps(b, ensure_ascii=False, indent=1))
    print('  _projects_min.json REGRAVADO')
