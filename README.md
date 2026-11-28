# carrosseis

Imagens dos carrosséis diários do Instagram (@liurialves e @spatherapieslisbon),
geradas automaticamente e publicadas pelo Buffer.

- `PLAYBOOK.md` — como a rotina diária funciona.
- `posts/AAAA-MM-DD/<perfil>-<n>/` — imagens dos últimos dias (as antigas são apagadas).
- `estado/historico.json` — o que já foi postado, para não repetir tema nem foto.
- `scripts/` — render, conversão das fotos do Drive e publicação.

Para trocar fotos: coloque novas imagens na pasta `fotos` do Google Drive
("conteudo para o instagram"). A rotina usa primeiro as mais novas.
