"""Extra de 05/11/2026 pedido pelo dono no chat: carrossel no molde de "escada de valores" (referência: print de um
carrossel do @homemricooficial que o dono mandou), com valores em euros, fotos novas do Pexels e texto próprio.
Formato novo: scripts/render_faixa.py. Ângulo A (dinheiro). CTA comentário, palavra EUROS (link da mentoria).
Publicado na hora (pedido explícito do dono: "já postando").
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/3ad2a2f4-1f39-5a28-8d68-94cb43b73f16/scratchpad"
R = "/home/claude/carrosseis"
P = lambda x: f"/tmp/pxe/pexels-{x}.jpg"

cfg = {"slides": [
  {"tipo": "foto", "foto": P(34862454), "foco_y": 0.35, "grande": True, "arraste": True,
   "faixa": "COM 1.000 € GUARDADOS,", "texto": "VOCÊ PARA DE VIVER NO LIMITE DO CARTÃO..."},
  {"tipo": "foto", "foto": P(6940880), "foco_y": 0.5,
   "faixa": "COM 5.000 € NA CONTA,", "texto": "UMA DESPESA SURPRESA DEIXA DE TIRAR O SEU SONO..."},
  {"tipo": "foto", "foto": P(9301906), "foco_y": 0.05,
   "faixa": "COM 10.000 € DE RESERVA,", "texto": "PERDER O EMPREGO OU UM CLIENTE GRANDE DEIXA DE SER O FIM DO MUNDO..."},
  {"tipo": "foto", "foto": P(40161922), "foco_y": 0.45,
   "faixa": "COM 25.000 € INVESTIDOS,", "texto": "A VIAGEM COM A FAMÍLIA SAI SEM PARCELAR NADA..."},
  {"tipo": "foto", "foto": P(7654184), "foco_y": 0.4,
   "faixa": "COM 100.000 € INVESTIDOS,", "texto": "OS JUROS JÁ PAGAM ALGUMAS CONTAS DO MÊS POR VOCÊ..."},
  {"tipo": "foto", "foto": P(6919708), "foco_y": 0.45,
   "faixa": "O ERRO MAIS CARO", "texto": "É GASTAR NO CONFORTO DE HOJE O DINHEIRO QUE IA COMPRAR A SUA TRANQUILIDADE.",
   "destaque": "QUEM PAGA ESSA CONTA É VOCÊ DAQUI A DEZ ANOS."},
  {"tipo": "foto", "foto": P(3975992), "foco_y": 0.3,
   "faixa": "CADA COMPRA POR IMPULSO", "texto": "ATRASA O SEU PRIMEIRO DEGRAU. QUEM QUER SAIR DO APERTO PRECISA APRENDER A",
   "destaque": "DIZER NÃO A ALGUNS DESEJOS DE AGORA."},
  {"tipo": "branco", "blocos": [
   ["t", "TODO MUNDO QUER CHEGAR AOS 100 MIL EUROS."], ["esp", 16],
   ["h", "SÓ QUE TUDO COMEÇA NOS PRIMEIROS 1.000 €"],
   ["n", "E EM SABER PARA ONDE VAI O SEU DINHEIRO TODO MÊS."], ["esp", 20],
   ["h", "O PROBLEMA QUASE NUNCA É QUANTO VOCÊ GANHA"],
   ["n", "É O QUE ACONTECE DEPOIS QUE O DINHEIRO CAI NA CONTA."], ["esp", 24],
   ["h", "COMENTE \"EUROS\""],
   ["n", "E EU TE MANDO NO DIRECT COMO FUNCIONA A MINHA MENTORIA."]]},
]}

LEGENDA = """Ninguém chega aos 100 mil euros de uma vez. Primeiro você para de sentir o aperto no peito no fim do mês.

Com 1.000 € guardados, o cartão deixa de ser a sua reserva. Com 5.000 €, uma despesa surpresa não tira mais o sono. Com 10.000 €, perder um cliente grande ou o emprego deixa de ser o fim do mundo. E com 100.000 € investidos, os juros já pagam algumas contas por você.

Cada degrau começa no mesmo lugar: saber para onde vai o seu dinheiro todo mês e dizer não a alguns desejos de agora.

Em qual degrau você está hoje?

🔻 Comente EUROS que eu te mando no direct como funciona a minha mentoria.

#dinheiro #financas #brasileirosemportugal #empreendedorismo #reservadeemergencia"""

if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    p = f"{S}/cfg-2026-11-05-euros.json"; json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    subprocess.run(["python3", f"{R}/scripts/render_faixa.py", p, f"{R}/posts/2026-11-05/liurialves-6"], check=True)
    print("ok")
