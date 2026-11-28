"""Post de IA de 08/11/2026 (item 10 do playbook), no layout da referência @99hud (estilo hud do render_clone.py;
07/11 foi tilli). As pastas clonar-ia e referencias-99hud não têm prints novos (só IMG_0667..0674, já clonados em 02/11),
então o tema é uma ferramenta de IA em alta, pesquisada: Browser Use (browser-use/browser-use).
Conferido em 08/11/2026 pela busca do GitHub (search/repositories e search/code no README oficial):
120.277 estrelas, licença MIT, descrição "Open-source Python library for AI browser agents, plus Browser Use Cloud",
exemplo do README com Agent(task=..., llm=...), navegador na nuvem a US$ 0,02 por hora de navegador mais tráfego
(browser-use.com/pricing, citado no README). A biblioteca é gratuita; o modelo de IA é da conta de quem usa (custo próprio).
Descartado: browser-use/jev-ultrafast (24 mil estrelas, demo técnica com chaves de API, longe do dono de negócio).
Teste de valor: passo a passo num problema real (tabela de preços de 5 concorrentes), tarefa pronta para copiar,
critério de decisão e a versão manual em 30 minutos para quem não instala nada.
CTA (regra do dono de 08/11, comprador ideal): Comente CLIENTES; exemplos de personal trainer e barbearia; não promete link da ferramenta.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/a44d0111-cae6-53e8-80e2-036407ec1b26/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-08"

hud = {"estilo": "hud", "slides": [
  {"texto": "Você ainda abre o site de cada concorrente, um por um, para saber quanto ele cobra?\n\nTem um agente de IA de código aberto que faz essa volta por você e devolve uma tabela. Deslize que eu mostro como eu usaria.",
   "imagem": {"tipo": "terminal", "linhas": ["> abra o site de 5 concorrentes", "> anote serviço e preço", "# devolve uma tabela com a data de hoje"]}},
  {"texto": "O nome é **Browser Use**. Licença **MIT**, código aberto, e a página dele no GitHub mostrava **120 mil estrelas** hoje, 08/11.",
   "imagem": {"tipo": "repo", "dono": "browser-use", "nome": "browser-use", "desc": "Open-source Python library for AI browser agents, plus Browser Use Cloud and a hosted agent API.", "badges": ["★ 120k", "MIT", "Python"], "h": 360}},
  {"texto": "Ele abre um navegador e **clica, lê e preenche** como uma pessoa faria. Você escreve a tarefa em português e escolhe o modelo de IA que vai pensar por ele."},
  {"texto": "**Passo 1.** Liste 5 concorrentes diretos, com o site de cada um. Se você é personal trainer, as academias e os personais do seu bairro. Se é barbearia, as barbearias da sua rua."},
  {"texto": "**Passo 2.** Escreva a tarefa assim:\n\n\"Abra estes 5 sites. Em cada um, encontre o preço de [plano mensal de treino / corte + barba]. Monte uma tabela com empresa, serviço, preço e a data de hoje. Se o site não mostrar preço, escreva sem preço.\""},
  {"texto": "**Passo 3.** Ponha o seu preço na mesma tabela e responda a uma pergunta: o cliente entende por que o seu custa o que custa?\n\nSe você é o mais caro e o seu perfil não explica o motivo, é isso que você ajusta primeiro. Baixar o preço é o caminho mais rápido para continuar parado."},
  {"texto": "Os limites. Ele roda com **Python** e precisa da sua conta num fornecedor de IA, que tem custo próprio. O navegador na nuvem deles custa **US$ 0,02 por hora**, mais o tráfego. Respeite os termos de uso de cada site.\n\nSem instalar nada, você faz a mesma tabela à mão em 30 minutos seguindo os passos 1 a 3."},
  {"texto": "Eu trago para cá só ferramenta que dá para usar num negócio de verdade.\n\nSe a sua empresa está parada no mesmo faturamento, comente **CLIENTES** que eu te chamo no direct.\n\nSiga @liurialves."},
]}

LEGENDA = """Quanto cobram hoje as 5 academias, personais ou barbearias que o seu cliente compara com você? Se você não sabe responder sem abrir site por site, este post é para você.

O Browser Use é uma biblioteca de código aberto (licença MIT) que controla um navegador com IA: abre, clica, lê e devolve o que você pediu. A página dele no GitHub mostrava 120 mil estrelas hoje, 08/11.

Como eu usaria: lista dos 5 concorrentes que o seu cliente compara com você, a tarefa pronta do slide 5 e, no fim, o seu preço na mesma tabela com uma pergunta só: o cliente entende por que o seu custa o que custa?

Os limites: pede Python, a IA tem custo próprio e o navegador na nuvem deles custa US$ 0,02 por hora mais tráfego. Sem instalar nada, a mesma tabela sai à mão em 30 minutos.

🔻 Se a sua empresa está parada no mesmo faturamento, comente CLIENTES que eu te chamo no direct. Siga @liurialves.

#inteligenciaartificial #donodenegocio #personaltrainer #barbearia #precificacao"""


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_clone.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    run(hud, f"{R}/posts/{DIA}/liurialves-4"); print("ok ia")
