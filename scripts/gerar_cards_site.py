"""Gera cards de marca com textos reais do site lisboamassagem.pt (paleta do site).
Uso: python3 scripts/gerar_cards_site.py  -> assets/spa-site/*.jpg (1200x1500)"""
import os, sys
sys.path.insert(0, "/mnt/skills/plugins/um-clique-darkgram/references")
from render import _fonts_b64
from playwright.sync_api import sync_playwright
F = _fonts_b64()
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "spa-site")
CARDS = {
 "01-home": ("lisboamassagem.pt", "Encontre o seu equilíbrio com terapeutas verificados.", ["Terapeutas verificados", "Contacto direto por WhatsApp", "Também ao domicílio"], "Pedir massagem agora"),
 "02-busca": ("Pesquisa", "Encontre exatamente o tipo de massagem que procura", ["Por distrito", "Por tipo de massagem", "Pelo nome do terapeuta"], "Explorar"),
 "03-como-funciona": ("Como funciona", "Escolhe, fala com o terapeuta e marca.", ["1  Escolhe o terapeuta", "2  Fala por WhatsApp", "3  Marca o dia que te dá jeito"], "Pedir massagem agora"),
 "04-terapeutas": ("Para terapeutas", "Quer fazer parte da maior plataforma de massagens de Portugal?", ["Registo grátis", "Perfil publicado grátis", "Plano Elite com destaque na pesquisa"], "Anuncie-se grátis"),
}
CSS = f"""
@font-face{{font-family:'Bebas';src:url(data:font/woff2;base64,{F['BEBAS']}) format('woff2')}}
@font-face{{font-family:'Neue';src:url(data:font/woff2;base64,{F['NEUE_ROMAN']}) format('woff2');font-weight:400}}
@font-face{{font-family:'Neue';src:url(data:font/woff2;base64,{F['NEUE_BOLD']}) format('woff2');font-weight:800}}
*{{margin:0;padding:0;box-sizing:border-box}}
.c{{width:1200px;height:1500px;background:radial-gradient(110% 70% at 50% 0%,#3a2c22 0%,#1E1712 60%);color:#F4EDE4;font-family:'Neue';position:relative;overflow:hidden}}
.win{{position:absolute;left:90px;right:90px;top:120px;height:760px;background:#F4EDE4;border-radius:28px;box-shadow:0 40px 80px rgba(0,0,0,.45);overflow:hidden;color:#1E1712}}
.bar{{height:64px;background:#e7ddd1;display:flex;align-items:center;gap:12px;padding:0 26px}}
.dot{{width:16px;height:16px;border-radius:50%;background:#C9A486}}
.url{{margin-left:20px;background:#fff;border-radius:30px;padding:8px 26px;font-size:24px;color:#8A6448}}
.in{{padding:56px 60px}}
.tag{{font-size:24px;font-weight:800;letter-spacing:4px;text-transform:uppercase;color:#8A6448}}
.h{{font-family:'Bebas';font-size:92px;line-height:.95;margin:22px 0 34px;color:#1E1712}}
.li{{font-size:32px;margin:14px 0;display:flex;gap:16px;align-items:center}}
.li:before{{content:'';width:14px;height:14px;border-radius:50%;background:#C9A486;flex:none}}
.btn{{position:absolute;left:150px;right:150px;top:960px;height:120px;border-radius:60px;background:#C9A486;color:#1E1712;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center}}
.foot{{position:absolute;bottom:90px;width:100%;text-align:center;font-family:'Bebas';font-size:64px;letter-spacing:3px;color:#C9A486}}
"""
os.makedirs(OUT, exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={"width":1200,"height":1500})
    for nome,(tag,h,itens,btn) in CARDS.items():
        lis = "".join(f'<div class="li">{i}</div>' for i in itens)
        html = f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=c>
<div class=win><div class=bar><span class=dot></span><span class=dot></span><span class=dot></span><span class=url>lisboamassagem.pt</span></div>
<div class=in><div class=tag>{tag}</div><div class=h>{h}</div>{lis}</div></div>
<div class=btn>{btn}</div><div class=foot>LISBOAMASSAGEM.PT</div></div></body></html>"""
        pg.set_content(html); pg.evaluate("() => document.fonts.ready"); pg.wait_for_timeout(400)
        pg.locator(".c").screenshot(path=f"{OUT}/{nome}.png")
        from PIL import Image
        Image.open(f"{OUT}/{nome}.png").convert("RGB").save(f"{OUT}/{nome}.jpg", quality=90); os.remove(f"{OUT}/{nome}.png")
    br.close()
print("ok")
