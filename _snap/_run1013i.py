# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-13 ~17:30 BRT. Mes corrente: 2026-10.
# Unica mudanca ao vivo nesta rodada: EG0256-30 saiu do lookahead
# (duedate 2026-12-19 -> 2027-01-30, alterado hoje as 17:04:26 BRT).
# Os outros 5 conjuntos e a lista de 21 projetos reproduziram o cache item a item.
import json, io, os
B = os.path.expanduser('~/mnt/pr03-relatorio-publico')
P = os.path.join(B, '_snap', 'lookahead_2026-10.json')
d = json.load(io.open(P, encoding='utf-8'))
before = len(d)
out = [i for i in d if i['key'] != 'EG0256-30']
assert before - len(out) == 1, 'esperava remover exatamente 1 item, removi %d' % (before - len(out))
io.open(P, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('lookahead_2026-10.json: %d -> %d itens (removido EG0256-30)' % (before, len(out)))
