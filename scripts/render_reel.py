"""
Renderiza um Reel 1080x1920 no estilo "frases curtas sobre fotos escuras" (@liurialves).

Uso: python3 scripts/render_reel.py reel.json reels/AAAA-MM-DD/reel-N.mp4
reel.json:
{
  "frases": [ {"texto": "acorda antes de todo mundo", "imagens": ["/tmp/a.jpg", "/tmp/b.jpg"]}, ... ],
  "segundos_por_frase": 2.4,          # opcional
  "musica": "/tmp/musica.mp3"          # opcional; sem música sai com áudio mudo
}
Visual: preto e branco, zoom lento, texto branco centrado com @liurialves pequeno embaixo.
Saída: MP4 H.264 + AAC, 30 fps, faststart (pronto para Buffer/Instagram/TikTok).
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
if not os.path.exists(FONT):
    FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FPS, W, H = 30, 1080, 1920


def wrap(d, t, font, maxw):
    linhas, cur = [], ""
    for w in t.split():
        test = (cur + " " + w).strip()
        if d.textlength(test, font=font) <= maxw: cur = test
        else: linhas.append(cur); cur = w
    return linhas + [cur]


def texto_png(t, out):
    f, s = ImageFont.truetype(FONT, 60), ImageFont.truetype(FONT, 30)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    linhas = wrap(d, t, f, 900); y0 = 900 - (len(linhas) - 1) * 40
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    for i, l in enumerate(linhas):
        ds.text(((W - d.textlength(l, font=f)) / 2, y0 + i * 78), l, font=f, fill=(0, 0, 0, 230))
    im = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(7)), im); d = ImageDraw.Draw(im)
    for i, l in enumerate(linhas):
        d.text(((W - d.textlength(l, font=f)) / 2, y0 + i * 78), l, font=f, fill="white")
    h = "@liurialves"; d.text(((W - d.textlength(h, font=s)) / 2, y0 + len(linhas) * 78 + 6), h, font=s, fill=(255, 255, 255, 110))
    im.save(out)


def main(cfg_path, out):
    cfg = json.load(open(cfg_path, encoding="utf-8")); tmp = tempfile.mkdtemp()
    spf = float(cfg.get("segundos_por_frase", 2.4)); clips = []; n = 0
    for i, fr in enumerate(cfg["frases"]):
        png = os.path.join(tmp, f"t{i}.png"); texto_png(fr["texto"], png)
        imgs = [p for p in fr["imagens"] if os.path.exists(p)] or [None]
        for img in imgs:
            nf = int(spf / len(imgs) * FPS); o = os.path.join(tmp, f"c{n:03d}.mp4"); n += 1
            src = ["-f", "lavfi", "-i", f"color=c=0x0b0a0a:s=1200x2134"] if img is None else ["-loop", "1", "-i", img]
            vf = ("scale=1200:2134:force_original_aspect_ratio=increase,crop=1200:2134,"
                  f"zoompan=z='1+0.06*on/{nf}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={nf}:s={W}x{H}:fps={FPS},"
                  "hue=s=0,eq=contrast=1.08:brightness=0.03:gamma=1.15,vignette=PI/6[b];[b][1:v]overlay=0:0")
            subprocess.run(["ffmpeg", "-v", "error", "-y", *src, "-i", png, "-filter_complex", vf, "-frames:v", str(nf),
                            "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", o], check=True)
            clips.append(o)
    lst = os.path.join(tmp, "l.txt"); open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    dur = len(cfg["frases"]) * spf
    mus = cfg.get("musica")
    aud = (["-i", mus, "-af", f"afade=t=in:d=0.5,afade=t=out:st={max(dur-1.5,0)}:d=1.5"] if mus and os.path.exists(mus)
           else ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"])
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, *aud, "-map", "0:v", "-map", "1:a",
                    "-t", str(dur), "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out], check=True)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
