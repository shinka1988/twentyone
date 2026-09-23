from PIL import Image, ImageFilter, ImageDraw
import numpy as np
from pathlib import Path
ROOT=Path('/mnt/data/v16work'); BASE=ROOT/'public/images/menu/body'
PINK=np.array([234,169,176],dtype=np.float32)

def neutralize(img):
    a=np.asarray(img.convert('RGB')).astype(np.float32)
    r,g,b=a[...,0],a[...,1],a[...,2]
    # remove obvious old pink/cyan treatment washes while retaining illustration shading
    pink=(r-g>9)&(r-b>12)&(r>170)&(g>115)
    cyan=(b-r>5)&(b-g>0)&(b>150)&(g>130)
    mask=pink|cyan
    lum=0.299*r+0.587*g+0.114*b
    # warm neutral skin-like reconstruction
    nr=lum*0.99+5; ng=lum*0.985+8; nb=lum*0.97+12
    strength=np.clip(np.maximum(np.abs(r-g)-5, np.abs(b-r)-3)/45,0,1)*0.75
    strength=np.where(mask,strength,0)
    a[...,0]=np.where(mask,a[...,0]*(1-strength)+nr*strength,a[...,0])
    a[...,1]=np.where(mask,a[...,1]*(1-strength)+ng*strength,a[...,1])
    a[...,2]=np.where(mask,a[...,2]*(1-strength)+nb*strength,a[...,2])
    return Image.fromarray(np.uint8(np.clip(a,0,255)))

def skin_mask(base):
    a=np.asarray(base.convert('RGB')).astype(np.int16); r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
    m=((r>165)&(g>105)&(b>95)&(r-g>4)&(g-b>-5)&(r-g<100)).astype(np.uint8)*255
    # close tiny gaps, then soften
    m=Image.fromarray(m).filter(ImageFilter.GaussianBlur(1.2))
    return np.asarray(m).astype(np.float32)/255.0

def make(base, polys, alpha=115):
    mask=Image.new('L',base.size,0); d=ImageDraw.Draw(mask)
    for p in polys: d.polygon(p,fill=255)
    mask=np.asarray(mask).astype(np.float32)/255.0
    sm=skin_mask(base)
    mask*=sm
    mask=Image.fromarray(np.uint8(mask*255)).filter(ImageFilter.GaussianBlur(4))
    ov=Image.new('RGBA',base.size,(234,169,176,0)); ov.putalpha(mask.point(lambda x:int(x*alpha/255)))
    return Image.alpha_composite(base.convert('RGBA'),ov).convert('RGB')

# Same exact framing as arms.jpg. Polygons are tight and then clipped to skin pixels.
arm_masks={
'upper-arms':[[(247,28),(274,30),(281,90),(280,155),(276,220),(267,255),(248,250),(243,205),(242,145),(243,80)],[(426,30),(453,28),(457,80),(458,145),(457,205),(452,250),(433,255),(424,220),(420,155),(419,90)]],
'forearms':[[(244,232),(276,240),(274,300),(267,360),(258,395),(240,395),(233,365),(236,300)],[(424,240),(456,232),(464,300),(467,365),(460,395),(442,395),(433,360),(426,300)]],
'hands':[[(223,375),(246,388),(263,414),(261,445),(247,461),(230,451),(220,425),(216,400)],[(454,388),(477,375),(484,400),(480,425),(470,451),(453,461),(439,445),(437,414)]]}
leg_masks={
'thigh-front':[[(286,5),(343,5),(348,65),(346,130),(342,195),(337,250),(291,250),(285,195),(282,130),(283,65)],[(357,5),(414,5),(417,65),(418,130),(415,195),(409,250),(363,250),(358,195),(354,130),(352,65)]],
'thigh-back':[[(286,5),(343,5),(348,65),(346,130),(342,195),(337,250),(291,250),(285,195),(282,130),(283,65)],[(357,5),(414,5),(417,65),(418,130),(415,195),(409,250),(363,250),(358,195),(354,130),(352,65)]],
'lower-leg-front':[[(291,245),(337,245),(338,310),(335,375),(329,440),(322,492),(299,492),(290,440),(285,375),(286,310)],[(363,245),(409,245),(414,310),(415,375),(410,440),(401,492),(378,492),(371,440),(365,375),(362,310)]],
'lower-leg-back':[[(291,245),(337,245),(338,310),(335,375),(329,440),(322,492),(299,492),(290,440),(285,375),(286,310)],[(363,245),(409,245),(414,310),(415,375),(410,440),(401,492),(378,492),(371,440),(365,375),(362,310)]],
'feet':[[(286,420),(320,420),(330,447),(329,486),(320,510),(297,510),(281,490),(278,454)],[(380,420),(414,420),(422,454),(419,490),(403,510),(380,510),(371,486),(370,447)]]}

for gender in ['female','male']:
    out=BASE/gender
    arm_base=neutralize(Image.open(out/'arms.jpg'))
    leg_base=neutralize(Image.open(out/'legs.jpg'))
    for k,polys in arm_masks.items(): make(arm_base,polys).save(out/f'{k}.jpg',quality=95,optimize=True)
    for k,polys in leg_masks.items(): make(leg_base,polys).save(out/f'{k}.jpg',quality=95,optimize=True)
    # Ensure male underarm highlight is pink if any cyan tint exists.
    f=out/'underarms.jpg'; im=Image.open(f).convert('RGB'); a=np.asarray(im).astype(np.float32); r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
    cyan=(b-r>5)&(b-g>0)&(b>145)&(g>120)
    # tint only cyan pixels toward pink while preserving brightness
    a[cyan,0]=np.minimum(255,a[cyan,0]*0.72+234*0.28)
    a[cyan,1]=np.minimum(255,a[cyan,1]*0.78+169*0.22)
    a[cyan,2]=np.minimum(255,a[cyan,2]*0.78+176*0.22)
    Image.fromarray(np.uint8(np.clip(a,0,255))).save(f,quality=95,optimize=True)

# exact requested wording
p=ROOT/'src/data/menu.ts'; s=p.read_text(); s=s.replace('両ワキ','わき'); p.write_text(s)
