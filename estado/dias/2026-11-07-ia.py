"""Post de IA de 07/11/2026 (item 10 do playbook), no layout da referência @matheustilli (estilo tilli do render_clone.py;
06/11 foi hud). As pastas clonar-ia e referencias-99hud não têm prints novos (só IMG_0667..0674, já clonados em 02/11),
então o tema é uma ferramenta de IA em alta: PPT Master (hugohe3/ppt-master), listada no relatório
"AI Open Source Trends 2026-11-07" (agents-radar, issue #50) com cerca de 74 mil estrelas.
Conferido em 07/11/2026 pela busca do GitHub (search/repositories e search/code no README oficial):
74.302 estrelas, licença MIT, descrição "AI turns documents or topics into real, native PowerPoint decks—with native
shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and
support for your own .pptx templates", roda como workflow dentro de uma ferramenta de IA com agente (Claude Code, Cursor,
Copilot, Codex CLI...), instalação com Python 3.10–3.14 + pip, material (PDF, DOCX, imagens) na pasta projects/, gera
.pptx editável no computador ("your data stays local"). O projeto é gratuito e aberto; o modelo de IA usado é da conta
de quem instala (custo próprio).
CTA pela regra do dono de 02/11 (item 12): a palavra SLIDES leva ao link da mentoria no direct.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/04c62b7e-dce5-5dbd-8fa6-2ed5a6c62b3f/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-07"
REPO = {"tipo": "repo", "dono": "hugohe3", "nome": "ppt-master",
        "desc": "AI turns documents or topics into real, native PowerPoint decks, with data-backed charts and tables and support for your own .pptx templates.",
        "badges": ["★ 74.3k", "MIT", "Open source"], "h": 360}
T = lambda linhas: {"tipo": "terminal", "linhas": linhas}

tilli = {"estilo": "tilli", "slides": [
  {"tipo": "capa", "foto": "/tmp/px7/pexels-18935247.jpg", "foco_y": 0.45,
   "titulo": "Pare de montar apresentação de cliente slide por slide"},
  {"tipo": "item", "card": REPO, "titulo": "PPT Master", "sub": "Você entrega o material, ele monta o PowerPoint.",
   "bullets": ["Código aberto, licença MIT", "74,3 mil estrelas no GitHub em 07/11", "Gera um .pptx que você edita no PowerPoint", "Gráficos e tabelas nativos, não imagem colada"], "link": "github.com/hugohe3/ppt-master"},
  {"tipo": "item", "card": T(["> monte uma apresentação deste PDF", "# lê o material", "# organiza o argumento", "# exporta um .pptx editável"]),
   "titulo": "Como funciona", "sub": "Ele roda dentro de uma ferramenta de IA que trabalha no seu computador.",
   "bullets": ["Você põe PDF, Word ou imagens na pasta do projeto", "Pede no chat o que quer", "Ele estrutura a ideia antes de desenhar", "Entrega o arquivo para você ajustar"], "link": "Claude Code, Cursor, Copilot e outros"},
  {"tipo": "item", "card": T(["# usa o modelo .pptx da sua empresa", "# notas do orador viram narração em áudio", "# o material fica na sua máquina"]),
   "titulo": "O que chama atenção", "sub": "Ele respeita a identidade visual da sua empresa.",
   "bullets": ["Aceita o seu próprio modelo de PowerPoint", "Narração em áudio a partir das notas", "Gera tudo no seu computador", "Você escolhe o modelo de IA"], "link": "Arquivo nativo do PowerPoint"},
  {"tipo": "item", "card": T(["# proposta comercial", "# resultado do mês para o sócio", "# aula ou workshop", "# apresentação da empresa"]),
   "titulo": "Onde eu usaria", "sub": "Tudo o que hoje você monta à mão na véspera.",
   "bullets": ["Proposta para cliente a partir do orçamento", "Resultado do mês em gráfico", "Material de aula ou workshop", "Apresentação da empresa para parceiro"], "link": "Depois, você revisa e ajusta"},
  {"tipo": "item", "card": T(["# precisa do Python 3.10 a 3.14", "# precisa de uma ferramenta de IA com agente", "# o uso da IA tem custo próprio"]),
   "titulo": "Os limites", "sub": "Antes de instalar, saiba o que ele exige.",
   "bullets": ["Instala com Python, não é app de clicar", "A ferramenta de IA é sua, com o custo dela", "Confira números e textos antes de enviar", "Revise slide a slide no PowerPoint"], "link": "Grátis, mas pede configuração"},
  {"tipo": "cta", "palavra": "SLIDES", "promessa": "A MINHA MENTORIA",
   "itens": ["Como eu uso IA no meu negócio", "O passo a passo da mentoria", "Acesso direto comigo", "Para quem é e como começar"]},
]}

LEGENDA = """Você ainda monta apresentação de cliente slide por slide, na véspera, até tarde?

O PPT Master é um projeto de código aberto (licença MIT) que transforma PDF, Word ou um tema numa apresentação de PowerPoint editável, com gráficos e tabelas nativos e com o modelo de slides da sua empresa. A página dele no GitHub mostrava 74,3 mil estrelas hoje, 07/11.

Ele roda dentro de uma ferramenta de IA que trabalha no seu computador (Claude Code, Cursor, Copilot e outras). Os limites: a instalação pede Python, o uso da IA tem custo próprio e o resultado precisa de revisão antes de ir para o cliente.

🔻 Comente SLIDES que eu te mando no direct como funciona a minha mentoria, onde eu mostro como uso IA no meu negócio. Siga @liurialves.

#inteligenciaartificial #produtividade #empresario #empreendedorismo #ferramentasdeia"""


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_clone.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    run(tilli, f"{R}/posts/{DIA}/liurialves-4"); print("ok ia")
