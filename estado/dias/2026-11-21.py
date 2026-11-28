"""Plano 100 mil, semana 5 do PDF (leitura e corte, dia 1), 21/11/2026, sábado. Dia 15 do "Plano de 30 dias para lançar
a mentoria": conteúdo "O dia em que pensei em desistir" (vira a CONEXÃO das 12:40, contado com o fato real: "farto" depois de
2 anos de Uber, item 19) e tarefa "Contagem regressiva do desafio nos Stories" (no doc, stories do dia).
Grade do playbook (ajustes de 10/11, 16/11, 18/11 e 19/11 prevalecem sobre a tarefa agendada): 7 posts, sem post de IA.
Sábado: 10:30 NOTÍCIA · 12:40 CONEXÃO · 14:20 CONEXÃO (remodelado) · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 CONEXÃO · 22:15 BANDEIRA.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
Fotos: só do Liuri (sem a ex-esposa; a 78 está na lista negra e ficou fora), nenhum frame de vídeo. Indicação: 0 de 7 posts.
CTA (rodízio sobre 20/11, todos terminam em "Comente CLIENTES"):
10:30 envio · 12:40 salvar · 14:20 comentário · 17:40 comentário · 19:10 salvar · 20:30 salvar · 22:15 envio.
1) 10:30 NOTÍCIA: Instagram libera edição de Stories por 15 minutos (Gazeta Brasil e Portal Publicitário, 18/11/2026; Hardware.com.br, 19/11/2026).
2) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): "Depois de 2 anos de Uber eu fiquei farto. Ali eu decidi." Itens 12, 17, 19 e 20.
3) 14:20 FAIXA, conexão, pilar 5: "O meu primeiro trabalho em Portugal foi voluntário. Com marketing digital." Itens 13, 20 + prova 48.000 €.
   REMODELADO de liurialves:6afe7b3af6b6aa0cd49f7cc4 ("Íamos ao shopping só para usar o Wi-Fi", 272 views, 122 de alcance, não replicado):
   mesmo arco (cena de pouco recurso com detalhe do dia a dia → o que veio dela → lição), outra fase, gancho, fotos, lição e CTA.
4) 17:40 FAIXA, valor com rosto, pilar 3: Black Friday sem desconto, vender a vaga de janeiro (Chris Cooper, Two-Brain Business, 21/10 e 04/11/2025).
5) 19:10 LEGENDA, bandeira falada, pilar 2: dezembro se decide em novembro.
6) 20:30 FAIXA, conexão (apresentação), pilar 5: "Se o seu negócio está parado no mesmo faturamento, segue @liurialves." Molde do Reel
   "Segue @liurialves" (994 views em 19/11, o conteúdo com mais views da semana) levado para carrossel.
7) 22:15 FAIXA, bandeira, pilar 3: "Eu não acredito que o cliente paga pelo seu tempo." Fato: item 15 (subgerente em 6 meses) + cliente de ~300 €/mês.
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/0e4160c9-e59b-57d3-803e-3b2617248b47/scratchpad"
DIA = "2026-11-21"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h21/{x}.jpg"           # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px21/pexels-{x}.jpg"

# 1) 10:30 NOTÍCIA, CAPA + ESCURO, CTA = ENVIO + CLIENTES
noticia = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": P("5053767"), "foco_y": 0.45, "etiqueta": "Notícia",
   "titulo": "O Instagram agora deixa editar o Story depois de publicado. Você tem 15 minutos.",
   "sub": "Gazeta Brasil e Portal Publicitário, 18/11/2026. O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O que mudou", "frase": "Dá para editar o Story [[já publicado]].",
   "texto": "Quem anunciou foi Adam Mosseri, chefe do Instagram, na quarta, 18/11. Texto, música, figurinhas e desenhos. Antes, para corrigir, era preciso apagar e publicar de novo."},
  {"etiqueta": "O que quase ninguém leu", "frase": "Só nos [[primeiros 15 minutos]].",
   "texto": "Depois disso o botão some. A foto ou o vídeo original não podem ser trocados (Hardware.com.br, 19/11). O Story editado ganha a marca de editado."},
  {"etiqueta": "O que fica", "frase": "Visualizações, curtidas e respostas [[continuam]].",
   "texto": "Quem apagava para corrigir perdia o que já tinha entrado. A liberação é gradual: pode ser que ainda não tenha aparecido na sua conta."},
  {"etiqueta": "O que eu acredito", "frase": "O erro mais caro no Story é [[o que ficou faltando]].",
   "texto": "Eu vejo muito Story de negócio sem preço, sem horário e sem um jeito de responder. Agora dá para pôr a figurinha de pergunta ou o link depois. Só se você olhar a tempo."},
  {"etiqueta": "No seu negócio", "frase": "Publique e [[confira em 15 minutos]].",
   "texto": "Exemplo ilustrativo: o personal posta a vaga das 7h e esquece o horário. A fisio posta a avaliação sem o link. A barbearia posta o corte sem dizer como marcar. Os três corrigem sem perder as visualizações."},
  {"etiqueta": "Faça hoje", "frase": "[[3 itens]] antes de fechar o app.",
   "texto": "Depois de cada Story de venda, confira: 1. o que você vende e como saber o preço; 2. figurinha de pergunta, enquete ou link; 3. a palavra que a pessoa manda no direct. Faltou um? Edite dentro dos 15 minutos."},
  {"etiqueta": "Próximo passo", "frase": "Envie para quem posta Story sem pedir nada e [[comente CLIENTES]].",
   "texto": "Eu te chamo no direct e olho os seus 3 últimos Stories com você."},
]}

# 2) 12:40 FAIXA, CONEXÃO (plano 30 dias, dia 15), CTA = SALVAR + CLIENTES
farto = {"slides": [
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "LISBOA, DEPOIS DE 2 ANOS DE UBER",
   "texto": "UM DIA EU FIQUEI FARTO. FOI ALI QUE EU DECIDI MUDAR DE VIDA."},
  {"tipo": "foto", "foto": FL("carro-painel-rua"), "foco_y": 0.5, "faixa": "COMO ERA",
   "texto": "O CARRO DAVA PROBLEMA E EU CONTINUAVA NA RUA.", "destaque": "FORAM 2 ANOS ASSIM, EM PORTUGAL."},
  {"tipo": "foto", "foto": P("29241242"), "foco_y": 0.45, "faixa": "NÃO ERA A PRIMEIRA VEZ",
   "texto": "NO BRASIL, QUANDO SAÍ DA AERONÁUTICA, EU JÁ TINHA FEITO UBER.", "destaque": "JÁ COM A IDEIA DE MORAR FORA."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.55, "faixa": "ANTES DO UBER, EM LISBOA",
   "texto": "RESTAURANTE 12 HORAS POR DIA.", "destaque": "NO FIM DE SEMANA, CLUBE ATÉ AS 8 DA MANHÃ, POR 60 €."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.35, "faixa": "O DIA EM QUE EU FIQUEI FARTO",
   "texto": "EU DECIDI QUE QUERIA GANHAR MAIS.", "destaque": "E MUDAR DE VIDA."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "O QUE EU FIZ COM ISSO",
   "texto": "VOLTEI PARA A MASSAGEM E COMECEI A FAZER SITES PARA CLIENTES.", "destaque": "EM 2026, DE 1.500 € PARA 7.000 € POR MÊS."},
  {"tipo": "branco", "blocos": [
   ["h", "O QUE TE DEIXA FARTO TEM PREÇO."], ["esp", 8],
   ["n", "Muito dono parado no mesmo faturamento reclama do mesmo problema por meses e nunca faz a conta dele."],
   ["n", "Faça hoje: anote 3 coisas que te cansaram esta semana e, ao lado, quanto cada uma custou em horas ou euros. Exemplo ilustrativo de uma barbearia: 4 faltas sem aviso = 4 horas paradas = 100 €. Comece pela mais cara: sinal de 5 € para marcar."]]},
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE ACHA O QUE ESTÁ CUSTANDO MAIS CARO NO SEU NEGÓCIO.",
   "destaque": "O QUE TE DEIXOU FARTO ESTA SEMANA?"},
]}

# 3) 14:20 FAIXA, CONEXÃO (REMODELADO), CTA = COMENTÁRIO + CLIENTES
voluntario = {"slides": [
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.45, "grande": True, "arraste": True, "faixa": "A VIAGEM PARA PORTUGAL",
   "texto": "O MEU PRIMEIRO TRABALHO EM PORTUGAL FOI VOLUNTÁRIO. COM MARKETING DIGITAL."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.15, "faixa": "COMO EU CHEGUEI",
   "texto": "SOZINHO, COM 300 €, PARA UM INTERCÂMBIO.", "destaque": "2 MESES TRABALHANDO COM MARKETING DIGITAL."},
  {"tipo": "foto", "foto": P("8744793"), "foco_y": 0.4, "faixa": "OS 3 PRIMEIROS MESES",
   "texto": "COMIA PIZZA E LASANHA DE SUPERMERCADO.", "destaque": "NÃO DAVA NEM PARA CORTAR O CABELO."},
  {"tipo": "foto", "foto": P("12821628"), "foco_y": 0.4, "faixa": "DEPOIS",
   "texto": "RESTAURANTE, CLUBE À NOITE E 2 ANOS DE UBER.", "destaque": "O MARKETING SÓ VOLTOU ANOS DEPOIS."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "A VIRADA",
   "texto": "COMECEI A CRIAR SITES PARA CLIENTES E A FAZER OS MEUS ANÚNCIOS.", "destaque": "O QUE EU APRENDI SEM RECEBER VIROU O QUE EU COBRO."},
  {"tipo": "foto", "foto": FL("capa-48mil-plataformas"), "foco_y": 0.0, "faixa": "HOJE",
   "texto": "DUAS PLATAFORMAS CONSTRUÍDAS DO ZERO: LISBOA MASSAGEM E MEDPORTUGAL.", "destaque": "48.000 € FATURADOS EM 2026."},
  {"tipo": "branco", "blocos": [
   ["h", "ANTES DE PAGAR ALGUÉM, LIGUE UM ANÚNCIO VOCÊ MESMO."], ["esp", 8],
   ["n", "Quem nunca ligou um anúncio não sabe cobrar resultado de quem liga para ele."],
   ["n", "Faça esta semana (exemplo ilustrativo de uma fisio): 1 anúncio de mensagem, 5 € por dia, 3 dias, para quem mora a 5 km. Anote quantas conversas chegaram e o que as pessoas perguntaram. São 15 € para saber o que o seu público quer."]]},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-1"), "foco_y": 0.2, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTO VOCÊ JÁ GASTOU EM ANÚNCIO ESTE ANO. EU TE CHAMO NO DIRECT E A GENTE MONTA O TESTE DOS 15 €.",
   "destaque": "JÁ LIGOU UM ANÚNCIO SOZINHO?"},
]}

# 4) 17:40 FAIXA, VALOR COM ROSTO, CTA = COMENTÁRIO + CLIENTES
janeiro = {"slides": [
  {"tipo": "foto", "foto": FL("mma-equipe-treino"), "foco_y": 0.35, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "NÃO DÊ 30% DE DESCONTO NA BLACK FRIDAY. VENDA A VAGA DE JANEIRO."},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "faixa": "O QUE EU ACREDITO",
   "texto": "DESCONTO EM SERVIÇO SAI DA SUA MARGEM.", "destaque": "A SUA HORA DE TRABALHO NÃO FICA MAIS BARATA EM NOVEMBRO."},
  {"tipo": "branco", "blocos": [
   ["t", "A CONTA"], ["h", "30% DE DESCONTO NUM PLANO DE 160 €"], ["esp", 8],
   ["n", "Exemplo ilustrativo: são 48 € a menos por aluno, todo mês em que ele ficar nesse preço. Com 10 alunos assim, 480 € por mês. O trabalho é o mesmo."],
   ["n", "E quem entra pelo preço costuma pedir o preço de novo."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "ABRA POUCAS VAGAS PARA JANEIRO"], ["esp", 8],
   ["n", "Janeiro é um dos meses com mais entradas em academia (Wodify, dados de mais de 5.000 negócios de fitness, 2023 e 2024)."],
   ["n", "Escolha um número que você atende bem. Exemplo: 6 vagas no plano de 12 semanas."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "COBRE UM SINAL PARA RESERVAR"], ["esp", 8],
   ["n", "Quem reserva paga agora um valor que desconta da 1ª mensalidade. Exemplo: 30 €."],
   ["n", "A ideia é do Chris Cooper (Two-Brain Business, 04/11/2025): reserva com depósito no lugar de promoção. Quem paga para guardar a vaga aparece em janeiro."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "TROQUE O DESCONTO POR UM BÔNUS"], ["esp", 8],
   ["n", "Algo que custa pouco para você e vale para o cliente: avaliação extra no mês 2, treino para as férias de fim de ano, um desafio de hábitos de 14 dias por mensagem. Na barbearia: a barba de cortesia na 1ª visita de janeiro."],
   ["n", "Regra do Cooper: nunca dê de graça o que outro cliente paga."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "MANDE ESTA MENSAGEM HOJE"], ["esp", 8],
   ["n", "\"Oi, [nome]. Estou abrindo 6 vagas para começar em janeiro. Quem reservar até 30/11 garante a vaga com 30 € (desconta da 1ª mensalidade) e ganha [bônus]. Quer que eu guarde uma para você?\""],
   ["n", "Envie para ex-alunos e para quem pediu preço este ano."]]},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTAS VAGAS VOCÊ ABRE PARA JANEIRO. EU TE CHAMO NO DIRECT E A GENTE ESCREVE O SEU BÔNUS.",
   "destaque": "QUANTAS VAGAS PARA JANEIRO?"},
]}

# 5) 19:10 LEGENDA (fotos reais do Liuri), bandeira falada, CTA = SALVAR + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("selfie-jaqueta-verde"), HP("70")], "foco": [0.3, 0.3], "textos": ["Eu acho que o dezembro do seu negócio", "se decide agora, em novembro."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), FL("carro-painel-rua")], "foco": [0.2, 0.5], "textos": ["Quem espera janeiro para vender", "começa janeiro com a agenda vazia."]},
 {"fotos": [FL("lagoa-biceps-de-frente-editada"), HP("60")], "foco": [0.35, 0.35], "textos": ["O personal que só avisa em janeiro", "vê o aluno começar com outro."]},
 {"fotos": [HP("73"), FL("selfie-sem-camisa-serio")], "foco": [0.35, 0.3], "textos": ["A fisio que não chama o paciente antigo agora", "fica com dezembro aberto."]},
 {"fotos": [FL("home-office-headset"), HP("66")], "foco": [0.3, 0.5], "textos": ["A barbearia que não abre a agenda do Natal hoje", "atende no improviso no dia 23."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-3"), FL("cafe-pastel-pao-de-queijo")], "foco": [0.2, 0.45], "textos": ["Dezembro tem feriado e festa.", "O cliente marca antes."]},
 {"fotos": [FL("mma-equipe-treino"), FL("selfie-jaqueta-verde")], "foco": [0.35, 0.3], "textos": ["Hoje, mande mensagem a 10 clientes antigos", "com uma data de janeiro."]},
 {"fotos": [HP("70"), FL("dunas-punhos-camisa-preta-2")], "foco": [0.3, 0.2], "textos": ["Salve e comente CLIENTES.", "Eu te chamo no direct."]},
]}

# 6) 20:30 FAIXA, CONEXÃO (apresentação), CTA = SALVAR + CLIENTES
apresentacao = {"slides": [
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "QUEM ESTÁ FALANDO COM VOCÊ",
   "texto": "SE O SEU NEGÓCIO ESTÁ PARADO NO MESMO FATURAMENTO, SEGUE @LIURIALVES."},
  {"tipo": "foto", "foto": HP("13"), "foco_y": 0.3, "faixa": "DE ONDE EU VIM",
   "texto": "4 ANOS NA AERONÁUTICA.", "destaque": "SAÍ PORQUE PRECISAVA PEDIR AUTORIZAÇÃO PARA TUDO."},
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.3, "faixa": "O QUE EU JÁ QUEBREI",
   "texto": "UMA LOJA DE MODA PRAIA, NO TEMPO DE MILITAR.", "destaque": "A CONTA DA LOJA ERA A MESMA DA CASA."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.15, "faixa": "PORTUGAL",
   "texto": "CHEGUEI SOZINHO, COM 300 €.", "destaque": "RESTAURANTE, CLUBE À NOITE E UBER."},
  {"tipo": "foto", "foto": FL("cafe-pastel-pao-de-queijo"), "foco_y": 0.45, "faixa": "O QUE MUDOU EM 2026",
   "texto": "SAÍ DE 1.500 € PARA 5.500 € POR MÊS EM 5 MESES.", "destaque": "FAZENDO SOZINHO O CONTEÚDO, OS ANÚNCIOS E O ATENDIMENTO."},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente"), "foco_y": 0.3, "faixa": "O QUE VOCÊ VAI VER AQUI",
   "texto": "CLIENTE TODO MÊS, OFERTA, PREÇO E A CONTA QUE SOBRA NO FIM DO MÊS.", "destaque": "COM EXEMPLO DE PERSONAL, ACADEMIA, FISIO E BARBEARIA."},
  {"tipo": "branco", "blocos": [
   ["h", "COMECE PELO NÚMERO QUE VOCÊ NÃO SABE."], ["esp", 8],
   ["n", "Quase todo dono parado que eu vejo sabe quanto fatura e não sabe quanto custa trazer um cliente novo."],
   ["n", "Faça hoje: some o que gastou em anúncio, impulsionamento e brinde nos últimos 3 meses e divida pelos clientes novos. Exemplo ilustrativo: 300 € ÷ 6 clientes = 50 € por cliente. Agora você sabe quanto pode pagar por um."]]},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "E O SEU TIPO DE NEGÓCIO. EU TE CHAMO NO DIRECT E A GENTE FAZ ESSA CONTA JUNTOS.",
   "destaque": "QUANTO CUSTA UM CLIENTE NOVO PARA VOCÊ?"},
]}

# 7) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = ENVIO + CLIENTES
tempo = {"slides": [
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.25, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO QUE O CLIENTE PAGA PELO SEU TEMPO."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.35, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "NUM RESTAURANTE EM LISBOA, EU VIREI SUBGERENTE EM 6 MESES.", "destaque": "QUEM RESOLVE PROBLEMA SOBE."},
  {"tipo": "foto", "foto": P("30428668"), "foco_y": 0.4, "faixa": "O QUE EU VEJO",
   "texto": "O PERSONAL QUE VENDE \"AULA DE 45 MINUTOS\".", "destaque": "O ALUNO QUERIA TREINAR SEM DOR NAS COSTAS."},
  {"tipo": "foto", "foto": P("14797757"), "foco_y": 0.4, "faixa": "E TAMBÉM",
   "texto": "A FISIO QUE VENDE \"SESSÃO DE 50 MINUTOS\".", "destaque": "O PACIENTE QUERIA VOLTAR A CORRER."},
  {"tipo": "foto", "foto": P("9992820"), "foco_y": 0.35, "faixa": "E AINDA",
   "texto": "A BARBEARIA QUE COBRA PELO TEMPO NA CADEIRA.", "destaque": "O CLIENTE QUERIA CHEGAR BEM NA ENTREVISTA DE SEGUNDA."},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.35, "faixa": "O QUE EU VIVO",
   "texto": "NA MASSAGEM, TENHO CLIENTE QUE PAGA CERCA DE 300 € POR MÊS, 2 A 3 VEZES POR SEMANA.", "destaque": "ELE NÃO COMPRA PELO PREÇO."},
  {"tipo": "branco", "blocos": [
   ["h", "PONHA NO NOME DO SERVIÇO O QUE O CLIENTE QUER."], ["esp", 8],
   ["n", "Faça esta semana: reescreva o nome do serviço que você mais vende, com o resultado e o prazo."],
   ["n", "Exemplos ilustrativos: \"8 semanas para treinar sem dor nas costas\" (personal). \"Plano de 6 sessões para voltar a correr\" (fisio). \"Corte e barba com horário fixo a cada 15 dias\" (barbearia)."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.3, "faixa": "ENVIE PARA QUEM AINDA VENDE HORA",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE DÁ UM NOVO NOME AO SEU SERVIÇO.",
   "destaque": "COMO SE CHAMA O SEU SERVIÇO HOJE?"},
]}

LEGENDAS = {
 1: """O Instagram agora deixa editar o Story depois de publicado. Você tem 15 minutos.

Quem anunciou foi Adam Mosseri, chefe do Instagram, na quarta, 18/11. Dá para mexer no texto, na música, nas figurinhas e nos desenhos. Antes, para corrigir um erro, era preciso apagar e publicar de novo, e as visualizações iam junto.

O detalhe que quase ninguém leu: só vale nos primeiros 15 minutos. Depois o botão some, e a foto ou o vídeo original não podem ser trocados. O Story editado fica com a marca de editado. A liberação é gradual, então pode ser que ainda não tenha aparecido na sua conta.

O que eu acredito: o erro mais caro no Story é o que ficou faltando. Eu vejo muito Story de negócio sem preço, sem horário e sem um jeito de responder.

Exemplo ilustrativo: o personal posta a vaga das 7h e esquece o horário. A fisio posta a avaliação sem o link. A barbearia posta o corte sem dizer como marcar.

Faça hoje: depois de cada Story de venda, confira 3 itens. O que você vende e como saber o preço. Uma figurinha de pergunta, enquete ou link. A palavra que a pessoa manda no direct. Faltou um? Edite dentro dos 15 minutos.

🔻 Envie para quem posta Story sem pedir nada. E comente CLIENTES que eu te chamo no direct e olho os seus 3 últimos Stories com você.

Fontes: Gazeta Brasil (18/11/2026), Portal Publicitário (Felipe Martins, 18/11/2026) e Hardware.com.br (19/11/2026).

#instagram #stories #donodenegocio #personaltrainer #barbearia""",
 2: """Depois de 2 anos de Uber eu fiquei farto. Foi ali que eu decidi mudar de vida.

O carro dava problema e eu continuava na rua. Não era a primeira vez: no Brasil, quando saí da Aeronáutica, eu já tinha feito Uber, já com a ideia de morar fora. Em Lisboa, antes do Uber, foram 12 horas por dia num restaurante e, no fim de semana, um clube até as 8 da manhã por 60 € a noite.

Um dia eu fiquei farto e decidi que queria ganhar mais. Voltei para a massagem e comecei a fazer sites para clientes. Em 2026 a empresa saiu de 1.500 € para 7.000 € por mês.

O que te deixa farto tem preço. Muito dono parado no mesmo faturamento reclama do mesmo problema por meses e nunca faz a conta dele.

Faça hoje: anote 3 coisas que te cansaram esta semana e, ao lado, quanto cada uma custou em horas ou euros. Exemplo ilustrativo de uma barbearia: 4 faltas sem aviso, 4 horas paradas, 100 €. Comece pela mais cara. Nesse caso, um sinal de 5 € para marcar.

🔻 Salve e comente CLIENTES. Eu te chamo no direct e a gente acha o que está custando mais caro no seu negócio.

#empreendedorismo #brasileirosemportugal #historiareal #donodenegocio #barbearia""",
 3: """O meu primeiro trabalho em Portugal foi voluntário. Com marketing digital.

Cheguei sozinho, com 300 €, para um intercâmbio onde trabalhei 2 meses com marketing digital. Nos 3 primeiros meses eu comia pizza e lasanha de supermercado e não dava nem para cortar o cabelo. Depois vieram o restaurante, o clube à noite e 2 anos de Uber. O marketing só voltou anos depois.

Quando voltou, eu comecei a criar sites para clientes e a fazer os meus próprios anúncios. O que eu aprendi sem receber virou o que eu cobro. Hoje são duas plataformas construídas do zero, a Lisboa Massagem e a MedPortugal, e 48.000 € faturados em 2026.

Antes de pagar alguém, ligue um anúncio você mesmo. Quem nunca ligou não sabe cobrar resultado de quem liga para ele.

Faça esta semana (exemplo ilustrativo de uma fisio): 1 anúncio de mensagem, 5 € por dia, 3 dias, para quem mora a 5 km. Anote quantas conversas chegaram e o que as pessoas perguntaram. São 15 € para saber o que o seu público quer.

🔻 Comente CLIENTES e quanto você já gastou em anúncio este ano. Eu te chamo no direct e a gente monta o teste dos 15 €.

#marketingdigital #anuncios #brasileirosemportugal #donodenegocio #fisioterapia""",
 4: """Não dê 30% de desconto na Black Friday. Venda a vaga de janeiro.

Desconto em serviço sai da sua margem. A sua hora de trabalho não fica mais barata em novembro.

A conta (exemplo ilustrativo): 30% num plano de 160 € são 48 € a menos por aluno, todo mês em que ele ficar nesse preço. Com 10 alunos assim, 480 € por mês, e o trabalho é o mesmo. E quem entra pelo preço costuma pedir o preço de novo.

O que fazer no lugar:
1. Abra poucas vagas para janeiro, um dos meses com mais entradas em academia (Wodify, dados de mais de 5.000 negócios de fitness, 2023 e 2024). Exemplo: 6 vagas no plano de 12 semanas.
2. Cobre um sinal para reservar, que desconta da 1ª mensalidade. Exemplo: 30 €. A ideia é do Chris Cooper, da Two-Brain Business: depósito no lugar de promoção.
3. Troque o desconto por um bônus que custa pouco para você: avaliação extra no mês 2, treino para as férias, um desafio de hábitos de 14 dias por mensagem. Na barbearia, a barba de cortesia na 1ª visita de janeiro. Regra do Cooper: nunca dê de graça o que outro cliente paga.
4. Mande hoje: "Oi, [nome]. Estou abrindo 6 vagas para começar em janeiro. Quem reservar até 30/11 garante a vaga com 30 € (desconta da 1ª mensalidade) e ganha [bônus]. Quer que eu guarde uma para você?" Envie para ex-alunos e para quem pediu preço este ano.

🔻 Comente CLIENTES e quantas vagas você abre para janeiro. Eu te chamo no direct e a gente escreve o seu bônus.

Fontes: Chris Cooper, Two-Brain Business ("How to Beat Black Friday (Without Discounts)", 21/10/2025; "5 Ways to Boost Year-End Revenue", 04/11/2025); Wodify, "Behind the Numbers".

#blackfriday #personaltrainer #academia #fisioterapia #barbearia""",
 5: """O dezembro do seu negócio se decide agora, em novembro.

Quem espera janeiro para vender começa janeiro com a agenda vazia. O personal que só avisa em janeiro vê o aluno começar com outro. A fisio que não chama o paciente antigo agora fica com dezembro aberto. A barbearia que não abre a agenda do Natal hoje atende no improviso no dia 23.

Hoje: mande mensagem a 10 clientes antigos com uma data de janeiro.

🔻 Salve e comente CLIENTES. Eu te chamo no direct.

#donodenegocio #personaltrainer #fisioterapia #barbearia #agendacheia""",
 6: """Se o seu negócio está parado no mesmo faturamento, segue @liurialves.

Quem está falando com você: fiquei 4 anos na Aeronáutica e saí porque precisava pedir autorização para tudo. No tempo de militar eu abri uma loja de moda praia e ela quebrou: a conta da loja era a mesma da casa. Cheguei a Portugal sozinho, com 300 €, e passei por restaurante, clube à noite e Uber.

Em 2026 eu saí de 1.500 € para 5.500 € por mês em 5 meses, fazendo sozinho o conteúdo, os anúncios e o atendimento.

Aqui você vai ver cliente todo mês, oferta, preço e a conta que sobra no fim do mês, com exemplo de personal, academia, fisio e barbearia.

Comece pelo número que você não sabe. Quase todo dono parado que eu vejo sabe quanto fatura e não sabe quanto custa trazer um cliente novo. Faça hoje: some o que gastou em anúncio, impulsionamento e brinde nos últimos 3 meses e divida pelos clientes novos. Exemplo ilustrativo: 300 € ÷ 6 clientes = 50 € por cliente.

🔻 Salve e comente CLIENTES com o seu tipo de negócio. Eu te chamo no direct e a gente faz essa conta juntos.

Fotos da Aeronáutica: Robério Castro Fotografia.

#donodenegocio #empreendedorismo #brasileirosemportugal #personaltrainer #barbearia""",
 7: """Eu não acredito que o cliente paga pelo seu tempo.

Num restaurante em Lisboa eu virei subgerente em 6 meses. Ali eu aprendi que quem resolve problema sobe. E na massagem eu tenho cliente que paga cerca de 300 € por mês, 2 a 3 vezes por semana. Ele não compra pelo preço.

O que eu vejo: o personal que vende "aula de 45 minutos" quando o aluno queria treinar sem dor nas costas. A fisio que vende "sessão de 50 minutos" quando o paciente queria voltar a correr. A barbearia que cobra pelo tempo na cadeira quando o cliente queria chegar bem na entrevista de segunda.

Ponha no nome do serviço o que o cliente quer. Faça esta semana: reescreva o nome do serviço que você mais vende, com o resultado e o prazo. Exemplos ilustrativos: "8 semanas para treinar sem dor nas costas", "Plano de 6 sessões para voltar a correr", "Corte e barba com horário fixo a cada 15 dias".

🔻 Envie para quem ainda vende hora. E comente CLIENTES que eu te chamo no direct e a gente dá um novo nome ao seu serviço.

#oferta #preco #donodenegocio #personaltrainer #fisioterapia""",
}


def run(cfg, out, script="render_faixa.py"):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/{script}", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    for n in range(1, 8):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(noticia, O(1), "render_formatos.py")
    run(farto, O(2)); run(voluntario, O(3)); run(janeiro, O(4))
    run(legenda, O(5), "render_legenda.py")
    run(apresentacao, O(6))
    run(tempo, O(7))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
