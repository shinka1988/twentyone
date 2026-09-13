export interface MenuItem {
  category: string;
  name: string;
  price: string;
  description: string;
  image?: string;
}

export const menuItems: MenuItem[] = [
  {
    category: "NAIL & HAND",
    name: "ワンカラー / グラデーション",
    price: "¥6,500〜",
    description: "自爪を削らないパラジェル使用。シンプルで上品な仕上がりに。",
    // image: "/images/menu/one-color.jpg",
  },
  {
    category: "NAIL & HAND",
    name: "アートデザインコース",
    price: "¥8,500〜",
    description: "トレンドデザインや持ち込みデザインに対応した人気のコースです。",
    // image: "/images/menu/art-design.jpg",
  },
  {
    category: "NAIL & HAND",
    name: "ハンドケアコース",
    price: "¥4,000",
    description: "爪の形整え、甘皮処理、表面磨き、保湿トリートメントのトータルケア。",
    // image: "/images/menu/hand-care.jpg",
  },
  {
    category: "NAIL & HAND",
    name: "フットコース",
    price: "¥7,500〜",
    description: "フットバス付き。足元を美しく彩る長持ちジェルネイルコース。",
    // image: "/images/menu/foot.jpg",
  },
  {
    category: "EYEBROW",
    name: "眉スタイリング",
    price: "¥5,500",
    description: "アイブロウスタイリング（眉カット+毛量調整+メイク仕上げ）",
    // image: "/images/menu/eyebrow-styling.jpg",
  },
  {
    category: "EYEBROW",
    name: "眉パーマ",
    price: "¥7,600",
    description: "韓国風垢抜けハリウッドブロウリフト（カット+毛量調整+メイク仕上げ）",
    // image: "/images/menu/eyebrow-lift.jpg",
  },
];
