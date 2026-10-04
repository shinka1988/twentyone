# twenty one

Astroで作成している `twenty one` のデモサイトです。

## 現在の運用

- 施術メニューは紹介用です。現在、施術予約は受け付けていません。
- シェアサロンの見学・利用相談は受け付けています。
- シェアサロンの募集状況は `src/data/salon.ts` の `shareSalonRecruiting` で切り替えます。

## ローカル確認

```bash
npm install
npm run dev
```

本番ビルド確認:

```bash
npm run build
```

## 主な編集箇所

- `src/data/menu.ts` — メニュー内容・料金・脱毛画像の参照
- `src/data/salon.ts` — 店舗情報・シェアサロン募集状態
- `src/components/Menu.astro` — メニューUI
- `src/styles/global.css` — TOP・メニューを含む全体デザイン
- `src/pages/tenant.astro` — シェアサロンページ

## 画像

サイトで使用中の画像だけを `public/images/` に残しています。

脱毛画像は以下に整理しています。

- `public/images/menu/body/female/`
- `public/images/menu/body/male/`
- `public/images/menu/face/female/`
- `public/images/menu/face/male/`

アイブロウスタイリング・ハリウッドブロウリフト・ホワイトニングは、
`public/images/menu/beauty-menu-illustrations.png` の3面イラストを使用します。
`src/data/menu.ts` の `imagePosition` で左・中央・右を指定し、
メニューカードと詳細画面に各メニューの画像を表示します。

TOPの「脱毛」カードは、女性のみのイラスト
`public/images/menu/hair-removal-cover.png` を使用します。
4つのメニューカードは正方形の画像表示で揃えています。
脱毛の詳細で表示する男女別・部位別の画像は、上記の脱毛画像フォルダを使用します。
