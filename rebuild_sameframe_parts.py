from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from pathlib import Path

ROOT=Path('/mnt/data/v16work')
BASE=ROOT/'public/images/menu/body'
PINK=np.array([233,170,176],dtype=np.float32)

# The user wants every arm sub-part to use the exact same framing as the ARM overview,
# and every leg sub-part to use the exact same framing as the LEG overview. Only the
# highlight changes. We therefore neutralize the existing full-arm/full-leg tint first,
# then apply localized soft pink masks.

def neutralize(img):
    a=np.asarray(img.convert('RGB')).astype(np.float32)
    r,g,b=a[...,0],a[...,1],a[...,2]
    # Detect the stronger pink wash used by the old all-area highlight.
    mask=(r-g>10) & (r-b>14) & (r>175) & (g>125)
    # Reduce saturation toward a warm neutral skin tone while preserving luminance.
    lum=(0.299*r+0.587*g+0.114*b)
    nr=lum*0.985+7; ng=lum*0.98+10; nb=lum*0.965+14
    strength=np.clip((r-g-8)/45,0,1)*0.78
    for c,nc in enumerate([nr,ng,nb]):
        a[...,c]=np.where(mask, a[...,c]*(1-strength)+nc*strength, a[...,c])
    return Image.fromarray(np.uint8(np.clip(a,0,255)))

def apply_mask(base, polygons, blur=7, alpha=105):
    m=Image.new('L',base.size,0)
    from PIL import ImageDraw
    d=ImageDraw.Draw(m)
    for poly in polygons:
        d.polygon(poly, fill=255)
    m=m.filter(ImageFilter.GaussianBlur(blur))
    # keep highlight inside central body/arm region by using soft mask only; polygons are conservative.
    ov=Image.new('RGB',base.size,tuple(PINK.astype(int)))
    ov.putalpha(m.point(lambda x:int(x*alpha/255)))
    return Image.alpha_composite(base.convert('RGBA'),ov).convert('RGB')

# polygons for 700x520 arm frame. Coordinates are deliberately broad enough to remain visible,
# but do not spill into torso/legs.
arm_masks={
 'upper-arms': [
   [(238,25),(272,28),(286,100),(284,175),(278,248),(255,270),(236,238),(232,170),(233,90)],
   [(428,28),(462,25),(468,90),(469,170),(465,238),(444,270),(421,248),(416,175),(414,100)]],
 'forearms': [
   [(235,238),(278,250),(275,315),(268,380),(250,414),(228,395),(229,330)],
   [(422,250),(465,238),(471,330),(472,395),(450,414),(432,380),(425,315)]],
 'hands': [
   [(220,380),(250,398),(269,426),(264,456),(245,472),(225,453),(216,420)],
   [(450,398),(480,380),(484,420),(475,453),(455,472),(436,456),(431,426)]]
}

# legs frame 700x520: same composition for every leg sub-part.
leg_masks={
 'thigh-front': [[(286,20),(346,18),(351,80),(348,150),(342,225),(331,270),(291,270),(282,225),(279,150),(282,80)],
                 [(354,18),(414,20),(418,80),(421,150),(418,225),(409,270),(369,270),(358,225),(352,150),(349,80)]],
 'thigh-back': [[(286,20),(346,18),(351,80),(348,150),(342,225),(331,270),(291,270),(282,225),(279,150),(282,80)],
                [(354,18),(414,20),(418,80),(421,150),(418,225),(409,270),(369,270),(358,225),(352,150),(349,80)]],
 'lower-leg-front': [[(292,260),(330,260),(334,320),(332,390),(327,455),(317,500),(294,500),(286,455),(283,390),(286,320)],
                     [(370,260),(408,260),(414,320),(417,390),(410,455),(403,500),(380,500),(370,455),(365,390),(366,320)]],
 'lower-leg-back': [[(292,260),(330,260),(334,320),(332,390),(327,455),(317,500),(294,500),(286,455),(283,390),(286,320)],
                    [(370,260),(408,260),(414,320),(417,390),(410,455),(403,500),(380,500),(370,455),(365,390),(366,320)]],
 'feet': [[(286,430),(322,430),(330,458),(329,494),(322,510),(296,510),(282,490),(278,460)],
          [(378,430),(414,430),(422,460),(418,490),(404,510),(378,510),(371,494),(370,458)]]
}

for gender in ['female','male']:
    out=BASE/gender
    arms=Image.open(out/'arms.jpg')
    legs=Image.open(out/'legs.jpg')
    arm_base=neutralize(arms)
    leg_base=neutralize(legs)
    # Re-save overview base? Keep the current overview because it intentionally highlights the whole area.
    for key,polys in arm_masks.items():
        img=apply_mask(arm_base,polys,blur=6,alpha=115)
        img.save(out/f'{key}.jpg',quality=95,optimize=True)
    for key,polys in leg_masks.items():
        img=apply_mask(leg_base,polys,blur=6,alpha=115)
        img.save(out/f'{key}.jpg',quality=95,optimize=True)

# update labels and data keys
p=ROOT/'src/data/menu.ts'
s=p.read_text()
s=s.replace('name: "両ワキ", description: "両ワキのムダ毛をケアします。"','name: "わき", description: "わきのムダ毛をケアします。"')
s=s.replace('{ id: "upper-arms", name: "ひじ上", description: "肩からひじまでのムダ毛をケアします。", imageKey: "upper-arms" }','{ id: "upper-arms", name: "ひじ上", description: "肩からひじまでのムダ毛をケアします。", imageKey: "upper-arms" }')
# ensure exact subpart keys remain distinct but same frame
p.write_text(s)

# Fix breadcrumb body label wording: no "全身・顔" anywhere.
mp=ROOT/'src/components/Menu.astro'
ms=mp.read_text()
ms=ms.replace('"全身・顔"', '"メニュー一覧"')
mp.write_text(ms)

print('rebuilt same-frame arm/leg subparts and renamed わき')
