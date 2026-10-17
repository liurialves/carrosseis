"""Gera fundos escuros cinematográficos (1080x1350) para fatias do @liurialves sem foto.
Uso: python3 scripts/gerar_fundos_liuri.py  -> assets/liuri-fundos/*.jpg"""
import os, numpy as np
from PIL import Image, ImageFilter
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "liuri-fundos")
W, H = 1080, 1350
rng = np.random.default_rng(7)
yy, xx = np.mgrid[0:H, 0:W] / np.array([H, W])[:, None, None] if False else np.mgrid[0:H, 0:W]
xn, yn = xx / W, yy / H

def base(c=(10, 10, 10)):
    return np.ones((H, W, 3)) * np.array(c, float)

def glow(img, cx, cy, r, color, k=1.0):
    d = np.sqrt(((xn - cx) * W / H) ** 2 + (yn - cy) ** 2)
    a = np.clip(1 - d / r, 0, 1) ** 2 * k
    return img + a[..., None] * np.array(color, float)

def smoke(scale=60, k=40, blur=40):
    n = rng.random((H // scale + 2, W // scale + 2))
    im = Image.fromarray((n * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(blur))
    return (np.asarray(im, float) / 255 - .5)[..., None] * k

def finish(img, name, grain=10):
    img = img + rng.normal(0, grain, (H, W, 1))
    v = np.clip(1 - (((xn - .5) ** 2 + (yn - .45) ** 2) * 1.6), .25, 1)[..., None]
    Image.fromarray(np.clip(img * v, 0, 255).astype(np.uint8)).save(os.path.join(OUT, name), quality=92)

os.makedirs(OUT, exist_ok=True)
finish(glow(base(), .5, .05, .9, (90, 70, 20), 1) + smoke(), "01-luz-dourada.jpg")
finish(glow(base((8, 8, 9)), .85, .15, .8, (70, 50, 10), .9) + smoke(80, 55, 60), "02-fumaca.jpg")
img = base((9, 9, 10))
for i in range(0, W, 90):  # luz de janela / persiana
    img[:, i:i + 34] += np.clip(1 - yn[:, i:i + 34] * 1.3, 0, 1)[..., None] * np.array([38, 32, 18])
finish(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)) and np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)), float), "03-persiana.jpg")
finish(glow(glow(base(), .2, .1, .7, (60, 60, 70), .8), .9, .3, .5, (80, 55, 10), .7) + smoke(40, 30, 30), "04-cidade-noite.jpg")
img = base((7, 7, 8)); img += np.clip(1 - np.abs(xn - .5) * 5, 0, 1)[..., None] * np.clip(1 - yn * 1.1, 0, 1)[..., None] * np.array([70, 62, 40])
finish(img + smoke(70, 35, 50), "05-holofote.jpg")
finish(glow(base((12, 8, 6)), .5, .6, 1.0, (55, 25, 8), 1) + smoke(50, 50, 40), "06-brasa.jpg")
print("ok", sorted(os.listdir(OUT)))
