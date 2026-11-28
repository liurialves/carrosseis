"""Plano 100 mil, semana 4 do PDF (janela de testes, dia 6), 19/11/2026, quinta-feira. Dia 13 do "Plano de 30 dias para
lançar a mentoria": conteúdo "Viver só de indicação é perigoso" (vira a fala das 19:10, por um ângulo novo: o cliente que
trazia outros muda de cidade; a palavra nem aparece) e tarefa "Caixa de perguntas sobre negócios nos Stories" (no doc).
Grade do playbook (ajustes de 10/11, 16/11 e 18/11 prevalecem sobre a tarefa agendada): 6 posts, sem post de IA.
Quinta: 12:40 CONEXÃO · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 CONEXÃO · 22:15 BANDEIRA.
Ajuste de 11/11: tema indicação em 1 de 6 posts (19:10, sem a palavra), 0 de 5 roteiros, 0 stories.
Ajuste de 18/11: nenhum frame de vídeo; só fotos reais enviadas pelo dono (Drive historia-portugal + assets/fotos-liuri).
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
CTA (rodízio sobre 18/11, todos terminam em "Comente CLIENTES"):
12:40 salvar · 14:20 envio · 17:40 comentário · 19:10 envio · 20:30 comentário · 22:15 salvar.
1) 12:40 FAIXA, conexão, pilar 5 (lição pilar 3): "Saía do restaurante à meia-noite e ia trabalhar num clube até as 8 da
   manhã." Itens 13, 15, 17 e 18 (gancho novo: o clube por 60 € a noite).
2) 14:20 FAIXA, conexão, pilar 5 (lição pilar 1): "Íamos ao shopping só para usar o Wi-Fi. Dava para um sorvete só."
   Itens 2 a 5 (gancho novo: item 4). REMODELADO de liurialves:6af7e35bd16af15d4df096bf ("perdi os dois empregos", 360 views,
   ainda não replicado): mesma fase e arco, gancho novo, fotos novas (20, 38, 36, 22, 29), lição nova.
3) 17:40 FAIXA, valor com rosto, pilar 1: perguntou o preço e sumiu, 3 mensagens em 7 dias. Molde Two-Brain (lead nurture,
   18/06/2025) + FitHive (12/05/2026) + Wodify (toda mensagem termina em pergunta).
4) 19:10 LEGENDA, bandeira falada, pilar 2: a agenda que depende de 3 pessoas (toca_indicacao, sem a palavra).
5) 20:30 FAIXA, conexão, pilar 5 (lição pilar 1): "Por 4 anos eu fiz a barba, engraxei a bota e arrumei a cama todo dia."
   Itens 9 e 10 (gancho novo; o item 10 só apareceu como apoio na bandeira de 13/11).
6) 22:15 FAIXA, bandeira, pilar 6: "Eu não acredito em fazer tudo sozinho para sempre." Prova do comprador ideal + item 14 do playbook.
ATUALIZADO 19/11 às 11h (pedido do dono): sem fotos com a ex-esposa. Os posts 1, 2, 4 e 6 foram refeitos em liurialves-1b, -2b, -4b e -6b (a foto 78 tem uma mulher de costas ao fundo; saiu por cautela).
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/c01c7929-4b7d-5117-8d0a-026a02dbb8f7/scratchpad"
DIA = "2026-11-19"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h19/{x}.jpg"           # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px19/pexels-{x}.jpg"

# 1) 12:40 FAIXA, CONEXÃO, CTA = SALVAR + CLIENTES
clube = {"slides": [
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "OS MEUS FINS DE SEMANA EM LISBOA",
   "texto": "SAÍA DO RESTAURANTE À MEIA-NOITE E IA TRABALHAR NUM CLUBE ATÉ AS 8 DA MANHÃ."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.45, "faixa": "QUANTO PAGAVA",
   "texto": "60 € POR NOITE.", "destaque": "8 HORAS DE CLUBE DEPOIS DE 12 NO RESTAURANTE."},
  {"tipo": "foto", "foto": P("11077588"), "foco_y": 0.4, "faixa": "O DIA ANTES DA NOITE",
   "texto": "12 HORAS NO RESTAURANTE.", "destaque": "EM 6 MESES EU VIREI SUBGERENTE."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.35, "faixa": "A CONTA DO MÊS",
   "texto": "EU PRECISAVA DE 800 A 900 € PARA VIVER.", "destaque": "RECEBIA 700 €."},
  {"tipo": "foto", "foto": P("35209733"), "foco_y": 0.5, "faixa": "COMO EU FECHAVA A CONTA",
   "texto": "VENDENDO MAIS HORAS.", "destaque": "NOS PRIMEIROS 5 MESES, VENDIA ATÉ A FOLGA."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "O QUE EU APRENDI ALI",
   "texto": "QUEM SÓ VENDE HORA TRABALHA MAIS PARA GANHAR O MESMO.", "destaque": "O DIA NÃO PASSA DE 24 HORAS."},
  {"tipo": "branco", "blocos": [
   ["h", "A MESMA HORA PODE VALER O DOBRO."], ["esp", 8],
   ["n", "Exemplo ilustrativo de um personal: 1 aula individual a 30 €. A mesma hora em dupla, a 20 € por pessoa, vira 40 €. Na fisio, pilates clínico com 3 pacientes. Na barbearia, o pacote pai e filho."],
   ["n", "Faça hoje: escolha 2 horários vazios da semana e ofereça como treino em dupla a 4 alunos atuais. Mensagem: \"Abri 2 horários em dupla, 20 € por pessoa. Quer treinar com alguém que você conhece?\""]]},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "EU TE CHAMO NO DIRECT E A GENTE ESCOLHE QUAL DOS SEUS HORÁRIOS VIRA DUPLA.",
   "destaque": "QUAL HORA SUA PODE VALER O DOBRO?"},
]}

# 2) 14:20 FAIXA, CONEXÃO (REMODELADO), CTA = ENVIO + CLIENTES
shopping = {"slides": [
  {"tipo": "foto", "foto": HP("33"), "foco_y": 0.15, "grande": True, "arraste": True, "faixa": "NO BRASIL, ANTES DE TUDO",
   "texto": "ÍAMOS AO SHOPPING SÓ PARA USAR O WI-FI. DAVA PARA UM SORVETE SÓ."},
  {"tipo": "foto", "foto": P("34884133"), "foco_y": 0.5, "faixa": "POR QUE O SHOPPING",
   "texto": "ERA ALI QUE A GENTE PROCURAVA FORMAS DE GANHAR DINHEIRO."},
  {"tipo": "foto", "foto": P("7761650"), "foco_y": 0.4, "faixa": "O SORVETE",
   "texto": "UM PARA OS DOIS.", "destaque": "A GENTE DIVIDIA."},
  {"tipo": "foto", "foto": P("40293118"), "foco_y": 0.5, "faixa": "COMO A GENTE CHEGOU ALI",
   "texto": "AOS 18, EU PERDI OS DOIS EMPREGOS AO MESMO TEMPO."},
  {"tipo": "foto", "foto": FL("mercado-coco-verde-2-49"), "foco_y": 0.3, "faixa": "O QUE A GENTE TESTOU",
   "texto": "CHINELO COM PÉROLAS, COSMÉTICOS E JOIAS.", "destaque": "DEPOIS, ÁGUA NA PRAIA COM UMA BICICLETA ENFERRUJADA."},
  {"tipo": "foto", "foto": FL("coco-verde-mesa"), "foco_y": 0.4, "faixa": "PARA QUE ERA",
   "texto": "O DINHEIRO DA ÁGUA ERA PARA CASAR."},
  {"tipo": "foto", "foto": HP("46"), "foco_y": 0.3, "faixa": "O QUE EU APRENDI ALI",
   "texto": "A GENTE COMEÇOU DE ONDE ESTAVA, SEM VERGONHA DO COMEÇO."},
  {"tipo": "branco", "blocos": [
   ["h", "VOCÊ JÁ TEM MAIS DO QUE EU TINHA NAQUELE SHOPPING."], ["esp", 8],
   ["n", "Muito dono parado no mesmo faturamento espera sobrar dinheiro para anúncio, fotógrafo ou perfil novo."],
   ["n", "Faça hoje com o que já tem: peça a 3 clientes fiéis um áudio de 20 segundos dizendo o que mudou desde que começaram com você. Exemplo de um personal: \"subi a escada do metrô sem parar\". Poste 1 por semana nos stories."]]},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.25, "faixa": "ENVIE PARA QUEM ESPERA SOBRAR DINHEIRO",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E TE MOSTRO COMO USAR OS 3 ÁUDIOS.",
   "destaque": "O QUE VOCÊ JÁ TEM NA MÃO?"},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO, CTA = COMENTÁRIO + CLIENTES
followup = {"slides": [
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "ELE PERGUNTOU O PREÇO E SUMIU. MANDE ESTAS 3 MENSAGENS EM 7 DIAS."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "O QUE EU VEJO",
   "texto": "O DONO RESPONDE O PREÇO, ESPERA E NUNCA MAIS ESCREVE.",
   "destaque": "SILÊNCIO NÃO É UM NÃO."},
  {"tipo": "branco", "blocos": [
   ["t", "NO MESMO DIA"], ["h", "PREÇO COM UMA PERGUNTA NO FIM"], ["esp", 8],
   ["n", "\"São 160 € por mês, 2 treinos por semana. Para eu te dizer se esse é o plano certo: o que você quer mudar nos próximos 3 meses?\""],
   ["n", "Exemplo ilustrativo. Toda mensagem termina em pergunta."]]},
  {"tipo": "branco", "blocos": [
   ["t", "DIA 2 · MENSAGEM 1"], ["h", "AJUDE ANTES DE VENDER"], ["esp", 8],
   ["n", "\"Quem começa do zero comigo quase sempre quer saber em quanto tempo sente diferença. Quer que eu te explique como são as 4 primeiras semanas?\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "DIA 4 · MENSAGEM 2"], ["h", "MOSTRE ALGUÉM PARECIDO"], ["esp", 8],
   ["n", "\"Um aluno começou com a mesma dúvida que você. Em 8 semanas, [resultado real, com autorização dele]. Quer ver como foi o treino?\""],
   ["n", "Sem caso ainda? Mande um vídeo de 30 s seu explicando a primeira semana."]]},
  {"tipo": "branco", "blocos": [
   ["t", "DIA 7 · MENSAGEM 3"], ["h", "CONVIDE COM DIA E HORA"], ["esp", 8],
   ["n", "\"Tenho quinta às 7h e sábado às 9h para uma avaliação de 30 minutos. Qual fica melhor?\""],
   ["n", "Ficou sem resposta? Uma última, sem pressão: \"Prefere que eu pare de te escrever? Sem problema.\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "NO SEU NEGÓCIO"], ["h", "TROQUE SÓ A PERGUNTA"], ["esp", 8],
   ["n", "Fisioterapia: \"Onde dói e há quanto tempo?\""],
   ["n", "Barbearia: no dia 7, 2 horários da semana com o nome do barbeiro. Academia: o horário da aula experimental."]]},
  {"tipo": "foto", "foto": P("14765792"), "foco_y": 0.4, "faixa": "DE ONDE VEM",
   "texto": "A TWO-BRAIN ENSINA DONOS DE ACADEMIA A FAZER 6 CONTATOS EM 3 DIAS E DEPOIS 1 A CADA 2 SEMANAS, POR 90 DIAS.",
   "destaque": "(JOHN FRANKLIN, TWO-BRAIN BUSINESS, 18/06/2025)"},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E O SEU PREÇO. EU TE CHAMO NO DIRECT E A GENTE ESCREVE A SUA MENSAGEM DO DIA 1.",
   "destaque": "QUANTOS TE PEDIRAM PREÇO ESTE MÊS?"},
]}

# 4) 19:10 LEGENDA (fala com fotos reais do Liuri), bandeira falada, CTA = ENVIO + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), FL("carro-painel-rua")], "foco": [0.2, 0.5], "textos": ["Eu acho que a sua agenda", "não pode depender de 3 pessoas."]},
 {"fotos": [FL("selfie-sem-camisa-serio"), HP("41")], "foco": [0.35, 0.3], "textos": ["Aquele cliente que trazia os amigos", "um dia muda de cidade."]},
 {"fotos": [FL("lagoa-biceps-de-frente-editada"), HP("42")], "foco": [0.35, 0.35], "textos": ["O personal que lotou a agenda", "com a turma de um aluno só."]},
 {"fotos": [FL("home-office-headset"), HP("33")], "foco": [0.3, 0.3], "textos": ["A fisio que recebia todo mês", "os pacientes de um médico amigo."]},
 {"fotos": [FL("selfie-jaqueta-verde"), FL("dunas-punhos-camisa-preta-2")], "foco": [0.3, 0.2], "textos": ["O barbeiro que vivia", "dos colegas de trabalho de um cliente."]},
 {"fotos": [HP("05"), HP("46")], "foco": [0.3, 0.35], "textos": ["Quando essa pessoa sai,", "a agenda sai junto."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-3"), HP("60")], "foco": [0.2, 0.3], "textos": ["Hoje, abra os últimos 20 clientes", "e anote quem trouxe cada um."]},
 {"fotos": [FL("lagoa-biceps-de-frente"), FL("selfie-sem-camisa-serio")], "foco": [0.35, 0.4], "textos": ["Mais de 5 da mesma pessoa?", "Comente CLIENTES."]},
]}

# 5) 20:30 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
farda = {"slides": [
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.35, "grande": True, "arraste": True,
   "faixa": "OS MEUS 4 ANOS NA AERONÁUTICA",
   "texto": "TODO DIA EU FAZIA A BARBA, ENGRAXAVA A BOTA E DEIXAVA A CAMA PERFEITA."},
  {"tipo": "foto", "foto": HP("41"), "foco_y": 0.3, "faixa": "COMO ERA",
   "texto": "MUITO GRITO, MUITA CORRERIA E TROCA DE FARDA."},
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.3, "faixa": "O DETALHE",
   "texto": "CAMA PERFEITA NÃO GANHA ELOGIO.", "destaque": "SÓ É NOTADA QUANDO FALTA."},
  {"tipo": "foto", "foto": HP("43"), "foco_y": 0.35, "faixa": "O QUE MUDOU EM MIM",
   "texto": "FOI ALI QUE EU APRENDI A SER DISCIPLINADO."},
  {"tipo": "foto", "foto": HP("13"), "foco_y": 0.35, "faixa": "DEPOIS",
   "texto": "A VIDA FOI MELHORANDO.", "destaque": "OS SALÁRIOS TAMBÉM."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "HOJE",
   "texto": "NINGUÉM ME MANDA FAZER A BARBA.", "destaque": "O PADRÃO FICOU."},
  {"tipo": "branco", "blocos": [
   ["h", "O SEU CLIENTE TAMBÉM NÃO ELOGIA O PADRÃO. ELE SÓ PERCEBE QUANDO FALTA."], ["esp", 8],
   ["n", "Escreva hoje 4 coisas que acontecem com todo cliente, sem exceção. Exemplo ilustrativo de uma fisio:"],
   ["n", "1. Lembrete no WhatsApp na véspera. 2. Começar no horário. 3. No fim: \"O que eu posso melhorar?\" 4. Mensagem 24 h depois: \"Como ficou a dor hoje?\" Cole a lista na parede e marque um X por cliente."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E OS SEUS 4 ITENS. EU TE CHAMO NO DIRECT E A GENTE ACERTA O SEU PADRÃO DE ATENDIMENTO.",
   "destaque": "O QUE O SEU CLIENTE SÓ NOTA QUANDO FALTA?"},
]}

# 6) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = SALVAR + CLIENTES
sozinho = {"slides": [
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-1"), "foco_y": 0.2, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM FAZER TUDO SOZINHO PARA SEMPRE."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "EU JÁ FIZ",
   "texto": "O CONTEÚDO, OS ANÚNCIOS E O ATENDIMENTO.", "destaque": "TUDO SOZINHO."},
  {"tipo": "foto", "foto": FL("cafe-pastel-pao-de-queijo"), "foco_y": 0.4, "faixa": "E FUNCIONOU",
   "texto": "EM 5 MESES, SAÍ DE 1.500 € PARA 5.500 € POR MÊS."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.3, "faixa": "O OUTRO LADO",
   "texto": "A LISBOA MASSAGEM EU CONSTRUÍ DO ZERO.", "destaque": "HOJE SÃO MAIS DE 90 TERAPEUTAS."},
  {"tipo": "foto", "foto": P("19225277"), "foco_y": 0.45, "faixa": "O QUE EU VEJO",
   "texto": "O BARBEIRO QUE CORTA, RESPONDE O WHATSAPP E MONTA A ESCALA ENTRE UM CLIENTE E OUTRO."},
  {"tipo": "foto", "foto": P("39259258"), "foco_y": 0.45, "faixa": "E TAMBÉM",
   "texto": "O PERSONAL QUE GRAVA, EDITA E POSTA DEPOIS DAS 22H.", "destaque": "ÀS 6H JÁ ESTÁ NA ACADEMIA."},
  {"tipo": "branco", "blocos": [
   ["h", "ANTES DE CONTRATAR, ESCREVA COMO VOCÊ FAZ."], ["esp", 8],
   ["n", "Ninguém assume uma tarefa que só existe na sua cabeça."],
   ["n", "Faça esta semana: anote o que você fez de segunda a sexta e o tempo de cada coisa. Marque S no que só você pode fazer (atender, vender) e P no que outra pessoa faria com um passo a passo escrito. Exemplo ilustrativo: confirmar agendamentos, 6 horas por semana."]]},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "faixa": "SALVE E COMENTE CLIENTES",
   "texto": "COM QUANTOS P VOCÊ ACHOU. EU TE CHAMO NO DIRECT E A GENTE VÊ QUAL SAI DA SUA MÃO PRIMEIRO.",
   "destaque": "O QUE SÓ VOCÊ PODE FAZER?"},
]}

LEGENDAS = {
 1: """Saía do restaurante à meia-noite e ia trabalhar num clube até as 8 da manhã.

Era o meu fim de semana em Lisboa. 12 horas no restaurante, onde em 6 meses eu virei subgerente, e depois 8 horas de clube por 60 € a noite. Eu precisava de 800 a 900 € por mês para viver e recebia 700 €. A conta eu fechava vendendo mais horas; nos primeiros 5 meses, vendia até a folga.

Ali eu aprendi uma coisa: quem só vende hora trabalha mais para ganhar o mesmo. O dia não passa de 24 horas.

A mesma hora pode valer o dobro. Exemplo ilustrativo de um personal: 1 aula individual a 30 €. A mesma hora em dupla, a 20 € por pessoa, vira 40 €. Na fisio, pilates clínico com 3 pacientes. Na barbearia, o pacote pai e filho.

Faça hoje: escolha 2 horários vazios da semana e ofereça como treino em dupla a 4 alunos atuais. Mensagem: "Abri 2 horários em dupla, 20 € por pessoa. Quer treinar com alguém que você conhece?"

🔻 Salve e comente CLIENTES. Eu te chamo no direct e a gente escolhe qual dos seus horários vira dupla.

#brasileirosemportugal #historiareal #empreendedorismo #donodenegocio #personaltrainer""",
 2: """Íamos ao shopping só para usar o Wi-Fi. Dava para um sorvete só, e a gente dividia.

Era ali que eu e a minha namorada procurávamos formas de ganhar dinheiro. Aos 18 eu tinha perdido os dois empregos ao mesmo tempo. A gente testou chinelo com pérolas, cosméticos e joias. Depois, água na praia com uma bicicleta enferrujada. O dinheiro da água era para casar.

A gente começou de onde estava, sem vergonha do começo.

Muito dono parado no mesmo faturamento espera sobrar dinheiro para anúncio, fotógrafo ou perfil novo. Você já tem mais do que eu tinha naquele shopping.

Faça hoje com o que já tem: peça a 3 clientes fiéis um áudio de 20 segundos dizendo o que mudou desde que começaram com você. Exemplo de um personal: "subi a escada do metrô sem parar". Poste 1 por semana nos stories.

🔻 Envie para quem está esperando sobrar dinheiro. E comente CLIENTES que eu te chamo no direct e te mostro como usar os 3 áudios.

#historiareal #casal #empreendedorismo #donodenegocio #comecardozero""",
 3: """Ele perguntou o preço e sumiu.

O que eu vejo: o dono responde o preço, espera e nunca mais escreve. Silêncio não é um não.

No mesmo dia: preço com uma pergunta no fim. "São 160 € por mês, 2 treinos por semana. Para eu te dizer se esse é o plano certo: o que você quer mudar nos próximos 3 meses?" (exemplo ilustrativo)

Dia 2: ajude antes de vender. "Quem começa do zero comigo quase sempre quer saber em quanto tempo sente diferença. Quer que eu te explique como são as 4 primeiras semanas?"

Dia 4: mostre alguém parecido. "Um aluno começou com a mesma dúvida que você. Em 8 semanas, [resultado real, com autorização dele]. Quer ver como foi o treino?" Sem caso ainda? Um vídeo de 30 s seu explicando a primeira semana.

Dia 7: convide com dia e hora. "Tenho quinta às 7h e sábado às 9h para uma avaliação de 30 minutos. Qual fica melhor?" Sem resposta, uma última: "Prefere que eu pare de te escrever? Sem problema."

Na fisio, troque a pergunta por "Onde dói e há quanto tempo?". Na barbearia, ofereça 2 horários com o nome do barbeiro.

A Two-Brain Business ensina donos de academia a fazer 6 contatos em 3 dias e depois 1 a cada 2 semanas, por 90 dias (John Franklin, 18/06/2025). Eu adaptei para quem atende sozinho.

🔻 Comente CLIENTES e o seu preço. Eu te chamo no direct e a gente escreve a sua mensagem do dia 1.

#vendas #whatsappbusiness #personaltrainer #fisioterapia #donodenegocio""",
 4: """A sua agenda não pode depender de 3 pessoas.

Aquele cliente que trazia os amigos um dia muda de cidade. O personal que lotou a agenda com a turma de um aluno só. A fisio que recebia todo mês os pacientes de um médico amigo. O barbeiro que vivia dos colegas de trabalho de um cliente. Quando essa pessoa sai, a agenda sai junto.

Hoje: abra os últimos 20 clientes e anote quem trouxe cada um.

🔻 Envie para quem tem a agenda na mão de uma pessoa só. E comente CLIENTES com quantos vieram da mesma pessoa que eu te chamo no direct.

#donodenegocio #personaltrainer #barbearia #fisioterapia #empreendedorismo""",
 5: """Por 4 anos, todo dia eu fazia a barba, engraxava a bota e deixava a cama perfeita.

Na Aeronáutica era muito grito, muita correria e troca de farda. Cama perfeita não ganha elogio; só é notada quando falta. Foi ali que eu aprendi a ser disciplinado. Depois a vida foi melhorando, e os salários também. Hoje ninguém me manda fazer a barba, e o padrão ficou.

O seu cliente também não elogia o padrão. Ele só percebe quando falta.

Escreva hoje 4 coisas que acontecem com todo cliente, sem exceção. Exemplo ilustrativo de uma fisio: 1. lembrete no WhatsApp na véspera; 2. começar no horário; 3. no fim, "O que eu posso melhorar?"; 4. mensagem 24 h depois: "Como ficou a dor hoje?". Cole a lista na parede e marque um X por cliente.

🔻 Comente CLIENTES e os seus 4 itens. Eu te chamo no direct e a gente acerta o seu padrão de atendimento.

Fotos da Aeronáutica: Robério Castro Fotografia.

#aeronautica #disciplina #historiareal #atendimento #donodenegocio""",
 6: """Eu não acredito em fazer tudo sozinho para sempre.

Eu já fiz o conteúdo, os anúncios e o atendimento, tudo sozinho. Funcionou: em 5 meses saí de 1.500 € para 5.500 € por mês. A Lisboa Massagem eu construí do zero, e hoje são mais de 90 terapeutas.

O que eu vejo: o barbeiro que corta, responde o WhatsApp e monta a escala entre um cliente e outro. O personal que grava, edita e posta depois das 22h, e às 6h já está na academia.

Antes de contratar, escreva como você faz. Ninguém assume uma tarefa que só existe na sua cabeça.

Faça esta semana: anote o que você fez de segunda a sexta e o tempo de cada coisa. Marque S no que só você pode fazer (atender, vender) e P no que outra pessoa faria com um passo a passo escrito. Exemplo ilustrativo: confirmar agendamentos, 6 horas por semana.

🔻 Salve e comente CLIENTES com quantos P você achou. Eu te chamo no direct e a gente vê qual sai da sua mão primeiro.

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
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}" + ("b" if n in (1, 2, 4, 6) else "")
    for n in range(1, 7):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(clube, O(1)); run(shopping, O(2)); run(followup, O(3))
    run(legenda, O(4), "render_legenda.py")
    run(farda, O(5)); run(sozinho, O(6))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
