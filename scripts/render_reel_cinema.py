"""
Reel estilo "cinema escuro" (modelo do Reel de 167 mil views do @liurialves).

Visual: clipes de vídeo (ou fotos com zoom lento) em preto e branco escuro, troca a cada ~2,5 s
com fade curto, frase curta serifada branca no centro trocando a cada ~1,2 s, ícone do Instagram
+ @LIURIALVES no canto superior direito e tela final preta com o ícone e o @ por alguns segundos.
Sai SEM música (o dono põe a música no Instagram/CapCut).

Uso: python3 scripts/render_reel_cinema.py reel.json saida.mp4
reel.json:
{
  "clipes": [ {"src": "/tmp/v1.mp4", "inicio": 2.0, "dur": 2.5},     # vídeo: trecho a usar
              {"src": "/tmp/foto.jpg", "dur": 2.5, "foco_y": 0.4} ],  # foto: zoom lento
  "frases": [ {"t": 0.4, "texto": "Eu sumi"}, {"t": 1.6, "texto": "do grupo"}, ... ],
  "fim_texto": 17.0,          # quando o último texto some (opcional)
  "final_seg": 4.0            # duração da tela preta final (opcional)
}
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps, ImageEnhance

W, H, FPS = 1080, 1920, 30
FADE = 10  # frames
FONT = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
FONT_H = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
if not os.path.exists(FONT_H):
    FONT_H = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def grade(arr):
    """preto e branco escuro, contraste suave, levemente lavado (look do modelo)."""
    a = arr.astype(np.float32) / 255.0
    a = np.clip((a - 0.5) * 1.05 + 0.5, 0, 1)
    a = a * 0.66 + 0.04          # escurece e levanta os pretos
    return (a * 255).astype(np.uint8)


def frames_video(src, inicio, dur):
    n = int(round(dur * FPS))
    vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=gray"
    cmd = ["ffmpeg", "-loglevel", "error", "-ss", str(inicio), "-i", src, "-t", str(dur + 0.2),
           "-vf", vf, "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W)
    if len(fr) == 0:
        raise SystemExit(f"sem frames em {src}")
    while len(fr) < n:
        fr = np.concatenate([fr, fr[-1:]])
    return [grade(f) for f in fr[:n]]


def frames_foto(src, dur, foco_y=0.45):
    n = int(round(dur * FPS))
    im = ImageOps.exif_transpose(Image.open(src)).convert("L")
    s = max(W * 1.15 / im.width, H * 1.15 / im.height)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    out = []
    for i in range(n):
        z = 1.0 + 0.08 * i / max(n - 1, 1)
        cw, ch = int(W * 1.12 / z), int(H * 1.12 / z)
        cx = im.width / 2; cy = im.height * foco_y
        x0 = int(min(max(cx - cw / 2, 0), im.width - cw)); y0 = int(min(max(cy - ch / 2, 0), im.height - ch))
        f = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR)
        out.append(grade(np.asarray(f)))
    return out


def icone_ig(size):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    w = max(3, size // 12)
    d.rounded_rectangle((w, w, size - w, size - w), radius=size // 4, outline="white", width=w)
    r = size // 4; c = size // 2
    d.ellipse((c - r, c - r, c + r, c + r), outline="white", width=w)
    d.ellipse((size * 0.7, size * 0.2, size * 0.7 + w * 1.6, size * 0.2 + w * 1.6), fill="white")
    return im


def marca(alpha=235):
    """ícone + @LIURIALVES no canto superior direito."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    ic = icone_ig(56); im.alpha_composite(ic, (W - 128, 470))
    f = ImageFont.truetype(FONT_H, 26); t = "@LIURIALVES"
    d.text((W - 72 - d.textlength(t, font=f), 540), t, font=f, fill=(255, 255, 255, alpha))
    return im


def texto(t):
    f = ImageFont.truetype(FONT, 50)
    try:
        f.set_variation_by_name("Bold")
    except Exception:
        pass
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x = (W - d.textlength(t, font=f)) / 2; y = 960
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x, y), t, font=f, fill=(0, 0, 0, 200))
    im = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)), im)
    ImageDraw.Draw(im).text((x, y), t, font=f, fill="white")
    return im


def final(n):
    out = []
    ic = icone_ig(150); f = ImageFont.truetype(FONT_H, 38); t = "@LIURIALVES"
    for i in range(n):
        a = min(1.0, i / 12)
        im = Image.new("RGBA", (W, H), (0, 0, 0, 255)); d = ImageDraw.Draw(im)
        ic2 = ic.copy(); ic2.putalpha(ic2.getchannel("A").point(lambda v: int(v * a)))
        im.alpha_composite(ic2, ((W - 150) // 2, 780))
        d.text(((W - d.textlength(t, font=f)) / 2, 960), t, font=f, fill=(255, 255, 255, int(255 * a)))
        out.append(im.convert("RGB"))
    return out


def main(cfg_path, out):
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    seq = []
    for c in cfg["clipes"]:
        ext = os.path.splitext(c["src"])[1].lower()
        fr = (frames_foto(c["src"], c["dur"], c.get("foco_y", 0.45)) if ext in (".jpg", ".jpeg", ".png", ".webp")
              else frames_video(c["src"], c.get("inicio", 0), c["dur"]))
        if seq:  # fade cruzado
            for k in range(min(FADE, len(fr))):
                a = (k + 1) / (FADE + 1)
                seq[-FADE + k] = (seq[-FADE + k] * (1 - a) + fr[k] * a).astype(np.uint8)
            fr = fr[FADE:]
        seq.extend(fr)
    frases = sorted(cfg["frases"], key=lambda x: x["t"])
    fim_txt = cfg.get("fim_texto", len(seq) / FPS)
    cache = {}; mk = marca()
    tmp = out + ".frames.raw"
    with open(tmp, "wb") as fh:
        for i, g in enumerate(seq):
            t = i / FPS
            im = Image.fromarray(g).convert("RGBA")
            im.alpha_composite(mk)
            atual = None
            for fz in frases:
                if fz["t"] <= t < fim_txt: atual = fz["texto"]
            if atual:
                if atual not in cache: cache[atual] = texto(atual)
                im.alpha_composite(cache[atual])
            fh.write(im.convert("RGB").tobytes())
        for im in final(int(cfg.get("final_seg", 4.0) * FPS)):
            fh.write(im.tobytes())
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                    "-r", str(FPS), "-i", tmp, "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                    "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], check=True)
    os.remove(tmp)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
