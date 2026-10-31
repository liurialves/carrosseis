import json, os, subprocess, sys, re
W = "/tmp/claude-0/-home-claude-carrosseis/67b0f88d-22c2-50ce-b9bb-03a84ffe3ee0/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-10-26"
OUT = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
F = lambda x: f"{W}/fotos/{x}.jpg"
P2 = lambda x: f"{W}/pex2/pexels-{x}.jpg"
HL = lambda t: f"<span class='hl'>{t}</span>"


def run(script, cfg, out):
    p = f"{W}/cfg-{os.path.basename(out)}-{DIA}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    subprocess.run(["python3", f"{R}/scripts/{script}", p, out], check=True, capture_output=True)


# 1. POLÊMICA (alcance) — formato tweet
tweet = {"formato": "tweet", "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": f"{R}/assets/avatar-liuri.jpg",
 "slides": [
  "Se postar todo dia enchesse agenda, toda esteticista do Instagram estaria lotada até dezembro.",
  "Eu conheço profissional que posta há dois anos, todos os dias, e ainda depende da indicação de cliente antiga para fechar a semana.",
  "Frequência ela tem de sobra. O que falta em cada post é um motivo para a cliente sair do feed e abrir o WhatsApp.",
  "O antes e depois bonito ganha curtida de colega de profissão. A cliente que compra quer saber o preço, a zona, o horário e como marca.",
  "Na minha empresa, cada post tem uma função antes de ser publicado: atrair, ensinar, fazer agir, surpreender ou vender. Post sem função não sai.",
  "Eu prefiro três posts por semana com função a sete posts bonitos sem direção. Os três eu consigo medir no WhatsApp na segunda-feira.",
  "Isto vai incomodar quem vende pacote de trinta artes por mês. Tudo bem. Arte bonita nunca marcou horário sozinha.",
  "Antes de postar amanhã, responda uma pergunta: o que a cliente deve fazer depois de ver este post? Se a resposta for nada, guarde o post.",
  "Comente quantos dias por semana você posta hoje e quantas clientes isso trouxe no último mês.\n\nSiga @liurialves: ainda hoje eu mostro o funil que eu uso.",
 ]}

# 2. EDUCATIVO — formato quadro
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "Seu Instagram tem seguidor e não tem cliente porque falta este [[funil]].",
   "desenho": {"tipo": "funil", "camadas": ["atrair", "ensinar", "fazer agir", "surpreender", "vender"], "lado": "WhatsApp"},
   "texto": "Os cinco posts que eu uso para vender serviço local, do primeiro contato ao WhatsApp."},
  {"etiqueta": "Etapa 1 de 5", "titulo": "Atrair", "desenho": {"tipo": "numero", "n": 1, "nota": "quem não te conhece"},
   "texto": "O post de alcance traz uma opinião forte sobre um problema do seu cliente, como \"massagem não precisa doer para funcionar\". Ele não vende nada. Serve para chegar em quem ainda não sabe que você existe.",
   "soco": "Opinião forte divide, e por isso espalha."},
  {"etiqueta": "Etapa 2 de 5", "titulo": "Ensinar", "desenho": {"tipo": "numero", "n": 2, "nota": "a dor e o porquê"},
   "texto": "Aqui você explica por que o problema acontece e dá um passo que a pessoa aplica hoje. Por exemplo: o que fazer depois de um treino pesado para a lombar não travar no dia seguinte.",
   "soco": "Quem aprende com você passa a confiar em você."},
  {"etiqueta": "Etapa 3 de 5", "titulo": "Fazer agir", "desenho": {"tipo": "numero", "n": 3, "nota": "uma ação pequena"},
   "texto": "Um post que pede uma ação concreta e rápida: um teste de dois minutos, uma lista para conferir, uma pergunta para responder nos comentários.",
   "soco": "Quem já fez uma coisa por sua indicação está mais perto da próxima."},
  {"etiqueta": "Etapa 4 de 5", "titulo": "Surpreender", "desenho": {"tipo": "numero", "n": 4, "nota": "o que ninguém mostra"},
   "texto": "Mostre o que o seu mercado não mostra: o bastidor da preparação da sala, o erro que você corrige em quase todo cliente, uma forma nova de responder uma dúvida antiga. É o post que a pessoa salva e envia.",
   "soco": "As pessoas lembram do que foi diferente."},
  {"etiqueta": "Etapa 5 de 5", "titulo": "Vender", "desenho": {"tipo": "numero", "n": 5, "nota": "oferta clara"},
   "texto": "O post de venda diz o que é, para quem é, o que a pessoa recebe e como marca, sem rodeio e sem vergonha de pedir. A palavra do WhatsApp mostra de qual post a cliente veio.",
   "soco": "Quem não pede a venda deixa a cliente decidir sozinha."},
  {"etiqueta": "Na prática", "titulo": "A semana de quem vende", "desenho": {"tipo": "lista", "check": True, "itens": ["seg: atrair", "ter: ensinar", "qua: fazer agir", "qui: surpreender", "sex: vender"]},
   "texto": "Cinco posts, cinco funções. Quem chega pelo post de opinião encontra no seu perfil o resto do caminho até o WhatsApp."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "nota": "pular direto para a venda"},
   "texto": "Eu vejo dois perfis toda semana: o que só posta promoção e o que só posta frase bonita. O primeiro cansa o seguidor antes de ele confiar, e o segundo ganha curtida e nunca recebe mensagem.",
   "soco": "O funil funciona quando as cinco funções aparecem toda semana."},
  {"etiqueta": "Próximo passo", "titulo": "Salve e monte a sua semana", "desenho": {"tipo": "circulos", "rotulos": ["conteúdo", "anúncio", "WhatsApp"], "centro": "FUNIL"},
   "texto": "Se você quer que eu monte esse funil com você, com os temas tirados das perguntas reais dos seus clientes, clique no link da bio e me chame no WhatsApp com a palavra FUNIL.",
   "soco": "Salve este post para usar na segunda-feira."},
]}

# 3. INTENCIONAL — formato branco
branco = {"formato": "branco", "slides": [
  {"etiqueta": "10 MINUTOS", "frase": "Feche o feed agora e faça estes [[3 ajustes]] no seu perfil antes da próxima cliente entrar.",
   "texto": "Cada um leva poucos minutos e muda o que a pessoa faz quando chega no seu perfil."},
  {"etiqueta": "AJUSTE 1", "frase": "A primeira linha da bio diz [[o que você faz e onde]].",
   "texto": "Exemplo: \"Massagem desportiva e drenagem em Alvalade, Lisboa\". Tire a frase sobre propósito e energia. A cliente decide em segundos se está no lugar certo."},
  {"frase": "Se a bio não diz a zona, a cliente de [[outro bairro]] marca com quem diz.",
   "texto": "Ela pesquisa pelo celular, no ônibus ou no intervalo do trabalho, e não vai mandar mensagem só para perguntar onde você fica."},
  {"etiqueta": "AJUSTE 2", "frase": "O link da bio abre o seu WhatsApp com [[uma mensagem já escrita]].",
   "texto": "Use um link wa.me com o texto \"Olá, vi o seu Instagram e quero marcar um horário\". A pessoa só precisa tocar em enviar."},
  {"frase": "Cada passo a mais entre o perfil e a conversa é uma [[cliente que desiste]].",
   "texto": "Site lento, menu com seis links e formulário comprido fazem a pessoa deixar para depois. E depois ela esquece."},
  {"etiqueta": "AJUSTE 3", "frase": "Os três primeiros destaques respondem [[preço, local e como marcar]].",
   "texto": "São perguntas que aparecem todo dia no WhatsApp de quem atende estética e massagem. Responda antes que a cliente precise perguntar."},
  {"frase": "No destaque de preço, um [[valor de partida]] já resolve.",
   "texto": "\"A partir de\" e o valor filtra quem está fora do orçamento e tira o receio de perguntar de quem está dentro."},
  {"frase": "Três ajustes, [[dez minutos]]. Faça agora, antes de fechar este post.",
   "texto": "Depois peça para alguém abrir o seu perfil no celular e dizer em voz alta o que entendeu nos primeiros cinco segundos."},
  {"frase": "Comente [[FEITO]] quando terminar os três ajustes.",
   "texto": "Se quiser que eu confira o seu perfil e o seu link, clique no link da bio e me chame no WhatsApp com a palavra PERFIL."},
]}

# 4. INOVADOR — formato fotofrase
foto = {"formato": "fotofrase", "slides": [
  {"foto": F("v1rHg@2"), "foco_y": 0.3, "texto": "As perguntas que os seus clientes já fizeram no WhatsApp são **os seus próximos 10 posts.**"},
  {"foto": P2(40382716), "texto": "Abra o WhatsApp do seu negócio e **role as conversas do último mês.**"},
  {"foto": P2(6779331), "texto": "Copie cada pergunta numa nota, do jeito que o cliente escreveu: **\"dói?\", \"quanto tempo dura?\", \"vocês vão a casa?\"**"},
  {"foto": P2(7243185), "texto": "Cada pergunta repetida é uma dúvida que **outras pessoas tiveram e não chegaram a mandar.**"},
  {"foto": P2(7446657), "texto": "Transforme cada pergunta num post com **a resposta completa**, na mesma linguagem que o cliente usou."},
  {"foto": P2(9898392), "texto": "Use a frase exata na capa. **\"Massagem desportiva dói?\"** é o que a pessoa digita na busca do Instagram e do Google."},
  {"foto": P2(36930338), "texto": "Depois junte as três respostas mais pedidas e **fixe nos destaques do perfil.**"},
  {"foto": F("v1rHg@16"), "foco_y": 0.3, "texto": "Você para de inventar assunto e **passa a responder quem já quer comprar.**"},
  {"foto": F("1oEqMXCqpCRBcLK4Hem2bBPL0A4GVUJKG"), "foco_y": 0.2, "texto": "Faça a lista hoje e **comente quantas perguntas você encontrou.** Siga @liurialves para o próximo."},
]}

# 5. VENDA — capa + fatias escuras (premium)
venda = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": F("v1rHg@52"), "foco_y": 0.62, "etiqueta": "Oferta",
   "titulo": "Eu monto o [[funil]] do seu negócio.",
   "sub": "Conteúdo, anúncio e WhatsApp para clínicas de estética, estúdios de massagem e salões."},
  {"etiqueta": "Para quem é", "frase": "Para quem atende [[estética, massagem ou beleza]] e quer clientes da própria zona.",
   "texto": "Você já tem serviço definido, tem agenda para preencher e cansou de postar sem saber o que trouxe cliente. A seguir está tudo o que você recebe, na ordem em que eu trabalho."},
  {"etiqueta": "Etapa 1 · Diagnóstico", "frase": "Antes de criar qualquer post, eu leio o seu [[perfil e o seu WhatsApp]].",
   "texto": "Destaques, link da bio, tempo de resposta e as conversas do último mês. É ali que estão as dúvidas que travam a venda. Você sai com a lista do que corrigir primeiro."},
  {"etiqueta": "Etapa 2 · Calendário", "frase": "Um calendário com as [[cinco funções]] de conteúdo.",
   "texto": "Atrair, ensinar, fazer agir, surpreender e vender. Os temas saem das perguntas reais dos seus clientes, e cada post termina com a ação que a pessoa deve fazer."},
  {"etiqueta": "Etapa 3 · Treinamento", "frase": "Você aprende a produzir [[sem depender de agência]].",
   "texto": "Modelos de capa, roteiro de vídeo curto e a resposta rápida do WhatsApp já escrita. O ritmo continua mesmo nas semanas de agenda cheia."},
  {"etiqueta": "Etapa 4 · Anúncio", "frase": "O anúncio entra em cima do post que [[já provou interesse]].",
   "texto": "Comentários, salvamentos e mensagens mostram o que funciona. O tráfego pago leva esse post para quem mora na sua zona, direto para o seu WhatsApp."},
  {"etiqueta": "Etapa 5 · Acompanhamento", "frase": "Toda semana, [[o número decide]] o próximo passo.",
   "texto": "Quantas conversas chegaram, de qual post vieram e quantas viraram marcação. O que não funciona sai do calendário. O que funciona ganha espaço e verba."},
  {"etiqueta": "Para quem não é", "frase": "Isto não é para quem ainda não definiu [[o serviço principal]].",
   "texto": "Nesse caso, começamos organizando a oferta. Eu não prometo número de clientes, porque isso depende do serviço, do preço e da zona. O que você recebe é processo claro e relatório honesto toda semana."},
  {"etiqueta": "Primeiro passo", "frase": "Diagnóstico grátis, feito por mim, numa [[conversa direta]].",
   "texto": "Clique no link da bio e me chame no WhatsApp com a palavra FUNIL."},
]}

if __name__ == "__main__":
    sel = sys.argv[1:] or ["1", "2", "3", "4", "5"]
    if "1" in sel: run("render_formatos.py", dict(tweet, slides=[{"texto": t} for t in tweet["slides"]]), OUT(1))
    if "2" in sel: run("render_formatos.py", quadro, OUT(2))
    if "3" in sel: run("render_formatos.py", branco, OUT(3))
    if "4" in sel: run("render_formatos.py", foto, OUT(4))
    if "5" in sel:
        run("render_formatos.py", venda, OUT(5))
    print("ok")
