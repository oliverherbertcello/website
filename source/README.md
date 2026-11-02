# Site source

The whole site is one file: `source/oliver-herbert-dot.html` (all pages, text, concert data, styles and scripts).
Edit that file, then run `source/gen/deploy.sh "what changed"`. It writes `public/index.html`
(adding the head: title, description, link-preview tags), commits and pushes; Netlify publishes `public/`.

Assets sit beside the page in `public/`: `img/`, `audio/`, `webfonts/`, `files/`, plus `og.jpg` (link preview).
Redirects (old test address, old Wix pages) are in `netlify.toml`.

Launch switch: `LIVE=0` in `deploy.sh` keeps a noindex tag while the domain still points to Wix.
Set `LIVE=1` and redeploy once oliverherbertcello.com points to Netlify.

House rules for text: no em-dashes; quotes and attributions exact; Explore pages in third person.
Before each deploy: no missing images or audio, accessibility check clean.
