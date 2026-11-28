"""10/11/2026, pedido do dono no chat depois da rotina: "completar com mais dois, de conexão".
Dois carrosséis extra no molde vencedor (faixa + foto real + história + lição + CLIENTES), nos horários livres desta semana:
12:40 (liurialves-4) CONEXÃO, pilar 5: "Aos 17 anos eu disse a ela: tudo o que eu quero, eu conquisto" (parte 1, item 1;
      parte 2, itens 11 e 22). Lição: meta com número e prazo → clientes por semana. CTA comentário.
22:15 (liurialves-5) CONEXÃO, pilar 5: dez anos de massagem parados ("Cuidados" + item 20). Lição: o serviço que o dono
      já sabe fazer e não oferece. CTA envio.
Fotos: Drive fotos/historia-portugal 48, 20, 63, 04 (filho: post de família, nunca capa), 71, 72, 70, 09, 67, 68 + fotos-liuri.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/f135a8c9-526f-56ae-b839-cb3820169cf3/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-10"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h10b/{x}.jpg"

meta = {"slides": [
  {"tipo": "foto", "foto": HP("48"), "foco_y": 0.1, "grande": True, "arraste": True, "faixa": "COMO EU CONHECI A MINHA ESPOSA",
   "texto": "AOS 17 ANOS EU DISSE A ELA: TUDO O QUE EU QUERO, EU CONQUISTO."},
  {"tipo": "foto", "foto": HP("20"), "foco_y": 0.2, "faixa": "ELA NÃO QUERIA NAMORAR",
   "texto": "ELA É 2 ANOS MAIS VELHA. PERGUNTOU: TIPO O QUÊ? EU RESPONDI: TIPO VOCÊ. ELA RIU E DISSE QUE GOSTAVA DE MIM SÓ COMO AMIGO.",
   "destaque": "TRÊS MESES DEPOIS, A GENTE ESTAVA NAMORANDO."},
  {"tipo": "foto", "foto": HP("63"), "foco_y": 0.15, "faixa": "O CASAMENTO",
   "texto": "UM ANO DE NAMORO, UM ANO DE NOIVADO. CASAMOS UM ANO DEPOIS DA MINHA FORMATURA NA AERONÁUTICA."},
  {"tipo": "foto", "foto": HP("04"), "foco_y": 0.15, "faixa": "UM ANO DEPOIS",
   "texto": "VEIO O PRIMEIRO FILHO. A FRASE CONTINUOU A MESMA."},
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.3, "faixa": "A META DE AGORA",
   "texto": "EU CREIO QUE AINDA EM 2027 VOU FATURAR 100 MIL EUROS POR MÊS. EU DIGO ISSO EM VOZ ALTA, COMO DISSE A ELA AOS 17."},
  {"tipo": "branco", "blocos": [
   ["t", "TUDO COMEÇA COM UMA DECISÃO DITA EM VOZ ALTA, COM NÚMERO E PRAZO. FAÇA A SUA HOJE:"], ["esp", 10],
   ["h", "1. ESCREVA O NÚMERO"],
   ["n", "Quanto a empresa vai faturar por mês daqui a 90 dias. Exemplo: de 2.500 € para 4.000 €."],
   ["h", "2. DIVIDA PELO SEU TICKET"],
   ["n", "Exemplo: 4.000 € a 80 € por cliente = 50 clientes no mês, cerca de 12 por semana."],
   ["h", "3. DIGA A ALGUÉM"],
   ["n", "Para o sócio, a esposa ou um amigo. Meta dita em voz alta vira cobrança."]]},
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.3, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E A GENTE TRANSFORMA O SEU NÚMERO EM CLIENTES POR SEMANA.",
   "destaque": "QUEM NÃO DECIDE O NÚMERO ACEITA O QUE VIER."},
]}

massagem = {"slides": [
  {"tipo": "foto", "foto": HP("70"), "foco_y": 0.2, "grande": True, "arraste": True, "faixa": "DEZ ANOS DE MASSAGEM",
   "texto": "O MEU MELHOR SERVIÇO FICOU ANOS PARADO. SÓ EM 2026 EU VOLTEI A ELE."},
  {"tipo": "foto", "foto": HP("09"), "foco_y": 0.4, "faixa": "EM 2017, NO BRASIL",
   "texto": "JUNTO COM A AERONÁUTICA, FIZ O CURSO DE MASSAGEM E TRABALHEI UM TEMPO NUMA CLÍNICA."},
  {"tipo": "foto", "foto": HP("67"), "foco_y": 0.35, "faixa": "EM PORTUGAL",
   "texto": "RECOMECEI EM RESTAURANTE, CLUBE E UBER. A MASSAGEM FICOU DE LADO."},
  {"tipo": "foto", "foto": FL("video-rotina-1s"), "foco_y": 0.3, "faixa": "EM CASA",
   "texto": "A MINHA ESPOSA DIZIA QUE EU DEVIA TER COMEÇADO ANTES.",
   "destaque": "A HABILIDADE ESTAVA COMIGO HÁ ANOS."},
  {"tipo": "foto", "foto": FL("selfie-jaqueta-verde"), "foco_y": 0.25, "faixa": "EM 2026",
   "texto": "VOLTEI À MASSAGEM E COMECEI A CRIAR SITES PARA CLIENTES. O FATURAMENTO SAIU DE 1.500 € PARA 7.000 € POR MÊS."},
  {"tipo": "branco", "blocos": [
   ["t", "MUITO DONO PARADO NO MESMO FATURAMENTO JÁ TEM O SERVIÇO QUE VENDE MELHOR E NÃO OFERECE. ACHE O SEU HOJE:"], ["esp", 10],
   ["h", "1. LISTE O QUE VOCÊ NÃO ANUNCIA"],
   ["n", "Tudo o que você sabe fazer e não está na bio. Exemplo no personal: avaliação postural, treino em dupla, preparação para corrida."],
   ["h", "2. ESCOLHA 1 QUE JÁ PEDIRAM"],
   ["n", "Se um cliente já perguntou, existe procura."],
   ["h", "3. OFEREÇA A 10 CLIENTES"],
   ["n", "Esta semana, uma mensagem por pessoa, com o valor e dois horários."]]},
  {"tipo": "foto", "foto": HP("68"), "foco_y": 0.45, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E TE AJUDO A PÔR ESSE SERVIÇO NA FRENTE.",
   "destaque": "E ENVIE PARA QUEM TEM UM TALENTO PARADO."},
]}

LEGENDAS = {
 4: """Aos 17 anos eu disse a ela: "Tudo o que eu quero, eu conquisto."

Ela é 2 anos mais velha e não queria namorar. Perguntou: "Tipo o quê?" Eu respondi: "Tipo você." Ela riu e disse que gostava de mim só como amigo. Três meses depois, a gente estava namorando. Um ano de namoro, um ano de noivado, e casamos um ano depois da minha formatura na Aeronáutica. Um ano depois, veio o primeiro filho.

A frase continua a mesma. Hoje a minha meta é faturar 100 mil euros por mês ainda em 2027, e eu digo isso em voz alta.

Para quem está parado no mesmo faturamento: escreva hoje quanto a empresa vai faturar por mês daqui a 90 dias, divida pelo valor médio de cada cliente para saber quantos clientes precisa por semana, e diga esse número a alguém.

🔻 Comente CLIENTES que eu te chamo no direct e a gente transforma o seu número em clientes por semana.

#empreendedorismo #donodenegocio #historiareal #metas #familia""",
 5: """O meu melhor serviço ficou anos parado.

Em 2017, junto com a Aeronáutica, fiz o curso de massagem e trabalhei um tempo numa clínica. Em Portugal recomecei em restaurante, clube e Uber, e a massagem ficou de lado. A minha esposa dizia que eu devia ter começado antes. Em 2026 voltei à massagem, comecei a criar sites para clientes, e o faturamento saiu de 1.500 € para 7.000 € por mês.

Muito dono parado no mesmo faturamento já tem o serviço que vende melhor e não oferece. Liste o que você sabe fazer e não anuncia, escolha um que algum cliente já pediu e ofereça a 10 clientes esta semana, com o valor e dois horários.

🔻 Envie para quem tem um talento parado. E comente CLIENTES que eu te chamo no direct e te ajudo a pôr esse serviço na frente.

#empreendedorismo #donodenegocio #personaltrainer #historiareal #massagem""",
}


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_faixa.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    for n in (4, 5):
        if os.path.isdir(O(n)):
            for f in os.listdir(O(n)): os.remove(os.path.join(O(n), f))
    run(meta, O(4)); run(massagem, O(5))
    print("ok")
