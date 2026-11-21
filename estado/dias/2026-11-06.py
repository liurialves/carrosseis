"""Plano 100 mil, semana 2, dia 7 (06/11/2026, sexta). Tarefa do PDF: carrossel de APRESENTAÇÃO + fixar no topo.
Horários: 14:20 (FIXADO), 17:40 (FECHAMENTO), 19:00 (IA; as 12:40 já tinham passado quando a rotina rodou) e 20:30
(apresentação). Sem repost às 22:15: a pasta repost-modocaverna não tem prints.
17:40 QUADRO, ângulo A (dinheiro e gestão), CTA envio, palavra FECHAMENTO (fechamento de sexta).
20:30 FAIXA, ângulo C (vida de quem empreende), CTA comentário, palavra MENTORIA. Carrossel de APRESENTAÇÃO (tarefa do
      dia) e REMODELADO do Reel "Aos guerreiros, segue @liurialves" (buffer 6aeafabbcc5459467928b2a8, 04/11, 1.398 de
      alcance, 31 comentários, 7 guardados: o maior alcance dos últimos 30 dias ainda não replicado). Mudou: Reel de 11 s
      com pedido de seguir virou carrossel de apresentação em 9 slides (quem é, trajetória, o que faz, para quem é,
      o que vai ver no perfil), formato faixa, CTA comentário + seguir, fotos novas.
14:20 BRANCO, ângulo B (cliente e conteúdo), CTA salvar, palavra FIXADO (os 3 posts fixados do perfil).
CTA de todos os posts leva ao link do dono no direct (item 12).
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/3de97be0-9b10-54e4-a03c-47adc178e7b7/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-06"
F = lambda x: f"/tmp/fotos6/{x}.jpg"
P = lambda x: f"/tmp/px6/pexels-{x}.jpg"

# 1) 17:40 QUADRO, ângulo A, CTA = ENVIO (palavra FECHAMENTO)
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "Sexta-feira, fim do expediente. [[Os 4 números que eu confiro antes de fechar a semana]]",
   "desenho": {"tipo": "lista", "check": False, "itens": ["o que entrou", "o que falta receber", "a agenda da semana", "o caixa livre"]},
   "texto": "Para quem tem empresa pequena e só descobre como foi o mês depois que ele acabou."},
  {"etiqueta": "Por que na sexta", "titulo": "No dia 30 já não dá para corrigir o mês",
   "desenho": {"tipo": "numero", "n": 4, "nota": "sextas por mês para corrigir"},
   "texto": "Eu fazia o fechamento só no fim do mês. Quando o número vinha baixo, já não havia tempo para marcar mais cliente nem para cortar gasto. Hoje eu separo quinze minutos toda sexta, antes de desligar o computador.",
   "soco": "Quatro conferências por mês evitam a surpresa no extrato."},
  {"etiqueta": "Número 1 de 4", "titulo": "O que entrou na conta esta semana", "desenho": {"tipo": "numero", "n": 1, "nota": "entrou de verdade"},
   "texto": "Eu olho o extrato do banco, e não a agenda. Serviço feito e ainda não pago fica para o número dois. O valor vai para uma linha da planilha, ao lado das semanas anteriores.",
   "soco": "Venda que não caiu na conta ainda não é dinheiro."},
  {"etiqueta": "Número 2 de 4", "titulo": "O que ainda falta receber", "desenho": {"tipo": "numero", "n": 2, "nota": "com nome e data"},
   "texto": "Cada valor pendente leva o nome do cliente e a data combinada. Se a data já passou, a mensagem de cobrança sai ainda na sexta, com educação, sem deixar para segunda-feira.",
   "soco": "Cobrança esquecida acaba virando desconto."},
  {"etiqueta": "Número 3 de 4", "titulo": "Quantos horários a próxima semana já tem", "desenho": {"tipo": "numero", "n": 3, "nota": "agenda de segunda"},
   "texto": "Se a agenda da semana que vem está com buracos, eu fico sabendo na sexta à tarde e ainda tenho tempo de postar, chamar cliente antigo ou abrir um horário novo. Descobrir na segunda de manhã é tarde.",
   "soco": "A agenda da próxima semana se resolve hoje."},
  {"etiqueta": "Número 4 de 4", "titulo": "Quanto fica no caixa depois das contas fixas", "desenho": {"tipo": "numero", "n": 4, "nota": "o que vence até o dia 30"},
   "texto": "Do saldo eu tiro tudo o que vence até o fim do mês: aluguel, pró-labore, fornecedor e imposto. O que sobra é o dinheiro com que a empresa pode decidir alguma coisa.",
   "soco": "Saldo alto com conta para vencer engana o dono."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3", "4"], "nota": "olhar só o faturamento"},
   "texto": "O dono vê quanto vendeu, gosta do número e fecha o computador. O que falta receber e o que vence na semana seguinte ficam fora da conta até o dia em que o caixa não fecha.",
   "soco": "Faturamento sozinho não mostra se a empresa está bem."},
  {"etiqueta": "Na prática", "titulo": "Uma planilha com quatro colunas e uma linha por semana",
   "desenho": {"tipo": "lista", "check": True, "itens": ["entrou na conta", "falta receber", "horários marcados", "caixa livre", "15 minutos, toda sexta"]},
   "texto": "Depois de um mês você enxerga o padrão: qual semana costuma ser fraca e qual cliente sempre paga atrasado."},
  {"etiqueta": "Próximo passo", "titulo": "Envie para o seu sócio e façam a conta juntos hoje", "desenho": {"tipo": "numero", "n": 4, "nota": "números, 15 minutos"},
   "texto": "Envie este post para quem divide a empresa com você e confiram os quatro números ainda hoje. Se quiser montar esse fechamento comigo, comente FECHAMENTO que eu te mando no direct como funciona a minha mentoria.",
   "soco": "Comece nesta sexta."},
]}

# 2) 20:30 FAIXA, ângulo C, CTA = COMENTÁRIO (palavra MENTORIA). APRESENTAÇÃO + REMODELADO.
apresentacao = {"slides": [
  {"tipo": "foto", "foto": f"{R}/assets/foto-perfil-liuri.jpg", "foco_y": 0.25, "grande": True, "arraste": True,
   "faixa": "SE VOCÊ CHEGOU AGORA,", "texto": "EU SOU O LIURI. ESTE PERFIL É PARA QUEM TEM EMPRESA E QUER CRESCER."},
  {"tipo": "foto", "foto": F("15NSnynFNWlKqZF6ESORv54YM5V7XWI7E"), "foco_y": 0.55,
   "faixa": "QUEM ESCREVE AQUI", "texto": "BRASILEIRO, PAI E MARIDO. MORO EM LISBOA, TREINO MMA E TENHO A MINHA EMPRESA.",
   "destaque": "O QUE EU ENSINO AQUI EU USO NO MEU NEGÓCIO."},
  {"tipo": "foto", "foto": F("1TJmzsycOPx_IL3PyfKvKxM1u7-ePvkht"), "foco_y": 0.4,
   "faixa": "AOS 19 ANOS,", "texto": "ENTREI NA AERONÁUTICA POR NECESSIDADE FINANCEIRA E APRENDI A CUMPRIR HORÁRIO EM DIA RUIM.",
   "destaque": "SAÍ PARA CONSTRUIR ALGO MEU."},
  {"tipo": "foto", "foto": F("1twVqbxoeEiKp96xfrxEo_owVcIJ5FukW"), "foco_y": 0.45,
   "faixa": "EM LISBOA,", "texto": "RECOMECEI SEM NINGUÉM SABER O MEU NOME. DEZ ANOS DE MASSAGEM VIRARAM A LISBOA MASSAGEM.",
   "destaque": "HOJE ELA É PLATAFORMA PARA TERAPEUTAS."},
  {"tipo": "foto", "foto": P(20373333), "foco_y": 0.4,
   "faixa": "O QUE EU FAÇO HOJE", "texto": "AJUDO DONOS DE PEQUENA EMPRESA A CRESCER COM ESTRATÉGIA, FUNIL, CONTEÚDO E DINHEIRO NO CONTROLE.",
   "destaque": "FIZ O SITE DA CAROLWELL E A ESTRATÉGIA DA LB."},
  {"tipo": "foto", "foto": P(12326636), "foco_y": 0.35,
   "faixa": "ESTE PERFIL É PARA VOCÊ", "texto": "SE O SEU NEGÓCIO JÁ VENDE, MAS DEPENDE DE INDICAÇÃO E SÓ VÊ O LUCRO NO FIM DO MÊS.",
   "destaque": "SE AINDA NÃO SABE O QUE VENDER, DECIDA ISSO PRIMEIRO."},
  {"tipo": "foto", "foto": P(6296105), "foco_y": 0.45,
   "faixa": "O QUE VOCÊ VAI VER AQUI", "texto": "DINHEIRO E GESTÃO DA EMPRESA, CLIENTE E CONTEÚDO QUE VENDE, E A ROTINA REAL DE QUEM EMPREENDE COM TREINO E FAMÍLIA."},
  {"tipo": "foto", "foto": F("1vnjQCjXgn4PtXv2s5XrJv8-b9I4Z45jG"), "foco_y": 0.4,
   "faixa": "POR QUE EU FAÇO ISTO", "texto": "A MINHA FAMÍLIA DEPENDE DAS DECISÕES QUE EU TOMO NA EMPRESA.",
   "destaque": "E A SUA, PROVAVELMENTE, TAMBÉM."},
  {"tipo": "branco", "blocos": [
   ["t", "AGORA VOCÊ SABE QUEM EU SOU."], ["esp", 16],
   ["h", "SIGA @LIURIALVES"],
   ["n", "SE VOCÊ TEM EMPRESA E QUER CRESCER COM MÉTODO E NÚMERO NA MÃO."], ["esp", 20],
   ["h", "COMENTE \"MENTORIA\""],
   ["n", "E EU TE MANDO NO DIRECT COMO FUNCIONA O MEU ACOMPANHAMENTO."], ["esp", 20],
   ["n", "E ME CONTE NOS COMENTÁRIOS QUAL É O SEU NEGÓCIO."]]},
]}

# 3) 14:20 BRANCO, ângulo B, CTA = SALVAR (palavra FIXADO)
fixados = {"formato": "branco", "slides": [
  {"etiqueta": "Perfil que vende", "frase": "Os 3 posts que eu fixaria hoje no topo do perfil de [[qualquer pequena empresa]]",
   "texto": "Quem abre o seu perfil pela primeira vez lê esses três antes de qualquer outro. Salve para montar no fim de semana."},
  {"etiqueta": "Por que isso importa", "frase": "O cliente novo [[não rola o seu feed inteiro]]. Ele lê o topo e decide.",
   "texto": "O Instagram deixa fixar até três posts no topo do perfil. Em muitos perfis de empresa que eu abro, esse espaço está vazio ou mostra uma promoção que já acabou faz meses."},
  {"etiqueta": "Fixado 1", "frase": "[[Quem você é]] e para quem você trabalha.",
   "texto": "Um carrossel de apresentação com a sua história em poucas linhas, o serviço que você vende e o tipo de cliente que atende. Eu publiquei o meu hoje e ele vai para o topo."},
  {"etiqueta": "Fixado 2", "frase": "[[Um caso real]], com o que foi feito.",
   "texto": "Escolha um cliente e mostre como estava antes, o que você fez e o que mudou, sem inventar número. No meu perfil entra o site que eu fiz para a Carolwell."},
  {"etiqueta": "Fixado 3", "frase": "[[Como contratar você]], passo a passo.",
   "texto": "Faixa de preço, como marcar, onde você atende e o que acontece no primeiro contato. Quem chegou até esse post já está quase pronto para chamar e só precisa saber como."},
  {"etiqueta": "O erro que eu mais vejo", "frase": "Fixar [[a foto mais bonita]] no lugar do post que explica o negócio.",
   "texto": "A foto bonita ganha curtida de quem já conhece você. O cliente novo precisa entender, em poucos segundos, o que você vende e se aquilo serve para ele."},
  {"etiqueta": "Na prática", "frase": "Revise os três [[uma vez por mês]].",
   "texto": "Troque o caso quando tiver um mais recente e atualize o preço quando ele mudar. Post fixado com informação antiga faz o cliente perguntar no direct o que já devia estar respondido."},
  {"etiqueta": "Para fazer hoje", "frase": "Abra o seu perfil [[como se fosse um cliente]].",
   "texto": "Olhe só a bio e os três primeiros posts. Se em dez segundos não fica claro o que a empresa vende e como contratar, você já sabe por onde começar."},
  {"etiqueta": "Próximo passo", "frase": "Salve este post e [[monte os três até domingo]].",
   "texto": "Se quiser que eu olhe o seu perfil e diga o que fixar, comente FIXADO que eu te mando no direct como funciona a minha mentoria."},
]}

LEGENDAS = {
 1: """Sexta-feira, fim do expediente. Você sabe quanto a sua empresa tem de verdade para a semana que vem?

Eu fazia o fechamento só no fim do mês, quando já não dava para corrigir nada. Hoje são quinze minutos toda sexta, com quatro números: o que entrou na conta, o que falta receber, quantos horários a próxima semana já tem e quanto fica no caixa depois das contas fixas.

Uma planilha com quatro colunas e uma linha por semana. Depois de um mês você enxerga qual semana é fraca e qual cliente sempre atrasa.

🔻 Envie este post para o seu sócio e façam a conta juntos hoje. Se quiser montar esse fechamento comigo, comente FECHAMENTO que eu te mando no direct como funciona a minha mentoria.

#gestao #empresario #empreendedorismo #negocioproprio #financas""",
 2: """Se você chegou agora ao perfil, este post é para você saber com quem está falando.

Eu sou o Liuri: brasileiro, pai e marido, moro em Lisboa e treino MMA. Entrei na Aeronáutica aos 19 por necessidade financeira, saí para construir algo meu e recomecei em Lisboa. Dez anos de massagem viraram a minha empresa, a Lisboa Massagem.

Hoje eu ajudo donos de pequena empresa e autônomos a crescer com estratégia, funil, conteúdo e controle do dinheiro. Aqui você vai ver gestão, cliente e conteúdo que vende, e a rotina real de quem empreende.

🔻 Comente MENTORIA que eu te mando no direct como funciona o meu acompanhamento. E conte aqui embaixo qual é o seu negócio. Siga @liurialves.

#empreendedorismo #empresario #brasileirosemportugal #negocioproprio #vidadeempreendedor""",
 3: """O cliente novo não rola o seu feed inteiro. Ele lê a bio, olha os três posts do topo e decide se chama você.

Os três que eu fixaria hoje no perfil de qualquer pequena empresa: um post de apresentação (quem você é e para quem trabalha), um caso real com o que foi feito e um post que explica como contratar você, com faixa de preço e o primeiro passo.

O erro mais comum é fixar a foto mais bonita no lugar do post que explica o negócio.

🔻 Salve este post e monte os três até domingo. Se quiser que eu olhe o seu perfil, comente FIXADO que eu te mando no direct como funciona a minha mentoria.

#marketingdigital #instagramparanegocios #empreendedorismo #negocioproprio #empresario""",
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
    run(quadro, O(1)); run(apresentacao, O(2), "render_faixa.py"); run(fixados, O(3)); print("ok")
