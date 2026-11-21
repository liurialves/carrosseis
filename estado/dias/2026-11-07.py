"""Plano 100 mil, semana 3, dia 1 (07/11/2026, sábado). Dia 1 do "Plano de 30 dias para lançar a mentoria":
pilar 2, vídeo de anúncio do posicionamento; tarefa: trocar a bio e fixar o vídeo no topo.
Mensagem central nova (dono, 06/11): "Ajudo quem já tem um negócio, ou quer começar um, a conquistar clientes e crescer
com previsibilidade, começando de onde está."
Rodízio de CTA (06/11 foi 14:20 salvar, 17:40 envio, 20:30 comentário):
14:20 TWEET, pilar 2 (clientes, conteúdo e vendas), CTA comentário, palavra FRASE (a frase que explica o negócio).
17:40 QUADRO, pilar 1 (dinheiro e gestão), CTA salvar, palavra META (a conta de trás para a frente).
20:30 FOTOFRASE, pilar 3 (vida de quem empreende), CTA envio, palavra CASA. REMODELADO do carrossel "Empreender com
      filho pequeno em casa me obrigou a criar 5 regras" (buffer 6ae8131dc60bdbcc33d536bb, 02/11, 208 de alcance: o
      carrossel com mais alcance dos últimos 30 dias; os Reels acima dele já foram replicados ou são só "Segue
      @liurialves", sem tema legível daqui). Mudou: capa+escuro com lista de 5 regras e CTA salvar virou fotofrase com
      as fotos próprias (fotos-liuri), gancho novo (o horário que muda com filho pequeno), exemplos novos (manhã cedo,
      bloco de calls à tarde, plano que cai quando a criança adoece) e CTA envio.
CTA de todos os posts leva ao link do dono no direct (item 12).
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/04c62b7e-dce5-5dbd-8fa6-2ed5a6c62b3f/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-07"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
P = lambda x: f"/tmp/px7/pexels-{x}.jpg"

# 1) 14:20 TWEET, pilar 2, CTA = COMENTÁRIO (palavra FRASE)
tweet = {"formato": "tweet", "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": f"{R}/assets/avatar-liuri.jpg", "slides": [{"texto": t} for t in [
  "Durante anos, quando me perguntavam o que eu fazia, eu respondia \"marketing\". A pessoa acenava com a cabeça e nunca mais me procurava.",
  "A culpa não era dela. Ela não entendeu o que eu resolvia, então não tinha motivo para lembrar de mim no dia em que precisasse.",
  "Hoje eu digo assim: ajudo quem já tem um negócio, ou quer começar um, a conquistar clientes e crescer com previsibilidade, começando de onde está.",
  "Essa frase responde três perguntas. Para quem eu trabalho. O que muda para essa pessoa. E de onde ela começa, que é do ponto em que está hoje, sem fingir outro.",
  "Faça o teste com o seu negócio. Se a sua frase serve para qualquer concorrente da sua rua, ela ainda não diz por que o cliente deveria escolher você.",
  "Um exemplo de massagem, que é a área onde eu comecei. \"Faço massagem\" é a frase de todo mundo. \"Atendo quem passa o dia sentado e chega em casa com dor nas costas\" já escolhe o cliente.",
  "Com a frase pronta, ela vai para a bio, para a abertura dos vídeos e para a primeira mensagem do WhatsApp. O cliente ouve a mesma coisa em todo lugar e começa a lembrar de você.",
  "A frase sozinha não fecha venda. Ela abre a conversa. Quem fecha é o atendimento, o preço certo e a entrega.",
  "Escreva a sua frase aqui nos comentários que eu leio e respondo. Se quiser ajustar isso comigo, comente FRASE que eu te mando no direct como funciona a minha mentoria.",
]]}

# 2) 17:40 QUADRO, pilar 1, CTA = SALVAR (palavra META)
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "A conta de trás para a frente que eu faço para saber [[quantos clientes a empresa precisa no mês]]",
   "desenho": {"tipo": "funil", "camadas": ["meta do mês", "vendas", "conversas", "contatos"], "lado": "por dia"},
   "texto": "Previsibilidade começa com um número decidido antes de o mês começar."},
  {"etiqueta": "Por que de trás para a frente", "titulo": "Quase todo dono começa o mês postando e esperando",
   "desenho": {"tipo": "numero", "n": 4, "nota": "contas, uma folha de papel"},
   "texto": "Eu começo pelo valor que a empresa precisa faturar e desço até o que eu preciso fazer por dia. São quatro contas e cabem numa folha.",
   "soco": "Meta sem conta vira torcida."},
  {"etiqueta": "Conta 1 de 4", "titulo": "A meta do mês, em euros", "desenho": {"tipo": "numero", "n": 1, "nota": "custos + pró-labore + reserva"},
   "texto": "Use o valor que paga os custos fixos, o seu pró-labore e a reserva. Para mostrar a conta, vou usar um exemplo de 4.000 €. Você usa o seu número.",
   "soco": "A meta sai das contas da empresa."},
  {"etiqueta": "Conta 2 de 4", "titulo": "Quantas vendas isso exige", "desenho": {"tipo": "numero", "n": 2, "nota": "meta ÷ valor médio da venda"},
   "texto": "Divida a meta pelo valor médio de cada venda. Com 80 € por venda, os 4.000 € pedem 50 vendas no mês, umas 12 por semana.",
   "soco": "Agora a meta tem cara de agenda."},
  {"etiqueta": "Conta 3 de 4", "titulo": "Quantas conversas você precisa abrir", "desenho": {"tipo": "numero", "n": 3, "nota": "vendas ÷ taxa de fechamento"},
   "texto": "Pegue as últimas 20 conversas do WhatsApp e conte quantas viraram venda. Se metade fecha, as 50 vendas pedem 100 conversas no mês.",
   "soco": "Se você não sabe a sua taxa, comece a anotar hoje."},
  {"etiqueta": "Conta 4 de 4", "titulo": "Quantas pessoas precisam chegar até você", "desenho": {"tipo": "numero", "n": 4, "nota": "contatos por dia"},
   "texto": "Nem todo contato vira conversa. Se metade responde, são 200 contatos no mês, perto de 7 por dia. Entra cliente antigo, indicação, direct e quem chega pelo conteúdo.",
   "soco": "Sete por dia é uma meta que você consegue cobrar de si mesmo."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3", "4"], "nota": "ir direto para o post"},
   "texto": "O dono pula a conta e vai direto para o conteúdo. Posta todos os dias sem saber quantas conversas precisa abrir e, no dia 25, descobre que faltou metade das vendas.",
   "soco": "Primeiro a conta, depois o post."},
  {"etiqueta": "Na prática", "titulo": "O exemplo inteiro numa folha",
   "desenho": {"tipo": "lista", "check": True, "itens": ["1: meta de 4.000 €", "2: 50 vendas", "3: 100 conversas", "4: 200 contatos", "5: 7 contatos por dia"]},
   "texto": "Refaça a conta todo dia 1 com os seus números reais. Em três meses, a taxa de fechamento deixa de ser palpite."},
  {"etiqueta": "Próximo passo", "titulo": "Salve este post e faça a sua conta ainda hoje",
   "desenho": {"tipo": "numero", "n": 1, "nota": "folha, todo dia 1"},
   "texto": "Salve para refazer no começo de cada mês. Se quiser montar essa conta comigo, comente META que eu te mando no direct como funciona a minha mentoria.",
   "soco": "O mês começa na conta."},
]}

# 3) 20:30 FOTOFRASE, pilar 3, CTA = ENVIO (palavra CASA). REMODELADO.
foto = {"formato": "fotofrase", "slides": [
  {"foto": FL("video-rotina-9s"), "foco_y": 0.35, "texto": "Trabalhar depois que a casa dorme parecia a solução. **Com filho pequeno, eu precisei mudar o horário da empresa.**"},
  {"foto": FL("video-rotina-1s"), "foco_y": 0.3, "texto": "Hoje o meu dia começa cedo, na cozinha, antes da correria. **As tarefas que movem a empresa saem nessa primeira hora.**"},
  {"foto": P(5725561), "foco_y": 0.3, "texto": "Com criança em casa, o tempo vem em blocos curtos e com interrupção. **Planejar o dia como se fossem oito horas seguidas só gera frustração.**"},
  {"foto": FL("video-rotina-13s"), "foco_y": 0.3, "texto": "Por isso eu junto as calls num bloco só, à tarde. Fora dele, faço o que não depende de hora marcada: conteúdo, números, proposta. **O cliente sabe quando me encontra, e a família também.**"},
  {"foto": FL("video-rotina-4s"), "foco_y": 0.55, "texto": "O treino de MMA continua na agenda. **É ali que eu descarrego a semana para voltar para casa inteiro.**"},
  {"foto": FL("cafe-pastel-pao-de-queijo"), "foco_y": 0.5, "texto": "Em Lisboa, a nossa rede de apoio é pequena. **Por isso a semana é combinada entre mim e a minha esposa antes de começar.**"},
  {"foto": P(8432432), "foco_y": 0.35, "texto": "Vai ter dia em que a criança adoece e o plano cai. **Empresa que só funciona no dia perfeito não aguenta a vida de quem tem família.**"},
  {"foto": FL("video-rotina-17s"), "foco_y": 0.3, "texto": "O que eu ensino aos meus clientes eu aprendi assim. **Rotina boa é a que continua de pé na semana em que tudo atrasa.**"},
  {"foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "texto": "Envie este post para quem está construindo uma empresa com filho pequeno em casa. **Se quiser organizar a sua semana comigo, comente CASA que eu te mando no direct como funciona a minha mentoria.**"},
]}

LEGENDAS = {
 1: """Se a sua frase sobre o que você faz serve para qualquer concorrente da sua rua, o cliente não tem motivo para lembrar de você.

Durante anos eu respondi "marketing" quando me perguntavam o que eu fazia. Hoje eu digo: ajudo quem já tem um negócio, ou quer começar um, a conquistar clientes e crescer com previsibilidade, começando de onde está.

A frase responde para quem você trabalha, o que muda para essa pessoa e de onde ela começa. Depois ela vai para a bio, para a abertura dos vídeos e para a primeira mensagem do WhatsApp.

🔻 Escreva a sua frase nos comentários que eu leio e respondo. Se quiser ajustar isso comigo, comente FRASE que eu te mando no direct como funciona a minha mentoria.

#empreendedorismo #marketingdigital #vendas #negocioproprio #empresario""",
 2: """Quantos clientes a sua empresa precisa no mês? Se a resposta é "o máximo possível", o mês ainda não tem plano.

Eu faço a conta de trás para a frente: a meta em euros, dividida pelo valor médio da venda, dá o número de vendas. As vendas divididas pela taxa de fechamento dão as conversas. E as conversas mostram quantos contatos precisam chegar por dia.

No exemplo do post, 4.000 € com venda média de 80 € viram 50 vendas, 100 conversas e perto de 7 contatos por dia. Use os seus números.

🔻 Salve para refazer no começo de cada mês. Se quiser montar essa conta comigo, comente META que eu te mando no direct como funciona a minha mentoria.

#gestao #empresario #empreendedorismo #negocioproprio #vendas""",
 3: """Empreender com filho pequeno em casa mudou o horário da minha empresa.

Trabalhar depois que a casa dorme parecia a solução. Hoje o dia começa cedo, as calls ficam num bloco só à tarde, o treino de MMA continua na agenda e a semana é combinada com a minha esposa antes de começar. E, quando a criança adoece e o plano cai, a empresa precisa aguentar.

Rotina boa é a que continua de pé na semana em que tudo atrasa.

🔻 Envie este post para quem está construindo uma empresa com filho pequeno em casa. Se quiser organizar a sua semana comigo, comente CASA que eu te mando no direct como funciona a minha mentoria.

#empreendedorismo #vidadeempreendedor #brasileirosemportugal #negocioproprio #paiempreendedor""",
}


def run(cfg, out, script="render_formatos.py"):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/{script}", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    run(tweet, O(1)); run(quadro, O(2)); run(foto, O(3)); print("ok")
