from PIL import Image
from pathlib import Path
import shutil
root=Path('/mnt/data/v10work/public/images/menu/face/male')
srcroot=Path('/mnt/data/v10orig/public/images/menu/face/male')
target=(237,213,211)
for name in ['forehead','eyebrow','glabella','cheeks-sideburns','upper-lip','chin']:
    im=Image.open(srcroot/f'{name}.jpg').convert('RGB')
    px=im.load(); w,h=im.size
    for y in range(120,680):
        for x in range(180,720):
            r,g,b=px[x,y]
            if r-g >= 14 and g-b >= 3 and r < 245 and g < 235:
                a=0.42
                px[x,y]=(int(r*(1-a)+target[0]*a),int(g*(1-a)+target[1]*a),int(b*(1-a)+target[2]*a))
    im.save(root/f'{name}.jpg',quality=95)
shutil.copy2(srcroot.parent/'male-face-all.jpg', root.parent/'male-face-all.jpg')
