"""Post de IA de 04/11/2026 (item 10 do playbook), no layout da referência @99hud (estilo hud do render_clone.py).
As pastas clonar-ia e referencias-99hud do Drive estavam vazias, então o tema é uma ferramenta de IA em alta,
pesquisada e conferida hoje na página oficial: Ollama (github.com/ollama/ollama, 184,7 mil estrelas, licença MIT).
CTA pela regra do dono de 02/11 (item 12): a palavra leva ao link da mentoria no direct, nunca ao link da ferramenta.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/a82b3699-a12b-52b3-8a6b-6c577fd56db7/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-04"

hud = {"estilo": "hud", "slides": [
  {"texto": "Todo dia alguém cola contrato, lista de cliente e número do mês dentro de uma IA na internet, sem ler onde aquilo vai parar.\n\nDá para rodar a IA dentro do seu próprio computador.\n\nDeslize que eu mostro.",
   "imagem": {"tipo": "terminal", "linhas": ["$ ollama run gemma4", "# o modelo roda aqui, no seu computador"]}},
  {"texto": "O programa chama-se **Ollama**. É aberto, licença **MIT**, e a página dele no GitHub passa de **184 mil estrelas**.",
   "imagem": {"tipo": "repo", "dono": "ollama", "nome": "ollama", "desc": "Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.", "badges": ["★ 184.7k", "MIT", "Go"], "h": 340}},
  {"texto": "Instala em **macOS**, **Windows** e **Linux**, e também roda em Docker.\n\nDepois disso é um comando só para abrir um modelo e começar a conversar."},
  {"texto": "Ele roda modelos abertos conhecidos: **Gemma**, **Llama**, **Qwen**, **Mistral**, **DeepSeek** e **gpt-oss**.\n\nTudo dentro da sua máquina, sem conta e sem navegador."},
  {"texto": "A diferença que interessa a quem tem empresa é simples. **O texto não sai do seu computador.**\n\nProposta, contrato, tabela de preço e lista de cliente ficam onde estão."},
  {"texto": "Eles também oferecem uma versão na nuvem, que é outra coisa.\n\nSe for usar a nuvem, leia as condições no site antes de colar documento de cliente lá dentro."},
  {"texto": "Não serve para tudo. Modelo rodando em casa pede computador com memória sobrando e responde mais devagar do que os serviços pagos.\n\nPara rascunho, resumo e texto interno, resolve bem."},
  {"texto": "Eu testo essas ferramentas antes de trazer para cá, e o tempo que elas poupam eu ponho onde dá dinheiro: oferta, funil e atendimento.\n\nComente **IA** que eu te mando no direct como funciona a minha mentoria de crescimento.\n\nSiga @liurialves."},
]}

LEGENDA = """Você cola contrato, proposta e lista de cliente dentro de uma IA na internet sem ler onde aquilo vai parar?

Dá para rodar a IA dentro do seu computador. O programa é o Ollama: aberto, licença MIT, mais de 184 mil estrelas no GitHub, e instala em macOS, Windows e Linux. Ele roda modelos abertos conhecidos e o texto não sai da sua máquina.

Não serve para tudo. Pede computador com memória sobrando e responde mais devagar que os serviços pagos. Para rascunho, resumo e texto interno, resolve bem.

🔻 Comente IA que eu te mando no direct como funciona a minha mentoria de crescimento. Siga @liurialves.

#inteligenciaartificial #empresario #produtividade #empreendedorismo #negocioproprio"""


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_clone.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    run(hud, f"{R}/posts/{DIA}/liurialves-4"); print("ok ia")
