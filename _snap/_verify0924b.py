# -*- coding: utf-8 -*-
# Reconferencia ao vivo em 2026-09-24 ~13:30 UTC (10:30 BRT), rodada seguinte a
# _verify0924a.py. As 6 consultas de setembro/2026 foram refeitas no Jira com
# ETQ = issuetype in ("Epic","Fluxo de trabalho") e devolveram exatamente os
# mesmos registros: planned=20, overdue=2, sent=5, resolved=4, rework=2,
# lookahead=27. getVisibleJiraProjects: 20 projetos, mesmas 20 chaves de
# _projects_min.json, tipos de nivel Epic inalterados (Epic, Fluxo de trabalho).
# _artifact_src.html conferido contra o HTML do artifact obtido do app
# (md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes): identico.
import json, os, sys
D = os.path.expanduser('~/mnt/pr03-relatorio-publico/_snap')
N="Tarefas pendentes"; A="Em andamento"; R="Em Revisão"; R2="Em Revisã"
EA="Enviado - Aguardando Análise"; EA2="Enviado- Aguardando Análise"

live = {
"planned_2026-09":[
("EG0275-112",R2,"2026-09-04",None,"2026-09-21T09:51:05.827-0300"),
("EG0275-6",EA,"2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("G0280-53",N,"2026-09-08",None,"2026-07-28T16:03:46.832-0300"),
("EG0241-42",R,"2026-09-10",None,"2026-08-31T16:44:47.690-0300"),
("EG0240-43",EA,"2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-4",N,"2026-09-10",None,"2026-08-31T16:45:50.827-0300"),
("EG0286-13",N,"2026-09-14",None,"2026-07-03T11:07:40.831-0300"),
("G0280-51",A,"2026-09-15",None,"2026-08-31T00:42:45.248-0300"),
("G0280-52",A,"2026-09-16",None,"2026-07-28T16:05:36.102-0300"),
("G0280-50",A,"2026-09-16",None,"2026-07-28T16:04:10.678-0300"),
("EG0274-58",N,"2026-09-17",None,"2026-05-28T17:47:27.192-0300"),
("EG0274-21",N,"2026-09-17",None,"2026-05-28T17:47:32.287-0300"),
("EG0285-19",A,"2026-09-18",None,"2026-05-18T10:57:07.064-0300"),
("G0280-54",N,"2026-09-22",None,"2026-07-28T16:03:54.494-0300"),
("EG0286-11",A,"2026-09-23",None,"2026-08-30T23:27:03.793-0300"),
("G0280-55",N,"2026-09-29",None,"2026-07-28T16:04:01.727-0300"),
("EG0286-14",N,"2026-09-29",None,"2026-06-17T17:38:16.515-0300"),
("EG0286-10",A,"2026-09-30",None,"2026-08-28T16:30:11.901-0300"),
("EG0286-6",N,"2026-09-30",None,"2026-08-30T23:26:14.328-0300"),
("EG0240-5",R,"2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
],
"overdue_2026-09":[
("EG0239-28",R,"2026-08-10",None,"2026-09-21T10:55:55.586-0300"),
("EG0286-8",A,"2026-08-31",None,"2026-07-30T09:33:06.932-0300"),
],
"sent_2026-09":[
("EG0286-7",EA,"2026-08-31","2026-09-03T16:50:04.999-0300","2026-09-03T16:50:05.010-0300"),
("EG0275-6",EA,"2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0240-43",EA,"2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-5",R,"2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
("EG0286-30",EA,"2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
],
"resolved_2026-09":[
("EG0286-7",EA,"2026-08-31","2026-09-03T16:50:04.999-0300","2026-09-03T16:50:05.010-0300"),
("EG0275-6",EA,"2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0240-43",EA,"2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0286-30",EA,"2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
],
"rework_2026-09":[
("EG0240-43",EA,"2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-5",R,"2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
],
}
# lookahead: key + status + duedate only
live_look = [
("G0280-75",A,"2026-10-01"),("EG0256-28",A,"2026-10-01"),("EG0274-63",N,"2026-10-06"),
("EG0274-59",N,"2026-10-06"),("EG0286-21",N,"2026-10-12"),("EG0286-20",N,"2026-10-12"),
("EG0286-17",N,"2026-10-14"),("EG0286-16",N,"2026-10-14"),("EG0286-15",N,"2026-10-14"),
("EG0286-12",N,"2026-10-19"),("EG0286-23",N,"2026-10-20"),("EG0286-22",N,"2026-10-22"),
("EG0274-64",A,"2026-10-25"),("EG0274-62",N,"2026-10-25"),("EG0274-61",N,"2026-10-25"),
("EG0274-60",N,"2026-10-25"),("EG0286-9",N,"2026-10-28"),("EG0256-30",A,"2026-10-31"),
("EG0286-19",N,"2026-11-03"),("EG0285-16",N,"2026-11-03"),("EG0285-8",EA2,"2026-11-03"),
("EG0285-18",N,"2026-11-09"),("EG0285-14",N,"2026-11-09"),("EG0274-66",N,"2026-11-18"),
("EG0274-65",N,"2026-11-18"),("EG0274-57",N,"2026-11-30"),("EG0241-45",N,"2026-11-30"),
]

def load(n):
    return json.load(open(os.path.join(D, n + '.json'), encoding='utf-8'))

bad = 0
for name, rows in live.items():
    cur = load(name)
    got = [(i['key'], i['fields']['status']['name'], i['fields']['duedate'],
            i['fields']['resolutiondate'], i['fields']['updated']) for i in cur]
    exp = [tuple(r) for r in rows]
    if got == exp:
        print('OK   %-20s %d registros identicos' % (name, len(exp)))
    else:
        bad += 1
        print('DIFF %-20s arquivo=%d jira=%d' % (name, len(got), len(exp)))
        for x in exp:
            if x not in got: print('   + jira:', x)
        for x in got:
            if x not in exp: print('   - arquivo:', x)

cur = load('lookahead_2026-09')
got = [(i['key'], i['fields']['status']['name'], i['fields']['duedate']) for i in cur]
if got == live_look:
    print('OK   %-20s %d registros identicos' % ('lookahead_2026-09', len(live_look)))
else:
    bad += 1
    print('DIFF lookahead_2026-09  arquivo=%d jira=%d' % (len(got), len(live_look)))
    for x in live_look:
        if x not in got: print('   + jira:', x)
    for x in got:
        if x not in live_look: print('   - arquivo:', x)

print('\nRESULTADO:', 'SEM DELTA' if bad == 0 else '%d conjuntos divergentes' % bad)
sys.exit(1 if bad else 0)
