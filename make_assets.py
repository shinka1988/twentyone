from PIL import Image, ImageDraw, ImageFilter
import cv2, numpy as np, os, shutil
root='/mnt/data/v7inspect'
PINK=(198,150,154,88)
BORDER=(170,120,125,120)

def highlight(base_path, out_path, shapes):
    base=Image.open(base_path).convert('RGBA')
    ov=Image.new('RGBA', base.size, (0,0,0,0))
    d=ImageDraw.Draw(ov)
    for shape in shapes:
        kind=shape[0]; box=shape[1]
        if kind=='ellipse': d.ellipse(box, fill=PINK, outline=BORDER, width=2)
        elif kind=='rounded': d.rounded_rectangle(box, radius=shape[2], fill=PINK, outline=BORDER, width=2)
    # subtle soften
    ov=ov.filter(ImageFilter.GaussianBlur(0.5))
    Image.alpha_composite(base, ov).convert('RGB').save(out_path, quality=92)

# Face variants
for gender in ['female','male']:
    base=f'{root}/public/images/menu/face/{gender}-face-all.jpg'
    outdir=f'{root}/public/images/menu/face/{gender}'
    os.makedirs(outdir, exist_ok=True)
    # overwrite individual images from the same clean base, ensuring consistent alignment
    if gender=='female':
        shapes={
          'forehead':[('ellipse',(360,285,540,385))],
          'eyebrow':[('rounded',(335,380,425,414),20),('rounded',(475,380,565,414),20)],
          'glabella':[('ellipse',(420,395,480,455))],
          'cheeks-sideburns':[('ellipse',(300,410,410,520)),('ellipse',(490,410,600,520))],
          'mouth-area':[('ellipse',(350,475,550,600))],
        }
    else:
        shapes={
          'forehead':[('ellipse',(355,275,545,370))],
          'eyebrow':[('rounded',(330,355,425,392),20),('rounded',(475,355,570,392),20)],
          'glabella':[('ellipse',(420,370,480,430))],
          'cheeks-sideburns':[('ellipse',(295,395,410,515)),('ellipse',(490,395,605,515))],
          'upper-lip':[('ellipse',(370,455,530,520))],
          'chin':[('ellipse',(375,505,525,610))],
        }
    for name, ss in shapes.items():
        highlight(base, f'{outdir}/{name}.jpg', ss)

# Clean full-body and add correctly centered face highlight.
def clean_body(src, dst, old_circle_box, face_box):
    im=cv2.imread(src)
    mask=np.zeros(im.shape[:2], np.uint8)
    x1,y1,x2,y2=old_circle_box
    # elliptical mask around baked-in old circle
    cv2.ellipse(mask, ((x1+x2)//2,(y1+y2)//2), ((x2-x1)//2+5,(y2-y1)//2+5), 0, 0, 360, 255, -1)
    clean=cv2.inpaint(im, mask, 9, cv2.INPAINT_TELEA)
    rgba=Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGBA))
    ov=Image.new('RGBA', rgba.size, (0,0,0,0)); d=ImageDraw.Draw(ov)
    d.ellipse(face_box, fill=PINK, outline=BORDER, width=2)
    ov=ov.filter(ImageFilter.GaussianBlur(0.7))
    out=Image.alpha_composite(rgba,ov).convert('RGB')
    out.save(dst, quality=92)

clean_body(f'{root}/public/images/menu/body/female/full-body.jpg', f'{root}/public/images/menu/body/female/full-body.jpg', (300,70,395,165), (410,135,490,235))
clean_body(f'{root}/public/images/menu/body/male/full-body.jpg', f'{root}/public/images/menu/body/male/full-body.jpg', (330,70,425,165), (412,125,488,220))
print('done')
