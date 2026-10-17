// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://oliverherbertcello.com',
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'de', 'es'],
    routing: { prefixDefaultLocale: false },
  },
});
