#!/bin/bash
# uso: _latest.sh <dataset_name>   -> converte o tool-result .txt mais recente ainda nao consumido
TR="/sessions/serene-eager-keller/mnt/.claude/projects/C--Users-DELL-AppData-Roaming-Claude-local-agent-mode-sessions-805a2b19-8b9a-4441-a4a2-b12e4d71381d-47107925-0aa4-46df-9c0b-94fdb95926b5-local-7bbe88e4-4edc-4326-bc55-3bac1ea967f9-outputs/c36618cb-e40b-4c8d-a45b-1cf4e1a892d8/tool-results"
SNAP=/sessions/serene-eager-keller/mnt/pr03-relatorio-publico/_snap
CONS=$SNAP/.consumed
touch $CONS
F=$(ls -t "$TR"/*searchJiraIssuesUsingJql*.txt 2>/dev/null | while read f; do grep -qxF "$f" $CONS || { echo "$f"; break; }; done)
if [ -z "$F" ]; then echo "SEM ARQUIVO NOVO para $1"; exit 1; fi
echo "$F" >> $CONS
python3 $SNAP/_conv.py "$1" "$F"
