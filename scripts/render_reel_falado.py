"""
Edita um Reel em que o Liuri fala para a câmera, MANTENDO o áudio original, e intercala imagens (B-roll)
por cima enquanto a voz continua.

Uso: python3 scripts/render_reel_falado.py cfg.json reels/AAAA-MM-DD/falado-N.mp4
cfg.json:
{
  "video": "/tmp/v.mp4",                    # vídeo original (qualquer formato/orientação)
  "inicio": 0.0, "fim": null,               # corte opcional (segundos)
  "gancho": "Ninguém te conta isso sobre Portugal",   # texto no topo nos primeiros 3 s (opcional)
  "broll": [ {"de": 4.0, "ate": 6.5, "imagem": "/tmp/a.jpg", "texto": "frase opcional"}, ... ],
  "pb": false                                # true = tudo em preto e branco
}
Saída: 1080x1920, 30 fps, H.264 + AAC (voz original normalizada), faststart.
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONT = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
if not os.path.exists(FONT): FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
W, H = 1080, 1920


def png_texto(t, out, y, size=60, caixa=False):
    f = ImageFont.truetype(FONT, size); im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    linhas, cur = [], ""
    for w in t.split():
        test = (cur + " " + w).strip()
        if d.textlength(test, font=f) <= 940: cur = test
        else: linhas.append(cur); cur = w
    linhas.append(cur); lh = int(size * 1.3)
    if caixa:
        hbox = lh * len(linhas) + 40
        d.rounded_rectangle((40, y - 20, W - 40, y - 20 + hbox), 24, fill=(0, 0, 0, 170))
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    for i, l in enumerate(linhas):
        ds.text(((W - d.textlength(l, font=f)) / 2, y + i * lh), l, font=f, fill=(0, 0, 0, 230))
    im = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)), im); d = ImageDraw.Draw(im)
    for i, l in enumerate(linhas):
        d.text(((W - d.textlength(l, font=f)) / 2, y + i * lh), l, font=f, fill="white")
    im.save(out)


def main(cfg_path, out):
    c = json.load(open(cfg_path, encoding="utf-8")); tmp = tempfile.mkdtemp()
    ini = float(c.get("inicio") or 0); fim = c.get("fim")
    cut = ["-ss", str(ini)] + (["-to", str(fim)] if fim else [])
    base = os.path.join(tmp, "base.mp4"); cor = ",hue=s=0" if c.get("pb") else ""
    subprocess.run(["ffmpeg", "-v", "error", "-y", *cut, "-i", c["video"], "-vf",
                    f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1{cor}",
                    "-af", "highpass=f=80,loudnorm=I=-14:TP=-1.5", "-c:v", "libx264", "-preset", "veryfast", "-crf", "21",
                    "-c:a", "aac", "-b:a", "160k", base], check=True)
    inputs = ["-i", base]; fc = []; last = "0:v"; k = 1
    if c.get("gancho"):
        p = os.path.join(tmp, "g.png"); png_texto(c["gancho"], p, 260, 66, caixa=True)
        inputs += ["-i", p]; fc.append(f"[{last}][{k}:v]overlay=0:0:enable='between(t,0,3)'[v{k}]"); last = f"v{k}"; k += 1
    for j, b in enumerate(c.get("broll", [])):
        if not os.path.exists(b["imagem"]): continue
        de, ate = float(b["de"]), float(b["ate"]); n = max(int((ate - de) * 30), 1)
        clip = os.path.join(tmp, f"b{j}.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", b["imagem"], "-vf",
                        f"scale=1200:2134:force_original_aspect_ratio=increase,crop=1200:2134,zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps=30{cor}",
                        "-frames:v", str(n), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "veryfast", clip], check=True)
        inputs += ["-itsoffset", str(de), "-i", clip]
        fc.append(f"[{last}][{k}:v]overlay=0:0:eof_action=pass:enable='between(t,{de},{ate})'[v{k}]"); last = f"v{k}"; k += 1
        if b.get("texto"):
            p = os.path.join(tmp, f"t{j}.png"); png_texto(b["texto"], p, 1150, 58)
            inputs += ["-i", p]; fc.append(f"[{last}][{k}:v]overlay=0:0:enable='between(t,{de},{ate})'[v{k}]"); last = f"v{k}"; k += 1
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    cmd = ["ffmpeg", "-v", "error", "-y", *inputs]
    if fc: cmd += ["-filter_complex", ";".join(fc), "-map", f"[{last}]"]
    else: cmd += ["-map", "0:v"]
    cmd += ["-map", "0:a?", "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True); print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
