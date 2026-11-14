"""Plano 100 mil, semana 3, dia 5 (11/11/2026, quarta). Dia 5 do "Plano de 30 dias para lançar a mentoria":
conteúdo "O que a Aeronáutica me ensinou sobre disciplina"; tarefa: confirmar a agenda de calls (14h-17h) e o link de marcação.
AJUSTE DO DONO EM 10/11 (prevalece sobre a tarefa agendada em quantidade, horários e formato): 5 posts, sem post de IA.
12:40 CONEXÃO molde vencedor · 14:20 CONEXÃO molde vencedor (REMODELADO) · 17:40 VALOR com rosto · 20:30 PROVA (quarta,
molde de prova) · 22:15 CONEXÃO tipo BANDEIRA. Sem prints novos (prova-social, clonar-ia, repost-modocaverna): sem repost.
CTA (rodízio, todos terminam em "Comente CLIENTES"): 12:40 envio · 14:20 comentário · 17:40 salvar · 20:30 envio · 22:15 comentário.
1) 12:40 FAIXA, conexão, pilar 5: "Para ganhar, eu sempre perdi alguma coisa antes" (banco de ideias, molde da referência
   @jacob.yapping: tese curta + trocas concretas). Itens 7, 12, 13, 14 e 17. Fotos Drive 72, 35, 44, 66 + fotos-liuri.
2) 14:20 FAIXA, conexão, pilar 5 (lição do pilar 3). REMODELADO de liurialves:6af2d90e1586e43ae33e6ac4 ("Aos 17 anos eu
   disse a ela...", 10/11 12:40, 526 views, 3 comentários; o mais visto dos últimos 30 dias ainda não replicado em 14 dias).
   Mantém: faixa, 1ª pessoa com número no título, arco cronológico, lição com ação. Muda: trecho (item 16, o Punto de 450 €),
   fotos (Drive 74, 75, 76), lição de preço e CTA de comentário.
3) 17:40 FAIXA, valor, pilar 1, capa com rosto (47) + cena da Aeronáutica (43) e a opinião no 2º slide: rotina de 30 min/dia.
4) 20:30 CAPA + ESCURO, prova, pilar 5/4: Revolut julho -589 € → agosto +1.544 € → setembro +124 € (prints reais,
   recorte só dos cartões Rendimento e Fluxo líquido). Capa Drive 69.
5) 22:15 FAIXA, bandeira, pilar 5: "Eu não prometo faturamento a ninguém. Eu prometo outra coisa." (item 20 + entrega de 30 dias). Refeito em 11/11 sem o tema indicação.
"""
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps
S = "/tmp/claude-0/-home-claude-carrosseis/74052357-f8b7-5a10-bcdc-39a6cf1cce7d/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-11"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h11/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px11/pexels-{x}.jpg"

# 1) 12:40 FAIXA, CONEXÃO, CTA = ENVIO + CLIENTES
perder = {"slides": [
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.35, "grande": True, "arraste": True, "faixa": "O QUE EU APRENDI",
   "texto": "PARA GANHAR, EU SEMPRE PERDI ALGUMA COISA ANTES."},
  {"tipo": "foto", "foto": HP("35"), "foco_y": 0.2, "faixa": "PERDI 45 DIAS DE FAMÍLIA",
   "texto": "NA QUARENTENA DA AERONÁUTICA FIQUEI CERCA DE 40 A 45 DIAS LONGE DE CASA. SENTIA SAUDADE ATÉ DE ANDAR DE ÔNIBUS.",
   "destaque": "GANHEI A DISCIPLINA QUE EU USO ATÉ HOJE."},
  {"tipo": "foto", "foto": HP("44"), "foco_y": 0.3, "faixa": "PERDI A ESTABILIDADE",
   "texto": "DEPOIS DE 4 ANOS PEDINDO AUTORIZAÇÃO PARA TUDO, ATÉ PARA SAIR DA CIDADE, EU SAÍ DA AERONÁUTICA.",
   "destaque": "GANHEI A DECISÃO DE CONSTRUIR ALGO MEU."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.45, "faixa": "PERDI 3 MESES COM ELES",
   "texto": "VIM PARA PORTUGAL SOZINHO, COM 300 €. A MINHA ESPOSA E O NOSSO BEBÊ SÓ CHEGARAM 3 MESES DEPOIS."},
  {"tipo": "foto", "foto": FL("cafe-pastel-pao-de-queijo"), "foco_y": 0.45, "faixa": "PERDI AS FOLGAS",
   "texto": "NOS PRIMEIROS 5 MESES EU TRABALHAVA 12 HORAS POR DIA E VENDIA A FOLGA.",
   "destaque": "CONSEGUIMOS O QUARTO NO MESMO DIA EM QUE ELA CHEGOU."},
  {"tipo": "foto", "foto": FL("video-rotina-9s"), "foco_y": 0.3, "faixa": "PERDI O FIM DE SEMANA",
   "texto": "SAÍA DO RESTAURANTE À MEIA-NOITE E IA PARA UM CLUBE ATÉ AS 8 DA MANHÃ, POR 60 € A NOITE."},
  {"tipo": "branco", "blocos": [
   ["t", "PARA SAIR DO MESMO FATURAMENTO, ALGUMA COISA VAI TER QUE SAIR DA SUA SEMANA. ESCOLHA HOJE:"], ["esp", 10],
   ["h", "1. O QUE VOCÊ CORTA"],
   ["n", "Ache 3 horas por semana que hoje não trazem cliente. Exemplo: o feed rolando depois das 22h."],
   ["h", "2. ONDE ESSAS HORAS ENTRAM"],
   ["n", "1 hora para 5 mensagens a ex-clientes, 1 para gravar 1 vídeo, 1 para responder todo direct no mesmo dia."],
   ["h", "3. POR QUANTO TEMPO"],
   ["n", "30 dias. No fim, conte quantas conversas viraram cliente."]]},
  {"tipo": "foto", "foto": FL("video-rotina-17s"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM ESTÁ PARADO",
   "texto": "NO MESMO FATURAMENTO. E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT.",
   "destaque": "EU TE AJUDO A ESCOLHER O QUE TROCAR NA SUA SEMANA."},
]}

# 2) 14:20 FAIXA, CONEXÃO, REMODELADO, CTA = COMENTÁRIO + CLIENTES
punto = {"slides": [
  {"tipo": "foto", "foto": HP("74"), "foco_y": 0.45, "grande": True, "arraste": True, "faixa": "O MEU PRIMEIRO CARRO EM PORTUGAL",
   "texto": "PAGUEI 450 € NUM FIAT PUNTO DE 1996. DUROU 2 MESES."},
  {"tipo": "foto", "foto": HP("75"), "foco_y": 0.4, "faixa": "ERA O QUE CABIA NO BOLSO",
   "texto": "FOI NO ANO EM QUE NASCEU O NOSSO SEGUNDO FILHO. O DINHEIRO NÃO DAVA PARA MAIS DO QUE ISSO."},
  {"tipo": "foto", "foto": HP("76"), "foco_y": 0.45, "faixa": "PRIMEIRO, O MOTOR",
   "texto": "O MOTOR AQUECEU. DEPOIS DISSO O CARRO SÓ LIGAVA EMPURRANDO."},
  {"tipo": "foto", "foto": FL("video-rotina-1s"), "foco_y": 0.3, "faixa": "DEPOIS, AS MUDANÇAS",
   "texto": "O CABO DAS MUDANÇAS PARTIU. COM 2 MESES, O CARRO DE 450 € ACABOU.",
   "destaque": "E EU TIVE QUE COMPRAR O SEGUNDO CARRO."},
  {"tipo": "branco", "blocos": [
   ["h", "NO SEU NEGÓCIO, O PUNTO DE 450 € É O PREÇO BAIXO PARA ENCHER A AGENDA."], ["esp", 8],
   ["n", "Parece um bom negócio no dia. Dois meses depois, a agenda está cheia de quem veio pelo desconto e o dinheiro não sobra."],
   ["n", "Personal trainer, academia, fisioterapia ou barbearia: a conta é a mesma."]]},
  {"tipo": "branco", "blocos": [
   ["t", "FAÇA ESTA CONTA ANTES DA PRÓXIMA PROMOÇÃO:"], ["esp", 10],
   ["h", "1. ABRA A AGENDA DO MÊS PASSADO"],
   ["n", "Marque quem entrou por promoção e quem entrou pelo preço cheio."],
   ["h", "2. VEJA QUEM CONTINUA"],
   ["n", "Conte quantos de cada grupo voltaram este mês."],
   ["h", "3. TROQUE O DESCONTO POR BÔNUS"],
   ["n", "Se quem veio pelo desconto não ficou, mantenha o preço e dê algo a mais na 1ª visita. Exemplo: avaliação física incluída."]]},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E OLHO COM VOCÊ O PREÇO DO SEU SERVIÇO.",
   "destaque": "PREÇO BAIXO NÃO TIRA NINGUÉM DO MESMO FATURAMENTO."},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO, CTA = SALVAR + CLIENTES
rotina = {"slides": [
  {"tipo": "foto", "foto": HP("47"), "foco_y": 0.08, "grande": True, "arraste": True, "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "TEM CLIENTE ESQUECIDO NO SEU WHATSAPP. 30 MINUTOS POR DIA ACHAM ELE."},
  {"tipo": "foto", "foto": HP("43"), "foco_y": 0.35, "faixa": "O QUE EU APRENDI NA FARDA",
   "texto": "CAMA FEITA, BOTA ENGRAXADA E BARBA FEITA TODO DIA, COM VONTADE OU SEM VONTADE.",
   "destaque": "EU ACREDITO QUE CLIENTE TODO MÊS VEM DE ROTINA CHATA REPETIDA."},
  {"tipo": "branco", "blocos": [
   ["h", "QUEM PERGUNTOU O PREÇO E SUMIU AINDA TEM O PROBLEMA"], ["esp", 8],
   ["n", "Ele perguntou, recebeu o valor e a conversa morreu ali. A dor nas costas, o treino parado e o cabelo por cortar continuam."],
   ["n", "Falta um motivo para ele voltar a falar com você. A rotina abaixo dá esse motivo todo dia. Faça na ordem."]]},
  {"tipo": "branco", "blocos": [
   ["t", "MINUTOS 0 A 10"], ["h", "RESPONDA O QUE ESTÁ PARADO"], ["esp", 8],
   ["n", "Direct, WhatsApp e comentários. Quem perguntou o preço e não marcou recebe esta:"],
   ["n", "\"[Nome], ainda quer começar esta semana? Tenho [terça às 19h] ou [quinta às 7h]. Qual fica melhor?\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "MINUTOS 10 A 20"], ["h", "5 MENSAGENS PARA QUEM JÁ FOI CLIENTE"], ["esp", 8],
   ["n", "Abra a lista de quem não aparece há 60 dias e mande para 5 por dia:"],
   ["n", "\"[Nome], estou fechando a agenda de [dezembro]. Guardei 3 horários para quem já treinou comigo. Quer um?\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "MINUTOS 20 A 30"], ["h", "1 VÍDEO QUE PEDE CONVERSA"], ["esp", 8],
   ["n", "Grave 30 segundos respondendo a uma dúvida que um cliente te fez esta semana."],
   ["n", "Termine com: \"me chama no direct com a palavra AVALIAÇÃO\"."]]},
  {"tipo": "branco", "blocos": [
   ["h", "NO FIM DO DIA, ANOTE 3 NÚMEROS"], ["esp", 8],
   ["n", "Mensagens enviadas, respostas e horários marcados."],
   ["n", "Em 30 dias você sabe quantas mensagens precisa para fechar 1 cliente. Exemplo ilustrativo: 25 mensagens, 5 respostas, 1 aluno novo."]]},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.3, "faixa": "SALVE E COMECE AMANHÃ",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT PARA MONTAR A ROTINA DO SEU NEGÓCIO.",
   "destaque": "30 MINUTOS, TODO DIA, POR 30 DIAS."},
]}

# 4) 20:30 CAPA + ESCURO, PROVA, CTA = ENVIO + CLIENTES (fatia-1 = prints reais, montado à parte)
prova = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": HP("69"), "foco_y": 0.45, "etiqueta": "Prova",
   "titulo": "Julho: -589 € na minha conta. Agosto: +1.544 €.",
   "sub": "Os prints são reais. Eu olho este número todo mês."},
  {"etiqueta": "O print", "frase": "x", "texto": "x"},  # substituído pelo slide dos prints
  {"etiqueta": "Julho", "frase": "Entraram 4.669 €. Saíram 5.257 €. [[Fluxo de -589 €]].",
   "texto": "O dinheiro continuava entrando todo mês. Sem abrir a análise da conta, eu ia achar que estava tudo bem."},
  {"etiqueta": "Agosto", "frase": "Entraram 6.849 €. Saíram 5.306 €. [[Sobraram 1.544 €]].",
   "texto": "O gasto ficou quase igual ao de julho. O que mudou foi o lado de quem entra: 2.181 € a mais no mês."},
  {"etiqueta": "Setembro", "frase": "Entraram 5.135 €. Saíram 5.011 €. [[+124 €]].",
   "texto": "Positivo, mas apertado. Eu mostro o mês fraco também, porque é ele que me diz onde mexer."},
  {"etiqueta": "Por que eu olho", "frase": "Eu já quebrei uma loja porque [[não via o prejuízo]].",
   "texto": "A conta da loja era a mesma de casa. Hoje, todo mês, eu vejo três números: quanto entrou, quanto saiu e quanto sobrou."},
  {"etiqueta": "Faça hoje", "frase": "A sua análise [[em 20 minutos]].",
   "texto": "Abra o extrato dos últimos 3 meses. Some o que entrou e o que saiu em cada mês e escreva a diferença ao lado. No mês negativo, procure os 3 maiores gastos."},
  {"etiqueta": "Para quem é", "frase": "Para o dono que fatura e [[não vê sobrar]].",
   "texto": "Personal trainer, academia, fisioterapia ou barbearia, entre 1.500 € e 5.000 € por mês, trabalhando que nem um condenado sem saber para onde foi o dinheiro."},
  {"etiqueta": "Próximo passo", "frase": "Envie para um sócio [[que nunca abre o extrato]].",
   "texto": "E se esse dono é você, comente CLIENTES. Eu te chamo no direct e a gente olha os números do seu negócio."},
]}

# 5) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = COMENTÁRIO + CLIENTES
bandeira = {"slides": [
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.25, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO PROMETO FATURAMENTO A NINGUÉM. EU PROMETO OUTRA COISA."},
  {"tipo": "foto", "foto": P(14963655), "foco_y": 0.4, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "EM 2026 A MINHA EMPRESA SAIU DE 1.500 € PARA 7.000 € POR MÊS. NINGUÉM ME PROMETEU ISSO.",
   "destaque": "O QUE MUDOU FOI A MINHA ATITUDE E O QUE EU PASSEI A EXECUTAR."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.25, "faixa": "O QUE UM NÚMERO NÃO MOSTRA",
   "texto": "O FATURAMENTO DEPENDE DO SEU MERCADO, DO SEU PREÇO E DO QUE VOCÊ FAZ DEPOIS DE CADA CONVERSA. ISSO EU NÃO CONTROLO."},
  {"tipo": "foto", "foto": P(9644527), "foco_y": 0.45, "faixa": "EXEMPLO: DUAS ACADEMIAS",
   "texto": "A MESMA CAMPANHA RODA NAS DUAS. UMA RESPONDE EM 5 MINUTOS, A OUTRA NO DIA SEGUINTE. O RESULTADO NÃO VAI SER IGUAL."},
  {"tipo": "foto", "foto": P(34865582), "foco_y": 0.45, "faixa": "EXEMPLO: A BARBEARIA",
   "texto": "O DONO RECEBE O ROTEIRO DE ATENDIMENTO E GUARDA NA GAVETA. NENHUM MÉTODO TRABALHA SOZINHO."},
  {"tipo": "foto", "foto": FL("video-rotina-9s"), "foco_y": 0.3, "faixa": "O QUE EU PROMETO",
   "texto": "EM 30 DIAS: OFERTA REVISTA, PERFIL AJUSTADO, FUNIL MONTADO, PRIMEIRA CAMPANHA NO AR E ROTEIRO DE ATENDIMENTO.",
   "destaque": "ISSO EU CONTROLO. EXECUTAR É COM VOCÊ."},
  {"tipo": "branco", "blocos": [
   ["t", "ANTES DE PAGAR QUALQUER AJUDA PARA O SEU NEGÓCIO, FAÇA ESTAS 3 PERGUNTAS:"], ["esp", 10],
   ["h", "1. O QUE VAI ESTAR PRONTO EM 30 DIAS?"],
   ["n", "Se a resposta for só um número de faturamento, peça a lista de entregas."],
   ["h", "2. O QUE DEPENDE DE MIM?"],
   ["n", "Quem trabalha sério te diz o que você vai ter de fazer toda semana."],
   ["h", "3. COMO EU MEÇO SE ESTÁ FUNCIONANDO?"],
   ["n", "Três números por semana: contatos, conversas e vendas."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.15, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E TE MOSTRO O QUE ESTARIA PRONTO NO SEU NEGÓCIO EM 30 DIAS.",
   "destaque": "EU PROMETO O QUE EU CONTROLO."},
]}

LEGENDAS = {
 1: """Para ganhar, eu sempre perdi alguma coisa antes.

Na quarentena da Aeronáutica fiquei cerca de 40 a 45 dias longe de casa, com saudade até de andar de ônibus. Depois de 4 anos pedindo autorização para tudo, saí. Vim para Portugal sozinho, com 300 €, e a minha esposa e o nosso bebê só chegaram 3 meses depois. Nos primeiros 5 meses trabalhava 12 horas por dia e vendia a folga. No fim de semana saía do restaurante à meia-noite e ia para um clube até as 8 da manhã, por 60 € a noite.

Para sair do mesmo faturamento, alguma coisa vai ter que sair da sua semana. Ache hoje 3 horas que não trazem cliente e troque por isto, durante 30 dias: 5 mensagens a ex-clientes, 1 vídeo gravado e todo direct respondido no mesmo dia.

🔻 Envie para quem está parado no mesmo faturamento. E comente CLIENTES que eu te chamo no direct e te ajudo a escolher o que trocar na sua semana.

#empreendedorismo #donodenegocio #historiareal #brasileiroemportugal #personaltrainer""",
 2: """Paguei 450 € num Fiat Punto de 1996. Durou 2 meses.

Foi o meu primeiro carro em Portugal, no ano em que nasceu o nosso segundo filho. Era o que cabia no bolso. O motor aqueceu e o carro passou a ligar só empurrando. Depois o cabo das mudanças partiu. Com 2 meses acabou, e eu tive que comprar o segundo carro.

No seu negócio, o Punto de 450 € é o preço baixo para encher a agenda. Antes da próxima promoção, abra a agenda do mês passado, marque quem entrou pelo desconto e quem entrou pelo preço cheio, e conte quantos de cada grupo voltaram. Se quem veio pelo desconto não ficou, mantenha o preço e dê um bônus na 1ª visita.

🔻 Comente CLIENTES que eu te chamo no direct e olho com você o preço do seu serviço.

#empreendedorismo #donodenegocio #preco #personaltrainer #barbearia""",
 3: """Tem cliente esquecido no seu WhatsApp. 30 minutos por dia acham ele.

Quem perguntou o preço e sumiu ainda tem o problema. Falta um motivo para voltar a falar com você.

Na Aeronáutica era cama feita, bota engraxada e barba feita todo dia, com vontade ou sem vontade. Eu acredito que cliente todo mês vem desse tipo de rotina, chata e repetida.

A rotina, para personal trainer, academia, fisioterapia e barbearia:
1. Minutos 0 a 10: responda tudo que está parado (mensagem pronta no slide 4).
2. Minutos 10 a 20: 5 mensagens para quem não aparece há 60 dias (slide 5).
3. Minutos 20 a 30: 1 vídeo de 30 segundos respondendo a uma dúvida real de cliente.
No fim do dia, anote mensagens enviadas, respostas e horários marcados.

🔻 Salve e comece amanhã. E comente CLIENTES que eu te chamo no direct para montar a rotina do seu negócio.

#personaltrainer #academia #fisioterapia #barbearia #donodenegocio""",
 4: """Julho: -589 € na minha conta. Agosto: +1.544 €. Os prints estão no slide 2.

Julho: entraram 4.669 € e saíram 5.257 €. Agosto: entraram 6.849 € e saíram 5.306 €. Setembro: entraram 5.135 € e saíram 5.011 €, sobraram 124 €. Eu mostro o mês fraco também.

Eu já quebrei uma loja porque não via o prejuízo: a conta da loja era a mesma de casa. Hoje, todo mês, eu olho quanto entrou, quanto saiu e quanto sobrou.

Faça a sua em 20 minutos: abra o extrato dos últimos 3 meses, some o que entrou e o que saiu em cada um e escreva a diferença ao lado. No mês negativo, procure os 3 maiores gastos.

🔻 Envie para um sócio que nunca abre o extrato. E se esse dono é você, comente CLIENTES que eu te chamo no direct e a gente olha os números do seu negócio.

#gestaofinanceira #donodenegocio #empreendedorismo #personaltrainer #barbearia""",
 5: """Eu não prometo faturamento a ninguém. Eu prometo outra coisa.

Em 2026 a minha empresa saiu de 1.500 € para 7.000 € por mês, e ninguém me prometeu isso. O que mudou foi a minha atitude e o que eu passei a executar. O faturamento depende do seu mercado, do seu preço e do que você faz depois de cada conversa. Isso eu não controlo.

O que eu controlo cabe numa lista: em 30 dias, oferta revista, perfil ajustado, funil montado, primeira campanha no ar e roteiro de atendimento. Executar é com você.

Antes de pagar qualquer ajuda para o seu negócio, pergunte: o que vai estar pronto em 30 dias? O que depende de mim? Como eu meço se está funcionando?

🔻 Comente CLIENTES que eu te chamo no direct e te mostro o que estaria pronto no seu negócio em 30 dias.

#empreendedorismo #donodenegocio #personaltrainer #barbearia #academia""",
}


def inter(t, peso="Bold"):
    f = ImageFont.truetype(f"{R}/assets/fonts/Inter.ttf", t)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f


def slide_prints(dst, i, n):
    """Fatia escura com os 3 recortes reais da análise da Revolut (só Rendimento e Fluxo líquido; sem saldo nem ativos)."""
    cortes = [("JULHO", "/tmp/h11/rev-jul.jpg", (20, 680, 740, 1050)),
              ("AGOSTO", "/tmp/h11/rev-ago.jpg", (20, 640, 780, 1010)),
              ("SETEMBRO", "/tmp/h11/rev-set.jpg", (20, 640, 780, 1010))]
    im = Image.new("RGB", (1080, 1350), (14, 14, 14)); d = ImageDraw.Draw(im)
    d.text((110, 90), "O PRINT", font=inter(30, "Bold"), fill=(217, 84, 30))
    d.text((110, 138), "Análise mensal da minha conta.", font=inter(48, "Bold"), fill=(242, 239, 234))
    y = 230
    for rot, src, box in cortes:
        c = Image.open(src).convert("RGB").crop(box)
        c = ImageOps.contain(c, (700, 290))
        d.text((110, y + c.height // 2), rot, font=inter(30, "Bold"), fill=(245, 197, 24), anchor="lm")
        x = 1080 - 90 - c.width
        mask = Image.new("L", c.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, c.width, c.height), 22, fill=255)
        im.paste(c, (x, y), mask)
        y += c.height + 28
    d.text((110, 1215), "Prints reais. Saldo e dados da conta cortados.", font=inter(28, "Regular"), fill=(168, 164, 158))
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
    # Refeito em 11/11 a pedido do dono (menos "indicação"): 17:40 e 22:15 renderizados em pastas novas (-3b e -5b)
    # para o Buffer puxar imagens novas; as pastas -3 e -5 antigas foram apagadas.
    import sys
    if "--refazer" in sys.argv:
        for n in ("3b", "5b"):
            if os.path.isdir(O(n)):
                for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
        run(rotina, O("3b")); run(bandeira, O("5b"))
    else:
        for n in (1, 2, 4):
            if os.path.isdir(O(n)):
                for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
        run(perder, O(1)); run(punto, O(2)); run(rotina, O("3b"))
        run(prova, O(4), "render_formatos.py"); slide_prints(f"{O(4)}/fatia-1.jpg", 2, len(prova["slides"]))
        run(bandeira, O("5b"))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
