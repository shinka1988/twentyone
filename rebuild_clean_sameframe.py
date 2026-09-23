from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from pathlib import Path
ROOT=Path('/mnt/data/v16work'); OUT=ROOT/'public/images/menu/body'
SOURCES={'female':'/mnt/data/a_clean_minimal_high_key_illustration_diagram_st.png','male':'/mnt/data/a_clean_minimalist_illustration_medical_style_port.png'}
P=(235,170,178)
# Crop the clean, unhighlighted source into the same wide card frame for all arm subparts and all leg subparts.
def crop_frame(src, kind):
    im=Image.open(src).convert('RGB')
    if kind=='arms': box=(115,245,925,850)
    else: box=(115,675,925,1280)
    return im.crop(box).resize((700,520),Image.Resampling.LANCZOS)

def skinmask(im):
 a=np.asarray(im).astype(np.int16); r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
 m=((r>165)&(g>105)&(b>95)&(r-g>3)&(g-b>-12)&(r-g<110)).astype(np.uint8)*255
 return Image.fromarray(m).filter(ImageFilter.GaussianBlur(1))

def highlight(base, polys):
 m=Image.new('L',base.size,0); d=ImageDraw.Draw(m)
 for p in polys:d.polygon(p,fill=255)
 # constrain to body skin so nothing spills into white background/clothes
 m=np.minimum(np.asarray(m),np.asarray(skinmask(base))).astype(np.uint8)
 m=Image.fromarray(m).filter(ImageFilter.GaussianBlur(3))
 ov=Image.new('RGBA',base.size,P+(0,)); ov.putalpha(m.point(lambda x:int(x*120/255)))
 return Image.alpha_composite(base.convert('RGBA'),ov).convert('RGB')

arm_polys={
'upper-arms':[[(220,90),(275,90),(286,185),(282,270),(268,315),(239,315),(226,270),(220,185)],[(425,90),(480,90),(474,185),(468,270),(455,315),(426,315),(412,270),(414,185)]],
'forearms':[[(232,260),(276,265),(279,340),(272,405),(255,445),(230,430),(223,380)],[(424,265),(468,260),(477,380),(470,430),(445,445),(428,405),(421,340)]],
'hands':[[(215,405),(245,420),(262,452),(255,490),(235,505),(214,485),(205,450)],[(455,420),(485,405),(495,450),(486,485),(465,505),(445,490),(438,452)]]}
leg_polys={
'thigh-front':[[(282,0),(345,0),(353,70),(350,145),(344,225),(335,275),(292,275),(284,225),(278,145),(279,70)],[(355,0),(418,0),(421,70),(422,145),(416,225),(408,275),(365,275),(356,225),(350,145),(347,70)]],
'thigh-back':[[(282,0),(345,0),(353,70),(350,145),(344,225),(335,275),(292,275),(284,225),(278,145),(279,70)],[(355,0),(418,0),(421,70),(422,145),(416,225),(408,275),(365,275),(356,225),(350,145),(347,70)]],
'lower-leg-front':[[(291,245),(337,245),(341,315),(338,385),(331,455),(323,515),(298,515),(289,455),(284,385),(287,315)],[(363,245),(409,245),(413,315),(416,385),(411,455),(402,515),(377,515),(369,455),(362,385),(359,315)]],
'lower-leg-back':[[(291,245),(337,245),(341,315),(338,385),(331,455),(323,515),(298,515),(289,455),(284,385),(287,315)],[(363,245),(409,245),(413,315),(416,385),(411,455),(402,515),(377,515),(369,455),(362,385),(359,315)]],
'feet':[[(290,420),(325,420),(337,450),(335,492),(325,518),(299,518),(283,490),(280,452)],[(375,420),(410,420),(420,452),(417,490),(401,518),(375,518),(365,492),(363,450)]]}
for gender,src in SOURCES.items():
    armbase=crop_frame(src,'arms'); legbase=crop_frame(src,'legs')
    for k,p in arm_polys.items(): highlight(armbase,p).save(OUT/gender/f'{k}.jpg',quality=95,optimize=True)
    for k,p in leg_polys.items(): highlight(legbase,p).save(OUT/gender/f'{k}.jpg',quality=95,optimize=True)
print('done')
