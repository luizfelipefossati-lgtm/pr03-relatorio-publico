# -*- coding: utf-8 -*-
"""Localiza o arquivo de tool-result cujo JQL corresponde ao informado e converte
para o formato minimo do snapshot (concurrency-safe: casa por conteudo, nao por mtime).

Uso: python3 _pick.py <dataset_name> "<jql exato>"
"""
import glob, json, os, re, sys, subprocess
from urllib.parse import urlparse, parse_qs, unquote

D = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(D, os.pardir, os.pardir, '.claude', 'projects')

def norm(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()

def jql_of(path):
    try:
        d = json.load(open(path, encoding='utf-8'))
    except Exception:
        return None
    wu = (d.get('issues') or {}).get('webUrl') if isinstance(d.get('issues'), dict) else None
    if not wu:
        return None
    q = parse_qs(urlparse(wu).query).get('jql')
    return norm(unquote(q[0])) if q else None

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    name, want = sys.argv[1], norm(sys.argv[2])
    files = glob.glob(os.path.join(TR, '**', 'tool-results', '*searchJiraIssuesUsingJql*.txt'), recursive=True)
    hits = [f for f in files if jql_of(f) == want]
    if not hits:
        sys.exit('NAO ENCONTRADO: nenhum tool-result com jql=%r (%d arquivos varridos)' % (want, len(files)))
    hits.sort(key=os.path.getmtime)
    f = hits[-1]
    print('arquivo:', os.path.basename(f))
    subprocess.check_call([sys.executable, os.path.join(D, '_conv.py'), name, f])

main()
