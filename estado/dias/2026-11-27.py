"""Plano 100 mil, semana 5 do PDF (leitura e corte, dia 7), 27/11/2026, sexta. Dia 21 do "Plano de 30 dias para lançar
a mentoria": conteúdo "O que aprendi na primeira semana com os alunos" (sem resultado de aluno confirmado: fica como roteiro
de memória para o dono preencher; não vira post) e tarefa "Revisão da semana 3 e pedir autorização para usar resultados".
Grade do playbook (ajustes de 10/11, 16/11, 18/11, 19/11 e 23/11 prevalecem sobre a tarefa agendada): 7 posts, sem post de IA.
Sexta: 10:30 NOTÍCIA · 12:40 CONEXÃO · 14:20 CONEXÃO · 17:40 VALOR com rosto · 19:10 LEGENDA · 20:30 PROVA (remodelado) · 22:15 BANDEIRA.
Sem material novo no Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna, meus-videos-falando): sem repost.
Fotos: só do Liuri (sem a ex-esposa), nenhum frame de vídeo, nenhuma criança. Indicação: 0 de 7 posts.
CTA (rodízio sobre 26/11, todos terminam em "Comente CLIENTES"):
10:30 salvar · 12:40 comentário · 14:20 envio · 17:40 comentário · 19:10 salvar · 20:30 envio · 22:15 comentário.
1) 10:30 NOTÍCIA: Procon de João Pessoa, preços de academia (ParaibaOnline, 24/11/2026).
2) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): subgerente em 6 meses e posto para fora por um conflito. Item 15.
3) 14:20 FAIXA, conexão, pilar 6 (lição pilar 1): 5,02 km em 27:29, o pace. Print da corrida + item 10.
4) 17:40 FAIXA, valor com rosto, pilar 3: chão e teto do preço (molde @codiesanchez, BigDeal 10/09/2026).
5) 19:10 LEGENDA, bandeira falada, pilar 2: o seu concorrente não é o problema. Fato do playbook (cliente de ~300 €/mês).
6) 20:30 FAIXA, PROVA, pilar 5: Revolut jul/ago/set (prints da prova-social). REMODELADO de liurialves:6b026fd4024796909222f84f.
7) 22:15 FAIXA, bandeira, pilar 2: mais horas não resolvem faturamento parado. Itens 13, 17 e 18 como fatos de apoio.
"""
import json, os, subprocess
R = "/home/claude/carrosseis"
S = "/tmp/claude-0/-home-claude-carrosseis/d5417ebf-47e2-5eaa-b84e-410900bbed97/scratchpad"
DIA = "2026-11-27"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h27/{x}.jpg"           # fotos/historia-portugal e prova-social (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px27/pexels-{x}.jpg"

# 1) 10:30 NOTÍCIA, CAPA + ESCURO, CTA = SALVAR + CLIENTES
noticia = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": P("4164763"), "foco_y": 0.5, "etiqueta": "Notícia",
   "titulo": "Mesma cidade, mesmo plano básico de academia: de R$ 75 a R$ 180.",
   "sub": "Procon de João Pessoa (24/11/2026). O que isso muda para personal, fisio e barbearia."},
  {"etiqueta": "O número", "frase": "[[140%]] de diferença no plano básico.",
   "texto": "O Procon de João Pessoa visitou 16 academias no dia 19 de novembro e comparou 49 tipos de plano. Nas academias tradicionais, o plano básico vai de R$ 75,00 a R$ 180,00. São R$ 105,00 de diferença."},
  {"etiqueta": "O que quase ninguém leu", "frase": "No plano anual, a mensalidade cai para [[R$ 60]].",
   "texto": "Semestral: de R$ 65,00 a R$ 148,00. Anual: de R$ 60,00 a R$ 129,00. Até na academia mais cara da pesquisa, quem fecha por 12 meses paga menos por mês."},
  {"etiqueta": "E tem mais", "frase": "Nas redes, a diferença cai para [[49%]].",
   "texto": "Nas academias de rede, o básico vai de R$ 99,90 a R$ 149,00. E a natação fica fora do pacote: numa das academias, R$ 139 no trimestral, R$ 124 no semestral e R$ 108 no anual."},
  {"etiqueta": "O que eu acredito", "frase": "Quem cobra R$ 180 [[não está errado]].",
   "texto": "O problema não é ser o mais caro da cidade. É o cliente não saber por que você custa mais. Preço sem explicação vira comparação de número."},
  {"etiqueta": "No seu negócio", "frase": "Uma escada de [[3 planos]].",
   "texto": "Exemplo ilustrativo de um personal: aula avulsa a 35 €; plano de 8 aulas por mês a 240 €; trimestral a 220 € por mês, com avaliação física incluída. O cliente escolhe o compromisso e você ganha previsibilidade."},
  {"etiqueta": "Faça hoje", "frase": "[[3 linhas]] na sua tabela.",
   "texto": "1. Escreva o que está incluído em cada plano, não só o preço. 2. Crie uma opção de compromisso mais longo com mensalidade menor. 3. Mande a tabela nova para 5 clientes que hoje pagam avulso."},
  {"etiqueta": "Próximo passo", "frase": "[[Salve]] e comente CLIENTES.",
   "texto": "Eu te chamo no direct e a gente monta a sua escada de planos."},
]}

# 2) 12:40 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
subgerente = {"slides": [
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "LISBOA, O PRIMEIRO ANO",
   "texto": "EM 6 MESES EU VIREI SUBGERENTE. BASTOU UM CONFLITO PARA EU SAIR."},
  {"tipo": "foto", "foto": P("17466552"), "foco_y": 0.45, "faixa": "O COMEÇO",
   "texto": "UM RESTAURANTE E UM ESTÁGIO AO MESMO TEMPO.", "destaque": "O ESTÁGIO ACABOU EM 2 MESES."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.35, "faixa": "12 HORAS POR DIA",
   "texto": "EU FIQUEI NO RESTAURANTE.", "destaque": "EM 6 MESES, SUBGERENTE."},
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.3, "faixa": "E AÍ",
   "texto": "UM CONFLITO COM UM GERENTE.", "destaque": "E EU FUI COLOCADO PARA FORA."},
  {"tipo": "foto", "foto": HP("69"), "foco_y": 0.55, "faixa": "O QUE ISSO MOSTRA",
   "texto": "O MEU MÊS DEPENDIA DE UMA PESSOA SÓ.", "destaque": "E NÃO ERA EU."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.35, "faixa": "DEPOIS",
   "texto": "FUI GERENTE NOUTRO RESTAURANTE. SAÍ COM 3 MESES.", "destaque": "ENTREGUEI A CARTA: NÃO IA MAIS TRABALHAR PARA NINGUÉM."},
  {"tipo": "branco", "blocos": [
   ["h", "NO SEU NEGÓCIO, NENHUM CLIENTE PODE SER O SEU GERENTE."], ["esp", 8],
   ["n", "Se um cliente sozinho paga mais de 20% do seu mês, ele decide por você. Quando ele sai, o mês acaba."],
   ["n", "Exemplo ilustrativo de um personal que fatura 2.500 €: uma empresa paga 1.000 € por mês pelas aulas da equipe. São 40%. Faça hoje: liste os 5 clientes que mais pagam e a % de cada um no mês."]]},
  {"tipo": "foto", "foto": FL("selfie-sem-camisa-serio"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E A % DO SEU MAIOR CLIENTE. EU TE CHAMO NO DIRECT.",
   "destaque": "QUEM DECIDE O SEU MÊS?"},
]}

# 3) 14:20 FAIXA, CONEXÃO (vida de quem empreende), CTA = ENVIO + CLIENTES
pace = {"slides": [
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "O NÚMERO QUE EU OLHO",
   "texto": "CORRI 5,02 KM EM 27:29. O NÚMERO QUE IMPORTA NÃO É NENHUM DESSES."},
  {"tipo": "foto", "foto": FL("print-corrida-5km"), "foco_y": 0.4, "faixa": "O PRINT",
   "texto": "5,02 KM. 27 MINUTOS E 29 SEGUNDOS.", "destaque": "NO MEIO, O QUE EU OLHO: 5'28\" POR QUILÔMETRO."},
  {"tipo": "foto", "foto": HP("40"), "foco_y": 0.3, "faixa": "ONDE EU APRENDI ISSO",
   "texto": "NA AERONÁUTICA: GRITO, CORRERIA, TROCA DE FARDA.", "destaque": "CAMA PERFEITA E BARBA FEITA TODO DIA."},
  {"tipo": "foto", "foto": HP("41"), "foco_y": 0.3, "faixa": "O QUE A FARDA ENSINA",
   "texto": "UM DIA BOM NÃO MUDA NADA.", "destaque": "O RITMO DE TODO DIA MUDA."},
  {"tipo": "foto", "foto": P("39074079"), "foco_y": 0.5, "faixa": "NO SEU NEGÓCIO",
   "texto": "O DONO ESTAGNADO OLHA SÓ O TOTAL DO MÊS.", "destaque": "E NÃO SABE O PRÓPRIO RITMO."},
  {"tipo": "foto", "foto": HP("49"), "foco_y": 0.25, "faixa": "O PACE DO NEGÓCIO",
   "texto": "QUANTOS CLIENTES NOVOS ENTRAM POR SEMANA?", "destaque": "É ESSE NÚMERO QUE DIZ SE A META VEM."},
  {"tipo": "branco", "blocos": [
   ["h", "CALCULE O SEU RITMO EM 15 MINUTOS."], ["esp", 8],
   ["n", "Some os clientes novos das últimas 4 semanas e divida por 4. Esse é o seu pace."],
   ["n", "Exemplo ilustrativo de um personal: 6 alunos novos em 4 semanas = 1,5 por semana. Com 12 alunos hoje e meta de 20, faltam 8. Nesse ritmo, se ninguém sair, são mais de 5 semanas. Meta desta semana: 2 novos."]]},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-2"), "foco_y": 0.2, "faixa": "ENVIE PARA QUEM SÓ OLHA O TOTAL",
   "texto": "E COMENTE CLIENTES COM O SEU RITMO. EU TE CHAMO NO DIRECT.",
   "destaque": "QUANTOS CLIENTES NOVOS POR SEMANA?"},
]}

# 4) 17:40 FAIXA, VALOR COM ROSTO, CTA = COMENTÁRIO + CLIENTES
preco = {"slides": [
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "grande": True, "arraste": True,
   "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "ANTES DE MEXER NO PREÇO, DEFINA O CHÃO E O TETO."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "O QUE EU VEJO",
   "texto": "O DONO SOBE 2 € E PEDE DESCULPA NA MENSAGEM.", "destaque": "O CLIENTE ENTENDE QUE NEM ELE ACREDITA NO PREÇO."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "O CHÃO: QUANTO VOCÊ PRECISA"], ["esp", 8],
   ["n", "Custos do mês + quanto você quer tirar, dividido pelos atendimentos que cabem na sua agenda."],
   ["n", "Exemplo ilustrativo de uma barbearia: 1.400 € de custos + 1.600 € de retirada = 3.000 €. Cabem 160 cortes no mês. Chão: 18,75 € por corte. Abaixo disso, você paga para trabalhar."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "O TETO: O QUE A SUA CIDADE JÁ PAGA"], ["esp", 8],
   ["n", "Anote os 3 preços mais altos da sua cidade para o mesmo serviço."],
   ["n", "Em João Pessoa, o Procon achou o plano básico de academia de R$ 75 a R$ 180 na mesma cidade (24/11/2026). Alguém já paga o preço de cima."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "ESCOLHA O PONTO E MOSTRE O PORQUÊ"], ["esp", 8],
   ["n", "Entre o chão e o teto, o preço sobe com o que o cliente enxerga: horário garantido, acompanhamento, resultado."],
   ["n", "Escreva 3 linhas do que está incluído. Se não cabe em 3 linhas, o cliente também não vai entender."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "AVISE SEM PEDIR DESCULPA"], ["esp", 8],
   ["n", "Copie: \"A partir de 1 de janeiro, o corte + barba passa a 25 €. Quem marcar até 31/12 mantém o valor atual na próxima visita.\""],
   ["n", "Uma mensagem, com data e com motivo para marcar agora. Sem \"infelizmente\"."]]},
  {"tipo": "branco", "blocos": [
   ["h", "A CONTA QUE TIRA O MEDO"], ["esp", 8],
   ["n", "Exemplo ilustrativo: 160 cortes a 18 € = 2.880 €."],
   ["n", "Com 20 €, mesmo perdendo 10 cortes no mês: 150 × 20 € = 3.000 €. Mais dinheiro e menos horas na cadeira."]]},
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente-editada"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "E O SEU PREÇO DE HOJE. EU TE CHAMO NO DIRECT E A GENTE CALCULA O SEU CHÃO.",
   "destaque": "QUANDO FOI O SEU ÚLTIMO AUMENTO?"},
]}

# 5) 19:10 LEGENDA (fotos reais do Liuri, foto preenchida), bandeira falada, CTA = SALVAR + CLIENTES
legenda = {"slides": [
 {"fotos": [FL("selfie-jaqueta-verde"), HP("49")], "foco": [0.3, 0.25], "textos": ["Eu acho que o seu concorrente", "não é o problema."]},
 {"fotos": [FL("home-office-headset"), HP("41")], "foco": [0.35, 0.3], "textos": ["O cliente compara o que vê.", "E na sua página ele não vê nada."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-1"), HP("60")], "foco": [0.2, 0.3], "textos": ["O personal perde para a academia de 30 €", "e nunca mostrou o que um aluno ganhou."]},
 {"fotos": [FL("lagoa-biceps-de-frente"), HP("05")], "foco": [0.3, 0.35], "textos": ["A fisio perde para a clínica do lado", "e responde o paciente no dia seguinte."]},
 {"fotos": [FL("dunas-punhos-camisa-preta-3"), HP("47")], "foco": [0.2, 0.2], "textos": ["O barbeiro perde para o corte de 10 €", "e não tem plano para quem vem todo mês."]},
 {"fotos": [FL("selfie-sem-camisa-serio"), HP("70")], "foco": [0.3, 0.3], "textos": ["Um cliente meu paga cerca de 300 € por mês.", "E não compra pelo preço."]},
 {"fotos": [f"{R}/assets/foto-perfil-liuri.jpg", HP("71")], "foco": [0.3, 0.3], "textos": ["Hoje: escreva 3 diferenças suas", "e coloque na bio e num destaque."]},
 {"fotos": [f"{R}/assets/avatar-liuri.jpg", FL("dunas-punhos-camisa-preta-2")], "foco": [0.3, 0.2], "textos": ["Salve para fazer hoje", "e comente CLIENTES."]},
]}

# 6) 20:30 FAIXA, PROVA (REMODELADO), CTA = ENVIO + CLIENTES
prova = {"slides": [
  {"tipo": "foto", "foto": FL("lagoa-biceps-de-frente"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "PROVA · A MINHA CONTA PESSOAL",
   "texto": "EM SETEMBRO ENTRARAM 5.135 € NA MINHA CONTA. SOBRARAM 124 €."},
  {"tipo": "foto", "foto": HP("prova-revolut-setembro"), "foco_y": 1.0, "faixa": "O PRINT DE SETEMBRO",
   "texto": "ENTRARAM 5.135 €.", "destaque": "SAÍRAM 5.011 €. SOBRARAM 124 €."},
  {"tipo": "foto", "foto": HP("prova-revolut-julho"), "foco_y": 1.0, "faixa": "JULHO",
   "texto": "ENTRARAM 4.669 €.", "destaque": "SAÍRAM 5.257 €. FECHEI O MÊS EM -589 €."},
  {"tipo": "foto", "foto": HP("prova-revolut-agosto"), "foco_y": 1.0, "faixa": "AGOSTO",
   "texto": "ENTRARAM 6.849 €.", "destaque": "2.181 € A MAIS QUE EM JULHO. O GASTO SUBIU 48 €. SOBRARAM 1.544 €."},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-3"), "foco_y": 0.2, "faixa": "POR QUE EU MOSTRO ISSO",
   "texto": "O MÊS FRACO TAMBÉM É REAL.", "destaque": "EU JÁ QUEBREI UMA LOJA SEM OLHAR ESSES NÚMEROS."},
  {"tipo": "branco", "blocos": [
   ["h", "O QUE OS 3 MESES MOSTRAM"], ["esp", 8],
   ["n", "O gasto ficou perto de 5.000 € nos três meses: 5.257 €, 5.306 € e 5.011 €."],
   ["n", "O que separou o mês no vermelho do mês que sobrou dinheiro foi quanto entrou. Não foi um corte de gasto."]]},
  {"tipo": "branco", "blocos": [
   ["h", "FAÇA A SUA EM 20 MINUTOS."], ["esp", 8],
   ["n", "Abra o extrato dos últimos 3 meses e escreva, mês a mês: entrou, saiu, sobrou."],
   ["n", "Se o gasto é parecido todo mês, a sua alavanca é a entrada. Exemplo ilustrativo de um personal com 3.000 € de custo fixo: com 13 alunos a 230 € (2.990 €), ainda fecha no vermelho. Com 15 (3.450 €), sobram 450 €."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM NUNCA ABRE O EXTRATO",
   "texto": "E COMENTE CLIENTES. EU TE CHAMO NO DIRECT E A GENTE OLHA AS SUAS ENTRADAS.",
   "destaque": "QUANTO SOBROU NO SEU ÚLTIMO MÊS?"},
]}

# 7) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = COMENTÁRIO + CLIENTES
horas = {"slides": [
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO QUE MAIS HORAS RESOLVEM FATURAMENTO PARADO."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.3, "faixa": "POR QUE EU DIGO ISSO",
   "texto": "NOS PRIMEIROS 5 MESES EM LISBOA: 12 HORAS POR DIA.", "destaque": "E EU AINDA VENDIA A FOLGA."},
  {"tipo": "foto", "foto": P("36765600"), "foco_y": 0.4, "faixa": "NOS FINS DE SEMANA",
   "texto": "SAÍA À MEIA-NOITE E IA PARA UM CLUBE ATÉ AS 8.", "destaque": "60 € A NOITE."},
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.3, "faixa": "E NO FIM DO MÊS",
   "texto": "EU PRECISAVA DE 800 A 900 €.", "destaque": "RECEBIA 700 €."},
  {"tipo": "foto", "foto": P("6550849"), "foco_y": 0.4, "faixa": "O QUE EU VEJO HOJE",
   "texto": "O PERSONAL QUE ABRE HORÁRIO ÀS 6 DA MANHÃ E ÀS 10 DA NOITE.", "destaque": "COM O MESMO PREÇO DE 3 ANOS ATRÁS."},
  {"tipo": "foto", "foto": P("12304516"), "foco_y": 0.4, "faixa": "E TAMBÉM",
   "texto": "O BARBEIRO QUE ABRE NO DOMINGO", "destaque": "PARA COBRIR O QUE FALTOU NA SEMANA."},
  {"tipo": "branco", "blocos": [
   ["h", "DIVIDA O SEU MÊS PELAS SUAS HORAS."], ["esp", 8],
   ["n", "Faturamento do mês ÷ horas trabalhadas = quanto você ganha por hora. Faça essa conta antes de abrir mais um horário."],
   ["n", "Exemplo ilustrativo de um personal: 2.400 € em 200 horas = 12 € por hora. Com 10 alunos num plano de 8 aulas a 280 €, são 2.800 € em 80 horas de aula: 35 € por hora."]]},
  {"tipo": "foto", "foto": FL("dunas-punhos-camisa-preta-1"), "foco_y": 0.2, "faixa": "COMENTE CLIENTES",
   "texto": "E QUANTO VOCÊ GANHA POR HORA. EU TE CHAMO NO DIRECT.",
   "destaque": "QUANTAS HORAS VOCÊ TRABALHOU ESTA SEMANA?"},
]}

LEGENDAS = {
 1: """Mesma cidade, mesmo plano básico de academia: de R$ 75 a R$ 180.

O Procon de João Pessoa visitou 16 academias no dia 19 de novembro e comparou 49 tipos de plano. Nas academias tradicionais, o plano básico vai de R$ 75,00 a R$ 180,00: 140% de diferença.

O detalhe que quase ninguém leu: no plano anual, a mensalidade cai. Semestral de R$ 65,00 a R$ 148,00; anual de R$ 60,00 a R$ 129,00. Até na academia mais cara da pesquisa, quem fecha por 12 meses paga menos por mês. Nas redes, o básico vai de R$ 99,90 a R$ 149,00, e a natação é vendida à parte.

O que eu acredito: quem cobra R$ 180 não está errado. O problema é o cliente não saber por que você custa mais.

Exemplo ilustrativo de um personal: aula avulsa a 35 €; plano de 8 aulas por mês a 240 €; trimestral a 220 € por mês, com avaliação física incluída.

Faça hoje:
1. Escreva o que está incluído em cada plano, não só o preço.
2. Crie uma opção de compromisso mais longo com mensalidade menor.
3. Mande a tabela nova para 5 clientes que hoje pagam avulso.

🔻 Salve para montar a sua tabela. E comente CLIENTES que eu te chamo no direct e a gente monta a sua escada de planos.

Fonte: ParaibaOnline, com Secom/JP ("Pesquisa mostra preços das mensalidades nas academias de ginástica em João Pessoa", 24/11/2026), pesquisa do Procon-JP.

#academia #personaltrainer #preco #donodenegocio #fisioterapia""",
 2: """Em 6 meses eu virei subgerente. Bastou um conflito para eu sair.

Em Lisboa, eu trabalhava num restaurante junto com um estágio. O estágio acabou em 2 meses e eu fiquei no restaurante, 12 horas por dia. Em 6 meses, subgerente. Aí veio um conflito com um gerente e eu fui colocado para fora.

Depois fui gerente noutro restaurante conhecido. Saí com 3 meses, entreguei a carta e decidi que não ia mais trabalhar para ninguém.

O que essa fase mostra: o meu mês dependia de uma pessoa só. No seu negócio, nenhum cliente pode ser o seu gerente.

Se um cliente sozinho paga mais de 20% do seu mês, ele decide por você. Exemplo ilustrativo de um personal que fatura 2.500 €: uma empresa paga 1.000 € por mês pelas aulas da equipe. São 40%. Quando ela sai, o mês acaba.

Faça hoje: liste os 5 clientes que mais pagam e a % de cada um no seu mês.

🔻 Comente CLIENTES e a % do seu maior cliente. Eu te chamo no direct.

#brasileirosemportugal #historiareal #donodenegocio #personaltrainer #gestaofinanceira""",
 3: """Corri 5,02 km em 27:29. O número que importa não é nenhum desses.

É o do meio: 5'28" por quilômetro. O ritmo.

Eu aprendi isso na Aeronáutica. Grito, correria, troca de farda, cama perfeita e barba feita todo dia. Um dia bom não muda nada. O ritmo de todo dia muda.

No negócio, o dono estagnado olha só o total do mês e não sabe o próprio ritmo. O pace do negócio é quantos clientes novos entram por semana.

Calcule o seu em 15 minutos: some os clientes novos das últimas 4 semanas e divida por 4.

Exemplo ilustrativo de um personal: 6 alunos novos em 4 semanas = 1,5 por semana. Com 12 alunos hoje e meta de 20, faltam 8. Nesse ritmo, se ninguém sair, são mais de 5 semanas. Meta desta semana: 2 novos.

🔻 Envie para quem só olha o total do mês. E comente CLIENTES com o seu ritmo que eu te chamo no direct.

Fotos da Aeronáutica: Robério Castro Fotografia.

#disciplina #corrida #donodenegocio #personaltrainer #academia""",
 4: """Antes de mexer no preço, defina o chão e o teto.

O que eu mais vejo: o dono sobe 2 € e pede desculpa na mensagem. O cliente entende que nem ele acredita no preço.

1. O chão: custos do mês + quanto você quer tirar, dividido pelos atendimentos que cabem na agenda. Exemplo ilustrativo de uma barbearia: 1.400 € de custos + 1.600 € de retirada = 3.000 €. Cabem 160 cortes. Chão: 18,75 € por corte.
2. O teto: anote os 3 preços mais altos da sua cidade para o mesmo serviço. Em João Pessoa, o Procon achou o plano básico de academia de R$ 75 a R$ 180 na mesma cidade (24/11/2026).
3. Escolha o ponto e mostre o porquê: 3 linhas do que está incluído.
4. Avise sem pedir desculpa. Copie: "A partir de 1 de janeiro, o corte + barba passa a 25 €. Quem marcar até 31/12 mantém o valor atual na próxima visita."

A conta que tira o medo, exemplo ilustrativo: 160 cortes a 18 € = 2.880 €. Com 20 €, mesmo perdendo 10 cortes: 150 × 20 € = 3.000 €. Mais dinheiro e menos horas na cadeira.

🔻 Comente CLIENTES e o seu preço de hoje. Eu te chamo no direct e a gente calcula o seu chão.

#preco #barbearia #personaltrainer #fisioterapia #donodenegocio""",
 5: """Eu acho que o seu concorrente não é o problema.

O cliente compara o que vê. O personal perde para a academia de 30 € e nunca mostrou o que um aluno ganhou. A fisio perde para a clínica do lado e responde o paciente no dia seguinte. O barbeiro perde para o corte de 10 € e não tem plano para quem vem todo mês.

Um cliente meu paga cerca de 300 € por mês. E não compra pelo preço.

Hoje: escreva 3 diferenças suas e coloque na bio e num destaque.

🔻 Salve para fazer hoje. E comente CLIENTES que eu te chamo no direct.

Fotos da Aeronáutica: Robério Castro Fotografia.

#concorrencia #donodenegocio #personaltrainer #fisioterapia #barbearia""",
 6: """Em setembro entraram 5.135 € na minha conta pessoal. Sobraram 124 €.

Os prints estão nos slides. Julho: entraram 4.669 € e saíram 5.257 €, fechei em -589 €. Agosto: entraram 6.849 €, 2.181 € a mais, o gasto subiu 48 € e sobraram 1.544 €. Setembro: 5.135 € de entrada, 5.011 € de gasto, 124 €.

Eu mostro o mês fraco também. Eu já quebrei uma loja sem olhar esses números.

O que os 3 meses mostram: o gasto ficou perto de 5.000 € nos três. O que separou o mês no vermelho do mês que sobrou dinheiro foi quanto entrou. Não foi um corte de gasto.

Faça a sua em 20 minutos: abra o extrato dos últimos 3 meses e escreva, mês a mês, entrou, saiu, sobrou. Se o gasto é parecido todo mês, a sua alavanca é a entrada. Exemplo ilustrativo de um personal com 3.000 € de custo fixo: com 13 alunos a 230 € (2.990 €), ainda fecha no vermelho. Com 15 (3.450 €), sobram 450 €.

Na mentoria, o mês 2 inclui olhar esses números com você toda semana: entrou, saiu, sobrou e falta receber.

🔻 Envie para quem nunca abre o extrato. E comente CLIENTES que eu te chamo no direct e a gente olha as suas entradas.

#prova #gestaofinanceira #donodenegocio #brasileirosemportugal #personaltrainer""",
 7: """Eu não acredito que mais horas resolvem faturamento parado.

Nos primeiros 5 meses em Lisboa, eu trabalhava 12 horas por dia e ainda vendia a folga. Nos fins de semana, saía do restaurante à meia-noite e ia para um clube até as 8 da manhã, por 60 € a noite. No fim do mês, eu precisava de 800 a 900 € e recebia 700 €.

Hoje eu vejo o personal que abre horário às 6 da manhã e às 10 da noite com o mesmo preço de 3 anos atrás. E o barbeiro que abre no domingo para cobrir o que faltou na semana.

Divida o seu mês pelas suas horas antes de abrir mais um horário. Exemplo ilustrativo de um personal: 2.400 € em 200 horas = 12 € por hora. Com 10 alunos num plano de 8 aulas a 280 €, são 2.800 € em 80 horas de aula: 35 € por hora.

🔻 Comente CLIENTES e quanto você ganha por hora. Eu te chamo no direct.

Fotos da Aeronáutica: Robério Castro Fotografia.

#donodenegocio #empreendedorismo #personaltrainer #barbearia #brasileirosemportugal""",
}


def run(cfg, out, script="render_faixa.py"):
    if script == "render_faixa.py":  # "€" nunca fica sozinho na linha
        for sl in cfg["slides"]:
            for k in ("texto", "destaque"):
                if k in sl: sl[k] = sl[k].replace(" €", "\u00a0€")
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
    run(subgerente, O(2)); run(pace, O(3)); run(preco, O(4))
    run(legenda, O(5), "render_legenda.py")
    run(prova, O(6))
    run(horas, O(7))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
