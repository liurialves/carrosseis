"""Plano 100 mil, semana 3, dia 7 (13/11/2026, sexta). Dia 7 do "Plano de 30 dias para lançar a mentoria":
conteúdo "Case: 252 € em anúncios, 1.755 € em atendimentos" (vai para o roteiro de PROVA de hoje, sem print);
tarefa: revisão da semana 1.
AJUSTE DO DONO EM 10/11 (prevalece sobre a tarefa agendada em quantidade, horários e formato): 5 posts, sem post de IA.
AJUSTE DE 11/11: tema "indicação" fora de todos os posts, roteiros e stories de hoje (0 de 5).
12:40 CONEXÃO (REMODELADO) · 14:20 CONEXÃO (REMODELADO) · 17:40 VALOR com rosto · 20:30 PROVA (sexta) · 22:15 BANDEIRA.
Sem prints novos nas pastas do Drive. Print ainda NÃO usado em post: planilha-receita-2156-lucro-2081.jpg (prova-social,
08/11) -> prova das 20:30 (recorte só das colunas Total/valor; a coluna "fonte" ficou de fora).
CTA (rodízio, todos terminam em "Comente CLIENTES"): 12:40 envio · 14:20 comentário · 17:40 salvar · 20:30 comentário · 22:15 salvar.
1) 12:40 FAIXA, conexão, pilar 5 (lição pilar 1/vendas): "No dia da formatura eu pedi a minha namorada em casamento.
   Quase fiquei preso 4 dias." Itens 6, 7, 8, 10 e 11. REMODELADO de liurialves:6af14d27e29b1359f0cbde77 ("4 jeitos",
   1.690 views, 2º mais visto dos últimos 7 dias): casal na capa, 1ª pessoa, arco do casal; muda o trecho (noivado),
   as fotos (Drive 26, 10, 21, 28, 16, 25, 64) e a lição (pedir a venda) e o CTA (envio).
2) 14:20 FAIXA, conexão, pilar 6 (lição pilar 3): "Fiz Uber por 2 anos em Portugal. Hoje eu não olho o preço no
   supermercado." Itens 19, 20 e 21. REMODELADO de liurialves:6af08ee8d6bbae6fa1f59abb ("300 €", 1.856 views, o mais
   visto dos últimos 7 dias): mesmo arco antes→hoje com números; trecho novo (Uber, virada, hoje), capa video-rotina-5_5s
   (sem foto do Uber; avisado no doc), lição da hora vendida, CTA comentário.
3) 17:40 FAIXA, valor, pilar 3 (preço), capa com rosto (mma-equipe-treino) + opinião no 2º slide (cliente de ~300 €/mês).
4) 20:30 CAPA + ESCURO, prova, pilar 5/4: planilha real (receita 2.156,50 €, despesas 75 €, lucro 2.081,50 €, valor
   médio 196,05 €, semana 1 = 1.843 €, semana 2 = 313,50 €). Capa Drive 41.
5) 22:15 FAIXA, bandeira, pilar 6 (lição pilar 2): "Eu não acredito em motivação para tocar uma empresa." Item 10.
   Capa Drive 11.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
S = "/tmp/claude-0/-home-claude-carrosseis/94b38756-b6cf-554b-8b06-009a69ea3deb/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-13"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h13/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px13/pexels-{x}.jpg"

# 1) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = ENVIO + CLIENTES
noivado = {"slides": [
  {"tipo": "foto", "foto": HP("26"), "foco_y": 0.5, "grande": True, "arraste": True, "faixa": "A MINHA FORMATURA NA AERONÁUTICA",
   "texto": "NO DIA DA FORMATURA EU PEDI A MINHA NAMORADA EM CASAMENTO. QUASE FIQUEI PRESO 4 DIAS."},
  {"tipo": "foto", "foto": HP("10"), "foco_y": 0.35, "faixa": "ANTES DE ENTRAR",
   "texto": "AOS 18 ANOS EU DISSE A ELA: VOU ENTRAR NA AERONÁUTICA, VOU ESTAR ENTRE OS MELHORES E A GENTE VAI MUDAR DE VIDA.",
   "destaque": "PASSEI COMO 13º NO TESTE FÍSICO."},
  {"tipo": "foto", "foto": HP("21"), "foco_y": 0.3, "faixa": "LONGE DELA",
   "texto": "DEPOIS VIERAM 40 A 45 DIAS DE QUARENTENA SEM VER A FAMÍLIA. E MESES DE GRITO, FARDA E CAMA PERFEITA."},
  {"tipo": "foto", "foto": HP("28"), "foco_y": 0.45, "faixa": "O DIA DA FORMATURA",
   "texto": "NA FRENTE DA TROPA E DAS FAMÍLIAS, EU AJOELHEI.",
   "destaque": "E PEDI ELA EM CASAMENTO."},
  {"tipo": "foto", "foto": HP("16"), "foco_y": 0.35, "faixa": "A ALA",
   "texto": "OS COLEGAS FIZERAM UMA ALA PARA NÓS. SÓ QUE ALA É HOMENAGEM DE OFICIAL GENERAL."},
  {"tipo": "foto", "foto": HP("25"), "foco_y": 0.35, "faixa": "O PREÇO",
   "texto": "QUASE FIQUEI PRESO 4 DIAS POR CAUSA DISSO.",
   "destaque": "SAÍ SÓ COM UMA REPREENSÃO VERBAL."},
  {"tipo": "foto", "foto": HP("64"), "foco_y": 0.2, "faixa": "UM ANO DEPOIS",
   "texto": "FOI UM ANO DE NOIVADO. UM ANO DEPOIS DA FORMATURA, A GENTE CASOU."},
  {"tipo": "branco", "blocos": [
   ["h", "EU SABIA QUE PODIA LEVAR UMA PUNIÇÃO. PEDI MESMO ASSIM."], ["esp", 8],
   ["n", "No atendimento, muito dono de negócio explica tudo, tira todas as dúvidas e deixa o cliente ir embora sem pedir nada. Aí vem o \"vou pensar\"."],
   ["n", "Nesta semana, termine toda conversa com uma pergunta que só tem resposta de agenda: \"Começamos segunda ou quarta?\" Anote quantas vezes perguntou e quantos disseram sim."]]},
  {"tipo": "foto", "foto": HP("63"), "foco_y": 0.25, "faixa": "ENVIE PARA QUEM EXPLICA E NÃO PEDE",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E TE AJUDO A ESCREVER O SEU PEDIDO.",
   "destaque": "QUEM NÃO PEDE, ESPERA."},
]}

# 2) 14:20 FAIXA, CONEXÃO (REMODELADO), CTA = COMENTÁRIO + CLIENTES
uber = {"slides": [
  {"tipo": "foto", "foto": FL("video-rotina-5_5s"), "foco_y": 0.55, "grande": True, "arraste": True, "faixa": "DO VOLANTE ATÉ HOJE",
   "texto": "FIZ UBER POR 2 ANOS EM PORTUGAL. HOJE EU NÃO OLHO O PREÇO NO SUPERMERCADO."},
  {"tipo": "foto", "foto": P("9689391"), "foco_y": 0.5, "faixa": "DEPOIS DO RESTAURANTE",
   "texto": "SAÍ DO RESTAURANTE E FUI FAZER UBER. FORAM 2 ANOS.",
   "destaque": "O CARRO DAVA PROBLEMA E EU ESTAVA FARTO."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.3, "faixa": "UMA DECISÃO",
   "texto": "UM DIA EU DECIDI QUE QUERIA GANHAR MAIS E MUDAR DE VIDA."},
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.3, "faixa": "O QUE EU JÁ SABIA FAZER",
   "texto": "VOLTEI PARA A MASSAGEM, QUE EU FAZIA DESDE 2017 NO BRASIL, E COMECEI A CRIAR SITES PARA CLIENTES."},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "2026",
   "texto": "A MINHA EMPRESA SAIU DE 1.500 € PARA 7.000 € POR MÊS.",
   "destaque": "A MINHA VIDA MUDOU ESTE ANO, COM A MINHA ATITUDE."},
  {"tipo": "foto", "foto": FL("cafe-pastel-pao-de-queijo"), "foco_y": 0.45, "faixa": "HOJE",
   "texto": "NÃO PRECISO OLHAR O PREÇO NO SUPERMERCADO. TENHO RESERVA DE EMERGÊNCIA E ESTOU CONSTRUINDO PATRIMÔNIO."},
  {"tipo": "branco", "blocos": [
   ["h", "NO UBER, EU SÓ GANHAVA ENQUANTO O CARRO ANDAVA."], ["esp", 8],
   ["n", "Personal trainer, fisioterapeuta e barbeiro vivem a mesma conta: cada euro depende de uma hora sua."],
   ["n", "Faça hoje: faturamento do mês ÷ horas trabalhadas. Exemplo ilustrativo: 2.500 € ÷ 200 h = 12,50 € por hora. Depois escreva 1 serviço que você pode vender sem somar hora: plano mensal, treino em grupo, pacote."]]},
  {"tipo": "foto", "foto": FL("video-rotina-9s"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E FAÇO A CONTA DA SUA HORA COM VOCÊ.",
   "destaque": "QUANTO VALE A SUA HORA?"},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO, CTA = SALVAR + CLIENTES
preco = {"slides": [
  {"tipo": "foto", "foto": FL("mma-equipe-treino"), "foco_y": 0.55, "grande": True, "arraste": True, "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "HÁ QUANTO TEMPO VOCÊ NÃO SOBE O PREÇO? FAÇA ISTO ANTES DE MEXER NELE."},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.3, "faixa": "O QUE EU ACREDITO",
   "texto": "NA MASSAGEM EU TIVE UM CLIENTE QUE PAGAVA CERCA DE 300 € POR MÊS, 2 A 3 VEZES POR SEMANA. ELE NÃO COMPRAVA PELO PREÇO.",
   "destaque": "PREÇO PARADO HÁ 2 ANOS É CORTE DE SALÁRIO QUE VOCÊ MESMO SE DÁ."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "FAÇA A CONTA DO QUE SUBIU"], ["esp", 8],
   ["n", "Some o que aumentou desde o último reajuste: sala, sistema, material, combustível, anúncio."],
   ["n", "Exemplo ilustrativo: o plano de 80 € não muda há 2 anos e o custo por aluno subiu 12 €. Você trabalha o mesmo e leva menos para casa."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "PREÇO NOVO PRIMEIRO PARA QUEM ENTRA"], ["esp", 8],
   ["n", "Escolha uma data. Quem chegar a partir dela paga o valor novo."],
   ["n", "Exemplo: de 80 € para 95 € a partir de 1 de dezembro. Os alunos atuais continuam no valor antigo por mais 30 dias."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "AVISE OS ATUAIS COM 30 DIAS"], ["esp", 8],
   ["n", "Copie e troque o que está entre colchetes:"],
   ["n", "\"Olá, [nome]. Desde [ano] o valor do seu plano não muda. A partir de [data] ele passa a [novo valor]. Quis te avisar com 30 dias e agradecer por treinar comigo.\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "DÊ UMA SAÍDA QUE SEGURA O ALUNO"], ["esp", 8],
   ["n", "Quem fechar o plano de 6 meses até a data mantém o valor antigo."],
   ["n", "Exemplo: 6 × 80 € = 480 €. Você garante 6 meses de caixa e o aluno sente que ganhou alguma coisa."]]},
  {"tipo": "branco", "blocos": [
   ["h", "UM CRITÉRIO SIMPLES PARA SABER SE ACERTOU"], ["esp", 8],
   ["n", "Se ninguém comentou o preço novo, ele ainda está baixo."],
   ["n", "Anote em 30 dias: quantos alunos saíram e quantos fecharam o plano de 6 meses. É esse número que diz se você sobe de novo em junho."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.15, "faixa": "SALVE E MANDE A MENSAGEM HOJE",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E OLHO O SEU PREÇO COM VOCÊ.",
   "destaque": "4 PASSOS E UMA DATA NO CALENDÁRIO."},
]}

# 4) 20:30 CAPA + ESCURO, PROVA, CTA = COMENTÁRIO + CLIENTES (fatia-1 = print real recortado, montado à parte)
prova = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": HP("41"), "foco_y": 0.3, "etiqueta": "Prova",
   "titulo": "Semana 1: 1.843 €. Semana 2: 313,50 €. A mesma planilha.",
   "sub": "O print é real. Eu olho este número toda semana."},
  {"etiqueta": "O print", "frase": "x", "texto": "x"},  # substituído pelo slide do print
  {"etiqueta": "O total", "frase": "Receita de 2.156,50 €. Despesa de 75 €. [[Lucro de 2.081,50 €]].",
   "texto": "É a planilha que eu preencho a cada atendimento. Eu mostro inteira, com a semana fraca junto."},
  {"etiqueta": "A queda", "frase": "Da semana 1 para a semana 2 caiu [[de 1.843 € para 313,50 €]].",
   "texto": "Pelo total do mês, estava tudo bem. Olhando por semana, eu vejo a queda com metade do mês ainda pela frente para reagir."},
  {"etiqueta": "O número que eu mais olho", "frase": "Valor médio: [[196,05 €]] por atendimento.",
   "texto": "Para o mês crescer existem dois caminhos: mais atendimentos ou atendimentos que valem mais. Este número mostra em qual dos dois eu estou."},
  {"etiqueta": "Por que eu anoto tudo", "frase": "Eu já quebrei uma loja [[sem enxergar os números]].",
   "texto": "A conta da loja era a mesma de casa. Hoje cada atendimento entra na planilha no mesmo dia, com valor e custo."},
  {"etiqueta": "Faça hoje", "frase": "A sua planilha [[em 4 linhas]].",
   "texto": "Semana 1, 2, 3 e 4. Ao lado de cada uma: quanto entrou, quanto saiu e quantos atendimentos. Meta da semana = meta do mês ÷ 4. Exemplo ilustrativo: 3.000 € ÷ 4 = 750 €."},
  {"etiqueta": "Para quem é", "frase": "Para o dono que só descobre o mês [[no dia 30]].",
   "texto": "Personal trainer, academia, fisioterapia ou barbearia, faturando entre 1.500 € e 5.000 € por mês e olhando o extrato só quando a conta aperta."},
  {"etiqueta": "Próximo passo", "frase": "Qual foi a sua [[semana mais fraca]] deste mês?",
   "texto": "Comente CLIENTES. Eu te chamo no direct e a gente olha os seus números semana a semana."},
]}

# 5) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = SALVAR + CLIENTES
disciplina = {"slides": [
  {"tipo": "foto", "foto": HP("11"), "foco_y": 0.25, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM MOTIVAÇÃO PARA TOCAR UMA EMPRESA."},
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.3, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "NA AERONÁUTICA ERA GRITO, CORRERIA, TROCA DE FARDA, CAMA PERFEITA, ENGRAXAR E FAZER A BARBA TODO DIA.",
   "destaque": "NINGUÉM PERGUNTAVA SE EU ESTAVA MOTIVADO."},
  {"tipo": "foto", "foto": HP("43"), "foco_y": 0.35, "faixa": "O QUE FICOU",
   "texto": "FOI ALI QUE EU APRENDI A SER DISCIPLINADO. A MESMA ROTINA CHATA, TODO SANTO DIA."},
  {"tipo": "foto", "foto": P("7991944"), "foco_y": 0.5, "faixa": "EXEMPLO: O PERSONAL",
   "texto": "POSTA TRÊS VEZES NUMA SEMANA EM QUE ACORDOU ANIMADO. NAS DUAS SEGUINTES, NADA. RESPONDE O WHATSAPP QUANDO SOBRA TEMPO."},
  {"tipo": "foto", "foto": P("8867166"), "foco_y": 0.5, "faixa": "EXEMPLO: A BARBEARIA",
   "texto": "O SÁBADO LOTA SOZINHO. DE TERÇA A QUINTA A CADEIRA FICA VAZIA E NINGUÉM TEM UMA TAREFA FIXA PARA ENCHER ESSES DIAS."},
  {"tipo": "foto", "foto": HP("09"), "foco_y": 0.45, "faixa": "O QUE EU DEFENDO",
   "texto": "A TAREFA QUE TRAZ CLIENTE ENTRA NA AGENDA COM HORA MARCADA, COMO A FORMA. FAZ COM VONTADE OU SEM VONTADE."},
  {"tipo": "branco", "blocos": [
   ["t", "COMECE SEGUNDA, POR 20 DIAS ÚTEIS:"], ["esp", 10],
   ["h", "1. ESCOLHA UMA TAREFA SÓ"],
   ["n", "A que mais traz conversa nova. Exemplo: mandar 5 mensagens para ex-alunos às 9h."],
   ["h", "2. MARQUE UM X NO CALENDÁRIO"],
   ["n", "Na parede, não no celular. Dia sem X é dia que você vê."],
   ["h", "3. CONTE NO DIA 20"],
   ["n", "Quantas conversas abriram e quantas viraram cliente. Só então decida se troca a tarefa."]]},
  {"tipo": "foto", "foto": HP("44"), "foco_y": 0.4, "faixa": "SALVE E COMECE SEGUNDA",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E TE AJUDO A ESCOLHER A TAREFA.",
   "destaque": "20 X NO CALENDÁRIO."},
]}

LEGENDAS = {
 1: """No dia da formatura eu pedi a minha namorada em casamento. Quase fiquei preso 4 dias.

Aos 18 anos eu disse a ela que ia entrar na Aeronáutica, ficar entre os melhores e que a gente ia mudar de vida. Passei como 13º no teste físico. Depois vieram 40 a 45 dias de quarentena longe da família e meses de farda e grito. No dia da formatura, na frente da tropa e das famílias, eu ajoelhei e pedi. Os colegas fizeram uma ala para nós, e ala é homenagem de oficial general. Quase fiquei preso 4 dias. Saí com uma repreensão verbal. Um ano depois, a gente casou.

Eu sabia que podia levar uma punição e pedi mesmo assim. No seu atendimento, termine toda conversa desta semana com uma pergunta que só tem resposta de agenda: "Começamos segunda ou quarta?" Anote quantas vezes perguntou e quantos disseram sim.

🔻 Envie para quem explica tudo e não pede nada. E comente CLIENTES que eu te chamo no direct e te ajudo a escrever o seu pedido.

Fotos: Robério Castro Fotografia

#empreendedorismo #donodenegocio #historiareal #vendas #aeronautica""",
 2: """Fiz Uber por 2 anos em Portugal. Hoje eu não olho o preço no supermercado.

Depois do restaurante, fui fazer Uber. Foram 2 anos, com o carro dando problema, até eu ficar farto e decidir que queria ganhar mais e mudar de vida. Voltei para a massagem, que eu fazia desde 2017 no Brasil, e comecei a criar sites para clientes. Em 2026 a minha empresa saiu de 1.500 € para 7.000 € por mês. A minha vida mudou este ano, com a minha atitude. Hoje tenho reserva de emergência e estou construindo patrimônio.

No Uber eu só ganhava enquanto o carro andava. Faça a conta da sua hora: faturamento do mês ÷ horas trabalhadas (exemplo ilustrativo: 2.500 € ÷ 200 h = 12,50 € por hora). Depois escreva 1 serviço que você pode vender sem somar hora: plano mensal, treino em grupo, pacote.

🔻 Quanto vale a sua hora? Comente CLIENTES que eu te chamo no direct e faço essa conta com você.

#empreendedorismo #donodenegocio #brasileiroemportugal #personaltrainer #historiareal""",
 3: """Há quanto tempo você não sobe o preço?

Na massagem eu tive um cliente que pagava cerca de 300 € por mês, 2 a 3 vezes por semana. Ele não comprava pelo preço. Preço parado há 2 anos é corte de salário que você mesmo se dá.

Os 4 passos (exemplo ilustrativo de personal trainer, troque pelos seus números):
1. Some o que subiu desde o último reajuste: sala, sistema, material, anúncio.
2. Preço novo primeiro para quem entra, a partir de uma data. Ex.: de 80 € para 95 € em 1 de dezembro.
3. Avise os atuais com 30 dias: "Olá, [nome]. Desde [ano] o valor do seu plano não muda. A partir de [data] ele passa a [novo valor]. Quis te avisar com 30 dias e agradecer por treinar comigo."
4. Dê uma saída: quem fechar 6 meses até a data mantém o valor antigo.

Em 30 dias, anote quantos saíram e quantos fecharam os 6 meses.

🔻 Salve e mande a mensagem hoje. E comente CLIENTES que eu te chamo no direct e olho o seu preço com você.

#preco #personaltrainer #academia #fisioterapia #donodenegocio""",
 4: """Semana 1: 1.843 €. Semana 2: 313,50 €. A mesma planilha.

O print está no 2º slide. Receita de 2.156,50 €, despesa de 75 €, lucro de 2.081,50 € e valor médio de 196,05 € por atendimento. Eu mostro com a semana fraca junto, porque é olhando por semana que eu vejo a queda com metade do mês ainda pela frente.

Eu já quebrei uma loja sem enxergar os números. Hoje cada atendimento entra na planilha no mesmo dia.

Faça hoje a sua em 4 linhas: semana 1, 2, 3 e 4, com quanto entrou, quanto saiu e quantos atendimentos. Meta da semana = meta do mês ÷ 4 (exemplo ilustrativo: 3.000 € ÷ 4 = 750 €).

🔻 Qual foi a sua semana mais fraca deste mês? Comente CLIENTES que eu te chamo no direct e a gente olha os seus números semana a semana.

#gestaofinanceira #donodenegocio #empreendedorismo #personaltrainer #barbearia""",
 5: """Eu não acredito em motivação para tocar uma empresa.

Na Aeronáutica era grito, correria, troca de farda, cama perfeita, engraxar e fazer a barba todo dia. Ninguém perguntava se eu estava motivado. Foi ali que eu aprendi a ser disciplinado.

Vejo o contrário no dono de negócio parado: o personal que posta três vezes numa semana animada e some nas duas seguintes; a barbearia que lota no sábado e deixa a cadeira vazia de terça a quinta sem uma tarefa fixa para mudar isso.

A partir de segunda, por 20 dias úteis: escolha uma tarefa que traz conversa nova (ex.: 5 mensagens para ex-alunos às 9h), marque um X no calendário da parede a cada dia feito e, no dia 20, conte quantas conversas abriram e quantas viraram cliente.

🔻 Salve e comece segunda. E comente CLIENTES que eu te chamo no direct e te ajudo a escolher a tarefa.

Fotos: Robério Castro Fotografia

#disciplina #empreendedorismo #donodenegocio #aeronautica #barbearia""",
}


def inter(t, peso="Bold"):
    f = ImageFont.truetype(f"{R}/assets/fonts/Inter.ttf", t)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f


def slide_print(dst, i, n):
    """Fatia escura com o recorte real da planilha (só as colunas Total e valor; a coluna "fonte" ficou de fora)."""
    im = Image.new("RGB", (1080, 1350), (14, 14, 14)); d = ImageDraw.Draw(im)
    d.text((110, 90), "O PRINT", font=inter(30, "Bold"), fill=(217, 84, 30))
    d.text((110, 138), "A minha planilha de atendimentos.", font=inter(46, "Bold"), fill=(242, 239, 234))
    c = ImageOps.contain(Image.open("/tmp/ps13/planilha-corte.jpg").convert("RGB"), (860, 900))
    mask = Image.new("L", c.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, c.width, c.height), 26, fill=255)
    im.paste(c, ((1080 - c.width) // 2, 250), mask)
    d.text((110, 1215), "Print real. Recortado só nos totais.", font=inter(28, "Regular"), fill=(168, 164, 158))
    d.text((540, 1278), f"@liurialves  •  {i:02d}/{n:02d}", font=inter(26, "Medium"), fill=(120, 120, 120), anchor="ma")
    im.save(dst, quality=92)


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
    run(noivado, O(1)); run(uber, O(2)); run(preco, O(3))
    run(prova, O(4), "render_formatos.py"); slide_print(f"{O(4)}/fatia-1.jpg", 2, len(prova["slides"]))
    run(disciplina, O(5))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
