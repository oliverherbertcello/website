# oliverherbertcello.com: how the site works

Live at https://oliverherbertcello.com (Netlify, publishes `public/`). Domain registered at Weebly; DNS managed in Wix
(A @ 75.2.60.5, CNAME www to oliverherbertcello.netlify.app, MX + SPF for ImprovMX). Email: contact@oliverherbertcello.com
forwards to Oliver's Gmail via ImprovMX (free plan, receive only). Contact form: Netlify Forms, notifications to his Gmail.

## Editing
- The whole site is one file: `source/oliver-herbert-dot.html` (all views: home, full calendar, About, Explore pages,
  Impressum, Privacy; texts, data and styles). Edit this file, never `public/index.html`.
- Concerts: the `CONCERTS` array, newest first. Each entry:
  `[start "YYYY-MM-DD", end or "", presenter/title, place, program in one line, details (performers. venue.), presenter URL or ""]`.
  Upcoming/past and the homepage "next concert" are computed from today's date. Upcoming links read "Details and tickets", past ones "Presenter".
- Videos: `FILMS`; albums: `ALBUMS`; audio player: `TRACKS` (files in `public/audio/`); Explore: `PROJECTS`.
- Images in `public/img/`, fonts in `public/webfonts/` (self-hosted; no Google requests), downloads in `public/files/`.

## Publishing
1. `NOPUSH=1 source/gen/deploy.sh x` builds `public/index.html` (adds the head: title, description, link previews, schema).
2. `python3 source/gen/check.py` must print ALL CLEAR (accessibility on home/calendar/About, no failed requests,
   no broken images, no script errors, no em-dashes).
3. `source/gen/deploy.sh "what changed"` builds, commits and pushes. Netlify publishes in about a minute.
   Netlify builds only when `public/` or `netlify.toml` changes (saves build credits). Batch changes; don't redeploy needlessly.

## House rules (from Oliver)
- No em-dashes. Short-to-medium sentences. Facts over adjectives; direct, never pretentious.
- Quotes and attributions exact (trimming with … is fine, as in press quotes). Explore pages: third person, uniform tense.
- Uncropped photos where possible. Don't highlight Kronberg Academy in captions. No "based in X".
- No postal address in the Impressum (his decision, risk accepted).

## Planned next: German and Spanish (decided 2 Nov 2026)
- Spanish: neutral Latin American. German: the restrained register of German concert programs.
  Translate for meaning and register, not word for word; keep a glossary so recurring terms stay uniform.
- Everything is translated, including the Explore program notes.
- Press quotes: original language plus translation, without crowding (decide the cleanest display).
- Language switcher EN · DE · ES in the top bar and menu; must not crowd the phone header next to the player pill.
- Architecture plan: move every text into one table with en/de/es side by side; each translation stores the English
  it was made from, so a changed English line flags its translations; /de/ and /es/ are built from the same design;
  hreflang tags. English-only stays possible: stop building /de/ and /es/ and redirect them to /.
