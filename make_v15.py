from PIL import Image, ImageDraw
from pathlib import Path
import shutil, re

ROOT=Path('/mnt/data/v15work')
PINK=(231,207,210,115)

srcs={
 'female':Image.open('/mnt/data/a_clean_minimal_high_key_illustration_diagram_st.png').convert('RGBA'),
 'male':Image.open('/mnt/data/a_clean_minimalist_illustration_medical_style_port.png').convert('RGBA'),
}
# original source coordinate polygons, deliberately conservative so highlight stays on anatomy
regions={
 'upper-arms': lambda w,h: [
   [(335,360),(405,370),(405,610),(375,665),(330,635)],
   [(619,370),(689,360),(694,635),(649,665),(619,610)]],
 'forearms': lambda w,h: [
   [(330,625),(380,655),(360,850),(335,905),(300,855)],
   [(645,655),(695,625),(725,855),(690,905),(665,850)]],
 'hands': lambda w,h: [
   [(295,840),(340,855),(345,930),(320,955),(286,915)],
   [(680,855),(730,840),(738,915),(704,955),(678,930)]],
 'thigh-front': lambda w,h: [
   [(390,735),(500,730),(500,1110),(445,1145),(395,1080)],
   [(524,730),(634,735),(629,1080),(579,1145),(524,1110)]],
 'lower-leg-front': lambda w,h: [
   [(432,1080),(500,1095),(500,1440),(470,1480),(430,1435)],
   [(524,1095),(592,1080),(594,1435),(554,1480),(524,1440)]],
 'feet': lambda w,h: [
   [(435,1415),(495,1425),(505,1510),(455,1528),(420,1495)],
   [(525,1425),(585,1415),(600,1495),(565,1528),(515,1510)]],
}
# male anatomy is slightly wider; use same approximate central framing with wider polygons
male_regions={
 'upper-arms': [[(305,350),(395,355),(405,600),(370,655),(315,620)],[(629,355),(719,350),(709,620),(654,655),(619,600)]],
 'forearms': [[(315,610),(375,650),(355,850),(320,905),(290,850)],[(649,650),(709,610),(734,850),(700,905),(665,850)]],
 'hands': [[(285,845),(335,855),(338,935),(305,970),(270,920)],[(689,855),(739,845),(755,920),(720,970),(687,935)]],
 'thigh-front': [[(385,700),(505,700),(505,1115),(445,1160),(390,1080)],[(519,700),(639,700),(634,1080),(579,1160),(519,1115)]],
 'lower-leg-front': [[(430,1080),(505,1090),(505,1435),(465,1490),(425,1430)],[(519,1090),(594,1080),(599,1430),(559,1490),(519,1435)]],
 'feet': [[(425,1410),(500,1425),(505,1510),(450,1530),(415,1490)],[(524,1425),(599,1410),(610,1490),(575,1530),(520,1510)]],
}

# crop boxes tailored for each detail, preserving native pixels rather than stretching
crops={
 'upper-arms': (270,280,755,720),
 'forearms': (260,555,760,955),
 'hands': (245,805,780,990),
 'thigh-front': (350,665,680,1180),
 'thigh-back': (300,0,600,900), # replaced below using existing v13 back crops
 'lower-leg-front': (395,1040,635,1515),
 'lower-leg-back': (350,0,600,900),
 'feet': (380,1360,650,1536),
}

for gender,src in srcs.items():
    outdir=ROOT/f'public/images/menu/body/{gender}'
    outdir.mkdir(parents=True,exist_ok=True)
    regs=regions if gender=='female' else male_regions
    if gender=='female': regs={k:v(1024,1536) for k,v in regs.items()}
    for key in ['upper-arms','forearms','hands','thigh-front','lower-leg-front','feet']:
        box=crops[key]
        crop=src.crop(box)
        overlay=Image.new('RGBA',crop.size,(0,0,0,0))
        d=ImageDraw.Draw(overlay)
        ox,oy=box[:2]
        for poly in regs[key]:
            d.polygon([(x-ox,y-oy) for x,y in poly], fill=PINK)
        crop=Image.alpha_composite(crop,overlay).convert('RGB')
        crop.save(outdir/f'{key}.jpg',quality=94,optimize=True)

# Rebuild thigh-back / lower-leg-back from existing v13 images but normalize to same pink by recoloring near-highlight pixels.
# Keep their already-correct rear anatomy, only shift the highlight to conservative regions and remove any cyan.
for gender in ['female','male']:
    back_src=Image.open(ROOT/f'public/images/menu/body/{gender}/thigh-back.jpg').convert('RGB')
    # v13 image already has rear-thigh highlight; use it as source but recolor all obvious highlight tint to unified pink.
    import numpy as np
    arr=np.array(back_src).astype(np.int16)
    # detect saturated pink/blue highlight pixels relative to pale body: tint where R/B differ or saturation moderate
    # instead, gently map pixels with B-R > 4 (blue) or R-G > 4 (pink) in the body area toward pink.
    R,G,B=arr[:,:,0],arr[:,:,1],arr[:,:,2]
    mask=((B-R)>3)|((R-G)>5)
    # only pixels not near-white
    mask &= (R<245)
    arr[mask,0]=np.clip(arr[mask,0]+8,0,255)
    arr[mask,1]=np.clip(arr[mask,1]-2,0,255)
    arr[mask,2]=np.clip(arr[mask,2]-1,0,255)
    Image.fromarray(arr.astype(np.uint8)).save(ROOT/f'public/images/menu/body/{gender}/thigh-back.jpg',quality=94,optimize=True)

    lb=Image.open(ROOT/f'public/images/menu/body/{gender}/lower-leg-back.jpg').convert('RGB')
    arr=np.array(lb).astype(np.int16); R,G,B=arr[:,:,0],arr[:,:,1],arr[:,:,2]
    mask=(((B-R)>3)|((R-G)>5)) & (R<245)
    arr[mask,0]=np.clip(arr[mask,0]+8,0,255); arr[mask,1]=np.clip(arr[mask,1]-2,0,255); arr[mask,2]=np.clip(arr[mask,2]-1,0,255)
    Image.fromarray(arr.astype(np.uint8)).save(ROOT/f'public/images/menu/body/{gender}/lower-leg-back.jpg',quality=94,optimize=True)

# Feet crop a little higher, as requested.
# CSS already uses contain, so preserve native crop.

# Breadcrumb markup + script changes
p=ROOT/'src/components/Menu.astro'
s=p.read_text()
s=s.replace('''        <div class="hair-removal-breadcrumb" aria-live="polite">\n          <button type="button" data-level="body">全身</button>\n          <span>›</span>\n          <span class="hair-breadcrumb-current">全身・顔</span>\n        </div>''','''        <div class="hair-removal-breadcrumb" aria-live="polite">\n          <button type="button" data-level="body">脱毛</button>\n          <span>›</span>\n          <span class="hair-breadcrumb-parent">全身・顔</span>\n          <span class="hair-breadcrumb-separator" hidden>›</span>\n          <span class="hair-breadcrumb-current">全身・顔</span>\n        </div>''')
old='''    if (breadcrumbCurrent) {\n      breadcrumbCurrent.textContent = level === "body" ? "全身・顔" : level === "face" ? "顔の部位" : level === "arms" ? "腕の部位" : level === "legs" ? "脚の部位" : detailTitle?.textContent ?? "選択した部位";\n    }'''
new='''    const parent = document.querySelector<HTMLElement>(".hair-breadcrumb-parent");\n    const separator = document.querySelector<HTMLElement>(".hair-breadcrumb-separator");\n    const parentLabel = level === "body" ? "" : level === "face" ? "全身・顔" : level === "arms" ? "腕の部位" : level === "legs" ? "脚の部位" : previousListLevel === "face" ? "顔の部位" : previousListLevel === "arms" ? "腕の部位" : previousListLevel === "legs" ? "脚の部位" : "全身・顔";\n    const currentLabel = level === "body" ? "全身・顔" : level === "face" ? "顔の部位" : level === "arms" ? "腕の部位" : level === "legs" ? "脚の部位" : detailTitle?.textContent ?? "選択した部位";\n    if (parent) parent.textContent = parentLabel;\n    if (separator) separator.hidden = level === "body";\n    if (breadcrumbCurrent) breadcrumbCurrent.textContent = currentLabel;\n    if (level === "body" && parent) parent.textContent = "全身・顔";'''
s=s.replace(old,new)
p.write_text(s)

# remove duplicate parent on body via CSS hidden for body state handled by JS? Current markup would show 全身・顔 twice. JS sets parent same and current same.
# Instead alter showHairView to hide current for body via CSS class on container.

# Add data state class in script
s=s.replace('''    currentLevel = level;\n    views.forEach((view) => { view.hidden = view.dataset.view !== level; });''','''    currentLevel = level;\n    views.forEach((view) => { view.hidden = view.dataset.view !== level; });\n    const breadcrumb = document.querySelector<HTMLElement>(".hair-removal-breadcrumb");\n    breadcrumb?.classList.toggle("is-body", level === "body");''')
p.write_text(s)

# CSS breadcrumb body state and images
css=ROOT/'src/styles/global.css'
c=css.read_text()
c += '''\n\n.hair-removal-breadcrumb.is-body .hair-breadcrumb-separator,\n.hair-removal-breadcrumb.is-body .hair-breadcrumb-current { display: none; }\n'''
css.write_text(c)
