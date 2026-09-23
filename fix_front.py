from PIL import Image, ImageDraw, ImageChops
from pathlib import Path
ROOT=Path('/mnt/data/v10work'); F=Path('/mnt/data/a_clean_minimal_high_key_illustration_diagram_st.png'); M=Path('/mnt/data/a_clean_minimalist_illustration_medical_style_port.png')
COLOR=(237,213,211,150)
OUT=ROOT/'public/images/menu/body'

def prep(src):
 im=Image.open(src).convert('RGB'); w,h=im.size; cw=int(h*.70); left=(w-cw)//2; return im.crop((left,0,left+cw,h)).resize((700,1000),Image.LANCZOS)

def subject_mask(im):
 # Clip highlight to non-white illustration pixels.
 px=im.convert('RGB'); mask=Image.new('L',px.size,0); p=px.load(); m=mask.load()
 for y in range(px.height):
  for x in range(px.width):
   r,g,b=p[x,y]
   if min(r,g,b) < 246 or (max(r,g,b)-min(r,g,b)) > 7:
    m[x,y]=255
 return mask

def make(src, gender, kind):
 im=prep(src); w,h=im.size
 rough=Image.new('L',(w,h),0); d=ImageDraw.Draw(rough)
 if gender=='female':
  armL=[(250,270),(272,270),(276,340),(274,410),(268,480),(260,545),(248,575),(238,555),(246,490),(250,410),(250,340)]
  armR=[(428,270),(450,270),(450,340),(450,410),(454,490),(462,555),(452,575),(440,545),(432,480),(426,410),(424,340)]
  handL=[(236,535),(260,535),(268,565),(258,600),(244,605),(232,575)]
  handR=[(440,535),(464,535),(468,575),(456,605),(442,600),(432,565)]
  thighL=[(300,535),(340,530),(347,610),(345,690),(337,770),(325,845),(315,920),(300,920),(302,840),(307,760),(304,680)]
  thighR=[(360,530),(400,535),(396,680),(393,760),(398,840),(400,920),(385,920),(375,845),(363,770),(355,690),(353,610)]
  calfL=[(310,700),(345,700),(340,920),(325,960),(310,920)]
  calfR=[(355,700),(390,700),(390,920),(375,960),(360,920)]
  feetL=[(305,905),(330,905),(345,950),(340,975),(300,975),(292,950)]
  feetR=[(370,905),(395,905),(408,950),(400,975),(360,975),(355,950)]
 else:
  armL=[(248,255),(274,255),(278,335),(275,410),(268,485),(260,550),(248,580),(236,560),(245,490),(250,410),(248,335)]
  armR=[(426,255),(452,255),(452,335),(450,410),(455,490),(464,560),(452,580),(440,550),(432,485),(425,410),(422,335)]
  handL=[(232,530),(262,530),(270,565),(260,605),(242,610),(228,575)]
  handR=[(438,530),(468,530),(472,575),(458,610),(440,605),(430,565)]
  thighL=[(295,535),(340,530),(348,610),(346,690),(338,770),(326,845),(316,920),(300,920),(302,840),(306,760),(303,680)]
  thighR=[(360,530),(405,535),(402,680),(399,760),(404,840),(406,920),(390,920),(380,845),(368,770),(357,690),(355,610)]
  calfL=[(305,700),(345,700),(340,920),(325,960),(310,920)]
  calfR=[(355,700),(395,700),(395,920),(380,960),(365,920)]
  feetL=[(300,905),(330,905),(345,950),(340,975),(295,975),(288,950)]
  feetR=[(370,905),(400,905),(415,950),(405,975),(360,975),(355,950)]
 if kind in ('arms','upper-arms','forearms','hands'):
  if kind in ('arms','upper-arms'): d.polygon(armL,fill=255); d.polygon(armR,fill=255)
  if kind in ('arms','forearms'): 
   d.polygon([(245,390),(290,390),(280,590),(235,590)],fill=255); d.polygon([(410,390),(455,390),(465,590),(420,590)],fill=255)
  if kind in ('arms','hands'): d.polygon(handL,fill=255); d.polygon(handR,fill=255)
 if kind in ('legs','thigh-front','lower-leg-front','feet'):
  if kind in ('legs','thigh-front'): d.polygon(thighL,fill=255); d.polygon(thighR,fill=255)
  if kind in ('legs','lower-leg-front'): d.polygon(calfL,fill=255); d.polygon(calfR,fill=255)
  if kind in ('legs','feet'): d.polygon(feetL,fill=255); d.polygon(feetR,fill=255)
 rough=ImageChops.multiply(rough,subject_mask(im))
 overlay=Image.new('RGBA',(w,h),COLOR); overlay.putalpha(rough.point(lambda v: int(v*COLOR[3]/255)))
 out=Image.alpha_composite(im.convert('RGBA'),overlay).convert('RGB')
 out.save(OUT/gender/f'{kind}.jpg',quality=95)
for g,s in [('female',F),('male',M)]:
 for k in ['arms','upper-arms','forearms','hands','legs','thigh-front','lower-leg-front','feet']:
  make(s,g,k)
