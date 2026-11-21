"""Formato LEGENDA (dono, 16/11/2026; molde @therealbrianmark): carrossel de fala, cada slide = 2 fotos/frames do
Liuri empilhados (1080x675 cada) com a frase em estilo legenda de vídeo (branca, contorno escuro) na base de cada metade.
Uso: python3 scripts/render_legenda.py cfg.json PASTA_SAIDA
cfg = {"slides": [{"fotos": ["/a.jpg", "/b.jpg"], "foco": [0.35, 0.35], "textos": ["metade de cima", "metade de baixo"]}, ...]}
Saída: CAPA.jpg (slide 1) e fatia-1.jpg.. (slides 2..n).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
W, H, HH = 1080, 1350, 675
MAXW = 880  # largura máxima da legenda (centrada, sem encostar nas bordas)



def _preset(im, caminho):
    """Preset do Liuri (dono, 18/11/2026) nas fotos dele; nunca em Pexels nem em prints de prova."""
    c = str(caminho).lower()
    if "editada" in c or "pexels" in c or "prova" in c or "/ps" in c or "print" in c:
        return im
    import sys as _s, os as _o
    _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
    from preset_liuri import aplicar
    return aplicar(im)

def fonte(t):
    f = ImageFont.truetype(os.path.join(R, "assets/fonts/Inter.ttf"), t)
    try: f.set_variation_by_name("Bold")
    except Exception: pass
    return f


def quebra(d, txt, f, maxw):
    linhas, cur = [], ""
    for p in txt.split():
        t = (cur + " " + p).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: linhas.append(cur); cur = p
    if cur: linhas.append(cur)
    return linhas


def metade(path, foco, texto):
    src = _preset(ImageOps.exif_transpose(Image.open(path)).convert("RGB"), path)
    if src.width / src.height < 1.2:
        # foto/frame em pé: mostra cabeça e ombros (recorte de ~52% da altura) e completa as laterais com a própria
        # imagem desfocada, em vez de ampliar o rosto até cortar
        ch = int(src.height * 0.6); y0 = int((src.height - ch) * foco)
        recorte = src.crop((0, y0, src.width, y0 + ch))
        fg = recorte.resize((int(recorte.width * HH / ch), HH), Image.LANCZOS)
        bg = ImageOps.fit(recorte, (W, HH)).filter(ImageFilter.GaussianBlur(40))
        bg = ImageEnhance.Brightness(bg).enhance(0.55)
        im = bg.copy(); im.paste(fg, ((W - fg.width) // 2, 0))
        im = im.filter(ImageFilter.UnsharpMask(2, 60, 2))
    else:
        esc = max(W / src.width, HH / src.height)
        src = src.resize((int(src.width * esc + 0.5), int(src.height * esc + 0.5)), Image.LANCZOS)
        y0 = int((src.height - HH) * foco); x0 = (src.width - W) // 2
        im = src.crop((x0, y0, x0 + W, y0 + HH)).filter(ImageFilter.UnsharpMask(2, 80, 2))
    im = ImageEnhance.Brightness(ImageEnhance.Color(im).enhance(0.85)).enhance(0.78)
    # vinheta escura embaixo para a legenda
    g = Image.new("L", (1, HH)); [g.putpixel((0, y), int(170 * max(0, (y - HH * 0.45) / (HH * 0.55)) ** 1.4)) for y in range(HH)]
    im = Image.composite(Image.new("RGB", (W, HH), (0, 0, 0)), im, g.resize((W, HH)))
    d = ImageDraw.Draw(im)
    # legenda centrada, em 1 ou 2 linhas equilibradas, larga como no molde, com sombra (não só contorno)
    pal = texto.split()
    def melhor(f):
        if d.textlength(texto, font=f) <= MAXW: return [texto]
        cands = [(" ".join(pal[:k]), " ".join(pal[k:])) for k in range(1, len(pal))]
        return list(min(cands, key=lambda c: max(d.textlength(c[0], font=f), d.textlength(c[1], font=f))))
    tam = 70
    while True:
        f = fonte(tam); ls = melhor(f)
        if max(d.textlength(l, font=f) for l in ls) <= MAXW or tam <= 44: break
        tam -= 2
    if tam < 56: print(f"AVISO: frase longa demais para a legenda ({tam}px), encurte: {texto}")
    lh = int(tam * 1.16); y = HH - 58 - lh * len(ls)
    sombra = Image.new("RGBA", (W, HH), (0, 0, 0, 0)); ds = ImageDraw.Draw(sombra)
    for i, l in enumerate(ls):
        ds.text((W // 2 + 3, y + i * lh + 5), l, font=f, fill=(0, 0, 0, 210), anchor="ma", stroke_width=6, stroke_fill=(0, 0, 0, 210))
    im = Image.alpha_composite(im.convert("RGBA"), sombra.filter(ImageFilter.GaussianBlur(7))).convert("RGB")
    d = ImageDraw.Draw(im)
    for i, l in enumerate(ls):
        d.text((W // 2, y + i * lh), l, font=f, fill=(255, 255, 255), anchor="ma", stroke_width=2, stroke_fill=(20, 20, 20))
    return im


def main(cfg, out):
    os.makedirs(out, exist_ok=True)
    for i, s in enumerate(cfg["slides"]):
        im = Image.new("RGB", (W, H), (10, 10, 10))
        foco = s.get("foco", [0.35, 0.35])
        im.paste(metade(s["fotos"][0], foco[0], s["textos"][0]), (0, 0))
        im.paste(metade(s["fotos"][1], foco[1], s["textos"][1]), (0, HH))
        ImageDraw.Draw(im).line((0, HH, W, HH), fill=(10, 10, 10), width=6)
        im.save(os.path.join(out, "CAPA.jpg" if i == 0 else f"fatia-{i}.jpg"), quality=92)


if __name__ == "__main__":
    main(json.load(open(sys.argv[1])), sys.argv[2])
