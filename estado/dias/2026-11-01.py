"""Plano 100 mil, semana 2, dia 2 (01/11/2026, domingo, dia ímpar). 3 carrosséis do @liurialves, 3 CTAs diferentes.
CTA roda entre horários: ontem 14:20 envio / 17:40 salvar / 20:30 comentário -> hoje 14:20 salvar / 17:40 comentário / 20:30 envio.
Remodelado (dia ímpar): 17:40 refaz o Reel "Be strong, you have time to change, no excuses" (buffer 6ad4a982221235fdf9012459,
18/10, 1.531 de alcance, o maior dos posts enviados que a rotina conseguiu ler) como carrossel fotofrase com história do Liuri.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/0f0abd7e-0520-5a9f-8af1-a31530cc4d24/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-01"
F = lambda x: f"/tmp/fotos/{x}.jpg"
PX = lambda x: f"/tmp/px3/pexels-{x}.jpg"

# 1) 14:20 QUADRO, ângulo A dinheiro e gestão, CTA = SALVAR
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "A ordem em que eu separo o dinheiro de [[cada venda]]",
   "desenho": {"tipo": "funil", "camadas": ["tudo o que entra", "impostos", "custos do mês", "o seu salário", "lucro"], "lado": "o que sobra"},
   "texto": "Serve para quem fatura em reais ou em euros e ainda paga a casa e a empresa pela mesma conta."},
  {"etiqueta": "O problema", "titulo": "Uma conta só para tudo esconde o prejuízo", "desenho": {"tipo": "circulos", "rotulos": ["casa", "empresa"], "centro": "UMA CONTA"},
   "texto": "Quando o mercado de casa, a parcela do carro e o fornecedor saem da mesma conta, o saldo do fim do mês não diz nada. Você acha que sobrou e gastou o dinheiro do imposto.",
   "soco": "Saldo positivo na conta ainda não é lucro."},
  {"etiqueta": "Etapa 1 de 4", "titulo": "Tudo o que entra cai na conta da empresa", "desenho": {"tipo": "numero", "n": 1, "nota": "no mesmo dia"},
   "texto": "Pix, cartão, transferência e dinheiro vivo vão para a conta da empresa no dia em que entram. Receber na conta pessoal porque é mais prático é o começo da bagunça.",
   "soco": "O que não passa pela conta some do relatório."},
  {"etiqueta": "Etapa 2 de 4", "titulo": "O imposto sai antes de qualquer gasto", "desenho": {"tipo": "numero", "n": 2, "nota": "conta separada"},
   "texto": "No Brasil pode ser o DAS do MEI ou do Simples. Em Portugal, IVA, IRS e Segurança Social. Assim que a venda entra, a parte do imposto vai para uma conta que você não toca.",
   "soco": "Imposto guardado no dia não vira susto depois."},
  {"etiqueta": "Etapa 3 de 4", "titulo": "Os custos do mês têm dia marcado", "desenho": {"tipo": "numero", "n": 3, "nota": "aluguel, produto, anúncio"},
   "texto": "Liste os gastos fixos numa folha só e pague todos pela conta da empresa em um ou dois dias do mês: aluguel, produto, sistema, contador e anúncio.",
   "soco": "Gasto espalhado pelo mês é gasto que você esquece."},
  {"etiqueta": "Etapa 4 de 4", "titulo": "Você recebe um salário fixo", "desenho": {"tipo": "numero", "n": 4, "nota": "sempre no mesmo dia"},
   "texto": "Defina um valor que a empresa aguenta pagar todo mês e transfira para a sua conta pessoal sempre no mesmo dia. A casa vive desse valor, e nunca do saldo da empresa.",
   "soco": "O que sobra depois disso é o lucro de verdade."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3", "4", "5"], "nota": "pagar a casa primeiro"},
   "texto": "O dono recebe, paga as contas de casa com o dinheiro da venda e deixa o imposto para depois. Quando a guia chega, falta dinheiro e a empresa entra no cheque especial.",
   "soco": "A ordem pesa mais do que o valor."},
  {"etiqueta": "Na prática", "titulo": "Montando isso em uma semana", "desenho": {"tipo": "lista", "check": True, "itens": ["seg: conta da empresa", "ter: conta do imposto", "qua: folha dos custos", "qui: valor do salário", "sex: dia fixo no banco"]},
   "texto": "Dá para fazer tudo com o aplicativo do banco e uma folha de papel, sem planilha complicada."},
  {"etiqueta": "Próximo passo", "titulo": "Salve e separe as contas esta semana", "desenho": {"tipo": "numero", "n": 4, "nota": "contas, uma ordem"},
   "texto": "Salve este post para montar as quatro etapas com o extrato na mão. Se quiser que eu olhe os números da sua empresa com você, mande CALL no direct.",
   "soco": "Comece pela conta da empresa, ainda hoje."},
]}

# 2) 17:40 FOTOFRASE, ângulo C vida de quem empreende, CTA = COMENTÁRIO (1 ou 2). REMODELADO.
foto = {"formato": "fotofrase", "slides": [
  {"foto": F("1-Fjt_w42nRzVU4rBiKFqQdP3ekuXiciK"), "foco_y": 0.25, "texto": "Você acha que já passou da hora de mudar de vida. **Eu recomecei do zero em Lisboa, longe de tudo o que eu conhecia.**"},
  {"foto": PX(14297406), "texto": "Aos 19 eu entrei na Aeronáutica porque precisava do salário. **Anos depois, troquei a farda por um caminho sem salário fixo.**"},
  {"foto": PX(14462710), "texto": "Cheguei a Portugal sem carteira de clientes e sem conhecer o mercado daqui. **Comecei pelo que eu sabia fazer com as mãos.**"},
  {"foto": PX(4761659), "texto": "No MMA ninguém espera estar pronto para treinar com os mais fortes. **Você aprende a lutar lutando, e apanha bastante no começo.**"},
  {"foto": PX(6517400), "texto": "A empresa nasceu do mesmo jeito: atendendo de dia e aprendendo site, anúncio e números à noite. **Esse tempo eu tirei do sono.**"},
  {"foto": PX(14318650), "texto": "Muita gente usa a família como motivo para adiar. **Eu olho para o meu filho e é por ele que eu não adio mais.**"},
  {"foto": PX(19783892), "texto": "Mudar não pede uma segunda-feira perfeita. **Pede uma decisão pequena hoje: uma ligação, um orçamento enviado, um treino feito.**"},
  {"foto": PX(4398347), "texto": "Se eu tivesse esperado ter certeza, **ainda estaria contando os anos até a aposentadoria.**"},
  {"foto": F("1QLH5DwrDXIdhamp95FRNswZiauh35Z2f"), "foco_y": 0.45, "texto": "Você ainda tem tempo de mudar. **Comente 1 se já recomeçou alguma vez, ou 2 se ainda vai começar.**"},
]}

# 3) 20:30 TWEET, ângulo B cliente e conteúdo, CTA = ENVIO
tweet = {"formato": "tweet", "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": f"{R}/assets/avatar-liuri.jpg", "slides": [{"texto": t} for t in [
  "Muito post de pequena empresa é escrito para impressionar os colegas de profissão. O cliente lê, não entende metade das palavras e continua rolando o feed.",
  "A esteticista fala em protocolo e ativos. O mecânico fala em junta do cabeçote. O cliente só quer saber se resolve o problema dele e quanto custa.",
  "Quando eu escrevo o conteúdo de um negócio, começo pelas mensagens que os clientes mandaram no WhatsApp. As palavras do post saem dali, do jeito que eles escrevem.",
  "Pouca gente começa pela palavra técnica. A cliente escreve que a perna incha no fim do dia e quer saber se tem jeito. O post que usa a frase dela é entendido na hora.",
  "O termo técnico tem lugar no slide em que você explica por que o seu método funciona. Na capa, ele afasta quem ainda não conhece você.",
  "Faça o teste com os seus últimos nove posts. Leia cada capa como se fosse um cliente que nunca ouviu falar do seu serviço.",
  "Se ele precisaria perguntar o que a palavra quer dizer, troque a palavra. Se a capa não diz qual problema você resolve, reescreva antes de postar o próximo.",
  "Você não perde autoridade com isso. O cliente continua vendo que você entende do assunto e, agora, entende também o que você vende.",
  "Envie este post para o colega que escreve legenda como se fosse prova de faculdade, e façam o teste das nove capas juntos.\n\nSiga @liurialves: todo dia eu mostro uma parte do funil de uma pequena empresa.",
]]}

LEGENDAS = {
 1: """A ordem em que eu separo o dinheiro de cada venda numa pequena empresa. Você paga a casa e a empresa pela mesma conta?

Quando tudo sai do mesmo lugar, o saldo do fim do mês engana. Parece que sobrou, e o que sobrou era o imposto.

A ordem é simples: tudo o que entra cai na conta da empresa, o imposto vai para uma conta separada no mesmo dia, os custos têm dia marcado e você recebe um salário fixo. O que fica depois disso é lucro.

🔻 Salve este post para montar as quatro contas esta semana com o extrato na mão. Se quiser que eu olhe os números da sua empresa com você, mande CALL no direct.

#gestao #empreendedorismo #negocioproprio #empresario #brasileirosemportugal""",
 2: """Você acha que já passou da hora de mudar de vida?

Eu entrei na Aeronáutica aos 19 porque precisava do salário. Anos depois troquei a farda por um caminho sem salário fixo e recomecei do zero em Lisboa, pelo que eu sabia fazer com as mãos.

A empresa nasceu atendendo de dia e estudando site, anúncio e números à noite.

🔻 Comente 1 se você já recomeçou alguma vez, ou 2 se ainda vai começar.

#empreendedorismo #vidadeempreendedor #brasileirosemportugal #negocioproprio #lisboa""",
 3: """Você escreve post para o cliente ou para os colegas de profissão?

Protocolo, ativos, regime tributário, junta do cabeçote. O cliente não pesquisa assim. Ele escreve no WhatsApp do jeito dele, e é daí que devem sair as palavras do seu conteúdo.

Faça o teste: leia as capas dos seus últimos nove posts como se fosse alguém que nunca ouviu falar do seu serviço. A capa que precisa de tradução não traz cliente.

🔻 Envie este post para o colega que escreve legenda como se fosse prova de faculdade e façam o teste juntos. Se quiser que eu revise o seu perfil, mande CALL no direct.

#marketingdigital #empreendedorismo #vendas #negocioproprio #empresario""",
}


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_formatos.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    run(quadro, O(1)); run(foto, O(2)); run(tweet, O(3)); print("ok")
