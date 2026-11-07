"""
Busca e baixa fotos do Pexels (licença livre) para os carrosséis do @liurialves.

Pré-requisitos (configurados no ambiente cloud da rotina, ver PLAYBOOK):
- Rede: api.pexels.com e images.pexels.com liberados.
- Chave: guardada como "network secret" do ambiente para api.pexels.com (o proxy injeta o header
  Authorization sozinho) OU na variável de ambiente PEXELS_API_KEY.

Uso:
    python3 scripts/buscar_pexels.py PASTA_SAIDA "man silhouette dark" "boxing gym" ... [--n 6]
Saída: PASTA_SAIDA/pexels-<id>.jpg (retrato, máx. 1600px) e PASTA_SAIDA/creditos.json
Imprime "pexels:<id><TAB>fotógrafo<TAB>caminho" por foto. Usa só fotos que ainda não estão em
estado/historico.json (campo fotos, prefixo "pexels:").
"""
import io, json, os, sys, urllib.parse, urllib.request
from PIL import Image

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def usadas():
    try:
        h = json.load(open(os.path.join(RAIZ, "estado", "historico.json"), encoding="utf-8"))
        return {f for p in h.get("posts", []) for f in p.get("fotos", []) if str(f).startswith("pexels:")}
    except Exception:
        return set()


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "carrosseis-liuri/1.0", **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main(out, termos, n):
    os.makedirs(out, exist_ok=True)
    key = os.environ.get("PEXELS_API_KEY")
    hdr = {"Authorization": key} if key else {}  # sem chave local: o network secret do ambiente injeta
    ja = usadas(); creditos = []
    for t in termos:
        q = urllib.parse.urlencode({"query": t, "per_page": 30, "orientation": "portrait"})
        try:
            data = json.loads(get(f"https://api.pexels.com/v1/search?{q}", hdr))
        except Exception as e:
            print(f"ERRO busca '{t}': {e}", file=sys.stderr); continue
        pegou = 0
        for ph in data.get("photos", []):
            pid = f"pexels:{ph['id']}"
            if pid in ja or pegou >= n:
                continue
            try:
                im = Image.open(io.BytesIO(get(ph["src"]["large2x"]))).convert("RGB")
                im.thumbnail((1600, 1600))
                dst = os.path.join(out, f"pexels-{ph['id']}.jpg"); im.save(dst, "JPEG", quality=90)
            except Exception as e:
                print(f"ERRO foto {ph['id']}: {e}", file=sys.stderr); continue
            ja.add(pid); pegou += 1
            creditos.append({"id": pid, "termo": t, "fotografo": ph.get("photographer"), "url": ph.get("url"), "arquivo": dst})
            print(f"{pid}\t{ph.get('photographer')}\t{dst}")
    json.dump(creditos, open(os.path.join(out, "creditos.json"), "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    args = sys.argv[1:]; n = 4
    if "--n" in args:
        i = args.index("--n"); n = int(args[i + 1]); del args[i:i + 2]
    main(args[0], args[1:], n)
