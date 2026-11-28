"""Plano 100 mil, semana 5 do PDF (leitura e corte, dia 3), 23/11/2026, segunda. Dia 17 do "Plano de 30 dias para lançar
a mentoria": conteúdo "Como conseguir os primeiros clientes sem anúncio" (vira o VALOR das 17:40, pilar 1) e tarefa
"Mensagem individual a quem ficou em dúvida sobre o desafio" (no doc).
Grade do playbook (ajustes de 10/11, 16/11, 18/11 e 19/11 prevalecem sobre a tarefa agendada): 7 posts, sem post de IA.
Segunda: 10:30 NOTÍCIA · 12:40 CONEXÃO (remodelado) · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 PROVA · 22:15 BANDEIRA.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
Fotos: só do Liuri (sem a ex-esposa), nenhum frame de vídeo. Indicação: 0 de 7 posts.
CTA (rodízio sobre 22/11, todos terminam em "Comente CLIENTES"):
10:30 envio · 12:40 salvar · 14:20 comentário · 17:40 envio · 19:10 comentário · 20:30 salvar · 22:15 envio.
1) 10:30 NOTÍCIA: Proteção de Conteúdo chega ao Instagram (Fast Company Brasil, Lilian Campos, 18/11/2026; Portal
   Publicitário, Felipe Martins, 17/11/2026).
2) 12:40 FAIXA, conexão, pilar 5 (lição pilar 3): "Fiz o curso de massagem em 2017. Só em 2026 ela começou a pagar as contas."
   Cuidados (dez anos de massagem) + itens 12, 15, 17, 19, 20. REMODELADO de liurialves:6af7e33397efac0554da5491 ("Vendi água na
   praia...", 14/11 12:40, 147 de alcance, 314 views, nunca replicado): mesmo arco (trabalho humilde → o que aprendi sobre
   oferta), trecho, capa, fotos, lição e CTA novos.
3) 14:20 FAIXA, conexão, pilar 5 (lição pilar 1): "Durante 2 meses o meu carro só ligava empurrando." Item 16 (+14 e 17).
4) 17:40 FAIXA, valor com rosto (A), pilar 1: 5 vagas sem anúncio (Clubworx 10/02/2025; Two-Brain, Chris Cooper, 16/03/2026).
5) 19:10 LEGENDA, bandeira falada, pilar 4: os 4 números de cor.
6) 20:30 FAIXA, PROVA, pilar 5: 219 cliques por 16,81 € (print Meta Ads recortado; gancho livre desde 23/11).
7) 22:15 FAIXA, bandeira, pilar 2: "Eu não acredito que o Instagram 'não funciona' para o seu negócio." Objeção "já tentei e
   não funcionou" (Documento de Clareza).
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/dac1b4a3-3d7c-58ef-a28a-e158f6e1b262/scratchpad"
DIA = "2026-11-23"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h23/{x}.jpg"           # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px23/pexels-{x}.jpg"

# 1) 10:30 NOTÍCIA, CAPA + ESCURO, CTA = ENVIO + CLIENTES
noticia = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": P("8368350"), "foco_y": 0.5, "etiqueta": "Notícia",
   "titulo": "O Instagram agora avisa quando copiam o seu vídeo. E deixa esconder a cópia.",
   "sub": "Fast Company Brasil (18/11/2026) e Portal Publicitário (17/11/2026). O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O que mudou", "frase": "A Proteção de Conteúdo [[chegou ao Instagram]].",
   "texto": "Antes era só do Facebook. O recurso acompanha os seus vídeos originais e avisa quando encontra uma cópia no Instagram ou no Facebook, com as visualizações que a cópia teve."},
  {"etiqueta": "As 4 opções", "frase": "Acompanhar, ocultar, [[dar crédito]] ou liberar.",
   "texto": "Ocultar tira a cópia de vista no Instagram e no Facebook. Dar crédito põe o aviso \"Original por\" com link para o seu vídeo. Também dá para cadastrar perfis autorizados, como um parceiro."},
  {"etiqueta": "O que quase ninguém leu", "frase": "Só entra quem cumpre os [[critérios de originalidade]].",
   "texto": "O acesso está sendo liberado aos poucos. Quem não recebeu o aviso pode pedir nas ferramentas profissionais. A Meta ainda vai testar a detecção de vídeos feitos com IA que reaproveitam o áudio do original."},
  {"etiqueta": "O que eu acredito", "frase": "Vídeo copiado [[não traz cliente]] para ninguém.",
   "texto": "Eu vejo dono de academia repostar a trend de outro perfil e achar que fez conteúdo. A plataforma está protegendo, e mostrando mais, quem grava o próprio."},
  {"etiqueta": "No seu negócio", "frase": "O que é seu [[ninguém tem para copiar]].",
   "texto": "Exemplo ilustrativo: o personal grava a correção de agachamento do próprio aluno, com autorização. A fisio explica o exercício na sala dela. O barbeiro mostra o antes e depois de quem sentou na cadeira dele."},
  {"etiqueta": "Faça hoje", "frase": "[[3 vídeos seus]] antes de sexta.",
   "texto": "1. Uma pergunta que o seu cliente sempre faz, respondida em 30 segundos. 2. Um bastidor do seu dia. 3. Um resultado de cliente, com autorização. Depois, veja nas ferramentas profissionais se a Proteção de Conteúdo já apareceu para você."},
  {"etiqueta": "Próximo passo", "frase": "Envie para quem vive de repost e [[comente CLIENTES]].",
   "texto": "Eu te chamo no direct e a gente monta a sua lista de vídeos próprios para dezembro."},
]}

# 2) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = SALVAR + CLIENTES
massagem = {"slides": [
  {"tipo": "foto", "foto": HP("32"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "DEZ ANOS DE MASSAGEM",
   "texto": "EU FIZ O CURSO DE MASSAGEM EM 2017. SÓ EM 2026 ELA COMEÇOU A PAGAR AS CONTAS."},
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.35, "faixa": "EM 2017",
   "texto": "EU ERA MILITAR E FIZ O CURSO JUNTO COM A AERONÁUTICA.", "destaque": "TRABALHEI UM TEMPO NUMA CLÍNICA."},
  {"tipo": "foto", "foto": HP("37"), "foco_y": 0.4, "faixa": "DEPOIS",
   "texto": "SAÍ DA AERONÁUTICA E FUI FAZER UBER NO BRASIL.", "destaque": "A IDEIA JÁ ERA MORAR FORA."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.35, "faixa": "EM PORTUGAL",
   "texto": "RESTAURANTE, CLUBE À NOITE E 2 ANOS DE UBER.", "destaque": "A MASSAGEM FICOU DE LADO."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "O QUE EU VEJO HOJE",
   "texto": "A HABILIDADE ESTAVA COMIGO O TEMPO TODO.", "destaque": "EU SÓ NÃO OFERECIA."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "2026",
   "texto": "VOLTEI À MASSAGEM E COMECEI A CRIAR SITES PARA CLIENTES.", "destaque": "DE 1.500 € PARA 7.000 € POR MÊS."},
  {"tipo": "branco", "blocos": [
   ["h", "HABILIDADE QUE NINGUÉM SABE QUE VOCÊ VENDE NÃO PAGA CONTA."], ["esp", 8],
   ["n", "Escreva hoje a sua oferta numa linha só: para quem + o que entrega + em quanto tempo + preço."],
   ["n", "Exemplo ilustrativo de uma fisio: \"Para quem corre e sente o joelho: 6 sessões em 3 semanas para voltar a correr, 270 €.\" Se não cabe numa linha, o cliente também não entende. Coloque essa linha na bio e mande para 5 clientes antigos."]]},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE ESCREVE A SUA OFERTA EM UMA LINHA.",
   "destaque": "O QUE VOCÊ SABE FAZER E NÃO VENDE?"},
]}

# 3) 14:20 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
punto = {"slides": [
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-1"), "foco_y": 0.2, "grande": True, "arraste": True,
   "faixa": "O MEU PRIMEIRO CARRO EM PORTUGAL",
   "texto": "DURANTE 2 MESES, O MEU CARRO SÓ LIGAVA EMPURRANDO."},
  {"tipo": "foto", "foto": HP("74"), "foco_y": 0.45, "faixa": "LISBOA",
   "texto": "UM FIAT PUNTO DE 1996, COMPRADO POR 450 €.", "destaque": "FOI O PRIMEIRO CARRO QUE EU TIVE AQUI."},
  {"tipo": "foto", "foto": HP("75"), "foco_y": 0.45, "faixa": "EM POUCAS SEMANAS",
   "texto": "O MOTOR AQUECIA E ELE SÓ PEGAVA NO EMPURRÃO.", "destaque": "DEPOIS, O CABO DAS MUDANÇAS PARTIU."},
  {"tipo": "foto", "foto": HP("76"), "foco_y": 0.45, "faixa": "E FOI NO ANO DO PARTO",
   "texto": "O MEU SEGUNDO FILHO ESTAVA PARA NASCER.", "destaque": "E EU TRABALHAVA 12 HORAS POR DIA NO RESTAURANTE."},
  {"tipo": "foto", "foto": FL("carro-painel-rua"), "foco_y": 0.5, "faixa": "DEPOIS",
   "texto": "O PUNTO DUROU 2 MESES. COMPREI O SEGUNDO CARRO.", "destaque": "E PAREI DE EMPURRAR."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "O QUE EU VEJO HOJE",
   "texto": "MUITO NEGÓCIO SÓ ANDA EMPURRADO.", "destaque": "O DONO PARA DE CORRER ATRÁS E A VENDA PARA JUNTO."},
  {"tipo": "branco", "blocos": [
   ["h", "CONTE QUANTAS VENDAS VIERAM SEM VOCÊ EMPURRAR."], ["esp", 8],
   ["n", "Abra o mês passado e separe as vendas em 2 colunas: as que vieram porque você correu atrás (mensagem, ligação, favor) e as que chegaram sozinhas (perfil, anúncio, cliente que voltou)."],
   ["n", "Exemplo ilustrativo de um personal: 9 alunos novos, 7 na primeira coluna. Se a primeira coluna é a maior, o próximo passo é montar o que enche a segunda: oferta clara no perfil e 1 anúncio de mensagem."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTAS VENDAS DO SEU MÊS VIERAM SEM VOCÊ EMPURRAR. EU TE CHAMO NO DIRECT.",
   "destaque": "QUANTAS FORAM?"},
]}

# 4) 17:40 FAIXA, VALOR COM ROSTO (A), CTA = ENVIO + CLIENTES
vagas = {"slides": [
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "SEM 1 € EM ANÚNCIO: COMO EU PREENCHERIA 5 VAGAS ESTE MÊS."},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "faixa": "O QUE EU ACREDITO",
   "texto": "ANÚNCIO ACELERA O QUE JÁ FUNCIONA.", "destaque": "SE A OFERTA NÃO VENDE NO DIRECT, NÃO VENDE NO ANÚNCIO."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "LISTE 30 PESSOAS QUE JÁ TE CONHECEM"], ["esp", 8],
   ["n", "Clientes que pararam, quem pediu preço e não fechou, contatos do WhatsApp que sabem o que você faz."],
   ["n", "Uma planilha simples: nome, o que ela precisa, data da última conversa."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "ABRA 5 VAGAS COM DATA PARA FECHAR"], ["esp", 8],
   ["n", "Post e story no mesmo dia: \"Abri 5 vagas para [serviço] em dezembro. Fecho na sexta.\""],
   ["n", "Sem desconto. Se quiser um bônus, acrescente valor. Exemplo: avaliação e plano por escrito para quem entrar."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "1 MENSAGEM PARA CADA PESSOA DA LISTA"], ["esp", 8],
   ["n", "\"Oi, [nome]. Abri 5 vagas para [serviço] em dezembro e lembrei de você por causa de [o que ela te contou]. Quer que eu te explique como funciona?\""],
   ["n", "Pessoal, com o nome e terminando em pergunta. Nada de lista de transmissão."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "UMA PARCERIA NA SUA RUA"], ["esp", 8],
   ["n", "O personal com a fisio, a fisio com a academia, a barbearia com o personal. Cada um oferece aos próprios clientes uma sessão de 30 minutos do parceiro."],
   ["n", "Quem já confia num, conhece o outro."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 5"], ["h", "VOLTE EM 3 DIAS"], ["esp", 8],
   ["n", "Para quem não respondeu: \"Oi, [nome]. Ainda tenho [X] vagas e fecho na sexta. Quer uma?\""],
   ["n", "Anote quem disse sim, quem disse não e quem pediu para falar depois. É essa lista que vira o seu janeiro."]]},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM ACHA QUE PRECISA DE ANÚNCIO",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE ESCREVE A SUA MENSAGEM DAS 5 VAGAS.",
   "destaque": "QUANTAS VAGAS VOCÊ TEM?"},
]}

# 5) 19:10 LEGENDA (fotos reais do Liuri), bandeira falada, CTA = COMENTÁRIO + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("selfie-jaqueta-verde"), HP("32")], "foco": [0.3, 0.3], "textos": ["Eu acho que todo dono de negócio", "devia saber 4 números de cor."]},
 {"fotos": [FL("home-office-headset"), FL("dunas-punhos-camisa-preta-1")], "foco": [0.5, 0.2], "textos": ["Quanto entrou, quanto saiu,", "quanto sobrou e quanto falta receber."]},
 {"fotos": [FL("lagoa-biceps-de-frente-editada"), HP("60")], "foco": [0.35, 0.35], "textos": ["O personal sabe quantos alunos tem", "e não sabe quanto sobra de cada um."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-2"), HP("37")], "foco": [0.2, 0.4], "textos": ["A fisio sabe a agenda da semana", "e não sabe quem ainda não pagou."]},
 {"fotos": [FL("selfie-sem-camisa-serio"), FL("carro-painel-rua")], "foco": [0.3, 0.5], "textos": ["O barbeiro sabe quanto cortou no sábado", "e não sabe quanto gastou no mês."]},
 {"fotos": [f"{R}/assets/avatar-liuri.jpg", FL("dunas-punhos-camisa-preta-3")], "foco": [0.3, 0.45], "textos": ["Eu já quebrei uma loja", "por misturar a conta dela com a de casa."]},
 {"fotos": [HP("67"), FL("cafe-pastel-pao-de-queijo")], "foco": [0.3, 0.45], "textos": ["No domingo, 20 minutos:", "os 4 números num papel."]},
 {"fotos": [HP("60"), f"{R}/assets/foto-perfil-liuri.jpg"], "foco": [0.35, 0.3], "textos": ["Comente CLIENTES", "e eu te chamo no direct."]},
]}

# 6) 20:30 FAIXA, PROVA, CTA = SALVAR + CLIENTES
prova = {"slides": [
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "PROVA · UM ANÚNCIO DE 16,81 €",
   "texto": "GASTEI 16,81 € NUM ANÚNCIO. 219 PESSOAS TOCARAM NO BOTÃO DE LIGAR."},
  {"tipo": "foto", "foto": HP("prova-219"), "foco_y": 0.4, "faixa": "O PRINT",
   "texto": "11.541 PESSOAS ALCANÇADAS.", "destaque": "0,0768 € POR CLIQUE NA LIGAÇÃO."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.35, "faixa": "DE ONDE VEIO",
   "texto": "ERA A MINHA EMPRESA DE MASSAGEM EM LISBOA.", "destaque": "E EU MESMO FIZ O ANÚNCIO."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "O ANÚNCIO",
   "texto": "PEDIA UMA AÇÃO SÓ: LIGAR.", "destaque": "QUEM LIGA ESTÁ COM O PROBLEMA NA MÃO."},
  {"tipo": "branco", "blocos": [
   ["h", "CLIQUE AINDA NÃO É CLIENTE."], ["esp", 8],
   ["n", "Do clique até a marcação, quem decide é o atendimento. Por isso eu não olho só o custo por clique."],
   ["n", "Eu olho 3 números: cliques, ligações atendidas e marcações."]]},
  {"tipo": "branco", "blocos": [
   ["h", "ANTES DE SUBIR O ORÇAMENTO, ESCREVA O ANÚNCIO EM 3 LINHAS."], ["esp", 8],
   ["n", "Linha 1: para quem e o problema. Linha 2: o que você entrega. Linha 3: o botão."],
   ["n", "Exemplo ilustrativo de um personal: \"Voltar a treinar depois dos 35, sem dor nas costas. Avaliação e plano de 4 semanas. Toque em ligar e marque a sua avaliação.\""]]},
  {"tipo": "branco", "blocos": [
   ["h", "E TENHA A RESPOSTA PRONTA ANTES DO 1º CLIQUE."], ["esp", 8],
   ["n", "\"Olá, aqui é o [nome]. Vi que você ligou pelo anúncio. O que te fez procurar agora?\""],
   ["n", "Ouça a resposta e só depois fale de horário e preço."]]},
  {"tipo": "foto", "foto": f"{R}/assets/avatar-liuri.jpg", "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE ESCREVE O SEU ANÚNCIO DE 3 LINHAS.",
   "destaque": "O SEU ANÚNCIO PEDE O QUÊ?"},
]}

# 7) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = ENVIO + CLIENTES
insta = {"slides": [
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO QUE O INSTAGRAM \"NÃO FUNCIONA\" PARA O SEU NEGÓCIO."},
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.35, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "UM REEL MEU, SÓ DIZENDO \"SEGUE @LIURIALVES\", ALCANÇOU 1.205 PESSOAS.", "destaque": "NO MESMO PERFIL, TEVE POST QUE NÃO PASSOU DE 30."},
  {"tipo": "foto", "foto": P("20860588"), "foco_y": 0.35, "faixa": "O QUE EU VEJO",
   "texto": "A FISIO QUE POSTA EXERCÍCIO E NUNCA DIZ COMO MARCAR.", "destaque": "O SEGUIDOR SALVA E VAI EMBORA."},
  {"tipo": "foto", "foto": P("4853661"), "foco_y": 0.4, "faixa": "E TAMBÉM",
   "texto": "A ACADEMIA QUE POSTA A AULA CHEIA.", "destaque": "E NÃO DIZ QUANTO CUSTA NEM COMO ENTRAR."},
  {"tipo": "foto", "foto": P("9992819"), "foco_y": 0.35, "faixa": "E AINDA",
   "texto": "O BARBEIRO QUE POSTA 30 CORTES POR MÊS.", "destaque": "E NENHUM PEDE PARA MARCAR."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "O QUE EU FAÇO NO LUGAR",
   "texto": "TODO POST MEU TERMINA PEDINDO UMA COISA SÓ.", "destaque": "VOCÊ SABE QUAL É."},
  {"tipo": "branco", "blocos": [
   ["h", "PERFIL SEM PEDIDO É VITRINE SEM PREÇO."], ["esp", 8],
   ["n", "Faça esta semana: abra os seus 3 últimos posts e acrescente no fim da legenda uma linha dizendo o que fazer agora."],
   ["n", "Exemplo ilustrativo de uma fisio: \"Dor no joelho quando corre? Mande JOELHO no direct e eu te digo se a avaliação é para você.\" Na sexta, compare as mensagens da semana com as da anterior."]]},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM DIZ QUE NÃO FUNCIONA",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E OLHO OS SEUS 3 ÚLTIMOS POSTS.",
   "destaque": "O SEU POST PEDE ALGUMA COISA?"},
]}

LEGENDAS = {
 1: """O Instagram agora avisa quando copiam o seu vídeo. E deixa esconder a cópia.

A Proteção de Conteúdo, que era só do Facebook, chegou ao Instagram. O recurso acompanha os seus vídeos originais e avisa quando encontra uma cópia no Instagram ou no Facebook, com as visualizações que ela teve.

São 4 opções: acompanhar, ocultar (a cópia deixa de aparecer no Instagram e no Facebook), dar crédito (aviso "Original por" com link para o seu vídeo) ou liberar. Dá também para cadastrar perfis autorizados, como um parceiro.

O detalhe que quase ninguém leu: o acesso está sendo liberado aos poucos, só para quem cumpre os critérios de originalidade. Quem não recebeu o aviso pode pedir nas ferramentas profissionais. E a Meta vai testar a detecção de vídeos feitos com IA que reaproveitam o áudio do original.

O que eu acredito: vídeo copiado não traz cliente para ninguém. Eu vejo dono de academia repostar a trend de outro perfil e achar que fez conteúdo.

Exemplo ilustrativo: o personal grava a correção de agachamento do próprio aluno, com autorização. A fisio explica o exercício na sala dela. O barbeiro mostra o antes e depois de quem sentou na cadeira dele.

Faça antes de sexta, 3 vídeos seus:
1. Uma pergunta que o seu cliente sempre faz, respondida em 30 segundos.
2. Um bastidor do seu dia.
3. Um resultado de cliente, com autorização.

🔻 Envie para quem vive de repost. E comente CLIENTES que eu te chamo no direct e a gente monta a sua lista de vídeos próprios para dezembro.

Fontes: Fast Company Brasil (Lilian Campos, "Instagram lança ferramenta para identificar cópias de vídeos e proteger criadores", 18/11/2026) e Portal Publicitário (Felipe Martins, 17/11/2026).

#instagram #instagramparanegocios #donodenegocio #personaltrainer #barbearia""",
 2: """Eu fiz o curso de massagem em 2017. Só em 2026 ela começou a pagar as contas.

Eu era militar e fiz o curso junto com a Aeronáutica. Trabalhei um tempo numa clínica. Depois saí da Aeronáutica e fui fazer Uber no Brasil, já com a ideia de morar fora. Em Portugal foram restaurante, clube à noite e 2 anos de Uber. A massagem ficou de lado.

O que eu vejo hoje: a habilidade estava comigo o tempo todo. Eu só não oferecia.

Em 2026 eu voltei à massagem e comecei a criar sites para clientes. A empresa saiu de 1.500 € para 7.000 € por mês.

Habilidade que ninguém sabe que você vende não paga conta. Escreva hoje a sua oferta numa linha só: para quem + o que entrega + em quanto tempo + preço.

Exemplo ilustrativo de uma fisio: "Para quem corre e sente o joelho: 6 sessões em 3 semanas para voltar a correr, 270 €." Se não cabe numa linha, o cliente também não entende. Coloque essa linha na bio e mande para 5 clientes antigos.

🔻 Salve para escrever a sua hoje. E comente CLIENTES que eu te chamo no direct e a gente escreve a sua oferta em uma linha.

Fotos da Aeronáutica: Robério Castro Fotografia.

#empreendedorismo #historiareal #brasileirosemportugal #fisioterapia #donodenegocio""",
 3: """Durante 2 meses, o meu carro só ligava empurrando.

Foi o meu primeiro carro em Portugal: um Fiat Punto de 1996, comprado por 450 €. O motor aquecia, ele só pegava no empurrão e depois o cabo das mudanças partiu. Foi no ano do parto do meu segundo filho, e eu trabalhava 12 horas por dia no restaurante. O Punto durou 2 meses. Comprei o segundo carro e parei de empurrar.

O que eu vejo hoje: muito negócio só anda empurrado. O dono para de correr atrás e a venda para junto.

Faça esta conta: abra o mês passado e separe as vendas em 2 colunas. Na primeira, as que vieram porque você correu atrás (mensagem, ligação, favor). Na segunda, as que chegaram sozinhas (perfil, anúncio, cliente que voltou).

Exemplo ilustrativo de um personal: 9 alunos novos, 7 na primeira coluna. Se a primeira coluna é a maior, o próximo passo é montar o que enche a segunda: oferta clara no perfil e 1 anúncio de mensagem.

🔻 Comente CLIENTES e quantas vendas do seu mês vieram sem você empurrar. Eu te chamo no direct.

#empreendedorismo #brasileirosemportugal #historiareal #donodenegocio #personaltrainer""",
 4: """Sem 1 € em anúncio: como eu preencheria 5 vagas este mês.

Anúncio acelera o que já funciona. Se a oferta não vende no direct, não vende no anúncio.

1. Liste 30 pessoas que já te conhecem: clientes que pararam, quem pediu preço e não fechou, contatos do WhatsApp que sabem o que você faz. Planilha com nome, o que ela precisa e a data da última conversa.
2. Abra 5 vagas com data para fechar. Post e story no mesmo dia: "Abri 5 vagas para [serviço] em dezembro. Fecho na sexta." Sem desconto. Se quiser bônus, acrescente valor (avaliação e plano por escrito, por exemplo).
3. Uma mensagem para cada pessoa da lista: "Oi, [nome]. Abri 5 vagas para [serviço] em dezembro e lembrei de você por causa de [o que ela te contou]. Quer que eu te explique como funciona?"
4. Uma parceria na sua rua: o personal com a fisio, a fisio com a academia, a barbearia com o personal. Cada um oferece aos próprios clientes uma sessão de 30 minutos do parceiro.
5. Volte em 3 dias para quem não respondeu: "Oi, [nome]. Ainda tenho [X] vagas e fecho na sexta. Quer uma?" Anote sim, não e "fala comigo depois". Essa lista vira o seu janeiro.

🔻 Envie para quem acha que precisa de anúncio para começar. E comente CLIENTES que eu te chamo no direct e a gente escreve a sua mensagem das 5 vagas.

Base: Clubworx ("How to get clients as a personal trainer when you're starting out", 10/02/2025) e Two-Brain Business (Chris Cooper, "How to Find Your Next 10 Clients Without Paying a Dime", 16/03/2026), adaptados por mim.

#clientes #personaltrainer #academia #fisioterapia #barbearia""",
 5: """Todo dono de negócio devia saber 4 números de cor: quanto entrou, quanto saiu, quanto sobrou e quanto falta receber.

O personal sabe quantos alunos tem e não sabe quanto sobra de cada um. A fisio sabe a agenda da semana e não sabe quem ainda não pagou. O barbeiro sabe quanto cortou no sábado e não sabe quanto gastou no mês.

Eu já quebrei uma loja por misturar a conta dela com a de casa.

No domingo, 20 minutos: os 4 números num papel.

🔻 Comente CLIENTES e eu te chamo no direct.

#gestao #donodenegocio #personaltrainer #fisioterapia #barbearia""",
 6: """Gastei 16,81 € num anúncio. 219 pessoas tocaram no botão de ligar.

O print é real: 11.541 pessoas alcançadas e 0,0768 € por clique na ligação. Era a minha empresa de massagem em Lisboa, e eu mesmo fiz o anúncio. Ele pedia uma ação só: ligar. Quem liga está com o problema na mão.

Mas clique ainda não é cliente. Do clique até a marcação, quem decide é o atendimento. Por isso eu olho 3 números: cliques, ligações atendidas e marcações.

Antes de subir o orçamento, escreva o anúncio em 3 linhas:
1. Para quem e o problema.
2. O que você entrega.
3. O botão.
Exemplo ilustrativo de um personal: "Voltar a treinar depois dos 35, sem dor nas costas. Avaliação e plano de 4 semanas. Toque em ligar e marque a sua avaliação."

E tenha a resposta pronta antes do primeiro clique: "Olá, aqui é o [nome]. Vi que você ligou pelo anúncio. O que te fez procurar agora?" Ouça, e só depois fale de horário e preço.

Isto não é promessa de resultado para você. É o que aconteceu no meu negócio, com os meus números.

🔻 Salve para escrever o seu. E comente CLIENTES que eu te chamo no direct e a gente escreve o seu anúncio de 3 linhas.

#prova #anuncios #trafegopago #donodenegocio #personaltrainer""",
 7: """Eu não acredito que o Instagram "não funciona" para o seu negócio.

Um Reel meu, só dizendo "Segue @liurialves", alcançou 1.205 pessoas. No mesmo perfil, teve post que não passou de 30. A plataforma era a mesma.

O que eu vejo: a fisio que posta exercício e nunca diz como marcar. O seguidor salva e vai embora. A academia que posta a aula cheia e não diz quanto custa nem como entrar. O barbeiro que posta 30 cortes por mês e nenhum pede para marcar.

O que eu faço no lugar: todo post meu termina pedindo uma coisa só. Você sabe qual é.

Perfil sem pedido é vitrine sem preço. Faça esta semana: abra os seus 3 últimos posts e acrescente no fim da legenda uma linha dizendo o que fazer agora. Exemplo ilustrativo de uma fisio: "Dor no joelho quando corre? Mande JOELHO no direct e eu te digo se a avaliação é para você." Na sexta, compare as mensagens da semana com as da anterior.

🔻 Envie para quem diz que o Instagram não funciona. E comente CLIENTES que eu te chamo no direct e olho os seus 3 últimos posts.

#instagram #donodenegocio #fisioterapia #academia #barbearia""",
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
    for n in [1, 2, 3, 4, 6, 7]:
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(noticia, O(1), "render_formatos.py")
    run(massagem, O(2)); run(punto, O(3)); run(vagas, O(4))
    run(legenda, f"{R}/posts/{DIA}/liurialves-5b", "render_legenda.py")  # 23/11 12:50: refeito com foto preenchida (pedido do dono)
    run(prova, O(6))
    run(insta, O(7))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
