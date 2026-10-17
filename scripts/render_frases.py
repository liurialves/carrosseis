"""
Carrosséis de frase em dois formatos (referência: @codiesanchez, pedido do dono em 15/10/2026).

  "tweet": fundo branco, avatar redondo + nome + @, texto grande preto alinhado à esquerda
           (parece um post do X). Um pensamento por slide.
  "foto":  foto de corpo inteiro/rosto ocupando o slide e frase branca, grossa, centrada na parte de baixo
           (estilo meme/selfie). Normalmente 2 slides: a frase e a virada.

Uso:  python3 scripts/render_frases.py cfg.json posts/AAAA-MM-DD/liurialves-N
cfg.json:
{
  "formato": "tweet",
  "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": "assets/avatar-liuri.jpg",
  "slides": ["texto do 1º", "texto do 2º", ...]           # \n\n separa parágrafos
}
ou
{
  "formato": "foto",
  "slides": [{"foto": "/caminho.jpg", "texto": "frase", "foco_y": 0.4}, ...]
}
Saída: CAPA.jpg, fatia-1.jpg ... (1080x1350), como o render_carrossel.py.
Nunca coloque selo de verificado: a conta não é verificada.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter, ImageEnhance

W, H = 1080, 1350
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
INTER = os.path.join(RAIZ, "assets", "fonts", "Inter.ttf")
GF = "/usr/share/fonts/truetype/google-fonts/"


def inter(tam, peso="Regular"):
    f = ImageFont.truetype(INTER, tam)
    try:
        f.set_variation_by_name(peso)
    except Exception:
        pass
    return f


def quebra(d, txt, f, maxw):
    linhas = []
    for par in txt.split("\n"):
        cur = ""
        for w in par.split():
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) <= maxw:
                cur = t
            else:
                linhas.append(cur); cur = w
        linhas.append(cur)
    return linhas


def tweet(cfg, txt):
    im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
    mx = 110; maxw = W - 2 * mx
    # o tamanho da letra diminui se o texto for longo
    for tam in (68, 62, 56, 50, 46):
        f = inter(tam); lin = quebra(d, txt, f, maxw)
        lh = int(tam * 1.3); alt_txt = sum(lh if l else int(tam * 0.7) for l in lin)
        if alt_txt < 760:
            break
    av = 150; alt = av + 50 + alt_txt
    y = (H - alt) // 2
    a = Image.open(os.path.join(RAIZ, cfg["avatar"]) if not os.path.isabs(cfg["avatar"]) else cfg["avatar"]).convert("RGB")
    a = ImageOps.fit(a, (av * 2, av * 2), Image.LANCZOS).resize((av, av), Image.LANCZOS)
    m = Image.new("L", (av * 4, av * 4), 0); ImageDraw.Draw(m).ellipse([0, 0, av * 4, av * 4], fill=255)
    im.paste(a, (mx, y), m.resize((av, av), Image.LANCZOS))
    d.text((mx + av + 28, y + av / 2 - 6), cfg.get("nome", "Liuri Alves"), font=inter(42, "Bold"), fill="#0F1419", anchor="ls")
    d.text((mx + av + 28, y + av / 2 + 44), cfg.get("arroba", "@liurialves"), font=inter(36), fill="#8B98A5", anchor="ls")
    y += av + 50
    for l in lin:
        if not l:
            y += int(tam * 0.7); continue
        d.text((mx, y), l, font=f, fill="#0F1419"); y += lh
    return im


def foto(s):
    im = Image.open(s["foto"]).convert("RGB")
    im = ImageOps.exif_transpose(im)
    fy = s.get("foco_y", 0.4)
    im = ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.5, fy))
    im = im.filter(ImageFilter.UnsharpMask(2, 70, 2))
    # sombra suave embaixo para o texto ler bem
    g = Image.new("L", (1, H)); [g.putpixel((0, y), int(150 * max(0, (y - H * 0.55) / (H * 0.45)) ** 1.4)) for y in range(H)]
    sombra = Image.new("RGB", (W, H), (0, 0, 0)); im = Image.composite(sombra, im, g.resize((W, H)))
    d = ImageDraw.Draw(im)
    fonte = GF + "Poppins-Bold.ttf" if os.path.exists(GF + "Poppins-Bold.ttf") else INTER
    for tam in (66, 60, 54, 48):
        f = ImageFont.truetype(fonte, tam); lin = quebra(d, s["texto"], f, W - 160)
        if len(lin) <= 5:
            break
    lh = int(tam * 1.12); y = int(H * s.get("y", 0.80)) - len(lin) * lh // 2
    for l in lin:
        d.text((W / 2, y), l, font=f, fill="white", anchor="ma", stroke_width=3, stroke_fill=(0, 0, 0))
        y += lh
    return im


def main(cfg_path, out_dir):
    cfg = json.load(open(cfg_path, encoding="utf-8")); os.makedirs(out_dir, exist_ok=True)
    nomes = ["CAPA"] + [f"fatia-{i}" for i in range(1, 20)]
    for i, s in enumerate(cfg["slides"]):
        im = tweet(cfg, s) if cfg["formato"] == "tweet" else foto(s)
        p = os.path.join(out_dir, nomes[i] + ".jpg"); im.save(p, "JPEG", quality=92); print(p)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
