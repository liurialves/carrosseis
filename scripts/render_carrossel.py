"""
Renderiza um carrossel Darkgram a partir de um JSON e salva JPGs prontos pro Buffer.

Uso:
    python3 scripts/render_carrossel.py config.json posts/AAAA-MM-DD/perfil-N

config.json:
{
  "hook": "texto da capa",
  "hook_hl": "trecho em destaque",
  "accent": "#F5C518",
  "logo_png": "/caminho/logo.png" ou null,
  "slides": ["paragrafo\\n\\nparagrafo\\n\\n<span class='hl'>soco</span>", ... 8 itens],
  "images": {"cover": "/caminho.jpg", "2": "/caminho.jpg", ... "9": ...}
}
Saída: CAPA.jpg, fatia-1.jpg ... fatia-8.jpg (1080x1350).
"""
import json, os, sys, tempfile
from PIL import Image

SKILL = "/mnt/skills/plugins/um-clique-darkgram/references"
sys.path.insert(0, SKILL)
from render import build_carousel  # noqa: E402


def main(cfg_path, out_dir):
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    imgs = {}
    for k, v in (cfg.get("images") or {}).items():
        if v and os.path.exists(v):
            imgs["cover" if k == "cover" else int(k)] = v
    cfg["images"] = imgs
    cfg.setdefault("accent", "#F5C518")
    cfg.setdefault("logo_mode", "branco")
    if cfg.get("logo_png") and not os.path.exists(cfg["logo_png"]):
        cfg["logo_png"] = None
    assert len(cfg["slides"]) == 8, "precisa de 8 fatias"
    tmp = tempfile.mkdtemp()
    pngs = build_carousel(cfg, out_dir=tmp)
    os.makedirs(out_dir, exist_ok=True)
    out = []
    for p in pngs:
        nome = os.path.splitext(os.path.basename(p))[0] + ".jpg"
        dst = os.path.join(out_dir, nome)
        Image.open(p).convert("RGB").save(dst, "JPEG", quality=90, optimize=True)
        out.append(dst)
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
