"""Plano 100 mil, semana 4 do PDF (janela de testes, dia 7), 20/11/2026, sexta-feira. Dia 14 do "Plano de 30 dias para
lançar a mentoria": conteúdo "3 erros que vejo em perfis de negócio" (vira o VALOR das 17:40) e tarefa "Revisão da semana 2" (no doc).
Grade do playbook (ajustes de 10/11, 16/11, 18/11 e 19/11 prevalecem sobre a tarefa agendada): 7 posts, sem post de IA.
Sexta: 10:30 NOTÍCIA · 12:40 CONEXÃO · 14:20 CONEXÃO (remodelado) · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 PROVA · 22:15 BANDEIRA.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
Fotos: só do Liuri (sem a ex-esposa, regra de 19/11); nenhum frame de vídeo (18/11). Indicação: 0 de 7 posts.
O print revolut-recebido-600 NÃO foi usado: a categoria no print é "Carregamentos" para a conta "Pessoal" (pode ser movimento
interno, regra do playbook: nunca apresentar como venda). Perguntar ao dono no doc.
CTA (rodízio sobre 19/11, todos terminam em "Comente CLIENTES"):
10:30 salvar · 12:40 comentário · 14:20 salvar · 17:40 envio · 19:10 comentário · 20:30 envio · 22:15 comentário.
1) 10:30 NOTÍCIA: Meta lança o app Direct (O Tempo, Pollyana Sales, 18/11/2026; Agência O Globo, 18/11/2026).
2) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): "Antes dos testes eu disse: vou ser escolhido e vou estar entre os melhores."
   Item 6 (gancho novo: a frase dita antes do alistamento; o 13º só como fato).
3) 14:20 FAIXA, conexão, pilar 6 (lição pilar 4): "Hoje eu tenho reserva de emergência. Nem sempre foi assim." Itens 21, 13, 18 e 13a.
   REMODELADO de liurialves:6afd28f7fc933ac285c3b63b ("3 meses sem cortar o cabelo", 291 views, ainda não replicado):
   mesmo arco (detalhe de dinheiro pessoal em Lisboa → lição de gestão), gancho novo (reserva), fotos novas, lição nova (10% para a reserva).
4) 17:40 FAIXA, valor com rosto, pilar 1: os 3 erros do perfil (plano 30 dias, dia 14) + PT Distinction (Tim Saye, 20/06/2024).
5) 19:10 LEGENDA, bandeira falada, pilar 2: quem demora a responder perde para quem responde primeiro.
6) 20:30 CAPA + ESCURO, prova, pilar 5 (lição pilar 1): 252 € em anúncios → 1.755 € em atendimentos (15 a 31/10/2026). Sem print
   (o print dessa campanha não está na pasta prova-social): prova de processo com o número do playbook.
7) 22:15 FAIXA, bandeira, pilar 2: "Eu não acredito em curso gravado para destravar negócio parado." Fato: item 13a (loja).
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/6e678910-7709-5c92-ab8d-e61d4361a063/scratchpad"
DIA = "2026-11-20"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h20/{x}.jpg"           # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px20/pexels-{x}.jpg"

# 1) 10:30 NOTÍCIA, CAPA + ESCURO, CTA = SALVAR + CLIENTES
noticia = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": P("7342998"), "foco_y": 0.45, "etiqueta": "Notícia",
   "titulo": "A Meta criou um app só para o direct. Lá, quem não te conhece não começa conversa.",
   "sub": "O Tempo e Agência O Globo, 18/11/2026. O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O que foi lançado", "frase": "O [[Direct]], um app separado do Instagram.",
   "texto": "Começou aos poucos em [[2 países]], Turquia e Tailândia, no Android e no iPhone. Ainda não há previsão para o Brasil."},
  {"etiqueta": "O que quase ninguém leu", "frase": "Só [[contatos e conexões]] podem iniciar uma conversa.",
   "texto": "Quem não te conhece não consegue te chamar nem te pôr num grupo. A Meta diz que o app é para relações próximas."},
  {"etiqueta": "Como funciona", "frase": "Entra com a [[mesma conta]] e as conversas vêm junto.",
   "texto": "Também aceita cadastro só com e-mail ou telefone. Idade mínima: 13 anos. Tem notas, figurinhas, efeitos de voz e desenho no chat."},
  {"etiqueta": "O que eu acredito", "frase": "Quem espera o cliente [[chamar primeiro]] vai esperar mais.",
   "texto": "Não sei se o Direct chega a Portugal ou ao Brasil. Mas a conversa está ficando entre quem já se conhece. O seu trabalho é fazer a pessoa te conhecer antes de precisar de você."},
  {"etiqueta": "No seu negócio", "frase": "Faça o cliente [[abrir a conversa]] com você.",
   "texto": "Exemplo ilustrativo: o personal fecha o vídeo com \"comente TREINO que eu te mando os horários\". A fisio, \"comente DOR\". A barbearia, \"comente CORTE\". Quem comenta abre a porta; você responde no direct."},
  {"etiqueta": "Faça hoje", "frase": "[[1 palavra]] no fim dos próximos 3 posts.",
   "texto": "Ponha a palavra no último slide e na legenda. Responda cada comentário no direct em até 1 hora, com uma pergunta: \"Qual é o seu objetivo para os próximos 3 meses?\""},
  {"etiqueta": "Próximo passo", "frase": "Salve e [[comente CLIENTES]].",
   "texto": "Eu te chamo no direct e a gente escolhe a palavra do seu negócio."},
]}

# 2) 12:40 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
escolhido = {"slides": [
  {"tipo": "foto", "foto": HP("49"), "foco_y": 0.25, "grande": True, "arraste": True,
   "faixa": "AOS 18 ANOS, NO ALISTAMENTO",
   "texto": "ANTES DOS TESTES EU DISSE: VOU SER ESCOLHIDO E VOU ESTAR ENTRE OS MELHORES."},
  {"tipo": "foto", "foto": HP("37"), "foco_y": 0.35, "faixa": "DE ONDE VEIO",
   "texto": "O MEU PAI SEMPRE ACONSELHOU A AERONÁUTICA.", "destaque": "NO DIA DO ALISTAMENTO, EU DISSE QUE QUERIA SERVIR."},
  {"tipo": "foto", "foto": HP("09"), "foco_y": 0.45, "faixa": "O RESTO DA FRASE",
   "texto": "\"E A GENTE VAI MUDAR DE VIDA.\"", "destaque": "EU FALEI ANTES DE SABER SE IA PASSAR."},
  {"tipo": "foto", "foto": HP("44"), "foco_y": 0.45, "faixa": "OS TESTES FÍSICOS",
   "texto": "PASSEI COMO O 13º MELHOR.", "destaque": "DEPOIS, NOS MÉDICOS. E ENTREI."},
  {"tipo": "foto", "foto": HP("32"), "foco_y": 0.25, "faixa": "O PREÇO",
   "texto": "40 A 45 DIAS DE QUARENTENA LONGE DA FAMÍLIA.", "destaque": "DEPOIS, SALÁRIOS MELHORES."},
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.3, "faixa": "O QUE EU APRENDI ALI",
   "texto": "EU DECIDI ANTES DE TER O RESULTADO.", "destaque": "E FALEI EM VOZ ALTA."},
  {"tipo": "branco", "blocos": [
   ["h", "META SEM NÚMERO É SÓ VONTADE."], ["esp", 8],
   ["n", "Muito dono parado no mesmo faturamento diz \"quero crescer\" e não diz quanto nem até quando."],
   ["n", "Faça hoje: escreva a meta de dezembro em clientes, não em euros. Exemplo ilustrativo de um personal: 6 planos novos até 31/12. Divida por 4 semanas: 2 por semana. Diga isso em voz alta a alguém que vai te perguntar na sexta."]]},
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E A SUA META DE DEZEMBRO EM NÚMERO DE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE DIVIDE POR SEMANA.",
   "destaque": "QUANTOS CLIENTES ATÉ 31/12?"},
]}

# 3) 14:20 FAIXA, CONEXÃO (REMODELADO), CTA = SALVAR + CLIENTES
reserva = {"slides": [
  {"tipo": "foto", "foto": HP("69"), "foco_y": 0.5, "grande": True, "arraste": True, "faixa": "LISBOA, 2026",
   "texto": "HOJE EU TENHO RESERVA DE EMERGÊNCIA. NEM SEMPRE FOI ASSIM."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.6, "faixa": "COMO EU CHEGUEI",
   "texto": "SOZINHO, COM 300 €."},
  {"tipo": "foto", "foto": FL("carro-painel-rua"), "foco_y": 0.5, "faixa": "O PRIMEIRO ANO",
   "texto": "EU PRECISAVA DE 800 A 900 € POR MÊS.", "destaque": "RECEBIA 700 €."},
  {"tipo": "foto", "foto": P("4969835"), "foco_y": 0.4, "faixa": "COMO A CONTA FECHAVA",
   "texto": "UM GERENTE AMIGO ME EMPRESTAVA DINHEIRO TODO MÊS."},
  {"tipo": "foto", "foto": HP("05"), "foco_y": 0.35, "faixa": "ANTES, NO BRASIL",
   "texto": "A MINHA LOJA DE MODA PRAIA VENDIA NO VERÃO.", "destaque": "QUEBROU NA COVID, SEM RESERVA."},
  {"tipo": "foto", "foto": FL("cafe-pastel-pao-de-queijo"), "foco_y": 0.45, "faixa": "HOJE",
   "texto": "NÃO PRECISO OLHAR O PREÇO NO SUPERMERCADO.", "destaque": "E ESTOU CONSTRUINDO PATRIMÔNIO."},
  {"tipo": "branco", "blocos": [
   ["h", "O MÊS BOM PRECISA PAGAR O MÊS RUIM."], ["esp", 8],
   ["n", "Academia também tem verão e inverno. Nos dados da Wodify (mais de 5.000 negócios de fitness, 2023 e 2024), janeiro e junho trazem mais alunos; novembro e dezembro têm o pior saldo."],
   ["n", "Faça hoje: abra uma conta só para a reserva e mande para ela 10% de cada pagamento. Exemplo ilustrativo de uma barbearia que fatura 3.000 €: 300 € por mês, 1.800 € em 6 meses."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE CALCULA QUANTOS MESES O SEU NEGÓCIO AGUENTA.",
   "destaque": "QUANTOS MESES O SEU AGUENTA?"},
]}

# 4) 17:40 FAIXA, VALOR COM ROSTO, CTA = ENVIO + CLIENTES
perfil = {"slides": [
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "OS 3 ERROS QUE EU MAIS VEJO EM PERFIL DE NEGÓCIO. DÁ PARA CORRIGIR EM 1 HORA."},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.35, "faixa": "O QUE EU ACREDITO",
   "texto": "O PERFIL É A SUA RECEPÇÃO.", "destaque": "QUEM ENTRA E NÃO ENTENDE SAI SEM PERGUNTAR."},
  {"tipo": "branco", "blocos": [
   ["t", "ERRO 1"], ["h", "A BIO DIZ O QUE VOCÊ É, NÃO O QUE RESOLVE"], ["esp", 8],
   ["n", "\"Personal trainer | Lisboa\" não diz para quem é nem o que muda."],
   ["n", "Modelo em 3 linhas (exemplo ilustrativo): Para quem: \"Homens 35+ que pararam de treinar\". O que muda: \"45 min, 3x por semana, sem dor nas costas\". O que fazer: \"Avaliação: toque no WhatsApp\"."]]},
  {"tipo": "branco", "blocos": [
   ["t", "ERRO 2"], ["h", "NÃO HÁ UM JEITO ÓBVIO DE COMPRAR"], ["esp", 8],
   ["n", "Link com 8 botões, ou nenhum. A pessoa desiste no meio."],
   ["n", "Faça: 1 link só, direto para o seu WhatsApp com a mensagem pronta. Formato: wa.me/351XXXXXXXXX?text=Quero marcar uma avaliação. E o botão de contato do perfil ligado."]]},
  {"tipo": "branco", "blocos": [
   ["t", "ERRO 3"], ["h", "NINGUÉM SABE COMO FUNCIONA NEM QUANTO CUSTA"], ["esp", 8],
   ["n", "Destaques \"Treinos\", \"Alunos\", \"Viagem\". Falta o que a pessoa pergunta antes de comprar."],
   ["n", "Crie o destaque COMECE AQUI com 4 stories: 1. para quem é; 2. como é a primeira semana; 3. a partir de quanto custa; 4. como marcar. Deixe em primeiro."]]},
  {"tipo": "branco", "blocos": [
   ["t", "NO SEU NEGÓCIO"], ["h", "TROQUE SÓ AS PALAVRAS"], ["esp", 8],
   ["n", "Fisioterapia: \"Dor lombar que não passa? Avaliação em 40 minutos.\""],
   ["n", "Barbearia: \"Corte e barba em 45 min, sem fila. Marque pelo WhatsApp.\" Academia: \"Aula experimental às terças e quintas.\" (exemplos ilustrativos)"]]},
  {"tipo": "foto", "foto": P("15226555"), "foco_y": 0.45, "faixa": "DE ONDE VEM",
   "texto": "A PT DISTINCTION ENSINA PERSONAL TRAINERS A DIZER NA BIO O QUE FAZEM, PARA QUEM E QUE PROBLEMA RESOLVEM, EM ATÉ 150 CARACTERES.",
   "destaque": "(TIM SAYE, PT DISTINCTION, 20/06/2024)"},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM TEM PERFIL E NÃO TEM CLIENTE",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E OLHO A SUA BIO COM VOCÊ.",
   "destaque": "QUAL DOS 3 ESTÁ NO SEU PERFIL?"},
]}

# 5) 19:10 LEGENDA (fotos reais do Liuri), bandeira falada, CTA = COMENTÁRIO + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("home-office-headset"), HP("49")], "foco": [0.3, 0.25], "textos": ["Eu acho que quem demora a responder", "perde o cliente para quem responde primeiro."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), FL("carro-painel-rua")], "foco": [0.2, 0.5], "textos": ["Quem pede preço no direct", "quase nunca pede só para você."]},
 {"fotos": [FL("lagoa-biceps-de-frente-editada"), HP("60")], "foco": [0.35, 0.3], "textos": ["O personal responde à noite,", "o aluno já marcou de manhã com outro."]},
 {"fotos": [HP("05"), FL("selfie-jaqueta-verde")], "foco": [0.35, 0.3], "textos": ["A fisio retorna no dia seguinte,", "a dor já foi tratada noutro lugar."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-2"), HP("37")], "foco": [0.2, 0.35], "textos": ["O barbeiro vê a mensagem às 20h,", "o cliente cortou às 18h."]},
 {"fotos": [HP("71"), FL("selfie-sem-camisa-serio")], "foco": [0.3, 0.35], "textos": ["Ninguém fica esperando a sua resposta.", "Quem responde antes marca antes."]},
 {"fotos": [FL("home-office-headset"), HP("32")], "foco": [0.3, 0.25], "textos": ["Hoje, salve 3 respostas rápidas no WhatsApp Business:", "preço, horários e endereço."]},
 {"fotos": [HP("69"), FL("dunas-punhos-camisa-preta-3")], "foco": [0.5, 0.2], "textos": ["Quanto tempo você leva para responder?", "Comente CLIENTES."]},
]}

# 6) 20:30 CAPA + ESCURO, PROVA, CTA = ENVIO + CLIENTES
prova = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "etiqueta": "Prova",
   "titulo": "Coloquei 252 € em anúncios. Voltaram 1.755 € em atendimentos.",
   "sub": "De 15 a 31/10/2026, anúncio de mensagem feito por mim. E a conta que eu faço antes de pôr mais 1 €."},
  {"etiqueta": "O que foi", "frase": "[[252 €]] em anúncios de mensagem.",
   "texto": "De 15 a 31 de outubro de 2026. O anúncio levava a pessoa direto para uma conversa comigo no WhatsApp."},
  {"etiqueta": "O que voltou", "frase": "[[1.755 €]] em atendimentos.",
   "texto": "No mesmo período. Fazendo a conta: cada 1 € de anúncio voltou como cerca de 6,96 € em atendimentos."},
  {"etiqueta": "O que eu acredito", "frase": "Serviço de confiança se vende [[numa conversa]].",
   "texto": "Quem nunca te viu não compra no primeiro clique. Mas responde a uma pergunta. Por isso o anúncio abria o WhatsApp, e não uma página de compra."},
  {"etiqueta": "A conta que quase ninguém faz", "frase": "Quanto volta por [[cada 1 €]]?",
   "texto": "Muito dono de negócio olha só o preço da mensagem. A pergunta que paga a conta é outra: quanto entrou em atendimentos por cada euro do anúncio."},
  {"etiqueta": "No seu negócio", "frase": "[[3 colunas]] numa folha.",
   "texto": "Conversa que entrou · marcou avaliação · pagou. Exemplo ilustrativo de um personal: 20 conversas, 6 avaliações, 3 planos de 160 €. 480 € de entrada."},
  {"etiqueta": "Faça esta semana", "frase": "Anote [[toda conversa]] que vier do anúncio.",
   "texto": "No fim de 7 dias, divida o que entrou pelo que você gastou. Se o número for baixo, troque o vídeo antes de subir o orçamento."},
  {"etiqueta": "Próximo passo", "frase": "Envie para quem acha que anúncio não funciona e [[comente CLIENTES]].",
   "texto": "Eu te chamo no direct e a gente monta a sua folha de 3 colunas."},
]}

# 7) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = COMENTÁRIO + CLIENTES
curso = {"slides": [
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente"), "foco_y": 0.35, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM CURSO GRAVADO PARA DESTRAVAR NEGÓCIO PARADO."},
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.3, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "NO TEMPO DA AERONÁUTICA EU ABRI UMA LOJA DE MODA PRAIA.", "destaque": "INVESTI ENTRE 10 E 12 MIL REAIS. ELA QUEBROU."},
  {"tipo": "foto", "foto": FL("cafe-tapioca-mesa-casa"), "foco_y": 0.45, "faixa": "O ERRO",
   "texto": "ESTAVA NUM DETALHE: A CONTA DA LOJA ERA A MESMA DA CASA.", "destaque": "O DINHEIRO DELA FOI EM VIAGENS E CONTAS."},
  {"tipo": "foto", "foto": P("5725612"), "foco_y": 0.4, "faixa": "O QUE O VÍDEO NÃO FAZ",
   "texto": "NENHUM VÍDEO ABRE O SEU EXTRATO.", "destaque": "CADA AULA ENSINA UMA COISA E NÃO CONTINUA A OUTRA."},
  {"tipo": "foto", "foto": P("6455895"), "foco_y": 0.4, "faixa": "O QUE EU VEJO",
   "texto": "O PERSONAL QUE ASSISTIU A AULAS DE TRÁFEGO O ANO TODO E NUNCA LIGOU UM ANÚNCIO."},
  {"tipo": "foto", "foto": P("5152514"), "foco_y": 0.45, "faixa": "E TAMBÉM",
   "texto": "O BARBEIRO QUE COMPROU O CURSO DE PREÇO E COBRA O MESMO HÁ 2 ANOS."},
  {"tipo": "branco", "blocos": [
   ["h", "INFORMAÇÃO SÓ VIRA RESULTADO QUANDO ALGUÉM OLHA O DETALHE COM VOCÊ."], ["esp", 8],
   ["n", "Até lá, comece pelo que já está no seu celular."],
   ["n", "Faça esta semana: escolha UMA coisa que você aprendeu e nunca aplicou. Ponha uma data, aplique e anote o número antes e depois. Exemplo ilustrativo de uma fisio: mensagem 24 h depois da sessão. Antes, quantos voltaram? Em 2 semanas, quantos?"]]},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E O QUE VOCÊ APRENDEU E NUNCA APLICOU. EU TE CHAMO NO DIRECT E A GENTE PÕE UMA DATA.",
   "destaque": "QUANTAS AULAS ESTÃO PARADAS NO SEU CELULAR?"},
]}

LEGENDAS = {
 1: """A Meta criou um app só para o direct. Lá, quem não te conhece não começa conversa.

O app se chama Direct. Foi anunciado esta semana e começou aos poucos na Turquia e na Tailândia, no Android e no iPhone, sem previsão para o Brasil. Quem tem Instagram entra com a mesma conta e as conversas vêm junto; também dá para entrar só com e-mail ou telefone. Idade mínima: 13 anos.

O detalhe que quase ninguém leu: só contatos e conexões podem iniciar uma conversa ou te pôr num grupo. A Meta diz que o app é para relações próximas.

O que eu acredito: quem espera o cliente chamar primeiro vai esperar mais. Não sei se o Direct chega a Portugal ou ao Brasil, mas a conversa está ficando entre quem já se conhece. O seu trabalho é fazer a pessoa te conhecer antes de precisar de você.

No seu negócio, faça o cliente abrir a conversa. Exemplo ilustrativo: o personal fecha o vídeo com "comente TREINO que eu te mando os horários". A fisio, "comente DOR". A barbearia, "comente CORTE".

Faça hoje: 1 palavra no fim dos próximos 3 posts, no último slide e na legenda. Responda cada comentário no direct em até 1 hora, com uma pergunta: "Qual é o seu objetivo para os próximos 3 meses?"

🔻 Salve e comente CLIENTES. Eu te chamo no direct e a gente escolhe a palavra do seu negócio.

Fontes: O Tempo (Pollyana Sales, 18/11/2026) e Agência O Globo (18/11/2026); Portal Publicitário (Felipe Martins, 17/11/2026).

#instagram #donodenegocio #personaltrainer #fisioterapia #barbearia""",
 2: """Antes dos testes eu disse: vou ser escolhido e vou estar entre os melhores.

Aos 18 anos, no alistamento. O meu pai sempre aconselhou a Aeronáutica, e no dia eu disse que queria servir. A frase completa foi: "Vou entrar na Aeronáutica, vou ser escolhido, vou estar entre os melhores e a gente vai mudar de vida." Eu falei antes de saber se ia passar.

Passei nos testes físicos como o 13º melhor, passei nos médicos e entrei. Depois vieram 40 a 45 dias de quarentena longe da família, e depois salários melhores.

O que eu aprendi ali: decidir antes de ter o resultado, e falar em voz alta.

Muito dono parado no mesmo faturamento diz "quero crescer" e não diz quanto nem até quando. Faça hoje: escreva a meta de dezembro em clientes, não em euros. Exemplo ilustrativo de um personal: 6 planos novos até 31/12. Divida por 4 semanas: 2 por semana. Diga isso em voz alta a alguém que vai te perguntar na sexta.

🔻 Comente CLIENTES e a sua meta de dezembro em número de clientes. Eu te chamo no direct e a gente divide por semana.

Fotos da Aeronáutica: Robério Castro Fotografia.

#aeronautica #historiareal #metas #donodenegocio #brasileirosemportugal""",
 3: """Hoje eu tenho reserva de emergência. Nem sempre foi assim.

Cheguei a Lisboa sozinho, com 300 €. No primeiro ano eu precisava de 800 a 900 € por mês e recebia 700 €. Um gerente amigo me emprestava dinheiro todo mês. Antes disso, no Brasil, a minha loja de moda praia vendia no verão e quebrou na Covid, sem reserva.

Hoje eu não preciso olhar o preço no supermercado, e estou construindo patrimônio.

O mês bom precisa pagar o mês ruim. Academia também tem verão e inverno: nos dados da Wodify, com mais de 5.000 negócios de fitness (2023 e 2024), janeiro e junho trazem mais alunos, e novembro e dezembro têm o pior saldo.

Faça hoje: abra uma conta só para a reserva e mande para ela 10% de cada pagamento. Exemplo ilustrativo de uma barbearia que fatura 3.000 €: 300 € por mês, 1.800 € em 6 meses.

🔻 Salve e comente CLIENTES. Eu te chamo no direct e a gente calcula quantos meses o seu negócio aguenta.

#reservadeemergencia #gestaofinanceira #donodenegocio #brasileirosemportugal #personaltrainer""",
 4: """Os 3 erros que eu mais vejo em perfil de negócio. Dá para corrigir em 1 hora.

O perfil é a sua recepção. Quem entra e não entende sai sem perguntar.

Erro 1: a bio diz o que você é, não o que resolve. "Personal trainer | Lisboa" não diz para quem é nem o que muda. Modelo em 3 linhas (exemplo ilustrativo): para quem ("Homens 35+ que pararam de treinar"), o que muda ("45 min, 3x por semana, sem dor nas costas") e o que fazer ("Avaliação: toque no WhatsApp").

Erro 2: não há um jeito óbvio de comprar. Deixe 1 link só, direto para o seu WhatsApp com a mensagem pronta (wa.me/351XXXXXXXXX?text=Quero marcar uma avaliação), e o botão de contato ligado.

Erro 3: ninguém sabe como funciona nem quanto custa. Crie o destaque COMECE AQUI com 4 stories: para quem é, como é a primeira semana, a partir de quanto custa e como marcar. Deixe em primeiro.

Na fisio: "Dor lombar que não passa? Avaliação em 40 minutos." Na barbearia: "Corte e barba em 45 min, sem fila." Na academia: "Aula experimental às terças e quintas."

A PT Distinction ensina personal trainers a dizer na bio o que fazem, para quem e que problema resolvem, em até 150 caracteres (Tim Saye, 20/06/2024).

🔻 Envie para quem tem perfil e não tem cliente. E comente CLIENTES que eu te chamo no direct e olho a sua bio com você.

#instagramparanegocios #personaltrainer #fisioterapia #barbearia #donodenegocio""",
 5: """Quem demora a responder perde o cliente para quem responde primeiro.

Quem pede preço no direct quase nunca pede só para você. O personal responde à noite, e o aluno já marcou de manhã com outro. A fisio retorna no dia seguinte, e a dor já foi tratada noutro lugar. O barbeiro vê a mensagem às 20h, e o cliente cortou às 18h.

Hoje: salve 3 respostas rápidas no WhatsApp Business, com preço, horários e endereço.

🔻 Comente CLIENTES e quanto tempo você leva para responder. Eu te chamo no direct.

#atendimento #whatsappbusiness #donodenegocio #personaltrainer #barbearia""",
 6: """Coloquei 252 € em anúncios. Voltaram 1.755 € em atendimentos.

Foi de 15 a 31 de outubro de 2026, com anúncio de mensagem feito por mim. O anúncio levava a pessoa direto para uma conversa comigo no WhatsApp. Fazendo a conta: cada 1 € de anúncio voltou como cerca de 6,96 € em atendimentos.

O que eu acredito: serviço de confiança se vende numa conversa. Quem nunca te viu não compra no primeiro clique, mas responde a uma pergunta.

A conta que quase ninguém faz: quanto volta por cada 1 €. Muito dono de negócio olha só o preço da mensagem.

No seu negócio, 3 colunas numa folha: conversa que entrou, marcou avaliação, pagou. Exemplo ilustrativo de um personal: 20 conversas, 6 avaliações, 3 planos de 160 €, 480 € de entrada.

Faça esta semana: anote toda conversa que vier do anúncio. No fim de 7 dias, divida o que entrou pelo que gastou. Se o número for baixo, troque o vídeo antes de subir o orçamento.

🔻 Envie para quem acha que anúncio não funciona. E comente CLIENTES que eu te chamo no direct e a gente monta a sua folha de 3 colunas.

#anuncios #metaads #donodenegocio #personaltrainer #fisioterapia""",
 7: """Eu não acredito em curso gravado para destravar negócio parado.

No tempo da Aeronáutica eu abri uma loja de moda praia. Investi entre 10 e 12 mil reais, e ela quebrou na Covid. O erro estava num detalhe: a conta da loja era a mesma da casa, e o dinheiro dela foi em viagens e contas.

Nenhum vídeo abre o seu extrato. Cada aula ensina uma coisa e não continua a outra.

O que eu vejo: o personal que assistiu a aulas de tráfego o ano todo e nunca ligou um anúncio. O barbeiro que comprou o curso de preço e cobra o mesmo há 2 anos.

Informação só vira resultado quando alguém olha o detalhe com você. Até lá, comece pelo que já está no seu celular.

Faça esta semana: escolha UMA coisa que você aprendeu e nunca aplicou. Ponha uma data, aplique e anote o número antes e depois. Exemplo ilustrativo de uma fisio: mensagem 24 h depois da sessão. Antes, quantos voltaram? Em 2 semanas, quantos?

🔻 Comente CLIENTES e o que você aprendeu e nunca aplicou. Eu te chamo no direct e a gente põe uma data.

Foto da Aeronáutica: arquivo pessoal.

#donodenegocio #empreendedorismo #gestao #barbearia #personaltrainer""",
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
    run(escolhido, O(2)); run(reserva, O(3)); run(perfil, O(4))
    run(legenda, O(5), "render_legenda.py")
    run(prova, O(6), "render_formatos.py")
    run(curso, O(7))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
