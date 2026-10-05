export const salonName = "twenty one";

export const salonAddress = "北海道札幌市豊平区平岸３条１３丁目５−２２　１Ｆ";

// Googleマップで確認した建物の位置（43.026738, 141.3693725）。
// 住所検索ではピンが出ないため、座標の赤いピンを共有した埋め込みを使用します。
// 地図の中心も同じ位置に指定しています。
export const mapEmbedUrl =
  "https://www.google.com/maps/embed?pb=!1m13!1m8!1m3!1d1458.3491290025183!2d141.3693725!3d43.026738!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zNDPCsDAxJzM2LjMiTiAxNDHCsDIyJzA5LjciRQ!5e0!3m2!1sja!2suk!4v1791206177793!5m2!1sja!2suk";

export const mapUrl =
  "https://www.google.com/maps/place/43%C2%B001'36.3%22N+141%C2%B022'09.7%22E/@43.026738,141.3693725,18z/data=!4m4!3m3!8m2!3d43.02675!4d141.3693611?hl=ja&entry=ttu&g_ep=EgoyMDI2MDkzMC4wIKXMDSoASAFQAw%3D%3D";

export const instagramUrl =
  "https://www.instagram.com/eyebrow.nail_21/";

export const lineUrl =
  "https://lin.ee/1ZlvOrl";

// シェアサロン募集状況
// true = 募集中 / false = 満席
export const shareSalonRecruiting = true;
export const shareSalonStatus = shareSalonRecruiting ? "募集中" : "満席";

// 写真を追加したら、パスのコメントを外してください。
// export const heroImage = "/images/hero/main.jpg";
// export const aboutImage = "/images/salon/about.jpg";
export const heroImage: string | undefined = "/images/hero/twenty-one-top.jpg";
export const heroMobileImage: string = "/images/hero/twenty-one-top-mobile.jpg";
export const aboutImage: string | undefined = undefined;
