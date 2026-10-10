#!/usr/bin/env bash
# Publica as imagens do dia no GitHub mantendo o repositório leve.
# Mantém só as pastas posts/ dos últimos 4 dias e reescreve o histórico
# num único commit (as imagens antigas já foram puxadas pelo Buffer).
#
# Uso: bash scripts/publicar_github.sh
set -euo pipefail
cd "$(dirname "$0")/.."

LIMITE=$(date -u -d '4 days ago' +%F)
for d in posts/*/; do
  dia=$(basename "$d")
  [[ "$dia" < "$LIMITE" ]] && rm -rf "$d"
done

git checkout -q --orphan tmp-publicacao
git add -A
git -c user.name="liurialves" -c user.email="liurialves@outlook.com" \
  commit -qm "Carrosséis $(date -u +%F)"
git branch -D main -q 2>/dev/null || true
git branch -m main
git push -f -q origin main
echo "OK: publicado em https://raw.githubusercontent.com/liurialves/carrosseis/main/posts/"
