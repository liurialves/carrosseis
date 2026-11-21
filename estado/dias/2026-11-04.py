"""Plano 100 mil, semana 2, dia 5 (04/11/2026, quarta). LOTE DE RECUPERAÇÃO: a rotina de 03/11 e 04/11 não rodou
(limite de uso), o Buffer ficou vazio e o perfil passou dois dias sem carrossel. O dono pediu em 04/11 para publicar
tudo o que estava atrasado, um por um.
Horários usados (os de 12:40 e 14:20 já tinham passado): 17:40, 19:00 (IA), 20:30 e 22:15.
Sem repost do @modocaverna: a pasta repost-modocaverna do Drive está vazia (item 11 do playbook: sem prints, sem repost).
CTA de todos os posts leva ao link do dono no direct (item 12), nunca a link de ferramenta.
Remodelado: o Reel do próprio dono de 03/11 "Você não tem medo de errar, tem medo de parecer fraco" (buffer
6ae9314fa7cfc3fe3c3f528f) vira carrossel fotofrase. Os dois posts com mais alcance da semana eram só "Segue
@liurialves", sem tema para remodelar.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/a82b3699-a12b-52b3-8a6b-6c577fd56db7/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-04"
F = lambda x: f"/tmp/fotos/{x}.jpg"
PX = lambda x: f"/tmp/px4/pexels-{x}.jpg"

# 1) 17:40 BRANCO, ângulo A dinheiro e gestão, CTA = SALVAR (palavra RESERVA)
branco = {"formato": "branco", "slides": [
  {"etiqueta": "Reserva da empresa", "frase": "O mês fechou bem. [[Antes de reinvestir, separe a reserva.]]",
   "texto": "Como eu monto a reserva de uma pequena empresa, em quatro passos que cabem numa semana. Salve para aplicar."},
  {"etiqueta": "O problema", "frase": "Negócio pequeno quebra [[no mês fraco]], não no mês ruim de vendas.",
   "texto": "O mês fraco chega sempre: cliente que adia, verão parado, obra na rua, uma gripe que tira você de circulação por dez dias. Sem reserva, esse mês vira dívida."},
  {"etiqueta": "Passo 1", "frase": "Descubra o seu [[custo fixo mensal]].",
   "texto": "Some tudo o que sai mesmo sem vender nada: aluguel, contador, sistema, telefone, seguro e o seu salário. Esse número é a sua medida, e não o faturamento."},
  {"etiqueta": "Passo 2", "frase": "A meta são [[três meses de custo fixo]].",
   "texto": "Três meses dão tempo de ajustar preço, procurar cliente ou mudar o serviço sem precisar aceitar o primeiro trabalho mal pago que aparecer. Se hoje parece longe, comece com um mês."},
  {"etiqueta": "Passo 3", "frase": "Separe [[na entrada]], nunca no que sobrar.",
   "texto": "No dia em que o dinheiro cai, uma parte vai para uma conta que você não movimenta. Dez por cento já constrói. O que sobra no fim do mês nunca sobra."},
  {"etiqueta": "Passo 4", "frase": "A reserva fica [[fora do alcance do cartão]].",
   "texto": "Outra conta, de preferência em outro banco, sem cartão e sem o aplicativo na primeira tela do celular. Dinheiro fácil de mexer não é reserva, é saldo."},
  {"etiqueta": "O erro que eu mais vejo", "frase": "Reinvestir tudo porque [[o mês foi bom]].",
   "texto": "Entra um valor acima da média e no mesmo dia o dono compra equipamento, contrata alguém ou aumenta a verba de anúncio. Dois meses depois o custo fixo subiu e a reserva continua em zero."},
  {"etiqueta": "Na prática", "frase": "Esta semana: [[abra a conta e faça a primeira transferência]].",
   "texto": "Pegue o extrato, some o custo fixo, abra a segunda conta e transfira a primeira parcela hoje, nem que seja pequena. O valor importa menos do que começar a rotina."},
  {"etiqueta": "Próximo passo", "frase": "Salve este post e [[faça a conta com o seu extrato na mão]].",
   "texto": "Se você quer montar esse plano comigo, olhando os números da sua empresa, comente RESERVA que eu te mando no direct como funciona a minha mentoria."},
]}

# 2) 20:30 FOTOFRASE, ângulo C vida de quem empreende, CTA = COMENTÁRIO. REMODELADO.
foto = {"formato": "fotofrase", "slides": [
  {"foto": PX(40671295), "foco_y": 0.3, "texto": "Você não tem medo de errar. **Você tem medo de alguém ver que você errou.**"},
  {"foto": PX(4460015), "foco_y": 0.35, "texto": "Eu levei anos para entender isso. No tatame o erro aparece na hora e todo mundo vê. **Foi lá que eu parei de me importar com a plateia.**"},
  {"foto": PX(3680661), "foco_y": 0.3, "texto": "Na empresa é igual. O anúncio que não deu retorno, o preço errado, o cliente que foi embora. **Dói mais quando alguém de fora comenta.**"},
  {"foto": PX(5913599), "foco_y": 0.3, "texto": "Só que o erro escondido custa mais caro. **Ele continua acontecendo porque ninguém pode olhar e dizer onde está o problema.**"},
  {"foto": PX(13732745), "foco_y": 0.35, "texto": "Quando eu comecei a mostrar número e processo para quem entende, o conserto passou a levar dias em vez de meses."},
  {"foto": PX(29992451), "foco_y": 0.3, "texto": "Homem que empreende aprende a separar duas coisas: **errar é parte do trabalho, repetir o mesmo erro é escolha.**"},
  {"foto": PX(13703544), "foco_y": 0.35, "texto": "A conta do orgulho aparece no fim do ano. **Não no dia em que você preferiu não perguntar.**"},
  {"foto": PX(14262893), "foco_y": 0.3, "texto": "Hoje eu trato erro como relatório. **Anoto o que fiz, o que deu, e o que muda na próxima.**"},
  {"foto": PX(3266372), "foco_y": 0.32, "texto": "Comente 1 se você já escondeu um erro no seu negócio, ou 2 se você aprendeu a mostrar. **Eu respondo um por um.**"},
]}

# 3) 22:15 QUADRO, ângulo B cliente e conteúdo, CTA = ENVIO (palavra VENDA)
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "O que eu respondo quando o cliente diz [[vou pensar]]",
   "desenho": {"tipo": "funil", "camadas": ["mensagem", "orçamento", "vou pensar", "silêncio", "venda perdida"], "lado": "onde trava"},
   "texto": "Para quem vende serviço pelo WhatsApp e vê a conversa morrer logo depois do preço."},
  {"etiqueta": "O problema", "titulo": "Vou pensar quase nunca é sobre pensar", "desenho": {"tipo": "circulos", "rotulos": ["dúvida", "valor", "momento"], "centro": "VOU PENSAR"},
   "texto": "Na maioria das vezes falta uma informação que você não deu, ou a pessoa não entendeu o que recebe por aquele valor. Ela não vai perguntar de novo.",
   "soco": "Quem entende o que está comprando responde na hora."},
  {"etiqueta": "Resposta 1 de 4", "titulo": "Pergunte o que ficou em aberto", "desenho": {"tipo": "numero", "n": 1, "nota": "sem pressionar"},
   "texto": "Escreva assim: claro, só para eu te ajudar melhor, ficou alguma dúvida sobre o que está incluído ou sobre o prazo? A pessoa costuma dizer exatamente o que travou.",
   "soco": "A objeção aparece quando você abre espaço para ela."},
  {"etiqueta": "Resposta 2 de 4", "titulo": "Confirme o que ela leva", "desenho": {"tipo": "numero", "n": 2, "nota": "em três linhas"},
   "texto": "Repita em três linhas o que está incluído, o prazo e a forma de pagamento. Orçamento comprido no WhatsApp não é lido até o fim.",
   "soco": "Proposta que cabe na tela é proposta que é lida."},
  {"etiqueta": "Resposta 3 de 4", "titulo": "Dê uma data, não uma cobrança", "desenho": {"tipo": "numero", "n": 3, "nota": "data concreta"},
   "texto": "Eu consigo começar na quinta. Se você me confirmar até amanhã, eu seguro esse horário para você. Prazo real organiza a decisão sem empurrar ninguém.",
   "soco": "Agenda organizada convence mais do que desconto."},
  {"etiqueta": "Resposta 4 de 4", "titulo": "Marque o retorno antes de encerrar", "desenho": {"tipo": "numero", "n": 4, "nota": "no calendário"},
   "texto": "Posso te chamar na sexta para saber? Quem responde que sim continua interessado. Quem não responde já te deu a resposta e libera o seu tempo.",
   "soco": "Conversa sem data de volta some."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3", "4"], "nota": "mandar o preço e sumir"},
   "texto": "O dono envia o valor, não pergunta nada e fica esperando. Depois conclui que o mercado está caro. O que faltou foi conversa, não desconto.",
   "soco": "Preço sem contexto vira comparação."},
  {"etiqueta": "Na prática", "titulo": "Deixe as quatro respostas salvas", "desenho": {"tipo": "lista", "check": True, "itens": ["pergunta aberta", "o que ela leva", "data real", "retorno marcado", "nada de desconto"]},
   "texto": "No WhatsApp Business, salve cada uma como resposta rápida. Você para de improvisar justamente no momento que decide a venda."},
  {"etiqueta": "Próximo passo", "titulo": "Envie para quem atende o seu WhatsApp", "desenho": {"tipo": "numero", "n": 4, "nota": "respostas prontas"},
   "texto": "Envie este post para o seu sócio ou para quem responde o cliente no seu negócio. Se você quer esse roteiro montado para a sua oferta, comente VENDA que eu te mando no direct como funciona a minha mentoria.",
   "soco": "Comece pela pergunta aberta, ainda hoje."},
]}

LEGENDAS = {
 1: """O mês fechou bem e você já está pensando onde reinvestir. Antes disso, separe a reserva da empresa.

Negócio pequeno raramente quebra por um mês ruim de vendas. Quebra no mês fraco que chega sem aviso, com a conta de sempre para pagar.

Os quatro passos: descubra o seu custo fixo, defina a meta de três meses, separe na entrada e não no que sobrar, e deixe a reserva em outra conta, longe do cartão.

🔻 Salve este post e faça a conta com o seu extrato na mão. Se quiser montar esse plano comigo, comente RESERVA que eu te mando no direct como funciona a minha mentoria.

#gestao #empresario #empreendedorismo #negocioproprio #brasileirosemportugal""",
 2: """Você não tem medo de errar. Tem medo de alguém ver que você errou.

No tatame o erro aparece na hora e todo mundo vê. Foi lá que eu parei de me importar com a plateia. Na empresa é igual: o anúncio que não deu retorno, o preço errado, o cliente que foi embora.

O problema é que erro escondido continua acontecendo, porque ninguém pode olhar e dizer onde está o furo. Errar é parte do trabalho. Repetir o mesmo erro é escolha.

🔻 Comente 1 se você já escondeu um erro no seu negócio, ou 2 se você aprendeu a mostrar. Eu respondo um por um.

#vidadeempreendedor #empreendedorismo #negocioproprio #mma #brasileirosemportugal""",
 3: """O cliente pediu o orçamento, você mandou, e veio o vou pensar. O que você responde depois disso decide a venda.

Vou pensar quase nunca é sobre pensar. Falta uma informação que você não deu, ou a pessoa não entendeu o que recebe por aquele valor.

As quatro respostas que eu uso: pergunta aberta sobre o que ficou em dúvida, confirmação em três linhas do que ela leva, uma data real de começo e o retorno marcado antes de encerrar a conversa.

🔻 Envie este post para quem atende o WhatsApp do seu negócio. Se quiser esse roteiro montado para a sua oferta, comente VENDA que eu te mando no direct como funciona a minha mentoria.

#vendas #marketingdigital #empreendedorismo #negocioproprio #empresario""",
}


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_formatos.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    run(branco, O(1)); run(foto, O(2)); run(quadro, O(3)); print("ok")
