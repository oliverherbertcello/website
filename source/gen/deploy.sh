#!/bin/bash
# Build public/index.html from source/oliver-herbert-dot.html, then commit and push (Netlify publishes public/).
# Usage: source/gen/deploy.sh "commit message"
# LIVE=1 once oliverherbertcello.com points to Netlify (search engines may index). Until then the page says noindex.
LIVE=1
cd "$(dirname "$0")/../.." || exit 1
SRC=source/oliver-herbert-dot.html
if [ "$LIVE" = 1 ]; then ROBOTS='<meta name="robots" content="index, follow">'; else ROBOTS='<meta name="robots" content="noindex">'; fi
TITLE='Oliver Herbert, cellist'
DESC='Oliver Herbert is a cellist who performs internationally as a soloist, as a chamber musician, and in creative projects of his own. Concerts, recordings, videos and projects.'
URL='https://oliverherbertcello.com/'
{
  echo '<!doctype html><html lang="en"><head><meta charset="utf-8">'
  echo '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
  echo "<title>$TITLE</title>$ROBOTS"
  echo "<meta name=\"description\" content=\"$DESC\"><link rel=\"canonical\" href=\"$URL\">"
  echo '<link rel="icon" href="img/favicon.svg" type="image/svg+xml">'
  echo "<meta property=\"og:type\" content=\"website\"><meta property=\"og:site_name\" content=\"Oliver Herbert\"><meta property=\"og:title\" content=\"$TITLE\"><meta property=\"og:description\" content=\"$DESC\"><meta property=\"og:url\" content=\"$URL\">"
  echo "<meta property=\"og:image\" content=\"${URL}og.jpg\"><meta property=\"og:image:width\" content=\"1200\"><meta property=\"og:image:height\" content=\"630\"><meta property=\"og:image:alt\" content=\"Oliver Herbert, cellist\">"
  echo '<meta name="twitter:card" content="summary_large_image">'
  echo '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Oliver Herbert","jobTitle":"Cellist","url":"'"$URL"'","sameAs":["https://www.youtube.com/@OliverHerbertCello","https://www.instagram.com/oliverherbert_/"]}</script>'
  echo '<style>[hidden]{display:none!important}body{margin:0}</style></head><body>'
  grep -v -e '^<title>' -e '^<link rel="icon"' "$SRC"
  echo '</body></html>'
} > public/index.html
[ -n "$NOPUSH" ] && exit 0; git add -A && git commit -qm "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019u7Kq4gBrnmXPFszSKhexq" && git push -q origin main && git log --oneline -1
