"""Plano 100 mil, semana 5 do PDF (leitura e corte, dia 6), 26/11/2026, quinta. Dia 20 do "Plano de 30 dias para lançar
a mentoria": conteúdo "Funil simples: conteúdo, direct, call, venda" (vira o valor das 17:40) e tarefa "Acompanhar os participantes no grupo".
Grade do playbook (ajustes de 10/11, 16/11, 18/11, 19/11 e 23/11 prevalecem sobre a tarefa agendada): 7 posts, sem post de IA.
Quinta: 10:30 NOTÍCIA · 12:40 CONEXÃO (remodelado) · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 CONEXÃO · 22:15 BANDEIRA.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
Fotos: só do Liuri (sem a ex-esposa), nenhum frame de vídeo; filhos só no post de família (20:30), fatias internas. Indicação: 0 de 7.
CTA (rodízio sobre 25/11, todos terminam em "Comente CLIENTES"):
10:30 envio · 12:40 salvar · 14:20 comentário · 17:40 salvar · 19:10 envio · 20:30 comentário · 22:15 envio.
1) 10:30 NOTÍCIA: Observatório IPAM (Jornal Económico com Lusa, 25/11/2026; PME Magazine, Daniela Felício, 25/11/2026).
2) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): o quarto conseguido no dia em que a família chegou. Itens 13 e 14.
   REMODELADO de liurialves:6afe7b04749099bdc70d5423 ("Saía do restaurante à meia-noite...", 19/11 12:40, 81 de alcance, 190 views,
   o carrossel com mais alcance ainda não replicado em 14 dias): mesma fase (primeiro ano em Lisboa) e arco; trecho, capa, fotos, lição e CTA novos.
3) 14:20 FAIXA, conexão, pilar 5 (lição pilar 2): na quarentena aprendi a valorizar um banho. Item 7 (gancho novo) + item 10.
4) 17:40 FAIXA, valor com rosto, pilar 1: funil em 4 passos (Two-Brain Business, John Franklin, 04/08/2026).
5) 19:10 LEGENDA, bandeira falada, pilar 3: o seu negócio não precisa de Black Friday. Item 16 em 1 linha.
6) 20:30 FAIXA, conexão (família), pilar 6 (lição pilar 4): o primeiro filho nasceu quando eu ainda vestia a farda. Itens 9, 11, 12, 13.
7) 22:15 FAIXA, bandeira, pilar 2: "Eu não acredito em quem promete o seu faturamento." Item 20 + item 10 + Documento de Clareza.
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/8c63aa34-dcf6-5814-9f9c-d5781b8d93ef/scratchpad"
DIA = "2026-11-26"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h26/{x}.jpg"           # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px26/pexels-{x}.jpg"

# 1) 10:30 NOTÍCIA, CAPA + ESCURO, CTA = ENVIO + CLIENTES
noticia = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": P("33191824"), "foco_y": 0.5, "etiqueta": "Notícia",
   "titulo": "71% já usaram IA para decidir uma compra. O seu próximo cliente pode estar perguntando por você ao ChatGPT.",
   "sub": "Observatório IPAM (25/11/2026). O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O número", "frase": "[[71%]] usaram IA para decidir uma compra.",
   "texto": "Nos últimos 6 meses. Inquérito do Observatório IPAM com 1.208 respostas de residentes em Portugal com 18 anos ou mais, de 28 de outubro a 12 de novembro. Entre eles, 88% usam o ChatGPT, 45% o Gemini e 31% a Meta AI."},
  {"etiqueta": "O que quase ninguém leu", "frase": "[[52%]] já pegaram a IA com informação errada.",
   "texto": "Errada, desatualizada ou contraditória. Por isso 46% confirmam sempre ou quase sempre noutra fonte. As mais usadas: o site oficial da marca (91%) e a avaliação de outros clientes (71%)."},
  {"etiqueta": "E tem mais", "frase": "Só [[15%]] deixariam a IA fechar a compra.",
   "texto": "85% usam a IA para comparar alternativas. A escolha final continua com a pessoa. A PME Magazine lembra que a amostra não é probabilística: os números são indicativos."},
  {"etiqueta": "O que eu acredito", "frase": "Quem só diz \"chama no direct\" [[sai da comparação]].",
   "texto": "A pessoa e a IA comparam o que está escrito: serviço, preço, horário e avaliação. Se nada disso está em lugar nenhum, você nem entra na lista."},
  {"etiqueta": "No seu negócio", "frase": "Escreva o que a pessoa [[confere]].",
   "texto": "Exemplo ilustrativo de uma barbearia. Antes, na bio: \"Agende já\". Depois: \"Corte + barba 25 €. Terça a sábado, das 9h às 20h. Plano mensal 60 €.\" E 10 avaliações no Google de clientes desta semana."},
  {"etiqueta": "Faça hoje", "frase": "[[3 coisas]] em menos de 1 hora.",
   "texto": "1. Serviços com preço, ou \"a partir de\", no Perfil da Empresa no Google. 2. A mesma lista num destaque do Instagram. 3. Peça avaliação a 5 clientes desta semana, com o link pronto no WhatsApp."},
  {"etiqueta": "Próximo passo", "frase": "[[Envie]] para quem tem negócio e comente CLIENTES.",
   "texto": "Eu te chamo no direct e te digo o que um cliente encontra hoje quando procura por você."},
]}

# 2) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = SALVAR + CLIENTES
quarto = {"slides": [
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.45, "grande": True, "arraste": True,
   "faixa": "LISBOA, O PRIMEIRO ANO",
   "texto": "CONSEGUIMOS O QUARTO NO MESMO DIA EM QUE A MINHA FAMÍLIA CHEGOU."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.55, "faixa": "EU VIM ANTES, SOZINHO",
   "texto": "COM 300 €.", "destaque": "A FAMÍLIA VEIO 3 MESES DEPOIS."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.3, "faixa": "ATÉ ELES CHEGAREM",
   "texto": "12 HORAS POR DIA DE TRABALHO.", "destaque": "E EU AINDA VENDIA A FOLGA."},
  {"tipo": "foto", "foto": HP("62"), "foco_y": 0.15, "faixa": "UM QUARTO SÓ",
   "texto": "MORÁVAMOS OS TRÊS NUM QUARTO. JÁ TÍNHAMOS UM BEBÊ.", "destaque": "E O SEGUNDO FILHO JÁ ESTAVA A CAMINHO."},
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.3, "faixa": "AQUELE ANO",
   "texto": "FOI O MAIS DIFÍCIL DA NOSSA VIDA.", "destaque": "DEPOIS A GENTE JUNTOU DINHEIRO."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "SÓ ENTÃO",
   "texto": "MUDAMOS PARA UMA CASA.", "destaque": "PRIMEIRO A GENTE JUNTOU. A CASA VEIO DEPOIS."},
  {"tipo": "branco", "blocos": [
   ["h", "O SEU NEGÓCIO TAMBÉM PRECISA JUNTAR ANTES DE MUDAR."], ["esp", 8],
   ["n", "Antes de trocar de espaço, contratar ou comprar equipamento, separe uma parte de cada pagamento numa conta que você não mexe."],
   ["n", "Exemplo ilustrativo de um personal que fatura 2.500 € por mês: 10% de cada pagamento são 250 € por mês. Em 6 meses, 1.500 € guardados antes de assinar o aluguel de um estúdio."]]},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-1"), "foco_y": 0.2, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE VÊ QUANTO O SEU NEGÓCIO CONSEGUE GUARDAR.",
   "destaque": "QUANTO VOCÊ SEPARA HOJE?"},
]}

# 3) 14:20 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
banho = {"slides": [
  {"tipo": "foto", "foto": HP("40"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "AERONÁUTICA, OS PRIMEIROS DIAS",
   "texto": "NA QUARENTENA EU APRENDI A VALORIZAR UM BANHO."},
  {"tipo": "foto", "foto": HP("11"), "foco_y": 0.2, "faixa": "40 A 45 DIAS",
   "texto": "LONGE DA FAMÍLIA, NO COMEÇO DA AERONÁUTICA.", "destaque": "FOI MUITO DIFÍCIL."},
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.3, "faixa": "LÁ DENTRO",
   "texto": "MUITO GRITO, MUITA CORRERIA, TROCA DE FARDA.", "destaque": "UM BANHO PASSOU A TER OUTRO VALOR."},
  {"tipo": "foto", "foto": HP("13"), "foco_y": 0.3, "faixa": "O QUE EU ENTENDI ALI",
   "texto": "A GENTE SÓ PERCEBE O BÁSICO QUANDO ELE FALTA.", "destaque": "FOI ALI QUE EU AMADURECI."},
  {"tipo": "foto", "foto": P("4625626"), "foco_y": 0.4, "faixa": "NO SEU NEGÓCIO",
   "texto": "O CLIENTE TAMBÉM PERCEBE O BÁSICO.", "destaque": "QUANDO ELE FALTA."},
  {"tipo": "foto", "foto": P("37963580"), "foco_y": 0.35, "faixa": "O BÁSICO QUE FALTA",
   "texto": "RESPOSTA QUE DEMORA UM DIA. HORÁRIO QUE NINGUÉM CONFIRMA.", "destaque": "SESSÃO QUE ACABA SEM A PRÓXIMA MARCADA."},
  {"tipo": "branco", "blocos": [
   ["h", "O TESTE DO BÁSICO, EM 1 SEMANA."], ["esp", 8],
   ["n", "Anote 3 números: em quanto tempo você responde uma mensagem nova, quantos clientes recebem confirmação na véspera e quantos saem da sessão com a próxima marcada."],
   ["n", "Exemplo ilustrativo de uma fisio: responde em 5 horas, confirma 4 de 20 e marca a próxima com 6 de 20. Meta da semana: responder em até 1 hora, confirmar 20 de 20 e marcar a próxima antes do paciente sair."]]},
  {"tipo": "foto", "foto": HP("05"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E O SEU TEMPO DE RESPOSTA DE HOJE. EU TE CHAMO NO DIRECT.",
   "destaque": "QUAL BÁSICO ESTÁ FALTANDO AÍ?"},
]}

# 4) 17:40 FAIXA, VALOR COM ROSTO, CTA = SALVAR + CLIENTES
funil = {"slides": [
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "O MEU FUNIL CABE EM 4 PASSOS: CONTEÚDO, DIRECT, CONVERSA E VENDA."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "O QUE EU VEJO",
   "texto": "O DONO POSTA E FICA ESPERANDO A PESSOA PERGUNTAR O PREÇO.", "destaque": "O FUNIL DELE PARA NO PRIMEIRO PASSO."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "CONTEÚDO QUE PEDE UMA PALAVRA"], ["esp", 8],
   ["n", "Todo post termina com 1 pedido: comente uma palavra ou mande uma mensagem."],
   ["n", "Exemplo ilustrativo de um personal: carrossel sobre dor nas costas de quem passa o dia sentado, fechando com \"Comente COSTAS\"."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "DIRECT EM 3 MENSAGENS CURTAS"], ["esp", 8],
   ["n", "1: o nome da pessoa. 2: \"Vi que você comentou COSTAS, obrigado.\" 3: \"Hoje você faz alguma coisa para isso?\""],
   ["n", "Três balões curtos e uma pergunta só. John Franklin, da Two-Brain Business (04/08/2026), recomenda o mesmo para donos de academia."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "CONVITE COM DIA E HORA"], ["esp", 8],
   ["n", "Quando a pessoa contar o problema, ofereça horário fechado: \"Tenho terça às 12h ou quinta às 18h para uma avaliação de 30 minutos. Qual fica melhor?\""],
   ["n", "Na véspera, confirme com uma mensagem curta."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "A VENDA ACONTECE NA CONVERSA"], ["esp", 8],
   ["n", "Na avaliação: o objetivo, o que está travando, o plano e o preço. Uma oferta só."],
   ["n", "Se a resposta for \"agora não\": \"Posso te procurar daqui a 2 meses?\" Anote na agenda e cumpra."]]},
  {"tipo": "branco", "blocos": [
   ["h", "A CONTA DA ROTINA"], ["esp", 8],
   ["n", "3 conversas novas por dia. 3 × 7 × 52 = 1.092 conversas num ano (a conta é da Two-Brain Business)."],
   ["n", "Exemplo ilustrativo: se 1 em cada 10 conversas vira avaliação e 1 em cada 3 avaliações vira aluno, são cerca de 36 alunos novos no ano."]]},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE ESCREVE AS SUAS 3 PRIMEIRAS MENSAGENS.",
   "destaque": "EM QUE PASSO O SEU FUNIL PARA?"},
]}

# 5) 19:10 LEGENDA (fotos reais do Liuri, foto preenchida), bandeira falada, CTA = ENVIO + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), HP("70")], "foco": [0.2, 0.3], "textos": ["Eu acho que o seu negócio", "não precisa de Black Friday."]},
 {"fotos": [FL("home-office-headset"), HP("73")], "foco": [0.35, 0.3], "textos": ["Desconto enche a agenda uma semana.", "Quem paga a conta é o seu mês."]},
 {"fotos": [FL("lagoa-biceps-de-frente"), HP("46")], "foco": [0.3, 0.3], "textos": ["O personal dá 30% no plano", "para quem já ia renovar."]},
 {"fotos": [FL("selfie-jaqueta-verde"), HP("32")], "foco": [0.3, 0.25], "textos": ["A fisio corta o preço da sessão", "e trabalha mais para ganhar o mesmo."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-3"), HP("60")], "foco": [0.2, 0.3], "textos": ["O barbeiro faz corte a 10 €", "e o cliente de sempre paga menos."]},
 {"fotos": [FL("selfie-sem-camisa-serio"), HP("66")], "foco": [0.3, 0.6], "textos": ["Eu já comprei um carro de 450 €.", "Durou 2 meses."]},
 {"fotos": [f"{R}/assets/foto-perfil-liuri.jpg", HP("05")], "foco": [0.3, 0.35], "textos": ["Hoje: troque o desconto", "por um bônus que custa pouco a você."]},
 {"fotos": [f"{R}/assets/avatar-liuri.jpg", FL("dunas-punhos-camisa-preta-2")], "foco": [0.3, 0.2], "textos": ["Envie para quem vai dar desconto", "e comente CLIENTES."]},
]}

# 6) 20:30 FAIXA, CONEXÃO (família), CTA = COMENTÁRIO + CLIENTES
filho = {"slides": [
  {"tipo": "foto", "foto": HP("32"), "foco_y": 0.25, "grande": True, "arraste": True,
   "faixa": "AERONÁUTICA",
   "texto": "O MEU PRIMEIRO FILHO NASCEU QUANDO EU AINDA VESTIA A FARDA."},
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.3, "faixa": "FOI NESTA ORDEM",
   "texto": "UM ANO DE NAMORO, UM ANO DE NOIVADO.", "destaque": "CASEI UM ANO DEPOIS DA FORMATURA."},
  {"tipo": "foto", "foto": HP("04"), "foco_y": 0.2, "faixa": "UM ANO DEPOIS",
   "texto": "NASCEU O PRIMEIRO FILHO.", "destaque": "EU AINDA ESTAVA NA AERONÁUTICA."},
  {"tipo": "foto", "foto": HP("61"), "foco_y": 0.15, "faixa": "O QUE MUDA",
   "texto": "A CONTA DE CASA DEIXA DE SER SÓ SUA.", "destaque": "TEM ALGUÉM QUE DEPENDE DELA TODO MÊS."},
  {"tipo": "foto", "foto": HP("41"), "foco_y": 0.3, "faixa": "NA FARDA",
   "texto": "PASSEI A GANHAR SALÁRIOS MELHORES.", "destaque": "MAS EU QUERIA CONSTRUIR ALGO MEU."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.6, "faixa": "DEPOIS",
   "texto": "SAÍ DA AERONÁUTICA, FIZ UBER E VIM PARA PORTUGAL.", "destaque": "A FAMÍLIA VEIO 3 MESES DEPOIS."},
  {"tipo": "branco", "blocos": [
   ["h", "QUEM TEM FAMÍLIA PRECISA DE UMA RETIRADA FIXA."], ["esp", 8],
   ["n", "Defina um valor que sai da conta da empresa para a sua no mesmo dia, todo mês. O resto fica na empresa."],
   ["n", "Exemplo ilustrativo de um barbeiro que fatura 3.000 € com 1.200 € de custos: retirada fixa de 1.300 € no dia 5. Os 500 € que sobram ficam na empresa para o mês fraco."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTO VOCÊ TIRA DA EMPRESA POR MÊS. EU TE CHAMO NO DIRECT.",
   "destaque": "A SUA RETIRADA TEM DIA MARCADO?"},
]}

# 7) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = ENVIO + CLIENTES
promessa = {"slides": [
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM QUEM PROMETE O SEU FATURAMENTO."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "POR QUE EU DIGO ISSO",
   "texto": "EM 2026 EU SAÍ DE 1.500 € PARA 7.000 € POR MÊS.", "destaque": "FAZENDO SOZINHO O CONTEÚDO, OS ANÚNCIOS E O ATENDIMENTO."},
  {"tipo": "foto", "foto": P("4854263"), "foco_y": 0.4, "faixa": "O QUE EU VEJO",
   "texto": "O PERSONAL QUE PAGOU POR \"10 ALUNOS EM 30 DIAS\".", "destaque": "E NÃO GRAVOU UM VÍDEO."},
  {"tipo": "foto", "foto": P("41122206"), "foco_y": 0.4, "faixa": "E TAMBÉM",
   "texto": "O BARBEIRO QUE COMPROU UM CURSO DE ANÚNCIOS.", "destaque": "E NUNCA LIGOU A CAMPANHA."},
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.3, "faixa": "O QUE A FARDA ME ENSINOU",
   "texto": "DISCIPLINA É ROTINA REPETIDA, TODO DIA.", "destaque": "NINGUÉM FAZ ISSO POR VOCÊ."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "O QUE EU FAÇO NO LUGAR",
   "texto": "NA MENTORIA EU PROMETO A ENTREGA.", "destaque": "EM 30 DIAS: OFERTA REVISTA, PERFIL AJUSTADO, FUNIL, 1ª CAMPANHA E SCRIPT DE ATENDIMENTO."},
  {"tipo": "branco", "blocos": [
   ["h", "ANTES DE PAGAR QUALQUER MENTOR, PERGUNTE 3 COISAS."], ["esp", 8],
   ["n", "1. O que eu recebo pronto em 30 dias? 2. Quem corrige o que eu fizer errado, e quando? 3. Quanto tempo por dia eu preciso dar?"],
   ["n", "Se a resposta for só um número de faturamento, desconfie. Na minha, a resposta da 3 é: pelo menos 2 horas por dia."]]},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM VAI CONTRATAR ALGUÉM",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E TE DIGO O QUE EU ENTREGO.",
   "destaque": "SEM PROMESSA DE NÚMERO."},
]}

LEGENDAS = {
 1: """71% já usaram IA para decidir uma compra. O seu próximo cliente pode estar perguntando por você ao ChatGPT.

O Observatório IPAM ouviu 1.208 residentes em Portugal com 18 anos ou mais, de 28 de outubro a 12 de novembro. 71% usaram IA para decidir uma compra nos últimos 6 meses. Entre eles, 88% usam o ChatGPT, 45% o Gemini e 31% a Meta AI.

O detalhe que quase ninguém leu: 52% já pegaram a IA com informação errada, desatualizada ou contraditória. Por isso 46% confirmam sempre ou quase sempre noutra fonte, e as mais usadas são o site oficial da marca (91%) e a avaliação de outros clientes (71%). Só 15% deixariam a IA fechar a compra sozinha. A amostra não é probabilística, então os números são indicativos.

O que eu acredito: quem só diz "chama no direct" sai da comparação. A pessoa e a IA comparam o que está escrito.

Exemplo ilustrativo de uma barbearia. Antes, na bio: "Agende já". Depois: "Corte + barba 25 €. Terça a sábado, das 9h às 20h. Plano mensal 60 €." E 10 avaliações no Google de clientes desta semana.

Faça hoje, em menos de 1 hora:
1. Serviços com preço, ou "a partir de", no Perfil da Empresa no Google.
2. A mesma lista num destaque do Instagram.
3. Peça avaliação a 5 clientes desta semana, com o link pronto no WhatsApp.

🔻 Envie para quem tem negócio. E comente CLIENTES que eu te chamo no direct e te digo o que um cliente encontra hoje quando procura por você.

Fontes: Jornal Económico com Lusa ("Observatório IPAM: Consumidores usam IA nas compras mas 65% não deixa operação concluir sozinha", 25/11/2026); PME Magazine (Daniela Felício, "IA já influencia decisões de compra e coloca novo desafio às PME", 25/11/2026).

#inteligenciaartificial #donodenegocio #barbearia #personaltrainer #fisioterapia""",
 2: """Conseguimos o quarto no mesmo dia em que a minha família chegou.

Eu vim antes, sozinho, com 300 €. Até eles chegarem, 3 meses depois, eu trabalhava 12 horas por dia e ainda vendia a folga.

Morávamos os três num quarto. Já tínhamos um bebê e o segundo filho estava a caminho. Aquele foi o ano mais difícil da nossa vida. Depois a gente juntou dinheiro e só então mudou para uma casa.

O que eu levo disso para a empresa: primeiro junta, depois muda.

Antes de trocar de espaço, contratar ou comprar equipamento, separe uma parte de cada pagamento numa conta que você não mexe. Exemplo ilustrativo de um personal que fatura 2.500 € por mês: 10% de cada pagamento são 250 € por mês. Em 6 meses, 1.500 € guardados antes de assinar o aluguel de um estúdio.

🔻 Salve para fazer a sua conta. E comente CLIENTES que eu te chamo no direct e a gente vê quanto o seu negócio consegue guardar.

#brasileirosemportugal #historiareal #empreendedorismo #personaltrainer #donodenegocio""",
 3: """Na quarentena da Aeronáutica eu aprendi a valorizar um banho.

Foram 40 a 45 dias longe da família, no começo. Muito grito, muita correria, troca de farda. Um banho passou a ter outro valor. Foi ali que eu amadureci.

A gente só percebe o básico quando ele falta. O seu cliente também.

Resposta que demora um dia. Horário que ninguém confirma. Sessão que acaba sem a próxima marcada.

O teste do básico, em 1 semana: anote em quanto tempo você responde uma mensagem nova, quantos clientes recebem confirmação na véspera e quantos saem da sessão com a próxima marcada.

Exemplo ilustrativo de uma fisio: responde em 5 horas, confirma 4 de 20 e marca a próxima com 6 de 20. Meta da semana: responder em até 1 hora, confirmar 20 de 20 e marcar a próxima antes do paciente sair.

🔻 Comente CLIENTES e o seu tempo de resposta de hoje. Eu te chamo no direct.

Fotos: Robério Castro Fotografia.

#aeronautica #disciplina #atendimento #fisioterapia #donodenegocio""",
 4: """O meu funil cabe em 4 passos: conteúdo, direct, conversa e venda.

O que eu mais vejo: o dono posta e fica esperando a pessoa perguntar o preço. O funil dele para no primeiro passo.

1. Conteúdo que pede uma palavra. Exemplo ilustrativo de um personal: carrossel sobre dor nas costas de quem passa o dia sentado, fechando com "Comente COSTAS".
2. Direct em 3 mensagens curtas: o nome da pessoa; "Vi que você comentou COSTAS, obrigado"; "Hoje você faz alguma coisa para isso?".
3. Convite com dia e hora: "Tenho terça às 12h ou quinta às 18h para uma avaliação de 30 minutos. Qual fica melhor?" Na véspera, confirme.
4. A venda acontece na conversa: o objetivo, o que está travando, o plano e o preço. Uma oferta só. Se a resposta for "agora não", pergunte se pode procurar daqui a 2 meses, anote e cumpra.

A conta da rotina: 3 conversas novas por dia são 1.092 conversas num ano. Exemplo ilustrativo: se 1 em cada 10 vira avaliação e 1 em cada 3 avaliações vira aluno, são cerca de 36 alunos novos no ano.

Os passos 2 e 3 seguem o que John Franklin, da Two-Brain Business, recomenda para donos de academia ("How to Sell Gym Memberships in Your DMs", 04/08/2026).

🔻 Salve para montar o seu. E comente CLIENTES que eu te chamo no direct e a gente escreve as suas 3 primeiras mensagens.

#funildevendas #personaltrainer #academia #fisioterapia #donodenegocio""",
 5: """Eu acho que o seu negócio não precisa de Black Friday.

Desconto enche a agenda uma semana e quem paga a conta é o seu mês. O personal dá 30% no plano para quem já ia renovar. A fisio corta o preço da sessão e trabalha mais para ganhar o mesmo. O barbeiro faz corte a 10 € e o cliente de sempre paga menos.

Eu já comprei um carro de 450 €. Durou 2 meses.

Hoje: troque o desconto por um bônus que custa pouco a você.

🔻 Envie para quem vai dar desconto amanhã. E comente CLIENTES que eu te chamo no direct.

Fotos: Robério Castro Fotografia.

#blackfriday #preco #donodenegocio #personaltrainer #barbearia""",
 6: """O meu primeiro filho nasceu quando eu ainda vestia a farda.

Foi nesta ordem: um ano de namoro, um ano de noivado, casei um ano depois da formatura e, um ano depois, nasceu o primeiro filho. Eu ainda estava na Aeronáutica.

A conta de casa deixa de ser só sua. Tem alguém que depende dela todo mês.

Na farda eu passei a ganhar salários melhores, mas eu queria construir algo meu. Saí, fiz Uber e vim para Portugal. A família veio 3 meses depois.

O que eu aprendi: quem tem família precisa de uma retirada fixa. Um valor que sai da conta da empresa para a sua no mesmo dia, todo mês. O resto fica na empresa.

Exemplo ilustrativo de um barbeiro que fatura 3.000 € com 1.200 € de custos: retirada fixa de 1.300 € no dia 5. Os 500 € que sobram ficam na empresa para o mês fraco.

🔻 Comente CLIENTES e quanto você tira da empresa por mês. Eu te chamo no direct.

Fotos: Robério Castro Fotografia.

#paiempreendedor #aeronautica #gestaofinanceira #historiareal #donodenegocio""",
 7: """Eu não acredito em quem promete o seu faturamento.

Em 2026 eu saí de 1.500 € para 7.000 € por mês, fazendo sozinho o conteúdo, os anúncios e o atendimento. Ninguém fez isso por mim.

O que eu vejo: o personal que pagou por "10 alunos em 30 dias" e não gravou um vídeo. O barbeiro que comprou um curso de anúncios e nunca ligou a campanha.

A farda me ensinou que disciplina é rotina repetida, todo dia.

Na mentoria eu prometo a entrega. Em 30 dias: oferta revista, perfil ajustado, funil montado, primeira campanha no ar e script de atendimento. O número é a meta que a gente persegue junto.

Antes de pagar qualquer mentor, pergunte 3 coisas:
1. O que eu recebo pronto em 30 dias?
2. Quem corrige o que eu fizer errado, e quando?
3. Quanto tempo por dia eu preciso dar?

Se a resposta for só um número de faturamento, desconfie. Na minha, a resposta da 3 é: pelo menos 2 horas por dia.

🔻 Envie para quem vai contratar alguém. E comente CLIENTES que eu te chamo no direct e te digo o que eu entrego.

#mentoria #donodenegocio #empreendedorismo #personaltrainer #barbearia""",
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
    for n in [1, 2, 3, 4, 5, 6, 7]:
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(noticia, O(1), "render_formatos.py")
    run(quarto, O(2)); run(banho, O(3)); run(funil, O(4))
    run(legenda, O(5), "render_legenda.py")
    run(filho, O(6))
    run(promessa, O(7))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
