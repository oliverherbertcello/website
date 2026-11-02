# Site source

`oliver-herbert-dot.html` is the single source file for the site (all pages, text, data and styles).
Edit this file, never the deployed copy in `public/prototype/dot/index.html`.

Deploy: the deployed copy is this file with `img/` paths rewritten to `../img/`
(see `gen/deploy_dot.sh`). Audio lives in `public/prototype/dot/audio/`, fonts in
`public/prototype/dot/webfonts/`, images in `public/prototype/img/`.

Checks before each deploy: accessibility (`gen/axe_dot.py`), no em-dashes, no missing assets.
