# twenty one — project notes

## Current status

This repository is the demo version of the twenty one site.
Treatment reservations are intentionally not enabled. The site currently guides visitors to LINE / Instagram for Share Salon inquiries and tours.

## Structure

- `src/pages/` — pages
- `src/components/` — reusable UI components
- `src/layouts/` — page layout / metadata
- `src/data/` — salon and menu content
- `src/styles/global.css` — one consolidated global stylesheet
- `public/images/` — static site images
- `astro.config.mjs` — Astro configuration
- `package.json` — scripts and dependencies

## Local development

```bash
npm install
npm run dev
```

Build check:

```bash
npm run build
```

## Cloudflare Pages

For the current static Astro site:

- Production branch: `main`
- Build command: `npm run build`
- Build directory: `dist`

When the production domain is decided, add the final URL to `astro.config.mjs` as `site`.

## シェアサロン募集状況の変更

`src/data/salon.ts` の `shareSalonRecruiting` を変更すると、SHARE SALONページの募集状況を切り替えられます。

- `true` → 「募集状況：募集中」＋問い合わせボタンを表示
- `false` → 「募集状況：満席」＋新規募集停止の案内を表示

満席にする場合：
```ts
export const shareSalonRecruiting = false;
```
