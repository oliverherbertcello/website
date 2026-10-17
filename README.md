# oliverherbertcello.com

The website of Oliver Herbert, cellist. Built with [Astro](https://astro.build), hosted on Netlify.

## Run it locally

```
npm install
npm run dev
```

## Structure

- `src/styles/tokens.css`: colors, typefaces, motion. Change the look here.
- `src/i18n/ui.ts`: interface words in English, German and Spanish.
- `src/layouts/Base.astro`: the page shell shared by every page.
- `src/pages/`: English at the root, German under `de/`, Spanish under `es/`.
- `public/prototype/`: the design prototype, for review only (not indexed).

Each change pushed to GitHub gets its own Netlify preview link. The live site changes only from `main`.
