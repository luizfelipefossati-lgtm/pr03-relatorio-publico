# -*- coding: utf-8 -*-
"""Regera o snapshot PR.03 na geracao de 15/10/2026 23:3x BRT.
Dados do Jira conferidos ao vivo e identicos aos do snapshot anterior
(ver _snap/_live1016c.py), entao so os carimbos de tempo mudam."""
import io, os, sys, datetime

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OLD_ISO = '2026-10-15T22:30:19-03:00'
OLD_BR  = '15/10/2026 22:30'

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
NEW_ISO = now.strftime('%Y-%m-%dT%H:%M:%S-03:00')
NEW_BR  = now.strftime('%d/%m/%Y %H:%M')
NEW_DAY = now.strftime('%Y-%m-%d')

def patch(rel, pairs):
    p = os.path.join(BASE, rel)
    s = io.open(p, encoding='utf-8').read()
    orig = s
    for old, new, n in pairs:
        c = s.count(old)
        if c != n:
            sys.exit('ERRO %s: esperava %d ocorrencias de %r, achei %d' % (rel, n, old[:60], c))
        s = s.replace(old, new)
    if s == orig:
        sys.exit('ERRO %s: nada mudou' % rel)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    print('%-20s %d bytes' % (rel, len(s.encode('utf-8'))))

patch('snapshot-data.js', [
    (OLD_ISO, NEW_ISO, 3),
    ('"generated":"2026-10-15"', '"generated":"%s"' % NEW_DAY, 1),
])
patch('index.html', [
    (OLD_ISO, NEW_ISO, 4),
    ('"generated":"2026-10-15"', '"generated":"%s"' % NEW_DAY, 1),
    (OLD_BR, NEW_BR, 1),
])
print('NEW_ISO =', NEW_ISO)
print('NEW_BR  =', NEW_BR)
