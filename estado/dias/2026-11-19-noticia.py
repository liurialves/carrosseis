"""CARROSSEL DE NOTÍCIA (pedido do dono em 19/11/2026, no chat: "Cadê o carrossel de notícia?" → 1 por dia, 10:30).
Notícia: Observador Cetelem, Black Friday 2026 (ecommercenews.pt, Margarida Raposo Alves, 18/11/2026; Grande Consumo, Bárbara
Sousa, 17/11/2026): 1.000 entrevistas online de 3 a 9/11/2026, 18 a 74 anos; gasto médio previsto 272 € (+29% vs 211 € em
2025); 79% planejam comprar; 92% conferem preços; 4% confiam no desconto sem verificar; roupa 63%, beleza 42%, brinquedos 39%.
Formato capa + escuro, etiqueta NOTÍCIA. Valor, pilar 3 (oferta e preço). CTA envio + CLIENTES. toca_indicacao: false.
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/c01c7929-4b7d-5117-8d0a-026a02dbb8f7/scratchpad"
cfg = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": f"{R}/assets/fotos-liuri/mercado-acougue-picanha-precos.jpg", "foco_y": 0.4, "etiqueta": "Notícia",
   "titulo": "Os portugueses vão gastar 272 € na Black Friday. Só 4% confiam no desconto sem conferir.",
   "sub": "Observador Cetelem, 18/11/2026. O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O número", "frase": "[[272 €]] por pessoa, 29% a mais do que em 2025.",
   "texto": "Estudo Observador Cetelem: 1.000 entrevistas online de 3 a 9/11/2026, pessoas de 18 a 74 anos. 79% pretendem comprar."},
  {"etiqueta": "O que quase ninguém leu", "frase": "[[92%]] conferem o preço antes de comprar.",
   "texto": "E só 4% confiam no desconto anunciado sem verificar. O cliente chega a novembro desconfiado."},
  {"etiqueta": "Para onde vai o dinheiro", "frase": "Roupa 63%, [[beleza 42%]], brinquedos 39%.",
   "texto": "Cuidar da aparência já está entre as primeiras compras do ano. O seu serviço disputa esse mesmo dinheiro."},
  {"etiqueta": "O que eu acredito", "frase": "Desconto [[não salva]] negócio parado.",
   "texto": "Quem dá 30% em novembro enche a agenda de quem só volta no próximo desconto. E o preço cheio fica mais difícil de cobrar em janeiro."},
  {"etiqueta": "No seu negócio", "frase": "No lugar do desconto, [[bônus com prazo]].",
   "texto": "Exemplo ilustrativo: personal, quem fechar 3 meses até 30/11 ganha uma avaliação física extra. Fisio, 1 sessão de revisão. Barbearia, a barba incluída no pacote do mês. O preço fica igual."},
  {"etiqueta": "Faça hoje", "frase": "[[1 story e 10 mensagens]] até domingo.",
   "texto": "Story: o bônus, o prazo e quantas vagas. Mensagem aos 10 clientes mais antigos: \"Até 30/11, quem renovar por 3 meses ganha [bônus]. Quer garantir a sua?\""},
  {"etiqueta": "Próximo passo", "frase": "Envie para quem vai dar 50% e [[comente CLIENTES]].",
   "texto": "Eu te chamo no direct e a gente monta o seu bônus sem mexer no preço."},
]}
LEGENDA = """Os portugueses vão gastar 272 € na Black Friday. Só 4% acreditam no desconto sem conferir.

O estudo é do Observador Cetelem (1.000 entrevistas online de 3 a 9/11/2026, pessoas de 18 a 74 anos), publicado esta semana: gasto médio previsto de 272 €, 29% a mais do que em 2025. 79% pretendem comprar. Mas 92% conferem o preço antes, e só 4% confiam no desconto anunciado sem verificar. Roupa (63%) e beleza (42%) lideram a lista.

O que eu acredito: desconto não salva negócio parado. Quem dá 30% em novembro enche a agenda de quem só volta no próximo desconto, e o preço cheio fica mais difícil de cobrar em janeiro.

No lugar do desconto, bônus com prazo. Exemplo ilustrativo: personal, quem fechar 3 meses até 30/11 ganha uma avaliação física extra. Fisio, 1 sessão de revisão. Barbearia, a barba incluída no pacote do mês. O preço fica igual.

Faça hoje: 1 story com o bônus, o prazo e as vagas. E 10 mensagens aos clientes mais antigos: "Até 30/11, quem renovar por 3 meses ganha [bônus]. Quer garantir a sua?"

🔻 Envie para quem vai dar 50% de desconto. E comente CLIENTES que eu te chamo no direct e a gente monta o seu bônus sem mexer no preço.

Fontes: ecommercenews.pt (18/11/2026) e Grande Consumo (17/11/2026), estudo Observador Cetelem.

#blackfriday #donodenegocio #personaltrainer #barbearia #fisioterapia"""
if __name__ == "__main__":
    out = f"{R}/posts/2026-11-19/liurialves-7"
    os.makedirs(S, exist_ok=True)
    p = f"{S}/cfg-noticia.json"; json.dump(cfg, open(p, "w"), ensure_ascii=False)
    r = subprocess.run(["python3", f"{R}/scripts/render_formatos.py", p, out], capture_output=True, text=True)
    print(r.stdout[-300:], r.stderr[-500:])
    open(f"{S}/legenda-noticia.txt", "w").write(LEGENDA)
