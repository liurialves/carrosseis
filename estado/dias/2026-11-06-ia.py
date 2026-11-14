"""Post de IA de 06/11/2026 (item 10 do playbook), no layout da referência @99hud (estilo hud do render_clone.py).
As pastas clonar-ia e referencias-99hud não têm prints novos (só IMG_0667..0674, já clonados em 02/11), então o tema é
uma ferramenta de IA em alta (relatório "AI Open Source Trends 2026-11-06" do agents-radar): CowAgent (zhayujie/CowAgent).
Conferido em 06/11/2026 na página oficial github.com/zhayujie/CowAgent: 47,6 mil estrelas, licença MIT, descrição do
"About", canais (web, Telegram, Slack, Discord, WeChat, Feishu/Lark, DingTalk, WeCom), cliente para macOS e Windows,
Docker, instalação por linha de comando, aviso de que o modo agente gasta mais tokens e de que o agente acessa o sistema
operacional (usar só em ambiente de confiança). A página não fala em preço; diz que liga nos principais fornecedores de
modelo, por isso o post diz que você usa a sua conta num fornecedor de IA, que tem custo próprio.
Descartado: anomalyco/hex (ditado por voz, repetiria o tema do Handy de 05/11).
CTA pela regra do dono de 02/11 (item 12): a palavra AGENTE leva ao link da mentoria no direct, nunca ao link da ferramenta.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/3de97be0-9b10-54e4-a03c-47adc178e7b7/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-06"

hud = {"estilo": "hud", "slides": [
  {"texto": "Tem um assistente de IA de código aberto, com quase 48 mil estrelas no GitHub, que roda no seu próprio computador e conversa com você pelo Telegram.\n\nDeslize que eu mostro o que ele faz e o que ele exige.",
   "imagem": {"tipo": "terminal", "linhas": ["> resuma a proposta do cliente", "> pesquise os preços do concorrente", "# o agente planeja, executa e lembra"]}},
  {"texto": "O nome é **CowAgent**. Licença **MIT**, código aberto, e a página dele no GitHub mostrava **47,6 mil estrelas** hoje, 06/11.",
   "imagem": {"tipo": "repo", "dono": "zhayujie", "nome": "CowAgent", "desc": "Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge.", "badges": ["★ 47.6k", "MIT", "Open source"], "h": 360}},
  {"texto": "Ele divide o pedido em etapas, usa ferramentas como **busca na web**, **leitura de arquivos** e **navegador**, e guarda **memória** do que vocês já conversaram."},
  {"texto": "Conecta em vários canais: **web**, **Telegram**, **Slack** e **Discord**, além de apps de mensagem da China.\n\nTem cliente para **macOS** e **Windows** e também roda em **Docker**."},
  {"texto": "Você escolhe o modelo. Ele liga nos principais fornecedores de IA, então você usa a sua conta num deles, e esse uso tem custo próprio."},
  {"texto": "Onde eu vejo uso numa pequena empresa: um assistente interno que resume documento, pesquisa concorrente e consulta uma base com as regras da casa, que ele monta em arquivos de texto."},
  {"texto": "Os limites estão na própria página. O modo agente gasta bem mais do que uma conversa normal, e o agente tem acesso ao sistema do computador, por isso só deve rodar em ambiente de confiança.\n\nA instalação é por linha de comando. Não é para quem nunca abriu um terminal."},
  {"texto": "Eu acompanho essas ferramentas e trago para cá só o que dá para usar num negócio de verdade.\n\nComente **AGENTE** que eu te mando no direct como funciona a minha mentoria.\n\nSiga @liurialves."},
]}

LEGENDA = """Já imaginou um assistente de IA que roda no seu computador, conversa com você pelo Telegram e lembra o que vocês combinaram?

O CowAgent é de código aberto (licença MIT) e a página dele no GitHub mostrava 47,6 mil estrelas hoje, 06/11. Ele divide o pedido em etapas, usa busca na web, leitura de arquivos e navegador, e guarda memória das conversas. Conecta em web, Telegram, Slack e Discord, com cliente para macOS e Windows.

Os limites: você usa a sua conta num fornecedor de IA, que tem custo próprio; o modo agente gasta bem mais do que uma conversa normal; e o agente acessa o sistema do computador, então só deve rodar em ambiente de confiança. A instalação é por linha de comando.

🔻 Comente AGENTE que eu te mando no direct como funciona a minha mentoria. Siga @liurialves.

#inteligenciaartificial #empresario #produtividade #empreendedorismo #ferramentasdeia"""


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_clone.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    run(hud, f"{R}/posts/{DIA}/liurialves-4"); print("ok ia")
