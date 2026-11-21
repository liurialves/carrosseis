"""
Carrosséis de IA/ferramentas no layout das referências que o dono mandou (pedido de 02/11/2026).
Só o LAYOUT é o da referência; texto, imagens, nome e @ são do @liurialves. Nunca usar nome, @, foto,
logo ou arte do outro perfil. Os cards de repositório e de terminal são desenhados aqui com dados verificados.

Estilos (campo "estilo" do cfg):
  "hud"    fundo branco, card estilo tweet (avatar, nome, @, texto com **negrito**) + imagem opcional.
           slide: {"texto": "...", "imagem": {"tipo": "repo"|"terminal"|"pdfmd"|"paginas"|"arquivo", ...}}
  "tilli"  capa: {"tipo": "capa", "foto": "/x.jpg", "titulo": "...", "foco_y": 0.5}
           ferramenta: {"tipo": "item", "card": {...imagem...}, "titulo": "...", "sub": "...",
                        "bullets": [...], "link": "..."}
           cta: {"tipo": "cta", "palavra": "REPO", "promessa": "OS 6 LINKS", "itens": [...]}

Uso:  python3 scripts/render_clone.py cfg.json posts/AAAA-MM-DD/liurialves-N
Saída: CAPA.jpg, fatia-1.jpg, ...
"""
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

W, H = 1080, 1350
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FD = os.path.join(RAIZ, "assets", "fonts")
INTER = os.path.join(FD, "Inter.ttf")
ANTON = os.path.join(FD, "Anton-Regular.ttf")
AVATAR = os.path.join(RAIZ, "assets", "avatar-liuri.jpg")
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
LARANJA = (232, 130, 58)
NOME, ARROBA = "Liuri Alves", "@liurialves"


def inter(t, peso="Regular"):
    f = ImageFont.truetype(INTER, t)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f


def anton(t): return ImageFont.truetype(ANTON, t)


def mono(t):
    try: return ImageFont.truetype(MONO, t)
    except Exception: return inter(t)


# ---------- texto rico (**negrito**) ----------
def toks(txt):
    out, ant = [], " "
    for parte in re.split(r"(\*\*.+?\*\*)", txt):
        if not parte: continue
        b = parte.startswith("**")
        bruto = parte
        if b: parte = parte[2:-2]
        for i, w in enumerate(parte.split(" ")):
            if w == "": continue
            cola = i == 0 and not parte.startswith(" ") and out and not ant.endswith(" ")
            out.append((w, b, bool(cola)))
        ant = bruto
    return out


def linhas_ricas(d, txt, fn, fb, maxw):
    res = []
    for par in txt.split("\n"):
        if par.strip() == "":
            res.append(None); continue
        cur, lw = [], 0
        for w, b, cola in toks(par):
            f = fb if b else fn
            ww = d.textlength(w, font=f); sp = 0 if (cola or not cur) else d.textlength(" ", font=fn)
            if cur and lw + sp + ww > maxw:
                res.append(cur); cur, lw, sp = [], 0, 0
            cur.append((w, b, sp)); lw += sp + ww
        res.append(cur)
    return res


def desenha_rico(d, txt, x, y, maxw, tam, cor, lh=1.38):
    fn, fb = inter(tam), inter(tam, "Bold")
    for ln in linhas_ricas(d, txt, fn, fb, maxw):
        if ln is None:
            y += int(tam * 0.75); continue
        cx = x
        for w, b, sp in ln:
            cx += sp; f = fb if b else fn
            d.text((cx, y), w, font=f, fill=cor); cx += d.textlength(w, font=f)
        y += int(tam * lh)
    return y


def altura_rico(d, txt, maxw, tam, lh=1.38):
    fn, fb = inter(tam), inter(tam, "Bold"); h = 0
    for ln in linhas_ricas(d, txt, fn, fb, maxw):
        h += int(tam * 0.75) if ln is None else int(tam * lh)
    return h


def arred(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], r, fill=255)
    out = Image.new("RGBA", im.size); out.paste(im, (0, 0), m); return out


def avatar(t):
    a = ImageOps.fit(Image.open(AVATAR).convert("RGB"), (t, t))
    m = Image.new("L", (t, t), 0); ImageDraw.Draw(m).ellipse([0, 0, t - 1, t - 1], fill=255)
    out = Image.new("RGBA", (t, t)); out.paste(a, (0, 0), m); return out


# ---------- imagens desenhadas (cards) ----------
def card_repo(c, w=900, h=400, escuro=True):
    bg, fg, sub, bd = ((13, 17, 23), (230, 237, 243), (139, 148, 158), (48, 54, 61)) if escuro else ((255, 255, 255), (31, 35, 40), (89, 99, 110), (208, 215, 222))
    im = Image.new("RGB", (w, h), bg); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 22, outline=bd, width=2)
    x = 48; y = 44
    d.ellipse([x, y + 4, x + 34, y + 38], outline=sub, width=3)
    d.text((x + 52, y), c["dono"] + " / ", font=inter(36), fill=(88, 166, 255))
    d.text((x + 52 + d.textlength(c["dono"] + " / ", font=inter(36)), y), c["nome"], font=inter(36, "Bold"), fill=(88, 166, 255))
    if x + 52 + d.textlength(c["dono"] + " / " + c["nome"], font=inter(36, "Bold")) < w - 180:
        d.rounded_rectangle([w - 160, y + 2, w - 48, y + 40], 19, outline=bd, width=2); d.text((w - 140, y + 8), "Public", font=inter(22), fill=sub)
    y += 80
    y = desenha_rico(d, c["desc"], x, y, w - 2 * x, 30, fg, 1.35) + 24
    badges = c.get("badges", [])
    bx = x
    for b in badges:
        tw = d.textlength(b, font=inter(26, "SemiBold"))
        d.rounded_rectangle([bx, h - 92, bx + tw + 36, h - 46], 23, fill=(33, 38, 45) if escuro else (246, 248, 250), outline=bd, width=2)
        d.text((bx + 18, h - 84), b, font=inter(26, "SemiBold"), fill=fg); bx += tw + 52
    return im


def card_terminal(linhas, w=900, h=None):
    h = h or 90 + 50 * len(linhas)
    im = Image.new("RGB", (w, h), (30, 30, 34)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, 52], 0, fill=(44, 44, 50))
    for i, cor in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([24 + i * 34, 16, 44 + i * 34, 36], fill=cor)
    y = 76
    for ln in linhas:
        cor = (120, 220, 140) if ln.startswith("$") else ((150, 150, 160) if ln.startswith("#") else (225, 225, 230))
        d.text((32, y), ln, font=mono(27), fill=cor); y += 50
    return arred(im, 22).convert("RGB")


def card_pdfmd(w=900, h=380):
    im = Image.new("RGB", (w, h), (247, 247, 248)); d = ImageDraw.Draw(im)
    def doc(x, rot, cor, fg):
        d.rounded_rectangle([x, 50, x + 230, 330], 18, fill=cor)
        for i in range(5): d.rounded_rectangle([x + 30, 150 + i * 30, x + 200 - (i % 2) * 50, 162 + i * 30], 6, fill=fg)
        d.text((x + 115, 95), rot, font=inter(52, "Bold"), fill=(255, 255, 255), anchor="mm")
    doc(110, "PDF", (214, 69, 65), (240, 170, 168))
    d.line([400, 190, 500, 190], fill=(40, 40, 40), width=8); d.polygon([(500, 170), (540, 190), (500, 210)], fill=(40, 40, 40))
    doc(560, ".md", (30, 30, 34), (110, 110, 118))
    return arred(im, 22).convert("RGB")


def card_paginas(n=3, w=900, h=380):
    im = Image.new("RGB", (w, h), (247, 247, 248)); d = ImageDraw.Draw(im)
    for i in range(n):
        x = 70 + i * 280
        d.rounded_rectangle([x, 40, x + 220, 200], 14, fill=(255, 255, 255), outline=(200, 200, 205), width=3)
        d.text((x + 110, 120), f"pág. {i+1}", font=inter(34, "SemiBold"), fill=(60, 60, 66), anchor="mm")
        d.text((x + 110, 245), "imagem", font=inter(30, "Bold"), fill=(214, 69, 65), anchor="mm")
        d.text((x + 110, 285), "+", font=inter(30), fill=(60, 60, 66), anchor="mm")
        d.text((x + 110, 325), "texto", font=inter(30, "Bold"), fill=(30, 30, 34), anchor="mm")
    return arred(im, 22).convert("RGB")


def imagem(spec, w):
    t = spec["tipo"]
    if t == "repo": return card_repo(spec, w, spec.get("h", 400), spec.get("escuro", True))
    if t == "terminal": return card_terminal(spec["linhas"], w)
    if t == "pdfmd": return card_pdfmd(w)
    if t == "paginas": return card_paginas(3, w)
    if t == "arquivo":
        im = Image.open(spec["arquivo"]).convert("RGB"); im = ImageOps.contain(im, (w, spec.get("h", 420))); return im
    raise ValueError(t)


# ---------- estilo hud ----------
def slide_hud(s):
    im = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(im)
    x, maxw = 96, W - 192
    img = imagem(s["imagem"], maxw) if s.get("imagem") else None
    tam = s.get("tam", 46)
    ht = altura_rico(d, s["texto"], maxw, tam)
    tot = 110 + 40 + ht + ((40 + img.height) if img else 0)
    y = max(110, (H - tot) // 2 - 20)
    im.paste(avatar(116), (x, y), avatar(116))
    d.text((x + 140, y + 16), NOME, font=inter(44, "Bold"), fill=(15, 20, 25))
    d.text((x + 140, y + 70), ARROBA, font=inter(34), fill=(83, 100, 113))
    y += 166
    y = desenha_rico(d, s["texto"], x, y, maxw, tam, (15, 20, 25))
    if img:
        y += 30; r = arred(img, 24); im.paste(r, (x, y), r)
    return im


# ---------- estilo tilli ----------
def linha_arroba(d, y, x0=60, x1=W - 60, cor=(120, 120, 120)):
    f = inter(30, "SemiBold"); tw = d.textlength("@liurialves", font=f)
    d.line([x0, y, W / 2 - tw / 2 - 20, y], fill=cor, width=2); d.line([W / 2 + tw / 2 + 20, y, x1, y], fill=cor, width=2)
    d.text((W / 2, y), "@liurialves", font=f, fill=(225, 225, 225), anchor="mm")


def quebra(d, txt, f, maxw):
    ls, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > maxw and cur: ls.append(cur); cur = w
        else: cur = t
    ls.append(cur); return ls


def slide_capa(s):
    im = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
    HF = 900
    f = Image.open(s["foto"]).convert("RGB")
    r = max(W / f.width, HF / f.height); f = f.resize((int(f.width * r) + 1, int(f.height * r) + 1))
    y0 = int((f.height - HF) * s.get("foco_y", 0.5)); f = f.crop(((f.width - W) // 2, y0, (f.width - W) // 2 + W, y0 + HF))
    f = ImageEnhance.Brightness(f).enhance(0.85)
    # degradê para o preto
    grad = Image.linear_gradient("L").resize((W, 220)); f.paste((0, 0, 0), (0, HF - 220), grad)
    im.paste(f, (0, 0))
    linha_arroba(d, 935)
    tit = s["titulo"].upper()
    for t in range(104, 50, -2):
        fo = anton(t); ls = quebra(d, tit, fo, W - 110)
        if len(ls) * t * 1.1 <= 270: break
    y = 985
    for l in ls:
        d.text((W / 2, y), l, font=fo, fill=(255, 255, 255), anchor="ma"); y += int(t * 1.1)
    fd = anton(44); a = "DESLIZE E VEJA "; tw = d.textlength(a + ">>>", font=fd)
    d.text((W / 2 - tw / 2, y + 22), a, font=fd, fill=(255, 255, 255))
    d.text((W / 2 - tw / 2 + d.textlength(a, font=fd), y + 22), ">>>", font=fd, fill=LARANJA)
    return im


def slide_item(s):
    im = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
    cw = W - 160; card = imagem(s["card"], cw - 40)
    ch = card.height + 40
    d.rounded_rectangle([80, 90, 80 + cw, 90 + ch], 30, fill=(18, 18, 20), outline=(70, 70, 74), width=3)
    r = arred(card, 20); im.paste(r, (100, 110), r)
    y = 90 + ch + 50
    fo = anton(118)
    while d.textlength(s["titulo"].upper(), font=fo) > W - 160: fo = anton(fo.size - 4)
    d.text((80, y), s["titulo"].upper(), font=fo, fill=LARANJA); y += int(fo.size * 1.42)
    y = desenha_rico(d, s["sub"], 80, y, W - 160, 44, (240, 240, 240), 1.3) + 22
    for b in s["bullets"]:
        d.ellipse([92, y + 20, 103, y + 31], fill=(240, 240, 240))
        y = desenha_rico(d, b, 126, y, W - 210, 40, (240, 240, 240), 1.32) + 8
    fl = inter(38)
    while d.textlength(s["link"], font=fl) > W - 160: fl = inter(fl.size - 2)
    d.text((80, y + 36), s["link"], font=fl, fill=(240, 240, 240))
    linha_arroba(d, H - 50)
    return im


def slide_cta(s):
    im = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
    linha_arroba(d, 150, cor=LARANJA)
    y = 200
    for l in ["SIGA O PERFIL", "E COMENTE"]:
        d.text((W / 2, y), l, font=anton(124), fill=(255, 255, 255), anchor="ma"); y += 165
    d.rectangle([80, y + 20, W - 80, y + 170], fill=LARANJA)
    d.text((W / 2, y + 95), s["palavra"], font=anton(128), fill=(10, 10, 10), anchor="mm"); y += 200
    fa = anton(54); a = "E EU TE MANDO "; d.text((80, y), a, font=fa, fill=(255, 255, 255))
    d.text((80 + d.textlength(a, font=fa), y), s["promessa"], font=fa, fill=LARANJA); y += 90
    d.line([80, y, W - 80, y], fill=LARANJA, width=2); y += 40
    for i, it in enumerate(s["itens"], 1):
        d.text((100, y), f"{i:02d}", font=inter(40, "Bold"), fill=LARANJA)
        d.text((175, y), it, font=inter(38), fill=(240, 240, 240)); y += 68
    d.line([80, y + 10, W - 80, y + 10], fill=LARANJA, width=2)
    fs = anton(48); x = W / 2 - 2 * 95
    for i in range(4):
        d.text((x + i * 120, y + 70), ">>>", font=fs, fill=LARANJA if i == 3 else (150, 150, 150))
    return im


def main(cfg, out):
    os.makedirs(out, exist_ok=True)
    for i, s in enumerate(cfg["slides"]):
        if cfg["estilo"] == "hud": im = slide_hud(s)
        else: im = {"capa": slide_capa, "item": slide_item, "cta": slide_cta}[s["tipo"]](s)
        im.convert("RGB").save(os.path.join(out, "CAPA.jpg" if i == 0 else f"fatia-{i}.jpg"), quality=92)


if __name__ == "__main__":
    main(json.load(open(sys.argv[1])), sys.argv[2])
