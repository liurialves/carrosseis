"""Plano 100 mil, semana 5 do PDF (leitura e corte, dia 5), 25/11/2026, quarta. Dia 19 do "Plano de 30 dias para lançar
a mentoria": conteúdo "Bastidores: hoje começa o desafio" (entra na bandeira das 22:15) e tarefa "Aula 1 do desafio" (no doc).
Grade do playbook (ajustes de 10/11, 16/11, 18/11, 19/11 e 23/11 prevalecem sobre a tarefa agendada): 7 posts, sem post de IA.
Quarta: 10:30 NOTÍCIA · 12:40 CONEXÃO (remodelado) · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 PROVA · 22:15 BANDEIRA.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
Fotos: só do Liuri (sem a ex-esposa), nenhum frame de vídeo. Indicação: 0 de 7 posts.
CTA (rodízio sobre 24/11, todos terminam em "Comente CLIENTES"):
10:30 comentário · 12:40 envio · 14:20 salvar · 17:40 comentário · 19:10 salvar · 20:30 envio · 22:15 comentário.
1) 10:30 NOTÍCIA: DECO PROteste, Black Friday 2026 (24/11/2026) + Sebrae/RS na Mix Vale (Carolina Costa, 18/11/2026).
2) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): ajudante de personal numa academia de elite cujo dono já não conseguia pagar. Item 2.
   REMODELADO de liurialves:6affcd64738ce4635f883105 ("Antes dos testes eu disse...", 20/11 12:40, 129 de alcance, 269 views,
   o carrossel com mais alcance ainda não replicado): mesma fase (18 anos) e arco; trecho, capa, fotos, lição e CTA novos.
3) 14:20 FAIXA, conexão, pilar 5 (lição pilar 3): massagem + sites, as duas coisas que ele já sabia fazer. Item 20 + 13 + Cuidados.
4) 17:40 FAIXA, valor com rosto, pilar 1: os últimos 30 clientes (Physitrack, 07/08/2026).
5) 19:10 LEGENDA, bandeira falada, pilar 2: o seu cliente não sabe o que você vende.
6) 20:30 FAIXA, PROVA, pilar 5 (lição pilar 3): 48.000 € em 2026 com duas plataformas (telas da capa do dono + print Stripe 9,90 €).
7) 22:15 FAIXA, bandeira, pilar 6: "Eu não acredito em meta sem data." Item 22 + hoje começa o Desafio 6 semanas.
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/3d9e8bf7-f171-5ad8-8a79-9c137b44f2dc/scratchpad"
DIA = "2026-11-25"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h25/{x}.jpg"           # fotos/historia-portugal e prints (Drive), baixados nesta execução
P = lambda x: f"/tmp/px25/pexels-{x}.jpg"

# 1) 10:30 NOTÍCIA, CAPA + ESCURO, CTA = COMENTÁRIO + CLIENTES
noticia = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": P("7564159"), "foco_y": 0.5, "etiqueta": "Notícia",
   "titulo": "Nesta Black Friday, 26% de quem já comprava vai gastar menos. O motivo muda a sua oferta.",
   "sub": "DECO PROteste (24/11/2026). O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O número", "frase": "[[75%]] dos portugueses planeiam comprar.",
   "texto": "Inquérito online da DECO PROteste, com 2.000 respostas de pessoas dos 18 aos 74 anos, feito de 12 a 20 de outubro. No ano passado eram 74%. O orçamento médio é de 289 €."},
  {"etiqueta": "O que quase ninguém leu", "frase": "Entre quem repete, [[26% vai gastar menos]].",
   "texto": "60% vão gastar o mesmo e só 14% vão gastar mais. Quem corta aponta a inflação (50%) ou a situação financeira (42%)."},
  {"etiqueta": "E tem mais", "frase": "[[78%]] desconfiam dos descontos anunciados.",
   "texto": "E mesmo assim 67% dizem que vale a pena comprar. A pessoa compra, mas compara tudo antes de pagar."},
  {"etiqueta": "O que eu acredito", "frase": "Quem compara precisa de [[clareza]], não de mais desconto.",
   "texto": "Quando o dinheiro aperta, o cliente não some. Ele escolhe com mais cuidado. Leva quem mostra o que está incluído, quanto custa e até quando vale."},
  {"etiqueta": "No seu negócio", "frase": "Troque o \"20% off\" pelo que a pessoa [[leva]].",
   "texto": "Exemplo ilustrativo de um personal. Antes: \"Black Friday, 20% no plano\". Depois: \"Avaliação + 8 treinos + plano por escrito, 160 €, até domingo\". O Sebrae/RS (Mix Vale, 18/11/2026) também recomenda mostrar preço, validade e o que entra na promoção."},
  {"etiqueta": "Faça hoje", "frase": "A sua oferta em [[3 linhas]].",
   "texto": "Linha 1: o que a pessoa leva. Linha 2: o preço. Linha 3: até quando vale. Publique nos Stories e deixe a mesma mensagem nas respostas rápidas do WhatsApp."},
  {"etiqueta": "Próximo passo", "frase": "[[Comente CLIENTES]] e a sua oferta em 1 linha.",
   "texto": "Eu te chamo no direct e te digo se ela passa no teste das 3 linhas."},
]}

# 2) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = ENVIO + CLIENTES
academia = {"slides": [
  {"tipo": "foto", "foto": HP("47"), "foco_y": 0.25, "grande": True, "arraste": True,
   "faixa": "AOS 18 ANOS",
   "texto": "EU ERA AJUDANTE DE PERSONAL NUMA ACADEMIA DE ELITE. O DONO JÁ NÃO CONSEGUIA PAGAR."},
  {"tipo": "foto", "foto": HP("33"), "foco_y": 0.2, "faixa": "EU TINHA DOIS TRABALHOS",
   "texto": "JOVEM APRENDIZ NUMA CORRETORA E AJUDANTE DE PERSONAL.", "destaque": "OS DOIS ENQUANTO EU TERMINAVA A ESCOLA."},
  {"tipo": "foto", "foto": P("29495718"), "foco_y": 0.5, "faixa": "A ACADEMIA",
   "texto": "ERA PERSONALIZADA E DE ELITE.", "destaque": "E O DONO JÁ NÃO CONSEGUIA PAGAR O AJUDANTE."},
  {"tipo": "foto", "foto": P("4164765"), "foco_y": 0.45, "faixa": "AO MESMO TEMPO",
   "texto": "O CONTRATO DE 1 ANO NA CORRETORA ACABOU.", "destaque": "FIQUEI SEM OS DOIS TRABALHOS."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "O QUE EU ENTENDI DEPOIS",
   "texto": "EQUIPAMENTO NÃO PAGA SALÁRIO.", "destaque": "QUEM PAGA É O ALUNO QUE CONTINUA TODO MÊS."},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente"), "foco_y": 0.3, "faixa": "O QUE EU VEJO HOJE",
   "texto": "O DONO SABE QUANTO CUSTOU O EQUIPAMENTO.", "destaque": "E NÃO SABE QUANTOS ALUNOS PAGAM O MÊS."},
  {"tipo": "branco", "blocos": [
   ["h", "FAÇA A CONTA DO SEU PONTO DE EQUILÍBRIO."], ["esp", 8],
   ["n", "Some o custo fixo do mês: aluguel, salários, sistema, luz e a sua retirada. Divida pelo que sobra de cada aluno depois do custo dele."],
   ["n", "Exemplo ilustrativo de um estúdio: 3.600 € de custo fixo ÷ 60 € que sobram por aluno = 60 alunos. Só do 61º em diante é que sobra dinheiro."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM TEM ACADEMIA OU ESTÚDIO",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE FAZ A SUA CONTA.",
   "destaque": "QUANTOS ALUNOS PAGAM O SEU MÊS?"},
]}

# 3) 14:20 FAIXA, CONEXÃO, CTA = SALVAR + CLIENTES
duas = {"slides": [
  {"tipo": "foto", "foto": HP("69"), "foco_y": 0.55, "grande": True, "arraste": True,
   "faixa": "LISBOA, 2026",
   "texto": "EM 2026 EU JUNTEI DUAS COISAS QUE EU JÁ SABIA FAZER: MASSAGEM E SITE."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.35, "faixa": "DEPOIS DE 2 ANOS DE UBER",
   "texto": "EU QUERIA GANHAR MAIS E MUDAR DE VIDA.", "destaque": "E OLHEI PARA O QUE EU JÁ SABIA FAZER."},
  {"tipo": "foto", "foto": HP("40"), "foco_y": 0.3, "faixa": "A PRIMEIRA",
   "texto": "MASSAGEM. FIZ O CURSO EM 2017, JUNTO COM A AERONÁUTICA.", "destaque": "E DEIXEI PARADA POR ANOS."},
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.5, "faixa": "A SEGUNDA",
   "texto": "MARKETING. O MEU PRIMEIRO TRABALHO EM PORTUGAL FOI COM MARKETING DIGITAL.", "destaque": "NUM INTERCÂMBIO DE 2 MESES."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "EM 2026",
   "texto": "VOLTEI PARA A MASSAGEM E COMECEI A CRIAR SITES PARA CLIENTES.", "destaque": "UM DELES FOI O DA CAROLWELL."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-1"), "foco_y": 0.2, "faixa": "O RESULTADO",
   "texto": "SAÍ DE 1.500 € PARA 7.000 € POR MÊS.", "destaque": "A HABILIDADE ESTAVA COMIGO HAVIA ANOS."},
  {"tipo": "branco", "blocos": [
   ["h", "O QUE VOCÊ JÁ SABE FAZER E NÃO VENDE?"], ["esp", 8],
   ["n", "Escreva 3 coisas que os clientes já te pedem e que você faz de graça ou nem oferece."],
   ["n", "Exemplo ilustrativo de uma fisio: ela passa exercício para casa de graça no fim da sessão. Isso vira um plano de 4 semanas com 1 revisão por vídeo, por 60 €, oferecido no fim de cada tratamento."]]},
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE ACHA O SERVIÇO QUE VOCÊ JÁ TEM PARADO.",
   "destaque": "QUAL É O SEU?"},
]}

# 4) 17:40 FAIXA, VALOR COM ROSTO, CTA = COMENTÁRIO + CLIENTES
trinta = {"slides": [
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "ABRA A LISTA DOS SEUS ÚLTIMOS 30 CLIENTES. A SUA PRÓXIMA OFERTA ESTÁ LÁ."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "O QUE EU ACREDITO",
   "texto": "VOCÊ NÃO PRECISA DE CLIENTE NOVO PARA DESCOBRIR O QUE VENDER.", "destaque": "QUEM JÁ PAGOU TE DIZ."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "LISTE OS ÚLTIMOS 30"], ["esp", 8],
   ["n", "Numa folha ou planilha só sua, 3 colunas: o que cada um comprou, quanto pagou e se voltou."],
   ["n", "Os nomes ficam com você. O que importa são as 3 colunas."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "CIRCULE OS 5 MELHORES"], ["esp", 8],
   ["n", "Os que pagaram mais e voltaram mais vezes."],
   ["n", "Exemplo ilustrativo de uma fisio: dos 30 pacientes, 5 fecharam pacote de 8 sessões e 4 deles são corredores."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "ESCREVA O QUE ELES TÊM EM COMUM"], ["esp", 8],
   ["n", "O problema, o objetivo, a faixa de idade e o horário que preferem."],
   ["n", "No exemplo: corredores de 30 a 45 anos, com dor no joelho, que treinam de manhã."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "REESCREVA A BIO E A OFERTA PARA ELES"], ["esp", 8],
   ["n", "\"Fisioterapia para corredores com dor no joelho. Pacote de 8 sessões com plano de volta à corrida. Mande JOELHO.\""],
   ["n", "Copie e troque pelo seu caso: o barbeiro com cliente de barba toda semana, o personal com aluno acima dos 40."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 5"], ["h", "OS PRÓXIMOS 4 POSTS FALAM SÓ DISSO"], ["esp", 8],
   ["n", "1 erro que esse cliente comete, 1 exercício ou dica, 1 história de quem você atendeu (com autorização) e 1 convite com a oferta."],
   ["n", "A Physitrack, plataforma para fisioterapeutas, recomenda o mesmo ponto de partida: olhar os últimos 30 pacientes antes de escolher o nicho."]]},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E QUEM SÃO OS SEUS 5 MELHORES CLIENTES. EU TE CHAMO NO DIRECT.",
   "destaque": "O QUE ELES TÊM EM COMUM?"},
]}

# 5) 19:10 LEGENDA (fotos reais do Liuri, foto preenchida), bandeira falada, CTA = SALVAR + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("lagoa-biceps-de-frente"), HP("72")], "foco": [0.3, 0.5], "textos": ["Eu acho que o seu cliente", "não sabe o que você vende."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), HP("69")], "foco": [0.2, 0.5], "textos": ["Ele vê o seu trabalho", "e não vê a sua oferta."]},
 {"fotos": [FL("home-office-headset"), HP("46")], "foco": [0.35, 0.3], "textos": ["O personal posta o treino", "e nunca posta o plano."]},
 {"fotos": [FL("selfie-sem-camisa-serio"), HP("47")], "foco": [0.3, 0.3], "textos": ["A fisio posta o exercício", "e não diz como marcar."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-2"), HP("05")], "foco": [0.2, 0.4], "textos": ["O barbeiro posta o corte", "e esconde o preço do plano."]},
 {"fotos": [HP("40"), HP("67")], "foco": [0.35, 0.3], "textos": ["Eu passei anos com a massagem", "parada, sem oferecer a ninguém."]},
 {"fotos": [FL("selfie-jaqueta-verde"), HP("33")], "foco": [0.3, 0.2], "textos": ["Hoje: 1 post com o que você vende,", "para quem e quanto custa."]},
 {"fotos": [f"{R}/assets/foto-perfil-liuri.jpg", FL("dunas-punhos-camisa-preta-3")], "foco": [0.3, 0.2], "textos": ["Salve para postar hoje", "e comente CLIENTES."]},
]}

# 6) 20:30 FAIXA, PROVA, CTA = ENVIO + CLIENTES
prova = {"slides": [
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "grande": True, "arraste": True,
   "faixa": "PROVA · 2026",
   "texto": "COMECEI 2026 COM 1.500 € POR MÊS. ATÉ AQUI JÁ SÃO 48.000 €."},
  {"tipo": "foto", "foto": HP("print-48mil-telas"), "foco_y": 0.3, "faixa": "AS DUAS PLATAFORMAS",
   "texto": "LISBOA MASSAGEM E MEDPORTUGAL.", "destaque": "AS DUAS CONSTRUÍDAS DO ZERO."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.3, "faixa": "A PRIMEIRA",
   "texto": "A LISBOA MASSAGEM TEM MAIS DE 90 TERAPEUTAS.", "destaque": "EM PORTUGAL."},
  {"tipo": "foto", "foto": P("20860614"), "foco_y": 0.35, "faixa": "A SEGUNDA",
   "texto": "A MEDPORTUGAL JUNTA PROFISSIONAIS DE SAÚDE.", "destaque": "OSTEOPATIA, FISIOTERAPIA, NUTRIÇÃO E PERSONAL TRAINER."},
  {"tipo": "foto", "foto": HP("print-stripe"), "foco_y": 0.3, "faixa": "O QUE ENTRA SEM EU ATENDER",
   "texto": "AS PLATAFORMAS COBRAM ASSINATURA.", "destaque": "ESTE PAGAMENTO DE 9,90 € CHEGOU NUM DOMINGO."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "COMO EU FIZ",
   "texto": "SOZINHO: O CONTEÚDO, OS ANÚNCIOS E O ATENDIMENTO.", "destaque": "A MINHA VIDA MUDOU ESTE ANO, COM A MINHA ATITUDE."},
  {"tipo": "branco", "blocos": [
   ["h", "RECEITA QUE SE REPETE MUDA O SEU MÊS."], ["esp", 8],
   ["n", "Quem paga avulso decide de novo a cada vez. Quem paga por mês já decidiu."],
   ["n", "Exemplo ilustrativo de um personal: em vez de 35 € por treino, plano de 8 treinos por 240 € por mês, no débito automático. Ofereça primeiro a quem já treina com você há mais de 2 meses."]]},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM AINDA COBRA AVULSO",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE MONTA O SEU PLANO MENSAL.",
   "destaque": "QUANTO ENTRA FIXO NO SEU MÊS?"},
]}

# 7) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = COMENTÁRIO + CLIENTES
meta = {"slides": [
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM META SEM DATA."},
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.5, "faixa": "A MINHA TEM DATA",
   "texto": "100 MIL EUROS POR MÊS, AINDA EM 2027.", "destaque": "É A MINHA META. EU DIGO EM VOZ ALTA."},
  {"tipo": "foto", "foto": P("37963578"), "foco_y": 0.4, "faixa": "O QUE EU VEJO",
   "texto": "O PERSONAL QUE QUER \"CRESCER ESTE ANO\".", "destaque": "E NÃO SABE QUANTOS ALUNOS ISSO SIGNIFICA."},
  {"tipo": "foto", "foto": P("39559269"), "foco_y": 0.4, "faixa": "E TAMBÉM",
   "texto": "O BARBEIRO QUE VAI \"ORGANIZAR AS CONTAS\".", "destaque": "UM DIA."},
  {"tipo": "foto", "foto": P("20860612"), "foco_y": 0.4, "faixa": "E AINDA",
   "texto": "A FISIO QUE VAI \"POSTAR MAIS\".", "destaque": "A PARTIR DA SEMANA QUE VEM."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "O QUE EU FAÇO NO LUGAR",
   "texto": "HOJE COMEÇA O MEU DESAFIO DE 6 SEMANAS.", "destaque": "A DATA FOI MARCADA ANTES. HOJE É O DIA."},
  {"tipo": "branco", "blocos": [
   ["h", "ESCREVA A SUA META COM 3 COISAS."], ["esp", 8],
   ["n", "1. O número: alunos, clientes ou euros. 2. A data. 3. A primeira ação de amanhã, com hora marcada."],
   ["n", "Exemplo ilustrativo de um personal: \"De 18 para 25 alunos até 31 de janeiro. Amanhã, 8h: mensagem para 10 ex-alunos.\" Deixe num lugar onde você olhe todo dia."]]},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "COMENTE CLIENTES",
   "texto": "E A SUA META COM NÚMERO E DATA. EU TE CHAMO NO DIRECT.",
   "destaque": "QUAL É A SUA DATA?"},
]}

LEGENDAS = {
 1: """Nesta Black Friday, 26% de quem já comprava vai gastar menos. O motivo muda a sua oferta.

A DECO PROteste ouviu 2.000 pessoas dos 18 aos 74 anos, de 12 a 20 de outubro. 75% planeiam comprar (no ano passado eram 74%), com um orçamento médio de 289 €.

O detalhe que quase ninguém leu: entre quem repete, 60% vão gastar o mesmo, 26% vão gastar menos e só 14% vão gastar mais. Quem corta aponta a inflação (50%) ou a situação financeira (42%). E 78% desconfiam dos descontos anunciados, mesmo com 67% achando que vale a pena comprar.

O que eu acredito: quem compara precisa de clareza, não de mais desconto. Quando o dinheiro aperta, o cliente não some. Ele escolhe com mais cuidado.

Exemplo ilustrativo de um personal. Antes: "Black Friday, 20% no plano". Depois: "Avaliação + 8 treinos + plano por escrito, 160 €, até domingo". O Sebrae/RS também recomenda mostrar preço, validade e o que entra na promoção.

Faça hoje: a sua oferta em 3 linhas. O que a pessoa leva, o preço e até quando vale. Nos Stories e nas respostas rápidas do WhatsApp.

🔻 Comente CLIENTES e a sua oferta em 1 linha. Eu te chamo no direct e te digo se ela passa no teste das 3 linhas.

Fontes: DECO PROteste ("Black Friday 2026: 75% dos portugueses planeiam comprar, apesar da desconfiança nas promoções", 24/11/2026); Mix Vale (Carolina Costa, "Black Friday nas redes sociais tem sete estratégias do Sebrae para pequenos negócios...", 18/11/2026).

#blackfriday #donodenegocio #personaltrainer #barbearia #fisioterapia""",
 2: """Aos 18 anos eu era ajudante de personal numa academia de elite. O dono já não conseguia pagar.

Eu tinha dois trabalhos enquanto terminava a escola: jovem aprendiz numa corretora e ajudante de personal numa academia personalizada. O contrato de 1 ano da corretora acabou e, ao mesmo tempo, o dono da academia já não conseguia pagar o ajudante. Fiquei sem os dois trabalhos.

O que eu entendi depois: equipamento não paga salário. Quem paga é o aluno que continua todo mês.

O que eu vejo hoje: o dono sabe quanto custou o equipamento e não sabe quantos alunos pagam o mês.

Faça a conta do seu ponto de equilíbrio. Some o custo fixo do mês (aluguel, salários, sistema, luz e a sua retirada) e divida pelo que sobra de cada aluno depois do custo dele.

Exemplo ilustrativo de um estúdio: 3.600 € de custo fixo ÷ 60 € que sobram por aluno = 60 alunos. Só do 61º em diante é que sobra dinheiro.

🔻 Envie para quem tem academia ou estúdio. E comente CLIENTES que eu te chamo no direct e a gente faz a sua conta.

#academia #personaltrainer #gestaofinanceira #historiareal #donodenegocio""",
 3: """Em 2026 eu juntei duas coisas que eu já sabia fazer: massagem e site.

Depois de 2 anos de Uber, eu queria ganhar mais e mudar de vida. Olhei para o que eu já sabia fazer.

A primeira era a massagem. Fiz o curso em 2017, junto com a Aeronáutica, e deixei parada por anos. A segunda era o marketing: o meu primeiro trabalho em Portugal foi num intercâmbio de 2 meses com marketing digital.

Em 2026 eu voltei para a massagem e comecei a criar sites para clientes. Um deles foi o da Carolwell. Saí de 1.500 € para 7.000 € por mês. A habilidade estava comigo havia anos.

O dono de negócio parado muitas vezes já tem o serviço que vende melhor e não oferece.

Escreva 3 coisas que os clientes já te pedem e que você faz de graça ou nem oferece. Exemplo ilustrativo de uma fisio: ela passa exercício para casa de graça no fim da sessão. Isso vira um plano de 4 semanas com 1 revisão por vídeo, por 60 €, oferecido no fim de cada tratamento.

🔻 Salve para fazer a sua lista. E comente CLIENTES que eu te chamo no direct e a gente acha o serviço que você já tem parado.

Foto: Robério Castro Fotografia.

#empreendedorismo #brasileirosemportugal #historiareal #fisioterapia #donodenegocio""",
 4: """Abra a lista dos seus últimos 30 clientes. A sua próxima oferta está lá.

Você não precisa de cliente novo para descobrir o que vender. Quem já pagou te diz.

1. Liste os últimos 30 numa folha só sua, com 3 colunas: o que comprou, quanto pagou e se voltou.
2. Circule os 5 que pagaram mais e voltaram mais vezes. Exemplo ilustrativo de uma fisio: dos 30, 5 fecharam pacote de 8 sessões e 4 deles são corredores.
3. Escreva o que eles têm em comum: o problema, o objetivo, a faixa de idade e o horário. No exemplo: corredores de 30 a 45 anos, com dor no joelho, que treinam de manhã.
4. Reescreva a bio e a oferta para eles: "Fisioterapia para corredores com dor no joelho. Pacote de 8 sessões com plano de volta à corrida. Mande JOELHO."
5. Os próximos 4 posts falam só disso: 1 erro desse cliente, 1 exercício ou dica, 1 história de quem você atendeu (com autorização) e 1 convite com a oferta.

A Physitrack, plataforma para fisioterapeutas, recomenda o mesmo ponto de partida: olhar os últimos 30 pacientes antes de escolher o nicho ("How to Grow an Instagram Account as a Physical Therapist", 07/08/2026).

🔻 Comente CLIENTES e quem são os seus 5 melhores clientes. Eu te chamo no direct e a gente escreve a sua oferta para eles.

#fisioterapia #personaltrainer #barbearia #marketingdigital #donodenegocio""",
 5: """O seu cliente não sabe o que você vende.

Ele vê o seu trabalho e não vê a sua oferta. O personal posta o treino e nunca posta o plano. A fisio posta o exercício e não diz como marcar. O barbeiro posta o corte e esconde o preço do plano.

Eu passei anos com a massagem parada, sem oferecer a ninguém.

Hoje: 1 post com o que você vende, para quem e quanto custa.

🔻 Salve para postar hoje. E comente CLIENTES que eu te chamo no direct.

Foto: Robério Castro Fotografia.

#oferta #donodenegocio #personaltrainer #fisioterapia #barbearia""",
 6: """Comecei 2026 com 1.500 € por mês. Até aqui já são 48.000 €.

Foram duas plataformas que eu construí do zero. A Lisboa Massagem tem mais de 90 terapeutas em Portugal. A MedPortugal junta profissionais de saúde: osteopatia, fisioterapia, nutrição e personal trainer.

As plataformas cobram assinatura. No 5º slide está um pagamento de 9,90 € que chegou num domingo, sem eu atender ninguém.

Eu fiz sozinho o conteúdo, os anúncios e o atendimento. A minha vida mudou este ano, com a minha atitude.

O que eu aprendi: receita que se repete muda o seu mês. Quem paga avulso decide de novo a cada vez. Quem paga por mês já decidiu.

Exemplo ilustrativo de um personal: em vez de 35 € por treino, plano de 8 treinos por 240 € por mês, no débito automático. Ofereça primeiro a quem já treina com você há mais de 2 meses.

🔻 Envie para quem ainda cobra avulso. E comente CLIENTES que eu te chamo no direct e a gente monta o seu plano mensal.

#prova #empreendedorismo #personaltrainer #fisioterapia #donodenegocio""",
 7: """Eu não acredito em meta sem data.

A minha tem: 100 mil euros por mês, ainda em 2027. É a minha meta e eu digo em voz alta.

O que eu vejo: o personal que quer "crescer este ano" e não sabe quantos alunos isso significa. O barbeiro que vai "organizar as contas" um dia. A fisio que vai "postar mais" a partir da semana que vem.

O que eu faço no lugar: data marcada. Hoje, 25 de novembro, começa o meu Desafio de 6 semanas. A data foi marcada antes. Hoje é o dia.

Escreva a sua meta com 3 coisas:
1. O número: alunos, clientes ou euros.
2. A data.
3. A primeira ação de amanhã, com hora marcada.

Exemplo ilustrativo de um personal: "De 18 para 25 alunos até 31 de janeiro. Amanhã, 8h: mensagem para 10 ex-alunos." Deixe num lugar onde você olhe todo dia.

🔻 Comente CLIENTES e a sua meta com número e data. Eu te chamo no direct.

#metas #empreendedorismo #disciplina #personaltrainer #donodenegocio""",
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
    run(academia, O(2)); run(duas, O(3)); run(trinta, O(4))
    run(legenda, O(5), "render_legenda.py")
    run(prova, O(6))
    run(meta, O(7))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
