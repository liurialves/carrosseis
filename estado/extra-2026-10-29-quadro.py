"""Extra pedido pelo dono em 28/10 à noite: mais posts como o quadro do funil (26/10). Agendado para 29/10 20:30."""
import json, subprocess, sys
R = "/home/claude/carrosseis"
OUT = f"{R}/posts/2026-10-29/liurialves-extra"
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "A cliente passa por [[5 portas]] antes de marcar com você. Em cada uma ela pode ir embora.",
   "desenho": {"tipo": "funil", "camadas": ["pesquisa", "perfil", "WhatsApp", "preço", "marcação"], "lado": "agenda"},
   "texto": "O caminho que eu desenho para todo negócio local antes de mexer em anúncio."},
  {"etiqueta": "Porta 1 de 5", "titulo": "Pesquisa", "desenho": {"tipo": "numero", "n": 1, "nota": "ela precisa te achar"},
   "texto": "A cliente digita o serviço e o bairro no Google ou no Instagram. Se o seu nome não aparece no mapa nem na busca, as outras portas nem chegam a existir para ela.",
   "soco": "Quem não aparece não entra na disputa."},
  {"etiqueta": "Porta 2 de 5", "titulo": "Perfil", "desenho": {"tipo": "numero", "n": 2, "nota": "segundos para entender"},
   "texto": "Bio com serviço e zona, fotos reais do trabalho e destaques de preço, local e como marcar. A cliente decide nos primeiros segundos se está no lugar certo.",
   "soco": "O perfil simples que explica ganha do perfil bonito que confunde."},
  {"etiqueta": "Porta 3 de 5", "titulo": "WhatsApp", "desenho": {"tipo": "numero", "n": 3, "nota": "a conversa começa aqui"},
   "texto": "O link da bio abre o WhatsApp com a mensagem já escrita, e a resposta chega rápido, inclusive fora do horário, com a mensagem de ausência configurada.",
   "soco": "Resposta no dia seguinte costuma virar marcação no concorrente."},
  {"etiqueta": "Porta 4 de 5", "titulo": "Preço", "desenho": {"tipo": "numero", "n": 4, "nota": "a pergunta que espanta"},
   "texto": "Quando a cliente pergunta \"quanto custa?\", responda o valor, o que está incluído e um horário livre na mesma mensagem. O número sozinho faz a pessoa comparar com o mais barato.",
   "soco": "Preço sem explicação vira comparação."},
  {"etiqueta": "Porta 5 de 5", "titulo": "Marcação", "desenho": {"tipo": "numero", "n": 5, "nota": "e a próxima visita"},
   "texto": "Confirme o dia por escrito, mande lembrete na véspera e, no fim do atendimento, já sugira a próxima data. É nessa porta que a cliente nova passa a ser fixa.",
   "soco": "A segunda venda custa menos do que a primeira."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "nota": "anúncio com as portas quebradas"},
   "texto": "Muita gente liga anúncio para levar mais gente à porta 1 enquanto as portas 2, 3 e 4 continuam quebradas. O dinheiro traz visita, e a agenda continua igual.",
   "soco": "Conserte as portas antes de pagar para trazer mais gente."},
  {"etiqueta": "Na prática", "titulo": "Faça o caminho hoje", "desenho": {"tipo": "lista", "check": True, "itens": ["1: pesquise o seu serviço", "2: abra o seu perfil", "3: mande uma mensagem", "4: pergunte o preço", "5: tente marcar"]},
   "texto": "Faça o caminho no celular, como se fosse cliente, e anote em que porta você mesmo desistiria."},
  {"etiqueta": "Próximo passo", "titulo": "Salve e teste as suas portas", "desenho": {"tipo": "circulos", "rotulos": ["Google", "perfil", "WhatsApp"], "centro": "AGENDA"},
   "texto": "Se quiser que eu faça esse caminho no seu negócio e mostre em que porta a cliente está desistindo, clique no link da bio e me chame no WhatsApp com a palavra DIAGNÓSTICO.",
   "soco": "Salve este post e faça o teste ainda hoje."},
]}
if __name__ == "__main__":
    p = "/tmp/claude-0/-home-claude-carrosseis/77fd91f6-615b-5095-80b8-625e04866922/scratchpad/cfg-extra.json"
    json.dump(quadro, open(p, "w"), ensure_ascii=False)
    r = subprocess.run(["python3", f"{R}/scripts/render_formatos.py", p, OUT], capture_output=True, text=True)
    print(r.stdout[-300:], r.stderr[-800:])
