"""Preset de cor do Liuri (dono, 18/11/2026: "sempre edite as fotos dentro dos presets").
O preset foi aprendido das fotos que o dono mandou já editadas por ele (original x editada):
lagoa-biceps-de-frente(-editada) e casal-noite-pousada(-editada). Modelo polinomial RGB guardado em
assets/preset/preset-liuri.npy e aplicado por uma LUT 3D de 33 pontos.

Uso como módulo:  from preset_liuri import aplicar;  im = aplicar(im)            (PIL.Image RGB)
Uso na linha de comando:  python3 scripts/preset_liuri.py entrada.jpg saida.jpg
Não aplicar em prints de prova (Stripe, Revolut, Meta Ads, planilha) nem em fotos Pexels.
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
_LUT = None


def _feats(a):
    r, g, b = a[:, 0], a[:, 1], a[:, 2]
    cols = [np.ones_like(r)]
    for i in range(4):
        for j in range(4 - i):
            for k in range(4 - i - j):
                if i + j + k > 0:
                    cols.append(r ** i * g ** j * b ** k)
    return np.stack(cols, 1)


def _lut():
    global _LUT
    if _LUT is None:
        W = np.load(os.path.join(R, "assets", "preset", "preset-liuri.npy"))
        n = 33
        s = np.linspace(0, 1, n)
        rr, gg, bb = np.meshgrid(s, s, s, indexing="ij")
        grid = np.stack([rr.ravel(), gg.ravel(), bb.ravel()], 1)
        out = np.clip(_feats(grid) @ W, 0, 1)
        # ordem do ImageFilter.Color3DLUT: r varia mais rápido
        out = out.reshape(n, n, n, 3).transpose(2, 1, 0, 3).reshape(-1, 3)
        _LUT = ImageFilter.Color3DLUT(n, out.ravel().tolist())
    return _LUT


def aplicar(im):
    return im.convert("RGB").filter(_lut())


if __name__ == "__main__":
    aplicar(Image.open(sys.argv[1])).save(sys.argv[2], quality=92)
