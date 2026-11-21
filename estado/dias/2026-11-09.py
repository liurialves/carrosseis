"""Plano 100 mil, semana 3, dia 3 (09/11/2026, segunda). Dia 3 do "Plano de 30 dias para lançar a mentoria":
pilar 1, "Os 4 números do fim do mês" (vira o post de IA das 12:40); tarefa: enviar a mensagem aos 10 primeiros contatos.
AJUSTE DE QUALIDADE (08/11): 4 posts. 12:40 IA (valor, ver 2026-11-09-ia.py) · 14:20 CONEXÃO com foto real ·
17:40 VALOR · 20:30 PROVA (segunda). Sem prints novos do @modocaverna: sem post às 22:15.
CTA (rodízio): 14:20 comentário, 17:40 salvar, 20:30 envio; todos terminam em "Comente CLIENTES".
14:20 FAIXA, conexão, pilar comprador 5. REMODELADO do carrossel do dono com mais alcance nos últimos 30 dias
      (buffer 6af08ee8d6bbae6fa1f59abb, "Cheguei a Portugal sozinho, com 300 €...", 08/11, 498 de alcance, 38 reações).
      Mantém o que funcionou (faixa, foto real, história em 1ª pessoa + lição). Muda: trecho (parte 1, itens 2 a 5:
      os dois empregos perdidos, chinelo/cosmético/joia/água na praia, o sorvete dividido, o dinheiro para casar),
      gancho novo, fotos da fase do namoro (Drive fotos/historia-portugal 08, 20, 22, 48, 07), lição de oferta.
17:40 QUADRO, valor, pilar comprador 1: o roteiro de 4 mensagens para responder "quanto custa?" no WhatsApp.
20:30 CAPA + ESCURO, prova, pilar comprador 5: print real do Meta Ads (prova-social/meta-ads-whatsapp-relaxante-219-cliques.png):
      16,81 € gastos, 219 cliques em ligações, 0,0768 € por clique, 11.541 de alcance. Recorte só do bloco de resultados
      (sem avatar, sem nome da campanha, sem barra do telemóvel).
"""
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps
S = "/tmp/claude-0/-home-claude-carrosseis/3e4b2116-f258-538c-9a85-01ca1b2740ed/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-09"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
HP = lambda x: f"/tmp/h9/{x}.jpg"          # fotos/historia-portugal (Drive), baixadas nesta execução
P = lambda x: f"/tmp/px9/pexels-{x}.jpg"
PRINT = "/tmp/prova/16pmnSDbMijkVznyuNnzKdPeQj0fkeD7H.jpg"

# 1) 14:20 FAIXA, CONEXÃO, CTA = COMENTÁRIO + CLIENTES. REMODELADO.
faixa = {"slides": [
  {"tipo": "foto", "foto": HP("08"), "foco_y": 0.0, "grande": True, "arraste": True, "faixa": "ANTES DE QUALQUER EMPRESA",
   "texto": "EU E A MINHA NAMORADA TESTAMOS 4 JEITOS DE GANHAR DINHEIRO. SÓ UM FEZ CAIXA."},
  {"tipo": "foto", "foto": HP("20"), "foco_y": 0.3, "faixa": "AOS 18 ANOS",
   "texto": "PERDI OS DOIS EMPREGOS AO MESMO TEMPO, UM DELES DE AJUDANTE DE PERSONAL NUMA ACADEMIA QUE JÁ NÃO CONSEGUIA PAGAR."},
  {"tipo": "foto", "foto": HP("22"), "foco_y": 0.3, "faixa": "TESTES 1, 2 E 3",
   "texto": "HAVAIANAS DECORADAS COM PÉROLAS, COSMÉTICO DE CATÁLOGO E JOIAS. EU E ELA VENDÍAMOS JUNTOS."},
  {"tipo": "foto", "foto": HP("48"), "foco_y": 0.25, "faixa": "A FASE MAIS DIFÍCIL",
   "texto": "ÍAMOS AO SHOPPING SÓ PARA USAR O WI-FI E PROCURAR COMO GANHAR DINHEIRO. O DINHEIRO DAVA PARA UM SORVETE, E A GENTE DIVIDIA."},
  {"tipo": "foto", "foto": P(16154281), "foco_y": 0.5, "faixa": "TESTE 4",
   "texto": "ÁGUA NA PRAIA, COM UMA BICICLETA ENFERRUJADA. FOI ESSA QUE FEZ CAIXA.",
   "destaque": "COM CALOR, NINGUÉM PRECISA SER CONVENCIDO A COMPRAR ÁGUA."},
  {"tipo": "foto", "foto": HP("07"), "foco_y": 0.0, "faixa": "PARA QUE ERA O DINHEIRO",
   "texto": "PARA CASAR. TEVE GENTE QUE RIU E DISSE QUE NÃO VALIA A PENA. HOJE ELA É A MINHA ESPOSA E A MÃE DOS MEUS FILHOS."},
  {"tipo": "branco", "blocos": [
   ["t", "SE A SUA EMPRESA ESTÁ PARADA NO MESMO FATURAMENTO, PROCURE A SUA ÁGUA NA PRAIA:"], ["esp", 14],
   ["h", "1. LISTE O QUE VOCÊ VENDE"],
   ["n", "Cada serviço e pacote, com quantas vendas teve nos últimos 3 meses."],
   ["h", "2. ACHE O QUE VENDE SOZINHO"],
   ["n", "O serviço que o cliente pede sem você insistir. Exemplo: no personal, o plano de 3 treinos por semana."],
   ["h", "3. PONHA ELE NA FRENTE"],
   ["n", "Na bio, no post fixado e no anúncio. O resto você oferece depois da primeira compra."]]},
  {"tipo": "foto", "foto": FL("video-rotina-13s"), "foco_y": 0.35, "faixa": "COMENTE CLIENTES",
   "texto": "QUE EU TE CHAMO NO DIRECT E TE AJUDO A ACHAR A OFERTA QUE O SEU CLIENTE JÁ QUER COMPRAR.",
   "destaque": "SE VOCÊ TAMBÉM COMEÇOU DO ZERO, ESTE POST É SEU."},
]}

# 2) 17:40 QUADRO, VALOR, CTA = SALVAR + CLIENTES
quadro = {"formato": "quadro", "slides": [
  {"etiqueta": "Método", "titulo": "O que responder quando perguntam [[\"quanto custa?\"]] no WhatsApp",
   "desenho": {"tipo": "circulos", "rotulos": ["objetivo", "plano", "horário"], "centro": "AULA"}, "texto": ""},
  {"etiqueta": "Faturamento parado?", "titulo": "Quem manda só o preço entra na comparação de preço",
   "desenho": {"tipo": "numero", "n": 3, "nota": "outros receberam a mesma pergunta"},
   "texto": "Personal, academia, fisioterapia ou barbearia: quem pergunta \"quanto custa?\" mandou a mesma mensagem para mais dois ou três. Se a sua resposta é só o número, a pessoa escolhe pelo número.",
   "soco": "O preço entra depois de uma pergunta."},
  {"etiqueta": "Passo 1 de 4", "titulo": "Agradeça e pergunte o objetivo", "desenho": {"tipo": "numero", "n": 1, "nota": "uma pergunta, não um formulário"},
   "texto": "\"Olá, [nome]! Obrigado pela mensagem. Antes de te passar os valores, me conta: o que você quer resolver? [emagrecer / voltar a treinar / dor nas costas]\"",
   "soco": "Quem responde a pergunta já está conversando com você."},
  {"etiqueta": "Passo 2 de 4", "titulo": "Repita o objetivo com as palavras dele", "desenho": {"tipo": "numero", "n": 2, "nota": "uma linha só"},
   "texto": "\"Entendi. Você quer [objetivo dele] até [data que ele falou]. É exatamente o que eu mais faço aqui.\"",
   "soco": "A pessoa compra de quem mostrou que ouviu."},
  {"etiqueta": "Passo 3 de 4", "titulo": "Um plano só, com o valor por mês", "desenho": {"tipo": "numero", "n": 3, "nota": "nunca a tabela inteira"},
   "texto": "\"Para isso eu recomendo o plano de [3 vezes por semana], que fica [valor] por mês. Inclui [avaliação, ajuste do treino e acompanhamento no WhatsApp].\"",
   "soco": "Três opções na primeira mensagem viram \"vou pensar\"."},
  {"etiqueta": "Passo 4 de 4", "titulo": "Termine marcando", "desenho": {"tipo": "numero", "n": 4, "nota": "dois horários para escolher"},
   "texto": "\"Tenho horário na [terça às 7h] ou na [quinta às 18h] para a sua avaliação. Qual fica melhor para você?\"",
   "soco": "\"Qualquer coisa me avisa\" deixa a decisão para depois."},
  {"etiqueta": "Atenção", "titulo": "O erro que eu mais vejo", "desenho": {"tipo": "pular", "pontos": ["1", "2", "3", "4"], "nota": "print da tabela de preços"},
   "texto": "Mandar a tabela inteira em PDF ou print. A pessoa compara linha a linha com o concorrente e some. A tabela é para você consultar; para o cliente vai o plano escolhido pelo objetivo que ele contou.",
   "soco": "Conversa primeiro, preço depois."},
  {"etiqueta": "Na prática", "titulo": "Deixe pronto hoje",
   "desenho": {"tipo": "lista", "check": True, "itens": ["as 4 mensagens nas respostas rápidas", "colchetes trocados pelo seu serviço", "resposta em até 15 minutos", "quem marcou anotado"]},
   "texto": "Daqui a 7 dias, conte: de cada 10 pessoas que perguntaram o preço, quantas marcaram? Esse é o número que você vai melhorar."},
  {"etiqueta": "Próximo passo", "titulo": "Salve e use na próxima mensagem que chegar",
   "desenho": {"tipo": "numero", "n": 4, "nota": "mensagens prontas para copiar"},
   "texto": "O atendimento é uma peça do sistema. Se a sua empresa está parada no mesmo faturamento, comente CLIENTES que eu te chamo no direct.",
   "soco": "Quem conduz a conversa marca a aula."},
]}

# 3) 20:30 CAPA + ESCURO, PROVA, CTA = ENVIO + CLIENTES (fatia-1 = print real, montado à parte)
prova = {"formato": "escuro", "slides": [
  {"formato": "capa", "foto": FL("video-rotina-17s"), "foco_y": 0.3, "etiqueta": "Prova",
   "titulo": "Gastei 16,81 € num anúncio e recebi 219 cliques no botão de ligar.",
   "sub": "O print é real. O que isso ensina a quem vive de indicação."},
  {"etiqueta": "O print", "frase": "x", "texto": "x"},  # substituído pelo slide do print
  {"etiqueta": "Os números", "frase": "16,81 € gastos. [[219 cliques para ligar]]. 11.541 pessoas alcançadas.",
   "texto": "Dá 0,0768 € por clique: menos de 8 cêntimos para alguém tocar no botão e ligar para a minha empresa de massagem."},
  {"etiqueta": "O que eu fiz", "frase": "O anúncio pede [[uma ação só]].",
   "texto": "Ele não pede curtida nem seguidor. Quem vê o anúncio tem um caminho: ligar. Alcance sem caminho para o contato vira só número bonito no painel."},
  {"etiqueta": "Por que funciona", "frase": "Quem toca em ligar [[está com o problema na mão]].",
   "texto": "No seu negócio é igual: o aluno que quer voltar a treinar, o paciente com a lombar travada, o cliente que quer cortar o cabelo ainda hoje."},
  {"etiqueta": "Atenção", "frase": "Clique em ligar [[ainda não é venda]].",
   "texto": "Do clique até a marcação, quem decide é o atendimento: atender na hora, perguntar o objetivo e marcar o horário na mesma ligação."},
  {"etiqueta": "Para começar", "frase": "Um anúncio, [[uma oferta clara]], um botão.",
   "texto": "Rode uma semana com um orçamento que não te aperte. No fim, conte três números: cliques, ligações atendidas e marcações. Eles dizem se vale aumentar."},
  {"etiqueta": "Para quem é", "frase": "Para o dono que vive de [[indicação]] e está parado.",
   "texto": "Personal trainer, academia, fisioterapia, barbearia, faturando entre 1.500 € e 5.000 € por mês e sem nenhum anúncio que traga contato."},
  {"etiqueta": "Próximo passo", "frase": "Envie para um dono de negócio [[que nunca anunciou]].",
   "texto": "E se esse dono é você, comente CLIENTES. Eu te chamo no direct e te mostro como montar a primeira campanha no seu negócio."},
]}

LEGENDAS = {
 1: """Antes de qualquer empresa, eu e a minha namorada testamos 4 jeitos de ganhar dinheiro. Só um fez caixa.

Aos 18 anos fiquei sem os dois empregos ao mesmo tempo: jovem aprendiz numa corretora e ajudante de personal numa academia que já não conseguia pagar. A gente decorou Havaianas com pérolas, vendeu cosmético de catálogo e joias. Ia ao shopping só para usar o Wi-Fi e dividia um sorvete. O que fez caixa foi água na praia, com uma bicicleta enferrujada. O dinheiro era para casar. Teve gente que riu. Hoje ela é a minha esposa.

A água vendia porque ninguém precisa ser convencido a comprar água no calor. Se a sua empresa está parada no mesmo faturamento, liste o que você vende, ache o serviço que o cliente pede sem você insistir e ponha esse na frente: na bio, no post fixado e no anúncio.

🔻 Comente CLIENTES que eu te chamo no direct e te ajudo a achar a oferta que o seu cliente já quer comprar.

#empreendedorismo #donodenegocio #personaltrainer #historiareal #vidadeempreendedor""",
 2: """Quando alguém pergunta "quanto custa?" no seu WhatsApp, a mesma pergunta foi para mais dois ou três concorrentes. Se a resposta é só o número, a pessoa escolhe pelo número.

O roteiro de 4 mensagens, para personal trainer, academia, fisioterapia ou barbearia:
1. Agradeça e pergunte o objetivo.
2. Repita o objetivo com as palavras dele.
3. Um plano só, com o valor por mês.
4. Termine com dois horários para escolher.

As mensagens prontas estão nos slides 3 a 6. Salve nas respostas rápidas e conte, daqui a 7 dias, quantas pessoas que perguntaram o preço marcaram.

🔻 Salve para usar na próxima mensagem. E se a sua empresa está parada no mesmo faturamento, comente CLIENTES que eu te chamo no direct.

#personaltrainer #fisioterapia #barbearia #whatsappbusiness #donodenegocio""",
 3: """Gastei 16,81 € num anúncio da minha empresa de massagem e recebi 219 cliques no botão de ligar. Alcance de 11.541 pessoas, 0,0768 € por clique. O print está no slide 2.

O anúncio pedia uma ação só: ligar. Quem toca em ligar está com o problema na mão. Mas clique ainda não é venda: do clique até a marcação, quem decide é o atendimento.

Para o seu negócio: um anúncio, uma oferta clara e um botão, durante uma semana, com um orçamento que não te aperte. No fim, conte cliques, ligações atendidas e marcações.

🔻 Envie para um dono de negócio que nunca anunciou. Se esse dono é você, comente CLIENTES que eu te chamo no direct e te mostro como montar a primeira campanha no seu negócio.

#trafegopago #anuncios #personaltrainer #barbearia #donodenegocio""",
}


def inter(t, peso="Bold"):
    f = ImageFont.truetype(f"{R}/assets/fonts/Inter.ttf", t)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f


def slide_print(dst, i, n):
    """Fatia escura com o recorte do print (só o bloco de resultados: sem avatar, nome da campanha nem barra do telemóvel)."""
    src = Image.open(PRINT).convert("RGB")
    crop = src.crop((20, 470, 719, 985))  # abas de período + números (219 / 0,0768 € / 16,81 € / 11 541)
    crop = ImageOps.contain(crop, (880, 900))
    im = Image.new("RGB", (1080, 1350), (14, 14, 14)); d = ImageDraw.Draw(im)
    d.text((110, 130), "O PRINT", font=inter(30, "Bold"), fill=(217, 84, 30))
    d.text((110, 180), "Meta Ads, anúncio para ligar.", font=inter(52, "Bold"), fill=(242, 239, 234))
    d.text((110, 250), "Resultado do período máximo da campanha.", font=inter(34, "Regular"), fill=(168, 164, 158))
    x = (1080 - crop.width) // 2; y = 350
    mask = Image.new("L", crop.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, crop.width, crop.height), 28, fill=255)
    im.paste(crop, (x, y), mask)
    d.rounded_rectangle((x - 2, y - 2, x + crop.width + 2, y + crop.height + 2), 30, outline=(217, 84, 30), width=3)
    d.text((110, 1170), "Print real da minha conta. Dados da campanha cortados.", font=inter(28, "Regular"), fill=(168, 164, 158))
    d.text((540, 1278), f"@liurialves  •  {i:02d}/{n:02d}", font=inter(26, "Medium"), fill=(120, 120, 120), anchor="ma")
    im.save(dst, quality=92)


def run(cfg, out, script="render_formatos.py"):
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
    run(faixa, O(1), "render_faixa.py"); run(quadro, O(2)); run(prova, O(3))
    slide_print(f"{O(3)}/fatia-1.jpg", 2, len(prova["slides"]))
    print("ok")
