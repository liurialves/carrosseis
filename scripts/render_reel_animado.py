"""
Edita um Reel falado no estilo "fala + animação em fundo preto" (referência: vídeos do Matheus/FitFolio).

A voz original corre o vídeo todo. A imagem alterna entre:
  - "rosto": o vídeo da pessoa a falar, com zoom (punch-in) e legenda grande palavra a palavra;
  - "preto": tela preta com tipografia animada, número gigante, palavra manuscrita, seta a desenhar-se,
    figurinha recortada da pessoa com contorno branco, botões e carimbo.
Cada mudança de bloco leva um "whoosh" e cada elemento que entra leva um "pop" (sons sintetizados, baixos).

Uso:  python3 scripts/render_reel_animado.py edl.json saida.mp4
edl.json:
{
  "video": "/caminho/fala.mp4", "ini": 7.0, "fim": 37.6,       # corte do vídeo original (segundos)
  "acento": "#F5C518",
  "blocos": [
    {"tipo": "rosto", "ini": 7.0, "fim": 10.2, "zoom": [1.0, 1.12],
     "legendas": [{"t0": 7.3, "t1": 8.4, "texto": "O EMPREGO FIXO", "destaque": ["FIXO"]}, ...]},
    {"tipo": "preto", "ini": 13.4, "fim": 17.0, "elementos": [
       {"tipo": "palavras", "t0": 14.1, "texto": "seu salário depende", "y": 520, "tam": 64, "passo": 0.25},
       {"tipo": "grande", "t0": 15.4, "texto": "1", "y": 900, "tam": 520, "cor": "acento"},
       {"tipo": "mao", "t0": 15.7, "texto": "pessoa", "x": 540, "y": 1180, "tam": 120, "rot": -6},
       {"tipo": "seta", "t0": 15.0, "dur": 0.5, "pontos": [[200,600],[300,800],[420,860]]},
       {"tipo": "sticker", "t0": 14.4, "img": "/tmp/sticker.png", "x": 540, "y": 1560, "larg": 520, "rot": 4},
       {"tipo": "botao", "t0": 33.0, "texto": "1  CONCORDO", "x": 540, "y": 800, "fundo": "#FFFFFF", "cor": "#000000"},
       {"tipo": "carimbo", "t0": 21.4, "texto": "ACABOU.", "y": 960, "cor": "#E02116"}
    ]}
  ]
}
Tempos sempre no relógio do vídeo original. Coordenadas na tela 1080x1920.
"""
import json, math, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

W, H, FPS = 1080, 1920, 30
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
F = os.path.join(RAIZ, "assets", "fonts")
GF = "/usr/share/fonts/truetype/google-fonts/"
FONTE = {
    "bold": GF + "Poppins-Bold.ttf" if os.path.exists(GF + "Poppins-Bold.ttf") else "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "anton": os.path.join(F, "Anton-Regular.ttf"),
    "mao": os.path.join(F, "Caveat.ttf"),
    "marker": os.path.join(F, "PermanentMarker-Regular.ttf"),
}
_cache = {}


def fonte(nome, tam):
    k = (nome, int(tam))
    if k not in _cache:
        f = ImageFont.truetype(FONTE[nome], int(tam))
        if nome == "mao":
            try:
                f.set_variation_by_axes([700])
            except Exception:
                pass
        _cache[k] = f
    return _cache[k]


def ease_back(p):
    p = max(0.0, min(1.0, p)); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2


def ease_out(p):
    p = max(0.0, min(1.0, p)); return 1 - (1 - p) ** 3


def cor(c, acento):
    return acento if c in (None, "acento") else c


def texto_img(txt, fnome, tam, fill, contorno=0, cor_contorno=(0, 0, 0)):
    # caixa com métricas fixas da fonte (não do recorte da palavra), para todas as palavras
    # ficarem na mesma linha de base e com a largura real (espaços corretos)
    f = fonte(fnome, tam)
    asc, desc = f.getmetrics(); pad = 10 + contorno
    w = int(f.getlength(txt)) + 2 * pad
    im = Image.new("RGBA", (w, asc + desc + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((pad, pad + asc), txt, font=f, fill=fill, anchor="ls", stroke_width=contorno, stroke_fill=cor_contorno)
    return im


def colar(base, im, cx, cy, escala=1.0, alpha=1.0, rot=0.0):
    if escala <= 0.01 or alpha <= 0.01:
        return
    if escala != 1.0:
        im = im.resize((max(1, int(im.width * escala)), max(1, int(im.height * escala))), Image.LANCZOS)
    if rot:
        im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    if alpha < 1.0:
        a = im.split()[3].point(lambda v: int(v * alpha)); im = im.copy(); im.putalpha(a)
    base.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))


# ---------------- elementos do fundo preto ----------------

def el_palavras(base, e, t, ac):
    ws = e["texto"].split(); passo = e.get("passo", 0.22); tam = e.get("tam", 64)
    f = fonte(e.get("fonte", "bold"), tam); dr = ImageDraw.Draw(base)
    larg = [dr.textlength(w + " ", font=f) for w in ws]
    # quebra em linhas de até 900px
    linhas, cur, cl = [], [], 0
    for w, l in zip(ws, larg):
        if cur and cl + l > e.get("max", 900):
            linhas.append(cur); cur, cl = [], 0
        cur.append((w, l)); cl += l
    linhas.append(cur)
    k = 0
    for li, lin in enumerate(linhas):
        x = e.get("x", 540) - sum(l for _, l in lin) / 2; y = e.get("y", 900) + li * tam * 1.25
        for w, l in lin:
            p = (t - e["t0"] - k * passo) / 0.18
            if p > 0:
                dest = w.strip(".,?!").upper() in [d.upper() for d in e.get("destaque", [])]
                im = texto_img(w, e.get("fonte", "bold"), tam, cor("acento" if dest else e.get("cor", "#FFFFFF"), ac))
                colar(base, im, x + l / 2 - f.getlength(" ") / 2, y + (1 - ease_out(p)) * 30, 1.0, ease_out(p))
            x += l; k += 1


def el_grande(base, e, t, ac):
    p = (t - e["t0"]) / 0.35
    if p <= 0: return
    im = texto_img(e["texto"], e.get("fonte", "anton"), e.get("tam", 400), cor(e.get("cor", "#FFFFFF"), ac))
    colar(base, im, e.get("x", 540), e.get("y", 900), ease_back(p) * (1 + 0.02 * math.sin(t * 3)), min(1, p * 2), e.get("rot", 0))


def el_mao(base, e, t, ac):
    p = (t - e["t0"]) / max(0.15, 0.05 * len(e["texto"]))
    if p <= 0: return
    im = texto_img(e["texto"], e.get("fonte", "mao"), e.get("tam", 110), cor(e.get("cor", "#FFFFFF"), ac))
    # revela da esquerda para a direita, como se estivesse a ser escrito
    r = int(im.width * ease_out(p)); m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rectangle([0, 0, r, im.height], fill=255)
    a = Image.composite(im.split()[3], Image.new("L", im.size, 0), m); im.putalpha(a)
    colar(base, im, e.get("x", 540), e.get("y", 900), 1.0, 1.0, e.get("rot", -4))


def el_seta(base, e, t, ac):
    p = (t - e["t0"]) / e.get("dur", 0.45)
    if p <= 0: return
    pts = [tuple(map(float, q)) for q in e["pontos"]]
    # curva suave (Catmull-Rom) entre os pontos
    curva = []
    P = [pts[0]] + pts + [pts[-1]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for s in np.linspace(0, 1, 18, endpoint=False):
            s2, s3 = s * s, s * s * s
            curva.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * s + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * s2 + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * s3) for j in range(2)))
    curva.append(pts[-1])
    n = max(2, int(len(curva) * ease_out(p)))
    c = cor(e.get("cor", "#FFFFFF"), ac); lw = e.get("esp", 9)
    d = ImageDraw.Draw(base)
    d.line(curva[:n], fill=c, width=lw, joint="curve")
    for q in (curva[0], curva[n - 1]):
        d.ellipse([q[0] - lw / 2, q[1] - lw / 2, q[0] + lw / 2, q[1] + lw / 2], fill=c)
    if p >= 1 and e.get("ponta", True):
        (x1, y1), (x2, y2) = curva[-4], curva[-1]
        a = math.atan2(y2 - y1, x2 - x1); L = 42
        for da in (2.6, -2.6):
            d.line([(x2, y2), (x2 + L * math.cos(a + da), y2 + L * math.sin(a + da))], fill=c, width=lw)


_stk = {}


def el_sticker(base, e, t, ac):
    p = (t - e["t0"]) / 0.4
    if p <= 0: return
    if e["img"] not in _stk:
        _stk[e["img"]] = Image.open(e["img"]).convert("RGBA")
    im = _stk[e["img"]]; esc = e.get("larg", 500) / im.width
    rot = e.get("rot", 0) + 2.5 * math.sin((t - e["t0"]) * 4)
    colar(base, im, e.get("x", 540), e.get("y", 1500), esc * ease_back(p), 1.0, rot)


def el_botao(base, e, t, ac):
    p = (t - e["t0"]) / 0.35
    if p <= 0: return
    tam = e.get("tam", 78); f = fonte("bold", tam)
    tw = f.getlength(e["texto"]); bw, bh = int(tw + 110), int(tam * 1.9)
    im = Image.new("RGBA", (bw + 16, bh + 22), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([8, 14, bw + 8, bh + 14], radius=bh // 2, fill=(0, 0, 0, 160))
    d.rounded_rectangle([8, 6, bw + 8, bh + 6], radius=bh // 2, fill=cor(e.get("fundo", "#FFFFFF"), ac))
    d.text((8 + bw / 2, 6 + bh / 2), e["texto"], font=f, fill=cor(e.get("cor", "#000000"), ac), anchor="mm")
    pulso = 1 + (0.035 * math.sin((t - e["t0"]) * 6) if p > 1 else 0)
    colar(base, im, e.get("x", 540), e.get("y", 900), ease_back(p) * pulso, 1.0, e.get("rot", 0))


def el_carimbo(base, e, t, ac):
    p = (t - e["t0"]) / 0.22
    if p <= 0: return
    tam = e.get("tam", 230); c = cor(e.get("cor", "#E02116"), ac)
    im = texto_img(e["texto"], "anton", tam, c)
    pad = 40; box = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(box).rounded_rectangle([6, 6, box.width - 6, box.height - 6], radius=24, outline=c, width=14)
    box.alpha_composite(im, (pad, pad))
    esc = 1 + 1.6 * (1 - ease_out(p))  # cai de cima, grande para o tamanho final
    tremor = 8 * math.sin(t * 60) * max(0, 1 - (t - e["t0"]) / 0.4)
    colar(base, box, e.get("x", 540) + tremor, e.get("y", 960), esc, min(1, p * 1.5), e.get("rot", -8))


ELS = {"palavras": el_palavras, "grande": el_grande, "mao": el_mao, "seta": el_seta,
       "sticker": el_sticker, "botao": el_botao, "carimbo": el_carimbo}


# ---------------- bloco rosto ----------------

def legenda(base, lg, t, ac):
    ws = lg["texto"].split(); n = len(ws); dur = max(0.01, lg["t1"] - lg["t0"])
    ativo = min(n - 1, int((t - lg["t0"]) / dur * n))
    tam = lg.get("tam", 92); f = fonte("bold", tam); d = ImageDraw.Draw(base)
    gap = f.getlength(" ") + 18
    larg = [d.textlength(w, font=f) + gap for w in ws]
    linhas, cur, cl = [], [], 0
    for i, (w, l) in enumerate(zip(ws, larg)):
        if cur and cl + l > 940:
            linhas.append(cur); cur, cl = [], 0
        cur.append((i, w, l)); cl += l
    linhas.append(cur)
    p = ease_back((t - lg["t0"]) / 0.18)
    y0 = lg.get("y", 1330) - (len(linhas) - 1) * tam * 0.6
    dest = [x.upper() for x in lg.get("destaque", [])]
    for li, lin in enumerate(linhas):
        x = 540 - (sum(l for _, _, l in lin) - gap) / 2; y = y0 + li * tam * 1.18
        for i, w, l in lin:
            if i <= ativo:
                c = cor(lg.get("cor_destaque", "acento"), ac) if w.strip(".,?!").upper() in dest else "#FFFFFF"
                esc = p * (1.06 if i == ativo else 1.0)
                im = texto_img(w, "bold", tam, c, contorno=9)
                colar(base, im, x + (l - gap) / 2, y, esc)
            x += l


class Fonte:
    """Lê os frames do vídeo original já cortado, em 30 fps."""

    def __init__(self, video, ini, fim, tmp):
        self.dir = os.path.join(tmp, "src"); os.makedirs(self.dir, exist_ok=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(ini), "-to", str(fim), "-i", video,
                        "-vf", f"fps={FPS}", "-q:v", "2", os.path.join(self.dir, "%05d.jpg")], check=True)
        self.n = len(os.listdir(self.dir)); self.ini = ini

    def frame(self, t):
        i = min(self.n, max(1, int(round((t - self.ini) * FPS)) + 1))
        return Image.open(os.path.join(self.dir, f"{i:05d}.jpg")).convert("RGB")


def rosto(src, b, t, ac):
    im = src.frame(t)
    # preenche 1080x1920 (cover) e aplica o zoom do bloco
    esc = max(W / im.width, H / im.height)
    z0, z1 = b.get("zoom", [1.0, 1.08]); p = (t - b["ini"]) / max(0.01, b["fim"] - b["ini"])
    z = esc * (z0 + (z1 - z0) * ease_out(p))
    im = im.resize((int(im.width * z), int(im.height * z)), Image.LANCZOS)
    cy = b.get("foco_y", 0.42)
    x0 = (im.width - W) // 2; y0 = int(max(0, min(im.height - H, im.height * cy - H * 0.42)))
    im = im.crop((x0, y0, x0 + W, y0 + H)).filter(ImageFilter.UnsharpMask(2, 80, 2))
    im = ImageEnhance.Contrast(im).enhance(1.06)
    base = im.convert("RGBA")
    for lg in b.get("legendas", []):
        if lg["t0"] <= t < lg["t1"]:
            legenda(base, lg, t, ac)
    for e in b.get("elementos", []):
        if t >= e["t0"]:
            ELS[e["tipo"]](base, e, t, ac)
    return base


def preto(b, t, ac):
    base = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    for e in b.get("elementos", []):
        if t >= e["t0"] and t < e.get("t1", 1e9):
            ELS[e["tipo"]](base, e, t, ac)
    return base


# ---------------- sons ----------------

def sfx(edl, tmp):
    sr = 44100; dur = edl["fim"] - edl["ini"]; out = np.zeros(int(sr * dur) + sr, np.float32)
    rng = np.random.default_rng(7)

    def whoosh(t):
        n = int(sr * 0.35); s = rng.standard_normal(n).astype(np.float32)
        env = np.sin(np.linspace(0, np.pi, n)) ** 2
        k = np.linspace(0.02, 0.3, n)  # filtro passa-baixo variável (varrimento)
        y = np.zeros(n, np.float32); acc = 0.0
        for i in range(n):
            acc += k[i] * (s[i] - acc); y[i] = acc
        return 0.22 * y * env

    def pop(t):
        n = int(sr * 0.09); tt = np.arange(n) / sr
        f = 900 * np.exp(-tt * 25) + 300
        return 0.18 * np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-tt * 40)

    def soma(t, y):
        i = int((t - edl["ini"]) * sr)
        if 0 <= i < len(out) - len(y): out[i:i + len(y)] += y
    for b in edl["blocos"][1:]:
        soma(b["ini"] - 0.12, whoosh(b["ini"]))
    for b in edl["blocos"]:
        for e in b.get("elementos", []):
            if e["tipo"] in ("grande", "sticker", "botao", "carimbo"):
                soma(e["t0"], pop(e["t0"]) * (2.2 if e["tipo"] == "carimbo" else 1))
    p = os.path.join(tmp, "sfx.wav")
    import wave
    with wave.open(p, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(out, -1, 1) * 32767).astype(np.int16).tobytes())
    return p


def main(edl_path, saida):
    edl = json.load(open(edl_path, encoding="utf-8")); ac = edl.get("acento", "#F5C518")
    tmp = tempfile.mkdtemp(); src = Fonte(edl["video"], edl["ini"], edl["fim"], tmp)
    fr = os.path.join(tmp, "out"); os.makedirs(fr)
    n = int((edl["fim"] - edl["ini"]) * FPS)
    for i in range(n):
        t = edl["ini"] + i / FPS
        b = next((b for b in edl["blocos"] if b["ini"] <= t < b["fim"]), edl["blocos"][-1])
        im = rosto(src, b, t, ac) if b["tipo"] == "rosto" else preto(b, t, ac)
        im.convert("RGB").save(os.path.join(fr, f"{i:05d}.jpg"), quality=92)
    s = sfx(edl, tmp)
    os.makedirs(os.path.dirname(os.path.abspath(saida)), exist_ok=True)
    subprocess.run([
        "ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(fr, "%05d.jpg"),
        "-ss", str(edl["ini"]), "-to", str(edl["fim"]), "-i", edl["video"], "-i", s,
        "-filter_complex",
        "[1:a]highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,loudnorm=I=-14:TP=-1.5:LRA=9[v];"
        "[2:a]volume=0.8[s];[v][s]amix=inputs=2:duration=longest:normalize=0,apad[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", str(edl["fim"] - edl["ini"]), saida], check=True)
    print(saida)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
