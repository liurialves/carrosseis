"""Plano 100 mil, semana 4 do PDF (janela de testes, dia 1), 14/11/2026, sábado. Dia 8 do "Plano de 30 dias para lançar
a mentoria": conteúdo "Rotina real: treino de MMA cedo, trabalho depois" (vai para os stories) e tarefa "Abrir lista de
espera do desafio nos Stories" (material pronto no doc).
AJUSTE DO DONO EM 10/11 (prevalece sobre a tarefa agendada em quantidade, horários e formato): 5 posts, sem post de IA.
Sábado: 12:40 CONEXÃO · 14:20 CONEXÃO · 17:40 VALOR com rosto · 20:30 CONEXÃO · 22:15 BANDEIRA.
AJUSTE DE 11/11: "indicação" só no valor das 17:40 (ângulo "como você me achou?"), 1 de 5 posts.
Sem prints novos nas pastas do Drive (prova-social, clonar-ia, referencias-99hud, repost-modocaverna): sem repost.
CTA (rodízio, todos terminam em "Comente CLIENTES"): 12:40 comentário · 14:20 salvar · 17:40 envio · 20:30 envio · 22:15 comentário.
1) 12:40 FAIXA, conexão, pilar 5 (lição pilar 3 oferta): "Vendi água na praia com uma bicicleta enferrujada." Itens 3, 4, 5.
   REMODELADO de liurialves:6af691e95ec1c9d5be5c5009 (noivado, 591 views): arco do casal, capa do casal jovem.
2) 14:20 FAIXA, conexão, pilar 5 (lição pilar 4): "Aos 18 anos eu perdi os dois empregos ao mesmo tempo. Um deles era
   numa academia." Itens 2 e 6. REMODELADO de liurialves:6af5405e8a1a2f52b522312d (quarto dos três, 611 views): cena
   dura com número + lição de conta. Molde de lista de trabalhos: Moisés Leal (@moisesleall, ABC da Comunicação 22/05/2026).
3) 17:40 FAIXA, valor, pilar 1: "De onde veio o seu último cliente?" (pergunta + planilha de 5 colunas). Molde Gymdesk
   (30/09/2026, 74,8% dos donos de academia não sabem o custo de um aluno novo).
4) 20:30 FAIXA, conexão, pilar 6 (lição pilar 2): "Na Aeronáutica eu precisava de autorização até para tirar férias."
   Itens 9, 10 e 12.
5) 22:15 FAIXA, bandeira, pilar 6 (lição pilar 1): "Eu não acredito em atender cliente no improviso." 252 € → 1.755 €.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/f0f02111-1cbf-5ac1-9fd5-394d98e1fa84/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-14"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h14/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px14/pexels-{x}.jpg"

# 1) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = COMENTÁRIO + CLIENTES
agua = {"slides": [
  {"tipo": "foto", "foto": HP("08"), "foco_y": 0.15, "grande": True, "arraste": True, "faixa": "EU E ELA, ANTES DE QUALQUER EMPRESA",
   "texto": "VENDI ÁGUA NA PRAIA COM UMA BICICLETA ENFERRUJADA. ALI EU APRENDI O QUE É OFERTA."},
  {"tipo": "foto", "foto": HP("38"), "foco_y": 0.2, "faixa": "O COMEÇO",
   "texto": "A GENTE IA AO SHOPPING SÓ PARA USAR O WI-FI E PROCURAR UM JEITO DE GANHAR DINHEIRO.",
   "destaque": "DINHEIRO PARA UM SORVETE SÓ. A GENTE DIVIDIA."},
  {"tipo": "foto", "foto": P("31504382"), "foco_y": 0.5, "faixa": "TENTATIVA 1",
   "texto": "COLAMOS PÉROLAS E ENFEITES EM CHINELOS HAVAIANAS PARA VENDER.",
   "destaque": "FICAVA BONITO. NÃO FEZ CAIXA."},
  {"tipo": "foto", "foto": HP("07"), "foco_y": 0.12, "faixa": "TENTATIVAS 2 E 3",
   "texto": "DEPOIS VIERAM OS COSMÉTICOS: AVON, BOTICÁRIO, NATURA. ELA VENDEU JOIAS E EU FUI JUNTO.",
   "destaque": "TAMBÉM NÃO FEZ CAIXA."},
  {"tipo": "foto", "foto": P("14763567"), "foco_y": 1.0, "faixa": "TENTATIVA 4",
   "texto": "AÍ FOMOS OS DOIS PARA A PRAIA VENDER ÁGUA, COM UMA BICICLETA ENFERRUJADA.",
   "destaque": "ESSA FEZ CAIXA."},
  {"tipo": "foto", "foto": P("9322159"), "foco_y": 0.5, "faixa": "POR QUE ESSA DEU CERTO",
   "texto": "NA PRAIA, NO CALOR, NINGUÉM PRECISA SER CONVENCIDO A COMPRAR ÁGUA. A PESSOA JÁ ESTÁ COM SEDE.",
   "destaque": "ERA A OFERTA MAIS FEIA E A MAIS ÓBVIA."},
  {"tipo": "foto", "foto": HP("22"), "foco_y": 0.2, "faixa": "PARA QUE ERA O DINHEIRO",
   "texto": "O DINHEIRO DA ÁGUA ERA PARA A GENTE CASAR. TEVE GENTE QUE FEZ CHACOTA: \"NÃO CASA, NÃO VALE A PENA\".",
   "destaque": "A GENTE CASOU."},
  {"tipo": "branco", "blocos": [
   ["h", "O SEU CLIENTE JÁ ESTÁ COM SEDE DE ALGUMA COISA."], ["esp", 8],
   ["n", "Personal trainer, academia e fisioterapia vendem o pacote mais bonito e esquecem o pedido que o cliente repete toda semana."],
   ["n", "Hoje: abra as últimas 20 conversas do WhatsApp e anote a frase que mais aparece. Exemplo: \"tenho dor nas costas\" ou \"quero perder a barriga até o verão\". Essa frase vira o nome da sua próxima oferta e a primeira linha da sua bio."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.2, "faixa": "COMENTE CLIENTES",
   "texto": "E A FRASE QUE OS SEUS CLIENTES MAIS REPETEM. EU TE CHAMO NO DIRECT E A GENTE TRANSFORMA ELA EM OFERTA.",
   "destaque": "QUAL É A SEDE DO SEU CLIENTE?"},
]}

# 2) 14:20 FAIXA, CONEXÃO (REMODELADO), CTA = SALVAR + CLIENTES
empregos = {"slides": [
  {"tipo": "foto", "foto": HP("33"), "foco_y": 0.2, "grande": True, "arraste": True, "faixa": "EU, AOS 18 ANOS",
   "texto": "PERDI OS DOIS EMPREGOS AO MESMO TEMPO. UM DELES ERA NUMA ACADEMIA DE ELITE."},
  {"tipo": "foto", "foto": HP("37"), "foco_y": 0.5, "faixa": "FIM DO ENSINO MÉDIO",
   "texto": "EU ESTUDAVA E TINHA DOIS TRABALHOS.",
   "destaque": "OS DOIS ACABARAM JUNTOS."},
  {"tipo": "foto", "foto": P("7735629"), "foco_y": 0.5, "faixa": "TRABALHO 1",
   "texto": "JOVEM APRENDIZ, AUXILIAR ADMINISTRATIVO NUMA CORRETORA.",
   "destaque": "O CONTRATO ERA DE 1 ANO. ACABOU."},
  {"tipo": "foto", "foto": P("30147880"), "foco_y": 0.5, "faixa": "TRABALHO 2",
   "texto": "AJUDANTE DE PERSONAL TRAINER NUMA ACADEMIA PERSONALIZADA DE ELITE."},
  {"tipo": "foto", "foto": P("38965744"), "foco_y": 0.5, "faixa": "O MOTIVO",
   "texto": "A ACADEMIA ERA DE ELITE. MESMO ASSIM, O DONO JÁ NÃO CONSEGUIA PAGAR.",
   "destaque": "FIQUEI SEM OS DOIS AO MESMO TEMPO."},
  {"tipo": "foto", "foto": HP("31"), "foco_y": 0.25, "faixa": "O QUE EU FIZ DEPOIS",
   "texto": "TESTEI TUDO PARA GANHAR DINHEIRO COM A MINHA NAMORADA. NO ALISTAMENTO, EU DISSE QUE QUERIA SERVIR.",
   "destaque": "ENTREI NA AERONÁUTICA."},
  {"tipo": "branco", "blocos": [
   ["h", "ACADEMIA BONITA TAMBÉM PARA DE PAGAR A EQUIPE."], ["esp", 8],
   ["n", "Eu não sei os números daquela academia. Sei o que vejo em quem fatura entre 1.500\u00a0€ e 5.000\u00a0€: o custo fixo chega todo mês e a entrada depende de quem aparecer."],
   ["n", "Faça hoje: some o custo fixo do mês (aluguel, equipe, sistemas) e divida pelo valor do seu plano mensal. Exemplo ilustrativo: 1.800 € ÷ 90 € = 20 planos ativos. Esse número paga a casa antes do primeiro euro de lucro. Quantos você tem hoje?"]]},
  {"tipo": "foto", "foto": HP("18"), "foco_y": 0.35, "faixa": "SALVE E FAÇA A CONTA HOJE",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E FAÇO ESSA CONTA COM VOCÊ.",
   "destaque": "QUANTOS PLANOS PAGAM A SUA CASA?"},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO, CTA = ENVIO + CLIENTES
origem = {"slides": [
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "DE ONDE VEIO O SEU ÚLTIMO CLIENTE? SE VOCÊ PRECISOU PENSAR, ISTO É PARA VOCÊ."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "O QUE EU ACREDITO",
   "texto": "NUMA PESQUISA DA GYMDESK, 74,8% DOS DONOS DE ACADEMIA NÃO SABIAM QUANTO CUSTA TRAZER UM ALUNO NOVO.",
   "destaque": "QUEM NÃO SABE DE ONDE VEM O CLIENTE INVESTE NO ESCURO."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "FAÇA A PERGUNTA EM TODA CONVERSA NOVA"], ["esp", 8],
   ["n", "Copie: \"Antes de eu te passar os horários, me conta: como você chegou até mim?\""],
   ["n", "Pergunte antes de falar de preço, enquanto a pessoa ainda está curiosa."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "UMA PLANILHA COM 5 COLUNAS"], ["esp", 8],
   ["n", "Data · nome · de onde veio · fechou (sim ou não) · valor do primeiro mês."],
   ["n", "Origens fixas, no máximo 6: Instagram, anúncio, Google, indicação, passou na porta, outro. Lista fixa é o que deixa você somar no fim do mês."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "SOME NO DIA 30"], ["esp", 8],
   ["n", "Para cada origem: quantas conversas, quantas fecharam e quanto entrou."],
   ["n", "Exemplo ilustrativo de um personal: Instagram, 14 conversas e 2 alunos. Indicação, 5 conversas e 4 alunos. Anúncio, 6 conversas e 3 alunos."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "DECIDA COM O NÚMERO"], ["esp", 8],
   ["n", "A origem que mais fecha ganha a sua primeira hora do dia."],
   ["n", "A que traz muita conversa e pouco aluno pede ajuste no atendimento. No anúncio, divida o gasto pelos alunos fechados: esse é o seu custo por cliente."]]},
  {"tipo": "foto", "foto": P("4088463"), "foco_y": 0.45, "faixa": "O ERRO QUE EU MAIS VEJO",
   "texto": "FAZER A PERGUNTA SÓ PARA PUXAR CONVERSA E NÃO ANOTAR A RESPOSTA.",
   "destaque": "EM 30 DIAS, VOCÊ SABE ONDE POR O PRÓXIMO EURO."},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.15, "faixa": "ENVIE PARA O SEU SÓCIO",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E OLHO AS ORIGENS DOS SEUS CLIENTES COM VOCÊ.",
   "destaque": "5 COLUNAS. 30 DIAS."},
]}

# 4) 20:30 FAIXA, CONEXÃO, CTA = ENVIO + CLIENTES
autorizacao = {"slides": [
  {"tipo": "foto", "foto": HP("47"), "foco_y": 0.2, "grande": True, "arraste": True, "faixa": "4 ANOS NA AERONÁUTICA",
   "texto": "EU PRECISAVA DE AUTORIZAÇÃO ATÉ PARA TIRAR FÉRIAS. FOI POR ISSO QUE EU SAÍ."},
  {"tipo": "foto", "foto": HP("13"), "foco_y": 0.3, "faixa": "O QUE A FARDA ME DEU",
   "texto": "GRITO, FORMA E CAMA PERFEITA TODO DIA. ALI EU APRENDI DISCIPLINA E PASSEI A GANHAR SALÁRIOS MELHORES.",
   "destaque": "MESMO ASSIM, EU JÁ NÃO ME SENTIA BEM."},
  {"tipo": "foto", "foto": HP("30"), "foco_y": 0.3, "faixa": "O QUE PESAVA",
   "texto": "FÉRIAS, SAIR DA CIDADE: TUDO PASSAVA POR UMA AUTORIZAÇÃO.",
   "destaque": "E NÃO HAVIA MAIS NADA PARA EU APRENDER ALI."},
  {"tipo": "foto", "foto": HP("12"), "foco_y": 0.4, "faixa": "A PROVA",
   "texto": "EXISTIA UMA PROVA QUE ME LEVARIA A OUTRO NÍVEL. EU NÃO ESTUDEI PARA ELA.",
   "destaque": "NÃO PASSEI. E SAÍ."},
  {"tipo": "foto", "foto": P("9779284"), "foco_y": 0.5, "faixa": "DEPOIS",
   "texto": "COMECEI A FAZER UBER NO BRASIL PARA FATURAR.",
   "destaque": "JÁ COM A IDEIA DE MORAR FORA."},
  {"tipo": "foto", "foto": P("3374249"), "foco_y": 0.5, "faixa": "O QUE VEIO",
   "texto": "DEPOIS VIERAM PORTUGAL, O RESTAURANTE, O CLUBE À NOITE E MAIS UBER.",
   "destaque": "HOJE A EMPRESA É MINHA. A AUTORIZAÇÃO TAMBÉM."},
  {"tipo": "branco", "blocos": [
   ["h", "EU NÃO ESTUDEI PARA A PROVA. FOI ESCOLHA MINHA."], ["esp", 8],
   ["n", "Muito dono parado no mesmo faturamento está onde eu estava: não se prepara para o próximo nível e também não muda nada."],
   ["n", "Faça hoje: escreva qual é a próxima \"prova\" do seu negócio (lançar o plano mensal, subir o preço, fazer o primeiro anúncio) e marque 3 horas por semana na agenda só para ela, durante 4 semanas."]]},
  {"tipo": "foto", "foto": FL("video-rotina-9s"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM ESPERA O MOMENTO CERTO",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E A GENTE ESCOLHE A SUA PRÓXIMA PROVA.",
   "destaque": "QUAL PROVA VOCÊ ESTÁ ADIANDO?"},
]}

# 5) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = COMENTÁRIO + CLIENTES
improviso = {"slides": [
  {"tipo": "foto", "foto": FL("video-rotina-17s"), "foco_y": 0.6, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM ATENDER CLIENTE NO IMPROVISO."},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.35, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "DE 15 A 31/10 EU COLOQUEI 252 € EM ANÚNCIOS DE MENSAGEM. VOLTARAM 1.755 € EM ATENDIMENTOS.",
   "destaque": "O ANÚNCIO TROUXE A CONVERSA. QUEM VENDEU FOI A RESPOSTA."},
  {"tipo": "foto", "foto": P("36631639"), "foco_y": 0.5, "faixa": "EXEMPLO: A ACADEMIA",
   "texto": "A PESSOA PERGUNTA O PREÇO ÀS 21H. NO DIA SEGUINTE, QUEM PEGA O CELULAR MANDA UMA FOTO DA TABELA."},
  {"tipo": "foto", "foto": P("17665771"), "foco_y": 0.5, "faixa": "EXEMPLO: A BARBEARIA",
   "texto": "CADA BARBEIRO RESPONDE DE UM JEITO. UM MANDA ÁUDIO DE 2 MINUTOS. OUTRO MANDA SÓ O VALOR."},
  {"tipo": "foto", "foto": P("5807886"), "foco_y": 0.5, "faixa": "O QUE EU DEFENDO",
   "texto": "TODA CONVERSA NOVA SEGUE O MESMO ROTEIRO ESCRITO, SEJA QUEM FOR QUE ESTEJA COM O CELULAR."},
  {"tipo": "branco", "blocos": [
   ["t", "O ROTEIRO EM 4 MENSAGENS (TROQUE OS COLCHETES)"], ["esp", 8],
   ["n", "1. \"Olá, [nome]! Obrigado por chamar. Para eu te mostrar o plano certo: qual é o seu objetivo?\""],
   ["n", "2. \"Você já fez [serviço] antes? Tem alguma dor ou restrição?\""],
   ["n", "3. \"Pelo que você me contou, o ideal é [plano], [frequência], por [valor] por mês.\""],
   ["n", "4. \"Tenho [dia] às [hora] ou [dia] às [hora]. Qual fica melhor para você?\""]]},
  {"tipo": "branco", "blocos": [
   ["h", "FAÇA HOJE"], ["esp", 8],
   ["n", "Cole as 4 mensagens nas respostas rápidas do WhatsApp Business (atalhos /1, /2, /3 e /4)."],
   ["n", "Por 7 dias, toda conversa nova passa por elas. No dia 7, conte quantas chegaram à mensagem 4 e quantas marcaram horário."]]},
  {"tipo": "foto", "foto": FL("mma-equipe-treino"), "foco_y": 0.5, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E OLHO O SEU ATENDIMENTO COM VOCÊ.",
   "destaque": "O ROTEIRO VENDE ATÉ NO DIA CANSADO."},
]}

LEGENDAS = {
 1: """Vendi água na praia com uma bicicleta enferrujada. Ali eu aprendi o que é oferta.

Antes de qualquer empresa, eu e a minha namorada íamos ao shopping só para usar o Wi-Fi e procurar um jeito de ganhar dinheiro. Tínhamos dinheiro para um sorvete só, e dividíamos. Colamos pérolas em chinelos Havaianas. Vendemos Avon, Boticário e Natura. Ela vendeu joias e eu fui junto. Nada disso fez caixa. Aí fomos os dois para a praia vender água, com uma bicicleta enferrujada. Essa fez. O dinheiro era para a gente casar, e teve quem dissesse "não casa, não vale a pena". A gente casou.

Na praia, no calor, ninguém precisa ser convencido a comprar água. No seu negócio é igual: abra as últimas 20 conversas do WhatsApp e anote a frase que mais se repete ("tenho dor nas costas", "quero perder a barriga até o verão"). Ela vira o nome da sua próxima oferta e a primeira linha da sua bio.

🔻 Comente CLIENTES e a frase que os seus clientes mais repetem. Eu te chamo no direct e a gente transforma ela em oferta.

#empreendedorismo #donodenegocio #historiareal #oferta #personaltrainer""",
 2: """Aos 18 anos eu perdi os dois empregos ao mesmo tempo. Um deles era numa academia de elite.

No fim do ensino médio eu estudava e tinha dois trabalhos: jovem aprendiz numa corretora e ajudante de personal trainer numa academia personalizada de elite. O contrato da corretora era de 1 ano e acabou. O dono da academia já não conseguia pagar. Fiquei sem os dois no mesmo momento. Testei de tudo para ganhar dinheiro com a minha namorada e, no alistamento, disse que queria servir. Entrei na Aeronáutica.

Academia bonita também para de pagar a equipe. Faça hoje: some o custo fixo do mês (aluguel, equipe, sistemas) e divida pelo valor do seu plano mensal. Exemplo ilustrativo: 1.800 € ÷ 90 € = 20 planos ativos. É o que paga a casa antes do primeiro euro de lucro. Quantos você tem hoje?

🔻 Salve e faça a conta hoje. E comente CLIENTES que eu te chamo no direct e faço essa conta com você.

Foto: Robério Castro Fotografia

#academia #personaltrainer #donodenegocio #gestaofinanceira #historiareal""",
 3: """De onde veio o seu último cliente?

Numa pesquisa da Gymdesk com donos de academia, 74,8% não sabiam quanto custa trazer um aluno novo. Quem não sabe de onde vem o cliente investe no escuro.

O método em 4 passos:
1. Em toda conversa nova, antes do preço: "Antes de eu te passar os horários, me conta: como você chegou até mim?"
2. Planilha com 5 colunas: data, nome, de onde veio, fechou (sim/não), valor do primeiro mês. Origens fixas: Instagram, anúncio, Google, indicação, passou na porta, outro.
3. No dia 30, some por origem: conversas, fechados e quanto entrou.
4. A origem que mais fecha ganha a sua primeira hora do dia. No anúncio, gasto ÷ alunos fechados = custo por cliente.

O erro que eu mais vejo: fazer a pergunta e não anotar a resposta.

🔻 Envie para o seu sócio. E comente CLIENTES que eu te chamo no direct e olho as origens dos seus clientes com você.

Dado: Gymdesk, "Lead Source Tracking for Gyms", 30/09/2026.

#academia #personaltrainer #fisioterapia #barbearia #donodenegocio""",
 4: """Na Aeronáutica eu precisava de autorização até para tirar férias. Foi por isso que eu saí.

Foram 4 anos de grito, forma e cama perfeita. Ali eu aprendi disciplina e passei a ganhar salários melhores. Mesmo assim, já não me sentia bem: férias e sair da cidade passavam por autorização, e não havia mais o que aprender. Existia uma prova que me levaria a outro nível. Eu não estudei, não passei e saí. Comecei a fazer Uber no Brasil, já com a ideia de morar fora. Depois vieram Portugal, o restaurante, o clube à noite e mais Uber. Hoje a empresa é minha.

Não estudar para a prova foi escolha minha. Muito dono parado no mesmo faturamento está onde eu estava. Faça hoje: escreva a próxima "prova" do seu negócio (lançar o plano mensal, subir o preço, fazer o primeiro anúncio) e marque 3 horas por semana na agenda só para ela, durante 4 semanas.

🔻 Envie para quem está esperando o momento certo. E comente CLIENTES que eu te chamo no direct e a gente escolhe a sua próxima prova.

Fotos: Robério Castro Fotografia

#empreendedorismo #donodenegocio #aeronautica #decisao #historiareal""",
 5: """Eu não acredito em atender cliente no improviso.

De 15 a 31/10 eu coloquei 252 € em anúncios de mensagem e voltaram 1.755 € em atendimentos. O anúncio trouxe a conversa. Quem vendeu foi a resposta.

Vejo o contrário todo dia: a academia que recebe a pergunta do preço às 21h e responde no dia seguinte com uma foto da tabela; a barbearia em que cada barbeiro responde de um jeito, um com áudio de 2 minutos, outro só com o valor.

O roteiro em 4 mensagens:
1. "Olá, [nome]! Obrigado por chamar. Para eu te mostrar o plano certo: qual é o seu objetivo?"
2. "Você já fez [serviço] antes? Tem alguma dor ou restrição?"
3. "Pelo que você me contou, o ideal é [plano], [frequência], por [valor] por mês."
4. "Tenho [dia] às [hora] ou [dia] às [hora]. Qual fica melhor para você?"

Cole nas respostas rápidas do WhatsApp Business (/1 a /4). Em 7 dias, conte quantas conversas chegaram à mensagem 4 e quantas marcaram.

🔻 Comente CLIENTES que eu te chamo no direct e olho o seu atendimento com você.

#atendimento #whatsappbusiness #academia #barbearia #donodenegocio""",
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
    for n in (1, 2, 3, 4, 5):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(agua, O(1)); run(empregos, O(2)); run(origem, O(3)); run(autorizacao, O(4)); run(improviso, O(5))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
