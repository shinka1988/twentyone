export interface MenuItem {
  category: string;
  name: string;
  price: string;
  description: string;
  image?: string;
}

// Twenty one 自店の施術メニュー。
// 現在はメニュー紹介のみ。予約受付は今後開始予定です。
export const menuItems: MenuItem[] = [
  {
    category: "HAIR REMOVAL",
    name: "脱毛",
    price: "料金未定",
    description: "Twenty oneでご案内する脱毛メニューです。料金・詳細は決まり次第掲載します。",
  },
  {
    category: "EYEBROW",
    name: "アイブロウ",
    price: "料金未定",
    description: "眉を整え、自然で印象的な目元へ。料金・詳細は決まり次第掲載します。",
  },
  {
    category: "WHITENING",
    name: "ホワイトニング",
    price: "料金未定",
    description: "Twenty oneでご案内するホワイトニングメニューです。料金・詳細は決まり次第掲載します。",
  },
];
