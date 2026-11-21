"""Plano 100 mil, semana 4 do PDF (janela de testes, dia 2), 15/11/2026, domingo. Dia 9 do "Plano de 30 dias para lançar
a mentoria": conteúdo "Conta pessoal misturada com a da empresa" (valor das 17:40) e tarefa "Follow-up com quem não
respondeu" (mensagem pronta no doc).
AJUSTE DO DONO EM 10/11 (prevalece sobre a tarefa agendada em quantidade, horários e formato): 5 posts, sem post de IA.
Domingo: 12:40 CONEXÃO · 14:20 CONEXÃO · 17:40 VALOR com rosto · 20:30 PROVA · 22:15 BANDEIRA.
AJUSTE DE 11/11: "indicação" em 0 de 5 posts hoje (ontem foi 1, no valor).
Sem prints novos nas pastas do Drive. Print ainda NÃO usado em carrossel: stripe-pagamento-9-90-08-11.png (prova-social,
08/11) -> prova das 20:30 (recorte do dia/hora e da notificação; e-mail do comprador já desfocado no original).
CTA (rodízio, todos terminam em "Comente CLIENTES"): 12:40 envio · 14:20 comentário · 17:40 salvar · 20:30 comentário · 22:15 salvar.
1) 12:40 FAIXA, conexão, pilar 5 (lição pilar 4): "Eu já precisei de 900 € e ganhava 700 €. A minha meta para 2027 é
   100 mil euros por mês." Itens 17 a 20 e 22. REMODELADO de liurialves:6af691e9da25c4db3e952aa6 (Uber, 396 views): mesmo
   arco antes → hoje com números; gancho novo (a meta), capa nova (Drive 46), lição nova (meta em clientes por semana).
2) 14:20 FAIXA, conexão, pilar 5 (lição pilar 1): "Passei quase 45 dias sem ver a minha família. Senti saudade até de
   andar de ônibus." Itens 6 a 10. Estrutura do noivado (6af691e95ec1c9d5be5c5009, 678 views): fase da farda, capa Drive 43.
3) 17:40 FAIXA, valor, pilar 4: conta da empresa separada em 4 passos. Molde TrueCoach (09/04/2026, erro nº 4).
4) 20:30 CAPA + ESCURO, prova, pilar 5 (lição pilar 3): Stripe 9,90 € num domingo às 15h.
5) 22:15 FAIXA, bandeira, pilar 6 (lição pilar 1): "Eu não acredito em esperar estar pronto para começar." Item 13.
"""
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps
S = "/tmp/claude-0/-home-claude-carrosseis/6ad18000-d4fa-58d9-91bf-e55bb405cbd4/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-15"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h15/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px15/pexels-{x}.jpg"

# 1) 12:40 FAIXA, CONEXÃO (REMODELADO), CTA = ENVIO + CLIENTES
meta = {"slides": [
  {"tipo": "foto", "foto": HP("46"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "A MINHA META PARA 2027",
   "texto": "EU JÁ PRECISEI DE 900 € POR MÊS E GANHAVA 700 €. AGORA A META É 100 MIL EUROS POR MÊS."},
  {"tipo": "foto", "foto": HP("78"), "foco_y": 0.2, "faixa": "OS PRIMEIROS ANOS EM LISBOA",
   "texto": "PARA VIVER, EU PRECISAVA DE 800 A 900 € POR MÊS. RECEBIA 700 €.",
   "destaque": "UM GERENTE AMIGO ME EMPRESTAVA A DIFERENÇA."},
  {"tipo": "foto", "foto": P("38390360"), "foco_y": 0.5, "faixa": "PARA FECHAR A CONTA",
   "texto": "12 HORAS NO RESTAURANTE. NO FIM DE SEMANA, DA MEIA-NOITE ÀS 8 DA MANHÃ NUM CLUBE, POR 60 € A NOITE."},
  {"tipo": "foto", "foto": P("39487359"), "foco_y": 0.6, "faixa": "DEPOIS",
   "texto": "2 ANOS DE UBER EM PORTUGAL. COM O CARRO DANDO PROBLEMA, EU ME CANSEI.",
   "destaque": "DECIDI QUE IA GANHAR MAIS."},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.35, "faixa": "2026",
   "texto": "VOLTEI PARA A MASSAGEM E COMECEI A CRIAR SITES PARA CLIENTES. O FATURAMENTO SAIU DE 1.500 € PARA 7.000 € POR MÊS.",
   "destaque": "A MINHA VIDA MUDOU COM A MINHA ATITUDE."},
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.35, "faixa": "O PRÓXIMO NÚMERO",
   "texto": "EU CREIO QUE VOU FATURAR 100 MIL EUROS POR MÊS AINDA EM 2027.",
   "destaque": "DESDE OS 17 EU REPITO: TUDO O QUE EU QUERO, EU CONQUISTO."},
  {"tipo": "branco", "blocos": [
   ["h", "META SEM NÚMERO DA SEMANA É SÓ VONTADE."], ["esp", 8],
   ["n", "Quem está parado no mesmo faturamento costuma ter uma meta solta: \"este ano eu cresço\". Ela não diz o que fazer na segunda."],
   ["n", "Faça hoje: meta do mês ÷ valor de um cliente = clientes que você precisa. Exemplo ilustrativo de um personal com 30 alunos a 80 €: meta de 4.000 € = 50 alunos. Faltam 20. Em 12 semanas, são menos de 2 alunos novos por semana. Esse é o número que vai para a agenda."]]},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.2, "faixa": "ENVIE PARA QUEM DIZ \"ESTE ANO EU CRESÇO\"",
   "texto": "E COMENTE CLIENTES COM A SUA META. EU TE CHAMO NO DIRECT E A GENTE TRANSFORMA ELA EM CLIENTES POR SEMANA.",
   "destaque": "QUAL É O SEU NÚMERO?"},
]}

# 2) 14:20 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES
quarentena = {"slides": [
  {"tipo": "foto", "foto": HP("43"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "AERONÁUTICA, OS PRIMEIROS DIAS",
   "texto": "PASSEI QUASE 45 DIAS SEM VER A MINHA FAMÍLIA. SENTI SAUDADE ATÉ DE ANDAR DE ÔNIBUS."},
  {"tipo": "foto", "foto": HP("47"), "foco_y": 0.25, "faixa": "AOS 18 ANOS",
   "texto": "NO ALISTAMENTO EU DISSE QUE QUERIA SERVIR. PASSEI NOS TESTES E ENTREI.",
   "destaque": "AÍ VEIO A QUARENTENA: DE 40 A 45 DIAS LONGE DE CASA."},
  {"tipo": "foto", "foto": HP("11"), "foco_y": 0.3, "faixa": "LÁ DENTRO",
   "texto": "GRITO, CORRERIA E TROCA DE FARDA O DIA INTEIRO.",
   "destaque": "UM BANHO PASSOU A VALER MUITO."},
  {"tipo": "foto", "foto": P("15268069"), "foco_y": 0.5, "faixa": "DO LADO DE DENTRO DO MURO",
   "texto": "EU OLHAVA PARA FORA DO MURO E SENTIA SAUDADE DE ANDAR DE ÔNIBUS."},
  {"tipo": "foto", "foto": HP("44"), "foco_y": 0.45, "faixa": "O QUE MUDOU EM MIM",
   "texto": "FOI ALI QUE EU AMADURECI. O QUE EU ACHAVA PEQUENO PASSOU A TER VALOR."},
  {"tipo": "foto", "foto": HP("05"), "foco_y": 0.12, "faixa": "O QUE VEIO DEPOIS",
   "texto": "A FORMATURA, O NOIVADO E SALÁRIOS MELHORES.",
   "destaque": "ALI EU APRENDI A DAR VALOR A UM BANHO E A UM ÔNIBUS."},
  {"tipo": "branco", "blocos": [
   ["h", "O SEU CLIENTE TAMBÉM SENTE FALTA DO BÁSICO."], ["esp", 8],
   ["n", "Muitas vezes o aluno não sai pelo treino nem o paciente pela técnica. Sai pela mensagem que ficou sem resposta ou pelo horário trocado sem aviso."],
   ["n", "Faça hoje: mande para 5 clientes atuais \"Uma pergunta rápida: do que você sentiria falta se eu parasse amanhã?\". Anote as respostas. As palavras que se repetirem vão para a sua bio e para o seu próximo anúncio."]]},
  {"tipo": "foto", "foto": FL("video-rotina-5_5s"), "foco_y": 0.5, "faixa": "COMENTE CLIENTES",
   "texto": "E A RESPOSTA QUE MAIS TE SURPREENDEU. EU TE CHAMO NO DIRECT E A GENTE COLOCA ELA NO SEU PERFIL.",
   "destaque": "DO QUE O SEU CLIENTE SENTIRIA FALTA?"},
]}

# 3) 17:40 FAIXA, VALOR COM ROSTO, CTA = SALVAR + CLIENTES
contas = {"slides": [
  {"tipo": "foto", "foto": FL("video-rotina-9s"), "foco_y": 0.4, "grande": True, "arraste": True, "faixa": "PERSONAL, ACADEMIA, FISIO, BARBEARIA",
   "texto": "O DINHEIRO DA EMPRESA PAGA A CONTA DE CASA? ENTÃO VOCÊ NÃO SABE SE TEM LUCRO."},
  {"tipo": "foto", "foto": P("10557059"), "foco_y": 0.5, "faixa": "O QUE EU ACREDITO",
   "texto": "EU JÁ QUEBREI UMA LOJA DE MODA PRAIA ASSIM. A CONTA DA LOJA ERA A MESMA DE CASA.",
   "destaque": "O DINHEIRO DELA FOI EMBORA EM VIAGENS E CONTAS DE CASA."},
  {"tipo": "foto", "foto": P("6633602"), "foco_y": 0.6, "faixa": "NÃO SOU SÓ EU",
   "texto": "UM GUIA DA TRUECOACH PARA PERSONAL TRAINERS (ABRIL DE 2026) PÕE MISTURAR AS CONTAS ENTRE OS MAIORES ERROS FINANCEIROS DE QUEM DÁ AULA."},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "ABRA UMA CONTA SÓ DA EMPRESA"], ["esp", 8],
   ["n", "Pode ser num banco digital, ainda hoje. Todo pagamento de aluno ou paciente cai nela: MB Way, Pix, transferência ou cartão."],
   ["n", "Na conta pessoal não entra mais nenhum euro de cliente."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "DEFINA O SEU SALÁRIO FIXO"], ["esp", 8],
   ["n", "Um valor igual todo mês, transferido sempre no mesmo dia (por exemplo, dia 5). É o único dinheiro que sai da empresa para casa."],
   ["n", "Comece com um valor que a empresa paga mesmo num mês fraco."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "A CONTA DO MÊS, NESTA ORDEM"], ["esp", 8],
   ["n", "Exemplo ilustrativo de uma barbearia que faturou 3.000 €:"],
   ["n", "Custos (aluguel, produtos, sistemas): 900 €. Seu salário fixo: 1.500 €. Reserva de 10%: 300 €. Sobra para reinvestir: 300 €."],
   ["n", "Se não sobrar nada, você descobre o problema antes de ele virar dívida."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "15 MINUTOS TODA SEGUNDA"], ["esp", 8],
   ["n", "Abra o extrato da empresa e anote 3 números: quanto entrou, quanto saiu e o saldo."],
   ["n", "Se o saldo cair 3 segundas seguidas, mexa no preço ou nos custos antes de mexer no seu salário."]]},
  {"tipo": "foto", "foto": FL("video-rotina-1s"), "foco_y": 0.45, "faixa": "SALVE E FAÇA NA SEGUNDA",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E OLHO A DIVISÃO DO SEU MÊS COM VOCÊ.",
   "destaque": "A EMPRESA NÃO É A SUA CARTEIRA."},
]}

# 4) 20:30 CAPA + ESCURO, PROVA, CTA = COMENTÁRIO + CLIENTES
prova = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": FL("home-office-headset"), "foco_y": 0.3, "etiqueta": "Prova",
   "titulo": "Domingo, 15h. Entraram 9,90 € e eu não atendi ninguém.",
   "sub": "Na massagem eu só recebo quando atendo. Aqui é diferente."},
  {"etiqueta": "O print", "frase": "x", "texto": "x"},  # substituído pelo slide do print
  {"etiqueta": "O que é", "frase": "É a assinatura da [[minha plataforma]].",
   "texto": "As plataformas que eu construí cobram uma assinatura mensal pelo Stripe. Este aviso chegou no domingo, 8/11. No sábado tinha chegado outro igual."},
  {"etiqueta": "Por que eu mostro 9,90 €", "frase": "O valor é pequeno. [[O modelo não é.]]",
   "texto": "Na massagem, se eu paro, a entrada para junto. Na assinatura, a pessoa paga todo mês enquanto o serviço continua valendo para ela."},
  {"etiqueta": "No seu negócio", "frase": "Sessão avulsa é [[começar do zero]] todo mês.",
   "texto": "Personal com aula solta, fisioterapia cobrada por consulta, barbearia esperando o cliente lembrar do corte: no dia 1, a conta volta a zero."},
  {"etiqueta": "Faça hoje", "frase": "Monte [[1 plano mensal]] com o que você já vende.",
   "texto": "Pegue o serviço que o cliente mais repete. Exemplo ilustrativo de um personal: 8 aulas por mês, cobrança no mesmo dia, 280 € contra 40 € a aula avulsa. Ofereça primeiro a quem já vem toda semana."},
  {"etiqueta": "Para quem é", "frase": "Para quem fatura entre [[1.500 € e 5.000 €]] e começa o mês do zero.",
   "texto": "Personal trainer, academia, fisioterapia ou barbearia que vende sessão solta e não sabe quanto entra no mês que vem."},
  {"etiqueta": "Próximo passo", "frase": "Quanto do seu mês [[já está pago]] no dia 1?",
   "texto": "Comente CLIENTES. Eu te chamo no direct e a gente desenha o seu plano mensal."},
]}

# 5) 22:15 FAIXA, CONEXÃO TIPO BANDEIRA, CTA = SALVAR + CLIENTES
pronto = {"slides": [
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "O QUE EU ACREDITO",
   "texto": "EU NÃO ACREDITO EM ESPERAR ESTAR PRONTO PARA COMEÇAR."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.7, "faixa": "POR QUE EU PENSO ASSIM",
   "texto": "EU VIM PARA PORTUGAL SOZINHO, COM 300 €. A MINHA ESPOSA AJUDOU A JUNTAR O DINHEIRO."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.45, "faixa": "OS PRIMEIROS 5 MESES",
   "texto": "12 HORAS POR DIA DE TRABALHO. EU AINDA VENDIA A FOLGA.",
   "destaque": "PRONTO EU NÃO ESTAVA. FUI MESMO ASSIM."},
  {"tipo": "foto", "foto": P("9958668"), "foco_y": 0.6, "faixa": "EXEMPLO: O PERSONAL",
   "texto": "ESPERA TER SITE, LOGO NOVO E 10 MIL SEGUIDORES PARA FAZER O PRIMEIRO ANÚNCIO."},
  {"tipo": "foto", "foto": P("19020383"), "foco_y": 0.5, "faixa": "EXEMPLO: A BARBEARIA",
   "texto": "QUER REFORMAR A LOJA ANTES DE LANÇAR O PLANO MENSAL. ENQUANTO ISSO, A CADEIRA FICA VAZIA NA TERÇA."},
  {"tipo": "foto", "foto": FL("video-rotina-17s"), "foco_y": 0.35, "faixa": "O QUE EU DEFENDO",
   "texto": "LANCE DO JEITO QUE ESTÁ E AJUSTE COM O QUE OS CLIENTES RESPONDEREM.",
   "destaque": "QUEM VENDE APRENDE MAIS DO QUE QUEM SÓ PLANEJA."},
  {"tipo": "branco", "blocos": [
   ["t", "ESTA SEMANA, DO JEITO QUE ESTÁ:"], ["esp", 10],
   ["h", "1. ESCREVA A OFERTA EM 3 LINHAS"],
   ["n", "Para quem é, o que entrega e quanto custa."],
   ["h", "2. MOSTRE PARA 10 PESSOAS"],
   ["n", "1 post, 1 story e 10 mensagens para clientes antigos."],
   ["h", "3. CONTE NA SEXTA"],
   ["n", "Quantos responderam e quantos perguntaram o preço. Só então mude alguma coisa."]]},
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.15, "faixa": "SALVE E LANCE ESTA SEMANA",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT E TE AJUDO A ESCREVER AS 3 LINHAS.",
   "destaque": "PRONTO VEM DEPOIS."},
]}

LEGENDAS = {
 1: """Eu já precisei de 900 € por mês e ganhava 700 €. Agora a minha meta é 100 mil euros por mês.

Nos primeiros anos em Lisboa, eu precisava de 800 a 900 € para viver e recebia 700 €. Um gerente amigo me emprestava a diferença. Eram 12 horas no restaurante e, no fim de semana, da meia-noite às 8 da manhã num clube, por 60 € a noite. Depois vieram 2 anos de Uber, até eu me cansar e decidir ganhar mais. Em 2026 voltei para a massagem, comecei a criar sites para clientes, e o faturamento saiu de 1.500 € para 7.000 € por mês. Eu creio que vou faturar 100 mil euros por mês ainda em 2027.

Meta sem número da semana é só vontade. Faça hoje: meta do mês ÷ valor de um cliente = clientes que você precisa. Exemplo ilustrativo de um personal com 30 alunos a 80 €: meta de 4.000 € = 50 alunos. Faltam 20. Em 12 semanas, são menos de 2 alunos novos por semana. Esse número vai para a agenda.

🔻 Envie para quem diz "este ano eu cresço". E comente CLIENTES com a sua meta que eu te chamo no direct e a gente transforma ela em clientes por semana.

#empreendedorismo #donodenegocio #metas #personaltrainer #historiareal""",
 2: """Passei quase 45 dias sem ver a minha família. Senti saudade até de andar de ônibus.

Aos 18 anos, no alistamento, eu disse que queria servir. Passei nos testes e entrei na Aeronáutica. Aí veio a quarentena: de 40 a 45 dias longe de casa, com grito, correria e troca de farda o dia inteiro. Um banho passou a valer muito. Eu olhava para fora do muro e sentia saudade de andar de ônibus. Foi ali que eu amadureci. Depois vieram a formatura, o noivado e salários melhores.

O seu cliente também sente falta do básico. Muitas vezes o aluno não sai pelo treino nem o paciente pela técnica: sai pela mensagem sem resposta ou pelo horário trocado sem aviso. Faça hoje: mande para 5 clientes atuais "Uma pergunta rápida: do que você sentiria falta se eu parasse amanhã?". As palavras que se repetirem vão para a sua bio e para o seu próximo anúncio.

🔻 Comente CLIENTES e a resposta que mais te surpreendeu. Eu te chamo no direct e a gente coloca ela no seu perfil.

Fotos: Robério Castro Fotografia

#empreendedorismo #donodenegocio #aeronautica #academia #historiareal""",
 3: """O dinheiro da empresa paga a conta de casa? Então você não sabe se tem lucro.

Eu já quebrei uma loja de moda praia assim. A conta da loja era a mesma de casa, e o dinheiro dela foi embora em viagens e contas da família. Não sou só eu: um guia da TrueCoach para personal trainers (abril de 2026) põe misturar as contas entre os maiores erros financeiros de quem dá aula.

A separação em 4 passos:
1. Abra uma conta só da empresa. Todo pagamento de aluno ou paciente cai nela (MB Way, Pix, transferência ou cartão).
2. Defina um salário fixo, transferido sempre no mesmo dia. É o único dinheiro que sai da empresa para casa.
3. A conta do mês nesta ordem. Exemplo ilustrativo de uma barbearia com 3.000 €: custos 900 €, salário 1.500 €, reserva de 10% 300 €, sobra para reinvestir 300 €.
4. Toda segunda, 15 minutos: entrou, saiu, saldo. Se o saldo cair 3 segundas seguidas, mexa no preço ou nos custos antes de mexer no seu salário.

🔻 Salve e faça na segunda. E comente CLIENTES que eu te chamo no direct e olho a divisão do seu mês com você.

Fonte: TrueCoach, "The Biggest Financial Mistakes Personal Trainers Make", 09/04/2026.

#gestaofinanceira #donodenegocio #personaltrainer #barbearia #fisioterapia""",
 4: """Domingo, 15h. Entraram 9,90 € e eu não atendi ninguém.

O print é real: é a assinatura da minha plataforma, cobrada pelo Stripe. Chegou no domingo, 8/11. No sábado tinha chegado outro igual. O valor é pequeno. O modelo não é: na massagem, se eu paro, a entrada para junto; na assinatura, a pessoa paga todo mês enquanto o serviço continua valendo para ela.

Sessão avulsa é começar do zero todo mês. Faça hoje: monte 1 plano mensal com o serviço que o cliente mais repete. Exemplo ilustrativo de um personal: 8 aulas por mês, cobrança no mesmo dia, 280 € contra 40 € a aula avulsa. Ofereça primeiro a quem já vem toda semana.

🔻 Quanto do seu mês já está pago no dia 1? Comente CLIENTES que eu te chamo no direct e a gente desenha o seu plano mensal.

#planomensal #recorrencia #personaltrainer #academia #donodenegocio""",
 5: """Eu não acredito em esperar estar pronto para começar.

Eu vim para Portugal sozinho, com 300 €. A minha esposa ajudou a juntar o dinheiro. Nos primeiros 5 meses eram 12 horas de trabalho por dia, e eu ainda vendia a folga. Pronto eu não estava. Fui mesmo assim.

Vejo o contrário toda semana: o personal que espera ter site, logo novo e 10 mil seguidores para fazer o primeiro anúncio; a barbearia que quer reformar a loja antes de lançar o plano mensal, com a cadeira vazia na terça.

Esta semana, do jeito que está:
1. Escreva a oferta em 3 linhas: para quem é, o que entrega e quanto custa.
2. Mostre para 10 pessoas: 1 post, 1 story e 10 mensagens para clientes antigos.
3. Na sexta, conte quantos responderam e quantos perguntaram o preço. Só então mude alguma coisa.

🔻 Salve e lance esta semana. E comente CLIENTES que eu te chamo no direct e te ajudo a escrever as 3 linhas.

#empreendedorismo #donodenegocio #oferta #barbearia #personaltrainer""",
}


def inter(t, peso="Bold"):
    f = ImageFont.truetype(f"{R}/assets/fonts/Inter.ttf", t)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f


def slide_print(dst, i, n):
    """Fatia escura com o print real do Stripe: dia/hora e a notificação (e-mail do comprador já desfocado)."""
    src = Image.open("/tmp/ps15/stripe.png").convert("RGB")
    topo = src.crop((60, 185, 768, 470)); notif = src.crop((25, 1300, 805, 1520))
    w = 780
    topo = topo.resize((w, int(topo.height * w / topo.width))); notif = notif.resize((w, int(notif.height * w / notif.width)))
    comp = Image.new("RGB", (w, topo.height + notif.height + 30), src.getpixel((400, 900)))
    comp.paste(topo, (0, 0)); comp.paste(notif, (0, topo.height + 30))
    im = Image.new("RGB", (1080, 1350), (14, 14, 14)); d = ImageDraw.Draw(im)
    d.text((110, 90), "O PRINT", font=inter(30, "Bold"), fill=(217, 84, 30))
    d.text((110, 138), "O aviso no meu celular.", font=inter(46, "Bold"), fill=(242, 239, 234))
    c = ImageOps.contain(comp, (860, 900))
    mask = Image.new("L", c.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, c.width, c.height), 26, fill=255)
    im.paste(c, ((1080 - c.width) // 2, 250), mask)
    d.text((110, 1215), "Print real. Dados do comprador desfocados.", font=inter(28, "Regular"), fill=(168, 164, 158))
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
    run(meta, O(1)); run(quarentena, O(2)); run(contas, O(3))
    run(prova, O(4), "render_formatos.py"); slide_print(f"{O(4)}/fatia-1.jpg", 2, len(prova["slides"]))
    run(pronto, O(5))
    json.dump(LEGENDAS, open(f"{S}/legendas-{DIA}.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
