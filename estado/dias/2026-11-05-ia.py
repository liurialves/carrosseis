"""Post de IA de 05/11/2026 (item 10 do playbook), no layout da referência @matheustilli (estilo tilli do render_clone.py).
As pastas clonar-ia e referencias-99hud não têm prints novos (só IMG_0667..0674, já clonados em 02/11), então o tema é
uma ferramenta de IA em alta (lista de trending de 02-04/11/2026): Handy (cjpais/Handy), ditado por voz offline.
Conferido em 05/11/2026: licença MIT, grátis e código aberto, Windows/macOS/Linux, modelos Whisper e Parakeet, atalho
de teclado que grava e cola o texto no campo ativo, áudio não sai do computador (espelho oficial do projeto no
SourceForge e guia da Better Stack de 03/08/2026). A página do GitHub não pôde ser aberta nesta execução, por isso o
post NÃO cita número de estrelas.
CTA pela regra do dono de 02/11 (item 12): a palavra VOZ leva ao link da mentoria no direct, nunca ao link da ferramenta.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/3ad2a2f4-1f39-5a28-8d68-94cb43b73f16/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-05"
REPO = {"tipo": "repo", "dono": "cjpais", "nome": "Handy", "desc": "Free, open source and offline speech-to-text app. Press a shortcut and speak.", "badges": ["MIT", "Offline", "Grátis"], "h": 360}
T = lambda linhas: {"tipo": "terminal", "linhas": linhas}

tilli = {"estilo": "tilli", "slides": [
  {"tipo": "capa", "foto": "/tmp/px5/pexels-6860629.jpg", "foco_y": 0.45,
   "titulo": "Pare de digitar proposta de cliente com dois dedos"},
  {"tipo": "item", "card": REPO, "titulo": "Handy", "sub": "Você fala, ele escreve. No seu computador.",
   "bullets": ["Código aberto, licença MIT", "Gratuito, sem conta e sem assinatura", "Funciona sem internet", "Windows, macOS e Linux"], "link": "github.com/cjpais/Handy"},
  {"tipo": "item", "card": T(["# 1. aperte o atalho do teclado", "# 2. fale normalmente", "# 3. solte o atalho", "# o texto aparece onde o cursor está"]),
   "titulo": "Como funciona", "sub": "Um atalho e a sua voz vira texto em qualquer programa.",
   "bullets": ["E-mail, WhatsApp Web, documento, planilha", "Modo segurar para falar ou liga e desliga", "Corta o silêncio antes de transcrever"], "link": "Atalho configurável"},
  {"tipo": "item", "card": T(["# áudio processado no seu computador", "# nada é enviado para servidor", "# modelos: Whisper e Parakeet"]),
   "titulo": "Sem nuvem", "sub": "O que você fala não sai da sua máquina.",
   "bullets": ["Bom para conversa de cliente e número da empresa", "Whisper usa a placa de vídeo, quando tem", "Parakeet roda só no processador", "Você baixa o modelo uma vez"], "link": "Reconhece o idioma sozinho"},
  {"tipo": "item", "card": T(["# ditado: proposta para cliente", "# ditado: resposta de orçamento", "# ditado: roteiro de vídeo", "# ditado: ata da reunião"]),
   "titulo": "Onde eu usaria", "sub": "Tudo o que você explica bem falando e trava escrevendo.",
   "bullets": ["Rascunho de proposta em poucos minutos", "Resposta longa de WhatsApp sem digitar", "Roteiro de Reels falado de primeira", "Anotação logo depois da reunião"], "link": "Depois, você só revisa"},
  {"tipo": "item", "card": T(["# leva alguns segundos para transcrever", "# a pontuação pode precisar de ajuste", "# só computador, não tem app de celular"]),
   "titulo": "Os limites", "sub": "Antes de instalar, saiba o que ele não faz.",
   "bullets": ["Não escreve em tempo real enquanto você fala", "Revise vírgulas e nomes próprios", "Pede permissão de microfone e acessibilidade", "Projeto aberto, sem suporte pago"], "link": "Grátis, mas é ferramenta, não serviço"},
  {"tipo": "cta", "palavra": "VOZ", "promessa": "A MINHA MENTORIA",
   "itens": ["Como eu uso IA no meu negócio", "O passo a passo da mentoria", "Acesso direto comigo", "Para quem é e como começar"]},
]}

LEGENDA = """Você ainda digita proposta, orçamento e resposta de cliente com dois dedos no celular?

O Handy é um programa gratuito e de código aberto (licença MIT) que transforma a sua voz em texto no computador. Você aperta um atalho, fala e o texto aparece onde o cursor está: e-mail, WhatsApp Web, documento. Funciona sem internet, com os modelos Whisper e Parakeet, em Windows, macOS e Linux. O áudio não sai da sua máquina.

Os limites: leva alguns segundos para transcrever, a pontuação pede revisão e não tem versão para celular. Informações conferidas hoje, 05/11.

🔻 Comente VOZ que eu te mando no direct como funciona a minha mentoria, onde eu mostro como uso IA no meu negócio. Siga @liurialves.

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
