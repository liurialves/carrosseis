import json, os, subprocess, sys
from PIL import Image
S = "/tmp/claude-0/-home-claude-carrosseis/31af8ca0-beea-584d-b999-81ad2499e244/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-10-27"
F = lambda x: f"{S}/fotos/{x}.jpg"
FR = lambda x: f"{S}/frames/{x}.jpg"
PR = lambda x: f"{S}/prints/{x}.jpg"
PX = lambda x: f"{S}/pexels/pexels-{x}.jpg"
SF = lambda x: f"{R}/assets/spa-fundos/{x}.jpg"
SS = lambda x: f"{R}/assets/spa-site/{x}.jpg"
HL = lambda t: f"<span class='hl'>{t}</span>"
LOGO_SPA = f"{R}/assets/logos/lisboa-massagem.png"


def corta_topo(src, dst, frac=0.16):
    im = Image.open(src); w, h = im.size
    im.crop((0, int(h * frac), w, h)).save(dst, quality=92)
    return dst


def retrato(src, dst, cx=0.5):
    """recorta frame horizontal para 4:5 centrado em cx"""
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
polemica = {"formato": "branco", "slides": [
  {"etiqueta": "Opinião", "frase": "Em dez anos de massagem em Lisboa, eu vi muita agenda cair no mês em que [[uma cliente fixa mudou de cidade]].",
   "texto": "Quem vive só de indicação está dependendo da agenda e da memória de outras pessoas para pagar as próprias contas."},
  {"etiqueta": "A tese", "frase": "Depender de indicação é deixar [[o seu faturamento na mão de outra pessoa]].",
   "texto": "A cliente que indica decide quando fala de você, para quem fala e com que palavras. Você só fica sabendo quando o WhatsApp toca, ou quando ele para de tocar."},
  {"frase": "Quem vive de indicação costuma chamar o mês fraco de [[azar]].",
   "texto": "Eu chamo de falta de processo. Se você não sabe de onde veio a cliente da semana passada, também não sabe como trazer a da semana que vem."},
  {"frase": "Atender melhor [[não aumenta]] o número de indicações no mesmo ritmo.",
   "texto": "Você pode chegar mais cedo e caprichar no acabamento. A cliente satisfeita continua indicando quando lembra, e só para quem pergunta a ela."},
  {"frase": "Quem tem agenda previsível sabe [[de onde vem cada cliente]].",
   "texto": "Perfil que diz o serviço e a zona, ficha no Google com avaliações, post que responde dúvida real e, quando faz sentido, anúncio para o bairro. Cada canal com um número que você confere toda segunda-feira."},
  {"frase": "Isto vai incomodar quem acredita que [[o bom trabalho se vende sozinho]].",
   "texto": "Ele se vende para quem já conhece você. A pessoa que mora a dois quarteirões e nunca ouviu o seu nome precisa de outro caminho até a sua porta."},
  {"frase": "Indicação deve ser [[o bônus]] do seu mês.",
   "texto": "Quando o resto do processo funciona, a cliente indicada chega por cima do planejado. Quando ela é a única fonte, qualquer mudança na vida de uma cliente fixa vira problema no seu caixa."},
  {"frase": "Faça a conta hoje: quantas clientes do último mês [[chegaram por indicação]]?",
   "texto": "Abra a agenda e anote ao lado de cada nome como ela chegou até você. Se quase todas vieram de indicação, o seu negócio depende de poucas pessoas lembrarem de você."},
  {"frase": "Comente a [[porcentagem]] da sua agenda que vem de indicação.",
   "texto": "Siga @liurialves: ainda hoje eu mostro três ajustes para a cliente nova chegar até você sem depender de ninguém lembrar do seu nome."},
]}

intencional = {"formato": "branco", "slides": [
  {"etiqueta": "Hoje", "frase": "Faça estes [[3 ajustes]] hoje para a próxima cliente chegar até você sem indicação.",
   "texto": "Nenhum deles custa dinheiro, e os três cabem numa tarde."},
  {"etiqueta": "Ajuste 1", "frase": "Crie ou revise o seu [[Perfil de Empresa no Google]].",
   "texto": "Nome, serviço principal, bairro, horário, telefone e fotos reais do espaço. É ali que aparece quem pesquisa \"massagem perto de mim\" ou \"limpeza de pele em Alvalade\"."},
  {"frase": "A cliente que não conhece ninguém para indicar você [[começa pela busca]].",
   "texto": "Ela acabou de se mudar, trabalha longe de casa ou quer resolver hoje. Se o seu nome não aparece no mapa, ela marca com quem aparece."},
  {"etiqueta": "Ajuste 2", "frase": "Peça [[avaliação no Google]] às cinco últimas clientes satisfeitas.",
   "texto": "Mande a mensagem hoje, com o link direto para avaliar, e peça que escrevam o serviço que fizeram. Quem lê uma avaliação quer saber exatamente o que você fez."},
  {"frase": "Uma avaliação pública trabalha para você [[com gente que nunca ouviu o seu nome]].",
   "texto": "É uma indicação que fica escrita, visível para qualquer pessoa que esteja comparando você com o concorrente da rua ao lado."},
  {"etiqueta": "Ajuste 3", "frase": "Responda [[todas as avaliações]], inclusive as antigas.",
   "texto": "Agradeça pelo nome e cite o serviço. Quem chega pela busca lê as respostas e percebe como você trata quem já atendeu."},
  {"frase": "Quem pesquisa compara você com [[três ou quatro nomes]] na mesma tela.",
   "texto": "Fotos reais, avaliações recentes e respostas educadas decidem a escolha antes de qualquer conversa sobre preço."},
  {"frase": "Três ajustes, uma tarde. [[Comece agora]] pelo primeiro.",
   "texto": "Depois pesquise o seu serviço e o seu bairro no celular, como uma cliente faria, e veja em que posição o seu nome aparece."},
  {"frase": "Comente [[FEITO]] quando terminar os três ajustes.",
   "texto": "Se quiser que eu confira a sua ficha no Google e o seu perfil, clique no link da bio e me chame no WhatsApp com a palavra GOOGLE."},
]}

venda = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": FR("L-44"), "foco_y": 0.6, "etiqueta": "Oferta",
   "titulo": "Eu treino você para trazer [[cliente que não depende de indicação]].",
   "sub": "Treinamento de marketing para clínicas de estética, estúdios de massagem, salões e serviços locais."},
  {"etiqueta": "Para quem é", "frase": "Para quem atende bem, tem cliente satisfeita e ainda [[espera o WhatsApp tocar]].",
   "texto": "Você já tem serviço definido e preço, mas a agenda sobe e desce conforme as indicações do mês. A seguir está o que você aprende, na ordem em que eu ensino."},
  {"etiqueta": "Etapa 1 · Diagnóstico", "frase": "Antes de ensinar, eu descubro [[de onde vêm as suas clientes]] hoje.",
   "texto": "Olhamos juntos a agenda dos últimos meses, o seu perfil, a sua ficha no Google e as conversas do WhatsApp. Você sai sabendo qual canal funciona e qual está parado."},
  {"etiqueta": "Etapa 2 · Presença", "frase": "Perfil e Google [[prontos para quem não conhece você]].",
   "texto": "Bio com serviço e zona, destaques que respondem preço, local e como marcar, ficha no Google com fotos reais e um jeito simples de pedir avaliação depois de cada atendimento."},
  {"etiqueta": "Etapa 3 · Conteúdo", "frase": "Posts com [[função]], tirados das dúvidas reais das suas clientes.",
   "texto": "Você aprende a montar a semana com posts que atraem, ensinam e vendem, e a terminar cada um com a ação que a pessoa deve fazer. O ritmo continua sem depender de agência."},
  {"etiqueta": "Etapa 4 · WhatsApp", "frase": "A conversa que [[vira marcação]].",
   "texto": "Mensagem de boas-vindas, resposta para \"quanto custa?\" que não espanta a cliente e o retorno para quem perguntou e sumiu. É no WhatsApp que muita venda se perde por falta de resposta certa."},
  {"etiqueta": "Etapa 5 · Números", "frase": "Toda semana, [[três números]] guiam a sua decisão.",
   "texto": "Quantas conversas chegaram, de qual canal vieram e quantas viraram marcação. Com isso você sabe onde colocar o seu tempo e, quando fizer sentido, a verba de anúncio."},
  {"etiqueta": "Para quem não é", "frase": "Isto não é para quem procura [[resultado sem fazer a sua parte]].",
   "texto": "O treinamento ensina processo, e quem aplica é você. Eu não prometo número de clientes, porque isso depende do serviço, do preço e da zona. Se você ainda não definiu o serviço principal, começamos por aí."},
  {"etiqueta": "Primeiro passo", "frase": "Diagnóstico grátis, feito por mim, numa [[conversa direta]].",
   "texto": "Clique no link da bio e me chame no WhatsApp com a palavra TREINAMENTO."},
]}

# ---------------- @spatherapieslisbon ----------------
def spa(hook, hl, slides, imgs):
    return {"hook": hook, "hook_hl": hl, "accent": "#C9A486", "logo_png": LOGO_SPA, "logo_mode": "original",
            "slides": slides, "images": imgs}

def sl(*pars):
    *a, soco = pars
    return "\n\n".join(list(a) + [HL(soco)])

spa1 = spa("Envia isto a quem passa o dia no portátil em Alcântara e diz que a dor no pescoço é normal",
  "a dor no pescoço é normal", [
  sl("Às nove da manhã abres o portátil na mesa da cozinha ou num escritório em Alcântara, e às sete da tarde ainda lá estás, com o ecrã um pouco abaixo dos olhos.", "O queixo vai avançando sem dares por isso.", "Ao fim do dia, o pescoço já não volta sozinho ao sítio."),
  sl("Quem se queixa costuma culpar o colchão ou o frio. Só que a tensão aparece sempre no mesmo sítio: na base da nuca e entre as omoplatas, onde os músculos seguram a cabeça inclinada durante horas.", "Chamar a isto normal é só uma forma de adiar."),
  sl("Depois vem o ombro que estala quando o rodas, a tensão que sobe até à cabeça ao fim da tarde e a noite em que não encontras posição na almofada.", "Nada disto chega de um dia para o outro. Vai-se juntando, semana após semana de ecrã.", "O corpo avisa durante meses antes de travar."),
  sl("Antes de marcares seja o que for, há três ajustes que podes fazer hoje no teu posto de trabalho.", "Sobe o portátil com dois ou três livros até o topo do ecrã ficar à altura dos olhos, usa um teclado à parte e levanta-te a cada hora, nem que seja para ir buscar água.", "Assim deixas de juntar tensão nova todos os dias."),
  sl("A tensão que já lá está precisa de mãos. Numa massagem terapêutica, o terapeuta trabalha o trapézio, a nuca e a zona entre as omoplatas com a pressão ajustada ao que sentes na marquesa.", "Dizes se está forte demais e ele adapta.", "É uma hora dedicada à zona que passas o dia a esquecer."),
  sl("Se trabalhas em casa, nem precisas de atravessar Lisboa. Há terapeutas que vão ao domicílio com a marquesa e montam tudo na sala, ao fim do dia, quando fechas o portátil.", "No fim tomas um duche e vais para a cama.", "Sem trânsito entre a massagem e o descanso."),
  sl("O erro mais comum é esperar pela semana em que o pescoço bloqueia de vez. Aí a massagem chega tarde e a primeira sessão vai quase toda para soltar o que se foi acumulando.", "Marcar quando ainda só incomoda poupa o teu corpo."),
  sl("Tu conheces alguém assim: passa o dia ao portátil, roda o pescoço em cada reunião e jura que é normal.", "Envia-lhe este post. Se fores tu, marca a tua massagem pelo link na bio e escolhe um terapeuta perto de casa ou ao domicílio.", "Marca esta semana, antes de o pescoço decidir por ti."),
], {"cover": F("1RL41ouAX1SU8FSA2fm90RaYmNZJ3GsuC"), "2": F("1QSmcSmlkR9ZZ4bYiCzxG97cDp-TBotEh"), "3": f"{S}/F-21-r.jpg",
    "4": SF("06-vela"), "5": F("15jHyDN2OGtdgpaC2XEsCX6B3Ay3PoR_V"), "6": f"{S}/K-10-c.jpg", "7": F("1Xv0A7goYJeokBaB28wf43TwIlLOkCiom"),
    "8": SF("03-ondas"), "9": F("1e7aoT-5HwNMwOR6cJZNh5Bmakh5xkeAU")})

spa2 = spa("Massagem em Lisboa depois do treino: em que dia marcar para não chegares ao jogo dorido",
  "em que dia marcar", [
  sl("Treinas três vezes por semana em Lisboa e ao sábado tens futebol com os amigos ou uma prova de corrida no Parque das Nações.", "Na quinta-feira as pernas estão pesadas e decides marcar uma massagem para o dia seguinte.", "É aqui que muita gente erra o dia."),
  sl("Uma massagem desportiva mais profunda trabalha o músculo cansado com pressão firme. Nos dias seguintes, é comum sentires as pernas sensíveis, como depois de um treino puxado.", "Se isso calhar no dia do jogo, entras em campo com as pernas a pedir descanso."),
  sl("Por isso, muitos terapeutas desportivos separam dois tipos de sessão. A de recuperação, mais intensa, fica longe da competição. A de preparação, mais leve e curta, fica perto do jogo e serve para soltar sem cansar.", "O dia que escolhes muda a massagem que pedes."),
  sl("Na prática, se jogas ao sábado, a sessão mais profunda encaixa no início da semana, logo a seguir ao jogo anterior ou ao treino mais pesado.", "Assim o corpo tem dias de folga para assentar antes de voltares ao campo.", "Recuperas do último jogo sem roubar pernas ao próximo."),
  sl("Na véspera, se sentires necessidade, pede uma massagem leve e curta, focada nas zonas que mais usaste: gémeos, coxas e lombar.", "Diz ao terapeuta que jogas no dia seguinte.", "Ele ajusta a pressão quando sabe para onde vais a seguir."),
  sl("Logo a seguir ao jogo, toma banho, come e dorme. A massagem rende mais no dia seguinte, quando o corpo já arrefeceu e consegues dizer onde dói de facto.", "Na marquesa, sabes explicar o que sentes e o terapeuta vai direto ao sítio."),
  sl("Há um erro que se repete: marcar só quando a coxa já prende e o jogo é amanhã. Aí já não dá para fazer o trabalho profundo e a sessão fica a meio caminho.", "Quem planeia a massagem como planeia o treino chega mais solto ao fim de semana."),
  sl("Se treinas em Lisboa, procura um terapeuta de massagem desportiva perto do teu ginásio ou que vá a casa, e marca já a sessão de segunda-feira.", "Guarda este post para a próxima semana de jogo.", "Marca pelo link na bio e envia isto ao teu colega de equipa."),
], {"cover": F("1oEqMXCqpCRBcLK4Hem2bBPL0A4GVUJKG"), "2": FR("P-13"), "3": f"{S}/F-10-r.jpg", "4": SF("04-ripado"),
    "5": FR("O-16"), "6": f"{S}/K-17-c.jpg", "7": F("1huK-Phz3jFOV8rQ6Y4UGJwch5sw0Ewfh"), "8": SF("05-oliva"),
    "9": F("1o1yvvbcuIg6K7r20rkXWLqwXJqQ411m2")})

spa3 = spa("Terapeuta em Lisboa: o cliente de Benfica procura massagem perto de mim e o teu perfil não diz onde atendes",
  "não diz onde atendes", [
  sl("São nove da noite e alguém em Benfica fecha o portátil com as costas presas. Pega no telemóvel e escreve \"massagem perto de mim\".", "Aparecem nomes, mapas e perfis com zona, preço e WhatsApp.", "O teu não aparece, porque em lado nenhum dizes onde atendes."),
  sl("Muitos terapeutas escrevem na bio \"massagens com amor\" ou \"cuidar de ti\" e deixam de fora o bairro, os tipos de massagem e se vão a casa.", "O cliente que procura às nove da noite não manda mensagem para perguntar.", "Passa ao perfil seguinte, que já lhe respondeu."),
  sl("Quem pesquisa por zona quer resolver depressa. Quer saber se estás perto, se fazes o tipo de massagem que procura e se pode marcar para amanhã.", "Se uma destas respostas falta, a marcação vai para outro terapeuta.", "A zona na bio pesa mais do que a foto mais bonita do teu feed."),
  sl("Hoje mesmo podes mudar três coisas. A primeira é a linha de cima da bio: tipo de massagem e bairro, por exemplo \"Massagem terapêutica e desportiva em Benfica e ao domicílio\".", "Quem lê sabe logo se és a pessoa certa."),
  sl("A segunda é o link. Põe um link direto para o teu WhatsApp, com uma mensagem já escrita a pedir horário.", "Cada passo a mais entre o perfil e a conversa é uma marcação que fica para depois e acaba esquecida.", "Facilita o contacto e o cliente faz o resto."),
  sl("A terceira é estar onde o cliente procura. Em lisboamassagem.pt, a busca é feita por distrito, categoria ou nome, e o teu perfil mostra a zona, os tipos de massagem e o contacto direto por WhatsApp.", "Quem procura em Benfica encontra quem atende em Benfica."),
  sl("O registo e o anúncio na plataforma são grátis. Crias o perfil, escolhes as categorias, indicas a tua zona, dizes se vais ao domicílio e passas pela verificação.", "Quem quiser aparecer mais acima na busca tem ainda o plano Elite, com destaque nos resultados.", "Ficas visível para quem procura massagem na tua zona."),
  sl("Se és terapeuta em Lisboa e o teu perfil ainda não diz onde atendes, corrige a bio hoje e anuncia-te grátis em lisboamassagem.pt.", "Conheces um colega na mesma situação? Envia-lhe isto.", "O cliente de amanhã à noite já está a pesquisar."),
], {"cover": f"{S}/F-26-r.jpg", "2": F("1pQFtt3YF92Q5QZZGDUt-ADVvU_8q3Rvk"), "3": SF("02-linho"), "4": PR("1FY3ED2H_NGKPLdVVVM-737srpBfuJiti"),
    "5": F("1sQpoW-4ihQ9et4DOmxJ1TpPq2MrFKfoi"), "6": FR("K-26"), "7": SS("02-busca"), "8": PR("17o_IysOhBkDnEFUwBPsFRD3nY00IhyHW"),
    "9": SF("01-luz-quente")})

if __name__ == "__main__":
    for n in ("21", "10", "26"):
        retrato(FR(f"F-{n}"), f"{S}/F-{n}-r.jpg", cx=0.42)
    for n in ("10", "17"):
        corta_topo(FR(f"K-{n}"), f"{S}/K-{n}-c.jpg")
    corta_topo(FR("K-26"), FR("K-26"))
    sel = sys.argv[1:] or ["l1", "l2", "l3", "s1", "s2", "s3"]
    O = lambda p, n: f"{R}/posts/{DIA}/{p}-{n}"
    if "l1" in sel: run("render_formatos.py", polemica, O("liurialves", 1))
    if "l2" in sel: run("render_formatos.py", intencional, O("liurialves", 2))
    if "l3" in sel: run("render_formatos.py", venda, O("liurialves", 3))
    if "s1" in sel: run("render_carrossel.py", spa1, O("spatherapieslisbon", 1))
    if "s2" in sel: run("render_carrossel.py", spa2, O("spatherapieslisbon", 2))
    if "s3" in sel: run("render_carrossel.py", spa3, O("spatherapieslisbon", 3))
    print("ok")
