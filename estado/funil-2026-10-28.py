import json, os, subprocess, sys, re
from PIL import Image
S = "/tmp/claude-0/-home-claude-carrosseis/77fd91f6-615b-5095-80b8-625e04866922/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-10-28"
F = lambda x: f"{S}/fotos/{x}.jpg"
FR = lambda x: f"{S}/frames/{x}.jpg"
PX = lambda x: f"{S}/pexels/pexels-{x}.jpg"
SF = lambda x: f"{R}/assets/spa-fundos/{x}.jpg"
SS = lambda x: f"{R}/assets/spa-site/{x}.jpg"
HL = lambda t: f"<span class='hl'>{t}</span>"
LOGO_SPA = f"{R}/assets/logos/lisboa-massagem.png"


def corta_topo(src, dst, frac=0.2):
    im = Image.open(src); w, h = im.size
    im.crop((0, int(h * frac), w, h)).save(dst, quality=92)
    return dst


def retrato(src, dst, cx=0.5):
    im = Image.open(src); w, h = im.size
    nw = int(h * 4 / 5); x0 = max(0, min(w - nw, int(w * cx - nw / 2)))
    im.crop((x0, 0, x0 + nw, h)).save(dst, quality=92)
    return dst


def run(script, cfg, out):
    p = f"{S}/cfg-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/{script}", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


# ---------------- @liurialves ----------------
# Tema do dia: o básico digital de quem está começando (oferta KIT).
# 12:10 POLÊMICA (tweet; ontem foi branco)
tweet = {"formato": "tweet", "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": f"{R}/assets/avatar-liuri.jpg",
 "slides": [
  "Antes de pagar logotipo, cartão de visita e uniforme bordado, pesquise o nome do seu negócio no Google. Se não aparecer nada, você começou pelo lado errado.",
  "Eu pesquiso no celular quase todo negócio que me chama para ajudar. Muitos têm logotipo bonito e nenhum endereço no mapa, nenhum horário e nenhum WhatsApp que abra a conversa com um toque.",
  "A cliente nova nunca vê o seu cartão de visita. Ela vê o que aparece quando digita \"manicure em Odivelas\" ou \"massagem perto de mim\" às dez da noite.",
  "Logotipo e identidade visual têm a hora certa. Essa hora chega depois que a cliente consegue encontrar você, entender o que você faz e marcar sem perguntar três vezes.",
  "Quem está começando com pouco dinheiro precisa de quatro coisas: ficha no Google, WhatsApp Business com respostas prontas, uma página simples com serviço e zona e um perfil que diga como marcar.",
  "Nada disso custa caro. Custa uma tarde e um pouco de ordem. Só que ninguém mostra a ficha do Google aos amigos com orgulho, e o cartão de visita todo mundo mostra.",
  "Isto vai incomodar quem vende identidade visual para negócio que ainda não tem cliente. Design é importante, mas a reserva do primeiro mês precisa ir antes para aquilo que traz a primeira marcação.",
  "Faça o teste agora: pegue o celular, desligue o Wi-Fi e pesquise o seu serviço com o nome do seu bairro. Conte quantos concorrentes aparecem antes de você.",
  "Comente a posição em que o seu negócio apareceu nessa pesquisa.\n\nSiga @liurialves: ainda hoje eu mostro como o WhatsApp Business pode responder a cliente enquanto você atende.",
 ]}

# 14:20 INOVADOR (quarta-feira) — fotofrase
foto = {"formato": "fotofrase", "slides": [
  {"foto": F("1xT6k04o7jm6UZ3zK9xTxzoPxB8CHf0Ht"), "foco_y": 0.35, "texto": "A cliente que manda mensagem às 23h **marca com quem responde primeiro.** O seu WhatsApp Business pode responder por você."},
  {"foto": PX(8036752), "texto": "Abra o WhatsApp Business, entre nas ferramentas comerciais e ative a **mensagem de ausência fora do horário.**"},
  {"foto": PX(950737), "texto": "Escreva nela o que a cliente quer saber: **o serviço, o preço de partida, a zona e a hora em que você responde amanhã.**"},
  {"foto": PX(7804600), "texto": "Ative também a **mensagem de saudação** para quem fala com você pela primeira vez, com as perguntas que você sempre faz."},
  {"foto": PX(7534097), "texto": "Crie **respostas rápidas** para preço, endereço e forma de pagamento. Você digita uma barra e a resposta já aparece escrita."},
  {"foto": PX(4677852), "texto": "Monte o **catálogo** com cada serviço, uma foto real e o valor. A cliente escolhe antes mesmo de perguntar."},
  {"foto": PX(2881253), "texto": "Use **etiquetas** para separar quem perguntou, quem marcou e quem sumiu. Na sexta-feira, **retome quem sumiu.**"},
  {"foto": PX(6628614), "texto": "Uma tarde de configuração e o WhatsApp **passa a trabalhar nas horas em que você está com cliente.**"},
  {"foto": F("1oZgJKGAs1bwyjH_AAxuMNVI6bjqblMWL"), "foco_y": 0.35, "texto": "Configure hoje e **comente PRONTO quando terminar.** Siga @liurialves para o próximo."},
]}

# 17:40 VENDA — capa A (cena em 1ª pessoa; dia par) + fatias escuras. Oferta: kit digital.
venda = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": F("1-rwjYk1j1vC2M3zomrjj3S9KN99Jk4_c"), "foco_y": 0.05, "etiqueta": "Oferta",
   "titulo": "Eu pesquiso o seu negócio no celular, como uma cliente faria, e monto [[o básico que está faltando]].",
   "sub": "Kit digital para pequenas empresas que estão começando: estética, massagem, beleza e serviços locais."},
  {"etiqueta": "Para quem é", "frase": "Para quem abriu o negócio há pouco e [[ainda não aparece]] quando a cliente pesquisa.",
   "texto": "Você tem serviço definido, pouco orçamento para agência e quer começar pela parte que traz a primeira marcação. A seguir está o que o kit organiza, na ordem em que eu trabalho."},
  {"etiqueta": "Etapa 1 · Diagnóstico", "frase": "Primeiro eu procuro você [[como uma cliente procuraria]].",
   "texto": "Google, mapa, Instagram e WhatsApp, no celular e com o nome do seu bairro. Você recebe a lista do que já existe, do que está errado e do que falta."},
  {"etiqueta": "Etapa 2 · Google", "frase": "Ficha no Google com [[serviço, zona, horário e fotos reais]].",
   "texto": "É o que aparece para quem pesquisa o seu serviço perto de casa. Também fica pronto o link para pedir avaliação depois de cada atendimento."},
  {"etiqueta": "Etapa 3 · WhatsApp", "frase": "WhatsApp Business configurado para [[responder enquanto você atende]].",
   "texto": "Mensagem de saudação, mensagem de ausência, respostas rápidas para preço e endereço e o catálogo com os seus serviços."},
  {"etiqueta": "Etapa 4 · Página", "frase": "Uma página simples que leva [[direto para o WhatsApp]].",
   "texto": "Serviço, zona, fotos reais e o botão com a mensagem já escrita. A página abre rápido no celular, mesmo no 4G."},
  {"etiqueta": "Etapa 5 · Perfil", "frase": "Bio e destaques que dizem [[o que você faz e como marcar]].",
   "texto": "A primeira linha com serviço e bairro, o link certo e os destaques de preço, local e marcação. O que entra exatamente no seu kit eu confirmo no diagnóstico, conforme o que você já tem."},
  {"etiqueta": "Para quem não é", "frase": "Isto não é para quem precisa de [[anúncio e gestão todo mês]].",
   "texto": "O kit monta a base. Se você já tem tudo isso e precisa de cliente novo toda semana, o caminho é estratégia e tráfego pago, e eu digo isso no diagnóstico. Eu não prometo número de clientes, porque isso depende do serviço, do preço e da zona."},
  {"etiqueta": "Primeiro passo", "frase": "Diagnóstico grátis, feito por mim, numa [[conversa direta]].",
   "texto": "Clique no link da bio e me chame no WhatsApp com a palavra KIT."},
]}


# ---------------- @spatherapieslisbon ----------------
def spa(hook, hl, slides, imgs):
    return {"hook": hook, "hook_hl": hl, "accent": "#C9A486", "logo_png": LOGO_SPA, "logo_mode": "original",
            "slides": slides, "images": imgs}


def sl(*pars):
    *a, soco = pars
    return "\n\n".join(list(a) + [HL(soco)])


spa1 = spa("Mudaste de casa no fim de semana, subiste caixas ao terceiro andar sem elevador em Arroios e hoje nem consegues calçar as meias",
  "nem consegues calçar as meias", [
  sl("Sábado de manhã começas a subir caixas de livros, a máquina de lavar com a ajuda de um amigo e o colchão pela escada estreita de um prédio antigo em Arroios.", "No domingo à noite ainda estás a montar a cama.", "Na segunda-feira, a lombar avisa que contou cada degrau."),
  sl("Numa mudança pegas em peso de forma torta dezenas de vezes: a caixa encostada à barriga, o tronco rodado no patamar, os braços esticados para passar o sofá pela porta.", "Os músculos das costas seguram tudo isso sem aquecimento e sem pausa.", "Por isso a dor costuma aparecer no dia seguinte."),
  sl("Depois vem o resto da semana. Dormes num colchão ainda no chão, passas horas agachado a arrumar armários e continuas a descer sacos para o lixo.", "A lombar não tem um dia de descanso desde sábado.", "E tu andas meio de lado, à espera que passe sozinho."),
  sl("Há coisas simples para os próximos dias. Dobra os joelhos sempre que pegares numa caixa, leva as mais pesadas a dois e faz uma pausa a cada hora de arrumação.", "Se a dor for forte, aguda ou descer para a perna, fala primeiro com um médico.", "O resto das caixas pode esperar pela próxima semana."),
  sl("Quando é só tensão muscular, uma massagem terapêutica ajuda a soltar a lombar, os glúteos e a parte de trás das coxas, que também trabalharam em cada degrau.", "O terapeuta pergunta o que fizeste e ajusta a pressão ao que sentes na marquesa.", "Contas que foi a mudança e ele sabe por onde começar."),
  sl("Com a casa ainda cheia de caixas, sair para um espaço parece mais uma tarefa na lista.", "Há terapeutas que vão ao domicílio com a marquesa e a montam no meio da sala nova, entre os caixotes ainda por abrir.", "Estreias a casa nova deitado, sem pegar em peso nenhum."),
  sl("O erro mais comum é esperar que a dor desapareça sozinha enquanto continuas a carregar, a agachar e a dormir mal.", "Passam duas semanas e a lombar continua presa de manhã.", "Marca enquanto a tensão é recente, antes de a mudança te ficar nas costas o mês inteiro."),
  sl("Conheces alguém que mudou de casa este mês? Envia-lhe este post antes de ele subir a próxima caixa.", "Se foste tu, marca a tua massagem pelo link na bio e escolhe um terapeuta perto da casa nova ou ao domicílio.", "A casa já está montada. Agora trata das tuas costas."),
], {"cover": f"{S}/A-12-r.jpg", "2": F("1pQFtt3YF92Q5QZZGDUt-ADVvU_8q3Rvk"), "3": SF("02-linho"), "4": SF("06-vela"),
    "5": f"{S}/B-16-c.jpg", "6": F("1fmeXMbDDBUlcJUUDMBWNc70xlC2zW2T2"), "7": SF("04-ripado"), "8": SF("01-luz-quente"),
    "9": F("1Xv0A7goYJeokBaB28wf43TwIlLOkCiom")})

spa2 = spa("Reflexologia em Lisboa: uma hora em que o terapeuta só toca nos teus pés e sais mais leve do que entraste",
  "só toca nos teus pés", [
  sl("Muita gente ouve falar de reflexologia e imagina cinco minutos de massagem aos pés no fim de outra massagem.", "Numa sessão de reflexologia, os pés são o centro do trabalho durante quase toda a hora.", "O terapeuta usa os polegares em pontos da planta, dos dedos e do calcanhar."),
  sl("Tiras os sapatos e as meias e deitas-te de costas na marquesa, ou ficas recostado numa cadeira, com uma toalha por baixo das pernas.", "Não precisas de tirar mais roupa nenhuma.", "Para quem nunca fez massagem e tem vergonha de se despir, é uma boa forma de começar."),
  sl("A pressão é firme, feita com a ponta dos dedos, e há pontos onde sentes mais sensibilidade do que noutros.", "Se incomodar, dizes ao terapeuta e ele ajusta na hora. A sessão é tua e o ritmo também.", "Ninguém tem de aguentar dor calado na marquesa."),
  sl("Quem passa o dia de pé numa loja do Chiado, atrás de um balcão ou a correr entre mesas num restaurante da Baixa chega à noite com os pés pesados.", "Muitos procuram a reflexologia por isso, para uma hora de descanso dedicada aos pés.", "Os pés aguentam o teu dia inteiro e quase nunca recebem atenção."),
  sl("Vais encontrar quem diga que a reflexologia trata doenças através dos pés. Não há base para prometer isso, e um bom terapeuta não o promete.", "O que podes esperar é uma hora de pressão nos pés, relaxamento e tempo longe do ecrã.", "Se tens um problema de saúde, a consulta é com o médico."),
  sl("É comum ficares sonolento a meio da sessão, sobretudo quando marcas ao fim do dia.", "Se puderes, marca para depois do trabalho e não deixes nada importante para essa noite, nem o ginásio nem o supermercado.", "Sais da marquesa com vontade de ir direto para casa."),
  sl("Em lisboamassagem.pt procuras por categoria, escolhes reflexologia, vês a zona de cada terapeuta e falas diretamente por WhatsApp.", "Há terapeutas que vão ao domicílio, o que dá jeito a quem chega a casa sem vontade de voltar a sair.", "Escolhes perto de casa e combinas o horário numa mensagem."),
  sl("Se passas o dia de pé, ou se nunca fizeste massagem e queres começar por algo simples, experimenta uma sessão de reflexologia.", "Guarda este post e envia-o a quem chega a casa e tira os sapatos logo à porta.", "Marca a tua sessão pelo link na bio."),
], {"cover": F("1trcnSD0hNoc4Rckj_iPh8MR9LXSoOspq"), "2": F("15jHyDN2OGtdgpaC2XEsCX6B3Ay3PoR_V"), "3": SF("03-ondas"), "4": f"{S}/B-21-c.jpg",
    "5": F("1QSmcSmlkR9ZZ4bYiCzxG97cDp-TBotEh"), "6": SF("05-oliva"), "7": F("1e7aoT-5HwNMwOR6cJZNh5Bmakh5xkeAU"), "8": SS("02-busca"),
    "9": F("1huK-Phz3jFOV8rQ6Y4UGJwch5sw0Ewfh")})

spa3 = spa("Terapeuta, em novembro começam a procurar massagens para oferecer no Natal e o teu perfil não diz se fazes vales-oferta",
  "não diz se fazes vales-oferta", [
  sl("A partir de novembro, muita gente em Lisboa começa a pensar no presente da mãe, do companheiro ou do amigo secreto do escritório.", "Uma massagem entra na lista de quem já não sabe o que oferecer.", "Essa pessoa pesquisa e escolhe quem deixa claro que faz vales."),
  sl("Quem procura um presente quer resolver depressa: o preço, como recebe o vale, até quando pode ser usado e onde fica o espaço.", "Se o teu perfil só mostra fotos da marquesa, essa pessoa tem de te mandar mensagem a perguntar tudo.", "Muitas não perguntam e compram a outro terapeuta."),
  sl("Podes preparar o teu vale hoje. Escolhe uma ou duas massagens para oferecer, define o preço e um prazo de validade, por exemplo três meses.", "Faz um cartão simples, em papel ou em PDF, com o teu nome, o contacto e um código para cada vale.", "Simples chega, desde que esteja pronto antes de te pedirem."),
  sl("Depois diz isso em todo o lado: uma linha na bio, um destaque com o preço e as regras do vale e uma resposta pronta no WhatsApp para quando alguém perguntar.", "Quem compra um presente às onze da noite não espera pela tua resposta de manhã.", "Cada pergunta já respondida é uma venda que não se perde."),
  sl("Pensa também em quem recebe. A pessoa que ganha o vale vai procurar-te pela primeira vez, muitas vezes em janeiro, e precisa de saber onde atendes e como marca.", "Cada vale vendido traz alguém que ainda não te conhecia.", "É a altura do ano em que um cliente paga para te apresentar a outro."),
  sl("Para isso, o teu nome tem de aparecer a quem procura massagem na tua zona. Em lisboamassagem.pt, a busca é feita por distrito, categoria ou nome.", "O teu perfil mostra a zona, os tipos de massagem e o contacto direto por WhatsApp.", "Quem te encontra fala contigo sem intermediários."),
  sl("O registo e o anúncio na plataforma são grátis. Crias o perfil, escolhes as categorias, indicas a zona e dizes se vais ao domicílio.", "Quem quiser aparecer mais acima na busca tem o plano Elite, com destaque nos resultados.", "Deixa isto feito antes de começar a corrida aos presentes."),
  sl("Se és terapeuta, prepara o teu vale esta semana e anuncia-te grátis em lisboamassagem.pt. Começa pelo vale da massagem que mais fazes, põe o preço na bio e deixa a resposta pronta no WhatsApp.", "Conheces um colega que ainda não pensou no Natal? Envia-lhe este post.", "Em dezembro já é tarde para começar a preparar."),
], {"cover": F("1o1yvvbcuIg6K7r20rkXWLqwXJqQ411m2"), "2": F("1Hq8h2rFVGh6unveQSmvbTFmZZNkeAOBq"), "3": SF("01-luz-quente"), "4": SF("04-ripado"),
    "5": SF("02-linho"), "6": f"{S}/A-24-r.jpg", "7": SS("04-terapeutas"), "8": SF("06-vela"),
    "9": F("1fmeXMbDDBUlcJUUDMBWNc70xlC2zW2T2")})


def palavras(t):
    return len(re.sub(r"<[^>]+>", "", t).split())


if __name__ == "__main__":
    for c in (spa1, spa2, spa3):
        for i, s in enumerate(c["slides"], 2):
            n = palavras(s)
            if not 40 <= n <= 80:
                print("AVISO palavras", c["hook"][:30], i, n)
    retrato(FR("A-12"), f"{S}/A-12-r.jpg", cx=0.45)
    retrato(FR("A-24"), f"{S}/A-24-r.jpg", cx=0.45)
    corta_topo(FR("B-16"), f"{S}/B-16-c.jpg")
    corta_topo(FR("B-21"), f"{S}/B-21-c.jpg")
    sel = sys.argv[1:] or ["l1", "l2", "l3", "s1", "s2", "s3"]
    O = lambda p, n: f"{R}/posts/{DIA}/{p}-{n}"
    if "l1" in sel: run("render_formatos.py", dict(tweet, slides=[{"texto": t} for t in tweet["slides"]]), O("liurialves", 1))
    if "l2" in sel: run("render_formatos.py", foto, O("liurialves", 2))
    if "l3" in sel: run("render_formatos.py", venda, O("liurialves", 3))
    if "s1" in sel: run("render_carrossel.py", spa1, O("spatherapieslisbon", 1))
    if "s2" in sel: run("render_carrossel.py", spa2, O("spatherapieslisbon", 2))
    if "s3" in sel: run("render_carrossel.py", spa3, O("spatherapieslisbon", 3))
    print("ok")
