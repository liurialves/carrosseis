"""Plano 100 mil, semana 2, dia 1 (31/10/2026). 3 carrosséis do @liurialves, 3 CTAs diferentes."""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/d9659ce6-2f34-51c2-9de7-e579d3399dad/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-10-31"
F = lambda x: f"/tmp/fotos/{x}.jpg"
PX = lambda x: f"/tmp/px2/pexels-{x}.jpg"

# 1) 14:20 TWEET, ângulo dinheiro e gestão, CTA = ENVIO
tweet = {"formato": "tweet", "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": f"{R}/assets/avatar-liuri.jpg", "slides": [{"texto": t} for t in [
  "Hoje é dia 31. Se você só vai descobrir no extrato de amanhã se o mês deu lucro, a sua empresa está sendo pilotada no escuro.",
  "Na Aeronáutica eu aprendi a fazer relatório de tudo. Hoje é o mesmo relatório que eu peço a todo dono de negócio antes de falar de anúncio: quatro números, no último dia do mês.",
  "Leva uns 20 minutos. Uma folha de papel, o extrato do banco e nenhuma planilha complicada.",
  "Número 1: quanto entrou de verdade na conta neste mês, contando só o dinheiro que já caiu.",
  "Número 2: quanto saiu. Aluguel, produto, taxas, impostos, anúncio e o seu próprio salário, que muita gente esquece de colocar na conta.",
  "Número 3: quanto sobrou. Se esse número está negativo há dois meses seguidos, mais cliente pelo mesmo preço não resolve.",
  "Número 4: quanto ainda vai entrar. Cliente marcado, pagamento parcelado, proposta enviada. É ele que diz se novembro começa tranquilo ou apertado.",
  "Com os quatro números na mão, a decisão de segunda-feira deixa de ser no susto: ajustar o preço, cortar um gasto ou investir em anúncio.",
  "Envie este post para o seu sócio, ou para quem divide as contas com você, e façam esses 20 minutos ainda hoje.\n\nSiga @liurialves para mais rotinas de quem toca uma pequena empresa.",
]]}

# 2) 17:40 QUADRO, ângulo cliente e conteúdo, CTA = SALVAR
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "As [[3 perguntas]] que eu respondo antes de criar um único post",
   "desenho": {"tipo": "lista", "itens": ["1: quem compra", "2: o que pergunta", "3: por que desiste"]},
   "texto": "Serve para qualquer negócio que quer vender pelo Instagram, do restaurante ao consultório."},
  {"etiqueta": "Por que isso importa", "titulo": "Post sem essas respostas vira enfeite no feed", "desenho": {"tipo": "numero", "n": "?", "nota": "antes do primeiro post"},
   "texto": "A maioria dos perfis de pequenas empresas posta o que o dono acha bonito. O cliente rola o feed e não encontra um motivo para chamar no WhatsApp.",
   "soco": "Conteúdo que vende começa numa conversa com o cliente."},
  {"etiqueta": "Pergunta 1 de 3", "titulo": "Quem compra de verdade", "desenho": {"tipo": "numero", "n": 1, "nota": "uma pessoa, não um público"},
   "texto": "Pegue os últimos 10 clientes que pagaram. Idade, bairro, profissão e o que estava acontecendo na vida deles quando decidiram comprar.",
   "soco": "Você escreve para essa pessoa, e só para ela."},
  {"etiqueta": "Pergunta 2 de 3", "titulo": "O que ele pergunta antes de comprar", "desenho": {"tipo": "numero", "n": 2, "nota": "está no seu WhatsApp"},
   "texto": "Abra as conversas do último mês e copie as perguntas que se repetem: preço, prazo, onde fica, se dói, se funciona para o caso dele.",
   "soco": "Cada pergunta repetida é um post pronto."},
  {"etiqueta": "Pergunta 3 de 3", "titulo": "Por que ele desiste", "desenho": {"tipo": "numero", "n": 3, "nota": "o post que ninguém faz"},
   "texto": "Liste os motivos de quem pediu orçamento e sumiu: achou caro, não confiou, não entendeu o serviço ou deixou para depois.",
   "soco": "O post certo responde a objeção antes de ela virar silêncio."},
  {"etiqueta": "Na prática", "titulo": "Uma semana de conteúdo", "desenho": {"tipo": "lista", "check": True, "itens": ["seg: a dor de quem compra", "ter: a pergunta frequente", "qua: o bastidor do serviço", "qui: a objeção respondida", "sex: um caso real"]},
   "texto": "Com as três respostas na mão, a semana de posts sai em uma tarde."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3"], "nota": "postar antes de perguntar"},
   "texto": "O dono contrata design, compra curso de Reels e começa a postar todo dia sem ter perguntado a um cliente o que ele precisa ouvir.",
   "soco": "Frequência sem direção só cansa você."},
  {"etiqueta": "Exemplo", "titulo": "Uma oficina mecânica", "desenho": {"tipo": "lista", "itens": ["quem: mãe, carro de 10 anos", "dúvida: quanto custa", "medo: ser enganada", "post: a peça antes e depois"]},
   "texto": "Um vídeo curto mostrando a peça gasta ao lado da nova responde à dúvida e ao medo de uma vez só."},
  {"etiqueta": "Próximo passo", "titulo": "Salve e responda hoje", "desenho": {"tipo": "circulos", "rotulos": ["quem", "dúvida", "medo"], "centro": "POST"},
   "texto": "Salve este post e responda as três perguntas do seu negócio hoje à noite. Se quiser montar isso comigo, mande CALL no direct.",
   "soco": "Salvou? Faça antes de segunda-feira."},
]}

# 3) 20:30 FOTOFRASE, ângulo vida de quem empreende, CTA = COMENTÁRIO (fogo)
foto = {"formato": "fotofrase", "slides": [
  {"foto": F("1oEqMXCqpCRBcLK4Hem2bBPL0A4GVUJKG"), "foco_y": 0.3, "texto": "Sábado. Treino de manhã, filho à tarde, números da empresa à noite. **Ninguém posta essa parte de empreender.**"},
  {"foto": F("12mJMPCcewLStqOPxj3aKVoU2EyEpYoZH"), "texto": "Eu saí da Aeronáutica porque queria **construir algo que fosse meu.** Não sabia que a conta vinha junto."},
  {"foto": F("1RL41ouAX1SU8FSA2fm90RaYmNZJ3GsuC"), "texto": "Empresa própria não tem chefe. **Também não tem salário garantido no dia 5.**"},
  {"foto": PX(11740029), "texto": "No tatame eu aprendi a **aguentar o round ruim sem largar a luta.** Na empresa eu uso isso quase todo mês."},
  {"foto": PX(30149857), "texto": "Tem semana em que a agenda está cheia e **o caixa está vazio.** Aprendi a olhar os dois antes de comemorar."},
  {"foto": PX(15065469), "texto": "A minha família não vê o post bonito. **Vê eu saindo cedo e chegando tarde.**"},
  {"foto": PX(13872517), "texto": "Por isso o domingo tem ordem: **treino, família e meia hora com os números da semana.**"},
  {"foto": PX(4398357), "texto": "Empreender é continuar no sábado à noite, **quando ninguém está vendo.**"},
  {"foto": F("1sQpoW-4ihQ9et4DOmxJ1TpPq2MrFKfoi"), "foco_y": 0.3, "texto": "Se você também está construindo algo pela sua família, **deixe o seu fogo nos comentários.**"},
]}


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_formatos.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    run(tweet, O(1)); run(quadro, O(2)); run(foto, O(3)); print("ok")
