"""Plano 100 mil, semana 5 do PDF (leitura e corte, dia 4), 24/11/2026, terça. Dia 18 do "Plano de 30 dias para lançar
a mentoria": conteúdo "Baixar o preço pode quebrar o seu negócio" (vira o VALOR das 17:40, pilar 4) e tarefa "Fechar inscrições
e dar boas-vindas no grupo" (no doc; o Desafio 6 semanas começa amanhã, 25/11).
Grade do playbook (ajustes de 10/11, 16/11, 18/11, 19/11 e 23/11 prevalecem sobre a tarefa agendada): 7 posts, sem post de IA.
Terça: 10:30 NOTÍCIA · 12:40 CONEXÃO (remodelado) · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 CONEXÃO · 22:15 BANDEIRA.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
Fotos: só do Liuri (sem a ex-esposa), nenhum frame de vídeo. Indicação: 0 de 7 posts.
CTA (rodízio sobre 23/11, todos terminam em "Comente CLIENTES"):
10:30 salvar · 12:40 comentário · 14:20 envio · 17:40 salvar · 19:10 envio · 20:30 comentário · 22:15 salvar.
1) 10:30 NOTÍCIA: cobrança por mensagem de serviço na API do WhatsApp Business (O Tempo, 17/11/2026; Varejo S.A./CNDL, 09/11/2026;
   Tribuna de Jundiaí, Willian Porto, 21/09/2026, para a franquia e os balões).
2) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): "Por 3 meses eu comi pizza e lasanha de supermercado." Item 13.
   REMODELADO de liurialves:6afbd82885dca6b14a1ecbd5 ("Um gerente amigo me deu 100 €...", 17/11 14:20, 132 de alcance, 259 views,
   o carrossel com mais alcance ainda não replicado): mesma fase e arco; trecho, capa, fotos, lição e CTA novos.
3) 14:20 FAIXA, conexão, pilar 5 (lição pilar 1): "Fiquei em 13º no teste físico." Item 6 (+ 9).
4) 17:40 FAIXA, valor com rosto (A, dia par), pilar 4: a conta do desconto de 20% (plano 30 dias dia 18).
5) 19:10 LEGENDA, bandeira falada, pilar 1: negócio parado precisa de conversa, não de seguidor.
6) 20:30 FAIXA, conexão, pilar 5 (lição pilar 4): a loja de moda praia, negócio sazonal. Item 13a.
7) 22:15 FAIXA, bandeira, pilar 2: "Eu não acredito em aprender negócio com vídeo solto." Comparação YouTube (Documento de Clareza).
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/f85871af-1ed2-5182-89c8-d00f58b7a000/scratchpad"
DIA = "2026-11-24"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h24/{x}.jpg"           # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px24/pexels-{x}.jpg"

# 1) 10:30 NOTÍCIA, CAPA + ESCURO, CTA = SALVAR + CLIENTES
noticia = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": P("7342997"), "foco_y": 0.5, "etiqueta": "Notícia",
   "titulo": "R$ 0,035 por resposta no WhatsApp. E o app grátis que você usa ficou de fora.",
   "sub": "O Tempo (17/11/2026) e Varejo S.A., da CNDL (09/11/2026). O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O que mudou", "frase": "A resposta dentro das [[24 horas]] passou a ser cobrada.",
   "texto": "Desde 1º de outubro, quem usa a API oficial do WhatsApp Business paga por cada mensagem de serviço enviada na janela de 24 horas de atendimento. Vale para resposta de atendente, de robô ou de IA."},
  {"etiqueta": "O número", "frase": "No Brasil, [[US$ 0,0068]] por mensagem.",
   "texto": "Cerca de R$ 0,035, segundo a Varejo S.A., da CNDL. E o atendente de IA da própria Meta, o Meta Business Agent, já é cobrado desde 1º de agosto."},
  {"etiqueta": "O que quase ninguém leu", "frase": "No app grátis do celular [[nada muda]].",
   "texto": "A cobrança vale só para a API oficial, a que fica por trás de plataformas de atendimento e robôs. Quem usa o WhatsApp Business gratuito no celular não é afetado. A conversa que começa num anúncio de clique para o WhatsApp continua com 72 horas gratuitas."},
  {"etiqueta": "O que eu acredito", "frase": "Conversa comprida [[custa caro]] mesmo de graça.",
   "texto": "Eu vejo dono de academia mandar 6 mensagens antes de dizer o preço e o horário. No app grátis isso custa o seu tempo e o cliente. Na API, custa também por mensagem."},
  {"etiqueta": "No seu negócio", "frase": "Pergunte ao seu fornecedor [[uma coisa só]].",
   "texto": "Exemplo ilustrativo: a fisio usa uma plataforma de marcação com robô no WhatsApp. Pergunte se o número roda na API oficial. Se rodar, peça a conta das mensagens de outubro e veja quantas eram respostas repetidas."},
  {"etiqueta": "Faça hoje", "frase": "A resposta do preço [[em 1 balão]].",
   "texto": "Escreva a resposta para \"quanto custa?\" numa mensagem só: o que está incluído, o preço, 2 horários livres e uma pergunta no fim. Salve nas respostas rápidas do WhatsApp Business. Na API, dividir a resposta em vários balões pode contar como várias mensagens."},
  {"etiqueta": "Próximo passo", "frase": "Salve para revisar o seu atendimento e [[comente CLIENTES]].",
   "texto": "Eu te chamo no direct e a gente escreve a sua resposta de preço em 1 balão."},
]}

# 2) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = COMENTÁRIO + CLIENTES
pizza = {"slides": [
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "OS MEUS PRIMEIROS 3 MESES EM LISBOA",
   "texto": "POR 3 MESES EU COMI PIZZA E LASANHA DE SUPERMERCADO. ERA O QUE A CONTA DEIXAVA."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.55, "faixa": "COMO EU CHEGUEI",
   "texto": "VIM SOZINHO, COM 300 €.", "destaque": "PARA UM INTERCÂMBIO VOLUNTÁRIO DE 2 MESES."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.4, "faixa": "A CONTA",
   "texto": "NEM O CABELO EU PODIA CORTAR.", "destaque": "PIZZA E LASANHA DE SUPERMERCADO, TODO DIA."},
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.3, "faixa": "O TRABALHO",
   "texto": "NOS PRIMEIROS 5 MESES, 12 HORAS POR DIA.", "destaque": "E EU AINDA VENDIA A MINHA FOLGA."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "O QUE EU NÃO CORTEI",
   "texto": "CORTEI COMIDA, CABELO E FOLGA.", "destaque": "AS HORAS DE TRABALHO QUE PAGAVAM AS CONTAS EU NÃO CORTEI."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "O QUE EU VEJO HOJE",
   "texto": "O MÊS APERTA E O DONO CORTA O ANÚNCIO E O CONTEÚDO.", "destaque": "CORTA JUSTAMENTE O QUE TRAZ CLIENTE."},
  {"tipo": "branco", "blocos": [
   ["h", "ANTES DE CORTAR, SEPARE OS GASTOS EM 2 COLUNAS."], ["esp", 8],
   ["n", "Coluna 1: o que traz cliente (anúncio, conteúdo, a agenda online). Coluna 2: o que não traz (assinatura esquecida, material parado, taxa que ninguém revisou)."],
   ["n", "Exemplo ilustrativo de um barbeiro: 3 assinaturas que ninguém usa somam 47 € por mês. Corte a coluna 2 primeiro. Da coluna 1 só sai o que tiver o número dizendo que não trouxe ninguém."]]},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E O QUE VOCÊ CORTOU PRIMEIRO NO ÚLTIMO MÊS RUIM. EU TE CHAMO NO DIRECT.",
   "destaque": "O QUE FOI?"},
]}

# 3) 14:20 FAIXA, CONEXÃO, CTA = ENVIO + CLIENTES
teste = {"slides": [
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "AERONÁUTICA, AOS 18 ANOS",
   "texto": "FIQUEI EM 13º NO TESTE FÍSICO. O SEU CLIENTE TAMBÉM FAZ UM RANKING."},
  {"tipo": "foto", "foto": HP("09"), "foco_y": 0.45, "faixa": "O ALISTAMENTO",
   "texto": "ERA OBRIGATÓRIO. EU DISSE QUE QUERIA SERVIR.", "destaque": "O MEU PAI SEMPRE ACONSELHOU A AERONÁUTICA."},
  {"tipo": "foto", "foto": HP("41"), "foco_y": 0.35, "faixa": "ANTES DOS TESTES",
   "texto": "EU DISSE: VOU SER ESCOLHIDO E VOU ESTAR ENTRE OS MELHORES.", "destaque": "FALEI ANTES DE SABER O RESULTADO."},
  {"tipo": "foto", "foto": HP("11"), "foco_y": 0.25, "faixa": "O RESULTADO",
   "texto": "13º MELHOR NOS TESTES FÍSICOS.", "destaque": "PASSEI NOS MÉDICOS E ENTREI."},
  {"tipo": "foto", "foto": HP("13"), "foco_y": 0.4, "faixa": "O QUE EU VI ALI",
   "texto": "A VAGA ERA DISPUTADA. QUEM ESCOLHIA, COMPARAVA.", "destaque": "COM O SEU CLIENTE É IGUAL."},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "faixa": "O QUE EU VEJO HOJE",
   "texto": "O CLIENTE ABRE O SEU PERFIL E O DO CONCORRENTE NA MESMA HORA.", "destaque": "E ESCOLHE QUEM DEIXA TUDO MAIS CLARO."},
  {"tipo": "branco", "blocos": [
   ["h", "FAÇA O TESTE DO CLIENTE HOJE."], ["esp", 8],
   ["n", "Abra o seu perfil e o de 3 concorrentes da sua cidade, como se fosse cliente. Compare 3 coisas: em 5 segundos dá para saber o que você faz e para quem? Tem preço ou um \"a partir de\"? Tem um jeito claro de marcar?"],
   ["n", "Exemplo ilustrativo de um personal: o concorrente escreve \"Avaliação + plano de 4 semanas, a partir de 120 €. Mande AVALIAÇÃO\". O seu perfil só tem fotos de treino. Em que lugar você fica?"]]},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM TEM CONCORRENTE NA RUA",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E FAÇO O TESTE NO SEU PERFIL.",
   "destaque": "EM QUE LUGAR VOCÊ FICA?"},
]}

# 4) 17:40 FAIXA, VALOR COM ROSTO (A), CTA = SALVAR + CLIENTES
desconto = {"slides": [
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "ANTES DE DAR 20% DE DESCONTO NA BLACK FRIDAY, FAÇA ESTA CONTA."},
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "faixa": "O QUE EU ACREDITO",
   "texto": "O DESCONTO SAI INTEIRO DO QUE SOBRA PARA VOCÊ.", "destaque": "O SEU CUSTO CONTINUA IGUAL."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "ESCREVA O PREÇO E O CUSTO POR CLIENTE"], ["esp", 8],
   ["n", "Custo é o que sai do seu bolso para atender aquela pessoa: sala, material, comissão, taxa do cartão."],
   ["n", "Exemplo ilustrativo de um personal: plano de 200 € por mês e custo de 80 € por aluno. Sobram 120 €."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "TIRE O DESCONTO DO QUE SOBRA"], ["esp", 8],
   ["n", "Com 20% de desconto, o plano vai para 160 €. O custo continua 80 €."],
   ["n", "Sobram 80 € por aluno. O desconto de 20% no preço comeu 33% do que sobrava."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "QUANTOS CLIENTES A MAIS VOCÊ PRECISA"], ["esp", 8],
   ["n", "Conta: o que sobra hoje ÷ o que sobra com desconto."],
   ["n", "120 ÷ 80 = 1,5. Para sobrar o mesmo, 10 alunos viram 15. São 5 alunos a mais só para ficar no mesmo lugar."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "TROQUE O DESCONTO POR VALOR"], ["esp", 8],
   ["n", "Mantenha o preço e acrescente algo que custa pouco para você e vale muito para o cliente."],
   ["n", "Exemplo ilustrativo: avaliação extra, plano por escrito ou 1 sessão com a fisio parceira. Com prazo para fechar: domingo."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 5"], ["h", "A RESPOSTA PARA QUEM PEDE DESCONTO"], ["esp", 8],
   ["n", "\"Eu não mexo no preço, porque é ele que paga o meu acompanhamento. Quem fechar até domingo leva [bônus]. Quer que eu reserve a sua vaga?\""],
   ["n", "Copie, troque o bônus e deixe nas respostas rápidas do WhatsApp."]]},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente"), "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE FAZ A CONTA DO SEU DESCONTO.",
   "destaque": "QUANTOS CLIENTES A MAIS VOCÊ PRECISARIA?"},
]}

# 5) 19:10 LEGENDA (fotos reais do Liuri, foto preenchida), bandeira falada, CTA = ENVIO + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("selfie-sem-camisa-serio"), HP("70")], "foco": [0.3, 0.3], "textos": ["Eu acho que negócio parado", "não precisa de mais seguidor."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), HP("49")], "foco": [0.2, 0.25], "textos": ["Precisa de mais conversa", "começada por você."]},
 {"fotos": [FL("home-office-headset"), HP("40")], "foco": [0.4, 0.35], "textos": ["O personal com 3 mil seguidores", "recebe 2 mensagens por semana."]},
 {"fotos": [HP("71"), FL("lagoa-biceps-de-frente-editada")], "foco": [0.3, 0.35], "textos": ["A fisio posta todo dia", "e não pergunta nada a ninguém."]},
 {"fotos": [HP("05"), FL("dunas-punhos-camisa-preta-3")], "foco": [0.35, 0.25], "textos": ["O barbeiro espera o cliente", "lembrar que precisa cortar."]},
 {"fotos": [HP("72"), HP("66")], "foco": [0.45, 0.55], "textos": ["Nos meus primeiros meses em Lisboa", "eu vendia até a minha folga."]},
 {"fotos": [FL("selfie-jaqueta-verde"), HP("46")], "foco": [0.3, 0.3], "textos": ["Hoje: 10 conversas começadas por você.", "Sem oferta. Só uma pergunta."]},
 {"fotos": [f"{R}/assets/foto-perfil-liuri.jpg", HP("11")], "foco": [0.3, 0.25], "textos": ["Envie para quem está esperando o cliente", "e comente CLIENTES."]},
]}

# 6) 20:30 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
loja = {"slides": [
  {"tipo": "foto", "foto": HP("46"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "A MINHA PRIMEIRA EMPRESA",
   "texto": "A MINHA LOJA DE MODA PRAIA VENDIA NO VERÃO. O DINHEIRO DO VERÃO IA PARA CASA."},
  {"tipo": "foto", "foto": HP("49"), "foco_y": 0.25, "faixa": "NO TEMPO DE MILITAR",
   "texto": "ABRI UMA LOJA DE MODA PRAIA.", "destaque": "INVESTI ENTRE 10 E 12 MIL REAIS."},
  {"tipo": "foto", "foto": HP("05"), "foco_y": 0.35, "faixa": "O NEGÓCIO",
   "texto": "MODA PRAIA VENDE NUMA ÉPOCA DO ANO.", "destaque": "NO RESTO DO ANO, AS CONTAS CONTINUAM CHEGANDO."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-1"), "foco_y": 0.2, "faixa": "O MEU ERRO",
   "texto": "A CONTA DA LOJA E A DE CASA ERAM UMA SÓ.", "destaque": "O DINHEIRO DA LOJA PAGOU VIAGENS E CONTAS DE CASA."},
  {"tipo": "foto", "foto": FL("cafe-tapioca-mesa-casa"), "foco_y": 0.5, "faixa": "DEPOIS VEIO A COVID",
   "texto": "A LOJA QUEBROU.", "destaque": "E EU NÃO SABIA QUANTO ELA TINHA DADO DE VERDADE."},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "faixa": "O QUE EU VEJO HOJE",
   "texto": "ACADEMIA E PERSONAL TAMBÉM TÊM O SEU VERÃO.", "destaque": "NOVEMBRO E DEZEMBRO COSTUMAM SER OS MESES MAIS FRACOS."},
  {"tipo": "branco", "blocos": [
   ["h", "O MÊS BOM TEM QUE PAGAR O MÊS RUIM."], ["esp", 8],
   ["n", "Abra os últimos 12 meses e marque o pior. Esse é o mês que a sua reserva precisa cobrir."],
   ["n", "Exemplo ilustrativo de uma barbearia: custo fixo de 2.400 € por mês e dezembro com 1.600 € de entrada. Faltam 800 €. De março a novembro, separe 90 € por mês numa conta só da empresa."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E QUAL É O PIOR MÊS DO SEU NEGÓCIO. EU TE CHAMO NO DIRECT.",
   "destaque": "VOCÊ SABE QUAL É?"},
]}

# 7) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = SALVAR + CLIENTES
video = {"slides": [
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM APRENDER NEGÓCIO COM VÍDEO SOLTO."},
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.3, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "CADA VÍDEO ENSINA UMA COISA DIFERENTE.", "destaque": "E UM NÃO CONTINUA O OUTRO."},
  {"tipo": "foto", "foto": P("37963576"), "foco_y": 0.35, "faixa": "O QUE EU VEJO",
   "texto": "O PERSONAL QUE ASSISTIU 40 VÍDEOS DE ANÚNCIO.", "destaque": "E NUNCA SUBIU O PRIMEIRO."},
  {"tipo": "foto", "foto": P("9992818"), "foco_y": 0.35, "faixa": "E TAMBÉM",
   "texto": "O BARBEIRO COM 200 POSTS SALVOS.", "destaque": "E A MESMA BIO DE 2 ANOS ATRÁS."},
  {"tipo": "foto", "foto": P("20860580"), "foco_y": 0.4, "faixa": "E AINDA",
   "texto": "A FISIO QUE APRENDEU FUNIL NUMA SEMANA E PREÇO NA OUTRA.", "destaque": "E NÃO APLICOU NENHUM DOS DOIS."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "O QUE EU FAÇO NO LUGAR",
   "texto": "UMA COISA DE CADA VEZ, NA ORDEM.", "destaque": "OFERTA, PERFIL, CONVERSA E SÓ DEPOIS ANÚNCIO."},
  {"tipo": "branco", "blocos": [
   ["h", "ESCOLHA UMA COISA E EXECUTE ATÉ DOMINGO."], ["esp", 8],
   ["n", "Na ordem: 1. a oferta numa linha; 2. a bio com o que você faz, para quem e como marcar; 3. 10 conversas começadas por você; 4. só então o anúncio."],
   ["n", "Exemplo ilustrativo de um personal: esta semana é só a oferta. \"Avaliação + plano de 4 semanas para voltar a treinar sem dor, 120 €.\" Os vídeos ficam para depois de aplicar."]]},
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E TE DIGO POR ONDE COMEÇAR NO SEU NEGÓCIO.",
   "destaque": "EM QUAL DOS 4 VOCÊ ESTÁ?"},
]}

LEGENDAS = {
 1: """R$ 0,035 por resposta no WhatsApp. E o app grátis que você usa ficou de fora.

Desde 1º de outubro, quem usa a API oficial do WhatsApp Business paga por cada mensagem de serviço enviada na janela de 24 horas de atendimento, seja resposta de atendente, de robô ou de IA. No Brasil, US$ 0,0068 por mensagem, cerca de R$ 0,035. O Meta Business Agent, o atendente de IA da Meta, já é cobrado desde 1º de agosto.

O detalhe que quase ninguém leu: no app WhatsApp Business gratuito do celular nada muda. A cobrança é só na API, a que fica por trás de plataformas de atendimento e robôs. E a conversa que começa num anúncio de clique para o WhatsApp continua com 72 horas gratuitas.

O que eu acredito: conversa comprida custa caro mesmo de graça. Eu vejo dono de academia mandar 6 mensagens antes de dizer o preço e o horário.

Exemplo ilustrativo: a fisio usa uma plataforma de marcação com robô no WhatsApp. Pergunte ao fornecedor se o número roda na API oficial. Se rodar, peça a conta das mensagens de outubro.

Faça hoje: escreva a resposta para "quanto custa?" numa mensagem só (o que está incluído, o preço, 2 horários livres e uma pergunta no fim) e salve nas respostas rápidas. Na API, dividir a resposta em vários balões pode contar como várias mensagens.

🔻 Salve para revisar o seu atendimento. E comente CLIENTES que eu te chamo no direct e a gente escreve a sua resposta de preço em 1 balão.

Fontes: O Tempo ("WhatsApp mais caro: nova cobrança da Meta coloca eficiência do atendimento à prova", Edicase/Fernando Filho, 17/11/2026); Varejo S.A., da CNDL ("Empresas pagarão por cada resposta no WhatsApp Business", 09/11/2026); Tribuna de Jundiaí (Willian Porto, 21/09/2026).

#whatsappbusiness #atendimento #donodenegocio #personaltrainer #barbearia""",
 2: """Por 3 meses eu comi pizza e lasanha de supermercado. Era o que a conta deixava.

Vim para Lisboa sozinho, com 300 €, para um intercâmbio voluntário de 2 meses. Nem o cabelo eu podia cortar. Nos primeiros 5 meses trabalhei 12 horas por dia e ainda vendia a minha folga.

Cortei comida, cabelo e folga. As horas de trabalho que pagavam as contas eu não cortei.

O que eu vejo hoje: o mês aperta e o dono corta o anúncio e o conteúdo. Corta justamente o que traz cliente.

Antes de cortar, separe os gastos em 2 colunas. Coluna 1: o que traz cliente (anúncio, conteúdo, a agenda online). Coluna 2: o que não traz (assinatura esquecida, material parado, taxa que ninguém revisou).

Exemplo ilustrativo de um barbeiro: 3 assinaturas que ninguém usa somam 47 € por mês. Corte a coluna 2 primeiro. Da coluna 1 só sai o que tiver o número dizendo que não trouxe ninguém.

🔻 Comente CLIENTES e o que você cortou primeiro no último mês ruim. Eu te chamo no direct.

#empreendedorismo #brasileirosemportugal #historiareal #donodenegocio #barbearia""",
 3: """Fiquei em 13º no teste físico da Aeronáutica. O seu cliente também faz um ranking.

O alistamento era obrigatório e eu disse que queria servir. O meu pai sempre aconselhou a Aeronáutica. Antes dos testes eu disse: vou ser escolhido e vou estar entre os melhores. Fiquei em 13º nos testes físicos, passei nos médicos e entrei.

A vaga era disputada. Quem escolhia, comparava.

O que eu vejo hoje: o cliente abre o seu perfil e o do concorrente na mesma hora. E escolhe quem deixa tudo mais claro.

Faça o teste do cliente hoje. Abra o seu perfil e o de 3 concorrentes da sua cidade, como se fosse cliente, e compare 3 coisas:
1. Em 5 segundos dá para saber o que você faz e para quem?
2. Tem preço ou um "a partir de"?
3. Tem um jeito claro de marcar?

Exemplo ilustrativo de um personal: o concorrente escreve "Avaliação + plano de 4 semanas, a partir de 120 €. Mande AVALIAÇÃO". O seu perfil só tem fotos de treino. Em que lugar você fica?

🔻 Envie para quem tem concorrente na mesma rua. E comente CLIENTES que eu te chamo no direct e faço o teste no seu perfil.

Fotos: Robério Castro Fotografia.

#empreendedorismo #historiareal #disciplina #personaltrainer #donodenegocio""",
 4: """Antes de dar 20% de desconto na Black Friday, faça esta conta.

O desconto sai inteiro do que sobra para você. O seu custo continua igual.

1. Escreva o preço e o custo por cliente. Custo é o que sai do seu bolso para atender aquela pessoa: sala, material, comissão, taxa do cartão. Exemplo ilustrativo de um personal: plano de 200 € por mês e custo de 80 € por aluno. Sobram 120 €.
2. Tire o desconto do que sobra. Com 20%, o plano vai para 160 € e o custo continua 80 €. Sobram 80 €. O desconto de 20% no preço comeu 33% do que sobrava.
3. Descubra quantos clientes a mais você precisa: o que sobra hoje ÷ o que sobra com desconto. 120 ÷ 80 = 1,5. Para sobrar o mesmo, 10 alunos viram 15. São 5 alunos a mais só para ficar no mesmo lugar.
4. Troque o desconto por valor: mantenha o preço e acrescente algo que custa pouco para você e vale muito para o cliente (avaliação extra, plano por escrito, 1 sessão com a fisio parceira), com prazo para fechar.
5. Tenha a resposta pronta para quem pede desconto: "Eu não mexo no preço, porque é ele que paga o meu acompanhamento. Quem fechar até domingo leva [bônus]. Quer que eu reserve a sua vaga?"

🔻 Salve para fazer a sua conta antes de sexta. E comente CLIENTES que eu te chamo no direct e a gente faz a conta do seu desconto.

#precificacao #blackfriday #personaltrainer #academia #fisioterapia""",
 5: """Negócio parado não precisa de mais seguidor. Precisa de mais conversa começada por você.

O personal com 3 mil seguidores recebe 2 mensagens por semana. A fisio posta todo dia e não pergunta nada a ninguém. O barbeiro espera o cliente lembrar que precisa cortar.

Nos meus primeiros meses em Lisboa eu vendia até a minha folga.

Hoje: 10 conversas começadas por você. Sem oferta. Só uma pergunta.

🔻 Envie para quem está esperando o cliente aparecer. E comente CLIENTES que eu te chamo no direct.

#clientes #donodenegocio #personaltrainer #fisioterapia #barbearia""",
 6: """A minha loja de moda praia vendia no verão. O dinheiro do verão ia para casa.

No tempo de militar eu abri uma loja de moda praia e investi entre 10 e 12 mil reais. Moda praia vende numa época do ano, e no resto do ano as contas continuam chegando.

O meu erro: a conta da loja e a de casa eram uma só. O dinheiro da loja pagou viagens e contas de casa. Depois veio a Covid e a loja quebrou. E eu não sabia quanto ela tinha dado de verdade.

O que eu vejo hoje: academia e personal também têm o seu verão. Num levantamento da Wodify com mais de 5.000 negócios de fitness, novembro e dezembro tiveram o pior saldo de alunos do ano.

O mês bom tem que pagar o mês ruim. Abra os últimos 12 meses e marque o pior. Esse é o mês que a sua reserva precisa cobrir.

Exemplo ilustrativo de uma barbearia: custo fixo de 2.400 € por mês e dezembro com 1.600 € de entrada. Faltam 800 €. De março a novembro, separe 90 € por mês numa conta só da empresa.

🔻 Comente CLIENTES e qual é o pior mês do seu negócio. Eu te chamo no direct.

Fonte do dado de academias: Wodify, "Behind the Numbers: How Gym Membership Trends Shift Throughout the Year".

#gestaofinanceira #empreendedorismo #historiareal #academia #barbearia""",
 7: """Eu não acredito em aprender negócio com vídeo solto.

Cada vídeo ensina uma coisa diferente e um não continua o outro.

O que eu vejo: o personal que assistiu 40 vídeos de anúncio e nunca subiu o primeiro. O barbeiro com 200 posts salvos e a mesma bio de 2 anos atrás. A fisio que aprendeu funil numa semana e preço na outra, e não aplicou nenhum dos dois.

O que eu faço no lugar: uma coisa de cada vez, na ordem. Oferta, perfil, conversa e só depois anúncio.

Escolha uma coisa e execute até domingo:
1. A oferta numa linha.
2. A bio com o que você faz, para quem e como marcar.
3. 10 conversas começadas por você.
4. Só então o anúncio.

Exemplo ilustrativo de um personal: esta semana é só a oferta. "Avaliação + plano de 4 semanas para voltar a treinar sem dor, 120 €." Os vídeos ficam para depois de aplicar.

🔻 Salve para seguir a ordem. E comente CLIENTES que eu te chamo no direct e te digo por onde começar no seu negócio.

#empreendedorismo #donodenegocio #personaltrainer #barbearia #fisioterapia""",
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
    run(pizza, O(2)); run(teste, O(3)); run(desconto, O(4))
    run(legenda, O(5), "render_legenda.py")
    run(loja, O(6))
    run(video, O(7))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
