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
    # serifada alta e estreita, como no molde de 23/11 (Instrument Serif, OFL, em assets/fonts)
    return ImageFont.truetype(os.path.join(R, "assets/fonts/InstrumentSerif-Regular.ttf"), t)


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
    # FOTO PREENCHIDA (dono, 23/11/2026: "quero os posts assim com foto preenchida", molde @jondavisdtx):
    # a foto sempre ocupa a metade inteira, sem laterais desfocadas; "foco" escolhe a faixa vertical do recorte.
    esc = max(W / src.width, HH / src.height)
    src = src.resize((int(src.width * esc + 0.5), int(src.height * esc + 0.5)), Image.LANCZOS)
    y0 = int((src.height - HH) * foco); x0 = (src.width - W) // 2
    im = src.crop((x0, y0, x0 + W, y0 + HH)).filter(ImageFilter.UnsharpMask(2, 80, 2))
    im = ImageEnhance.Brightness(ImageEnhance.Color(im).enhance(0.95)).enhance(0.9)
    # vinheta escura embaixo para a legenda
    g = Image.new("L", (1, HH)); [g.putpixel((0, y), int(130 * max(0, (y - HH * 0.5) / (HH * 0.5)) ** 1.6)) for y in range(HH)]
    im = Image.composite(Image.new("RGB", (W, HH), (0, 0, 0)), im, g.resize((W, HH)))
    d = ImageDraw.Draw(im)
    # legenda centrada, em 1 ou 2 linhas equilibradas, larga como no molde, com sombra (não só contorno)
    pal = texto.split()
    def melhor(f):
        if d.textlength(texto, font=f) <= MAXW: return [texto]
        cands = [(" ".join(pal[:k]), " ".join(pal[k:])) for k in range(1, len(pal))]
        return list(min(cands, key=lambda c: max(d.textlength(c[0], font=f), d.textlength(c[1], font=f))))
    tam = 92
    while True:
        f = fonte(tam); ls = melhor(f)
        if max(d.textlength(l, font=f) for l in ls) <= MAXW or tam <= 60: break
        tam -= 2
    if tam < 70: print(f"AVISO: frase longa demais para a legenda ({tam}px), encurte: {texto}")
    lh = int(tam * 1.02); y = HH - 58 - lh * len(ls)
    sombra = Image.new("RGBA", (W, HH), (0, 0, 0, 0)); ds = ImageDraw.Draw(sombra)
    for i, l in enumerate(ls):
        ds.text((W // 2 + 3, y + i * lh + 5), l, font=f, fill=(0, 0, 0, 160), anchor="ma", stroke_width=4, stroke_fill=(0, 0, 0, 160))
    im = Image.alpha_composite(im.convert("RGBA"), sombra.filter(ImageFilter.GaussianBlur(7))).convert("RGB")
    d = ImageDraw.Draw(im)
    for i, l in enumerate(ls):
        d.text((W // 2, y + i * lh), l, font=f, fill=(255, 255, 255), anchor="ma")
    return im


def main(cfg, out):
    os.makedirs(out, exist_ok=True)
    for i, s in enumerate(cfg["slides"]):
        im = Image.new("RGB", (W, H), (10, 10, 10))
        foco = s.get("foco", [0.35, 0.35])
        im.paste(metade(s["fotos"][0], foco[0], s["textos"][0]), (0, 0))
        im.paste(metade(s["fotos"][1], foco[1], s["textos"][1]), (0, HH))
        
        im.save(os.path.join(out, "CAPA.jpg" if i == 0 else f"fatia-{i}.jpg"), quality=92)


if __name__ == "__main__":
    main(json.load(open(sys.argv[1])), sys.argv[2])
