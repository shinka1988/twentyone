from PIL import Image
from pathlib import Path
import numpy as np, cv2

ROOT=Path('/mnt/data/v13fresh')
body=ROOT/'public/images/menu/body'
face=ROOT/'public/images/menu/face/male'
PINK=np.array([244,204,200],dtype=float)

def normalize_blue_highlight(path, roi=None):
    im=Image.open(path).convert('RGB')
    a=np.array(im).astype(float)
    R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
    # Original male highlight is a cool gray-blue; skin/background are warmer.
    lum=0.299*R+0.587*G+0.114*B
    mask=((B>=R-1)&(B>=G-1)&(lum<240)&(lum>165)).astype(np.uint8)*255
    if roi:
        x1,y1,x2,y2=roi
        rr=np.zeros_like(mask); rr[y1:y2,x1:x2]=255; mask=cv2.bitwise_and(mask,rr)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8))
    mask=cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=1)
    n, labels, stats, _=cv2.connectedComponentsWithStats(mask,8)
    outmask=np.zeros_like(mask)
    for i in range(1,n):
        area=stats[i,cv2.CC_STAT_AREA]
        if area>=120:
            pts=np.column_stack(np.where(labels==i))[:,::-1].astype(np.int32)
            if len(pts)>=3:
                hull=cv2.convexHull(pts)
                cv2.fillConvexPoly(outmask,hull,255)
    # Smooth edges; use strong tint so no blue/cyan remains visible.
    alpha=cv2.GaussianBlur(outmask,(0,0),3).astype(float)/255*0.90
    out=a*(1-alpha[:,:,None])+PINK*alpha[:,:,None]
    Image.fromarray(np.clip(out,0,255).astype('uint8')).save(path,quality=96)

# Restore clean source male body/face from the v12 archive, then normalize blue highlights.
# Specific ROIs prevent neutral white areas from being interpreted as highlights.
rois={
 'chest':(150,190,560,410),
 'abdomen':(170,330,540,560),
 'underarms':(130,180,580,520),
 'back':(140,170,560,650),
}
for name,roi in rois.items():
    normalize_blue_highlight(body/'male'/f'{name}.jpg',roi)
# Normalize any remaining blue on all male body detail images.
for p in body.joinpath('male').glob('*.jpg'):
    if p.name[:-4] not in rois:
        normalize_blue_highlight(p)
for p in face.glob('*.jpg'):
    normalize_blue_highlight(p)

# True zoom crops from the 900x1200 full-body illustrations (not CSS stretching).
def crop_full(gender, box, outname):
    src=Image.open(body/gender/'full-body.jpg').convert('RGB')
    src.crop(box).save(body/gender/outname,quality=96)
for gender in ['female','male']:
    crop_full(gender,(110,70,790,700),'arms.jpg')
    crop_full(gender,(120,420,780,1190),'legs.jpg')

# True zoom crops for subpart cards.
arm_boxes={'upper-arms':(90,120,610,700),'forearms':(90,250,610,820),'hands':(110,500,590,980)}
leg_boxes={'thigh-front':(110,260,610,800),'thigh-back':(110,250,610,800),'lower-leg-front':(150,420,570,980),'lower-leg-back':(150,420,570,980),'feet':(120,650,600,1000)}
for gender in ['female','male']:
    for key,box in arm_boxes.items():
        src=Image.open(body/gender/f'{key}.jpg').convert('RGB'); src.crop(box).save(body/gender/f'{key}.jpg',quality=96)
    for key,box in leg_boxes.items():
        src=Image.open(body/gender/f'{key}.jpg').convert('RGB'); src.crop(box).save(body/gender/f'{key}.jpg',quality=96)
