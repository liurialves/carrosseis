"""
Formato "faixa" (pedido do dono em 05/11/2026, molde de estrutura de um carrossel de escada de valores):
foto em cima (~60%) com degradê para o preto, faixa amarela inclinada com o rótulo, texto branco em caixa alta,
destaque amarelo opcional e rodapé "@LIURIALVES • 02/08". Último slide pode ser "branco" (fundo claro com marcador
amarelo atrás das frases de destaque). Só a estrutura é a referência; texto, fotos e marca são do Liuri.

cfg: {"slides": [
  {"tipo": "foto", "foto": "/x.jpg", "foco_y": 0.4, "faixa": "COM 1.000 € GUARDADOS,", "texto": "...",
   "destaque": "... (amarelo, opcional)", "grande": true (capa), "arraste": true (capa)},
  {"tipo": "branco", "blocos": [["h", "TEXTO MARCADO"], ["n", "texto normal"], ...]}
]}
Uso: python3 scripts/render_faixa.py cfg.json posts/AAAA-MM-DD/liurialves-N
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

W, H = 1080, 1350
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
INTER = os.path.join(RAIZ, "assets", "fonts", "Inter.ttf")
AMARELO = (245, 197, 24)
PRETO = (8, 8, 8)
ARROBA = "@LIURIALVES"


def inter(t, peso="Bold"):
    f = ImageFont.truetype(INTER, t)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f


def quebra(d, txt, f, maxw):
    ls, l = [], ""
    for w in txt.split():
        t = (l + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: l = t
        else: ls.append(l); l = w
    if l: ls.append(l)
    return ls


def bloco(d, txt, y, tam, peso, cor, maxw, lh=1.12, minimo=34, maxlin=4):
    while True:
        f = inter(tam, peso); ls = quebra(d, txt, f, maxw)
        if len(ls) <= maxlin or tam <= minimo: break
        tam -= 2
    for l in ls:
        d.text((W / 2, y), l, font=f, fill=cor, anchor="ma"); y += int(tam * lh)
    return y


def rodape(d, i, n, cor=AMARELO, cor2=(235, 235, 235)):
    a = f"{ARROBA}  •  "; b = f"{i:02d}/{n:02d}"; f = inter(26, "Medium")
    x = W / 2 - (d.textlength(a + b, font=f)) / 2
    d.text((x, H - 72), a, font=f, fill=cor); d.text((x + d.textlength(a, font=f), H - 72), b, font=f, fill=cor2)


def slide_foto(s, i, n):
    im = Image.new("RGB", (W, H), PRETO)
    HF = s.get("hf", 700 if s.get("grande") else (740 if s.get("destaque") else 860))  # com destaque, a foto encolhe para o texto caber
    src = ImageOps.exif_transpose(Image.open(s["foto"])).convert("RGB")
    r = max(W / src.width, HF / src.height); src = src.resize((int(src.width * r) + 1, int(src.height * r) + 1), Image.LANCZOS)
    x = (src.width - W) // 2; y0 = int((src.height - HF) * s.get("foco_y", 0.4))
    foto = ImageEnhance.Brightness(src.crop((x, y0, x + W, y0 + HF))).enhance(0.92)
    mask = Image.new("L", (1, HF))
    for yy in range(HF):
        t = yy / HF; mask.putpixel((0, yy), int(255 * (1 - max(0.0, (t - 0.62) / 0.38) ** 1.3)))
    im.paste(foto, (0, 0), mask.resize((W, HF)))
    d = ImageDraw.Draw(im)
    y = HF - 60 if not s.get("grande") else HF - 20
    if s.get("grande"):
        d.line([120, y, 440, y], fill=AMARELO, width=3); d.line([640, y, 960, y], fill=AMARELO, width=3)
        d.text((W / 2, y), "LIURI ALVES", font=inter(26, "SemiBold"), fill=AMARELO, anchor="mm"); y += 50
    # faixa inclinada
    ff = inter(58 if s.get("grande") else 46, "Bold")
    while d.textlength(s["faixa"], font=ff) > W - 220: ff = inter(ff.size - 2, "Bold")
    hb = int(ff.size * 1.6)
    d.polygon([(70, y + hb), (95, y), (W - 60, y), (W - 85, y + hb)], fill=AMARELO)
    d.text((W / 2, y + hb / 2), s["faixa"], font=ff, fill=PRETO, anchor="mm")
    y += hb + 34
    if s.get("grande"):
        y = bloco(d, s["texto"], y, 96, "Black", (255, 255, 255), W - 140, 1.04, 60, 3)
    else:
        y = bloco(d, s["texto"], y, 54, "Bold", (255, 255, 255), W - 120, 1.14, 36, 4)
    if s.get("destaque"):
        y = bloco(d, s["destaque"], y + 26, 58, "Bold", AMARELO, W - 140, 1.12, 38, 3)
    if s.get("arraste"):
        f = inter(34, "Bold"); d.text((W / 2, H - 90), "ARRASTE →", font=f, fill=AMARELO, anchor="ma")
    else:
        rodape(d, i, n)
    return im


def slide_branco(s, i, n):
    im = Image.new("RGB", (W, H), (246, 245, 242)); d = ImageDraw.Draw(im)
    x0, maxw = 130, W - 260
    y = 120
    for est, txt in s["blocos"]:
        if est == "esp": y += int(txt); continue
        tam, peso = {"t": (56, "Bold"), "h": (54, "Bold"), "n": (40, "Medium")}[est]
        f = inter(tam, peso)
        for l in quebra(d, txt, f, maxw):
            if est == "h":
                tw = d.textlength(l, font=f)
                d.polygon([(x0 - 14, y + 6), (x0 + tw + 18, y + 2), (x0 + tw + 10, y + tam * 1.16), (x0 - 18, y + tam * 1.18)], fill=AMARELO)
            d.text((x0, y), l, font=f, fill=(15, 15, 15)); y += int(tam * 1.2)
        y += 26 if est != "h" else 8
    a = f"{ARROBA}  •  {i:02d}/{n:02d}"; d.text((W / 2, H - 72), a, font=inter(26, "Medium"), fill=(60, 60, 60), anchor="ma")
    return im


def main(cfg, out):
    os.makedirs(out, exist_ok=True); n = len(cfg["slides"])
    for k, s in enumerate(cfg["slides"]):
        im = (slide_branco if s["tipo"] == "branco" else slide_foto)(s, k + 1, n)
        im.save(os.path.join(out, "CAPA.jpg" if k == 0 else f"fatia-{k}.jpg"), quality=92)


if __name__ == "__main__":
    main(json.load(open(sys.argv[1])), sys.argv[2])
