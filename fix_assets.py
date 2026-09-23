from PIL import Image, ImageDraw
from pathlib import Path

ROOT=Path('/mnt/data/v10work')
F=Path('/mnt/data/a_clean_minimal_high_key_illustration_diagram_st.png')
M=Path('/mnt/data/a_clean_minimalist_illustration_medical_style_port.png')
MF=Path('/mnt/data/a_clean_minimal_softly_lit_pastel_watercolor_st.png')
OUT=ROOT/'public/images/menu/body'
COLOR=(237,213,211,150)


def prep(src):
    im=Image.open(src).convert('RGB')
    w,h=im.size
    crop_w=int(h*0.70)
    left=max(0,(w-crop_w)//2)
    im=im.crop((left,0,left+crop_w,h)).resize((700,1000),Image.LANCZOS)
    return im

def mask_front(gender, kind):
    # coordinates for 700x1000 front figure
    d=ImageDraw.Draw(gender,'RGBA'); c=COLOR
    if kind in ('arms','upper-arms','forearms','hands'):
        if kind in ('arms','upper-arms'):
            d.polygon([(257,274),(278,275),(282,330),(283,385),(278,435),(271,490),(265,540),(257,570),(245,552),(250,505),(254,450),(258,395),(257,335)],fill=c)
            d.polygon([(443,274),(422,275),(418,330),(417,385),(422,435),(429,490),(435,540),(443,570),(455,552),(450,505),(446,450),(442,395),(443,335)],fill=c)
        if kind=='forearms' or kind=='arms':
            d.polygon([(258,420),(273,425),(271,490),(265,540),(257,570),(245,552),(250,505),(254,460)],fill=c)
            d.polygon([(442,420),(427,425),(429,490),(435,540),(443,570),(455,552),(450,505),(446,460)],fill=c)
        if kind in ('hands','arms'):
            d.polygon([(245,548),(260,540),(267,565),(261,590),(250,600),(238,580)],fill=c)
            d.polygon([(455,548),(440,540),(433,565),(439,590),(450,600),(462,580)],fill=c)
    if kind in ('legs','thigh-front','lower-leg-front','feet'):
        if kind in ('legs','thigh-front'):
            d.polygon([(302,510),(343,512),(350,590),(349,670),(344,735),(337,795),(331,820),(312,820),(313,735),(310,670),(305,590)],fill=c)
            d.polygon([(357,512),(398,510),(395,590),(390,670),(387,735),(388,795),(390,820),(371,820),(363,795),(356,735),(351,670),(350,590)],fill=c)
        if kind in ('legs','lower-leg-front'):
            d.polygon([(313,700),(344,700),(337,795),(331,860),(326,905),(314,905),(309,850),(312,795)],fill=c)
            d.polygon([(356,700),(387,700),(388,795),(391,850),(386,905),(374,905),(369,860),(363,795)],fill=c)
        if kind in ('feet','legs'):
            d.polygon([(314,895),(330,895),(337,925),(334,955),(310,955),(300,940),(303,915)],fill=c)
            d.polygon([(374,895),(390,895),(401,915),(404,940),(394,955),(370,955),(367,925)],fill=c)
    return gender

for label,src in [('female',F),('male',M)]:
    for kind in ['arms','upper-arms','forearms','hands','legs','thigh-front','lower-leg-front','feet']:
        im=prep(src)
        mask_front(im,kind).save(OUT/label/f'{kind}.jpg',quality=95)

# Rebuild male face parts with the exact same highlight color used by the female cards.
face_out=ROOT/'public/images/menu/face/male'
base=Image.open(MF).convert('RGB').resize((900,900),Image.LANCZOS)
# crop/fit is already close; use full square canvas with base centered vertically
for name in ['forehead','eyebrow','glabella','cheeks-sideburns','upper-lip','chin']:
    im=base.copy(); d=ImageDraw.Draw(im,'RGBA'); c=COLOR
    if name=='forehead': d.polygon([(335,285),(565,285),(600,340),(555,385),(345,385),(300,340)],fill=c)
    elif name=='eyebrow': d.rounded_rectangle((350,385,550,425),radius=18,fill=c)
    elif name=='glabella': d.ellipse((425,385,475,435),fill=c)
    elif name=='cheeks-sideburns':
        d.ellipse((300,420,390,560),fill=c); d.ellipse((510,420,600,560),fill=c)
    elif name=='upper-lip': d.ellipse((410,530,490,575),fill=c)
    elif name=='chin': d.ellipse((400,575,500,650),fill=c)
    im.save(face_out/f'{name}.jpg',quality=95)
# male face-all should be clean
base.save(ROOT/'public/images/menu/face/male-face-all.jpg',quality=95)
