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

- `src/data/menu.ts` — メニュー内容・料金・画像の参照・ネイルのご案内
- `src/data/salon.ts` — 店舗情報・住所・Googleマップ・シェアサロン募集状態
- `src/components/SalonMap.astro` — TOPとシェアサロンで共通のピン付き地図
- `src/components/Menu.astro` — メニューUI
- `src/components/NailInfo.astro` — メニュー選択後に表示するネイルのデザイン条件・オフ料金
- `src/styles/global.css` — TOP・メニューを含む全体デザイン
- `src/pages/tenant.astro` — シェアサロンページ

地図は店舗住所の建物位置を確認し、赤いピンが出る座標指定の埋め込みを使用しています。
住所の表示は `salonAddress`、埋め込み地図は `mapEmbedUrl`、別タブで開く地図は `mapUrl` で変更できます。

## 画像

サイトで使用中の画像だけを `public/images/` に残しています。

脱毛画像は以下に整理しています。

- `public/images/menu/body/female/`
- `public/images/menu/body/male/`
- `public/images/menu/face/female/`
- `public/images/menu/face/male/`

女性の上半身（お腹・胸・両腕・わき・うなじ・背中）と顔の部位画像は、
全身画像・顔全体画像を基準に、白の肩ひも付きブラトップと高めのお団子ヘアで揃えています。
部位別のハイライトを残し、全身・顔全体の専用画像はハイライトなしです。

女性のお尻と、男女の太もも表裏・ひざ下表裏・ひざ周り・脚一覧も、全身画像を基準に描き直しています。
脚の前面は膝のお皿と足の指、背面は膝裏・ふくらはぎ・かかとで向きが分かる構図です。
男性の下着はグレーのボクサーパンツで統一しています。
男女の足（甲・指）は、左右の親指が内側になる向きで、甲と指先が見える拡大画像です。
女性の足は、足幅と足首を細めにして華奢な形に調整しています。
部位のハイライトは女性がピンク、男性が水色です。
男性の胸・お腹は女性版と同じ正面の構図に揃え、腕が下端まで自然につながるように描いています。
脱毛のパンくずは「脱毛メニュー」を起点とし、部位の階層と選択中の部位を表示します。

アイブロウスタイリング・ハリウッドブロウリフト・ホワイトニングは、
`public/images/menu/beauty-menu-illustrations.png` の3面イラストを使用します。
`src/data/menu.ts` の `imagePosition` で左・中央・右を指定し、
メニューカードと詳細画面に各メニューの画像を表示します。

TOPの「脱毛」カードは、女性のみのイラスト
`public/images/menu/hair-removal-cover.png` を使用します。
6つのメニューカードは正方形の画像表示で揃えています。
脱毛の詳細で表示する男女別・部位別の画像は、上記の脱毛画像フォルダを使用します。

ネイルのワンカラー・フットワンカラーには、ご指定の手元・足元の画像を使用します。
画像内に料金は入れず、カードと詳細画面にそれぞれ `1回 5,500円（税込）` を表示します。
ネイルオフも `1,500円（税込）` の形式で表示し、自店オフ（付け替え）は `無料` です。

- `public/images/menu/nail-one-color.png`
- `public/images/menu/nail-foot-one-color.png`

デザインのご案内条件とネイルオフ料金は `src/data/menu.ts` の `nailInformation` で編集できます。
これらの説明はメニュー選択後の詳細画面に表示します。
