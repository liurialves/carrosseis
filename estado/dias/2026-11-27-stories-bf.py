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
O="/home/claude/carrosseis/posts/2026-11-27/stories-bf"; os.makedirs(O,exist_ok=True)
B=(255,255,255)
tela(FL("dunas-punhos-camisa-preta-1"),0.2,[("HOJE É BLACK FRIDAY",44,AM),("Eu não vou dar desconto.",84,B),("E vou te explicar por quê.",46,B)],f"{O}/01.jpg")
tela(FL("selfie-sem-camisa-serio"),0.25,[("UMA LIÇÃO CARA",44,AM),("Eu já comprei um carro de 450 €.",76,B),("Durou 2 meses. Só ligava empurrando.",46,B)],f"{O}/02.jpg")
tela(FL("home-office-headset"),0.3,[("NO SEU NEGÓCIO",44,AM),("Desconto enche a agenda uma semana.",72,B),("Quem paga a conta é o seu mês.",50,B)],f"{O}/03.jpg")
tela(FL("lagoa-biceps-de-frente-editada"),0.3,[("NO LUGAR DO DESCONTO",44,AM),("Dê um bônus que custa pouco a você.",70,B),("Exemplo de um personal: quem fechar 3 meses hoje ganha a avaliação e o plano por escrito.",42,B)],f"{O}/04.jpg")
tela(FL("selfie-jaqueta-verde"),0.15,[("E VOCÊ?",44,AM),("O que o seu negócio pode oferecer no lugar do desconto?",66,B)],f"{O}/05.jpg")
tela(f"{R}/assets/foto-perfil-liuri.jpg",0.3,[("EU TE AJUDO A MONTAR",40,AM),("Me mande CLIENTES aqui no direct.",72,AM),("Eu respondo pessoalmente e te digo o bônus certo para o seu negócio.",44,B)],f"{O}/06.jpg")
