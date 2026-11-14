"""
Prepara os carrosséis do @spatherapieslisbon de um dia para repostar à mão no TikTok da massagem.

Uso:  python3 scripts/pacote_tiktok_spa.py AAAA-MM-DD
Cria  tiktok-spa/AAAA-MM-DD/spatherapieslisbon-N/ (9 imagens numeradas na ordem) e spatherapieslisbon-N.zip
e imprime as URLs públicas de cada ZIP e de cada imagem, para colocar no documento do Drive.
Mantém só os últimos 14 dias em tiktok-spa/ (o publicar_github.sh guarda isso no repositório).
"""
import datetime, glob, os, shutil, sys, zipfile

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RAW = "https://raw.githubusercontent.com/liurialves/carrosseis/main/"


def main(dia):
    src = sorted(glob.glob(os.path.join(RAIZ, "posts", dia, "spatherapieslisbon-*")))
    out_dir = os.path.join(RAIZ, "tiktok-spa", dia)
    os.makedirs(out_dir, exist_ok=True)
    for d in src:
        nome = os.path.basename(d)
        ordem = ["CAPA"] + [f"fatia-{i}" for i in range(1, 9)]
        arqs = []
        for i, base in enumerate(ordem, 1):
            cand = [p for p in (os.path.join(d, base + ".jpg"), os.path.join(d, base + ".png")) if os.path.exists(p)]
            if cand:
                arqs.append((f"{i:02d}-{'capa' if i == 1 else 'slide'}{os.path.splitext(cand[0])[1]}", cand[0]))
        img_dir = os.path.join(out_dir, nome)
        os.makedirs(img_dir, exist_ok=True)
        for arcname, path in arqs:
            shutil.copy(path, os.path.join(img_dir, arcname))
        zp = os.path.join(out_dir, nome + ".zip")
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_STORED) as z:
            for arcname, path in arqs:
                z.write(path, arcname)
        print(f"## {nome}")
        print("ZIP: " + RAW + os.path.relpath(zp, RAIZ))
        for arcname, _ in arqs:
            print(f"{arcname}: {RAW}{os.path.relpath(img_dir, RAIZ)}/{arcname}")
    # limpeza: 14 dias
    limite = (datetime.date.fromisoformat(dia) - datetime.timedelta(days=14)).isoformat()
    for p in glob.glob(os.path.join(RAIZ, "tiktok-spa", "*")):
        if os.path.basename(p) < limite:
            shutil.rmtree(p, ignore_errors=True)


if __name__ == "__main__":
    main(sys.argv[1])
