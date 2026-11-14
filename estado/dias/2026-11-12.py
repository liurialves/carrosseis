"""Plano 100 mil, semana 3, dia 6 (12/11/2026, quinta). Dia 6 do "Plano de 30 dias para lançar a mentoria":
conteúdo "Faturar mais não significa ganhar mais" (pilar dinheiro); tarefa: escrever o roteiro da call de diagnóstico e da oferta.
AJUSTE DO DONO EM 10/11 (prevalece sobre a tarefa agendada em quantidade, horários e formato): 5 posts, sem post de IA.
AJUSTE DE 11/11: tema "indicação" fora de todos os posts, roteiros e stories de hoje (0 de 5; ontem também 0).
12:40 CONEXÃO · 14:20 CONEXÃO (REMODELADO) · 17:40 VALOR com rosto (capa A, dia par) · 20:30 CONEXÃO (quinta) · 22:15 BANDEIRA.
Sem prints novos (prova-social, clonar-ia, referencias-99hud, repost-modocaverna): sem repost.
CTA (rodízio, todos terminam em "Comente CLIENTES"): 12:40 comentário · 14:20 salvar · 17:40 envio · 20:30 salvar · 22:15 envio.
1) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): "Eu precisava de 900 € por mês para viver. Ganhava 700 €." Itens 15, 17, 18.
   Fotos Drive 68 (capa), 73, 66, 72 + fotos-liuri home-office-headset.
2) 14:20 FAIXA, conexão, pilar 5 (lição pilar 3). REMODELADO de liurialves:6af29c5cd35dff5701daf234 ("Aos 18 anos fiquei em 13º
   no teste físico", 10/11 14:20, 534 views, 10 curtidas, 1 envio; o mais visto dos últimos 30 dias ainda não replicado em 14 dias).
   Mantém: faixa, 1ª pessoa com número no título, subir de posição por mérito, arco cronológico, lição com ação. Muda: trecho
   (item 15, subgerente em 6 meses e posto para fora), fotos (Drive 71 + Pexels sem rosto), lição de oferta e CTA de salvar.
3) 17:40 FAIXA, valor, pilar 4 (dinheiro), capa A com rosto (Drive 49) + opinião no 2º slide (loja que quebrou, item 13a, como cena):
   a conta de quanto sobra de um cliente (custo para trazer, margem por mês, meses que fica). Molde @twobrainbusiness.
4) 20:30 FAIXA, conexão, pilar 6 (família): "Morávamos os três num quarto só." Itens 13, 14 e 21. Capa fotos-liuri video-rotina-1s
   (sem criança na capa); fatias Drive 03, 04, 67, 78, 77, 61 (post de família: filhos só nas fatias).
5) 22:15 FAIXA, bandeira, pilar 5 (lição pilar 1): "Eu não acredito em post que não pede nada." Capa Drive 60 (selfie com o celular). Fatos: anúncio de vendas 30,61 €,
   6.345 de alcance, 0 compras; anúncio de ligação 16,81 €, 219 cliques (playbook, prints de 08/11).
"""
import json, os, subprocess, sys
S = "/tmp/claude-0/-home-claude-carrosseis/55739fb9-38ed-5ace-8282-20b5171b290d/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-12"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h12/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px12/pexels-{x}.jpg"
PB = lambda x: f"/tmp/px12b/pexels-{x}.jpg"

# 1) 12:40 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
conta = {"slides": [
  {"tipo": "foto", "foto": HP("68"), "foco_y": 0.55, "grande": True, "arraste": True, "faixa": "O MEU PRIMEIRO ANO EM LISBOA",
   "texto": "EU PRECISAVA DE 900 € POR MÊS PARA VIVER. GANHAVA 700 €."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.4, "faixa": "A CONTA NÃO FECHAVA",
   "texto": "PARA SOBREVIVER EU PRECISAVA DE 800 A 900 € POR MÊS. O QUE ENTRAVA ERA 700 €.",
   "destaque": "TODO MÊS FALTAVAM 100 A 200 €."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.45, "faixa": "12 HORAS POR DIA",
   "texto": "TRABALHAVA 12 HORAS NO RESTAURANTE. NO FIM DE SEMANA SAÍA À MEIA-NOITE E IA PARA UM CLUBE ATÉ AS 8 DA MANHÃ.",
   "destaque": "60 € POR NOITE."},
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.35, "faixa": "UM GERENTE AMIGO",
   "texto": "UM EX-GERENTE ME EMPRESTAVA DINHEIRO TODO MÊS. UM DIA ELE ME DEU 100 € DE PRESENTE E EU CHOREI.",
   "destaque": "ALGUÉM SE PREOCUPAVA COMIGO."},
  {"tipo": "branco", "blocos": [
   ["h", "NAQUELE ANO EU SABIA, TODO MÊS, QUANTO FALTAVA."], ["esp", 8],
   ["n", "Muito dono de negócio fatura 2 ou 3 mil euros e não sabe dizer qual é o mínimo que precisa entrar para a empresa e a casa fecharem."],
   ["n", "Sem esse número, o mês ruim só aparece quando o cartão já pagou a diferença."]]},
  {"tipo": "branco", "blocos": [
   ["t", "A CONTA DO SEU MÊS MÍNIMO, EM 15 MINUTOS:"], ["esp", 10],
   ["h", "1. O QUE A EMPRESA PAGA TODO MÊS"],
   ["n", "Sala, sistema, contabilidade, anúncio, material."],
   ["h", "2. O QUE VOCÊ PRECISA TIRAR PARA CASA"],
   ["n", "O valor que faz a sua casa fechar sem cartão."],
   ["h", "3. DIVIDA PELO VALOR MÉDIO DE UM CLIENTE"],
   ["n", "Exemplo ilustrativo: 1.800 € ÷ 120 € = 15 clientes por mês. Compare com o mês passado."]]},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E FAÇO ESSA CONTA COM VOCÊ.",
   "destaque": "QUANTO FALTA NO SEU MÊS?"},
]}

# 2) 14:20 FAIXA, CONEXÃO, REMODELADO, CTA = SALVAR + CLIENTES
subgerente = {"slides": [
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.4, "grande": True, "arraste": True, "faixa": "O RESTAURANTE EM LISBOA",
   "texto": "EM 6 MESES EU VIREI SUBGERENTE. DEPOIS ME COLOCARAM PARA FORA."},
  {"tipo": "foto", "foto": PB("13259521"), "foco_y": 0.45, "faixa": "RESTAURANTE E ESTÁGIO",
   "texto": "EM PORTUGAL EU COMECEI NUM RESTAURANTE, JUNTO COM UM ESTÁGIO. O ESTÁGIO ACABOU EM 2 MESES. O RESTAURANTE FICOU."},
  {"tipo": "foto", "foto": PB("26954008"), "foco_y": 0.4, "faixa": "6 MESES DEPOIS",
   "texto": "SUBI A SUBGERENTE.",
   "destaque": "ALI EU APRENDI QUE QUEM RESOLVE PROBLEMA SOBE."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.25, "faixa": "UM CONFLITO",
   "texto": "TIVE UM CONFLITO COM UM GERENTE. FUI COLOCADO PARA FORA."},
  {"tipo": "foto", "foto": PB("12106425"), "foco_y": 0.45, "faixa": "OUTRO RESTAURANTE",
   "texto": "DEPOIS FUI GERENTE NOUTRO RESTAURANTE CONHECIDO. SAÍ COM 3 MESES."},
  {"tipo": "foto", "foto": FL("video-rotina-9s"), "foco_y": 0.3, "faixa": "A CARTA",
   "texto": "ENTREGUEI A CARTA E DECIDI QUE NÃO IA MAIS TRABALHAR PARA NINGUÉM.",
   "destaque": "O QUE EU LEVEI DE LÁ: O CLIENTE PAGA QUEM RESOLVE O PROBLEMA DELE."},
  {"tipo": "branco", "blocos": [
   ["t", "REESCREVA A SUA OFERTA EM 3 LINHAS:"], ["esp", 10],
   ["h", "1. O PROBLEMA, NAS PALAVRAS DO CLIENTE"],
   ["n", "Exemplo de personal trainer: \"Voltei a sentir dor nas costas e parei de treinar.\""],
   ["h", "2. O QUE MUDA E EM QUANTO TEMPO"],
   ["n", "\"Treinar 3 vezes por semana sem dor em 8 semanas.\""],
   ["h", "3. O QUE ESTÁ INCLUÍDO"],
   ["n", "\"Avaliação, 24 treinos e ajuste do plano a cada 15 dias.\" Ponha a linha 2 na bio e no início de toda resposta de preço."]]},
  {"tipo": "foto", "foto": FL("mma-equipe-treino"), "foco_y": 0.45, "faixa": "SALVE E REESCREVA HOJE",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E LEIO A SUA OFERTA COM VOCÊ.",
   "destaque": "O SEU CLIENTE COMPRA O PROBLEMA RESOLVIDO."},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO (capa A), CTA = ENVIO + CLIENTES
sobra = {"slides": [
  {"tipo": "foto", "foto": HP("49"), "foco_y": 0.2, "grande": True, "arraste": True, "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "VOCÊ FATURA MAIS E NO FIM DO MÊS SOBRA O MESMO? FAÇA ESTA CONTA COM UM CLIENTE SÓ."},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.3, "faixa": "O QUE EU ACREDITO",
   "texto": "NO TEMPO DA FARDA EU ABRI UMA LOJA DE MODA PRAIA. ENTRAVA DINHEIRO, MAS ELE IA PARA VIAGEM E CONTA DE CASA. A LOJA QUEBROU NA COVID.",
   "destaque": "HOJE EU OLHO PRIMEIRO QUANTO SOBRA DE CADA CLIENTE."},
  {"tipo": "branco", "blocos": [
   ["h", "MAIS ALUNO NOVO PARECE CRESCIMENTO"], ["esp", 8],
   ["n", "Se cada um custa caro para entrar e vai embora no 2º mês, você trabalha mais e ganha quase igual."],
   ["n", "A conta abaixo mostra isso em 15 minutos. Os números são um exemplo ilustrativo de personal trainer: troque pelos seus."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "QUANTO CUSTA TRAZER UM CLIENTE"], ["esp", 8],
   ["n", "Some o que gastou no mês para atrair gente nova: anúncio, panfleto, aula grátis, desconto de entrada."],
   ["n", "Divida pelos clientes novos. Exemplo: 300 € ÷ 3 alunos = 100 € por aluno."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "QUANTO SOBRA DE CADA UM POR MÊS"], ["esp", 8],
   ["n", "Preço do plano menos o que esse cliente te custa: hora de sala, material, taxa do cartão."],
   ["n", "Exemplo: 160 € − 40 € = 120 € por mês."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "QUANTOS MESES ELE FICA"], ["esp", 8],
   ["n", "Pegue os últimos 10 clientes que saíram e conte quantos meses cada um ficou. Faça a média."],
   ["n", "Exemplo: 2 meses."]]},
  {"tipo": "branco", "blocos": [
   ["h", "O RESULTADO: 2 × 120 € − 100 € = 140 € POR ALUNO"], ["esp", 8],
   ["n", "Se o mesmo aluno ficasse 6 meses, sobravam 620 €. Sem gastar um euro a mais em anúncio."],
   ["n", "Antes de buscar mais clientes, ligue hoje para 3 que saíram e pergunte o que fez eles pararem."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.15, "faixa": "ENVIE PARA UM SÓCIO",
   "texto": "QUE SÓ OLHA O FATURAMENTO. E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E FAÇO A CONTA DO SEU NEGÓCIO.",
   "destaque": "15 MINUTOS E UMA CALCULADORA."},
]}

# 4) 20:30 FAIXA, CONEXÃO (família), CTA = SALVAR + CLIENTES
quarto = {"slides": [
  {"tipo": "foto", "foto": FL("video-rotina-1s"), "foco_y": 0.35, "grande": True, "arraste": True, "faixa": "A MINHA FAMÍLIA EM PORTUGAL",
   "texto": "MORÁVAMOS OS TRÊS NUM QUARTO SÓ. E O SEGUNDO FILHO JÁ ESTAVA A CAMINHO."},
  {"tipo": "foto", "foto": HP("03"), "foco_y": 0.4, "faixa": "EU VIM NA FRENTE",
   "texto": "VIM PARA PORTUGAL SOZINHO, COM 300 €. ELA E O NOSSO BEBÊ CHEGARAM 3 MESES DEPOIS."},
  {"tipo": "foto", "foto": HP("04"), "foco_y": 0.3, "faixa": "ELA CHEGOU GRÁVIDA",
   "texto": "QUANDO ELA CHEGOU, JÁ TÍNHAMOS UM BEBÊ E ELA ESTAVA GRÁVIDA DO SEGUNDO."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.35, "faixa": "NO MESMO DIA",
   "texto": "CONSEGUIMOS O QUARTO NO MESMO DIA EM QUE ELA CHEGOU. FICAMOS OS TRÊS ALI."},
  {"tipo": "foto", "foto": HP("78"), "foco_y": 0.35, "faixa": "QUASE NUM CAFÉ",
   "texto": "O NOSSO SEGUNDO FILHO QUASE NASCEU NUM CAFÉ AO LADO.",
   "destaque": "AQUELE PRIMEIRO ANO FOI O MAIS DIFÍCIL DA NOSSA VIDA."},
  {"tipo": "foto", "foto": HP("77"), "foco_y": 0.4, "faixa": "DEPOIS",
   "texto": "JUNTAMOS DINHEIRO E MUDAMOS PARA UMA CASA. HOJE ELES ESTÃO DE FÉRIAS NO BRASIL E EU VOU BUSCÁ-LOS."},
  {"tipo": "branco", "blocos": [
   ["h", "O QUARTO SAIU PORQUE A DATA ERA FIXA: O DIA EM QUE ELA CHEGAVA."], ["esp", 8],
   ["n", "No negócio, o que fica para \"quando der\" não sai. Escolha 1 decisão que você adia há meses e dê uma data:"],
   ["n", "Exemplo: \"Dia 1 de dezembro o plano mensal entra no ar.\" Escreva no calendário, conte para 1 cliente e para quem mora com você. Hoje."]]},
  {"tipo": "foto", "foto": HP("61"), "foco_y": 0.3, "faixa": "SALVE PARA LEMBRAR",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E TE AJUDO A ESCOLHER A DATA DA SUA PRÓXIMA DECISÃO.",
   "destaque": "FAMÍLIA E NEGÓCIO CABEM NA MESMA AGENDA."},
]}

# 5) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = ENVIO + CLIENTES
pedido = {"slides": [
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM POST QUE NÃO PEDE NADA."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "O QUE ME FEZ PENSAR ASSIM",
   "texto": "FIZ UM ANÚNCIO DE VENDAS. GASTEI 30,61 € E APARECI PARA 6.345 PESSOAS.",
   "destaque": "NINGUÉM COMPROU."},
  {"tipo": "foto", "foto": FL("video-rotina-17s"), "foco_y": 0.3, "faixa": "O OUTRO ANÚNCIO",
   "texto": "NUM ANÚNCIO SIMPLES, COM O BOTÃO DE LIGAR, GASTEI 16,81 € E RECEBI 219 CLIQUES PARA ME LIGAR.",
   "destaque": "ESTE PEDIA UMA AÇÃO SÓ."},
  {"tipo": "foto", "foto": P("4753987"), "foco_y": 0.45, "faixa": "EXEMPLO: O PERSONAL",
   "texto": "POSTA TREINO TODO DIA, COM MÚSICA E LEGENDA CAPRICHADA. NENHUM POST DIZ COMO COMEÇAR A TREINAR COM ELE."},
  {"tipo": "foto", "foto": P("18702143"), "foco_y": 0.5, "faixa": "EXEMPLO: A BARBEARIA",
   "texto": "POSTA O CORTE PRONTO. QUEM GOSTOU NÃO SABE SE TEM HORÁRIO NO SÁBADO NEM COMO MARCAR."},
  {"tipo": "foto", "foto": P("28704057"), "foco_y": 0.45, "faixa": "O QUE EU FAÇO",
   "texto": "TODO POST MEU TERMINA PEDINDO UMA COISA SÓ: UMA PALAVRA NOS COMENTÁRIOS. A PALAVRA ABRE A CONVERSA NO DIRECT."},
  {"tipo": "branco", "blocos": [
   ["t", "NOS SEUS PRÓXIMOS 7 POSTS:"], ["esp", 10],
   ["h", "1. UM PEDIDO SÓ POR POST"],
   ["n", "\"Comente AVALIAÇÃO\" ou \"Me mande HORÁRIO\". Nunca os dois."],
   ["h", "2. RESPONDA EM ATÉ 5 MINUTOS"],
   ["n", "Quem acabou de comentar ainda está com o celular na mão."],
   ["h", "3. CONTE AS CONVERSAS"],
   ["n", "No domingo, anote quantas conversas cada post abriu. O que abriu zero, você não repete."]]},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM POSTA TODO DIA",
   "texto": "E NÃO VÊ CLIENTE NOVO. E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT.",
   "destaque": "ESTE POST TAMBÉM PEDE UMA COISA SÓ."},
]}

LEGENDAS = {
 1: """Eu precisava de 900 € por mês para viver. Ganhava 700 €.

No meu primeiro ano em Lisboa, a conta não fechava. Para sobreviver eu precisava de 800 a 900 € por mês e o que entrava era 700 €. Trabalhava 12 horas por dia no restaurante e, no fim de semana, saía à meia-noite e ia para um clube até as 8 da manhã, por 60 € a noite. Um ex-gerente, meu amigo, me emprestava dinheiro todo mês. Um dia ele me deu 100 € de presente e eu chorei.

Naquele ano eu sabia, todo mês, quanto faltava. No seu negócio, faça hoje a conta do mês mínimo: some o que a empresa paga todo mês, some o que você precisa tirar para casa e divida pelo valor médio de um cliente. Exemplo ilustrativo: 1.800 € ÷ 120 € = 15 clientes. Compare com o mês passado.

🔻 Quanto falta no seu mês? Comente CLIENTES que eu te chamo no direct e faço essa conta com você.

#empreendedorismo #donodenegocio #historiareal #brasileiroemportugal #gestaofinanceira""",
 2: """Em 6 meses eu virei subgerente. Depois me colocaram para fora.

Em Portugal eu comecei num restaurante, junto com um estágio que acabou em 2 meses. Em 6 meses subi a subgerente. Depois tive um conflito com um gerente e fui colocado para fora. Fui gerente noutro restaurante conhecido e saí com 3 meses. Entreguei a carta e decidi que não ia mais trabalhar para ninguém.

O que eu levei de lá: o cliente paga quem resolve o problema dele. Reescreva a sua oferta em 3 linhas: o problema nas palavras do cliente, o que muda e em quanto tempo, e o que está incluído. Ponha a segunda linha na bio e no começo de toda resposta de preço.

🔻 Salve e reescreva hoje. E comente CLIENTES que eu te chamo no direct e leio a sua oferta com você.

#empreendedorismo #donodenegocio #oferta #personaltrainer #fisioterapia""",
 3: """Você fatura mais e no fim do mês sobra o mesmo? Faça esta conta com um cliente só.

No tempo da farda eu abri uma loja de moda praia. Entrava dinheiro, mas ele ia para viagem e conta de casa, e a loja quebrou na Covid. Hoje eu olho primeiro quanto sobra de cada cliente.

A conta (exemplo ilustrativo de personal trainer, troque pelos seus números):
1. Quanto custa trazer um cliente: 300 € de anúncio ÷ 3 alunos = 100 €.
2. Quanto sobra dele por mês: 160 € − 40 € de custos = 120 €.
3. Quantos meses ele fica: média de 2 meses.
Resultado: 2 × 120 € − 100 € = 140 € por aluno. Se ficasse 6 meses, 620 €.

Antes de buscar mais clientes, ligue hoje para 3 que saíram e pergunte o que fez eles pararem.

🔻 Envie para um sócio que só olha o faturamento. E comente CLIENTES que eu te chamo no direct e faço a conta do seu negócio.

#gestaofinanceira #personaltrainer #academia #barbearia #donodenegocio""",
 4: """Morávamos os três num quarto só. E o segundo filho já estava a caminho.

Eu vim para Portugal sozinho, com 300 €. A minha esposa e o nosso bebê chegaram 3 meses depois, e ela já estava grávida do segundo. Conseguimos o quarto no mesmo dia em que ela chegou. O nosso segundo filho quase nasceu num café ao lado. Aquele primeiro ano foi o mais difícil da nossa vida. Depois juntamos dinheiro e mudamos para uma casa. Hoje eles estão de férias no Brasil e eu vou buscá-los.

O quarto saiu porque a data era fixa: o dia em que ela chegava. No seu negócio, escolha 1 decisão que você adia há meses e dê uma data. Escreva no calendário e conte para 1 cliente e para quem mora com você. Hoje.

🔻 Salve para lembrar. E comente CLIENTES que eu te chamo no direct e te ajudo a escolher a data da sua próxima decisão.

#familia #brasileiroemportugal #empreendedorismo #pai #donodenegocio""",
 5: """Eu não acredito em post que não pede nada.

Fiz um anúncio de vendas, gastei 30,61 € e apareci para 6.345 pessoas. Ninguém comprou. Num anúncio simples, com o botão de ligar, gastei 16,81 € e recebi 219 cliques para me ligar. Este pedia uma ação só.

Vejo o mesmo no feed: o personal que posta treino todo dia e nenhum post diz como começar com ele; a barbearia que posta o corte pronto e ninguém sabe se tem horário no sábado. Todo post meu termina pedindo uma coisa só, uma palavra nos comentários, e é ela que abre a conversa no direct.

Nos seus próximos 7 posts: um pedido só por post, resposta em até 5 minutos e, no domingo, a conta de quantas conversas cada post abriu.

🔻 Envie para quem posta todo dia e não vê cliente novo. E comente CLIENTES que eu te chamo no direct.

#empreendedorismo #donodenegocio #instagramparanegocios #personaltrainer #barbearia""",
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
    for n, cfg in ((1, conta), (2, subgerente), (3, sobra), (4, quarto), (5, pedido)):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
        run(cfg, O(n))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
