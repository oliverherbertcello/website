#!/bin/bash
# Make the real-font render copy of the prototype
S=/tmp/claude-0/-home-claude/ad98d268-0f43-5383-a1a4-12a5a093ddd0/scratchpad; P=$S/proto/${1:-oliver-herbert-prototype}.html
{ echo -n '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>[hidden]{display:none!important}body{margin:0}</style></head><body>'
  cat $P
  echo -n '</body></html>'; } > $S/fonts/${2:-proto}.html
