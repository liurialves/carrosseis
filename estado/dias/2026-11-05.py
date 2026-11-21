"""Plano 100 mil, semana 2, dia 6 (05/11/2026, quinta). Tarefa do PDF: conta profissional, categoria e contato.
14:20 QUADRO, ângulo B (cliente e conteúdo), CTA envio, palavra PERFIL (liga com a tarefa do dia).
17:40 TWEET, ângulo A (dinheiro e gestão), CTA comentário, palavra SALÁRIO (pró-labore).
20:30 CAPA + ESCURO, ângulo C (vida de quem empreende), CTA salvar, palavra FORTE. REMODELADO do Reel do dono
      "Seja forte guerreiro" (buffer 6ae39df1d1cb43e9ed0c79f6, 29/10, 1.410 de alcance e 120 comentários, o maior
      alcance dos últimos 30 dias que ainda não tinha sido replicado). Mudou: Reel de 9 s virou carrossel de história
      em 5 momentos (Aeronáutica, Lisboa, atendimento, MMA, família), gancho novo, CTA salvar, foto nova.
Sem repost do @modocaverna: a pasta repost-modocaverna está vazia.
CTA de todos os posts leva ao link do dono no direct (item 12).
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/3ad2a2f4-1f39-5a28-8d68-94cb43b73f16/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-05"
F = lambda x: f"/tmp/fotos2/{x}.jpg"

# 1) 14:20 QUADRO, ângulo B, CTA = ENVIO (palavra PERFIL)
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "O cliente achou o seu perfil. [[Estes 4 ajustes decidem se ele chama você]]",
   "desenho": {"tipo": "lista", "check": False, "itens": ["conta profissional", "categoria", "botão de contato", "um link só"]},
   "texto": "Para quem tem empresa e ainda usa o Instagram como se fosse perfil pessoal."},
  {"etiqueta": "O problema", "titulo": "Perfil sem botão de contato perde cliente toda semana",
   "desenho": {"tipo": "funil", "camadas": ["viu o post", "abriu o perfil", "procurou o contato", "não achou", "foi embora"], "lado": "onde perde"},
   "texto": "Eu abro perfil de empresa toda semana e o padrão se repete: post bom, bio confusa e nenhum caminho para falar com o dono. O cliente não procura duas vezes.",
   "soco": "Quem precisa procurar o seu contato já está saindo."},
  {"etiqueta": "Ajuste 1 de 4", "titulo": "Mude para conta profissional", "desenho": {"tipo": "numero", "n": 1, "nota": "é gratuito"},
   "texto": "Em Configurações, Tipo de conta e ferramentas, troque para conta profissional. Você passa a ver quantas pessoas o post alcançou, quem salvou e quem enviou para alguém.",
   "soco": "Sem esses números, você posta no escuro."},
  {"etiqueta": "Ajuste 2 de 4", "titulo": "Escolha a categoria que o cliente procura", "desenho": {"tipo": "numero", "n": 2, "nota": "embaixo do nome"},
   "texto": "A categoria aparece logo abaixo do seu nome no perfil. Escolha a que descreve o serviço que você vende, como consultor, clínica de estética ou restaurante, e não a que soa mais bonita.",
   "soco": "O cliente precisa entender o que você faz em um segundo."},
  {"etiqueta": "Ajuste 3 de 4", "titulo": "Ligue o botão de contato", "desenho": {"tipo": "numero", "n": 3, "nota": "WhatsApp primeiro"},
   "texto": "Em Editar perfil, Opções de contato, coloque o WhatsApp da empresa, o e-mail e, se você tem ponto físico, o endereço. Para quem vende serviço, eu sempre deixo o WhatsApp como primeiro contato.",
   "soco": "Cada toque a mais é um cliente a menos."},
  {"etiqueta": "Ajuste 4 de 4", "titulo": "Um link, um destino", "desenho": {"tipo": "numero", "n": 4, "nota": "sem oito botões"},
   "texto": "O link da bio leva para um lugar só: a página de marcação, o WhatsApp ou a página do serviço. Uma lista com oito botões faz o cliente escolher, e quem precisa escolher costuma deixar para depois.",
   "soco": "Uma porta, bem sinalizada."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3", "4"], "nota": "conta pessoal com cliente real"},
   "texto": "O dono tem clientes de verdade, posta toda semana e continua com conta pessoal: sem botão, sem categoria e sem números. Depois conclui que o Instagram não traz cliente.",
   "soco": "Muitas vezes o problema está na configuração."},
  {"etiqueta": "Na prática", "titulo": "Faça os ajustes hoje, com o celular na mão", "desenho": {"tipo": "lista", "check": True, "itens": ["conta profissional", "categoria do serviço", "WhatsApp no botão", "endereço, se tiver", "um link só"]},
   "texto": "Leva menos de quinze minutos e você não precisa postar nada novo para isso."},
  {"etiqueta": "Próximo passo", "titulo": "Envie para quem cuida do Instagram da sua empresa", "desenho": {"tipo": "numero", "n": 4, "nota": "ajustes feitos hoje"},
   "texto": "Envie este post para o seu sócio ou para quem cuida do perfil. Se você quer que eu olhe o seu perfil inteiro com você, comente PERFIL que eu te mando no direct como funciona a minha mentoria.",
   "soco": "Comece pela configuração, que não depende de inspiração."},
]}

# 2) 17:40 TWEET, ângulo A, CTA = COMENTÁRIO (palavra SALÁRIO)
tweet = {"formato": "tweet", "nome": "Liuri Alves", "arroba": "@liurialves", "avatar": f"{R}/assets/avatar-liuri.jpg", "slides": [{"texto": t} for t in [
  "Se você tira dinheiro do caixa da empresa sempre que a conta de casa aperta, você não tem salário. Você tem uma empresa pagando as suas contas sem saber quanto.",
  "Eu fiz isso por muito tempo. No fim do mês eu não sabia se o negócio tinha dado lucro ou se eu só tinha gastado menos em casa.",
  "O nome disso é pró-labore: o valor fixo que o dono recebe pelo trabalho que faz na empresa. Mesmo valor, mesma data, todo mês.",
  "Sem esse número, a conta da empresa engana. Ela parece lucrativa porque o seu trabalho não entra no custo. No dia em que você precisar pagar alguém para fazer o que você faz, o lucro some.",
  "Como eu defino o meu: olho a média de faturamento dos últimos seis meses, tiro os custos fixos e a reserva, e escolho um valor que a empresa consegue pagar até no mês fraco.",
  "Se for preciso, comece baixo. Eu prefiro um valor pequeno que cai todo dia 5 a um valor alto que só aparece quando o mês foi bom.",
  "O que passar disso fica na empresa. Vira reserva, investimento ou lucro distribuído no fim do trimestre, com a conta feita antes e não no impulso de uma sexta-feira.",
  "A forma de declarar muda no Brasil e em Portugal, e conforme o tipo de empresa. Converse com o seu contador antes de mudar. O hábito de ter um valor fixo serve nos dois países.",
  "Comente SALÁRIO se hoje você ainda tira do caixa quando precisa. Eu respondo cada um, e a quem quiser montar essa conta comigo eu mando no direct como funciona a minha mentoria.",
]]}

# 3) 20:30 CAPA + ESCURO, ângulo C, CTA = SALVAR (palavra FORTE). REMODELADO.
vida = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": F("1VaAy0gfb96JaFX8Fs2hFZyuC7WPrADBU"), "foco_y": 0.55, "etiqueta": "Vida de quem empreende",
   "titulo": "Ser forte, para quem empreende, é [[cumprir quando ninguém está olhando]]",
   "sub": "Cinco momentos da farda até a minha empresa em Lisboa."},
  {"etiqueta": "Antes de começar", "frase": "A força que conta no negócio [[aparece às 23h]], com a casa dormindo e a conta do mês aberta na tela.",
   "texto": "Ninguém filma essa parte. Eu juntei cinco momentos da minha vida em que eu entendi isso. Salve para ler de novo no dia em que pensar em largar."},
  {"etiqueta": "Momento 1", "frase": "Aos 19, na Aeronáutica, [[eu tinha horário para tudo]].",
   "texto": "Eu entrei por necessidade financeira. Acordar, formar, cumprir, sem espaço para saber se eu estava com vontade. Foi ali que eu entendi que disciplina é a agenda cumprida no dia ruim."},
  {"etiqueta": "Momento 2", "frase": "Quando eu cheguei a Lisboa, [[ninguém sabia quem eu era]].",
   "texto": "Sem rede de contatos, sem nome no mercado, recomeçando num país que não era o meu. Da farda eu trouxe uma coisa só: o hábito de fazer o trabalho todos os dias, mesmo sem ninguém para conferir."},
  {"etiqueta": "Momento 3", "frase": "Dez anos atendendo cliente [[me ensinaram a ouvir antes de falar]].",
   "texto": "Com as mãos nas costas de alguém durante uma hora, você percebe o que a pessoa precisa antes de ela dizer. Hoje eu faço o mesmo com o dono de empresa antes de propor qualquer estratégia."},
  {"etiqueta": "Momento 4", "frase": "No tatame eu aprendi a [[treinar cansado]].",
   "texto": "O treino que mais conta é o de sexta à noite, depois de uma semana pesada. Na empresa acontece igual: a proposta que eu termino cansado e a ligação que eu faço sem vontade são as que fazem o mês andar."},
  {"etiqueta": "Momento 5", "frase": "Hoje [[a minha família depende das decisões]] que eu tomo às 23h.",
   "texto": "Preço, cliente, o que eu corto e o que eu mantenho. Ninguém aplaude essa parte e ela decide o mês inteiro. Para mim, ser forte virou isto: decidir com calma e cumprir no dia seguinte."},
  {"etiqueta": "O que eu levo de tudo isso", "frase": "Ninguém vai conferir se você fez. [[O resultado do mês vai.]]",
   "texto": "Quem empreende não tem chefe para cobrar. Por isso eu anoto no domingo o que prometi a mim mesmo para a semana e confiro no domingo seguinte."},
  {"etiqueta": "Próximo passo", "frase": "Salve este post [[para o dia em que pensar em largar]].",
   "texto": "Se você quer construir a sua empresa com método, número e acompanhamento, comente FORTE que eu te mando no direct como funciona a minha mentoria."},
]}

LEGENDAS = {
 1: """O cliente achou o seu perfil, gostou do post e foi procurar o contato. Se não achou em poucos segundos, ele foi embora.

Quatro ajustes que levam menos de quinze minutos: conta profissional, categoria que descreve o seu serviço, botão de contato com o WhatsApp da empresa e um link só na bio, com um destino claro.

Muito dono de negócio culpa o conteúdo quando o problema está na configuração do perfil.

🔻 Envie este post para quem cuida do Instagram da sua empresa. Se quiser que eu olhe o seu perfil com você, comente PERFIL que eu te mando no direct como funciona a minha mentoria.

#marketingdigital #empreendedorismo #negocioproprio #empresario #brasileirosemportugal""",
 2: """Você tira dinheiro do caixa da empresa toda vez que a conta de casa aperta?

Então a empresa paga as suas contas e ninguém sabe quanto. Sem pró-labore fixo, a conta do negócio engana: parece dar lucro porque o seu trabalho não entra no custo.

Como eu defino o meu: média de faturamento dos últimos seis meses, menos custos fixos e reserva, e um valor que a empresa paga até no mês fraco. O resto fica na empresa. A forma de declarar muda no Brasil e em Portugal, então converse com o seu contador antes.

🔻 Comente SALÁRIO se hoje você ainda tira do caixa quando precisa. Eu respondo cada um, e a quem quiser montar essa conta comigo eu mando no direct como funciona a minha mentoria.

#gestao #empresario #empreendedorismo #negocioproprio #financas""",
 3: """Ser forte, para quem empreende, quase nunca aparece em vídeo. Aparece às 23h, com a casa dormindo e a conta do mês aberta na tela.

Eu juntei cinco momentos em que aprendi isso: a Aeronáutica aos 19, a chegada a Lisboa sem ninguém saber quem eu era, dez anos atendendo cliente, o treino de sexta à noite no tatame e as decisões que hoje sustentam a minha família.

Ninguém vai conferir se você fez. O resultado do mês vai.

🔻 Salve este post para o dia em que pensar em largar. Se quiser construir a sua empresa com método e acompanhamento, comente FORTE que eu te mando no direct como funciona a minha mentoria.

#vidadeempreendedor #empreendedorismo #disciplina #brasileirosemportugal #negocioproprio""",
}


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_formatos.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    O = lambda n: f"{R}/posts/{DIA}/liurialves-{n}"
    run(quadro, O(1)); run(tweet, O(2)); run(vida, O(3)); print("ok")
