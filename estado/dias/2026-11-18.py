"""Plano 100 mil, semana 4 do PDF (janela de testes, dia 5), 18/11/2026, quarta-feira. Dia 12 do "Plano de 30 dias para
lançar a mentoria": conteúdo "Ser pai e empreender ao mesmo tempo" (bandeira das 22:15) e tarefa "Apresentar a mentoria a
quem fez call e tem perfil" (mensagem pronta no doc).
Grade do playbook (ajustes de 10/11 e 16/11, prevalecem sobre a tarefa agendada): 6 posts, sem post de IA.
Quarta: 12:40 CONEXÃO · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 PROVA · 22:15 BANDEIRA.
AJUSTE DE 11/11: "indicação" em 0 de 6 posts, 0 de 4 roteiros, 0 stories.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
REFEITO às 12:40 (pedido do dono): sem frames de vídeo; só fotos reais enviadas por ele.
Print de prova ainda não usado: prova-social/meta-ads-vendas-cbo-0-compras.png (recortado: só nome da campanha e resultados).
CTA (rodízio sobre 17/11, todos terminam em "Comente CLIENTES"):
12:40 comentário · 14:20 salvar · 17:40 envio · 19:10 comentário · 20:30 salvar · 22:15 envio.
1) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): "Fiquei 3 meses em Lisboa sem cortar o cabelo." Item 13 (os 3 primeiros meses).
2) 14:20 FAIXA, conexão, pilar 5 (lição pilar 2): "Não estudei para a prova que me levaria a outro nível. Reprovei e saí."
   Itens 6, 9, 11, 12. REMODELADO de liurialves:6af7e35dbb36d00909e90ece ("autorização até para tirar férias", 375 views,
   ainda não replicado): mesma fase, gancho novo (a prova), fotos novas (turma, aperto de mão, casal no avião), lição nova.
3) 17:40 FAIXA, valor com rosto, pilar 3: a avaliação que não vira cliente, 5 passos. Molde Two-Brain (COACH, 18/08/2026).
4) 19:10 LEGENDA, bandeira falada, pilar 2: "recomendar em vez de perguntar o que o cliente acha".
5) 20:30 CAPA + ESCURO, prova, pilar 5 (lição pilar 1): "Gastei 30,61 € num anúncio de vendas. Vendi zero." + print real.
6) 22:15 FAIXA, bandeira, pilar 6: "Eu não acredito em escolher entre a família e a empresa." Itens 11, 12, 13, 14.
"""
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/5414ef9a-8bb8-5085-8949-33408243ac70/scratchpad"
DIA = "2026-11-18"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h18/{x}.jpg"           # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px18/pexels-{x}.jpg"
F = lambda n: f"{R}/assets/frames-falando/video-2026-10-17-a-{n}.jpg"
FF = lambda n: f"/tmp/fr18/video-2026-10-17-a-{n}.jpg"   # frame com laterais desfocadas (formato faixa)


def gerar_ff():
    os.makedirs("/tmp/fr18", exist_ok=True)
    for f in os.listdir(f"{R}/assets/frames-falando"):
        src = Image.open(f"{R}/assets/frames-falando/{f}").convert("RGB")
        fundo = ImageOps.fit(src, (1080, 1350)).filter(ImageFilter.GaussianBlur(28))
        fr = ImageOps.contain(src, (1080, 1350))
        fundo.paste(fr, ((1080 - fr.width) // 2, 0))
        fundo.save(f"/tmp/fr18/{f}", quality=93)


# 1) 12:40 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
cabelo = {"slides": [
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.45, "grande": True, "arraste": True, "faixa": "OS MEUS PRIMEIROS 3 MESES EM LISBOA",
   "texto": "FIQUEI 3 MESES SEM CORTAR O CABELO. NÃO CABIA NA CONTA."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.55, "faixa": "COMO EU CHEGUEI",
   "texto": "VIM SOZINHO, COM 300 €, PARA UM INTERCÂMBIO VOLUNTÁRIO.",
   "destaque": "TRABALHEI 2 MESES COM MARKETING DIGITAL."},
  {"tipo": "foto", "foto": P("17546504"), "foco_y": 0.5, "faixa": "O QUE EU COMIA",
   "texto": "PIZZA E LASANHA DE SUPERMERCADO."},
  {"tipo": "foto", "foto": P("8603231"), "foco_y": 0.5, "faixa": "O BARBEIRO",
   "texto": "CORTAR O CABELO FICOU PARA DEPOIS.",
   "destaque": "FORAM 3 MESES ASSIM."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.3, "faixa": "OS PRIMEIROS 5 MESES",
   "texto": "12 HORAS POR DIA DE TRABALHO.",
   "destaque": "E EU AINDA VENDIA A MINHA FOLGA."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.3, "faixa": "O QUE EU APRENDI ALI",
   "texto": "COM 300 € NO BOLSO, CADA GASTO PRECISA DE UM MOTIVO.",
   "destaque": "NO SEU NEGÓCIO TAMBÉM."},
  {"tipo": "branco", "blocos": [
   ["h", "QUANTO DO SEU MÊS VAI PARA COISAS QUE NÃO TRAZEM CLIENTE?"], ["esp", 8],
   ["n", "Muito dono de negócio parado corta o anúncio quando o mês aperta e mantém o sistema que ninguém abre."],
   ["n", "Faça hoje: abra o extrato do último mês e marque cada gasto com C (traz ou segura cliente) ou X (não traz). Corte 1 X esta semana. Exemplo ilustrativo de uma barbearia: 45 € por mês num sistema que ninguém usa pagam 9 dias de anúncio a 5 € por dia."]]},
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.35, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTOS X VOCÊ ACHOU NO SEU MÊS. EU TE CHAMO NO DIRECT E A GENTE VÊ PARA ONDE ESSE DINHEIRO VAI.",
   "destaque": "QUANTOS X TEM NO SEU EXTRATO?"},
]}

# 2) 14:20 FAIXA, CONEXÃO (REMODELADO), CTA = SALVAR + CLIENTES
prova_aero = {"slides": [
  {"tipo": "foto", "foto": HP("40"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "OS MEUS 4 ANOS NA AERONÁUTICA",
   "texto": "NÃO ESTUDEI PARA A PROVA QUE ME LEVARIA A OUTRO NÍVEL. REPROVEI E SAÍ."},
  {"tipo": "foto", "foto": HP("59"), "foco_y": 0.55, "faixa": "COMO EU ENTREI",
   "texto": "PASSEI NO TESTE FÍSICO COMO O 13º MELHOR.",
   "destaque": "EU QUERIA ESTAR ENTRE OS MELHORES."},
  {"tipo": "foto", "foto": HP("24"), "foco_y": 0.4, "faixa": "DEPOIS DA FORMATURA",
   "texto": "OS SALÁRIOS MELHORARAM."},
  {"tipo": "foto", "foto": HP("23"), "foco_y": 0.45, "faixa": "A FAMÍLIA",
   "texto": "CASEI UM ANO DEPOIS DA FORMATURA.",
   "destaque": "UM ANO DEPOIS, VEIO O PRIMEIRO FILHO."},
  {"tipo": "foto", "foto": P("9182796"), "foco_y": 0.5, "faixa": "4 ANOS DEPOIS",
   "texto": "EU PEDIA AUTORIZAÇÃO PARA TUDO: FÉRIAS, SAIR DA CIDADE.",
   "destaque": "E JÁ NÃO HAVIA MAIS O QUE APRENDER."},
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.3, "faixa": "A PROVA",
   "texto": "NÃO ESTUDEI PARA A PROVA QUE ME LEVARIA A OUTRO NÍVEL.",
   "destaque": "NÃO PASSEI. SAÍ."},
  {"tipo": "foto", "foto": FL("carro-painel-rua"), "foco_y": 0.45, "faixa": "DEPOIS",
   "texto": "FUI FAZER UBER NO BRASIL PARA FATURAR.",
   "destaque": "JÁ COM A IDEIA DE MORAR FORA."},
  {"tipo": "branco", "blocos": [
   ["h", "QUANDO NÃO HÁ MAIS O QUE APRENDER, VOCÊ PARA DE SE PREPARAR."], ["esp", 8],
   ["n", "Eu vejo isso em negócio parado no mesmo faturamento: o mês se repete porque o dono faz o mesmo mês de novo."],
   ["n", "Faça esta semana: escreva 3 coisas que você não testou nos últimos 90 dias (um preço, uma oferta, um anúncio) e teste uma até domingo. Exemplo ilustrativo de um personal: oferecer o plano de 3 meses aos 5 alunos mais antigos."]]},
  {"tipo": "foto", "foto": HP("33"), "foco_y": 0.25, "faixa": "SALVE A LISTA DOS 3",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE ESCOLHE QUAL TESTAR PRIMEIRO.",
   "destaque": "O QUE VOCÊ NÃO TESTA HÁ 90 DIAS?"},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO, CTA = ENVIO + CLIENTES
avaliacao = {"slides": [
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "A AVALIAÇÃO ACABA E O CLIENTE DIZ: VOU PENSAR. FAÇA ISTO NA PRÓXIMA."},
  {"tipo": "foto", "foto": P("20860597"), "foco_y": 0.35, "faixa": "O QUE EU VEJO",
   "texto": "O PROFISSIONAL ENTREGA UMA TABELA COM 4 PREÇOS E PERGUNTA: O QUE VOCÊ ACHA?",
   "destaque": "QUEM ESCOLHE SOZINHO ESCOLHE ADIAR."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "CONVERSA EM LUGAR CALMO"], ["esp", 8],
   ["n", "Nada de conversar em pé, no meio da academia ou ao lado da cadeira com cliente esperando."],
   ["n", "Duas cadeiras lado a lado, 15 minutos, telefone virado para baixo."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "PERGUNTE DIRETO"], ["esp", 8],
   ["n", "\"O que te trouxe aqui hoje?\""],
   ["n", "Depois: \"O que você já tentou? O que fez você parar?\" e \"O que faz agora ser o momento?\" Evite o \"por quê\": soa como cobrança."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "REPITA O QUE OUVIU"], ["esp", 8],
   ["n", "\"Então você quer voltar a correr sem dor no joelho até março, e já parou duas vezes por falta de rotina. É isso?\""],
   ["n", "Feche com: \"Tem mais alguma coisa que eu precise saber?\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "RECOMENDE UM PLANO SÓ, COM UM NÚMERO SÓ"], ["esp", 8],
   ["n", "Exemplo ilustrativo de um personal: \"Para isso eu recomendo 2 treinos por semana. O investimento é 180 € por mês.\""],
   ["n", "Na fisioterapia: \"8 sessões em 4 semanas. O investimento é 280 €.\" Nada de tabela, nada de faixa de preço."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 5"], ["h", "PEÇA O SIM COM DATA"], ["esp", 8],
   ["n", "Responda antes que ele pergunte: falta, viagem, remarcação. Marque a revisão em 60 a 90 dias."],
   ["n", "E pergunte: \"Começamos segunda às 7h ou quarta às 18h?\""]]},
  {"tipo": "foto", "foto": HP("78"), "foco_y": 0.22, "faixa": "DE ONDE VEM",
   "texto": "É O ROTEIRO DE VENDA QUE A TWO-BRAIN ENSINA A DONOS DE ACADEMIA (18/08/2026).",
   "destaque": "SERVE PARA PERSONAL, ACADEMIA, FISIO E BARBEARIA."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM OUVE 'VOU PENSAR'",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE ESCREVE A SUA RECOMENDAÇÃO COM O SEU PREÇO.",
   "destaque": "QUAL É O SEU PLANO DE UM NÚMERO SÓ?"},
]}

# 4) 19:10 LEGENDA (fala com frames do Liuri), bandeira falada, CTA = COMENTÁRIO + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("selfie-jaqueta-verde"), HP("78")], "foco": [0.3, 0.3], "textos": ["Eu acho que dono de negócio", "devia parar de perguntar \"o que você acha?\""]},
 {"fotos": [FL("home-office-headset"), HP("49")], "foco": [0.3, 0.3], "textos": ["O cliente veio porque não sabe.", "Ele quer que você diga o caminho."]},
 {"fotos": [HP("47"), HP("23")], "foco": [0.3, 0.5], "textos": ["O personal que manda 4 planos", "e espera o aluno escolher."]},
 {"fotos": [FL("selfie-sem-camisa-serio"), FL("dunas-punhos-camisa-preta-2")], "foco": [0.35, 0.3], "textos": ["A fisio que termina a avaliação", "com \"depois você me fala\"."]},
 {"fotos": [FL("lagoa-biceps-de-frente-editada"), HP("70")], "foco": [0.35, 0.3], "textos": ["O barbeiro que nunca diz", "\"volta em 20 dias, já te deixo marcado\"."]},
 {"fotos": [HP("40"), HP("60")], "foco": [0.3, 0.3], "textos": ["Quem não recomenda", "deixa o cliente com a dúvida."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), FL("lagoa-grito-celebrando")], "foco": [0.3, 0.35], "textos": ["Na próxima conversa:", "um plano, um preço, uma data."]},
 {"fotos": [FL("selfie-sem-camisa-serio"), HP("58")], "foco": [0.4, 0.3], "textos": ["Você recomenda ou pergunta?", "Comente CLIENTES."]},
]}

# 5) 20:30 CAPA + ESCURO, PROVA, CTA = SALVAR + CLIENTES
prova = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.3, "etiqueta": "Prova",
   "titulo": "Gastei 30,61 € num anúncio de vendas. Vendi zero.",
   "sub": "O print é real. E mostra o anúncio errado para quem vende serviço."},
  {"etiqueta": "O que é", "frase": "[[6.345 pessoas]] viram. Ninguém comprou.",
   "texto": "Uma campanha de vendas criada em 02/11/2026, com 25 € de orçamento por dia, para levar a compra no site. Resultado no print: 30,61 € gastos e 0 compras."},
  {"etiqueta": "x", "frase": "x", "texto": "x"},  # substituído pelo slide do print
  {"etiqueta": "Por que eu mostro", "frase": "O anúncio que não vendeu [[ensina mais]] do que o que vendeu.",
   "texto": "Eu faço os meus anúncios sozinho. Quem só mostra o resultado bonito esconde a parte em que o dinheiro foi embora."},
  {"etiqueta": "O que eu acredito", "frase": "Quem nunca falou com você [[não compra no primeiro clique]].",
   "texto": "Serviço de confiança se vende numa conversa. O anúncio pedia uma compra no site a quem nem sabia quem eu era."},
  {"etiqueta": "O que funciona para mim", "frase": "Anúncio que [[abre conversa]] no WhatsApp.",
   "texto": "De 15 a 31/10/2026, 252 € em anúncios de mensagem geraram 1.755 € em atendimentos. O anúncio levava a pessoa direto para uma conversa comigo."},
  {"etiqueta": "No seu negócio", "frase": "Personal, fisio e barbearia vendem [[na conversa]].",
   "texto": "Exemplo ilustrativo: o aluno vê o seu vídeo, toca no botão e já cai no seu WhatsApp com a pergunta \"quero saber dos horários para avaliação\"."},
  {"etiqueta": "Faça esta semana", "frase": "[[5 € por dia, 7 dias]], anúncio de mensagem.",
   "texto": "Objetivo de mensagens com destino no WhatsApp, um vídeo seu de 15 s dizendo para quem é o serviço e uma pergunta pronta. No fim, anote quantas conversas entraram e quantas viraram avaliação."},
  {"etiqueta": "Próximo passo", "frase": "Salve e [[comente CLIENTES]].",
   "texto": "Eu te chamo no direct e a gente olha o seu anúncio antes de você gastar o primeiro euro."},
]}

# 6) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = ENVIO + CLIENTES
familia = {"slides": [
  {"tipo": "foto", "foto": HP("58"), "foco_y": 0.25, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM ESCOLHER ENTRE A FAMÍLIA E A EMPRESA."},
  {"tipo": "foto", "foto": HP("04"), "foco_y": 0.2, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "UM ANO DEPOIS DO CASAMENTO, VEIO O PRIMEIRO FILHO.",
   "destaque": "EU AINDA USAVA A FARDA."},
  {"tipo": "foto", "foto": HP("61"), "foco_y": 0.2, "faixa": "O QUE ME FEZ SAIR",
   "texto": "NA AERONÁUTICA EU PEDIA AUTORIZAÇÃO ATÉ PARA SAIR DA CIDADE.",
   "destaque": "EU JÁ NÃO ME SENTIA BEM ALI."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.55, "faixa": "PORTUGAL",
   "texto": "VIM SOZINHO. ELA CHEGOU 3 MESES DEPOIS, COM O NOSSO FILHO E GRÁVIDA DO SEGUNDO."},
  {"tipo": "foto", "foto": P("6943425"), "foco_y": 0.5, "faixa": "O PRIMEIRO ANO",
   "texto": "OS TRÊS NUM QUARTO SÓ. EU COM 12 HORAS POR DIA DE TRABALHO.",
   "destaque": "FOI O ANO MAIS DIFÍCIL DA NOSSA VIDA."},
  {"tipo": "foto", "foto": P("16215287"), "foco_y": 0.5, "faixa": "VOCÊ NÃO ESTÁ SOZINHO",
   "texto": "QUASE 6 EM CADA 10 PEQUENOS NEGÓCIOS NO BRASIL SÃO EMPRESAS FAMILIARES.",
   "destaque": "(SEBRAE, AGÊNCIA SEBRAE DE NOTÍCIAS, 04/08/2026)"},
  {"tipo": "foto", "foto": P("15828942"), "foco_y": 0.5, "faixa": "O QUE EU VEJO HOJE",
   "texto": "O PERSONAL QUE ATENDE DAS 6H ÀS 22H E SÓ VÊ O FILHO DORMINDO.",
   "destaque": "A BARBEARIA ABERTA TODO DIA PORQUE O DONO NÃO SABE QUANTO GANHA POR HORA."},
  {"tipo": "branco", "blocos": [
   ["h", "SE O NEGÓCIO SÓ FATURA COM VOCÊ 12 HORAS LÁ DENTRO, A FAMÍLIA PAGA A CONTA."], ["esp", 8],
   ["n", "Faça hoje: divida o faturamento do mês pelas horas que você trabalhou. Exemplo ilustrativo: 2.500 € ÷ 240 horas = 10,40 € por hora."],
   ["n", "Antes de aumentar as horas, suba esse número: um plano mensal, um preço revisto ou um horário vazio preenchido com anúncio."]]},
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.4, "faixa": "ENVIE PARA QUEM NÃO VÊ O FILHO ACORDADO",
   "texto": "E COMENTE CLIENTES COM O SEU VALOR POR HORA. EU TE CHAMO NO DIRECT E A GENTE VÊ COMO SUBIR ESSE NÚMERO.",
   "destaque": "QUANTO VALE A SUA HORA HOJE?"},
]}

LEGENDAS = {
 1: """Fiquei 3 meses em Lisboa sem cortar o cabelo.

Vim sozinho, com 300 €, para um intercâmbio voluntário onde trabalhei 2 meses com marketing digital. Comia pizza e lasanha de supermercado. Cortar o cabelo ficou para depois, e foram 3 meses assim. Nos primeiros 5 meses eu trabalhava 12 horas por dia e ainda vendia a minha folga.

Com 300 € no bolso, cada gasto precisa de um motivo. No seu negócio também. Muito dono de negócio parado corta o anúncio quando o mês aperta e mantém o sistema que ninguém abre.

Faça hoje: abra o extrato do último mês e marque cada gasto com C (traz ou segura cliente) ou X (não traz). Corte 1 X esta semana. Exemplo ilustrativo de uma barbearia: 45 € por mês num sistema que ninguém usa pagam 9 dias de anúncio a 5 € por dia.

🔻 Comente CLIENTES e quantos X você achou no seu mês. Eu te chamo no direct e a gente vê para onde esse dinheiro vai.

#brasileirosemportugal #empreendedorismo #historiareal #donodenegocio #gestaofinanceira""",
 2: """Não estudei para a prova que me levaria a outro nível. Reprovei e saí da Aeronáutica.

Eu entrei passando no teste físico como o 13º melhor. Depois da formatura os salários melhoraram, casei, e um ano depois veio o primeiro filho. Quatro anos depois eu já não me sentia bem: pedia autorização para tudo, férias, sair da cidade, e já não havia mais o que aprender. Não estudei para a prova, não passei e saí. Fui fazer Uber no Brasil para faturar, já com a ideia de morar fora.

Quando não há mais o que aprender, você para de se preparar. Eu vejo isso em negócio parado no mesmo faturamento: o mês se repete porque o dono faz o mesmo mês de novo.

Faça esta semana: escreva 3 coisas que você não testou nos últimos 90 dias (um preço, uma oferta, um anúncio) e teste uma até domingo. Exemplo ilustrativo de um personal: oferecer o plano de 3 meses aos 5 alunos mais antigos.

🔻 Salve a lista dos 3 e comente CLIENTES. Eu te chamo no direct e a gente escolhe qual testar primeiro.

Foto da formatura: Robério Castro Fotografia.

#aeronautica #historiareal #empreendedorismo #donodenegocio #disciplina""",
 3: """A avaliação acaba e o cliente diz: vou pensar.

O que eu vejo: o profissional entrega uma tabela com 4 preços e pergunta "o que você acha?". Quem escolhe sozinho escolhe adiar.

1. Converse em lugar calmo: duas cadeiras lado a lado, 15 minutos, telefone virado para baixo.
2. Pergunte direto: "O que te trouxe aqui hoje?", "O que você já tentou? O que fez você parar?", "O que faz agora ser o momento?"
3. Repita o que ouviu em 1 frase e feche com "Tem mais alguma coisa que eu precise saber?"
4. Recomende um plano só, com um número só. Exemplo ilustrativo de um personal: "Para isso eu recomendo 2 treinos por semana. O investimento é 180 € por mês." Na fisioterapia: "8 sessões em 4 semanas. O investimento é 280 €."
5. Peça o sim com data. Responda antes que ele pergunte (falta, viagem, remarcação), marque a revisão em 60 a 90 dias e pergunte: "Começamos segunda às 7h ou quarta às 18h?"

É o roteiro de venda que a Two-Brain Business ensina a donos de academia (artigo de John Franklin, 18/08/2026). A ordem serve para personal, academia, fisio e barbearia.

🔻 Envie para quem ouve "vou pensar" toda semana. E comente CLIENTES que eu te chamo no direct e a gente escreve a sua recomendação com o seu preço.

#vendas #personaltrainer #fisioterapia #academia #donodenegocio""",
 4: """Você recomenda ou pergunta?

O cliente veio porque não sabe o caminho. O personal que manda 4 planos e espera o aluno escolher, a fisio que termina a avaliação com "depois você me fala", o barbeiro que nunca diz "volta em 20 dias, já te deixo marcado". Quem não recomenda deixa o cliente com a dúvida.

Na próxima conversa: um plano, um preço, uma data.

🔻 Comente CLIENTES e me diga qual é o plano que você recomendaria hoje. Eu te chamo no direct e a gente ajusta a frase.

#vendas #donodenegocio #personaltrainer #barbearia #fisioterapia""",
 5: """Gastei 30,61 € num anúncio de vendas. Vendi zero.

Era uma campanha de vendas criada em 02/11/2026, com 25 € de orçamento por dia, para levar a compra no site. 6.345 pessoas viram. Ninguém comprou. O print é real.

Eu mostro porque faço os meus anúncios sozinho, e o anúncio que não vendeu ensina mais do que o que vendeu. Quem nunca falou com você não compra no primeiro clique. Serviço de confiança se vende numa conversa.

O que funciona para mim é o anúncio que abre conversa no WhatsApp: de 15 a 31/10/2026, 252 € em anúncios de mensagem geraram 1.755 € em atendimentos.

Faça esta semana, se você é personal, fisio ou barbeiro: 5 € por dia durante 7 dias, objetivo de mensagens com destino no WhatsApp, um vídeo seu de 15 s dizendo para quem é o serviço e uma pergunta pronta. No fim, anote quantas conversas entraram e quantas viraram avaliação.

🔻 Salve e comente CLIENTES. Eu te chamo no direct e a gente olha o seu anúncio antes de você gastar o primeiro euro.

#anuncios #metaads #trafegopago #donodenegocio #personaltrainer""",
 6: """Eu não acredito em escolher entre a família e a empresa.

Um ano depois do casamento veio o primeiro filho, e eu ainda usava a farda. Na Aeronáutica eu pedia autorização até para sair da cidade. Vim para Portugal sozinho; ela chegou 3 meses depois, com o nosso filho e grávida do segundo. Os três num quarto só, eu com 12 horas por dia de trabalho. Foi o ano mais difícil da nossa vida.

Quase 6 em cada 10 pequenos negócios no Brasil são empresas familiares (levantamento do Sebrae citado pela Agência Sebrae de Notícias, 04/08/2026). Mesmo assim eu vejo o personal que atende das 6h às 22h e só vê o filho dormindo, e a barbearia aberta todo dia porque o dono não sabe quanto ganha por hora.

Se o negócio só fatura com você 12 horas lá dentro, a família paga a conta.

Faça hoje: divida o faturamento do mês pelas horas que você trabalhou. Exemplo ilustrativo: 2.500 € ÷ 240 horas = 10,40 € por hora. Antes de aumentar as horas, suba esse número: um plano mensal, um preço revisto ou um horário vazio preenchido com anúncio.

🔻 Envie para quem não vê o filho acordado. E comente CLIENTES com o seu valor por hora que eu te chamo no direct e a gente vê como subir esse número.

#paiempreendedor #familia #empreendedorismo #brasileirosemportugal #donodenegocio""",
}


def inter(t, peso="Bold"):
    f = ImageFont.truetype(f"{R}/assets/fonts/Inter.ttf", t)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f


def slide_print(dst, i, n):
    """Fatia escura com o print real da campanha de vendas (só nome da campanha e resultados; sem barra de estado)."""
    src = Image.open("/tmp/ps18/meta-ads-vendas-cbo-0-compras.png").convert("RGB")
    c = src.crop((0, 120, src.width, 1180))
    im = Image.new("RGB", (1080, 1350), (14, 14, 14)); d = ImageDraw.Draw(im)
    d.text((110, 90), "O PRINT", font=inter(30, "Bold"), fill=(217, 84, 30))
    d.text((110, 138), "30,61 € gastos. 0 compras no site.", font=inter(40, "Bold"), fill=(242, 239, 234))
    c = ImageOps.contain(c, (860, 880))
    mask = Image.new("L", c.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, c.width, c.height), 26, fill=255)
    im.paste(c, ((1080 - c.width) // 2, 230), mask)
    d.text((110, 1170), "Gerenciador de anúncios da Meta, campanha de vendas.", font=inter(30, "Bold"), fill=(242, 239, 234))
    d.text((110, 1215), "Print real, período máximo da campanha.", font=inter(28, "Regular"), fill=(168, 164, 158))
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
    for n in range(1, 7):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(cabelo, O(1)); run(prova_aero, O(2)); run(avaliacao, O(3))
    run(legenda, O(4), "render_legenda.py")
    run(prova, O(5), "render_formatos.py"); slide_print(f"{O(5)}/fatia-2.jpg", 3, len(prova["slides"]))
    run(familia, O(6))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
