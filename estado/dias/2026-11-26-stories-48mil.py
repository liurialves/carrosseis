import sys, os
sys.path.insert(0,"/home/claude/carrosseis/scripts")
from preset_liuri import aplicar
from PIL import Image, ImageDraw, ImageFont, ImageOps
R="/home/claude/carrosseis"; FL=lambda x:f"{R}/assets/fotos-liuri/{x}.jpg"; HP=lambda x:f"/tmp/h26/{x}.jpg"
W,H=1080,1920; AM=(245,197,24)
def font(sz,w="Bold"):
    f=ImageFont.truetype(f"{R}/assets/fonts/Inter.ttf",sz)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
def wrap(d,t,f,mw):
    out=[];l=""
    for w in t.split(" "):
        x=(l+" "+w).strip()
        if d.textlength(x,font=f)<=mw: l=x
        else: out.append(l); l=w
    out.append(l); return out
def tela(foto,foco,linhas,out,nota=None):
    im=aplicar(ImageOps.exif_transpose(Image.open(foto)).convert("RGB"))
    s=max(W/im.width,H/im.height); im=im.resize((int(im.width*s)+1,int(im.height*s)+1))
    x=(im.width-W)//2; y=int((im.height-H)*foco); im=im.crop((x,y,x+W,y+H))
    g=Image.new("L",(1,H)); 
    for i in range(H): g.putpixel((0,i),int(235*max(0,(i-H*0.38)/(H*0.62))**0.9))
    im.paste(Image.new("RGB",(W,H),"black"),(0,0),g.resize((W,H)))
    d=ImageDraw.Draw(im)
    blocos=[]
    for txt,sz,cor in linhas:
        txt=txt.replace("R$ ","R$\u00a0")
        f=font(sz); blocos.append([(l,f,cor) for l in wrap(d,txt,f,W-140)]+[None])
    hs=sum((it[1].size+14) if it else 30 for b in blocos for it in b)
    y=H-330-hs
    for b in blocos:
        for it in b:
            if it is None: y+=30; continue
            l,f,cor=it; tw=d.textlength(l,font=f)
            d.text(((W-tw)/2,y),l,font=f,fill=cor); y+=f.size+14
    if nota:
        f=font(28,"Regular"); tw=d.textlength(nota,font=f); d.text(((W-tw)/2,H-260),nota,font=f,fill=(210,210,210))
    im.save(out,quality=92)
O="/home/claude/carrosseis/posts/2026-11-26/stories-48mil"; os.makedirs(O,exist_ok=True)
B=(255,255,255)
tela(FL("dunas-punhos-camisa-preta-3"),0.25,[("EM 2026",44,AM),("Eu já faturei R$ 306.720.",84,B),("Comecei o ano com R$ 9.585 por mês.",46,B)],f"{O}/01.jpg","Valores convertidos de euro: 1 € = R$ 6,39 (26/11/2026)")
tela(FL("home-office-headset"),0.3,[("COMO",44,AM),("Eu fazia tudo sozinho.",78,B),("O conteúdo, os anúncios e o atendimento.",46,B)],f"{O}/02.jpg")
tela(HP("72"),0.4,[("EM 5 MESES",44,AM),("R$ 35.145 por mês.",84,B),("Depois, R$ 44.730 por mês, com massagem e sites para clientes.",44,B)],f"{O}/03.jpg")
tela(HP("73"),0.3,[("UM DOS ANÚNCIOS",44,AM),("R$ 1.610 investidos.",78,B),("Voltaram R$ 11.214 em atendimentos, de 15 a 31 de outubro.",46,B)],f"{O}/04.jpg")
tela(FL("selfie-jaqueta-verde"),0.15,[("E VOCÊ?",44,AM),("Quanto o seu negócio faturou em 2026?",72,B)],f"{O}/05.jpg")
tela(FL("lagoa-biceps-de-frente-editada"),0.3,[("O CARROSSEL COMPLETO ESTÁ NO FEED",40,AM),("Quer o mesmo sistema no seu negócio?",66,B),("Me mande CLIENTES aqui no direct.",66,AM),("Eu respondo pessoalmente.",42,B)],f"{O}/06.jpg")
