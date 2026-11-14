"""Plano 100 mil, semana 3, dia 4 (10/11/2026, terça). Dia 4 do "Plano de 30 dias para lançar a mentoria":
conteúdo "Postar todos os dias não faz você vender"; tarefa: enviar a mensagem aos outros 10 contatos.
AJUSTE DO DONO EM 09/11 (noite, vale 10 a 16/11): 3 posts por dia, sem post de IA (12:40) e sem 22:15.
14:20 CONEXÃO molde vencedor · 17:40 VALOR (dia par = capa A: faixa com foto do Liuri + cena) · 20:30 CONEXÃO molde vencedor (terça).
CTA (rodízio a partir de 09/11: comentário/salvar/envio): 14:20 envio, 17:40 comentário, 20:30 salvar; todos terminam em "Comente CLIENTES".
14:20 FAIXA, conexão, pilar 5. REMODELADO do 2º carrossel com mais alcance em 30 dias e ainda não replicado
      (buffer 6af14d27e29b1359f0cbde77, "Antes de qualquer empresa, eu e a minha namorada testamos 4 jeitos...", 09/11 14:20,
      518 de alcance, 1.383 views, 5 envios). Mantém: faixa, foto real, 1ª pessoa, lição com ação. Muda: trecho (parte 1,
      itens 6 a 8 + parte 2, item 10: alistamento, 13º no teste físico, quarentena, farda, noivado na formatura), fotos da
      Aeronáutica (Drive 40, 41, 42, 11, 13, 26), lição de concorrência e CTA de envio.
17:40 FAIXA, valor, pilar 3, capa A: plano mensal no lugar da aula avulsa (personal, academia, fisioterapia).
20:30 FAIXA, conexão, pilar 5 (lição do pilar 4): a loja de moda praia que quebrou por misturar a conta da empresa com a de casa
      (parte 2, itens 12 e 13a). Fotos Drive 05, 60, 58, 66 + Pexels 32797410 e 16723181 (sem rosto).
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/f135a8c9-526f-56ae-b839-cb3820169cf3/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-10"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h10/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px10/pexels-{x}.jpg"

# 1) 14:20 FAIXA, CONEXÃO, CTA = ENVIO + CLIENTES. REMODELADO.
aero = {"slides": [
  {"tipo": "foto", "foto": HP("40"), "foco_y": 0.15, "grande": True, "arraste": True, "faixa": "AOS 18 ANOS",
   "texto": "FIQUEI EM 13º NO TESTE FÍSICO DA AERONÁUTICA. ALI EU APRENDI A SER ESCOLHIDO."},
  {"tipo": "foto", "foto": HP("41"), "foco_y": 0.2, "faixa": "ANTES DO ALISTAMENTO",
   "texto": "EU DISSE À MINHA NAMORADA: VOU SER ESCOLHIDO, VOU ESTAR ENTRE OS MELHORES E A GENTE VAI MUDAR DE VIDA."},
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.35, "faixa": "O TESTE FÍSICO",
   "texto": "PASSEI COMO O 13º MELHOR. DEPOIS VIERAM OS EXAMES MÉDICOS, E EU ENTREI.",
   "destaque": "A VAGA ERA DISPUTADA. EU ME PREPAREI PARA ISSO."},
  {"tipo": "foto", "foto": HP("11"), "foco_y": 0.15, "faixa": "A QUARENTENA",
   "texto": "40 A 45 DIAS LONGE DA FAMÍLIA. EU OLHAVA PARA FORA DO MURO COM SAUDADE DE ANDAR DE ÔNIBUS."},
  {"tipo": "foto", "foto": HP("13"), "foco_y": 0.3, "faixa": "A FARDA",
   "texto": "GRITO, CORRERIA, CAMA PERFEITA, BOTA ENGRAXADA E BARBA FEITA TODO DIA. FOI ALI QUE EU APRENDI DISCIPLINA."},
  {"tipo": "foto", "foto": HP("26"), "foco_y": 0.25, "faixa": "NA FORMATURA",
   "texto": "PEDI A MINHA NAMORADA EM CASAMENTO. FIZERAM UMA ALA QUE É SÓ PARA OFICIAL GENERAL, E EU QUASE FIQUEI PRESO 4 DIAS.",
   "destaque": "SAÍ COM UMA REPREENSÃO VERBAL E UMA NOIVA."},
  {"tipo": "branco", "blocos": [
   ["t", "O SEU CLIENTE TAMBÉM FAZ UM TESTE: ELE COMPARA VOCÊ COM OUTROS ANTES DE ESCOLHER. FAÇA HOJE O TESTE QUE ELE FAZ:"], ["esp", 10],
   ["h", "1. ESCREVA PARA 3 CONCORRENTES"],
   ["n", "Como se fosse cliente: \"quanto custa o acompanhamento?\". Anote quem respondeu e em quanto tempo."],
   ["h", "2. COMPARE COM VOCÊ"],
   ["n", "Tempo de resposta, se perguntou o seu objetivo, se mandou um plano só e se marcou horário."],
   ["h", "3. CORRIJA 1 COISA EM 7 DIAS"],
   ["n", "A que te deixa atrás. Exemplo: responder em até 15 minutos."]]},
  {"tipo": "foto", "foto": FL("home-office-headset"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E TE MOSTRO ONDE O SEU NEGÓCIO PERDE NA COMPARAÇÃO.",
   "destaque": "E ENVIE PARA QUEM ESTÁ PARADO NO MESMO FATURAMENTO."},
]}

# 2) 17:40 FAIXA, VALOR, CAPA A, CTA = COMENTÁRIO + CLIENTES
plano = {"slides": [
  {"tipo": "foto", "foto": HP("78"), "foco_y": 0.12, "grande": True, "arraste": True, "faixa": "PERSONAL, ACADEMIA, FISIO",
   "texto": "PARE DE VENDER AULA AVULSA. MONTE O PLANO MENSAL EM 4 PASSOS."},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.3, "faixa": "O QUE EU VI NA MASSAGEM",
   "texto": "O CLIENTE QUE MAIS ME PAGA NÃO COMPRA SESSÃO SOLTA. PAGA CERCA DE 300 € POR MÊS E VEM 2 A 3 VEZES POR SEMANA.",
   "destaque": "ELE NÃO COMPRA PELO PREÇO."},
  {"tipo": "branco", "blocos": [
   ["h", "QUEM VENDE AVULSO COMEÇA O MÊS DO ZERO"], ["esp", 8],
   ["n", "Cada aula é uma venda nova. O aluno some duas semanas e o seu faturamento cai junto."],
   ["n", "Com o plano mensal, a mesma agenda vira receita que você sabe no dia 1 quanto vai entrar."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 1"], ["h", "LISTE QUEM JÁ VEM TODA SEMANA"], ["esp", 8],
   ["n", "Abra a agenda dos últimos 30 dias e marque quem veio 4 vezes ou mais."],
   ["n", "Essas pessoas já compram como mensalistas. Só ainda não pagam como mensalistas."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 2"], ["h", "MONTE UM PLANO SÓ"], ["esp", 8],
   ["n", "Frequência fixa, o que inclui e o valor por mês."],
   ["n", "Exemplo (números ilustrativos): aula avulsa a 35 €. Duas vezes por semana dá 8 aulas, 280 €. Plano mensal: 249 €, com avaliação no início do mês."]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 3"], ["h", "OFEREÇA COM ESTA MENSAGEM"], ["esp", 8],
   ["n", "\"[Nome], você veio [8] vezes este mês. Montei um plano para quem treina com essa frequência: [2x por semana] por [249 €] por mês, com [avaliação mensal]. Reservo os seus horários fixos a partir do dia 1?\""]]},
  {"tipo": "branco", "blocos": [
   ["t", "PASSO 4"], ["h", "COBRE NO MESMO DIA"], ["esp", 8],
   ["n", "Pagamento no dia 1, por transferência ou débito. Regra escrita: falta sem aviso de 24 h não é reposta."],
   ["h", "NA PRÁTICA"],
   ["n", "Mande a mensagem hoje para 5 alunos. Daqui a 7 dias, conte quantos fecharam."]]},
  {"tipo": "foto", "foto": FL("video-rotina-17s"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E TE AJUDO A MONTAR O PLANO MENSAL DO SEU NEGÓCIO.",
   "destaque": "FATURAMENTO PARADO COMEÇA A ANDAR QUANDO A RECEITA SE REPETE."},
]}

# 3) 20:30 FAIXA, CONEXÃO, CTA = SALVAR + CLIENTES
loja = {"slides": [
  {"tipo": "foto", "foto": HP("05"), "foco_y": 0.3, "grande": True, "arraste": True, "faixa": "NO TEMPO DE MILITAR",
   "texto": "EU JÁ QUEBREI UMA LOJA POR MISTURAR A CONTA DA EMPRESA COM A DE CASA."},
  {"tipo": "foto", "foto": HP("60"), "foco_y": 0.25, "faixa": "O COMEÇO",
   "texto": "AINDA NA AERONÁUTICA, ABRI UMA LOJA DE MODA PRAIA NO BRASIL. INVESTI CERCA DE 10 A 12 MIL REAIS."},
  {"tipo": "foto", "foto": P(32797410), "foco_y": 0.4, "faixa": "O PRIMEIRO PROBLEMA",
   "texto": "MODA PRAIA É SAZONAL. VENDE BEM NUMA ÉPOCA DO ANO E POUCO NO RESTO DELE."},
  {"tipo": "foto", "foto": HP("58"), "foco_y": 0.15, "faixa": "O ERRO QUE EU COMETI",
   "texto": "JUNTEI A CONTA DA LOJA COM A MINHA CONTA PESSOAL. O DINHEIRO DA LOJA PAGAVA VIAGEM E CONTA DE CASA.",
   "destaque": "NA CONTA MISTURADA, EU NÃO VIA O PREJUÍZO."},
  {"tipo": "foto", "foto": P(16723181), "foco_y": 0.4, "faixa": "VEIO A COVID",
   "texto": "SEM RESERVA PARA O MÊS RUIM E COM O CAIXA GASTO EM CASA, A LOJA QUEBROU."},
  {"tipo": "foto", "foto": HP("66"), "foco_y": 0.45, "faixa": "DEPOIS",
   "texto": "SAÍ DA AERONÁUTICA, FIZ UBER NO BRASIL E VIM PARA PORTUGAL. ESSE ERRO EU CORRIGI E NÃO REPITO."},
  {"tipo": "branco", "blocos": [
   ["t", "SE O DINHEIRO DA EMPRESA E O DE CASA ESTÃO NA MESMA CONTA, FAÇA ISTO ESTA SEMANA:"], ["esp", 10],
   ["h", "1. ABRA UMA CONTA SÓ DA EMPRESA"],
   ["n", "Todo pagamento de cliente entra lá. Nenhuma conta de casa sai de lá."],
   ["h", "2. DEFINA O SEU SALÁRIO"],
   ["n", "Valor fixo, no mesmo dia do mês. Exemplo: 1.200 € no dia 5. Fora isso, não mexe."],
   ["h", "3. GUARDE 10% DE CADA ENTRADA"],
   ["n", "Todo negócio tem mês fraco. O mês bom paga o mês ruim."]]},
  {"tipo": "foto", "foto": FL("video-rotina-9s"), "foco_y": 0.3, "faixa": "SALVE E FAÇA ESTA SEMANA",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT PARA OLHAR OS NÚMEROS DO SEU NEGÓCIO.",
   "destaque": "EU APRENDI ISSO QUEBRANDO UMA LOJA. VOCÊ PODE APRENDER AQUI."},
]}

LEGENDAS = {
 1: """Aos 18 anos fiquei em 13º no teste físico da Aeronáutica. Ali eu aprendi a ser escolhido.

Antes do alistamento eu disse à minha namorada: "Vou ser escolhido, vou estar entre os melhores e a gente vai mudar de vida." Passei como o 13º melhor, passei nos exames médicos e entrei. Vieram 40 a 45 dias de quarentena longe da família, olhando para fora do muro com saudade de andar de ônibus. Depois, grito, correria, cama perfeita e barba feita todo dia. Na formatura, pedi a minha namorada em casamento. Fizeram uma ala que é só para oficial general e eu quase fiquei preso 4 dias. Saí com uma repreensão verbal e uma noiva.

O seu cliente também faz um teste: antes de fechar, ele compara você com outros. Faça hoje o teste que ele faz. Escreva para 3 concorrentes como se fosse cliente, compare o tempo de resposta e o atendimento com o seu e corrija 1 coisa em 7 dias.

🔻 Envie para quem está parado no mesmo faturamento. E comente CLIENTES que eu te chamo no direct e te mostro onde o seu negócio perde na comparação.

Fotos da formatura: Robério Castro Fotografia.

#empreendedorismo #donodenegocio #personaltrainer #historiareal #aeronautica""",
 2: """Pare de vender aula avulsa. Quem vende avulso começa o mês do zero.

Na massagem, o cliente que mais me paga não compra sessão solta: paga cerca de 300 € por mês e vem 2 a 3 vezes por semana. Ele não compra pelo preço.

O plano mensal em 4 passos, para personal trainer, academia e fisioterapia:
1. Liste quem veio 4 vezes ou mais nos últimos 30 dias.
2. Monte um plano só: frequência fixa, o que inclui e o valor por mês (exemplo ilustrativo no slide 5).
3. Ofereça com a mensagem do slide 6.
4. Cobre no mesmo dia, todo mês, com regra de falta escrita.

Mande a mensagem hoje para 5 alunos e conte, daqui a 7 dias, quantos fecharam.

🔻 Comente CLIENTES que eu te chamo no direct e te ajudo a montar o plano mensal do seu negócio.

#personaltrainer #fisioterapia #academia #donodenegocio #planomensal""",
 3: """Eu já quebrei uma loja por misturar a conta da empresa com a de casa.

Ainda na Aeronáutica, abri uma loja de moda praia no Brasil e investi cerca de 10 a 12 mil reais. Moda praia é sazonal. E eu cometi o erro: juntei a conta da loja com a minha conta pessoal. O dinheiro da loja pagava viagem e conta de casa, e na conta misturada eu não via o prejuízo. Veio a Covid e a loja quebrou. Esse erro eu corrigi e não repito.

Se o dinheiro da sua empresa e o de casa estão na mesma conta, faça isto esta semana:
1. Abra uma conta só da empresa. Todo pagamento de cliente entra lá.
2. Defina o seu salário: valor fixo, no mesmo dia do mês.
3. Guarde 10% de cada entrada para o mês fraco.

🔻 Salve e faça esta semana. E comente CLIENTES que eu te chamo no direct para olhar os números do seu negócio.

#empreendedorismo #gestaofinanceira #donodenegocio #personaltrainer #barbearia""",
}


def run(cfg, out, script="render_faixa.py"):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/{script}", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    for n in (1, 2, 3):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(aero, O(1)); run(plano, O(2)); run(loja, O(3))
    print("ok")
