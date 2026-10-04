export interface MenuItem {
  category: string;
  name: string;
  price: string;
  description: string;
  image?: string;
  detailType?: "hair-removal";
}

export interface HairRemovalFacePart {
  id: string;
  name: string;
  description: string;
  image: string;
  price: string;
}

export interface HairRemovalBodyPart {
  id: string;
  name: string;
  description: string;
  imageKey: string;
  price: string;
  femaleOnly?: boolean;
}

export interface HairRemovalSubPart {
  id: string;
  name: string;
  description: string;
  imageKey: string;
  price: string;
  femaleOnly?: boolean;
}

const femaleFace: HairRemovalFacePart[] = [
  { id: "forehead", name: "おでこ", description: "額の産毛やムダ毛をすっきりと。", image: "/images/menu/face/female/forehead.jpg", price: "1回 2,000円（税込）" },
  { id: "eyebrow", name: "眉上", description: "眉の上のムダ毛をきれいに整えます。", image: "/images/menu/face/female/eyebrow.jpg", price: "1回 2,000円（税込）" },
  { id: "glabella", name: "眉間", description: "眉間のムダ毛をすっきりと。", image: "/images/menu/face/female/glabella.jpg", price: "1回 2,000円（税込）" },
  { id: "cheeks-sideburns", name: "両ほほ・もみあげ", description: "ほほと、もみあげ部分をまとめてケア。", image: "/images/menu/face/female/cheeks-sideburns.jpg", price: "1回 2,000円（税込）" },
  { id: "upper-lip", name: "鼻下", description: "鼻下のムダ毛をすっきりと。", image: "/images/menu/face/female/upper-lip.jpg", price: "1回 2,000円（税込）" },
  { id: "chin", name: "あご", description: "あごまわりのムダ毛をきれいに整えます。", image: "/images/menu/face/female/chin.jpg", price: "1回 2,000円（税込）" },
];

const maleFace: HairRemovalFacePart[] = [
  { id: "forehead", name: "おでこ", description: "額のムダ毛をすっきりと。", image: "/images/menu/face/male/forehead.jpg", price: "1回 2,000円（税込）" },
  { id: "eyebrow", name: "眉上", description: "眉の上のムダ毛をきれいに整えます。", image: "/images/menu/face/male/eyebrow.jpg", price: "1回 2,000円（税込）" },
  { id: "glabella", name: "眉間", description: "眉間のムダ毛をすっきりと。", image: "/images/menu/face/male/glabella.jpg", price: "1回 2,000円（税込）" },
  { id: "cheeks-sideburns", name: "両ほほ・もみあげ", description: "ほほと、もみあげ部分をまとめてケア。", image: "/images/menu/face/male/cheeks-sideburns.jpg", price: "1回 2,000円（税込）" },
  { id: "upper-lip", name: "鼻下", description: "鼻下のムダ毛をすっきりと。", image: "/images/menu/face/male/upper-lip.jpg", price: "1回 2,000円（税込）" },
  { id: "chin", name: "あご", description: "あごのムダ毛をきれいに整えます。", image: "/images/menu/face/male/chin.jpg", price: "1回 2,000円（税込）" },
];

const legParts: HairRemovalSubPart[] = [
  { id: "thigh-front", name: "太もも表", description: "太ももの前側をケアします。", imageKey: "thigh-front", price: "1回 5,000円（税込）" },
  { id: "thigh-back", name: "太もも裏", description: "太ももの後ろ側をケアします。", imageKey: "thigh-back", price: "1回 5,000円（税込）" },
  { id: "lower-leg-front", name: "ひざ下表", description: "ひざ下の前側をケアします。", imageKey: "lower-leg-front", price: "1回 7,000円（税込）" },
  { id: "lower-leg-back", name: "ひざ下裏", description: "ひざ下の後ろ側をケアします。", imageKey: "lower-leg-back", price: "1回 7,000円（税込）" },
  { id: "knees", name: "ひざ周り", description: "ひざ周りをケアします。", imageKey: "knees", price: "1回 2,000円（税込）" },
  { id: "feet", name: "足（甲・指）", description: "足の甲・指をまとめてケアします。", imageKey: "feet-special", price: "1回 2,000円（税込）" },
];

const fullBodyPlans: HairRemovalSubPart[] = [
  { id: "full-body-no-face", name: "全身（顔なし・VIOなし）", description: "顔・VIOを除く全身をケアします。", imageKey: "full-body", price: "1回 9,800円（税込）" },
  { id: "full-body-face", name: "全身（顔あり・VIOなし）", description: "顔を含む全身をケアします。VIOは含みません。", imageKey: "full-body", price: "1回 13,000円（税込）" },
  { id: "full-body-face-vio", name: "全身（顔あり・VIOあり）", description: "顔とVIOを含む全身をケアします。", imageKey: "full-body", price: "1回 15,000円（税込）", femaleOnly: true },
];

const vioParts: HairRemovalSubPart[] = [
  { id: "vio-all", name: "VIO全体", description: "V・I・Oをまとめてケアします。", imageKey: "vio-all", price: "1回 10,000円（税込）", femaleOnly: true },
  { id: "vio-v", name: "Vパーツ", description: "Vラインをケアします。", imageKey: "vio-v", price: "1回 3,500円（税込）", femaleOnly: true },
  { id: "vio-i", name: "Iパーツ", description: "Iラインをケアします。", imageKey: "vio-i", price: "1回 3,500円（税込）", femaleOnly: true },
  { id: "vio-o", name: "Oパーツ", description: "Oラインをケアします。", imageKey: "vio-o", price: "1回 3,500円（税込）", femaleOnly: true },
];

const body: HairRemovalBodyPart[] = [
  { id: "full-body", name: "全身脱毛", description: "顔・VIOの有無からメニューを選べます。", imageKey: "full-body", price: "1回 9,800円〜（税込）" },
  { id: "face-all", name: "顔全体", description: "顔全体をまとめてケアするメニューです。", imageKey: "face-all", price: "1回 6,000円（税込）" },
  { id: "face", name: "顔の部位", description: "両ほほ・もみあげ、鼻下、あご、眉間、眉上、おでこから選べます。", imageKey: "face-all", price: "1回 各2,000円（税込）" },
  { id: "neck", name: "うなじ", description: "うなじのムダ毛をケアします。", imageKey: "neck", price: "1回 3,500円（税込）" },
  { id: "chest", name: "胸", description: "胸まわりのムダ毛をケアします。", imageKey: "chest", price: "1回 5,000円（税込）" },
  { id: "abdomen", name: "お腹", description: "お腹まわりのムダ毛をケアします。", imageKey: "abdomen", price: "1回 5,000円（税込）" },
  { id: "underarms", name: "わき", description: "わきのムダ毛をケアします。", imageKey: "underarms", price: "1回 2,500円（税込）" },
  { id: "arms", name: "両腕", description: "両腕をまとめてケアします。", imageKey: "arms", price: "1回 7,000円（税込）" },
  { id: "hands", name: "手（甲・指）", description: "手の甲・指をまとめてケアします。", imageKey: "hands-special", price: "1回 2,000円（税込）" },
  { id: "back", name: "背中全体", description: "背中全体をまとめてケアします。", imageKey: "back", price: "1回 5,000円（税込）" },
  { id: "hips-seat", name: "お尻", description: "お尻まわりのムダ毛をケアします。", imageKey: "hips-seat", price: "1回 5,000円（税込）" },
  { id: "leg-parts", name: "脚の部位", description: "太もも・ひざ下・ひざ周り・足（甲・指）から選べます。", imageKey: "legs", price: "1回 2,000円〜（税込）" },
  { id: "vio-parts", name: "VIOの部位", description: "VIO全体・V・I・Oから選べます。女性のみのメニューです。", imageKey: "vio-all", price: "1回 3,500円〜（税込）", femaleOnly: true },
];

export const hairRemoval = {
  coverImage: "/images/menu/body/female/full-body.jpg",
  female: {
    label: "女性",
    overviewImage: "/images/menu/body/female/full-body.jpg",
    faceAllImage: "/images/menu/face/female-face-all-highlight.jpg",
    face: femaleFace,
  },
  male: {
    label: "男性",
    overviewImage: "/images/menu/body/male/full-body.jpg",
    faceAllImage: "/images/menu/face/male-face-all-highlight.jpg",
    face: maleFace,
  },
  body,
  legParts,
  fullBodyPlans,
  vioParts,
};

export const menuItems: MenuItem[] = [
  {
    category: "HAIR REMOVAL",
    name: "脱毛",
    price: "1回 2,000円〜（税込）",
    description: "全身・顔・各部位から選べる脱毛メニューです。VIO脱毛は女性のみ対応しています。",
    image: hairRemoval.coverImage,
    detailType: "hair-removal",
  },
  {
    category: "EYEBROW",
    name: "アイブロウスタイリング",
    price: "1回 4,800円（税込）",
    description: "眉の形を整え、自然な印象へ。",
  },
  {
    category: "EYEBROW",
    name: "ハリウッドブロウリフト",
    price: "1回 6,900円（税込）",
    description: "眉毛の毛流れを整えるメニューです。",
  },
  {
    category: "WHITENING",
    name: "ホワイトニング",
    price: "1回 3,300円（税込）",
    description: "twenty oneでご案内するホワイトニングメニューです。",
  },
];
