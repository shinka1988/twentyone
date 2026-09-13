# Twenty one サイトの写真追加ガイド

写真は `src/assets/images/` ではなく、Astro の公開用 `public/images/` に置く想定です。

推奨:
- `public/images/hero/` : TOPのメイン写真
- `public/images/salon/` : ABOUT・店内写真
- `public/images/menu/` : メニュー写真
- `public/images/gallery/` : TOPのギャラリー
- `public/images/staff/` : スタッフ写真

写真を追加したら `src/data/salon.ts` や `src/data/menu.ts` のコメント例を参考にパスを設定してください。

### 今回追加したシェアサロン写真
- `public/images/space/space-01.jpg`
- `public/images/space/space-02.jpg`

`tenant.astro` の「SPACE GALLERY」に表示されます。

### メニュー詳細・予約
`src/data/menu.ts` の各メニューに `image` と `bookingUrl` を設定できます。
- `image`: メニュークリック時に表示する写真
- `bookingUrl`: Squareなどの予約ページURL。空欄なら予約ボタンは表示されません。
