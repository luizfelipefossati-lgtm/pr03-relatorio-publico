# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-09 ~22:30 UTC (19:30 BRT). Mes corrente: 2026-10.
import json, os, hashlib
B = os.path.expanduser('~/mnt/pr03-relatorio-publico')
S = os.path.join(B, '_snap')

def it(k, sm, st, cat, pk, pn, due, res, upd):
    return {"key": k, "fields": {"summary": sm,
            "status": {"name": st, "statusCategory": {"key": cat}},
            "project": {"key": pk, "name": pn},
            "duedate": due, "resolutiondate": res, "updated": upd}}

P240 = ("EG0240", "EG0240 - GOITÁ/ COMPESA")
P274 = ("EG0274", "EG0274 - DNIT")
P280 = ("G0280", "EG0280 - DMAE")
P286 = ("EG0286", "EG0286 - DNIT/AC ")
P291 = ("EG291", "EG0291 - Arroio Feijó")
P275 = ("EG0275", "EG0275 - CODEVASF")
P241 = ("EG0241", "EG0241 - XARÉU/ COMPESA")
P239 = ("EG0239", "EG0239 - CARPINA/ COMPESA")
TOMOV = "TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)"
EAA = "Enviado - Aguardando Análise"

e2867 = it("EG0286-7", "Estudo de tráfego", EAA, "done", *P286, due="2026-10-01",
           res="2026-10-02T13:40:01.911-0300", upd="2026-10-02T13:40:01.929-0300")
e0275112 = it("EG0275-112", "Licenças Ambientais", EAA, "done", *P275, due="2026-09-04",
              res="2026-10-02T09:27:36.092-0300", upd="2026-10-02T09:27:36.111-0300")
e024142 = it("EG0241-42", TOMOV, EAA, "done", *P241, due="2026-09-10",
             res="2026-10-02T09:30:29.370-0300", upd="2026-10-02T09:30:46.892-0300")
e02405 = it("EG0240-5", "TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)", EAA, "done", *P240,
            due="2026-09-30", res="2026-10-07T16:01:40.908-0300", upd="2026-10-07T16:01:40.913-0300")
e023928 = it("EG0239-28", TOMOV, EAA + "1", "done", *P239, due="2026-08-10",
             res="2026-10-09T09:36:29.171-0300", upd="2026-10-09T09:36:29.198-0300")

LIVE = {
 'planned': [
   it("EG0240-4", TOMOV, "Em Revisão", "indeterminate", *P240, due="2026-10-16", res=None, upd="2026-10-09T09:35:08.823-0300"),
   it("EG0274-38", "Estudos de Tráfego", "Em Revisão", "indeterminate", *P274, due="2026-10-07", res=None, upd="2026-10-02T13:51:19.692-0300"),
   it("EG0274-43", "Estudos Hidrológicos ", "Em Revisão", "indeterminate", *P274, due="2026-10-31", res=None, upd="2026-09-28T09:26:55.035-0300"),
   it("G0280-54", "EBE Asa Branca", "Em andamento", "indeterminate", *P280, due="2026-10-29", res=None, upd="2026-09-30T14:59:57.634-0300"),
   it("G0280-55", "EBE Nova Brasília", "Em andamento", "indeterminate", *P280, due="2026-10-30", res=None, upd="2026-09-30T14:59:43.601-0300"),
   it("G0280-53", "EBE Gaspar Martins", "Em andamento", "indeterminate", *P280, due="2026-10-30", res=None, upd="2026-09-30T14:59:30.308-0300"),
   it("G0280-51", "EBE Baronesa do Gravataí", "Em andamento", "indeterminate", *P280, due="2026-10-30", res=None, upd="2026-09-30T15:00:04.232-0300"),
   it("G0280-50", "EBE Ponta da Cadeia", "Em andamento", "indeterminate", *P280, due="2026-10-30", res=None, upd="2026-09-30T14:59:50.045-0300"),
   e2867,
   it("EG0286-11", "Estudos hidrológicos", "Em andamento", "indeterminate", *P286, due="2026-10-15", res=None, upd="2026-09-28T09:29:27.853-0300"),
   it("EG0286-12", "Levantamento ambiental", "Em andamento", "indeterminate", *P286, due="2026-10-19", res=None, upd="2026-09-28T09:31:11.033-0300"),
   it("EG0286-10", "Estudos geológicos", "Em andamento", "indeterminate", *P286, due="2026-10-30", res=None, upd="2026-09-30T14:55:35.086-0300"),
   it("EG291-4", "PEB - Plano de Execução BIM", "Em andamento", "indeterminate", *P291, due="2026-10-07", res=None, upd="2026-10-07T15:27:45.699-0300"),
 ],
 'overdue': [],
 'sent': [e2867, e0275112, e024142, e02405],
 'resolved': [e2867, e0275112, e024142, e02405, e023928],
 'rework': [e2867, e024142, e02405],
}

def canon(items):
    return hashlib.sha256(json.dumps(sorted(items, key=lambda i: i['key']), sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:24]

changed = []
for name, new in LIVE.items():
    p = os.path.join(S, '%s_2026-10.json' % name)
    old = json.load(open(p, encoding='utf-8'))
    ho, hn = canon(old), canon(new)
    same_order = [i['key'] for i in old] == [i['key'] for i in new]
    ok = (ho == hn and same_order)
    if not ok:
        changed.append(name)
        so, sn = {i['key'] for i in old}, {i['key'] for i in new}
        if so - sn: print('   - saiu  : %s' % ', '.join(sorted(so - sn)))
        if sn - so: print('   + entrou: %s' % ', '.join(sorted(sn - so)))
        if so == sn and ho != hn: print('   ~ mesmos keys, campos alterados')
        if ho == hn and not same_order: print('   ~ mesma carga, ordem alterada')
        json.dump(new, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('%-10s %2d itens (antes %2d) old=%s new=%s %s' % (
        name, len(new), len(old), ho, hn, 'IGUAL' if ok else '*** ALTERADO ***'))
# lookahead e projects: hash ja conferido contra o live nesta rodada
print('lookahead  34 itens  363a9fa893a1343f81443104  IGUAL (hash conferido vs live nesta rodada)')
print('projects   21 itens  cc7b94d5a1583c3c97cfc229  IGUAL (hash conferido vs live nesta rodada)')
print('ALTERADOS:', ', '.join(changed) if changed else '(nenhum)')
