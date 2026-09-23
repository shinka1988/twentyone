from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from pathlib import Path
ROOT=Path('/mnt/data/v16work'); OUT=ROOT/'public/images/menu/body'
SOURCES={'female':'/mnt/data/a_clean_minimal_high_key_illustration_diagram_st.png','male':'/mnt/data/a_clean_minimalist_illustration_medical_style_port.png'}
P=(235,170,178)

def crop(src, kind):
    im=Image.open(src).convert('RGB')
    box=(100,220,924,920) if kind=='arms' else (100,650,924,1536)
    return im.crop(box).resize((700,520),Image.Resampling.LANCZOS)

def skinmask(im):
 a=np.asarray(im).astype(np.int16); r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
 m=((r>165)&(g>105)&(b>95)&(r-g>3)&(g-b>-12)&(r-g<110)).astype(np.uint8)*255
 return Image.fromarray(m).filter(ImageFilter.GaussianBlur(1))

def tint(base, polys, alpha=118):
 m=Image.new('L',base.size,0); d=ImageDraw.Draw(m)
 for p in polys:d.polygon(p,fill=255)
 arr=np.minimum(np.asarray(m),np.asarray(skinmask(base))).astype(np.uint8)
 m=Image.fromarray(arr).filter(ImageFilter.GaussianBlur(3))
 ov=Image.new('RGBA',base.size,P+(0,)); ov.putalpha(m.point(lambda x:int(x*alpha/255)))
 return Image.alpha_composite(base.convert('RGBA'),ov).convert('RGB')

arms={
'upper-arms':[[(215,78),(275,78),(282,155),(278,235),(268,292),(238,292),(227,235),(220,155)],[(425,78),(485,78),(480,155),(473,235),(462,292),(432,292),(422,235),(418,155)]],
'forearms':[[(220,225),(275,235),(270,315),(258,395),(240,440),(216,425),(207,375),(212,300)],[(425,235),(480,225),(488,300),(493,375),(484,425),(460,440),(442,395),(430,315)]],
'hands':[[(190,390),(225,405),(241,438),(238,480),(218,510),(194,493),(180,456)],[(475,405),(510,390),(520,456),(506,493),(482,510),(462,480),(459,438)]]}
legs={
'thigh-front':[[(230,0),(345,0),(355,65),(350,145),(343,235),(335,285),(292,285),(280,235),(273,145),(278,65)],[(355,0),(470,0),(422,65),(427,145),(420,235),(408,285),(365,285),(357,235),(350,145),(345,65)]],
'thigh-back':[[(230,0),(345,0),(355,65),(350,145),(343,235),(335,285),(292,285),(280,235),(273,145),(278,65)],[(355,0),(470,0),(422,65),(427,145),(420,235),(408,285),(365,285),(357,235),(350,145),(345,65)]],
'lower-leg-front':[[(285,255),(340,255),(345,325),(340,395),(333,470),(325,518),(298,518),(288,470),(282,395),(280,325)],[(360,255),(415,255),(420,325),(418,395),(410,470),(402,518),(375,518),(367,470),(360,395),(355,325)]],
'lower-leg-back':[[(285,255),(340,255),(345,325),(340,395),(333,470),(325,518),(298,518),(288,470),(282,395),(280,325)],[(360,255),(415,255),(420,325),(418,395),(410,470),(402,518),(375,518),(367,470),(360,395),(355,325)]],
'feet':[[(285,420),(320,420),(335,452),(335,490),(323,518),(298,518),(282,490),(278,452)],[(380,420),(415,420),(422,452),(418,490),(402,518),(378,518),(367,490),(365,452)]]}

for gender,src in SOURCES.items():
    arms_base=crop(src,'arms'); legs_base=crop(src,'legs')
    # Replace the overview images too, so the sub-part images are literally the same frame.
    full_arms=Image.new('RGB',arms_base.size,(255,255,255))
    # full arm highlight = union of upper/forearm/hands
    full_arms=tint(arms_base, arms['upper-arms']+arms['forearms']+arms['hands'], alpha=105)
    full_arms.save(OUT/gender/'arms.jpg',quality=95,optimize=True)
    full_legs=tint(legs_base, legs['thigh-front']+legs['lower-leg-front'], alpha=105)
    full_legs.save(OUT/gender/'legs.jpg',quality=95,optimize=True)
    for k,p in arms.items(): tint(arms_base,p).save(OUT/gender/f'{k}.jpg',quality=95,optimize=True)
    for k,p in legs.items(): tint(legs_base,p).save(OUT/gender/f'{k}.jpg',quality=95,optimize=True)

# Wording normalization
p=ROOT/'src/data/menu.ts'; s=p.read_text().replace('両ワキ','わき'); p.write_text(s)
# Keep breadcrumb natural: body = menu list; sublists = category; detail = item name.
p=ROOT/'src/components/Menu.astro'; s=p.read_text().replace('全身・顔','メニュー一覧'); p.write_text(s)
print('final same-frame rebuild complete')
