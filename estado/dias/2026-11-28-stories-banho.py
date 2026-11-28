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
O="/home/claude/carrosseis/posts/2026-11-28/stories-banho"; os.makedirs(O,exist_ok=True)
B=(255,255,255)
tela(FL("selfie-sem-camisa-serio"),0.25,[("AGORA HÁ POUCO",44,AM),("Acabei de tomar um banho gelado.",80,B),("Não é moda. Eu te explico por que eu faço.",46,B)],f"{O}/01.jpg")
tela(FL("lagoa-biceps-de-frente"),0.3,[("UM ESTUDO NA HOLANDA",44,AM),("Mais de 3.000 pessoas. 30 dias.",72,B),("Pelo menos 30 segundos de água fria no fim do banho.",46,B)],f"{O}/02.jpg","Buijze e colegas, PLOS ONE, 2016")
tela(FL("dunas-punhos-camisa-preta-2"),0.2,[("O RESULTADO",44,AM),("29% menos faltas ao trabalho.",80,B),("Ficaram doentes o mesmo número de dias, mas conseguiram trabalhar mesmo assim.",44,B)],f"{O}/03.jpg")
tela(FL("home-office-headset"),0.3,[("E MAIS",44,AM),("Disseram ter mais energia.",76,B),("Dois terços continuaram depois dos 30 dias.",46,B)],f"{O}/04.jpg","Tem algum problema de saúde? Fale com o seu médico antes.")
tela(FL("dunas-punhos-camisa-preta-3"),0.2,[("PARA MIM",44,AM),("Eu faço uma coisa difícil de propósito, antes de qualquer outra.",66,B),("No negócio é igual: a mensagem que você adia, o preço que você não sobe.",44,B)],f"{O}/05.jpg")
tela(f"{R}/assets/avatar-liuri.jpg",0.3,[("E VOCÊ?",40,AM),("Qual é a tarefa difícil que você vem adiando no seu negócio?",62,B),("Me mande CLIENTES aqui no direct.",66,AM)],f"{O}/06.jpg")
