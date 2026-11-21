"""Plano 100 mil, semana 4 do PDF (janela de testes, dia 4), 17/11/2026, terça-feira. Dia 11 do "Plano de 30 dias para
lançar a mentoria": conteúdo "Quanto você precisa vender só para pagar a estrutura" (valor das 17:40) e tarefa "Enviar o
convite do desafio aos contatos e ex-clientes" (mensagem pronta no doc).
Grade do playbook (ajustes de 10/11 e 16/11, prevalecem sobre a tarefa agendada): 6 posts, sem post de IA.
Terça: 12:40 CONEXÃO · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 CONEXÃO · 22:15 BANDEIRA.
AJUSTE DE 11/11: "indicação" em 0 de 6 posts, 0 de 4 roteiros, 0 stories.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
CTA (rodízio sobre 16/11, todos terminam em "Comente CLIENTES"):
12:40 envio · 14:20 comentário · 17:40 salvar · 19:10 envio · 20:30 comentário · 22:15 salvar.
1) 12:40 FAIXA, conexão, pilar 6 (lição pilar 3): "O meu segundo filho quase nasceu num café." Itens 13, 14, 15/16.
   REMODELADO de liurialves:6afa875360a910801c6ae6aa (família no Brasil, 413 views): cena de família com número,
   trecho novo (o café, o ano do parto), lição nova (plano mensal pago no dia 1).
2) 14:20 FAIXA, conexão, pilar 5 (lição pilar 1): "Um gerente amigo me deu 100 € de presente. Eu chorei." Itens 15, 17, 18.
   REMODELADO de liurialves:6af5405dbfa789f6210abb2e (subgerente em 6 meses, 407 views): mesma fase (restaurante),
   número no gancho e contraste; gancho novo (o presente de 100 €).
3) 17:40 FAIXA, valor com rosto, pilar 4: quantos clientes para pagar a estrutura. Molde Two-Brain (17/10/2025).
4) 19:10 LEGENDA, bandeira falada, pilar 2: "uma manhã por semana sem cliente".
5) 20:30 FAIXA, conexão, pilar 6 (lição pilar 4): "Me disseram: não casa, não vale a pena. Eu casei." Itens 1, 3, 5, 6, 8, 11.
6) 22:15 FAIXA, bandeira, pilar 3: "Eu não acredito em vergonha de vender." Itens 2, 3, 4.
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/64249b54-0810-5c75-a043-3e128718a542/scratchpad"
DIA = "2026-11-17"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h17/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px17/pexels-{x}.jpg"
F = lambda n: f"{R}/assets/frames-falando/video-2026-10-17-a-{n}.jpg"
FF = lambda n: f"/tmp/fr17/video-2026-10-17-a-{n}.jpg"  # frame com laterais desfocadas (para o formato faixa)

# 1) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = ENVIO + CLIENTES
cafe = {"slides": [
  {"tipo": "foto", "foto": FF("25"), "foco_y": 0.34, "grande": True, "arraste": True, "faixa": "O ANO MAIS DIFÍCIL",
   "texto": "O MEU SEGUNDO FILHO QUASE NASCEU NUM CAFÉ."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.55, "faixa": "COMO A GENTE CHEGOU ATÉ ALI",
   "texto": "EU VIM PRIMEIRO PARA PORTUGAL, SOZINHO, COM 300 €.",
   "destaque": "ELA FICOU NO BRASIL COM O NOSSO FILHO."},
  {"tipo": "foto", "foto": HP("62"), "foco_y": 0.1, "faixa": "3 MESES DEPOIS",
   "texto": "ELA CHEGOU COM O NOSSO FILHO E GRÁVIDA DO SEGUNDO.",
   "destaque": "CONSEGUIMOS UM QUARTO NO MESMO DIA. ERAM TRÊS NUM QUARTO SÓ."},
  {"tipo": "foto", "foto": P("14525522"), "foco_y": 0.5, "faixa": "EU",
   "texto": "TRABALHAVA 12 HORAS POR DIA NUM RESTAURANTE.",
   "destaque": "E VENDIA A MINHA FOLGA."},
  {"tipo": "foto", "foto": HP("76"), "foco_y": 0.45, "faixa": "O CARRO",
   "texto": "NO ANO DO PARTO, COMPREI UM PUNTO DE 1996 POR 450 €.",
   "destaque": "DUROU 2 MESES. NO FIM, SÓ LIGAVA EMPURRANDO."},
  {"tipo": "foto", "foto": P("16969023"), "foco_y": 0.5, "faixa": "O CAFÉ",
   "texto": "O NOSSO SEGUNDO FILHO QUASE NASCEU NUM CAFÉ AO LADO.",
   "destaque": "FOI O ANO MAIS DIFÍCIL DA NOSSA VIDA."},
  {"tipo": "foto", "foto": HP("77"), "foco_y": 0.35, "faixa": "DEPOIS",
   "texto": "JUNTAMOS DINHEIRO E MUDAMOS PARA UMA CASA."},
  {"tipo": "branco", "blocos": [
   ["h", "SE VOCÊ PARASSE 15 DIAS AMANHÃ, QUANTO ENTRARIA?"], ["esp", 8],
   ["n", "Naquele ano, tudo dependia de eu aparecer para trabalhar. Muito dono de negócio vive assim: o personal que só recebe pela aula dada e o barbeiro que só recebe pelo corte feito."],
   ["n", "Faça esta semana: escolha 5 clientes que vêm toda semana e ofereça um plano mensal pago no dia 1. Exemplo ilustrativo de um personal com aula avulsa a 30 €, 2 vezes por semana: 8 aulas por 220 € no mês. O aluno economiza 20 € e você sabe o que entra antes de o mês começar."]]},
  {"tipo": "foto", "foto": FF("45"), "foco_y": 0.34, "faixa": "ENVIE PARA QUEM NÃO PODE PARAR",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE MONTA O SEU PLANO MENSAL.",
   "destaque": "QUANTO ENTRA SE VOCÊ PARAR?"},
]}

# 2) 14:20 FAIXA, CONEXÃO (REMODELADO), CTA = COMENTÁRIO + CLIENTES
presente = {"slides": [
  {"tipo": "foto", "foto": FF("46"), "foco_y": 0.34, "grande": True, "arraste": True, "faixa": "LISBOA, O PRIMEIRO ANO",
   "texto": "UM GERENTE AMIGO ME DEU 100 € DE PRESENTE. EU CHOREI."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.3, "faixa": "A CONTA QUE NÃO FECHAVA",
   "texto": "EU PRECISAVA DE 800 A 900 € POR MÊS PARA SOBREVIVER.",
   "destaque": "RECEBIA 700 €."},
  {"tipo": "foto", "foto": P("28051377"), "foco_y": 0.5, "faixa": "DE DIA",
   "texto": "12 HORAS POR DIA NO RESTAURANTE."},
  {"tipo": "foto", "foto": P("11734813"), "foco_y": 0.45, "faixa": "NO FIM DE SEMANA",
   "texto": "SAÍA À MEIA-NOITE E IA PARA UM CLUBE ATÉ AS 8 DA MANHÃ.",
   "destaque": "POR 60 € A NOITE. E AINDA FALTAVA."},
  {"tipo": "foto", "foto": P("5082977"), "foco_y": 0.5, "faixa": "TODO MÊS",
   "texto": "UM EX-GERENTE, QUE VIROU MEU AMIGO, ME EMPRESTAVA O QUE FALTAVA."},
  {"tipo": "foto", "foto": FF("13"), "foco_y": 0.34, "faixa": "UM DIA",
   "texto": "ELE ME DEU 100 € DE PRESENTE.",
   "destaque": "EU CHOREI. ALGUÉM SE PREOCUPAVA COMIGO."},
  {"tipo": "foto", "foto": FF("44"), "foco_y": 0.34, "faixa": "O QUE FICOU",
   "texto": "EU NUNCA ESQUECI QUEM LEMBROU DE MIM NO PIOR ANO.",
   "destaque": "O SEU CLIENTE TAMBÉM NÃO ESQUECE."},
  {"tipo": "branco", "blocos": [
   ["h", "MANDE HOJE 10 MENSAGENS QUE NÃO VENDEM NADA."], ["esp", 8],
   ["n", "Cliente que só tem notícias suas quando você quer vender começa a responder menos."],
   ["n", "Escolha 10 clientes atuais e mande, um por um, uma mensagem com o nome dele e um detalhe que só você sabe. Exemplo ilustrativo de uma fisioterapeuta: \"Oi, Ana. Lembrei de você hoje. Como ficou o ombro depois da mudança? Se voltar a doer, me avise.\" Anote quantos responderam até amanhã."]]},
  {"tipo": "foto", "foto": FF("57"), "foco_y": 0.34, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTOS DOS 10 TE RESPONDERAM. EU TE CHAMO NO DIRECT E A GENTE TRANSFORMA ISSO EM ROTINA DE ATENDIMENTO.",
   "destaque": "DE QUEM VOCÊ VAI LEMBRAR HOJE?"},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO, CTA = SALVAR + CLIENTES
estrutura = {"slides": [
  {"tipo": "foto", "foto": FF("54"), "foco_y": 0.34, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "QUANTOS CLIENTES VOCÊ PRECISA SÓ PARA ABRIR A PORTA?"},
  {"tipo": "foto", "foto": P("4969842"), "foco_y": 0.9, "faixa": "O QUE EU ACREDITO",
   "texto": "QUEM NÃO SABE ESSE NÚMERO COMEMORA FATURAMENTO QUE AINDA NÃO É LUCRO.",
   "destaque": "EU JÁ QUEBREI UMA LOJA SEM SABER O MEU."},
  {"tipo": "foto", "foto": P("5549509"), "foco_y": 0.5, "faixa": "UM CASO DE ACADEMIA",
   "texto": "UMA ACADEMIA NA SUÉCIA PRECISA DE 17 ALUNOS PARA EMPATAR. ABRIU COM 25.",
   "destaque": "O DONO SABE O NÚMERO DE CABEÇA. (TWO-BRAIN BUSINESS, 17/10/2025)"},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "SOME A ESTRUTURA DO MÊS"], ["esp", 8],
   ["n", "Tudo o que você paga mesmo sem atender ninguém: aluguel, sistemas, contador, luz, anúncio fixo e o seu salário."],
   ["n", "Exemplo ilustrativo de um estúdio de personal: 800 + 40 + 120 + 90 + 150 + 1.800 de salário = 3.000 €."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "QUANTO SOBRA DE CADA CLIENTE"], ["esp", 8],
   ["n", "Preço do plano menos o que você gasta só para atender aquele cliente: material, comissão, taxa do cartão."],
   ["n", "No exemplo: plano de 160 € menos 10 € de custos = 150 € por aluno."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "3.000 € ÷ 150 € = 20 ALUNOS"], ["esp", 8],
   ["n", "É o que ele precisa ter pagando todo mês só para a porta continuar aberta e ele receber o salário."],
   ["n", "O 21º aluno é o primeiro que vira lucro."]]},
  {"tipo": "branco", "blocos": [
   ["t", "NA BARBEARIA (EXEMPLO ILUSTRATIVO)"], ["esp", 6],
   ["h", "1.800 € ÷ 12 € POR CORTE = 150 CORTES"],
   ["n", "São 6 cortes por dia útil, num mês de 25 dias, antes de sobrar 1 euro."],
   ["n", "Se a terça tem 3 cortes, você já sabe que dia precisa de oferta."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "COMPARE COM O ÚLTIMO MÊS E DECIDA"], ["esp", 8],
   ["n", "Abaixo do número: o problema é cliente novo. Comece pelo anúncio e pelo atendimento."],
   ["n", "Perto do número: suba o valor por cliente antes de procurar mais gente."],
   ["n", "Acima do número: separe o que sobra numa conta só da empresa."]]},
  {"tipo": "foto", "foto": FF("58"), "foco_y": 0.34, "faixa": "SALVE E FAÇA A CONTA HOJE",
   "texto": "DEPOIS COMENTE CLIENTES COM O SEU NÚMERO. EU TE CHAMO NO DIRECT E A GENTE VÊ O QUE MEXER PRIMEIRO.",
   "destaque": "QUAL É O SEU NÚMERO?"},
]}

# 5) 20:30 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
casamento = {"slides": [
  {"tipo": "foto", "foto": HP("63"), "foco_y": 0.05, "grande": True, "arraste": True, "faixa": "O NOSSO CASAMENTO",
   "texto": "ME DISSERAM: NÃO CASA, NÃO VALE A PENA. EU CASEI."},
  {"tipo": "foto", "foto": HP("22"), "foco_y": 0.2, "faixa": "ANTES DISSO",
   "texto": "A GENTE VENDIA ÁGUA NA PRAIA COM UMA BICICLETA ENFERRUJADA.",
   "destaque": "O DINHEIRO DA ÁGUA ERA PARA CASAR."},
  {"tipo": "foto", "foto": HP("20"), "foco_y": 0.3, "faixa": "O QUE A GENTE OUVIA",
   "texto": "ALGUMAS PESSOAS FAZIAM PIADA.",
   "destaque": "\"NÃO CASA. NÃO VALE A PENA.\""},
  {"tipo": "foto", "foto": HP("29"), "foco_y": 0.15, "faixa": "O QUE EU DISSE A ELA",
   "texto": "VOU ENTRAR NA AERONÁUTICA, VOU ESTAR ENTRE OS MELHORES E A GENTE VAI MUDAR DE VIDA.",
   "destaque": "PASSEI NO TESTE FÍSICO EM 13º."},
  {"tipo": "foto", "foto": HP("28"), "foco_y": 0.35, "faixa": "A FORMATURA",
   "texto": "NO DIA DA FORMATURA, EU A PEDI EM CASAMENTO NA FRENTE DA TROPA."},
  {"tipo": "foto", "foto": HP("03"), "foco_y": 0.3, "faixa": "UM ANO DEPOIS",
   "texto": "CASAMOS UM ANO DEPOIS DA FORMATURA.",
   "destaque": "MAIS UM ANO E VEIO O PRIMEIRO FILHO."},
  {"tipo": "branco", "blocos": [
   ["h", "QUEM NÃO PAGA AS SUAS CONTAS NÃO DECIDE A SUA META."], ["esp", 8],
   ["n", "Todo dono de negócio parado escuta alguém dizer que está bom assim. A gente já tinha decidido e juntava o dinheiro da água para isso."],
   ["n", "Faça hoje: escreva quanto quer faturar daqui a 90 dias e divida pelo preço do seu plano. Exemplo ilustrativo de um personal que fatura 2.400 € com planos de 200 €: para chegar a 3.600 €, faltam 6 alunos. São 2 por mês, 1 a cada 15 dias."]]},
  {"tipo": "foto", "foto": FF("53"), "foco_y": 0.34, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTOS CLIENTES FALTAM PARA A SUA META. EU TE CHAMO NO DIRECT E A GENTE DIVIDE ISSO POR SEMANA.",
   "destaque": "QUANTOS FALTAM PARA VOCÊ?"},
]}

# 6) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = SALVAR + CLIENTES
vender = {"slides": [
  {"tipo": "foto", "foto": HP("07"), "foco_y": 0.12, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM VERGONHA DE VENDER."},
  {"tipo": "foto", "foto": HP("36"), "foco_y": 0.3, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "AOS 18 ANOS EU PERDI OS DOIS EMPREGOS. EU E A MINHA NAMORADA DECORAMOS CHINELOS COM PÉROLAS PARA VENDER."},
  {"tipo": "foto", "foto": HP("38"), "foco_y": 0.25, "faixa": "DEPOIS",
   "texto": "VENDEMOS AVON, BOTICÁRIO E NATURA. ELA VENDEU JOIAS E EU FUI JUNTO."},
  {"tipo": "foto", "foto": HP("39"), "foco_y": 0.2, "faixa": "A FASE MAIS DIFÍCIL",
   "texto": "A GENTE IA AO SHOPPING SÓ PELO WI-FI. DAVA PARA UM SORVETE SÓ, E A GENTE DIVIDIA.",
   "destaque": "NÃO SOBRAVA ESPAÇO PARA VERGONHA."},
  {"tipo": "foto", "foto": P("5549509"), "foco_y": 0.5, "faixa": "EXEMPLO: O PERSONAL",
   "texto": "TREINA O MESMO ALUNO HÁ 1 ANO E NUNCA OFERECEU O PLANO TRIMESTRAL.",
   "destaque": "O ALUNO NEM SABE QUE ELE EXISTE."},
  {"tipo": "foto", "foto": P("4969842"), "foco_y": 0.9, "faixa": "EXEMPLO: A BARBEARIA",
   "texto": "O CLIENTE VOLTA A CADA 20 DIAS E NINGUÉM FALA DO PLANO MENSAL NA HORA DE PAGAR."},
  {"tipo": "branco", "blocos": [
   ["h", "OFERECER FAZ PARTE DO ATENDIMENTO."], ["esp", 8],
   ["n", "Quem tem vergonha de falar de preço deixa o cliente decidir sozinho. E sozinho ele escolhe o mais barato ou nada."],
   ["n", "Esta semana, ofereça o seu plano a 10 clientes atuais, no fim do atendimento, com esta frase: \"Você vem toda semana. Tenho um plano mensal que sai mais em conta para quem vem assim. Posso te explicar em 1 minuto?\" Anote quantos disseram sim."]]},
  {"tipo": "foto", "foto": FF("50"), "foco_y": 0.34, "faixa": "SALVE A FRASE",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE AJUSTA A SUA OFERTA.",
   "destaque": "A QUANTOS DOS 10 VOCÊ VAI OFERECER?"},
]}

# 4) 19:10 LEGENDA (fala com frames do Liuri), bandeira falada, CTA = ENVIO + CLIENTES
legenda = {"slides": [
 {"fotos": [F("45"), F("13")], "foco": [0.6, 0.5], "textos": ["Eu acho que todo dono de negócio", "devia ter uma manhã por semana sem cliente."]},
 {"fotos": [F("55"), F("20")], "foco": [0.6, 0.5], "textos": ["Sem treino para dar, sem paciente,", "sem cadeira para cortar."]},
 {"fotos": [F("49"), F("31")], "foco": [0.6, 0.5], "textos": ["Quem atende o dia inteiro", "não tem tempo de olhar a própria empresa."]},
 {"fotos": [F("53"), F("29")], "foco": [0.6, 0.5], "textos": ["O personal que dá 9 aulas por dia", "e não sabe quanto sobrou no mês."]},
 {"fotos": [F("57"), F("33")], "foco": [0.6, 0.5], "textos": ["O barbeiro que corta até as 21h", "e posta a foto do corte às 23h."]},
 {"fotos": [F("44"), F("18")], "foco": [0.6, 0.5], "textos": ["Ocupado o dia inteiro", "e com o mesmo faturamento há meses."]},
 {"fotos": [F("58"), F("24")], "foco": [0.6, 0.5], "textos": ["Bloqueie 3 horas nesta semana:", "números, oferta e um post que peça algo."]},
 {"fotos": [F("50"), F("14")], "foco": [0.6, 0.5], "textos": ["Você tem essa manhã na agenda?", "Comente CLIENTES."]},
]}

LEGENDAS = {
 1: """O meu segundo filho quase nasceu num café.

Eu vim primeiro para Portugal, sozinho, com 300 €. Três meses depois ela chegou com o nosso filho e grávida do segundo. Conseguimos um quarto no mesmo dia e morávamos os três ali. Eu trabalhava 12 horas por dia num restaurante e vendia a folga. No ano do parto comprei um Punto de 1996 por 450 €, que durou 2 meses. O nosso segundo filho quase nasceu num café ao lado. Foi o ano mais difícil da nossa vida. Depois juntamos dinheiro e mudamos para uma casa.

Naquele ano, tudo dependia de eu aparecer para trabalhar. Muito dono de negócio vive assim. Se você parasse 15 dias amanhã, quanto entraria?

Faça esta semana: escolha 5 clientes que vêm toda semana e ofereça um plano mensal pago no dia 1. Exemplo ilustrativo de um personal com aula avulsa a 30 €, 2 vezes por semana: 8 aulas por 220 € no mês. O aluno economiza 20 € e você sabe o que entra antes de o mês começar.

🔻 Envie para quem não pode parar nem uma semana. E comente CLIENTES que eu te chamo no direct e a gente monta o seu plano mensal.

#empreendedorismo #familia #brasileirosemportugal #donodenegocio #historiareal""",
 2: """Um gerente amigo me deu 100 € de presente. Eu chorei.

No primeiro ano em Lisboa eu precisava de 800 a 900 € por mês para sobreviver e recebia 700 €. Eram 12 horas por dia no restaurante. No fim de semana eu saía à meia-noite e ia para um clube até as 8 da manhã, por 60 € a noite. E ainda faltava. Um ex-gerente, que virou meu amigo, me emprestava o que faltava todo mês. Um dia ele me deu 100 € de presente. Eu chorei por saber que alguém se preocupava comigo, e nunca esqueci.

O seu cliente funciona igual. Quem só tem notícias suas quando você quer vender começa a responder menos.

Faça hoje: escolha 10 clientes atuais e mande, um por um, uma mensagem com o nome dele e um detalhe que só você sabe. Sem oferta. Exemplo ilustrativo de uma fisioterapeuta: "Oi, Ana. Lembrei de você hoje. Como ficou o ombro depois da mudança? Se voltar a doer, me avise." Anote quantos responderam até amanhã.

🔻 Comente CLIENTES e quantos dos 10 te responderam. Eu te chamo no direct e a gente transforma isso em rotina de atendimento.

#empreendedorismo #brasileirosemportugal #atendimento #fisioterapia #donodenegocio""",
 3: """Quantos clientes você precisa só para abrir a porta?

Quem não sabe esse número comemora faturamento que ainda não é lucro. Eu já quebrei uma loja sem saber o meu. Uma academia na Suécia precisa de 17 alunos para empatar e abriu com 25 (Two-Brain Business, 17/10/2025). O dono sabe o número de cabeça.

1. Some a estrutura do mês: tudo o que você paga mesmo sem atender ninguém, com o seu salário. Exemplo ilustrativo de um estúdio de personal: 800 + 40 + 120 + 90 + 150 + 1.800 = 3.000 €.
2. Veja quanto sobra de cada cliente: plano de 160 € menos 10 € de custos = 150 €.
3. Divida: 3.000 € ÷ 150 € = 20 alunos. O 21º é o primeiro que vira lucro.
4. Compare com o último mês. Abaixo do número, o problema é cliente novo. Perto, suba o valor por cliente. Acima, separe o que sobra numa conta só da empresa.

Na barbearia (exemplo ilustrativo): 1.800 € ÷ 12 € por corte = 150 cortes, 6 por dia útil antes de sobrar 1 euro.

Dia 25 começa o meu Desafio 6 semanas. Quem comentar recebe os detalhes no direct.

🔻 Salve e faça a conta hoje. Depois comente CLIENTES com o seu número que eu te chamo no direct e a gente vê o que mexer primeiro.

#gestaofinanceira #donodenegocio #personaltrainer #barbearia #academia""",
 4: """Uma manhã por semana sem cliente.

Quem atende o dia inteiro não tem tempo de olhar a própria empresa. O personal que dá 9 aulas por dia e não sabe quanto sobrou no mês. O barbeiro que corta até as 21h e posta a foto do corte às 23h, sem pensar. Ocupados o dia inteiro e com o mesmo faturamento há meses.

Faça nesta semana: bloqueie 3 horas na agenda como se fosse um cliente. Na primeira hora, os números do mês. Na segunda, a sua oferta e o preço. Na terceira, um post que peça alguma coisa a quem lê.

🔻 Envie para quem atende o dia inteiro. E comente CLIENTES que eu te chamo no direct e a gente decide o que fazer nessas 3 horas.

#donodenegocio #empreendedorismo #personaltrainer #barbearia #gestao""",
 5: """Me disseram: não casa, não vale a pena. Eu casei.

A gente vendia água na praia com uma bicicleta enferrujada, e o dinheiro da água era para casar. Algumas pessoas faziam piada: "não casa, não vale a pena". Eu disse a ela que ia entrar na Aeronáutica, ficar entre os melhores, e que a gente ia mudar de vida. Passei no teste físico em 13º. No dia da formatura eu a pedi em casamento na frente da tropa. Casamos um ano depois, e mais um ano depois veio o primeiro filho.

Todo dono de negócio parado escuta alguém dizer que está bom assim. Quem não paga as suas contas não decide a sua meta.

Faça hoje: escreva quanto quer faturar daqui a 90 dias e divida pelo preço do seu plano. Exemplo ilustrativo de um personal que fatura 2.400 € com planos de 200 €: para chegar a 3.600 €, faltam 6 alunos. São 2 por mês, 1 a cada 15 dias.

🔻 Comente CLIENTES e quantos clientes faltam para a sua meta. Eu te chamo no direct e a gente divide isso por semana.

Fotos da formatura: Robério Castro Fotografia.

#casamento #historiareal #empreendedorismo #donodenegocio #metas""",
 6: """Eu não acredito em vergonha de vender.

Aos 18 anos eu perdi os dois empregos. Eu e a minha namorada decoramos chinelos com pérolas para vender. Depois vendemos Avon, Boticário e Natura, e ela vendeu joias comigo junto. Na fase mais difícil a gente ia ao shopping só pelo Wi-Fi e dividia um sorvete. Não sobrava espaço para vergonha.

Hoje eu vejo o personal que treina o mesmo aluno há 1 ano e nunca ofereceu o plano trimestral. E a barbearia em que o cliente volta a cada 20 dias e ninguém fala do plano mensal na hora de pagar. Quem tem vergonha de falar de preço deixa o cliente decidir sozinho, e sozinho ele escolhe o mais barato ou nada.

Esta semana, ofereça o seu plano a 10 clientes atuais, no fim do atendimento:
"Você vem toda semana. Tenho um plano mensal que sai mais em conta para quem vem assim. Posso te explicar em 1 minuto?"
Anote quantos disseram sim.

🔻 Salve a frase e comente CLIENTES. Eu te chamo no direct e a gente ajusta a sua oferta.

#vendas #oferta #personaltrainer #barbearia #donodenegocio""",
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
    for n in range(1, 7):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(cafe, O(1)); run(presente, O(2)); run(estrutura, O(3))
    run(legenda, O(4), "render_legenda.py"); run(casamento, O(5)); run(vender, O(6))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
