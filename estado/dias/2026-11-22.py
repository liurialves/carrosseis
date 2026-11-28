"""Plano 100 mil, semana 5 do PDF (leitura e corte, dia 2), 22/11/2026, domingo. Dia 16 do "Plano de 30 dias para lançar
a mentoria": conteúdo "Antes de contratar alguém, faça esta conta" (vira o VALOR das 17:40, pilar 4) e tarefa "Preparar o
material da semana 1 do desafio" (no doc).
Grade do playbook (ajustes de 10/11, 16/11, 18/11 e 19/11 prevalecem sobre a tarefa agendada): 7 posts, sem post de IA.
Domingo: 10:30 NOTÍCIA · 12:40 CONEXÃO · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 PROVA (remodelado) · 22:15 BANDEIRA.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
Fotos: só do Liuri (sem a ex-esposa), nenhum frame de vídeo. Indicação: 0 de 7 posts.
CTA (rodízio sobre 21/11, todos terminam em "Comente CLIENTES"):
10:30 salvar · 12:40 comentário · 14:20 envio · 17:40 salvar · 19:10 envio · 20:30 comentário · 22:15 salvar.
1) 10:30 NOTÍCIA: WhatsApp libera agendamento de mensagens (Economic News Brasil, Manoella Rufino, 20/11/2026, com testes do g1
   de 19/11; CBN Ribeirão, coluna Mundo Digital, 20/11/2026).
2) 12:40 FAIXA, conexão, pilar 5 (lição pilar 3): "Nos primeiros 5 meses eu trabalhava 12 horas por dia e ainda vendia a folga." Item 13.
3) 14:20 FAIXA, conexão, pilar 5: "Fui ajudante de personal, militar, subgerente de restaurante e motorista de Uber." Itens 2, 3, 6, 10,
   15, 17, 19, 20 + Cuidados (massagem desde 2017). Molde @moisesleall (lista de trabalhos antes do resultado).
4) 17:40 FAIXA, valor com rosto (A), pilar 4: antes de contratar, a conta (CoachLogik, Zack Bartell, 14/07/2026; FitHive, 16/08/2026).
5) 19:10 LEGENDA, bandeira falada, pilar 1: o cliente antigo vale mais do que um seguidor novo.
6) 20:30 FAIXA, PROVA, pilar 5: 1.500 € → 5.500 € em 5 meses → 7.000 €, com o print da planilha recortado.
   REMODELADO de liurialves:6af0889e9214322f685bb292 (08/11 17:40, capa+escuro, 332 views, 177 de alcance, nunca replicado):
   formato faixa no lugar de capa+escuro, outra foto de capa, print real dentro, lição nova (planilha de 30 dias), CTA comentário.
7) 22:15 FAIXA, bandeira, pilar 2: "Eu não acredito em 'agora não tenho tempo'." Fato: no tempo de militar, curso de massagem e
   a loja de moda praia (item 13a + Cuidados). Documento de Clareza: objeção "não tenho tempo" (pede 2 h por dia).
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/c0cd27e4-5c28-528e-b7a8-db15c0bdbb6b/scratchpad"
DIA = "2026-11-22"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h22/{x}.jpg"           # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px22/pexels-{x}.jpg"

# 1) 10:30 NOTÍCIA, CAPA + ESCURO, CTA = SALVAR + CLIENTES
noticia = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": P("9898392"), "foco_y": 0.45, "etiqueta": "Notícia",
   "titulo": "O WhatsApp começou a liberar mensagem agendada. Até 2 semanas antes.",
   "sub": "Economic News Brasil e CBN Ribeirão, 20/11/2026. O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O que mudou", "frase": "Dá para escrever hoje e [[enviar depois]].",
   "texto": "A função está chegando aos poucos. O g1 testou em 19/11 e viu no WhatsApp Web e em algumas contas de iPhone. A mensagem pendente pode ser consultada e cancelada."},
  {"etiqueta": "O que quase ninguém leu", "frase": "Áudio e documento [[ficaram de fora]].",
   "texto": "Nos testes, era preciso marcar com pelo menos 10 minutos de antecedência. E a Meta ainda não disse quando chega a todos nem confirmou se vale para o WhatsApp Business."},
  {"etiqueta": "O que eu acredito", "frase": "Cliente some no [[retorno que você esquece]].",
   "texto": "Eu vejo muito dono mandar o preço e nunca mais voltar a falar. No meio do dia, a mensagem de amanhã não sai."},
  {"etiqueta": "No seu negócio", "frase": "Agende [[na hora em que o pedido chega]].",
   "texto": "Exemplo ilustrativo: o personal manda o preço às 21h e já deixa a volta marcada para 2 dias depois. A fisio agenda o lembrete da véspera. A barbearia agenda o convite para o próximo corte 15 dias depois."},
  {"etiqueta": "Faça hoje", "frase": "[[3 mensagens]] agendadas antes de dormir.",
   "texto": "1. Para quem pediu preço esta semana: \"Oi, [nome]. Ficou alguma dúvida sobre o plano? Tenho 2 horários na quinta.\" 2. O lembrete de véspera de cada cliente de amanhã. 3. Um cliente que não aparece há 30 dias. Se a função ainda não chegou, use o alarme do celular."},
  {"etiqueta": "Próximo passo", "frase": "Salve para fazer hoje à noite e [[comente CLIENTES]].",
   "texto": "Eu te chamo no direct e a gente escreve a sua sequência de mensagens."},
]}

# 2) 12:40 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
folga = {"slides": [
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.35, "grande": True, "arraste": True,
   "faixa": "OS PRIMEIROS 5 MESES EM PORTUGAL",
   "texto": "EU TRABALHAVA 12 HORAS POR DIA E AINDA VENDIA A MINHA FOLGA."},
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.3, "faixa": "COMO EU CHEGUEI",
   "texto": "SOZINHO, COM 300 €.", "destaque": "A FAMÍLIA SÓ VEIO 3 MESES DEPOIS."},
  {"tipo": "foto", "foto": FL("cafe-pastel-pao-de-queijo"), "foco_y": 0.45, "faixa": "A FOLGA",
   "texto": "O DIA DE DESCANSO VIRAVA MAIS UM DIA DE TRABALHO.", "destaque": "CADA FOLGA VENDIDA IA PARA A CONTA DO MÊS."},
  {"tipo": "foto", "foto": P("18859074"), "foco_y": 0.45, "faixa": "E MESMO ASSIM",
   "texto": "EU PRECISAVA DE 800 A 900 € POR MÊS.", "destaque": "RECEBIA 700 €."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-1"), "foco_y": 0.2, "faixa": "O QUE EU VEJO HOJE",
   "texto": "MAIS HORA PAGAVA A CONTA DO MÊS.", "destaque": "O MÊS SEGUINTE COMEÇAVA IGUAL."},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente"), "foco_y": 0.3, "faixa": "O QUE MUDOU EM 2026",
   "texto": "COMECEI A FAZER MASSAGENS E SITES PARA CLIENTES.", "destaque": "DE 1.500 € PARA 7.000 € POR MÊS."},
  {"tipo": "branco", "blocos": [
   ["h", "TODO NEGÓCIO QUE VENDE HORA TEM UM TETO."], ["esp", 8],
   ["n", "Antes de trabalhar mais, descubra até onde a sua agenda vai."],
   ["n", "Faça a conta: horas que você aguenta atender por semana × preço da hora × 4. Exemplo ilustrativo de um personal: 30 sessões × 35 € × 4 = 4.200 € por mês com a agenda lotada. Se a sua meta passa disso, mais hora não resolve. O próximo passo é plano mensal, pacote ou turma."]]},
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E O SEU TETO DO MÊS. EU TE CHAMO NO DIRECT E A GENTE VÊ O QUE VEM DEPOIS DA AGENDA CHEIA.",
   "destaque": "QUAL É O SEU TETO?"},
]}

# 3) 14:20 FAIXA, CONEXÃO, CTA = ENVIO + CLIENTES
trabalhos = {"slides": [
  {"tipo": "foto", "foto": HP("40"), "foco_y": 0.25, "grande": True, "arraste": True, "faixa": "ANTES DA MINHA EMPRESA",
   "texto": "FUI AJUDANTE DE PERSONAL, MILITAR, SUBGERENTE DE RESTAURANTE E MOTORISTA DE UBER."},
  {"tipo": "foto", "foto": HP("47"), "foco_y": 0.25, "faixa": "AOS 18 ANOS",
   "texto": "JOVEM APRENDIZ NUMA CORRETORA E AJUDANTE DE PERSONAL NUMA ACADEMIA.", "destaque": "PERDI OS DOIS AO MESMO TEMPO."},
  {"tipo": "foto", "foto": P("38471760"), "foco_y": 0.5, "faixa": "DEPOIS",
   "texto": "VENDI CHINELO, COSMÉTICO, JOIA E ÁGUA NA PRAIA.", "destaque": "A ÁGUA FOI A QUE FEZ CAIXA."},
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.3, "faixa": "4 ANOS NA AERONÁUTICA",
   "texto": "CAMA PERFEITA, BOTA ENGRAXADA E BARBA FEITA TODO DIA.", "destaque": "ALI EU APRENDI DISCIPLINA."},
  {"tipo": "foto", "foto": P("14680058"), "foco_y": 0.45, "faixa": "PORTUGAL",
   "texto": "NUM RESTAURANTE, VIREI SUBGERENTE EM 6 MESES.", "destaque": "NO FIM DE SEMANA, CLUBE ATÉ AS 8 DA MANHÃ, POR 60 €."},
  {"tipo": "foto", "foto": FL("carro-painel-rua"), "foco_y": 0.5, "faixa": "DEPOIS",
   "texto": "2 ANOS DE UBER.", "destaque": "ATÉ FICAR FARTO E DECIDIR GANHAR MAIS."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "HOJE",
   "texto": "DUAS PLATAFORMAS CONSTRUÍDAS DO ZERO.", "destaque": "A LISBOA MASSAGEM TEM MAIS DE 90 TERAPEUTAS."},
  {"tipo": "branco", "blocos": [
   ["h", "VOCÊ JÁ SABE FAZER MAIS DO QUE VENDE."], ["esp", 8],
   ["n", "Eu fiz o curso de massagem em 2017 e só em 2026 passei a trabalhar bem com ela. A habilidade estava comigo esse tempo todo."],
   ["n", "Faça hoje: liste 3 coisas que você já sabe fazer e não cobra. Exemplos ilustrativos: o personal que monta a dieta de graça, a fisio que passa exercícios para casa, o barbeiro que acerta a sobrancelha. Escolha 1, dê um nome e um preço e ofereça a 5 clientes desta semana."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.3, "faixa": "ENVIE PARA QUEM JÁ FEZ DE TUDO",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE DÁ NOME E PREÇO AO QUE VOCÊ JÁ SABE FAZER.",
   "destaque": "QUAL FOI O SEU PRIMEIRO TRABALHO?"},
]}

# 4) 17:40 FAIXA, VALOR COM ROSTO (A), CTA = SALVAR + CLIENTES
contratar = {"slides": [
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "ANTES DE CONTRATAR ALGUÉM, FAÇA ESTA CONTA."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "O QUE EU ACREDITO",
   "texto": "CONTRATAR PARA SAIR DO OPERACIONAL É UMA ÓTIMA DECISÃO.", "destaque": "DESDE QUE JÁ EXISTA CLIENTE PARA PAGAR O SALÁRIO."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "MEÇA A SUA OCUPAÇÃO"], ["esp", 8],
   ["n", "Horas vendidas ÷ horas que você quer trabalhar. Exemplo ilustrativo: 32 sessões ÷ 40 horas = 80%."],
   ["n", "A CoachLogik (Zack Bartell, 14/07/2026) sugere pensar no primeiro contratado perto dos 80%, antes de chegar ao limite."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "SOME O CUSTO TOTAL DO MÊS"], ["esp", 8],
   ["n", "Salário, encargos, seguro, material e uniforme. Peça o número fechado ao seu contabilista."],
   ["n", "Exemplo ilustrativo: 1.000 € por mês."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "DESCUBRA QUANTO ELE PRECISA GERAR"], ["esp", 8],
   ["n", "Receita necessária = custo ÷ a parte da receita que você aceita pagar a ele (a fórmula é da FitHive, 16/08/2026)."],
   ["n", "Referência da CoachLogik: até cerca de 30% do que a aula gera. Exemplo: 1.000 € ÷ 30% = 3.333 € por mês."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "TRANSFORME EM CLIENTES"], ["esp", 8],
   ["n", "Exemplo ilustrativo de um estúdio: 3.333 € ÷ 120 € de mensalidade = 28 alunos."],
   ["n", "Na barbearia: 3.333 € ÷ 20 € por corte = 167 cortes por mês, cerca de 8 por dia útil."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 5"], ["h", "DECIDA COM UMA PERGUNTA"], ["esp", 8],
   ["n", "Eu tenho, ou consigo trazer em 90 dias, esses 28 alunos para ele?"],
   ["n", "Se a resposta for não, comece pagando por sessão ou por comissão. Se for sim, contrate e passe para ele os horários que você já não consegue atender."]]},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "E QUANTO CUSTA O SEU PRIMEIRO CONTRATADO. EU TE CHAMO NO DIRECT E A GENTE FAZ A CONTA COM OS SEUS NÚMEROS.",
   "destaque": "QUANTOS CLIENTES ELE PRECISA?"},
]}

# 5) 19:10 LEGENDA (fotos reais do Liuri), bandeira falada, CTA = ENVIO + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("selfie-jaqueta-verde"), HP("71")], "foco": [0.3, 0.3], "textos": ["Eu acho que o seu cliente antigo", "vale mais do que um seguidor novo."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), HP("72")], "foco": [0.2, 0.4], "textos": ["Ele já pagou, já confia", "e já sabe onde você fica."]},
 {"fotos": [FL("lagoa-biceps-de-frente-editada"), HP("47")], "foco": [0.35, 0.25], "textos": ["O personal posta para quem nunca treinou com ele", "e esquece o aluno que parou em agosto."]},
 {"fotos": [FL("home-office-headset"), HP("40")], "foco": [0.3, 0.3], "textos": ["A fisio procura paciente novo", "e não pergunta ao antigo como está o joelho."]},
 {"fotos": [FL("selfie-sem-camisa-serio"), FL("carro-painel-rua")], "foco": [0.3, 0.5], "textos": ["A barbearia faz promoção para estranho", "e o cliente de sempre some sem ninguém notar."]},
 {"fotos": [HP("05"), FL("dunas-punhos-camisa-preta-2")], "foco": [0.35, 0.2], "textos": ["Ninguém te esqueceu.", "Você parou de chamar."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-3"), FL("cafe-pastel-pao-de-queijo")], "foco": [0.2, 0.45], "textos": ["Hoje, 5 mensagens para quem não volta há 60 dias,", "sem oferta, só perguntando como está."]},
 {"fotos": [HP("42"), f"{R}/assets/foto-perfil-liuri.jpg"], "foco": [0.3, 0.3], "textos": ["Envie para quem corre atrás de seguidor", "e comente CLIENTES."]},
]}

# 6) 20:30 FAIXA, PROVA (REMODELADO), CTA = COMENTÁRIO + CLIENTES
prova = {"slides": [
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "PROVA · 2026",
   "texto": "EM 5 MESES, A MINHA EMPRESA SAIU DE 1.500 € PARA 5.500 € POR MÊS."},
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.3, "faixa": "E DEPOIS",
   "texto": "CHEGOU A 7.000 € POR MÊS.", "destaque": "EU FAZIA SOZINHO O CONTEÚDO, OS ANÚNCIOS E O ATENDIMENTO."},
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.35, "faixa": "DE ONDE EU VIM",
   "texto": "2 ANOS DE UBER EM PORTUGAL.", "destaque": "E A MASSAGEM DEIXADA DE LADO DESDE QUE CHEGUEI."},
  {"tipo": "foto", "foto": HP("prova-planilha"), "foco_y": 0.2, "faixa": "O PRINT",
   "texto": "A PLANILHA DE UM MÊS: RECEITA 2.156,50 €, DESPESAS 75 €.", "destaque": "SEMANA 1: 1.843 €. SEMANA 2: 313,50 €."},
  {"tipo": "branco", "blocos": [
   ["h", "NÃO FOI SORTE."], ["esp", 8],
   ["n", "Conteúdo toda semana, anúncio de mensagem e atendimento. Eu fazia os três sozinho."],
   ["n", "De 15 a 31/10/2026, 252 € em anúncios de mensagem viraram 1.755 € em atendimentos."]]},
  {"tipo": "foto", "foto": FL("coco-verde-mesa"), "foco_y": 0.5, "faixa": "O QUE ISSO NÃO É",
   "texto": "NÃO É PROMESSA PARA VOCÊ.", "destaque": "É O QUE EU FIZ NO MEU NEGÓCIO, COM OS MEUS NÚMEROS."},
  {"tipo": "branco", "blocos": [
   ["h", "ANTES DE MUDAR TUDO, ANOTE 30 DIAS."], ["esp", 8],
   ["n", "O print mostra o que uma planilha simples revela: uma semana de 1.843 € e outra de 313,50 € no mesmo mês."],
   ["n", "Faça hoje: abra uma planilha com 4 colunas (data, serviço, valor, de onde veio o cliente) e preencha todo atendimento por 30 dias. Some no domingo. Exemplo ilustrativo de uma barbearia: 62 cortes, 1.240 €, 40 vieram do Instagram."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTO O SEU NEGÓCIO FATURA HOJE. EU TE CHAMO NO DIRECT E TE MOSTRO COMO EU MONTEI A MINHA PLANILHA.",
   "destaque": "QUANTO VOCÊ FATURA POR MÊS?"},
]}

# 7) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = SALVAR + CLIENTES
tempo = {"slides": [
  {"tipo": "foto", "foto": HP("05"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM \"AGORA NÃO TENHO TEMPO\"."},
  {"tipo": "foto", "foto": P("6560291"), "foco_y": 0.9, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "NO TEMPO DE MILITAR, EU FIZ O CURSO DE MASSAGEM.", "destaque": "E ABRI UMA LOJA DE MODA PRAIA."},
  {"tipo": "foto", "foto": P("36772528"), "foco_y": 0.4, "faixa": "A LOJA QUEBROU",
   "texto": "NÃO FOI POR FALTA DE TEMPO.", "destaque": "EU MISTUREI A CONTA DA LOJA COM A DE CASA."},
  {"tipo": "foto", "foto": P("36120641"), "foco_y": 0.4, "faixa": "O QUE EU VEJO",
   "texto": "O PERSONAL COM AGENDA DAS 6H ÀS 22H.", "destaque": "NUNCA SOBRAM 2 HORAS PARA O PRÓPRIO NEGÓCIO."},
  {"tipo": "foto", "foto": P("20860625"), "foco_y": 0.35, "faixa": "E TAMBÉM",
   "texto": "A FISIO QUE RESPONDE WHATSAPP ENTRE UM PACIENTE E OUTRO.", "destaque": "E DEIXA O ORÇAMENTO PARA DEPOIS."},
  {"tipo": "foto", "foto": P("2076930"), "foco_y": 0.35, "faixa": "E AINDA",
   "texto": "O BARBEIRO QUE CORTA ATÉ FECHAR.", "destaque": "E POSTA O CORTE SEM PREÇO, À MEIA-NOITE."},
  {"tipo": "branco", "blocos": [
   ["h", "TEMPO PARA O NEGÓCIO SE MARCA NA AGENDA."], ["esp", 8],
   ["n", "Para quem eu acompanho, eu peço 2 horas por dia. Quem não consegue, ainda não está no momento."],
   ["n", "Faça esta semana: bloqueie 2 horas fixas como se fossem um cliente que paga. Exemplo: terça e quinta, das 14h às 15h. Na 1ª, revise a sua oferta. Na 2ª, responda quem pediu preço."]]},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE ACHA AS SUAS 2 HORAS NA AGENDA DESTA SEMANA.",
   "destaque": "QUANDO É O SEU HORÁRIO DO NEGÓCIO?"},
]}

LEGENDAS = {
 1: """O WhatsApp começou a liberar mensagem agendada. Dá para programar até 2 semanas antes.

A função está chegando aos poucos. Nos testes do g1, em 19/11, ela apareceu no WhatsApp Web e em algumas contas de iPhone. A mensagem pendente pode ser consultada e cancelada.

O detalhe que quase ninguém leu: áudio e documento ficaram de fora, e é preciso marcar com pelo menos 10 minutos de antecedência. A Meta ainda não disse quando chega a todos nem confirmou se vale para o WhatsApp Business.

O que eu acredito: cliente some no retorno que você esquece. Eu vejo muito dono mandar o preço e nunca mais voltar a falar.

Exemplo ilustrativo: o personal manda o preço às 21h e já deixa a volta marcada para 2 dias depois. A fisio agenda o lembrete da véspera. A barbearia agenda o convite para o próximo corte 15 dias depois.

Faça hoje, antes de dormir, 3 mensagens agendadas:
1. Para quem pediu preço esta semana: "Oi, [nome]. Ficou alguma dúvida sobre o plano? Tenho 2 horários na quinta."
2. O lembrete de véspera de cada cliente de amanhã.
3. Um cliente que não aparece há 30 dias.
Se a função ainda não chegou na sua conta, use o alarme do celular.

🔻 Salve para fazer hoje à noite. E comente CLIENTES que eu te chamo no direct e a gente escreve a sua sequência de mensagens.

Fontes: Economic News Brasil (Manoella Rufino, 20/11/2026, com testes do g1 de 19/11) e CBN Ribeirão (coluna Mundo Digital, 20/11/2026).

#whatsapp #whatsappbusiness #donodenegocio #personaltrainer #barbearia""",
 2: """Nos primeiros 5 meses em Portugal eu trabalhava 12 horas por dia e ainda vendia a minha folga.

Cheguei sozinho, com 300 €. A família só veio 3 meses depois. O dia de descanso virava mais um dia de trabalho, e cada folga vendida ia para a conta do mês. Mesmo assim, eu precisava de 800 a 900 € por mês e recebia 700 €.

O que eu vejo hoje: mais hora pagava a conta do mês, e o mês seguinte começava igual. Em 2026 eu comecei a fazer massagens e sites para clientes, e a empresa saiu de 1.500 € para 7.000 € por mês.

Todo negócio que vende hora tem um teto. Antes de trabalhar mais, descubra até onde a sua agenda vai.

Faça a conta: horas que você aguenta atender por semana × preço da hora × 4. Exemplo ilustrativo de um personal: 30 sessões × 35 € × 4 = 4.200 € por mês com a agenda lotada. Se a sua meta passa disso, mais hora não resolve. O próximo passo é plano mensal, pacote ou turma.

🔻 Comente CLIENTES e o seu teto do mês. Eu te chamo no direct e a gente vê o que vem depois da agenda cheia.

#empreendedorismo #brasileirosemportugal #historiareal #donodenegocio #personaltrainer""",
 3: """Antes da minha empresa, eu fui ajudante de personal, militar, subgerente de restaurante e motorista de Uber.

Aos 18 anos eu era jovem aprendiz numa corretora e ajudante de personal numa academia. Perdi os dois ao mesmo tempo. Depois vendi chinelo, cosmético, joia e água na praia, e a água foi a que fez caixa. Foram 4 anos na Aeronáutica, com cama perfeita, bota engraxada e barba feita todo dia. Em Portugal, virei subgerente de restaurante em 6 meses e, no fim de semana, trabalhava num clube até as 8 da manhã por 60 €. Depois vieram 2 anos de Uber, até eu ficar farto e decidir ganhar mais.

Hoje são duas plataformas construídas do zero, e a Lisboa Massagem tem mais de 90 terapeutas.

Você já sabe fazer mais do que vende. Eu fiz o curso de massagem em 2017 e só em 2026 passei a trabalhar bem com ela.

Faça hoje: liste 3 coisas que você já sabe fazer e não cobra. Exemplos ilustrativos: o personal que monta a dieta de graça, a fisio que passa exercícios para casa, o barbeiro que acerta a sobrancelha. Escolha 1, dê um nome e um preço e ofereça a 5 clientes desta semana.

🔻 Envie para quem já fez de tudo. E comente CLIENTES que eu te chamo no direct e a gente dá nome e preço ao que você já sabe fazer.

Fotos da Aeronáutica: Robério Castro Fotografia.

#empreendedorismo #historiareal #brasileirosemportugal #personaltrainer #donodenegocio""",
 4: """Antes de contratar alguém, faça esta conta.

Contratar para sair do operacional é uma ótima decisão, desde que já exista cliente para pagar o salário.

1. Meça a sua ocupação: horas vendidas ÷ horas que você quer trabalhar. Exemplo ilustrativo: 32 sessões ÷ 40 horas = 80%. A CoachLogik sugere pensar no primeiro contratado perto dos 80%, antes de chegar ao limite.
2. Some o custo total do mês: salário, encargos, seguro, material e uniforme. Peça o número fechado ao seu contabilista. Exemplo: 1.000 €.
3. Descubra quanto ele precisa gerar: custo ÷ a parte da receita que você aceita pagar a ele. Referência americana: até cerca de 30% do que a aula gera. 1.000 € ÷ 30% = 3.333 € por mês.
4. Transforme em clientes: 3.333 € ÷ 120 € de mensalidade = 28 alunos. Na barbearia, 3.333 € ÷ 20 € por corte = 167 cortes por mês, cerca de 8 por dia útil.
5. Decida com uma pergunta: eu tenho, ou consigo trazer em 90 dias, esses 28 alunos para ele? Se não, comece pagando por sessão ou por comissão. Se sim, contrate e passe para ele os horários que você já não consegue atender.

🔻 Salve para fazer com os seus números. E comente CLIENTES que eu te chamo no direct e a gente faz essa conta juntos.

Fontes: CoachLogik (Zack Bartell, "When to Hire Your First Assistant Coach", 14/07/2026) e FitHive (Sunny S., "How to Pay Fitness Coaches", 16/08/2026). Todos os valores do post são exemplos.

#gestao #personaltrainer #academia #fisioterapia #barbearia""",
 5: """O seu cliente antigo vale mais do que um seguidor novo.

Ele já pagou, já confia e já sabe onde você fica. O personal posta para quem nunca treinou com ele e esquece o aluno que parou em agosto. A fisio procura paciente novo e não pergunta ao antigo como está o joelho. A barbearia faz promoção para estranho e o cliente de sempre some sem ninguém notar.

Ninguém te esqueceu. Você parou de chamar.

Hoje: 5 mensagens para quem não volta há 60 dias, sem oferta, só perguntando como está.

🔻 Envie para quem corre atrás de seguidor. E comente CLIENTES que eu te chamo no direct.

#donodenegocio #personaltrainer #fisioterapia #barbearia #clientes""",
 6: """Em 5 meses, a minha empresa saiu de 1.500 € para 5.500 € por mês. Depois chegou a 7.000 €.

Eu fazia sozinho o conteúdo, os anúncios e o atendimento. Vinha de 2 anos de Uber em Portugal, com a massagem deixada de lado desde que cheguei.

O print é real: a planilha de um mês, com receita de 2.156,50 € e despesas de 75 €. Semana 1: 1.843 €. Semana 2: 313,50 €. E de 15 a 31/10/2026, 252 € em anúncios de mensagem viraram 1.755 € em atendimentos.

Isto não é promessa para você. É o que eu fiz no meu negócio, com os meus números.

Antes de mudar tudo, anote 30 dias. Abra uma planilha com 4 colunas (data, serviço, valor, de onde veio o cliente) e preencha todo atendimento. Some no domingo. Exemplo ilustrativo de uma barbearia: 62 cortes, 1.240 €, 40 vieram do Instagram.

Se quiser fazer isso acompanhado, o Desafio 6 semanas começa no dia 25/11.

🔻 Comente CLIENTES e quanto o seu negócio fatura hoje. Eu te chamo no direct e te mostro como eu montei a minha planilha.

#prova #donodenegocio #empreendedorismo #brasileirosemportugal #personaltrainer""",
 7: """Eu não acredito em "agora não tenho tempo".

No tempo de militar, eu fiz o curso de massagem e abri uma loja de moda praia. A loja quebrou, e não foi por falta de tempo: eu misturei a conta da loja com a de casa.

O que eu vejo: o personal com agenda das 6h às 22h, que nunca tem 2 horas para o próprio negócio. A fisio que responde WhatsApp entre um paciente e outro e deixa o orçamento para depois. O barbeiro que corta até fechar e posta o corte sem preço, à meia-noite.

Tempo para o negócio se marca na agenda. Para quem eu acompanho, eu peço 2 horas por dia. Quem não consegue, ainda não está no momento.

Faça esta semana: bloqueie 2 horas fixas como se fossem um cliente que paga. Exemplo: terça e quinta, das 14h às 15h. Na 1ª, revise a sua oferta. Na 2ª, responda quem pediu preço.

🔻 Salve e comente CLIENTES. Eu te chamo no direct e a gente acha as suas 2 horas na agenda desta semana.

#donodenegocio #disciplina #personaltrainer #fisioterapia #barbearia""",
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
    run(folga, O(2)); run(trabalhos, O(3)); run(contratar, O(4))
    run(legenda, O(5), "render_legenda.py")
    run(prova, O(6))
    run(tempo, O(7))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
