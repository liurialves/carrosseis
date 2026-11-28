import json, os, subprocess, sys, re
from PIL import Image
S = "/tmp/claude-0/-home-claude-carrosseis/d9659ce6-2f34-51c2-9de7-e579d3399dad/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-10-29"
F = lambda x: f"/tmp/fotos/{x}.jpg"
SF = lambda x: f"{R}/assets/spa-fundos/{x}.jpg"
SS = lambda x: f"{R}/assets/spa-site/{x}.jpg"
HL = lambda t: f"<span class='hl'>{t}</span>"
LOGO_SPA = f"{R}/assets/logos/lisboa-massagem.png"
V1 = lambda t: f"/tmp/fotos/v_1Fuv-Eqn2cPIszYIclLVxKVGY3xzXhxmo_{t}.jpg"
V2 = lambda t: f"/tmp/fotos/v_106kkqMJyo37eJ81TWbzD9Amp171csDc8_{t}.jpg"


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
# Tema do dia (frente 3, gestão e dinheiro): baixar o preço sem fazer a conta. Palavra única: CALL.
# 12:10 POLÊMICA (branco; ontem foi tweet)
polemica = {"formato": "branco", "slides": [
  {"etiqueta": "Opinião", "frase": "Quando um dono de negócio me diz que vai baixar o preço para encher a agenda, eu pergunto [[quanto sobra de cada atendimento]].",
   "texto": "Quase sempre a resposta vem com um número redondo e nenhuma conta por trás."},
  {"etiqueta": "A tese", "frase": "Baixar o preço sem saber a margem é [[trabalhar mais para levar o mesmo]] para casa.",
   "texto": "A agenda enche, o caixa não acompanha, e o dono termina o mês mais cansado e com a mesma conta no banco."},
  {"etiqueta": "A conta", "frase": "Um desconto de 20% pode levar [[dois terços do que sobra]].",
   "texto": "Num serviço de 50 euros que deixa 15 depois de produto, aluguel, taxas e impostos, um desconto de 10 euros deixa só 5. Para ganhar o mesmo, você precisa de três atendimentos onde antes fazia um."},
  {"etiqueta": "O que acontece", "frase": "A agenda cheia de desconto [[não deixa espaço]] para o cliente que paga o preço cheio.",
   "texto": "Você atende mais horas, compra mais produto e cansa mais. Quando aparece alguém disposto a pagar o valor normal, o horário já está ocupado por quem veio pela promoção."},
  {"etiqueta": "Depois da promoção", "frase": "Quem marcou por causa do desconto costuma sumir [[quando o desconto acaba]].",
   "texto": "E voltar ao preço antigo fica difícil. Subir 10 euros depois de três meses de promoção exige uma explicação que o cliente não pediu."},
  {"etiqueta": "Onde eu olho primeiro", "frase": "Quando a agenda está vazia, eu confiro [[se o cliente consegue encontrar e falar com você]].",
   "texto": "Perfil que não explica o serviço, WhatsApp que demora a responder e nenhuma prova do trabalho afastam mais gente do que o valor da tabela."},
  {"etiqueta": "O que eu faço antes", "frase": "Antes de mexer no preço, eu monto [[a conta de um atendimento]].",
   "texto": "Quanto entra, quanto sai em produto, tempo, aluguel e taxas, e quanto sobra. Com esse número na mão, baixar, manter ou subir o preço deixa de ser chute."},
  {"etiqueta": "Quando faz sentido", "frase": "Desconto com [[data para acabar]] e com a conta feita pode funcionar.",
   "texto": "Por exemplo, para preencher as terças de manhã que ficam sempre vazias. Desconto permanente para competir com o mais barato da rua tira o seu lucro todo mês, sem ninguém perceber."},
  {"etiqueta": "Sua vez", "frase": "Comente [[1]] se você já baixou o preço e o mês não melhorou. Comente [[2]] se nunca precisou.",
   "texto": "Siga @liurialves: hoje às 14h20 eu mostro, no quadro, a conta que eu faço antes de mexer em qualquer preço."},
]}

# 14:20 QUADRO / EDUCATIVO (quinta-feira). Capa com círculos (o extra de hoje usa funil).
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "A conta de [[3 números]] que eu faço antes de mexer no preço",
   "desenho": {"tipo": "circulos", "rotulos": ["entra", "sai", "sobra"], "centro": "MARGEM"},
   "texto": "Serve para salão, restaurante, loja ou consultório. Basta papel e os números do último mês."},
  {"etiqueta": "Número 1 de 3", "titulo": "Quanto entra", "desenho": {"tipo": "numero", "n": 1, "nota": "por atendimento, não por mês"},
   "texto": "Pegue o serviço que você mais vende e anote o valor que realmente cai na conta, já sem a taxa do cartão e a comissão da plataforma de marcação.",
   "soco": "O preço da tabela raramente é o que entra."},
  {"etiqueta": "Número 2 de 3", "titulo": "Quanto sai", "desenho": {"tipo": "numero", "n": 2, "nota": "o que quase todo mundo esquece"},
   "texto": "Produto usado, a sua hora ou a do funcionário e a parte do aluguel, da luz, do contador e do software que cabe em cada atendimento. Divida as contas fixas do mês pelo número de atendimentos.",
   "soco": "Conta fixa dividida também é custo."},
  {"etiqueta": "Número 3 de 3", "titulo": "Quanto sobra", "desenho": {"tipo": "numero", "n": 3, "nota": "esse é o seu número"},
   "texto": "O que entra menos o que sai é a margem de cada atendimento. É com ela que você paga o seu salário, guarda caixa e investe em anúncio.",
   "soco": "Sem esse número, qualquer preço é palpite."},
  {"etiqueta": "Bônus", "titulo": "Quantos atendimentos pagam o seu mês", "desenho": {"tipo": "numero", "n": "÷", "nota": "contas fixas ÷ margem"},
   "texto": "Divida as contas fixas do mês pela margem de cada atendimento. O resultado é quantos atendimentos você precisa só para empatar. O que vier depois disso é lucro.",
   "soco": "Esse número muda a forma como você olha para a agenda."},
  {"etiqueta": "Exemplo", "titulo": "Um atendimento de 50 euros", "desenho": {"tipo": "lista", "itens": ["entra: 50 euros", "sai: 35 euros", "sobra: 15 euros", "-10 €: sobra 5 euros"]},
   "texto": "Com um desconto de 10 euros, você precisa de três atendimentos para ganhar o que ganhava com um. Os números são de exemplo: faça a conta com os seus."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3"], "nota": "copiar o preço do vizinho"},
   "texto": "O dono copia o preço do concorrente, ou baixa o valor porque a agenda ficou fraca numa semana, sem olhar o número 2. A conta do concorrente tem outro aluguel, outro produto e outra equipe.",
   "soco": "O preço do vizinho foi feito com os custos dele."},
  {"etiqueta": "Na prática", "titulo": "Faça a conta hoje", "desenho": {"tipo": "lista", "check": True, "itens": ["1: escolha o serviço", "2: anote o que entra", "3: some o que sai", "4: veja o que sobra", "5: decida o preço"]},
   "texto": "Faça para os três serviços que você mais vende. Às vezes o mais procurado é o que menos deixa dinheiro."},
  {"etiqueta": "Próximo passo", "titulo": "Salve e faça a sua conta", "desenho": {"tipo": "circulos", "rotulos": ["preço", "custo", "meta"], "centro": "CAIXA"},
   "texto": "Se quiser fazer essa conta comigo e montar o plano de preço, caixa e metas do seu negócio, mande CALL no direct. A primeira conversa é um diagnóstico gratuito de 30 minutos.",
   "soco": "Salve este post e faça a conta ainda hoje."},
]}

# 17:40 VENDA (dia ímpar: capa B, tese sem cena) + fatias escuras. Oferta: mentoria de crescimento.
venda = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": F("1sQpoW-4ihQ9et4DOmxJ1TpPq2MrFKfoi"), "foco_y": 0.15, "etiqueta": "Mentoria",
   "titulo": "Negócio que fatura e não sobra dinheiro [[precisa da conta feita]] antes de precisar de mais cliente.",
   "sub": "Mentoria de crescimento para donos de pequena e média empresa: preço, margem, caixa e metas, com estratégia e conteúdo."},
  {"etiqueta": "Para quem é", "frase": "Para o dono que [[trabalha muito, vende bem]] e no fim do mês não sabe para onde foi o dinheiro.",
   "texto": "Salão, restaurante, loja, prestador de serviço ou profissional liberal, no Brasil ou em Portugal. Você já tem cliente e quer crescer sem trabalhar ainda mais horas."},
  {"etiqueta": "Etapa 1 · Diagnóstico", "frase": "Primeiro eu olho [[os números que você já tem]].",
   "texto": "Preço de cada serviço, custo, margem, contas fixas e o que entrou nos últimos meses. Você sai da conversa sabendo qual serviço dá dinheiro e qual só ocupa a agenda."},
  {"etiqueta": "Etapa 2 · Preço", "frase": "Depois revemos o preço [[serviço por serviço]].",
   "texto": "O que manter, o que subir, o que deixar de oferecer e quando um desconto vale a pena, sempre com a conta do atendimento na mão."},
  {"etiqueta": "Etapa 3 · Caixa", "frase": "Organizamos o caixa para [[o mês fraco não virar crise]].",
   "texto": "Separar o dinheiro da empresa do seu, definir o seu salário e criar a reserva para os meses mais fracos. É a parte menos bonita do trabalho e a que deixa o dono dormir tranquilo."},
  {"etiqueta": "Etapa 4 · Metas", "frase": "A meta do mês sai do [[valor que precisa sobrar]].",
   "texto": "Com a margem de cada serviço, a meta vira um número de atendimentos por semana que você e a sua equipe conseguem acompanhar."},
  {"etiqueta": "Etapa 5 · Crescimento", "frase": "Só então entram [[estratégia, funil e conteúdo]] para trazer o cliente certo.",
   "texto": "Com a conta feita, você sabe quanto pode pagar por cada cliente novo. Site e tráfego pago entram como serviço complementar quando o diagnóstico mostrar que é o caso."},
  {"etiqueta": "Para quem não é", "frase": "Isto não é para quem [[ainda não tem um serviço definido]].",
   "texto": "Também não é para quem procura promessa de faturamento. Eu não prometo número, porque o resultado depende do seu mercado, do seu preço e da sua execução."},
  {"etiqueta": "Primeiro passo", "frase": "Uma call de diagnóstico [[gratuita de 30 minutos]], feita por mim.",
   "texto": "Mande CALL no direct e eu envio o link para marcar. Alguns negócios que eu já atendi, como a Carolwell e a empresa de limpeza LB, estão no meu site."},
]}


# ---------------- @spatherapieslisbon ----------------
def spa(hook, hl, slides, imgs):
    return {"hook": hook, "hook_hl": hl, "accent": "#C9A486", "logo_png": LOGO_SPA, "logo_mode": "original",
            "slides": slides, "images": imgs}


def sl(*pars):
    *a, soco = pars
    return "\n\n".join(list(a) + [HL(soco)])


spa1 = spa("Fazes a IC19 todos os dias de Sintra para Lisboa e, quando sais do carro no parque do escritório, a lombar já vai dorida",
  "a lombar já vai dorida", [
  sl("O despertador toca às 6h40, o café é bebido em pé e às 7h15 já estás na fila da IC19, com o banco do carro demasiado reclinado e o telemóvel no suporte.", "São quarenta minutos parado, a avançar aos solavancos até à saída de Lisboa.", "A lombar faz a viagem toda contigo, sem pausa."),
  sl("Ao volante ficas na mesma posição durante muito tempo: a anca dobrada, o pé direito sempre no pedal e os ombros a subir sempre que alguém se mete à tua frente na faixa.", "Os músculos da lombar e dos glúteos seguram essa postura do primeiro ao último quilómetro.", "À noite, sair do carro já custa."),
  sl("Depois da viagem vêm oito horas sentado ao computador, com o almoço comido à secretária. Ao fim do dia, mais quarenta minutos de regresso pelo mesmo caminho.", "Num dia normal de trabalho passas quase dez horas sentado.", "O corpo passa o dia inteiro dobrado na mesma posição."),
  sl("Há ajustes simples que podes fazer no carro amanhã. Endireita o encosto, aproxima o banco para os joelhos ficarem ligeiramente dobrados e põe um casaco enrolado atrás da zona lombar.", "Nas filas longas, mexe os ombros e encosta as costas por completo ao banco.", "Ao fim de uma semana, a lombar nota a diferença."),
  sl("Se a dor desce para a perna, se sentes formigueiro ou se piora de dia para dia, fala primeiro com um médico antes de marcares qualquer massagem.", "Quando é tensão muscular de quem passa o dia sentado, entre o carro e a secretária, a massagem ajuda a soltar o que ficou preso.", "Na dúvida, começa sempre pelo médico."),
  sl("Numa massagem terapêutica, o terapeuta trabalha a lombar, os glúteos, a parte de trás das coxas e os ombros que passaram a viagem tensos.", "Contas que conduzes todos os dias e ele ajusta a pressão ao que sentes na marquesa.", "Sais com as costas mais soltas para a viagem do dia seguinte."),
  sl("Muita gente só marca quando já não consegue virar a cabeça para fazer marcha-atrás no parque.", "Se fazes a mesma viagem todos os dias, marca a massagem para um fim de tarde em que não precisas de conduzir a seguir, ou escolhe um terapeuta que vá ao domicílio.", "Assim a hora de descanso não acaba noutra fila de trânsito."),
  sl("Conheces alguém que passa a manhã na IC19 ou na A5 e se queixa das costas logo ao almoço? Envia-lhe este post.", "Se és tu, marca a tua massagem pelo link na bio e escolhe um terapeuta perto de casa ou do trabalho.", "As tuas costas também precisam de chegar inteiras ao fim da semana."),
], {"cover": f"{S}/V1-8-r.jpg", "2": F("1VaAy0gfb96JaFX8Fs2hFZyuC7WPrADBU"), "3": SF("06-vela"), "4": SF("01-luz-quente"),
    "5": SF("02-linho"), "6": SF("03-ondas"), "7": f"{S}/V2-8-c.jpg", "8": F("1QSmcSmlkR9ZZ4bYiCzxG97cDp-TBotEh"),
    "9": F("1e7aoT-5HwNMwOR6cJZNh5Bmakh5xkeAU")})

spa2 = spa("Marcaste uma massagem ao domicílio em Lisboa e não sabes o que preparar antes de o terapeuta tocar à campainha",
  "o que preparar", [
  sl("É a primeira vez que pedes uma massagem em casa. Marcaste para quinta às 20h, arrumaste a sala à pressa e agora perguntas-te onde é que a marquesa vai caber.", "A resposta é mais simples do que parece.", "Precisas de pouco espaço e de uns minutos de preparação."),
  sl("O terapeuta traz a marquesa dobrável, os óleos, os lençóis e as toalhas.", "Da tua parte basta um espaço livre mais ou menos do tamanho de uma cama de casal, com folga para ele andar à volta da marquesa sem bater nos móveis.", "A sala ou o quarto costumam chegar."),
  sl("Liga o aquecimento meia hora antes, sobretudo agora que as noites em Lisboa arrefeceram.", "Vais estar deitado e quieto durante uma hora, coberto só com uma toalha, e o corpo arrefece depressa quando não te mexes.", "Com frio, os ombros não relaxam."),
  sl("Baixa a luz do teto e acende um candeeiro de canto. Põe o telemóvel em silêncio e combina com quem vive contigo que essa hora fica sem chamadas nem visitas.", "Se tens cão ou gato, deixa-o noutra divisão com a porta fechada.", "Essa hora é tua, mesmo dentro de casa."),
  sl("Toma um duche antes, come qualquer coisa leve até uma hora antes e veste roupa fácil de tirar.", "Diz ao terapeuta se tens alguma lesão, se estás grávida ou se há uma zona onde não queres que toque, e ele ajusta a sessão a isso.", "Quanto mais claro fores, melhor corre a hora."),
  sl("Ao domicílio podes pedir massagem relaxante, terapêutica, desportiva, drenagem linfática, reflexologia e até massagem a casal, se houver espaço para duas marquesas.", "Nem todos os terapeutas fazem todas, por isso confirma ao marcar.", "Escolhe o tipo de massagem antes de escolher a hora."),
  sl("No fim, o terapeuta arruma tudo em poucos minutos. Tu não tens de sair, conduzir nem procurar estacionamento à porta de um espaço.", "Bebe um copo de água e deita-te mais cedo, porque o corpo pede descanso depois de uma hora na marquesa.", "Do sofá para a cama, sem trânsito pelo meio."),
  sl("Em lisboamassagem.pt encontras terapeutas que vão ao domicílio, vês a zona onde atendem e falas com eles diretamente por WhatsApp.", "Guarda este post para a primeira marcação e envia-o a quem diz que nunca tem tempo para ir a um espaço.", "Marca a tua massagem pelo link na bio."),
], {"cover": F("1Xv0A7goYJeokBaB28wf43TwIlLOkCiom"), "2": F("1trcnSD0hNoc4Rckj_iPh8MR9LXSoOspq"), "3": SF("04-ripado"), "4": F("1pQFtt3YF92Q5QZZGDUt-ADVvU_8q3Rvk"),
    "5": F("1e7aoT-5HwNMwOR6cJZNh5Bmakh5xkeAU"), "6": SF("01-luz-quente"), "7": f"{S}/V1-14-r.jpg", "8": SF("05-oliva"),
    "9": SS("01-home")})

spa3 = spa("Terapeuta, a cliente marcou para as 19h, não apareceu, não atendeu o telefone e tu ficaste uma hora com a marquesa montada",
  "ficaste uma hora com a marquesa montada", [
  sl("Preparaste a sala, aqueceste os óleos e recusaste outro pedido para esse horário porque já estava ocupado.", "Às 19h10 mandas mensagem, às 19h20 ligas e ninguém atende do outro lado.", "Às 20h desmontas a marquesa sem teres recebido um cêntimo pela hora."),
  sl("Uma falta destas custa mais do que a hora perdida. Custa a cliente que ficou sem vaga, a deslocação quando atendes ao domicílio e a vontade de abrir a agenda para a semana seguinte.", "Quando acontece duas vezes no mesmo mês, nota-se bem nas contas do mês.", "Muitas faltas evitam-se com uma mensagem."),
  sl("Confirma sempre na véspera. Uma mensagem curta no WhatsApp com o dia, a hora, a morada e o tipo de massagem, a pedir que a cliente responda com um sim.", "Quem não responde até ao fim do dia recebe uma segunda mensagem de manhã.", "Sem resposta, a vaga volta para a agenda."),
  sl("Escreve uma regra de cancelamento simples e envia-a logo na marcação. Por exemplo: cancelamentos até 24 horas antes sem custo, depois disso cobras metade da sessão.", "Muitos terapeutas têm vergonha de falar nisto com o cliente.", "Quem leva o teu horário a sério percebe a regra."),
  sl("Para clientes novos, podes pedir um sinal por MB WAY para segurar o horário, sobretudo nas horas mais procuradas, ao fim do dia e ao sábado.", "Diz o valor do sinal logo na primeira mensagem, junto com o preço da sessão.", "Um sinal pequeno mostra quem quer mesmo marcar."),
  sl("Mantém uma lista de espera. Quando alguém pede um horário que já está ocupado, guarda o contacto e pergunta se aceita ser avisado caso abra uma vaga.", "Quando uma cliente cancela na véspera, já tens a quem mandar mensagem.", "A vaga perdida pode voltar a ser ocupada no mesmo dia."),
  sl("Em lisboamassagem.pt, a cliente fala contigo diretamente por WhatsApp, sem intermediários. A confirmação, a regra de cancelamento e o sinal ficam todos na mesma conversa.", "O registo e o anúncio são grátis, com busca por distrito, categoria ou nome.", "Mais clientes a encontrar-te compensam a que falha."),
  sl("Se és terapeuta, escreve hoje a tua mensagem de confirmação e a tua regra de cancelamento, e anuncia-te grátis em lisboamassagem.pt.", "Conheces um colega que já ficou à espera de uma cliente que nunca chegou? Envia-lhe este post.", "A tua hora também tem valor."),
], {"cover": F("1e7aoT-5HwNMwOR6cJZNh5Bmakh5xkeAU"), "2": F("1o1yvvbcuIg6K7r20rkXWLqwXJqQ411m2"), "3": SF("06-vela"), "4": f"{S}/V2-14-c.jpg",
    "5": SF("02-linho"), "6": F("1pQFtt3YF92Q5QZZGDUt-ADVvU_8q3Rvk"), "7": SF("05-oliva"), "8": SS("04-terapeutas"),
    "9": F("1huK-Phz3jFOV8rQ6Y4UGJwch5sw0Ewfh")})


def palavras(t):
    return len(re.sub(r"<[^>]+>", "", t).split())


if __name__ == "__main__":
    for c in (spa1, spa2, spa3):
        print(len(c["hook"]), c["hook"][:40])
        for i, s in enumerate(c["slides"], 2):
            n = palavras(s)
            if not 40 <= n <= 80:
                print("AVISO palavras", c["hook"][:30], i, n)
    retrato(V1(8), f"{S}/V1-8-r.jpg", cx=0.5)
    retrato(V1(14), f"{S}/V1-14-r.jpg", cx=0.5)
    corta_topo(V2(8), f"{S}/V2-8-c.jpg", 0.18)
    corta_topo(V2(14), f"{S}/V2-14-c.jpg", 0.18)
    sel = sys.argv[1:] or ["l1", "l2", "l3", "s1", "s2", "s3"]
    O = lambda p, n: f"{R}/posts/{DIA}/{p}-{n}"
    if "l1" in sel: run("render_formatos.py", polemica, O("liurialves", 1))
    if "l2" in sel: run("render_formatos.py", quadro, O("liurialves", 2))
    if "l3" in sel: run("render_formatos.py", venda, O("liurialves", 3))
    if "s1" in sel: run("render_carrossel.py", spa1, O("spatherapieslisbon", 1))
    if "s2" in sel: run("render_carrossel.py", spa2, O("spatherapieslisbon", 2))
    if "s3" in sel: run("render_carrossel.py", spa3, O("spatherapieslisbon", 3))
    print("ok")
