"""
Recorta o slide de um print de tela do Instagram (iPhone, tema escuro) e devolve 1080x1350 pronto para repostar.
Uso pedido pelo dono em 02/11/2026 para os reposts AUTORIZADOS do @modocaverna (1 por dia): o carrossel fica igual,
só a legenda muda.

Uso:  python3 scripts/recortar_prints.py SAIDA print1.jpg print2.jpg ...   (na ordem dos slides)
Saída: SAIDA/CAPA.jpg, SAIDA/fatia-1.jpg, ...  e imprime, por slide, se limpou os selos da interface
("1/8" no canto de cima e o ícone de som embaixo). Em fundo de foto o selo não é apagado: confira a prancha.
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter

UI_MEAN, UI_STD = 15.7, 6.0


def eh_ui(a, y):
    r = a[y]; return abs(r.mean() - UI_MEAN) < 4 and r.std() < UI_STD


def area_post(im):
    """Acha a base do post (onde começa a barra de curtidas) e sobe largura*1,25 (4:5) ou largura (1:1)."""
    a = np.asarray(im.convert("RGB")).astype(float); h, w, _ = a.shape
    base = None
    for y in range(int(h * 0.55), int(h * 0.9)):
        if not eh_ui(a, y - 1) and all(eh_ui(a, y + k) for k in range(0, 6)):
            base = y; break
    if base is None:
        raise SystemExit("não achei a base do post no print")
    for prop in (1.25, 1.0):
        topo = base - int(round(w * prop))
        if topo > 0 and eh_ui(a, topo - 2):
            return (0, topo, w, base)
    return (0, base - int(round(w * 1.25)), w, base)


def limpa(im, caixa):
    """Pinta a caixa com a cor da borda se a borda for lisa (fundo chapado). Devolve True se limpou."""
    a = np.asarray(im).astype(float)
    x0, y0, x1, y1 = caixa; m = 6
    borda = np.concatenate([a[y0 - m:y0, x0:x1].reshape(-1, 3), a[y1:y1 + m, x0:x1].reshape(-1, 3),
                            a[y0:y1, x0 - m:x0].reshape(-1, 3), a[y0:y1, x1:x1 + m].reshape(-1, 3)])
    if borda.std(axis=0).max() > 14:
        return False
    cor = tuple(int(c) for c in np.median(borda, axis=0))
    im.paste(cor, (x0, y0, x1, y1)); return True


def processa(arq):
    im = Image.open(arq).convert("RGB")
    sl = im.crop(area_post(im)).resize((1080, 1350), Image.LANCZOS)
    ok1 = limpa(sl, (930, 24, 1060, 102)) or limpa(sl, (915, 10, 1068, 112))     # contador 1/8
    limpa(sl, (36, 1185, 205, 1340))          # selo de repost (avatar) no canto de baixo
    ok2 = limpa(sl, (950, 1225, 1062, 1335))  # ícone de som
    sl = sl.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    return sl, ok1, ok2


if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for i, f in enumerate(sys.argv[2:]):
        sl, a, b = processa(f)
        nome = "CAPA.jpg" if i == 0 else f"fatia-{i}.jpg"
        sl.save(os.path.join(out, nome), quality=93)
        print(nome, "contador:", "limpo" if a else "VERIFICAR", "| som:", "limpo" if b else "VERIFICAR")
