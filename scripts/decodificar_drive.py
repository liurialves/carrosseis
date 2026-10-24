"""
Converte resultados do conector Google Drive (download_file_content) em JPGs prontos.

O conector devolve {content: base64, id, title, mimeType}. Quando o arquivo é grande,
o resultado é salvo num .txt (JSON) em tool-results. Passe esses caminhos aqui.

Uso:
    python3 scripts/decodificar_drive.py PASTA_SAIDA arquivo1.txt [arquivo2.txt ...]
Saída: PASTA_SAIDA/<fileId>.jpg (orientação corrigida, máx. 1600px). HEIC suportado.
Imprime "fileId<TAB>titulo<TAB>caminho" por linha.
"""
import base64, io, json, os, sys
from PIL import Image, ImageOps

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass  # pip install pillow-heif --break-system-packages


def main(out_dir, files):
    os.makedirs(out_dir, exist_ok=True)
    for f in files:
        try:
            d = json.load(open(f, encoding="utf-8"))
            im = Image.open(io.BytesIO(base64.b64decode(d["content"])))
            im = ImageOps.exif_transpose(im).convert("RGB")
            im.thumbnail((1600, 1600))
            dst = os.path.join(out_dir, f"{d['id']}.jpg")
            im.save(dst, "JPEG", quality=88)
            print(f"{d['id']}\t{d['title']}\t{dst}")
        except Exception as e:  # um arquivo ruim não derruba o lote
            print(f"ERRO\t{f}\t{e}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
