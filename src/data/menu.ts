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
}

export interface HairRemovalBodyPart {
  id: string;
  name: string;
  description: string;
  imageKey: string;
}

export interface HairRemovalSubPart {
  id: string;
  name: string;
  description: string;
  imageKey: string;
}

const femaleFace: HairRemovalFacePart[] = [
  { id: "forehead", name: "おでこ", description: "額の産毛やムダ毛をすっきりと。", image: "/images/menu/face/female/forehead.jpg" },
  { id: "eyebrow", name: "眉上", description: "眉の上のムダ毛をきれいに整えます。", image: "/images/menu/face/female/eyebrow.jpg" },
  { id: "glabella", name: "眉間", description: "眉間のムダ毛をすっきりと。", image: "/images/menu/face/female/glabella.jpg" },
  { id: "cheeks-sideburns", name: "両ほほ・もみあげ", description: "ほほと、もみあげ部分をまとめてケア。", image: "/images/menu/face/female/cheeks-sideburns.jpg" },
  { id: "mouth-area", name: "口まわり", description: "鼻下からあごまわりまで、口元をまとめてケア。", image: "/images/menu/face/female/mouth-area.jpg" },
];

const maleFace: HairRemovalFacePart[] = [
  { id: "forehead", name: "おでこ", description: "額のムダ毛をすっきりと。", image: "/images/menu/face/male/forehead.jpg" },
  { id: "eyebrow", name: "眉上", description: "眉の上のムダ毛をきれいに整えます。", image: "/images/menu/face/male/eyebrow.jpg" },
  { id: "glabella", name: "眉間", description: "眉間のムダ毛をすっきりと。", image: "/images/menu/face/male/glabella.jpg" },
  { id: "cheeks-sideburns", name: "両ほほ・もみあげ", description: "ほほと、もみあげ部分をまとめてケア。", image: "/images/menu/face/male/cheeks-sideburns.jpg" },
  { id: "upper-lip", name: "鼻下", description: "鼻下のムダ毛をすっきりと。", image: "/images/menu/face/male/upper-lip.jpg" },
  { id: "chin", name: "あごひげ", description: "あごのムダ毛をきれいに整えます。", image: "/images/menu/face/male/chin.jpg" },
];

const armParts: HairRemovalSubPart[] = [
  { id: "upper-arms", name: "ひじ上", description: "肩からひじまでのムダ毛をケアします。", imageKey: "upper-arms" },
  { id: "forearms", name: "ひじ下", description: "ひじから手首までのムダ毛をケアします。", imageKey: "forearms" },
  { id: "hands", name: "手の甲・指", description: "手の甲から指までをまとめてケアします。", imageKey: "hands" },
];

const legParts: HairRemovalSubPart[] = [
  { id: "thigh-front", name: "太もも表", description: "太ももの前側をケアします。", imageKey: "thigh-front" },
  { id: "thigh-back", name: "太もも裏", description: "太ももの後ろ側をケアします。", imageKey: "thigh-back" },
  { id: "lower-leg-front", name: "ひざ下表", description: "ひざ下の前側をケアします。", imageKey: "lower-leg-front" },
  { id: "lower-leg-back", name: "ひざ下裏", description: "ひざ下の後ろ側をケアします。", imageKey: "lower-leg-back" },
  { id: "feet", name: "足の甲・指", description: "足の甲から足指までをまとめてケアします。", imageKey: "feet" },
];

const body: HairRemovalBodyPart[] = [
  { id: "full-body", name: "全身脱毛", description: "顔を含む全身をまとめてケアするメニューです。VIOは行っておりません。", imageKey: "full-body" },
  { id: "face-all", name: "顔全体", description: "顔全体をまとめてケアするメニューです。", imageKey: "face-all" },
  { id: "face", name: "顔の部位", description: "おでこ・眉上・眉間・ほほなど、細かい部位から選べます。", imageKey: "face-all" },
  { id: "neck", name: "首", description: "首まわりをすっきりと整えます。", imageKey: "neck" },
  { id: "chest", name: "胸", description: "胸まわりのムダ毛をケアします。", imageKey: "chest" },
  { id: "abdomen", name: "お腹", description: "お腹まわりをすっきりと。", imageKey: "abdomen" },
  { id: "underarms", name: "わき", description: "わきのムダ毛をケアします。", imageKey: "underarms" },
  { id: "arms", name: "腕全体", description: "ひじ上・ひじ下・手の甲・指をまとめてケアします。", imageKey: "arms" },
  { id: "arm-parts", name: "腕の部位", description: "ひじ上・ひじ下・手の甲・指から選べます。", imageKey: "arms" },
  { id: "back", name: "背中", description: "背中をまとめてケアします。", imageKey: "back" },
  { id: "legs", name: "脚全体", description: "太もも・ひざ下・足の甲・指をまとめてケアします。", imageKey: "legs" },
  { id: "leg-parts", name: "脚の部位", description: "太もも・ひざ下・足の甲・指から選べます。", imageKey: "legs" },
];

export const hairRemoval = {
  coverImage: "/images/menu/cover/hair-removal-menu.jpg",
  female: {
    label: "女性",
    overviewImage: "/images/menu/body/female/full-body.jpg",
    faceAllImage: "/images/menu/face/female-face-all.jpg",
    face: femaleFace,
  },
  male: {
    label: "男性",
    overviewImage: "/images/menu/body/male/full-body.jpg",
    faceAllImage: "/images/menu/face/male-face-all.jpg",
    face: maleFace,
  },
  body,
  armParts,
  legParts,
};

export const menuItems: MenuItem[] = [
  {
    category: "HAIR REMOVAL",
    name: "脱毛",
    price: "料金未定",
    description: "女性・男性それぞれのメニューに合わせ、全身・顔・各部位から選べる脱毛メニューです。全身脱毛は顔を含み、VIOは行っていません。",
    image: hairRemoval.coverImage,
    detailType: "hair-removal",
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
    description: "twenty oneでご案内するホワイトニングメニューです。料金・詳細は決まり次第掲載します。",
  },
];
