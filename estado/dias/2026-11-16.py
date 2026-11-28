"""Plano 100 mil, semana 4 do PDF (janela de testes, dia 3), 16/11/2026, segunda-feira. Dia 10 do "Plano de 30 dias para
lançar a mentoria": conteúdo "As 3 perguntas antes de publicar qualquer conteúdo" (valor das 17:40) e tarefa "Lançar o
Desafio 6 semanas (post + Stories + link)" (material pronto no doc).
AJUSTE DO DONO EM 10/11 (prevalece sobre a tarefa agendada em quantidade, horários e formato): 5 posts, sem post de IA.
Segunda: 12:40 CONEXÃO · 14:20 CONEXÃO · 17:40 VALOR com rosto (dia par = capa A) · 20:30 PROVA · 22:15 BANDEIRA.
AJUSTE DE 11/11: "indicação" em 0 de 5 posts hoje (ontem também 0).
Sem prints novos no Drive. Print ainda NÃO usado: whatsapp-chamada-cliente.png (prova-social, 08/11) -> slide da prova.
CTA (rodízio, todos terminam em "Comente CLIENTES"): 12:40 salvar · 14:20 envio · 17:40 comentário · 20:30 envio · 22:15 comentário.
1) 12:40 FAIXA, conexão, pilar 6 (lição pilar 4): "A minha esposa e os meus filhos estão há 3 meses no Brasil. Agora eu vou
   buscá-los." Itens 11, 12, 13, 14 e 21. REMODELADO de liurialves:6af5405e8a1a2f52b522312d (quarto dos três, 675 views):
   mesma cena de família com número; trecho novo (família no Brasil, item 21), capa nova (Drive 64), lição nova (reserva).
2) 14:20 FAIXA, conexão, pilar 5 (lição pilar 2): "Entreguei a carta e disse: não vou mais trabalhar para ninguém." Itens
   15, 19 e 20. REMODELADO de liurialves:6af2d90e1586e43ae33e6ac4 ("Tudo o que eu quero, eu conquisto", 602 views): frase
   dita em voz alta na capa → o que veio depois → lição.
3) 17:40 FAIXA, valor, pilar 1: as 3 perguntas antes de publicar. Molde: plano 30 dias, dia 10 + My PT Hub (13/04/2026).
4) 20:30 CAPA + ESCURO, prova, pilar 5 (lição pilar 1): Lisboa Massagem com mais de 90 terapeutas (número nunca usado como
   gancho) + print da chamada de WhatsApp (não usado). 252 € → 1.755 € ficou de fora: foi gancho do Reel de 13/11.
5) 22:15 FAIXA, bandeira, pilar 6 (lição pilar 3): "Eu não acredito em desconto para encher a agenda." Item 16 (Punto) +
   cliente de cerca de 300 €/mês. Molde Two-Brain ("The Discount Death Spiral", 20/10/2025) + PushPress (06/03/2024).
"""
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps
S = "/tmp/claude-0/-home-claude-carrosseis/d98bb076-8483-5c41-8cfe-e62d9469467b/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-16"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h16/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px16/pexels-{x}.jpg"

# 1) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = SALVAR + CLIENTES
familia = {"slides": [
  {"tipo": "foto", "foto": HP("64"), "foco_y": 0.15, "grande": True, "arraste": True, "faixa": "A MINHA FAMÍLIA",
   "texto": "A MINHA ESPOSA E OS MEUS FILHOS ESTÃO HÁ 3 MESES NO BRASIL. AGORA EU VOU BUSCÁ-LOS."},
  {"tipo": "foto", "foto": HP("58"), "foco_y": 0.2, "faixa": "COMO COMEÇOU",
   "texto": "UM ANO DE NAMORO, UM ANO DE NOIVADO. CASAMOS UM ANO DEPOIS DA MINHA FORMATURA.",
   "destaque": "UM ANO DEPOIS, NASCEU O PRIMEIRO FILHO."},
  {"tipo": "foto", "foto": HP("04"), "foco_y": 0.2, "faixa": "PAI DE FARDA",
   "texto": "FORAM 4 ANOS NA AERONÁUTICA.",
   "destaque": "QUANDO EU SAÍ, JÁ TINHA A IDEIA DE MORAR FORA."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.55, "faixa": "PORTUGAL",
   "texto": "EU VIM PRIMEIRO, SOZINHO, COM 300 €. A MINHA ESPOSA AJUDOU A JUNTAR O DINHEIRO.",
   "destaque": "ELA E O NOSSO FILHO CHEGARAM 3 MESES DEPOIS."},
  {"tipo": "foto", "foto": P("35110643"), "foco_y": 0.5, "faixa": "O PRIMEIRO ANO",
   "texto": "MORÁVAMOS OS TRÊS NUM QUARTO. ELA ESTAVA GRÁVIDA DO SEGUNDO.",
   "destaque": "FOI O ANO MAIS DIFÍCIL DA NOSSA VIDA."},
  {"tipo": "foto", "foto": HP("77"), "foco_y": 0.3, "faixa": "DEPOIS",
   "texto": "JUNTAMOS DINHEIRO E MUDAMOS PARA UMA CASA."},
  {"tipo": "foto", "foto": FL("video-rotina-17s"), "foco_y": 0.35, "faixa": "HOJE",
   "texto": "EU NÃO OLHO O PREÇO NO SUPERMERCADO E TENHO RESERVA DE EMERGÊNCIA.",
   "destaque": "ELES ESTÃO DE FÉRIAS NO BRASIL HÁ 3 MESES. EU VOU BUSCÁ-LOS."},
  {"tipo": "branco", "blocos": [
   ["h", "QUANTOS MESES A SUA EMPRESA AGUENTA SE VOCÊ PARAR?"], ["esp", 8],
   ["n", "Quem está parado no mesmo faturamento quase nunca tira férias. Se ele para, a entrada para junto e não há dinheiro guardado para cobrir o mês."],
   ["n", "Faça hoje: some os custos fixos de um mês (aluguel, sistemas, contas e o seu salário) e divida o que você tem guardado por esse número. Exemplo ilustrativo de um estúdio de personal com 2.400 € de custos fixos e 1.200 € guardados: meio mês. A partir de amanhã, 10% de cada pagamento vai para uma conta separada, até chegar a 3 meses."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.2, "faixa": "SALVE E FAÇA A CONTA HOJE",
   "texto": "E COMENTE CLIENTES COM O SEU NÚMERO DE MESES. EU TE CHAMO NO DIRECT E A GENTE VÊ COMO ENCHER ESSA RESERVA.",
   "destaque": "QUANTOS MESES VOCÊ AGUENTA?"},
]}

# 2) 14:20 FAIXA, CONEXÃO (REMODELADO), CTA = ENVIO + CLIENTES
carta = {"slides": [
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.15, "grande": True, "arraste": True,
   "faixa": "O DIA EM QUE EU DECIDI",
   "texto": "ENTREGUEI A CARTA E DISSE: NÃO VOU MAIS TRABALHAR PARA NINGUÉM."},
  {"tipo": "foto", "foto": P("18483758"), "foco_y": 0.5, "faixa": "ANTES DISSO",
   "texto": "NO MEU PRIMEIRO RESTAURANTE EM LISBOA, EM 6 MESES EU VIREI SUBGERENTE.",
   "destaque": "UM CONFLITO COM UM GERENTE E ME COLOCARAM PARA FORA."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.35, "faixa": "O SEGUNDO RESTAURANTE",
   "texto": "DEPOIS FUI GERENTE NUM RESTAURANTE CONHECIDO. FIQUEI 3 MESES.",
   "destaque": "ENTREGUEI A CARTA E SAÍ."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.3, "faixa": "A FRASE",
   "texto": "\"NÃO VOU MAIS TRABALHAR PARA NINGUÉM.\"",
   "destaque": "FALAR FOI FÁCIL. O QUE VEIO DEPOIS, NÃO."},
  {"tipo": "foto", "foto": P("4839255"), "foco_y": 0.5, "faixa": "O QUE VEIO DEPOIS",
   "texto": "2 ANOS DE UBER EM PORTUGAL, COM O CARRO DANDO PROBLEMA.",
   "destaque": "EU TINHA SAÍDO DO EMPREGO. O DINHEIRO AINDA DEPENDIA DE EU ESTAR AO VOLANTE."},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.35, "faixa": "2026",
   "texto": "VOLTEI PARA A MASSAGEM E COMECEI A CRIAR SITES PARA CLIENTES.",
   "destaque": "A MINHA VIDA MUDOU ESTE ANO, COM A MINHA ATITUDE."},
  {"tipo": "branco", "blocos": [
   ["h", "SAIR DO EMPREGO NÃO TE FAZ DONO DE NEGÓCIO."], ["esp", 8],
   ["n", "Se você para uma semana e não entra nada, você tem um emprego com o seu nome na porta. É assim que fica quem trabalha que nem um condenado e vê o dinheiro não sobrar."],
   ["n", "Faça hoje: liste tudo o que você fez na última semana e marque só o que precisa de você (treinar, atender, cortar). Do resto, escolha 1 tarefa e transforme numa mensagem pronta. Exemplo ilustrativo de um personal: a resposta ao \"quanto custa?\" escrita uma vez e salva nas respostas rápidas do WhatsApp Business."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.2, "faixa": "ENVIE PARA QUEM SAIU DO EMPREGO PARA SER LIVRE",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE ESCOLHE A PRIMEIRA TAREFA QUE SAI DAS SUAS MÃOS.",
   "destaque": "VOCÊ É DONO OU EMPREGADO DO SEU NEGÓCIO?"},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO (capa A), CTA = COMENTÁRIO + CLIENTES
perguntas = {"slides": [
  {"tipo": "foto", "foto": HP("69"), "foco_y": 0.62, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "ANTES DE POSTAR, FAÇA 3 PERGUNTAS. SE UMA FICAR SEM RESPOSTA, O POST NÃO SAI."},
  {"tipo": "foto", "foto": P("3850266"), "foco_y": 0.5, "faixa": "O QUE EU ACREDITO",
   "texto": "FOTO DO SERVIÇO FEITO É ÁLBUM DE RECORDAÇÃO. QUEM AINDA NÃO TE CONHECE PASSA RETO.",
   "destaque": "ELE PARA QUANDO O POST FALA DO PROBLEMA DELE."},
  {"tipo": "branco", "blocos": [
   ["t", "PERGUNTA 1"], ["h", "PARA QUEM, EXATAMENTE?"], ["esp", 8],
   ["n", "Uma pessoa, com idade e situação. \"Quem quer emagrecer\" é todo mundo, e todo mundo passa reto."],
   ["n", "Exemplo ilustrativo de fisioterapia: \"corredor de 40 anos que sente o joelho depois dos 5 km\"."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PERGUNTA 2"], ["h", "QUE DÚVIDA DELE ESTE POST RESPONDE?"], ["esp", 8],
   ["n", "Use a dúvida que já chega no seu WhatsApp, com as palavras dele e não com as suas."],
   ["n", "No exemplo: \"Posso continuar correndo com dor no joelho?\" vira a primeira frase do post."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PERGUNTA 3"], ["h", "O QUE ELE FAZ QUANDO TERMINAR DE LER?"], ["esp", 8],
   ["n", "Uma ação só, escrita no fim, com uma palavra para ele mandar. Post sem pedido pode ganhar curtida e mesmo assim não abre conversa."],
   ["n", "No exemplo: \"Mande JOELHO no direct e eu te digo se dá para correr esta semana.\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "EXEMPLO ILUSTRATIVO: UM PERSONAL"], ["esp", 6],
   ["h", "ANTES"], ["n", "\"Mais um treino concluído com a aluna.\""], ["esp", 6],
   ["h", "DEPOIS"],
   ["n", "\"Tem mais de 35 anos, começou a treinar 3 vezes e parou em 2 semanas? Quase sempre o erro é começar com 5 treinos por semana. Comigo você começa com 2. Mande VOLTA no direct que eu te mostro a sua primeira semana.\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "FAÇA EM 30 MINUTOS"], ["esp", 8],
   ["h", "PASSE OS SEUS ÚLTIMOS 6 POSTS PELAS 3 PERGUNTAS"],
   ["n", "Numa folha, escreva a resposta de cada pergunta para cada post."],
   ["n", "Se menos de 2 passarem nas três, a frequência não é o seu problema. Reescreva a legenda do próximo post com as 3 respostas antes de publicar."]]},
  {"tipo": "foto", "foto": FL("video-rotina-1s"), "foco_y": 0.4, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTOS DOS SEUS 6 POSTS PASSARAM NAS 3 PERGUNTAS. EU TE CHAMO NO DIRECT E A GENTE OLHA O PRÓXIMO JUNTOS.",
   "destaque": "QUAL FOI O SEU NÚMERO?"},
]}

# 4) 20:30 CAPA + ESCURO, PROVA, CTA = ENVIO + CLIENTES
prova = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": FL("video-rotina-13s"), "foco_y": 0.3, "etiqueta": "Prova",
   "titulo": "Construí a Lisboa Massagem do zero. Hoje são mais de 90 terapeutas.",
   "sub": "Para quem ainda pergunta o que um massagista entende de negócio."},
  {"etiqueta": "O que é", "frase": "[[Mais de 90]] terapeutas numa plataforma só.",
   "texto": "A Lisboa Massagem é uma das duas plataformas que eu construí do zero. A outra é a MedPortugal, de profissionais de saúde: osteopatia, fisioterapia, nutrição e personal trainer."},
  {"etiqueta": "x", "frase": "x", "texto": "x"},  # substituído pelo slide do print
  {"etiqueta": "Por que eu mostro", "frase": "Antes de ensinar, [[eu fiz]].",
   "texto": "Eu fiz dez anos de massagem. Também construí as plataformas, os anúncios e o atendimento. É desse lado que eu falo com quem tem negócio."},
  {"etiqueta": "O que eu vejo", "frase": "O cliente chama e [[espera pouco]].",
   "texto": "O guia de anúncios da Two-Brain para donos de academia (27/05/2026) manda responder ao contato novo em até 5 minutos. Depois disso ele já está falando com outro."},
  {"etiqueta": "No seu negócio", "frase": "Personal, fisio e barbearia perdem cliente [[no tempo de resposta]].",
   "texto": "Exemplo ilustrativo: o aluno manda mensagem às 19h, você responde às 23h, e ele já marcou a avaliação noutro lugar."},
  {"etiqueta": "Faça hoje", "frase": "Ative [[2 mensagens automáticas]] no WhatsApp Business.",
   "texto": "Saudação: \"Oi! Me diga o seu objetivo e o melhor horário que eu te respondo em seguida.\" Ausência: \"Estou em atendimento. Respondo até às 20h. Se quiser, já me diga o dia que prefere.\" Depois anote quanto tempo levou para responder às próximas 10 mensagens."},
  {"etiqueta": "Para quem é", "frase": "Para quem fatura entre [[1.500 € e 5.000 €]] e responde cliente no intervalo.",
   "texto": "Personal trainer, academia, fisioterapia ou barbearia que atende o dia todo e só abre o WhatsApp à noite."},
  {"etiqueta": "Próximo passo", "frase": "Envie para quem [[responde no dia seguinte]].",
   "texto": "E comente CLIENTES. Eu te chamo no direct e a gente monta as suas mensagens de atendimento."},
]}

# 5) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = COMENTÁRIO + CLIENTES
desconto = {"slides": [
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.15, "grande": True, "arraste": True,
   "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM DESCONTO PARA ENCHER A AGENDA."},
  {"tipo": "foto", "foto": P("19199869"), "foco_y": 0.4, "faixa": "NOVEMBRO",
   "texto": "É O MÊS EM QUE TODO MUNDO BAIXA O PREÇO. A BLACK FRIDAY É DIA 27.",
   "destaque": "ANTES DE ENTRAR NESSA, OLHE O QUE ACONTECEU COMIGO."},
  {"tipo": "foto", "foto": HP("75"), "foco_y": 0.3, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "O MEU PRIMEIRO CARRO EM PORTUGAL FOI UM PUNTO DE 1996, POR 450 €. DUROU 2 MESES.",
   "destaque": "O BARATO SAIU CARO."},
  {"tipo": "foto", "foto": FL("cafe-pastel-pao-de-queijo"), "foco_y": 0.5, "faixa": "DO OUTRO LADO",
   "texto": "NA MASSAGEM, UM CLIENTE MEU PAGA CERCA DE 300 € POR MÊS, DE 2 A 3 VEZES POR SEMANA.",
   "destaque": "ELE NÃO ME ESCOLHEU PELO PREÇO."},
  {"tipo": "foto", "foto": P("29224210"), "foco_y": 0.5, "faixa": "EXEMPLO: A ACADEMIA",
   "texto": "UMA DONA DE BOX NOS EUA DAVA DESCONTO A TODO MUNDO. ATRAIU QUEM SÓ QUERIA PREÇO E PERDEU OS ALUNOS FIÉIS.",
   "destaque": "ELA SUBIU O PREÇO E NINGUÉM RECLAMOU. (PUSHPRESS, 2024)"},
  {"tipo": "foto", "foto": P("18483780"), "foco_y": 0.5, "faixa": "EXEMPLO: A BARBEARIA",
   "texto": "CORTE PELA METADE DO PREÇO NA TERÇA. O CLIENTE APRENDE A SÓ APARECER NA TERÇA."},
  {"tipo": "branco", "blocos": [
   ["t", "PARA A BLACK FRIDAY, NO LUGAR DO DESCONTO:"], ["esp", 10],
   ["h", "1. UM BÔNUS QUE CUSTA POUCO PARA VOCÊ"],
   ["n", "Personal: uma avaliação física extra. Fisio: plano de exercícios para casa. Barbearia: barba incluída no 1º mês do plano."],
   ["h", "2. PRAZO E QUANTIDADE DE VERDADE"],
   ["n", "Só para quem fechar o plano até 30/11. 10 vagas."],
   ["h", "3. AVISE 20 CLIENTES ANTIGOS ANTES DO POST"],
   ["n", "Mensagem individual no WhatsApp. Quem já confia em você fecha primeiro."]]},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E O BÔNUS QUE VOCÊ VAI OFERECER NO LUGAR DO DESCONTO. EU TE CHAMO NO DIRECT E A GENTE MONTA A SUA OFERTA DE NOVEMBRO.",
   "destaque": "DESCONTO OU BÔNUS?"},
]}

LEGENDAS = {
 1: """A minha esposa e os meus filhos estão há 3 meses no Brasil. Agora eu vou buscá-los.

Um ano de namoro, um ano de noivado, e casamos um ano depois da minha formatura na Aeronáutica. Um ano depois nasceu o primeiro filho. Saí da farda já com a ideia de morar fora. Vim primeiro, sozinho, com 300 €, e ela chegou 3 meses depois com o nosso filho. Morávamos os três num quarto, com ela grávida do segundo. Foi o ano mais difícil da nossa vida. Juntamos dinheiro e mudamos para uma casa. Hoje eu não olho o preço no supermercado e tenho reserva de emergência. Graças a Deus.

Quantos meses a sua empresa aguenta se você parar? Some os custos fixos de um mês (aluguel, sistemas, contas e o seu salário) e divida o que você tem guardado por esse número. Exemplo ilustrativo de um estúdio de personal com 2.400 € de custos e 1.200 € guardados: meio mês. A partir de amanhã, 10% de cada pagamento vai para uma conta separada, até chegar a 3 meses.

🔻 Salve e faça a conta hoje. Depois comente CLIENTES com o seu número de meses que eu te chamo no direct e a gente vê como encher essa reserva.

#empreendedorismo #familia #brasileirosemportugal #donodenegocio #historiareal""",
 2: """Entreguei a carta e disse: não vou mais trabalhar para ninguém.

No meu primeiro restaurante em Lisboa, em 6 meses eu virei subgerente. Um conflito com um gerente e me colocaram para fora. Depois fui gerente num restaurante conhecido. Fiquei 3 meses, entreguei a carta e saí. Falar foi fácil. Depois vieram 2 anos de Uber, com o carro dando problema: eu tinha saído do emprego, mas o dinheiro ainda dependia de eu estar ao volante. Em 2026 voltei para a massagem e comecei a criar sites para clientes. A minha vida mudou este ano, com a minha atitude.

Sair do emprego não te faz dono de negócio. Se você para uma semana e não entra nada, você tem um emprego com o seu nome na porta. Faça hoje: liste tudo o que fez na última semana e marque só o que precisa de você. Do resto, escolha 1 tarefa e transforme numa mensagem pronta. Exemplo ilustrativo de um personal: a resposta ao "quanto custa?" escrita uma vez e salva nas respostas rápidas do WhatsApp Business.

🔻 Envie para quem saiu do emprego para ser livre. E comente CLIENTES que eu te chamo no direct e a gente escolhe a primeira tarefa que sai das suas mãos.

#empreendedorismo #donodenegocio #brasileirosemportugal #personaltrainer #historiareal""",
 3: """Antes de postar, faça 3 perguntas. Se uma ficar sem resposta, o post não sai.

Foto do serviço feito é álbum de recordação. Quem ainda não te conhece passa reto. Ele para quando o post fala do problema dele.

1. Para quem, exatamente? Uma pessoa, com idade e situação. Exemplo ilustrativo de fisioterapia: "corredor de 40 anos que sente o joelho depois dos 5 km".
2. Que dúvida dele este post responde? A que já chega no seu WhatsApp, com as palavras dele: "Posso continuar correndo com dor no joelho?"
3. O que ele faz quando terminar de ler? Uma ação só: "Mande JOELHO no direct e eu te digo se dá para correr esta semana."

Faça em 30 minutos: passe os seus últimos 6 posts pelas 3 perguntas. Se menos de 2 passarem nas três, a frequência não é o seu problema.

Esta semana eu abro as inscrições do Desafio 6 semanas, que começa a 25/11. Quem comentar recebe os detalhes no direct.

🔻 Comente CLIENTES e quantos dos seus 6 posts passaram. Eu te chamo no direct e a gente olha o próximo juntos.

#marketingparapersonal #instagramparanegocios #fisioterapia #academia #donodenegocio""",
 4: """Construí a Lisboa Massagem do zero. Hoje são mais de 90 terapeutas.

É uma das duas plataformas que eu construí do zero. A outra é a MedPortugal, de profissionais de saúde: osteopatia, fisioterapia, nutrição e personal trainer. Eu fiz dez anos de massagem e também construí as plataformas, os anúncios e o atendimento. O print é real: uma chamada de cliente no meu WhatsApp (nome desfocado).

O cliente chama e espera pouco. O guia de anúncios da Two-Brain para donos de academia (27/05/2026) manda responder ao contato novo em até 5 minutos. Faça hoje: ative 2 mensagens automáticas no WhatsApp Business.
Saudação: "Oi! Me diga o seu objetivo e o melhor horário que eu te respondo em seguida."
Ausência: "Estou em atendimento. Respondo até às 20h. Se quiser, já me diga o dia que prefere."
Depois anote quanto tempo levou para responder às próximas 10 mensagens.

🔻 Envie para quem responde cliente no dia seguinte. E comente CLIENTES que eu te chamo no direct e a gente monta as suas mensagens de atendimento.

#whatsappbusiness #atendimento #personaltrainer #fisioterapia #donodenegocio""",
 5: """Eu não acredito em desconto para encher a agenda.

Novembro é o mês em que todo mundo baixa o preço, e a Black Friday é dia 27. O meu primeiro carro em Portugal foi um Punto de 1996, por 450 €. Durou 2 meses. O barato saiu caro. Do outro lado, na massagem, um cliente meu paga cerca de 300 € por mês, de 2 a 3 vezes por semana. Ele não me escolheu pelo preço.

Uma dona de box nos EUA dava desconto a todo mundo, atraiu quem só queria preço e perdeu os alunos fiéis. Subiu o preço e ninguém reclamou (PushPress, 06/03/2024). Chris Cooper, da Two-Brain, chama isso de espiral do desconto (podcast Run a Profitable Gym, 20/10/2025).

No lugar do desconto:
1. Um bônus que custa pouco para você. Personal: avaliação física extra. Fisio: plano de exercícios para casa. Barbearia: barba incluída no 1º mês do plano.
2. Prazo e quantidade de verdade: até 30/11, 10 vagas.
3. Avise 20 clientes antigos por mensagem individual antes de postar.

🔻 Comente CLIENTES e o bônus que você vai oferecer. Eu te chamo no direct e a gente monta a sua oferta de novembro.

#blackfriday #precificacao #barbearia #academia #donodenegocio""",
}


def inter(t, peso="Bold"):
    f = ImageFont.truetype(f"{R}/assets/fonts/Inter.ttf", t)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f


def slide_print(dst, i, n):
    """Fatia escura com o print real da chamada de WhatsApp (nome do cliente já desfocado no original)."""
    src = Image.open("/tmp/ps16/whatsapp.png").convert("RGB")
    c = src.crop((0, 0, src.width, 420))
    c2 = src.crop((0, 1220, src.width, 1660))
    w = 760
    c = c.resize((w, int(c.height * w / c.width))); c2 = c2.resize((w, int(c2.height * w / c2.width)))
    comp = Image.new("RGB", (w, c.height + c2.height), (30, 40, 90)); comp.paste(c, (0, 0)); comp.paste(c2, (0, c.height))
    im = Image.new("RGB", (1080, 1350), (14, 14, 14)); d = ImageDraw.Draw(im)
    d.text((110, 90), "O PRINT", font=inter(30, "Bold"), fill=(217, 84, 30))
    d.text((110, 138), "Bastidor: o telefone toca pelo WhatsApp.", font=inter(40, "Bold"), fill=(242, 239, 234))
    c = ImageOps.contain(comp, (860, 880))
    mask = Image.new("L", c.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, c.width, c.height), 26, fill=255)
    im.paste(c, ((1080 - c.width) // 2, 240), mask)
    d.text((110, 1170), "Uma chamada de cliente no meu WhatsApp.", font=inter(30, "Bold"), fill=(242, 239, 234))
    d.text((110, 1215), "Print real. Nome do cliente desfocado.", font=inter(28, "Regular"), fill=(168, 164, 158))
    d.text((540, 1278), f"@liurialves  •  {i:02d}/{n:02d}", font=inter(26, "Medium"), fill=(120, 120, 120), anchor="ma")
    im.save(dst, quality=92)


def run(cfg, out, script="render_faixa.py"):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/{script}", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    for n in (1, 2, 3, 4, 5):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(familia, O(1)); run(carta, O(2)); run(perguntas, O(3))
    run(prova, O(4), "render_formatos.py"); slide_print(f"{O(4)}/fatia-2.jpg", 3, len(prova["slides"]))
    run(desconto, O(5))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
