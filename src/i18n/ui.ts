// Interface words in each language. Work titles, venues and names are never translated.
export const languages = { en: 'EN', de: 'DE', es: 'ES' } as const;
export type Lang = keyof typeof languages;

export const ui = {
  en: { cello: 'Cello', soon: 'A new website is in progress.', current: 'Current site' },
  de: { cello: 'Violoncello', soon: 'Eine neue Website ist in Arbeit.', current: 'Aktuelle Website' },
  es: { cello: 'Violonchelo', soon: 'Un nuevo sitio web está en preparación.', current: 'Sitio actual' },
} as const;
