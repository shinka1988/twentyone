from PIL import Image, ImageDraw, ImageChops
from pathlib import Path
ROOT=Path('/mnt/data/v13work'); OUT=ROOT/'public/images/menu/body'
F=Path('/mnt/data/a_clean_minimal_high_key_illustration_diagram_st.png')
M=Path('/mnt/data/a_clean_minimalist_illustration_medical_style_port.png')
FB=Path('/mnt/data/female_back_clean.jpg')
MB=Path('/mnt/data/a_clean_minimal_soft_pastel_neutral_illustration.png')
PINK=(237,213,211,145)

def mask_subject(im):
    rgb=im.convert('RGB'); p=rgb.load(); m=Image.new('L',rgb.size,0); mp=m.load()
    for y in range(rgb.height):
      for x in range(rgb.width):
        r,g,b=p[x,y]
        if min(r,g,b)<248 or (max(r,g,b)-min(r,g,b))>6: mp[x,y]=255
    return m

def apply(im, polys):
    mask=Image.new('L',im.size,0); d=ImageDraw.Draw(mask)
    for poly in polys: d.polygon(poly,fill=255)
    mask=ImageChops.multiply(mask,mask_subject(im)) if False else mask
    # subject clipping via intersection
    sm=mask_subject(im); mask=ImageChops.multiply(mask,sm)
    ov=Image.new('RGBA',im.size,PINK); ov.putalpha(mask.point(lambda v:int(v*PINK[3]/255)))
    return Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')

def save(im,path): im.save(path,quality=96,optimize=True)

def crop(src,box): return Image.open(src).convert('RGB').crop(box)

def make(g,src):
    # Upper-body zoom crop.
    a=crop(src,(250,250,774,1030))
    armL=[(105,90),(145,88),(150,185),(145,300),(135,430),(125,545),(112,610),(96,590),(102,520),(108,420),(110,300),(108,185)]
    armR=[(380,88),(420,90),(417,185),(418,300),(420,420),(430,520),(438,590),(422,610),(409,545),(399,430),(389,300),(382,185)]
    upperL=[(106,92),(145,90),(150,205),(146,300),(110,300),(108,205)]
    upperR=[(380,90),(419,92),(417,205),(418,300),(382,300),(378,205)]
    foreL=[(110,295),(146,295),(140,430),(128,545),(112,610),(96,590),(102,520),(108,420)]
    foreR=[(382,295),(418,295),(420,420),(430,520),(438,590),(422,610),(409,545),(399,430)]
    handL=[(96,585),(112,590),(128,620),(116,665),(97,648),(88,615)]
    handR=[(422,590),(438,585),(446,615),(437,648),(418,665),(410,620)]
    save(apply(a,[armL,armR]),OUT/g/'arms.jpg')
    save(apply(a,[upperL,upperR]),OUT/g/'upper-arms.jpg')
    save(apply(a,[foreL,foreR]),OUT/g/'forearms.jpg')
    hands=a.crop((80,565,455,690)); save(apply(hands,[[(10,20),(45,15),(70,75),(45,120),(20,100)],[(330,15),(365,20),(355,100),(330,120),(305,75)]]),OUT/g/'hands.jpg')

    # Lower-body zoom crop.
    l=crop(src,(270,520,754,1536))
    thighL=[(100,185),(165,175),(172,300),(168,430),(155,560),(143,650),(120,650),(112,560),(108,430),(102,300)]
    thighR=[(220,175),(285,185),(283,300),(277,430),(272,560),(260,650),(237,650),(225,560),(212,430),(215,300)]
    calfL=[(115,630),(145,630),(143,760),(138,870),(130,950),(112,990),(98,950),(108,870),(112,760)]
    calfR=[(238,630),(268,630),(270,760),(274,870),(286,950),(272,990),(256,950),(248,870),(242,760)]
    feetL=[(108,948),(132,948),(148,982),(150,1000),(95,1000),(92,980)]
    feetR=[(270,948),(292,948),(308,980),(305,1000),(250,1000),(252,982)]
    save(apply(l,[thighL,thighR,calfL,calfR,feetL,feetR]),OUT/g/'legs.jpg')
    # Individual true zoom crops
    th=l.crop((80,140,310,675)); save(apply(th,[[(20,35),(95,25),(100,250),(90,430),(70,520),(45,520),(25,420),(25,230)]]),OUT/g/'thigh-front.jpg')
    ll=l.crop((85,585,305,1016)); save(apply(ll,[[(25,30),(85,30),(90,180),(85,310),(70,405),(45,420),(25,340),(25,190)]]),OUT/g/'lower-leg-front.jpg')
    ft=l.crop((80,875,325,1016)); save(apply(ft,[[(25,70),(80,65),(100,95),(95,135),(5,135),(0,105)]]),OUT/g/'feet.jpg')

    # Back parts: use clean source and crop actual legs.
    if g=='female':
        b=Image.open(FB).convert('RGB')
        # Figure is centered; crop from hip to feet.
        back=b.crop((300,390,600,900)).resize((600,1020),Image.Resampling.LANCZOS)
        # target shapes only
        tf1=[(135,120),(285,120),(300,360),(275,470),(220,500),(170,470),(140,360)]
        tf2=[(315,120),(465,120),(460,360),(430,470),(380,500),(325,470),(300,360)]
        lb1=[(170,465),(270,465),(265,760),(230,970),(190,900),(165,700)]
        lb2=[(330,465),(430,465),(435,700),(410,900),(370,970),(335,760)]
    else:
        sheet=Image.open(MB).convert('RGB')
        back=sheet.crop((750,410,1110,1055)).resize((600,1075),Image.Resampling.LANCZOS)
        tf1=[(80,25),(285,25),(300,360),(275,460),(220,500),(150,460),(105,360)]
        tf2=[(315,25),(520,25),(495,360),(450,460),(390,500),(325,460),(300,360)]
        lb1=[(125,450),(275,450),(270,760),(235,1015),(180,1015),(135,760)]
        lb2=[(325,450),(475,450),(465,760),(420,1015),(365,1015),(330,760)]
    save(apply(back,[tf1,tf2]),OUT/g/'thigh-back.jpg')
    save(apply(back,[lb1,lb2]),OUT/g/'lower-leg-back.jpg')

for g,s in [('female',F),('male',M)]: make(g,s)
p=ROOT/'src/data/menu.ts'; s=p.read_text(encoding='utf-8').replace('ヒジ上','ひじ上').replace('ヒジ下','ひじ下'); p.write_text(s,encoding='utf-8')
