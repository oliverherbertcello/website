#!/bin/bash
# Publish the dot version beside the current one, at /prototype/dot/. Usage: deploy_dot.sh "commit message"
S=/tmp/claude-0/-home-claude/ad98d268-0f43-5383-a1a4-12a5a093ddd0/scratchpad; P=$S/proto/oliver-herbert-dot.html
cd /home/claude/website || exit 1
mkdir -p public/prototype/dot
{ echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><meta name="robots" content="noindex"><meta name="description" content="Oliver Herbert, cellist. Concerts, recordings and projects."><style>[hidden]{display:none!important}body{margin:0}</style></head><body>'; sed -e 's#"img/#"../img/#g' -e 's#, img/#, ../img/#g' $P; echo '</body></html>'; } > public/prototype/dot/index.html
git add -A && git commit -qm "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019u7Kq4gBrnmXPFszSKhexq" && git push -q origin main && git log --oneline -1
