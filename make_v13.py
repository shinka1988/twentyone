from PIL import Image
from pathlib import Path
import numpy as np

ROOT=Path('/mnt/data/v13work')
body=ROOT/'public/images/menu/body'
face=ROOT/'public/images/menu/face/male'

target=np.array([244,204,200],dtype=float)

def recolor_blue(p):
    im=Image.open(p).convert('RGB')
    a=np.array(im).astype(float)
    R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
    mask=(B > R+2) & (B > G+1) & (R < 245) & (G < 245) & (B < 245)
    lum=0.299*R+0.587*G+0.114*B
    # map blue/gray highlight to the same soft pink family, preserving lightness
    out=a.copy()
    tr=np.clip(lum*1.13,0,255)
    tg=np.clip(lum*0.95,0,255)
    tb=np.clip(lum*0.93,0,255)
    out[:,:,0][mask]=tr[mask]
    out[:,:,1][mask]=tg[mask]
    out[:,:,2][mask]=tb[mask]
    Image.fromarray(out.astype('uint8')).save(p,quality=96)

# Normalize every male body/face highlight away from blue.
for p in (body/'male').glob('*.jpg'):
    recolor_blue(p)
for p in face.glob('*.jpg'):
    recolor_blue(p)

# High-resolution zoom crops. Source is 900x1200 full-body, so these are true crops, not stretched.
def crop_full(gender, box, outname):
    src=Image.open(body/gender/'full-body.jpg').convert('RGB')
    crop=src.crop(box)
    crop.save(body/gender/outname,quality=96)

# Upper body: head through hips/upper thighs, both arms fully visible.
for gender in ['female','male']:
    crop_full(gender,(110,70,790,700),'arms.jpg')
    # Lower body: hips through feet, enlarged for legs.
    crop_full(gender,(120,420,780,1190),'legs.jpg')

# Subpart cards: crop the dedicated highlighted source to the relevant region.
# Arms: use dedicated images and crop to the upper-body/arm region.
arm_boxes={
 'upper-arms': (90,120,610,700),
 'forearms': (90,250,610,820),
 'hands': (110,500,590,980),
}
for gender in ['female','male']:
    for key,box in arm_boxes.items():
        src=Image.open(body/gender/f'{key}.jpg').convert('RGB')
        src.crop(box).save(body/gender/f'{key}.jpg',quality=96)

# Leg subparts: crop dedicated images tightly around legs/feet.
leg_boxes={
 'thigh-front': (110,260,610,800),
 'thigh-back': (110,250,610,800),
 'lower-leg-front': (150,420,570,980),
 'lower-leg-back': (150,420,570,980),
 'feet': (120,650,600,1000),
}
for gender in ['female','male']:
    for key,box in leg_boxes.items():
        src=Image.open(body/gender/f'{key}.jpg').convert('RGB')
        src.crop(box).save(body/gender/f'{key}.jpg',quality=96)
