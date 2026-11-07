"""Posts de IA clonados no layout das referências (pedido do dono em 02/11/2026: "clone identicamente, continue sendo de IA,
remodele como a mensagem é passada, sem perder o contexto, com os mesmos designs; mais 2 posts, total 5 por dia").
liurialves-4: layout @99hud (card tweet branco + imagem), tema MarkItDown. Dados verificados em 02/11 (GitHub e doc da Anthropic).
liurialves-5: layout @matheustilli (capa escura + slides pretos com card + título laranja + CTA código), 6 repositórios.
Estrelas e licenças conferidas nas páginas do GitHub em 02/11/2026. Nada de nome, @, foto ou arte deles.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/a82b3699-a12b-52b3-8a6b-6c577fd56db7/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-02"

hud = {"estilo": "hud", "slides": [
  {"texto": "Se você anexa PDF, Word ou Excel direto no Claude ou no ChatGPT, está queimando o seu limite sem perceber.\n\nE quem diz isso é a própria documentação da Anthropic.\n\nDeslize que eu mostro.", "imagem": {"tipo": "pdfmd"}},
  {"texto": "Quando você anexa um PDF, o Claude não recebe só o texto.\n\nSegundo a documentação oficial, **cada página vira uma imagem**, e o texto extraído vai junto com ela. Você paga pelas duas coisas.", "imagem": {"tipo": "paginas"}},
  {"texto": "A conta é simples. Cada página costuma gastar de **1.500 a 3.000 tokens** só de texto, e o custo da imagem entra por cima.\n\nUm relatório de 40 páginas passa de **60 mil tokens** antes mesmo da sua pergunta."},
  {"texto": "A saída é gratuita e vem da **Microsoft**: o **MarkItDown**.\n\nNão é projeto escondido. São mais de **192 mil estrelas** no GitHub.", "imagem": {"tipo": "repo", "dono": "microsoft", "nome": "markitdown", "desc": "Python tool for converting files and office documents to Markdown.", "badges": ["★ 192k", "MIT", "Python"], "h": 330}},
  {"texto": "Ele transforma PDF, Word, Excel, PowerPoint, HTML e até EPUB em **Markdown**, o texto limpo que a IA lê sem esforço.\n\nTítulos, listas, tabelas e links continuam no lugar.", "imagem": {"tipo": "terminal", "linhas": ["$ pip install 'markitdown[all]'", "$ markitdown relatorio.pdf -o relatorio.md", "# pronto: anexe o .md no lugar do PDF"]}},
  {"texto": "Na prática, você converte o arquivo uma vez e manda o **.md** para a IA no lugar do PDF.\n\nSem as imagens das páginas, sobra muito mais espaço no mesmo plano para a conversa que interessa."},
  {"texto": "Muita gente culpa a IA quando o limite acaba no meio da tarde.\n\nSó que, na maioria das vezes, o peso está no arquivo que você entrega para ela. Entregue do jeito certo e o mesmo plano rende muito mais."},
  {"texto": "Eu testo essas ferramentas antes de trazer para cá.\n\nQuer o link do MarkItDown e o passo a passo para instalar? Comente **PDF** que eu mando no seu direct.\n\nE siga @liurialves para não perder o próximo teste."},
]}

REPOS = [
 ("Hyperframes", "heygen-com", "hyperframes", "Write HTML. Render video. Built for agents.", ["★ 77.3k", "Apache-2.0"],
  "Você escreve a página, ele entrega o vídeo.",
  ["77,3 mil estrelas, licença Apache 2.0", "Transforma HTML e CSS em vídeo MP4", "Feito para agentes como o Claude Code", "Sem taxa por vídeo renderizado"]),
 ("Fincept Terminal", "Fincept-Corporation", "FinceptTerminal", "Modern finance application with market analytics, investment research and economic data tools.", ["★ 33k", "AGPL-3.0"],
  "Um terminal de mercado rodando no seu computador.",
  ["33 mil estrelas, licença AGPL-3.0", "Ações, cripto e dados de economia", "Agentes de IA com a sua própria chave", "Edição Enterprise paga, de US$ 15 a 45"]),
 ("Open-Generative-AI", "Anil-matcha", "Open-Generative-AI", "Open-source alternative to AI image and video platforms.", ["★ 31.6k", "MIT"],
  "Estúdio aberto de imagem e vídeo com IA.",
  ["31,6 mil estrelas, licença MIT", "Texto para imagem e imagem para vídeo", "Na nuvem, pede chave paga da Muapi", "Grátis de verdade só local, com GPU"]),
 ("Vibe-Trading", "HKUDS", "Vibe-Trading", "Your Personal Trading Agent.", ["★ 36.7k", "MIT"],
  "Um agente que testa estratégia antes de você arriscar.",
  ["36,7 mil estrelas, licença MIT", "Backtest e paper trading", "Puxa dados de mercado e liga em corretora", "Roda pela web, terminal ou MCP"]),
 ("Claude Ads", "AgriciDaniel", "claude-ads", "Paid-media operations skill for Claude Code across 12 ad platforms.", ["★ 8.5k", "MIT"],
  "O Claude auditando os seus anúncios.",
  ["8,5 mil estrelas, licença MIT", "12 plataformas, de Google a TikTok", "Audita a conta, planeja verba e relatório", "Rascunha mudanças, não aplica sozinho"]),
 ("Camofox Browser", "jo-inc", "camofox-browser", "Stealth headless browser for AI agents.", ["★ 11.9k", "MIT"],
  "Um navegador de verdade para o seu agente.",
  ["11,9 mil estrelas, licença MIT", "Baseado no Firefox, com anti-detecção", "Controlado por API, no lugar do Playwright", "Raspar site tem risco de bloqueio"]),
]

tilli = {"estilo": "tilli", "slides": [
  {"tipo": "capa", "foto": "/tmp/pxai/pexels-6424589.jpg", "foco_y": 0.45,
   "titulo": "Tem gente fazendo dinheiro em silêncio com repositórios gratuitos do GitHub e IA"}] +
  [{"tipo": "item", "card": {"tipo": "repo", "dono": d, "nome": n, "desc": desc, "badges": b, "h": 330},
    "titulo": t, "sub": sub, "bullets": bl, "link": f"github.com/{d}/{n}"} for t, d, n, desc, b, sub, bl in REPOS] +
  [{"tipo": "cta", "palavra": "REPO", "promessa": "OS 6 LINKS",
    "itens": ["Os 6 links oficiais, um por um", "A licença de cada repositório", "O que é grátis e o que é pago", "Por onde começar em cada um", "Como saber se o repo é o oficial"]}]}

LEGENDAS = {
 4: """O seu limite do Claude acaba rápido porque você anexa o PDF cru.

Segundo a documentação da Anthropic, cada página do PDF vira imagem e texto, e você paga pelos dois. Com o MarkItDown, a ferramenta gratuita da Microsoft com mais de 192 mil estrelas no GitHub, o arquivo vira Markdown e a IA lê só o texto limpo.

🔻 Comente PDF que eu mando o link e o passo a passo no direct. Siga @liurialves para o próximo teste.

#inteligenciaartificial #claude #chatgpt #produtividade #ferramentasdeia""",
 5: """6 repositórios gratuitos do GitHub que quem usa IA já está colocando para trabalhar.

Hyperframes, Fincept Terminal, Open-Generative-AI, Vibe-Trading, Claude Ads e Camofox Browser. Estrelas e licenças conferidas hoje, 02/11, e com o aviso do que é pago em cada um.

🔻 Siga o perfil e comente REPO que eu mando os 6 links oficiais no direct.

#inteligenciaartificial #github #opensource #ferramentasdeia #automacao""",
}


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_clone.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    run(hud, O(4)); run(tilli, O(5)); print("ok")
