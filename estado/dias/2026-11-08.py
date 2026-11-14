"""Plano 100 mil, semana 3, dia 2 (08/11/2026, domingo). Dia 2 do "Plano de 30 dias para lançar a mentoria":
pilar 3, "Cheguei a Lisboa sem clientes: como foi o começo"; tarefa: listar 20 contatos para a mensagem da mentoria.
REFEITO às 04:40 UTC a pedido do dono: o conteúdo passa a falar com o COMPRADOR IDEAL (Dream Buyer Sheet: dono de negócio
estagnado entre 1.500 € e 5.000 € por mês; exemplos de personal trainer, academia, fisioterapia e barbearia) e todo CTA é
"Comente CLIENTES" (regra do dono de 08/11). Prova nova do dono: 1.500 € → 5.500 € em 5 meses → 7.000 €/mês, sozinho.
FUNIL (regra de 07/11): 14:20 VALOR, 17:40 PROVA, 20:30 CONEXÃO (+ 12:40 IA = valor, 22:15 conexão própria, sem prints
do @modocaverna). Tipo de CTA: 14:20 salvar, 17:40 envio, 20:30 comentário, sempre com "Comente CLIENTES".
14:20 QUADRO, valor, pilar comprador 1 (cliente todo mês): trazer de volta o aluno/cliente que sumiu, com script.
17:40 CAPA+ESCURO, prova, pilar comprador 5: de 1.500 € para 7.000 € por mês, as 5 peças que eu montei sozinho.
20:30 FAIXA, conexão, pilar comprador 6. REMODELADO do post do dono "Essa foto é de alguns anos atrás. Antes de
      Lisboa..." (buffer 6aef12346e634ea12c142602, 07/11, 278 de alcance). Mudou: foto única virou carrossel faixa, a
      história da esposa entra no recomeço em Lisboa, fotos novas, lição para o dono parado e CTA CLIENTES.
22:15 TWEET, conexão, pilar comprador 3 (oferta e preço): o cliente de 300 € por mês da massagem e o plano mensal.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/a44d0111-cae6-53e8-80e2-036407ec1b26/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-08"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
P = lambda x: f"/tmp/px8/pexels-{x}.jpg"

# 1) 14:20 QUADRO, VALOR, CTA = SALVAR + CLIENTES
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "A mensagem que traz de volta [[o aluno que parou de treinar]]",
   "desenho": {"tipo": "circulos", "rotulos": ["lista", "mensagem", "agenda"], "centro": "VOLTA"},
   "texto": ""},
  {"etiqueta": "Faturamento parado?", "titulo": "Antes de procurar cliente novo, olhe para quem já pagou você",
   "desenho": {"tipo": "numero", "n": 20, "nota": "nomes que já pagaram você"},
   "texto": "Personal, academia, fisioterapia ou barbearia: role o WhatsApp até seis meses atrás. Cada nome ali já confiou em você. Trazer de volta custa uma mensagem bem escrita.",
   "soco": "O mês parado pode destravar no seu histórico."},
  {"etiqueta": "Passo 1 de 4", "titulo": "Faça a lista de 20 nomes", "desenho": {"tipo": "numero", "n": 1, "nota": "pagou e sumiu há 60 a 180 dias"},
   "texto": "Anote 20 alunos, pacientes ou clientes que pagaram e não voltaram entre dois e seis meses atrás. Ao lado de cada nome, escreva o que a pessoa fazia com você e quando parou.",
   "soco": "Sem a lista, a mensagem vira disparo em massa."},
  {"etiqueta": "Passo 2 de 4", "titulo": "Uma conversa por pessoa", "desenho": {"tipo": "numero", "n": 2, "nota": "nome + o que fazia com você"},
   "texto": "Nada de lista de transmissão. Cada mensagem leva o nome da pessoa e o que ela fazia com você, porque é isso que mostra que você lembrou dela.",
   "soco": "Mensagem que serve para todos é ignorada por todos."},
  {"etiqueta": "Passo 3 de 4", "titulo": "Copie esta mensagem", "desenho": {"tipo": "numero", "n": 3, "nota": "troque o que está entre colchetes"},
   "texto": "\"Olá, [nome], tudo bem? Aqui é o [seu nome]. Lembrei de você porque até [mês] você vinha [treinar / à fisioterapia / cortar] comigo. Como você está? Tenho dois horários livres na [dia]. Quer que eu reserve um?\"",
   "soco": "Termine sempre com uma pergunta fácil de responder."},
  {"etiqueta": "Passo 4 de 4", "titulo": "Volte uma vez, três dias depois", "desenho": {"tipo": "numero", "n": 4, "nota": "uma vez só"},
   "texto": "Para quem não respondeu: \"Oi, [nome], conseguiu ver a minha mensagem? Se preferir outro dia, me diga qual.\" Depois disso, siga para o próximo nome da lista.",
   "soco": "Lembrar uma vez é atendimento."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3", "4"], "nota": "desconto na primeira linha"},
   "texto": "O dono abre a conversa oferecendo desconto. O aluno que voltaria pelo preço normal aprende a esperar a próxima promoção, e a sua margem cai junto.",
   "soco": "Primeiro a conversa. Desconto, se precisar, fica para o fim."},
  {"etiqueta": "Na prática", "titulo": "Uma hora, hoje",
   "desenho": {"tipo": "lista", "check": True, "itens": ["20 nomes na lista", "20 mensagens com o nome", "respostas anotadas", "nova mensagem em 3 dias", "horários na agenda"]},
   "texto": "Anote quantos responderam e quantos voltaram. Esse número é a sua taxa de retorno, e no mês que vem você já sabe quanto esperar dela."},
  {"etiqueta": "Próximo passo", "titulo": "Salve e envie as 20 mensagens ainda hoje",
   "desenho": {"tipo": "numero", "n": 20, "nota": "mensagens antes de segunda"},
   "texto": "Se a sua empresa está parada no mesmo faturamento há meses, esta é a primeira peça. Comente CLIENTES que eu te chamo no direct para montar o resto do sistema com você.",
   "soco": "Quem já pagou conhece o caminho até você."},
]}

# 2) 17:40 CAPA + ESCURO, PROVA, CTA = ENVIO + CLIENTES
prova = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": FL("home-office-headset"), "foco_y": 0.3, "etiqueta": "Prova",
   "titulo": "A minha empresa saiu de 1.500 € para 7.000 € por mês. Eu fazia tudo sozinho.",
   "sub": "As peças que eu montei, na ordem, para quem está parado no mesmo faturamento."},
  {"etiqueta": "Os números", "frase": "1.500 €, depois [[5.500 € em 5 meses]], depois 7.000 € por mês.",
   "texto": "Sem equipe de marketing e sem agência. O conteúdo, os anúncios e o atendimento eram comigo, no mesmo dia em que eu atendia cliente."},
  {"etiqueta": "Peça 1", "frase": "Uma oferta que [[o cliente entende em uma frase]].",
   "texto": "Antes de postar ou anunciar, eu deixei claro para quem é, o que a pessoa recebe e quanto custa. Sem isso, todo o resto só gera curtida."},
  {"etiqueta": "Peça 2", "frase": "Um perfil que [[explica e convida]].",
   "texto": "Bio dizendo para quem eu trabalho, posts fixados com prova e um caminho claro para a mensagem. Quem chega precisa saber em cinco segundos o que fazer."},
  {"etiqueta": "Peça 3", "frase": "Um caminho do post [[até o WhatsApp]].",
   "texto": "Todo conteúdo termina numa conversa. É ali que a venda acontece, e é ali que a maioria dos donos perde o cliente por não saber conduzir."},
  {"etiqueta": "Peça 4", "frase": "Anúncio para [[quem já procura]].",
   "texto": "Eu parei de impulsionar post e passei a anunciar para gerar mensagem. É o mesmo que eu faço para a Lisboa Massagem, que hoje tem mais de 90 terapeutas."},
  {"etiqueta": "Peça 5", "frase": "Um script para [[transformar conversa em venda]].",
   "texto": "Pergunta certa, preço depois do valor e o próximo passo marcado na mesma conversa. Mensagem respondida sem roteiro é cliente que esfria."},
  {"etiqueta": "Para quem é", "frase": "Para o dono que fatura entre [[1.500 € e 5.000 €]] e está parado.",
   "texto": "Personal trainer, academia, fisioterapia, barbearia. Se você quer milagre sem executar, isto não é para você."},
  {"etiqueta": "Próximo passo", "frase": "Envie para um dono de negócio [[que está parado]].",
   "texto": "E se esse dono é você, comente CLIENTES. Eu te chamo no direct e te mostro como montar essas cinco peças no seu negócio na minha mentoria."},
]}

# 3) 20:30 FAIXA, CONEXÃO, CTA = COMENTÁRIO CLIENTES. REMODELADO.
faixa = {"slides": [
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "CHEGUEI A PORTUGAL",
   "texto": "COM 300 € E SEM NINGUÉM QUE ME INDICASSE"},
  {"tipo": "foto", "foto": P(35815356), "foco_y": 0.35, "faixa": "OS PRIMEIROS 3 MESES",
   "texto": "VIM SOZINHO. FIQUEI SEM CORTAR O CABELO E COMENDO PIZZA E LASANHA DE SUPERMERCADO PARA O DINHEIRO DURAR."},
  {"tipo": "foto", "foto": P(37026408), "foco_y": 0.5, "faixa": "PARA FECHAR O MÊS",
   "texto": "RESTAURANTE 12 HORAS POR DIA. NO FIM DE SEMANA, CLUBE DA MEIA-NOITE ÀS 8 DA MANHÃ, POR 60 € A NOITE."},
  {"tipo": "foto", "foto": P(14774928), "foco_y": 0.5, "faixa": "QUEM SEGUROU COMIGO",
   "texto": "A MINHA ESPOSA CHEGOU 3 MESES DEPOIS, GRÁVIDA DO NOSSO SEGUNDO FILHO. MORÁVAMOS NUM QUARTO.",
   "destaque": "ELA ACREDITOU QUANDO AINDA NÃO HAVIA NADA PARA MOSTRAR."},
  {"tipo": "foto", "foto": P(37719555), "foco_y": 0.4, "faixa": "A VIRADA",
   "texto": "SUBGERENTE EM 6 MESES, DOIS ANOS DE UBER E, DEPOIS, AS MASSAGENS E OS SITES PARA CLIENTES."},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.35, "faixa": "HOJE",
   "texto": "A MINHA EMPRESA SAIU DE 1.500 € E CHEGOU A 7.000 € POR MÊS, COMIGO FAZENDO CONTEÚDO, ANÚNCIO E ATENDIMENTO."},
  {"tipo": "branco", "blocos": [
   ["t", "SE A SUA EMPRESA ESTÁ PARADA NO MESMO FATURAMENTO, COMECE POR AQUI:"], ["esp", 14],
   ["h", "1. ESCREVA 20 NOMES"],
   ["n", "Alunos, pacientes e clientes satisfeitos que já viram o seu trabalho de perto."],
   ["h", "2. UMA MENSAGEM POR PESSOA"],
   ["n", "Pergunte como a pessoa está e quem ela conhece que precisa do que você faz."],
   ["h", "3. ANOTE E VOLTE EM 3 DIAS"],
   ["n", "Indicação que você pede tem dia marcado. A que você espera depende de sorte."]]},
  {"tipo": "foto", "foto": FL("mma-equipe-treino"), "foco_y": 0.4, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E TE MOSTRO COMO TER CLIENTES TODO MÊS SEM DEPENDER DE INDICAÇÃO.",
   "destaque": "SE VOCÊ TAMBÉM COMEÇOU DO ZERO, ESTE POST É SEU."},
]}

# 4) 22:15 TWEET, CONEXÃO, CTA comentário CLIENTES. No lugar do repost (sem prints do @modocaverna).
tweet = {"formato": "tweet", "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": f"{R}/assets/avatar-liuri.jpg", "slides": [{"texto": t} for t in [
  "Na massagem, eu tive um cliente que pagava cerca de 300 € por mês. Vinha duas a três vezes por semana e não escolhia pelo preço.",
  "Ele comprava porque eu era profissional, porque ele sentia o resultado no corpo e porque confiava em mim.",
  "Foi com ele que eu entendi a diferença entre vender sessão avulsa e ter cliente todo mês. Um cliente assim vale mais do que dez que aparecem quando sobra dinheiro.",
  "Hoje eu vejo personal trainer, fisioterapeuta e barbeiro presos nos 2 ou 3 mil euros pelo mesmo motivo: vendem uma hora de cada vez e recomeçam do zero todo mês.",
  "O cliente que paga com gosto existe no seu negócio. Ele só precisa de um motivo para ficar: um plano com frequência, acompanhamento e um resultado que ele sente.",
  "Faça a conta hoje. Quantos clientes você tem pagando todo mês, sem você precisar vender de novo? Se a resposta é quase nenhum, o seu faturamento depende de sorte.",
  "Comece pelos cinco clientes que mais voltam. Ofereça a eles um plano mensal com a frequência que eles já têm, e não um desconto na sessão.",
  "Faturamento previsível começa no dia em que o seu melhor cliente deixa de comprar por sessão.",
  "Se a sua empresa está parada no mesmo faturamento, comente CLIENTES que eu te chamo no direct.",
]]}

LEGENDAS = {
 1: """Faturamento parado há meses? Antes de procurar cliente novo, abra o WhatsApp e role até seis meses atrás.

Personal trainer, academia, fisioterapia ou barbearia: quem já pagou você e sumiu é o cliente mais fácil de trazer de volta. O método cabe em uma hora: lista de 20 nomes, uma mensagem por pessoa com o nome e o que ela fazia com você, uma pergunta fácil no fim e uma única mensagem de volta três dias depois.

A mensagem pronta está no slide 5. Troque o que está entre colchetes e envie hoje.

🔻 Salve para repetir todo mês. E se a sua empresa está parada no mesmo faturamento, comente CLIENTES que eu te chamo no direct.

#personaltrainer #barbearia #fisioterapia #empreendedorismo #donodenegocio""",
 2: """A minha empresa saiu de 1.500 € para 5.500 € em 5 meses e depois para 7.000 € por mês. Eu fazia sozinho o conteúdo, os anúncios e o atendimento.

Não foi um post que viralizou. Foram cinco peças montadas na ordem: uma oferta que o cliente entende em uma frase, um perfil que explica e convida, um caminho do post até o WhatsApp, anúncio para quem já procura e um script para transformar conversa em venda.

É para o dono que fatura entre 1.500 € e 5.000 € e está parado: personal trainer, academia, fisioterapia, barbearia. Se você quer milagre sem executar, não é para você.

🔻 Envie para um dono de negócio que está parado. Se esse dono é você, comente CLIENTES que eu te chamo no direct e te mostro como montar essas peças na minha mentoria.

#empreendedorismo #donodenegocio #marketingdigital #personaltrainer #brasileirosemportugal""",
 3: """Cheguei a Portugal sozinho, com 300 € e sem ninguém que me indicasse.

Nos primeiros três meses fiquei sem cortar o cabelo e comendo pizza e lasanha de supermercado. Depois vieram 12 horas por dia no restaurante e, no fim de semana, o clube da meia-noite às 8 da manhã por 60 € a noite. A minha esposa chegou grávida do nosso segundo filho e morávamos num quarto. Subi a subgerente em 6 meses, fiz dois anos de Uber e, depois, comecei com as massagens e os sites para clientes. Em 2026 a minha empresa saiu de 1.500 € e chegou a 7.000 € por mês.

Se a sua empresa está parada no mesmo faturamento, comece por quem já conhece o seu trabalho: 20 nomes, uma mensagem por pessoa e uma volta em três dias. Indicação que você pede tem dia marcado.

🔻 Comente CLIENTES que eu te chamo no direct e te mostro como ter clientes todo mês sem depender de indicação.

#empreendedorismo #brasileirosemportugal #donodenegocio #vidadeempreendedor #portugal""",
 5: """Na massagem, eu tive um cliente que pagava cerca de 300 € por mês, duas a três vezes por semana, e não escolhia pelo preço.

Ele comprava porque sentia o resultado e confiava em mim. Personal trainer, fisioterapeuta e barbeiro presos nos 2 ou 3 mil euros quase sempre vendem uma hora de cada vez e recomeçam do zero todo mês.

Faça a conta: quantos clientes pagam você todo mês sem você precisar vender de novo? Comece pelos cinco que mais voltam e ofereça um plano mensal com a frequência que eles já têm.

🔻 Se a sua empresa está parada no mesmo faturamento, comente CLIENTES que eu te chamo no direct.

#personaltrainer #barbearia #fisioterapia #donodenegocio #empreendedorismo""",
}


def run(cfg, out, script="render_formatos.py"):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/{script}", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    for n in (1, 2, 3, 5):
        for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(quadro, O(1)); run(prova, O(2)); run(faixa, O(3), "render_faixa.py"); run(tweet, O(5)); print("ok")
