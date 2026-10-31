"""
Formatos de carrossel do funil (referência de estrutura: @alfredosoares; pedido do dono em 25/10/2026).
Versão premium/minimalista (pedido do dono em 25/10/2026): papel claro quente, preto suave, um único destaque
laranja da marca, margens largas, cabeçalho discreto (ícone + LIURI ALVES + 01/09) e barra de progresso fina.
Só a estrutura visual é a referência: texto, desenho e marca são do Liuri.

  "tweet"     post estilo X sobre papel claro (avatar, nome, @, texto grande).            -> POLÊMICA
  "quadro"    folha com esquema desenhado à mão em traço fino laranja + título limpo.    -> EDUCATIVO
  "branco"    etiqueta pequena, frase grande e texto de apoio, grade editorial.          -> INTENCIONAL
  "fotofrase" foto P&B escurecida, frase branca alinhada à esquerda, filete laranja.      -> INOVADOR
  "capa"      capa de oferta: foto P&B do Liuri, etiqueta, título grande, subtítulo.      -> VENDA (capa)
  "escuro"    igual ao "branco" em fundo quase preto.                                      -> VENDA (fatias)

Uso:  python3 scripts/render_formatos.py cfg.json posts/AAAA-MM-DD/liurialves-N
cfg.json: {"formato": "...", "slides": [ {...}, ... ]}  (1º slide = CAPA.jpg, depois fatia-1.jpg ...)
Pode misturar formatos: cada slide aceita "formato" próprio (ex.: capa "capa" + fatias "escuro").
Marcação: **negrito** e [[destaque laranja]].

Campos:
  tweet:     {"texto": "..."}                      (cfg pode ter "nome", "arroba", "avatar")
  quadro:    {"titulo": "...", "desenho": {"tipo": "numero"|"funil"|"circulos"|"pular"|"lista", ...},
              "texto": "...", "soco": "..."}
  branco / escuro: {"etiqueta": "AJUSTE 1", "frase": "...", "texto": "..."}
  fotofrase: {"foto": "/caminho.jpg", "texto": "...", "foco_y": 0.35}
  capa:      {"foto": "/caminho.jpg", "etiqueta": "OFERTA", "titulo": "...", "sub": "...", "foco_y": 0.3}
"""
import json, math, os, random, re, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter, ImageEnhance

W, H = 1080, 1350
M = 110
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FD = os.path.join(RAIZ, "assets", "fonts")
INTER = os.path.join(FD, "Inter.ttf")
CAVEAT = os.path.join(FD, "Caveat.ttf")
ICONE = os.path.join(RAIZ, "assets", "logos", "liuri-alves-icone-laranja.png")
AVATAR = os.path.join(RAIZ, "assets", "avatar-liuri.jpg")

PAPEL = (244, 241, 235)
TINTA = (18, 18, 18)
CINZA = (112, 107, 100)
LINHA = (216, 211, 202)
ACC = (217, 84, 30)
ESCURO = (14, 14, 14)
CLARO = (242, 239, 234)
CINZA_E = (168, 164, 158)
LINHA_E = (52, 52, 52)


def inter(t, peso="Regular"):
    f = ImageFont.truetype(INTER, t)
    try:
        f.set_variation_by_name(peso)
    except Exception:
        pass
    return f


def caveat(t, peso="Bold"):
    f = ImageFont.truetype(CAVEAT, t)
    try:
        f.set_variation_by_name(peso)
    except Exception:
        pass
    return f


# ---------- texto com marcação ----------
def tokens(txt):
    out = []
    for parte in re.split(r"(\*\*.+?\*\*|\[\[.+?\]\])", txt):
        if not parte:
            continue
        est = "n"
        if parte.startswith("**"):
            est, parte = "b", parte[2:-2]
        elif parte.startswith("[["):
            est, parte = "h", parte[2:-2]
        for i, w in enumerate(parte.split()):
            cola = i == 0 and not parte[0].isspace() and out and re.match(r"^[.,;:!?)\]]", w)
            out.append((w, est, bool(cola)))
    return out


def layout(d, txt, fontes, maxw):
    linhas = []
    esp = d.textlength(" ", font=fontes["n"])
    for par in txt.split("\n"):
        cur, larg = [], 0
        for w, e, cola in tokens(par):
            lw = d.textlength(w, font=fontes[e])
            if cola and cur:
                cur.append((w, e, lw, True)); larg += lw; continue
            if cur and larg + esp + lw > maxw:
                linhas.append(cur); cur, larg = [], 0
            cur.append((w, e, lw, False)); larg += (esp if len(cur) > 1 else 0) + lw
        linhas.append(cur)
    return linhas, esp


def desenha(d, txt, fontes, cores, x, y, maxw, alt, centro=False):
    linhas, esp = layout(d, txt, fontes, maxw)
    for ln in linhas:
        tot = sum(t[2] for t in ln) + esp * len([1 for t in ln[1:] if not t[3]])
        cx = x + (maxw - tot) / 2 if centro else x
        for j, (w, e, lw, cola) in enumerate(ln):
            if j and not cola:
                cx += esp
            d.text((cx, y), w, font=fontes[e], fill=cores[e]); cx += lw
        y += alt
    return y


def altura(d, txt, fontes, maxw, alt):
    return len(layout(d, txt, fontes, maxw)[0]) * alt


def ajusta(d, txt, mk, maxw, maxh, tamanhos, fator):
    for t in tamanhos:
        f = mk(t)
        if altura(d, txt, f, maxw, int(t * fator)) <= maxh:
            return f, int(t * fator)
    return mk(tamanhos[-1]), int(tamanhos[-1] * fator)


def espacado(d, xy, txt, f, cor, track=3.0):
    x, y = xy
    for ch in txt:
        d.text((x, y), ch, font=f, fill=cor)
        x += d.textlength(ch, font=f) + track
    return x


def larg_espacado(d, txt, f, track=3.0):
    return sum(d.textlength(c, font=f) + track for c in txt) - track


# ---------- moldura comum ----------
def moldura(im, i, n, escuro=False, com_nome=True):
    d = ImageDraw.Draw(im)
    cor_t = CLARO if escuro else TINTA
    cor_c = CINZA_E if escuro else CINZA
    y = 84
    x = M
    if os.path.exists(ICONE):
        ic = Image.open(ICONE).convert("RGBA"); ic = ic.resize((int(ic.width * 34 / ic.height), 34))
        im.paste(ic, (x, y - 4), ic); x += ic.width + 16
    if com_nome:
        espacado(d, (x, y), "LIURI ALVES", inter(21, "SemiBold"), cor_t, 3.2)
    idx = f"{i + 1:02d} / {n:02d}"
    f = inter(21, "Medium")
    espacado(d, (W - M - larg_espacado(d, idx, f, 2), y), idx, f, cor_c, 2)
    yb = H - 86
    d.line((M, yb, W - M, yb), fill=LINHA_E if escuro else LINHA, width=3)
    d.line((M, yb, M + (W - 2 * M) * (i + 1) / n, yb), fill=ACC, width=3)


def etiqueta(d, x, y, txt, cor=ACC):
    d.line((x, y + 13, x + 44, y + 13), fill=cor, width=3)
    espacado(d, (x + 62, y), txt.upper(), inter(23, "SemiBold"), cor, 3.4)
    return y + 74


# ---------- traço à mão (fino) ----------
def traco(d, pts, cor=ACC, w=5, tremor=1.4, seed=0):
    rnd = random.Random(seed)
    p2 = [(x + rnd.uniform(-tremor, tremor), y + rnd.uniform(-tremor, tremor)) for x, y in pts]
    d.line(p2, fill=cor, width=w, joint="curve")
    for x, y in (p2[0], p2[-1]):
        d.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill=cor)


def circulo(d, cx, cy, r, cor=ACC, w=5, seed=1, voltas=1.1):
    rnd = random.Random(seed); pts = []; a0 = rnd.uniform(0, 6.28); n = 100
    for k in range(int(n * voltas)):
        a = a0 + 2 * math.pi * k / n
        rr = r * (1 + 0.035 * math.sin(a * 3 + seed))
        pts.append((cx + rr * math.cos(a), cy + rr * 0.94 * math.sin(a)))
    traco(d, pts, cor, w, 0.4, seed)


def seta(d, x1, y1, x2, y2, cor=ACC, w=5, seed=2, curva=0.16):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    nx, ny = -(y2 - y1) * curva, (x2 - x1) * curva
    pts = [((1 - t) ** 2 * x1 + 2 * (1 - t) * t * (mx + nx) + t * t * x2,
            (1 - t) ** 2 * y1 + 2 * (1 - t) * t * (my + ny) + t * t * y2) for t in [k / 30 for k in range(31)]]
    traco(d, pts, cor, w, 0.5, seed)
    ang = math.atan2(y2 - pts[-4][1], x2 - pts[-4][0])
    for da in (2.6, -2.6):
        traco(d, [(x2, y2), (x2 + 30 * math.cos(ang + da), y2 + 30 * math.sin(ang + da))], cor, w, 0.3, seed + 7)


def esquema(d, des, box):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    tipo = des.get("tipo")
    if tipo == "numero":
        r = 104; ccx = x0 + r + 10
        circulo(d, ccx, cy, r, seed=3)
        n = str(des["n"]); fn = inter(120, "Light")
        bb = d.textbbox((0, 0), n, font=fn)
        d.text((ccx - (bb[2] + bb[0]) / 2, cy - (bb[3] + bb[1]) / 2), n, font=fn, fill=TINTA)
        rx = ccx + r + 60
        if des.get("rotulo"):
            espacado(d, (rx, cy - 62), des["rotulo"].upper(), inter(30, "SemiBold"), TINTA, 4)
            d.line((rx, cy - 10, rx + 60, cy - 10), fill=LINHA, width=2)
        else:
            seta(d, rx - 40, cy - 40, rx - 5, cy + 30, seed=5, curva=-0.25)
        nota = des.get("nota", "")
        for t in (56, 50, 44):
            fl = caveat(t)
            if d.textlength(nota, font=fl) <= x1 - rx: break
        d.text((rx, cy + 10), nota, font=fl, fill=ACC)
    elif tipo == "funil":
        camadas = des["camadas"]; topo, base = 760, 220
        n = len(camadas); hh = (y1 - y0) / n
        for k, rot in enumerate(camadas):
            ya, yb = y0 + k * hh, y0 + (k + 1) * hh
            la = topo - (topo - base) * k / n; lb = topo - (topo - base) * (k + 1) / n
            traco(d, [(cx - la / 2, ya), (cx + la / 2, ya)], seed=10 + k)
            traco(d, [(cx - la / 2, ya), (cx - lb / 2, yb)], seed=20 + k)
            traco(d, [(cx + la / 2, ya), (cx + lb / 2, yb)], seed=30 + k)
            if k == n - 1:
                traco(d, [(cx - lb / 2, yb), (cx + lb / 2, yb)], seed=40)
            f = inter(30, "Medium")
            num = f"{k + 1}"
            d.text((cx - d.textlength(rot, font=f) / 2, ya + hh / 2 - 19), rot, font=f, fill=TINTA)
            d.text((cx - la / 2 - 44, ya + hh / 2 - 19), num, font=inter(26, "Medium"), fill=CINZA)
        if des.get("lado"):
            fl = caveat(50)
            d.text((cx + base / 2 + 40, y1 - 60), des["lado"], font=fl, fill=ACC)
            seta(d, cx + base / 2 + 30, y1 - 30, cx + base / 2 - 10, y1 + 10, seed=41, curva=0.3)
    elif tipo == "circulos":
        rots = des["rotulos"]
        pos = [(cx - 135, cy - 70), (cx + 135, cy - 70), (cx, cy + 140)][:len(rots)]
        for k, ((px, py), rot) in enumerate(zip(pos, rots)):
            circulo(d, px, py, 160, seed=50 + k, voltas=1.04)
            f = caveat(54)
            off = {0: (-55, -30), 1: (55, -30), 2: (0, 55)}[k]
            d.text((px + off[0] - d.textlength(rot, font=f) / 2, py + off[1] - 30), rot, font=f, fill=ACC)
        if des.get("centro"):
            f = inter(26, "SemiBold"); t = des["centro"]
            espacado(d, (cx - larg_espacado(d, t, f, 4) / 2, cy + 10), t, f, TINTA, 4)
    elif tipo == "pular":
        pontos = des.get("pontos", ["1", "2", "3", "4", "5"])
        n = len(pontos); esp = (x1 - x0 - 120) / (n - 1)
        ys = cy + 60; fn = inter(48, "Light")
        for k, p in enumerate(pontos):
            px = x0 + 60 + k * esp
            circulo(d, px, ys, 50, seed=60 + k, w=4, cor=TINTA if k in (0, n - 1) else LINHA)
            bb = d.textbbox((0, 0), p, font=fn)
            d.text((px - (bb[2] + bb[0]) / 2, ys - (bb[3] + bb[1]) / 2), p, font=fn, fill=TINTA if k in (0, n - 1) else CINZA)
        seta(d, x0 + 60, ys - 70, x0 + 60 + (n - 1) * esp, ys - 70, seed=70, curva=0.33)
        mx = x0 + 60 + (n - 1) * esp / 2
        traco(d, [(mx - 34, ys - 290), (mx + 34, ys - 222)], w=6, seed=71)
        traco(d, [(mx + 34, ys - 290), (mx - 34, ys - 222)], w=6, seed=72)
        if des.get("nota"):
            f = caveat(54)
            d.text((mx - d.textlength(des["nota"], font=f) / 2, ys + 70), des["nota"], font=f, fill=ACC)
    elif tipo == "lista":
        itens = des["itens"]; passo = (y1 - y0) / len(itens); yy = y0 + 10
        for k, it in enumerate(itens):
            dia, _, oque = it.partition(":")
            espacado(d, (x0, yy + 12), dia.strip().upper(), inter(24, "SemiBold"), CINZA, 3)
            d.text((x0 + 130, yy), oque.strip(), font=inter(40, "Medium"), fill=TINTA)
            if des.get("check"):
                traco(d, [(x1 - 60, yy + 26), (x1 - 44, yy + 44), (x1 - 14, yy + 6)], w=5, seed=90 + k)
            if k < len(itens) - 1:
                d.line((x0, yy + passo - 22, x1, yy + passo - 22), fill=LINHA, width=2)
            yy += passo


# ---------- formatos ----------
def f_tweet(s, cfg, i, n):
    im = Image.new("RGB", (W, H), PAPEL); d = ImageDraw.Draw(im)
    av = cfg.get("avatar", AVATAR)
    ft = {"n": inter(54, "Medium"), "b": inter(54, "Bold"), "h": inter(54, "Bold")}
    maxw = W - 2 * M
    ft, alt = ajusta(d, s["texto"], lambda t: {"n": inter(t, "Medium"), "b": inter(t, "Bold"), "h": inter(t, "Bold")},
                     maxw, 640, (60, 56, 52, 48, 44), 1.36)
    ht = altura(d, s["texto"], ft, maxw, alt)
    tot = 96 + 52 + ht
    y = (H - tot) / 2 - 10
    if os.path.exists(av):
        a = ImageOps.fit(Image.open(av).convert("RGB"), (96, 96))
        mk = Image.new("L", (96 * 4, 96 * 4), 0); ImageDraw.Draw(mk).ellipse((0, 0, 96 * 4, 96 * 4), fill=255)
        im.paste(a, (M, int(y)), mk.resize((96, 96), Image.LANCZOS))
    d.text((M + 120, y + 12), cfg.get("nome", "Liuri Alves"), font=inter(32, "Bold"), fill=TINTA)
    d.text((M + 120, y + 52), cfg.get("arroba", "@liurialves"), font=inter(28), fill=CINZA)
    desenha(d, s["texto"], ft, {"n": TINTA, "b": TINTA, "h": ACC}, M, y + 96 + 52, maxw, alt)
    moldura(im, i, n, com_nome=False)
    return im


def f_quadro(s, cfg, i, n):
    im = Image.new("RGB", (W, H), PAPEL); d = ImageDraw.Draw(im)
    maxw = W - 2 * M; y = 190
    if s.get("etiqueta"):
        y = etiqueta(d, M, y, s["etiqueta"])
    tit = s.get("titulo", "")
    if tit:
        capa = i == 0
        mk = lambda t: {"n": inter(t, "Bold"), "b": inter(t, "Black"), "h": inter(t, "Bold")}
        f, alt = ajusta(d, tit, mk, maxw, 330 if capa else 170, (78, 72, 66, 60) if capa else (58, 54, 50, 46), 1.14)
        y = desenha(d, tit, f, {"n": TINTA, "b": TINTA, "h": ACC}, M, y, maxw, alt)
    corpo = s.get("texto", ""); soco = s.get("soco", "")
    fb = {"n": inter(34), "b": inter(34, "SemiBold"), "h": inter(34, "SemiBold")}
    hb = altura(d, corpo, fb, maxw, 50) if corpo else 0
    fs = {"n": inter(36, "SemiBold"), "b": inter(36, "Bold"), "h": inter(36, "SemiBold")}
    hs = altura(d, soco, fs, maxw - 30, 50) if soco else 0
    yt = H - 150 - hb - hs - (36 if soco and corpo else 0)
    if s.get("desenho"):
        esquema(d, s["desenho"], (M, y + 60, W - M, yt - 70))
    if corpo:
        desenha(d, corpo, fb, {"n": CINZA, "b": TINTA, "h": ACC}, M, yt, maxw, 50)
    if soco:
        ys = yt + hb + (36 if corpo else 0)
        d.line((M, ys + 6, M, ys + hs - 10), fill=ACC, width=4)
        desenha(d, soco, fs, {"n": TINTA, "b": TINTA, "h": ACC}, M + 30, ys, maxw - 30, 50)
    moldura(im, i, n)
    return im


def bloco_frase(im, s, i, n, escuro):
    d = ImageDraw.Draw(im)
    cor_t = CLARO if escuro else TINTA; cor_c = CINZA_E if escuro else CINZA
    maxw = W - 2 * M
    capa = i == 0
    mk = lambda t: {"n": inter(t, "Bold"), "b": inter(t, "Black"), "h": inter(t, "Bold")}
    f, alt = ajusta(d, s["frase"], mk, maxw, 520, (84, 78, 72, 66, 60, 56) if capa else (72, 66, 62, 58, 54), 1.12)
    hf = altura(d, s["frase"], f, maxw, alt)
    tx = s.get("texto", "")
    fb = {"n": inter(35), "b": inter(35, "SemiBold"), "h": inter(35, "SemiBold")}
    hb = altura(d, tx, fb, maxw - 40, 52) if tx else 0
    tot = (74 if s.get("etiqueta") else 0) + hf + (64 + hb if tx else 0)
    y = max(250, (H - tot) / 2 - 30)
    if s.get("etiqueta"):
        y = etiqueta(d, M, y, s["etiqueta"])
    y = desenha(d, s["frase"], f, {"n": cor_t, "b": cor_t, "h": ACC}, M, y, maxw, alt)
    if tx:
        desenha(d, tx, fb, {"n": cor_c, "b": cor_t, "h": ACC}, M, y + 64, maxw - 40, 52)
    moldura(im, i, n, escuro)
    return im


def f_branco(s, cfg, i, n):
    return bloco_frase(Image.new("RGB", (W, H), PAPEL), s, i, n, False)


def f_escuro(s, cfg, i, n):
    return bloco_frase(Image.new("RGB", (W, H), ESCURO), s, i, n, True)


def cobre(path, foco_y=0.4):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    r = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * r + 1), int(im.height * r + 1)), Image.LANCZOS)
    x = (im.width - W) // 2; y = int((im.height - H) * foco_y)
    im = im.crop((x, y, x + W, y + H))
    im = ImageOps.grayscale(im).convert("RGB")
    return ImageEnhance.Contrast(im).enhance(1.08)


def gradiente(im, ini, forca):
    g = Image.new("L", (1, H))
    for yy in range(H):
        t = max(0.0, (yy / H - ini) / (1 - ini))
        g.putpixel((0, yy), int(forca * min(1.0, t ** 1.1)))
    topo = Image.new("L", (1, H))
    for yy in range(H):
        topo.putpixel((0, yy), int(170 * max(0.0, 1 - yy / 320) ** 1.2))
    from PIL import ImageChops
    m = ImageChops.lighter(g, topo).resize((W, H))
    return Image.composite(Image.new("RGB", (W, H), ESCURO), im, m)


def f_fotofrase(s, cfg, i, n):
    im = cobre(s["foto"], s.get("foco_y", 0.35))
    im = ImageEnhance.Brightness(im).enhance(0.82)
    im = gradiente(im, 0.28, 240)
    d = ImageDraw.Draw(im)
    maxw = W - 2 * M - 20
    capa = i == 0
    mk = lambda t: {"n": inter(t, "Light"), "b": inter(t, "SemiBold"), "h": inter(t, "SemiBold")}
    f, alt = ajusta(d, s["texto"], mk, maxw, 440, (64, 58, 54) if capa else (52, 48, 44), 1.3)
    h = altura(d, s["texto"], f, maxw, alt)
    y = H - 170 - h
    d.line((M, y - 44, M + 56, y - 44), fill=ACC, width=4)
    desenha(d, s["texto"], f, {"n": CLARO, "b": (255, 255, 255), "h": ACC}, M, y, maxw, alt)
    moldura(im, i, n, True)
    return im


def f_capa(s, cfg, i, n):
    # foto na parte de cima (até ~66% da altura) com fusão para o painel escuro onde fica o título
    HF = int(H * 0.66)
    src = ImageOps.exif_transpose(Image.open(s["foto"])).convert("RGB")
    r = max(W / src.width, HF / src.height) * s.get("zoom", 1.0)
    src = src.resize((int(src.width * r + 1), int(src.height * r + 1)), Image.LANCZOS)
    x = (src.width - W) // 2; y = int((src.height - HF) * s.get("foco_y", 0.3))
    foto = ImageEnhance.Contrast(ImageOps.grayscale(src.crop((x, y, x + W, y + HF))).convert("RGB")).enhance(1.1)
    foto = ImageEnhance.Brightness(foto).enhance(0.9)
    im = Image.new("RGB", (W, H), ESCURO)
    mask = Image.new("L", (1, HF))
    for yy in range(HF):
        t = yy / HF
        mask.putpixel((0, yy), int(255 * (1 - max(0.0, (t - 0.38) / 0.62) ** 1.6)))
    im.paste(foto, (0, 0), mask.resize((W, HF)))
    topo = Image.new("L", (1, H))
    for yy in range(H):
        topo.putpixel((0, yy), int(150 * max(0.0, 1 - yy / 300) ** 1.2))
    im = Image.composite(Image.new("RGB", (W, H), ESCURO), im, topo.resize((W, H)))
    d = ImageDraw.Draw(im)
    maxw = W - 2 * M
    mk = lambda t: {"n": inter(t, "Bold"), "b": inter(t, "Black"), "h": inter(t, "Bold")}
    f, alt = ajusta(d, s["titulo"], mk, maxw, 300, (92, 86, 80, 74), 1.08)
    ht = altura(d, s["titulo"], f, maxw, alt)
    fs = {"n": inter(33), "b": inter(33, "SemiBold"), "h": inter(33, "SemiBold")}
    hs = altura(d, s.get("sub", ""), fs, maxw - 60, 48) if s.get("sub") else 0
    y = H - 170 - hs - (40 if hs else 0) - ht - (74 if s.get("etiqueta") else 0)
    if s.get("etiqueta"):
        y = etiqueta(d, M, y, s["etiqueta"])
    y = desenha(d, s["titulo"], f, {"n": (255, 255, 255), "b": (255, 255, 255), "h": ACC}, M, y, maxw, alt)
    if s.get("sub"):
        desenha(d, s["sub"], fs, {"n": CINZA_E, "b": CLARO, "h": ACC}, M, y + 40, maxw - 60, 48)
    moldura(im, i, n, True)
    return im


FORMATOS = {"tweet": f_tweet, "quadro": f_quadro, "branco": f_branco, "escuro": f_escuro,
            "fotofrase": f_fotofrase, "capa": f_capa}


def main(cfg_path, out_dir):
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    os.makedirs(out_dir, exist_ok=True)
    n = len(cfg["slides"])
    for i, s in enumerate(cfg["slides"]):
        fn = FORMATOS[s.get("formato", cfg["formato"])]
        im = fn(s, cfg, i, n)
        assert im.size == (W, H)
        p = os.path.join(out_dir, ("CAPA" if i == 0 else f"fatia-{i}") + ".jpg")
        im.save(p, "JPEG", quality=92, optimize=True)
        print(p)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
