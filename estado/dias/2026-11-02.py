"""Plano 100 mil, semana 2, dia 3 (02/11/2026, segunda, dia par). 3 carrosséis do @liurialves, 3 CTAs diferentes.
CTA roda entre horários: ontem 14:20 salvar / 17:40 comentário / 20:30 envio -> hoje 14:20 comentário / 17:40 envio / 20:30 salvar.
Remodelado (dia par, @99hud): 14:20 tweet a partir do carrossel da @99hud "Teu limite do Claude some rápido..."
(prints IMG_0667 a IMG_0674 na pasta referencias-99hud). Copiado só o molde: alerta + teste que o leitor faz + ferramenta
gratuita de uma grande empresa + o que ela mostra + faça a conta + "a maioria culpa X, o gargalo é Y" + "eu testo antes" +
comente palavra + siga. Tema, texto e exemplos 100% do Liuri (Perfil da Empresa no Google para negócio de bairro).
Tema do dia: o cliente e o dinheiro que a empresa perde sem perceber.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/a82b3699-a12b-52b3-8a6b-6c577fd56db7/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-02"
F = lambda x: f"/tmp/fotos/{x}.jpg"

# 1) 14:20 TWEET, ângulo B cliente e conteúdo, CTA = COMENTÁRIO (MAPA). REMODELADO de @99hud.
tweet = {"formato": "tweet", "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": f"{R}/assets/avatar-liuri.jpg", "slides": [{"texto": t} for t in [
  "Se o seu negócio atende no bairro e não aparece no Google Maps, você está perdendo cliente para o concorrente da rua de baixo. E quase ninguém percebe, porque esse cliente nunca chegou a mandar mensagem.",
  "Faça este teste agora, no celular de outra pessoa: pesquise o seu serviço com o nome do bairro, como \"manicure Benfica\" ou \"mecânico Penha\". Veja quem aparece nos três primeiros lugares do mapa.",
  "Se o seu nome não está ali, a cliente liga para quem está. Ela não vai abrir o Instagram para descobrir que você existe. Decide em poucos segundos, olhando a nota, as fotos e a distância.",
  "A ferramenta que resolve isso é gratuita e é do próprio Google: o **Perfil da Empresa**. Você cadastra o endereço ou a área de atendimento, o horário, o telefone, fotos e o link do WhatsApp ou do site.",
  "Os três ajustes que eu faço primeiro: a categoria certa do serviço, fotos reais do espaço e do trabalho, e avaliações respondidas. Peça a avaliação no fim do atendimento, quando o cliente ainda está satisfeito.",
  "Depois de verificado, o perfil mostra quantas pessoas viram o seu negócio, quantas ligaram e quantas pediram a rota até você. É o primeiro relatório que eu peço a um dono de negócio local antes de falar em anúncio.",
  "Com um mês de perfil ativo, pegue as ligações e os pedidos de rota e multiplique pelo valor médio de um atendimento. Esse número mostra quanto o mapa vale para a sua empresa.",
  "Muito dono culpa o Instagram quando a agenda esvazia. Só que o cliente de bairro costuma procurar no Google, com pressa, a poucos minutos de casa, e o seu feed não aparece nessa busca.",
  "Eu testo essas ferramentas nos negócios que acompanho antes de falar delas aqui. Comente **MAPA** e o seu bairro que eu respondo com o primeiro ajuste que eu faria no seu perfil.\n\nSiga @liurialves para o próximo teste.",
]]}

# 2) 17:40 QUADRO, ângulo A dinheiro e gestão, CTA = ENVIO
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "Os 5 vazamentos que eu procuro primeiro no [[extrato]] de uma pequena empresa",
   "desenho": {"tipo": "numero", "n": 5, "nota": "somem com o lucro"},
   "texto": "Para quem fatura bem e não entende por que o dinheiro não aparece no fim do mês."},
  {"etiqueta": "O problema", "titulo": "Faturar bem e não ver o dinheiro no fim do mês", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3", "4", "5"], "nota": "sai aos poucos"},
   "texto": "Em empresa pequena, o dinheiro costuma sair em valores baixos, quase todo dia, por lugares que ninguém confere porque parecem normais.",
   "soco": "Você só enxerga o vazamento quando soma."},
  {"etiqueta": "Vazamento 1 de 5", "titulo": "A taxa da maquininha e do link de pagamento", "desenho": {"tipo": "numero", "n": 1, "nota": "some o mês inteiro"},
   "texto": "Cada venda no cartão paga uma taxa, e o parcelado sem juros quase sempre sai do seu bolso. Some todas as taxas do último extrato e compare com a proposta de outro banco.",
   "soco": "Taxa que você nunca somou parece pequena."},
  {"etiqueta": "Vazamento 2 de 5", "titulo": "Assinaturas que ninguém usa", "desenho": {"tipo": "numero", "n": 2, "nota": "app, sistema, plano"},
   "texto": "Sistema de agenda, editor de vídeo, armazenamento, aplicativo que alguém assinou para testar. Cobrança pequena no cartão da empresa, todo mês, durante anos.",
   "soco": "Cancele o que ninguém abriu nos últimos 30 dias."},
  {"etiqueta": "Vazamento 3 de 5", "titulo": "O desconto dado no WhatsApp", "desenho": {"tipo": "numero", "n": 3, "nota": "sem anotar"},
   "texto": "O cliente pede um desconto, você concede para não perder a venda e não anota. O custo do atendimento continua igual, então esse valor sai inteiro do seu lucro.",
   "soco": "Desconto sem registro é dinheiro que você nem viu sair."},
  {"etiqueta": "Vazamento 4 de 5", "titulo": "A falta sem aviso", "desenho": {"tipo": "numero", "n": 4, "nota": "horário perdido"},
   "texto": "Em serviço com hora marcada, o horário vazio não volta: você já pagou o espaço, o material e o seu tempo. Confirme na véspera e cobre sinal nos horários mais procurados.",
   "soco": "Agenda cheia no papel ainda não é dinheiro no caixa."},
  {"etiqueta": "Vazamento 5 de 5", "titulo": "Produto e estoque parados", "desenho": {"tipo": "numero", "n": 5, "nota": "validade, sobra"},
   "texto": "Produto comprado na promoção que vence na prateleira, estoque maior do que o mês consome, material que some sem controle. Tudo isso já foi pago e não volta como venda.",
   "soco": "Compre pelo que o mês consome."},
  {"etiqueta": "Na prática", "titulo": "A primeira rodada cabe numa hora", "desenho": {"tipo": "lista", "check": True, "itens": ["somar as taxas do mês", "cancelar 1 assinatura", "anotar cada desconto", "confirmar na véspera", "contar o estoque"]},
   "texto": "O extrato aberto no celular e uma folha de papel bastam para começar."},
  {"etiqueta": "Próximo passo", "titulo": "Envie para o seu sócio e façam a conta juntos", "desenho": {"tipo": "numero", "n": 1, "nota": "hora com o extrato"},
   "texto": "Envie este post para o seu sócio ou para quem cuida do financeiro e marquem uma hora esta semana para olhar o extrato. Se quiser que eu faça essa leitura com você, mande CALL no direct.",
   "soco": "Comece pela taxa do cartão, que é a mais fácil de somar."},
]}

# 3) 20:30 CAPA + ESCURO, ângulo C vida de quem empreende, CTA = SALVAR
vida = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": F("1YETcE8OmU8irqQkuTY36S4umU330SZGa"), "foco_y": 0.25, "etiqueta": "Vida de quem empreende",
   "titulo": "Empreender com filho pequeno em casa me obrigou a criar [[5 regras]]",
   "sub": "Empresa, treino e família na mesma semana. Salve para aplicar."},
  {"etiqueta": "Antes das regras", "frase": "No começo, a empresa ocupava [[todo horário que sobrava]], inclusive o jantar.",
   "texto": "A empresa crescia um pouco e a casa sentia muito. As regras a seguir vieram dessa fase, e é por elas que hoje eu consigo treinar, estar com a família e fechar os números da semana."},
  {"etiqueta": "Regra 1", "frase": "O horário de desligar entra na agenda [[como se fosse um cliente]].",
   "texto": "Se não está marcado, outra coisa ocupa. Eu coloco o fim do expediente no mesmo calendário dos atendimentos e respeito esse horário do mesmo jeito."},
  {"etiqueta": "Regra 2", "frase": "O celular da empresa [[não senta à mesa]].",
   "texto": "Mensagem que chega durante o jantar é respondida depois, e uma resposta automática avisa o horário de atendimento. O cliente que precisa mesmo espera meia hora."},
  {"etiqueta": "Regra 3", "frase": "O treino é [[inegociável]], porque é ele que segura o resto.",
   "texto": "No MMA eu descarrego a semana. Quando eu corto o treino para trabalhar mais, volto para casa pior e trabalho com menos cabeça no dia seguinte."},
  {"etiqueta": "Regra 4", "frase": "A família sabe [[qual é a meta do mês]].",
   "texto": "Quando a minha esposa sabe o que eu estou construindo e até quando, a noite mais longa passa a ser um combinado entre nós dois."},
  {"etiqueta": "Regra 5", "frase": "Um dia da semana é [[só da família]].",
   "texto": "Sem reunião, sem planilha e sem a mensagem rápida que vira uma hora. Esse dia protege o motivo pelo qual eu decidi empreender."},
  {"etiqueta": "O que eu aprendi", "frase": "Empresa que só fecha o mês com você longe de casa [[ainda não está pronta]].",
   "texto": "Se o negócio precisa do seu jantar, do seu domingo e do seu treino para dar resultado, o problema está no processo. E processo se ajusta."},
  {"etiqueta": "Salve", "frase": "Salve este post para aplicar [[as 5 regras]] esta semana.",
   "texto": "Escolha uma para começar hoje e mostre para quem divide a casa com você. Se a sua empresa só fecha o mês com você trabalhando até tarde, mande CALL no direct."},
]}

LEGENDAS = {
 1: """Se o seu negócio atende no bairro e não aparece no Google Maps, o cliente liga para o concorrente e você nem fica sabendo. Você já fez esse teste?

Pesquise o seu serviço com o nome do bairro, no celular de outra pessoa. Se você não está entre os primeiros do mapa, o problema não se resolve com mais post no Instagram.

O Perfil da Empresa do Google é gratuito. Categoria certa, fotos reais, avaliações respondidas e, depois de um mês, o relatório de ligações e pedidos de rota mostra quanto o mapa vale para você.

🔻 Comente MAPA e o seu bairro que eu respondo com o primeiro ajuste que eu faria no seu perfil.

#marketingdigital #negocioproprio #empreendedorismo #vendas #brasileirosemportugal""",
 2: """Os 5 vazamentos que eu procuro primeiro no extrato de uma pequena empresa. Você fatura bem e não vê o dinheiro no fim do mês?

Taxa da maquininha, assinatura que ninguém usa, desconto dado no WhatsApp sem anotar, falta sem aviso e estoque parado. Cada um parece pequeno sozinho. Somados, explicam muito mês apertado.

A primeira rodada cabe numa hora, com o extrato aberto e uma folha de papel.

🔻 Envie este post para o seu sócio ou para quem cuida do financeiro e marquem essa hora esta semana. Se quiser que eu faça a leitura com você, mande CALL no direct.

#gestao #empresario #empreendedorismo #negocioproprio #brasileirosemportugal""",
 3: """Empreender com filho pequeno em casa me obrigou a criar 5 regras. Quais delas você já segue?

No começo, a empresa ocupava todo horário que sobrava, inclusive o jantar. Hoje o horário de desligar está na agenda, o celular da empresa não senta à mesa, o treino é inegociável, a minha esposa sabe qual é a meta do mês e um dia da semana é só da família.

Empresa que só fecha o mês com você longe de casa ainda precisa de processo.

🔻 Salve este post para aplicar as 5 regras esta semana. Se a sua empresa só fecha o mês com você trabalhando até tarde, mande CALL no direct.

#vidadeempreendedor #empreendedorismo #negocioproprio #brasileirosemportugal #lisboa""",
}


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_formatos.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    run(tweet, O(1)); run(quadro, O(2)); run(vida, O(3)); print("ok")
