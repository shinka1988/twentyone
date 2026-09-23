from PIL import Image, ImageDraw
from pathlib import Path
import numpy as np
ROOT=Path('/mnt/data/v15work')
PINK=(232,204,208,105)

sources={
 'female':Image.open('/mnt/data/a_clean_minimal_high_key_illustration_diagram_st.png').convert('RGBA'),
 'male':Image.open('/mnt/data/a_clean_minimalist_illustration_medical_style_port.png').convert('RGBA'),
}
# Region polygons in 1024x1536 source coords, conservative and anatomically centered.
regs={
'female':{
'upper-arms':[[(338,365),(382,375),(386,585),(365,625),(332,610)],[(642,375),(686,365),(692,610),(659,625),(638,585)]],
'forearms':[[(330,590),(370,610),(354,825),(330,875),(305,835)],[(654,610),(694,590),(719,835),(694,875),(670,825)]],
'hands':[[(300,820),(342,842),(344,935),(319,955),(290,905)],[(682,842),(724,820),(734,905),(705,955),(680,935)]],
'thigh-front':[[(392,730),(452,735),(478,800),(482,900),(475,1020),(456,1090),(430,1110),(407,1050),(397,950),(390,840)],[(572,735),(632,730),(634,840),(627,950),(617,1050),(594,1110),(568,1090),(549,1020),(542,900),(546,800)]],
'lower-leg-front':[[(428,1070),(470,1090),(488,1180),(486,1320),(478,1420),(456,1480),(432,1430),(425,1320),(422,1180)],[(554,1090),(596,1070),(602,1180),(599,1320),(592,1430),(568,1480),(546,1420),(538,1320),(536,1180)]],
'feet':[[(430,1430),(468,1440),(492,1485),(490,1518),(455,1528),(420,1498)],[(556,1440),(594,1430),(604,1498),(569,1528),(534,1518),(532,1485)]],
},
'male':{
'upper-arms':[[(305,350),(375,360),(386,590),(365,630),(312,605)],[(649,360),(719,350),(712,605),(659,630),(638,590)]],
'forearms':[[(305,590),(365,610),(350,835),(322,890),(288,842)],[(659,610),(719,590),(736,842),(702,890),(670,835)]],
'hands':[[(286,832),(340,850),(342,935),(308,970),(270,915)],[(684,850),(738,832),(754,915),(716,970),(682,935)]],
'thigh-front':[[(382,690),(455,700),(486,805),(488,930),(476,1045),(448,1120),(410,1080),(390,950),(382,820)],[(569,700),(642,690),(642,820),(634,950),(614,1080),(576,1120),(548,1045),(536,930),(538,805)]],
'lower-leg-front':[[(420,1060),(468,1085),(492,1190),(490,1330),(476,1435),(450,1495),(422,1440),(418,1320),(416,1180)],[(556,1085),(604,1060),(608,1180),(606,1320),(602,1440),(574,1495),(548,1435),(534,1330),(532,1190)]],
'feet':[[(420,1430),(465,1445),(494,1490),(492,1520),(450,1535),(412,1495)],[(559,1445),(604,1430),(612,1495),(574,1535),(532,1520),(530,1490)]],
}}
boxes={
'upper-arms':(270,300,755,700),'forearms':(260,560,760,930),'hands':(250,800,780,1000),'thigh-front':(360,660,670,1140),'lower-leg-front':(395,1040,625,1515),'feet':(390,1360,640,1536)}

def skinmask(arr):
    r,g,b=arr[:,:,0],arr[:,:,1],arr[:,:,2]
    # Soft skin detection; excludes near-white background and white underwear.
    return (r>180)&(g>140)&(b>125)&((r-g)>5)&((g-b)>1)&(r<255)&(g<252)

for gender,src in sources.items():
    out=ROOT/f'public/images/menu/body/{gender}'
    for key,box in boxes.items():
        crop=src.crop(box)
        arr=np.array(crop.convert('RGB'))
        sm=skinmask(arr)
        overlay=Image.new('RGBA',crop.size,(0,0,0,0))
        poly_mask=Image.new('L',crop.size,0); d=ImageDraw.Draw(poly_mask)
        ox,oy=box[:2]
        for poly in regs[gender][key]: d.polygon([(x-ox,y-oy) for x,y in poly],fill=255)
        pm=np.array(poly_mask)>0
        final=Image.fromarray(np.where((sm&pm)[...,None],np.array(PINK,dtype=np.uint8),0).astype(np.uint8),'RGBA')
        crop=Image.alpha_composite(crop,final).convert('RGB')
        crop.save(out/f'{key}.jpg',quality=95,optimize=True)

# Rear thigh/lower leg: use cleaner male front/back pair; female existing rear image is retained but cropped and de-tinted.
# Male back is second half of the 1536x1024 montage.
mb=Image.open('/mnt/data/a_clean_minimal_soft_pastel_neutral_illustration.png').convert('RGB')
# source 2048x1448: right figure x~790..1080, legs y~690..1320
for gender, src in [('male',mb)]:
    out=ROOT/f'public/images/menu/body/{gender}'
    arr=np.array(src)
    # rear figure crop for thigh and lower leg
    crop=src.crop((760,650,1130,1250))
    crop.save(out/'thigh-back.jpg',quality=95,optimize=True)
    crop2=src.crop((780,1040,1110,1435))
    crop2.save(out/'lower-leg-back.jpg',quality=95,optimize=True)
# Female rear image: crop existing cleaner depink source to focus on legs; apply no extra highlight outside body.
fback=Image.open('/mnt/data/user-2FNw5eYcZLfkZTO6Kcp0sMxz/5736930d0a4c4551b36d7a0f06cb6adf/mnt/data/user-2FNw5eYcZLfkZTO6Kcp0sMxz/f0ef4e6057a04150a02669995cdc79f1/mnt/data/female_back_depink_25.jpg').convert('RGB')
# crop around thighs from original 900x900
fback.crop((300,360,600,690)).save(ROOT/'public/images/menu/body/female/thigh-back.jpg',quality=95,optimize=True)
fback.crop((330,540,570,850)).save(ROOT/'public/images/menu/body/female/lower-leg-back.jpg',quality=95,optimize=True)
