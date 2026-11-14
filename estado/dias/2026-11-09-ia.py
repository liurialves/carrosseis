"""Post de IA PRÁTICA de 09/11/2026 (12:40, valor, pilar comprador 4), estilo tilli do render_clone.py (08/11 foi hud).
As pastas clonar-ia e referencias-99hud não têm prints novos desde 02/11, então o post é feito no mesmo molde, com
uma ferramenta prática e sem instalação: ChatGPT para fechar o mês com os 4 números (entrou, saiu, sobrou, falta
receber). É também o conteúdo do dia 3 do "Plano de 30 dias" ("Os 4 números do fim do mês").
Conferido em 09/11/2026 na página oficial https://help.openai.com/en/articles/9275245-using-chatgpt-s-free-plan:
o plano gratuito permite "Upload images or files in your prompts" e "Analyze and extract insights from your data", e
"File uploads, image generation, voice, data analysis ... have separate usage limits" (limites mais apertados que
nos planos pagos). Preço de plano pago NÃO citado (a página de preços não pôde ser lida nesta execução).
Teste de valor: passo a passo (exportar extrato, prompt pronto, 4 perguntas), exemplo com números marcados como
exemplo, cuidado de privacidade, aplicável em menos de 1 hora.
"""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/3e4b2116-f258-538c-9a85-01ca1b2740ed/scratchpad"
R = "/home/claude/carrosseis"
DIA = "2026-11-09"
T = lambda linhas: {"tipo": "terminal", "linhas": linhas}

tilli = {"estilo": "tilli", "slides": [
  {"tipo": "capa", "foto": "/tmp/px9/pexels-8296983.jpg", "foco_y": 0.45,
   "titulo": "Pare de fechar o mês da sua empresa no olho"},
  {"tipo": "item", "card": T(["> extrato_outubro.csv", "# 1. entrou", "# 2. saiu", "# 3. sobrou", "# 4. falta receber"]),
   "titulo": "ChatGPT", "sub": "Você manda o extrato do mês, ele separa os 4 números.",
   "bullets": ["Funciona no plano gratuito", "No gratuito, o envio de ficheiros tem limite de uso", "Lê o extrato que o banco exporta", "Não precisa instalar nada"], "link": "chatgpt.com"},
  {"tipo": "item", "card": T(["# app do banco > extrato > exportar", "# formato: CSV, Excel ou PDF", "# período: 1 a 31 do mês"]),
   "titulo": "Passo 1", "sub": "Exporte o extrato da conta da empresa.",
   "bullets": ["Só a conta da empresa, nunca a pessoal", "Apague nomes de clientes e números de conta", "Anote à parte quem ainda não pagou", "Guarde o ficheiro numa pasta do mês"], "link": "Dado de cliente não vai para a IA"},
  {"tipo": "item", "card": T(["Separe este extrato de [mês] em:", "1. Entrou  2. Saiu  3. Sobrou", "4. Falta receber: [lista abaixo]", "Agrupe as saídas por categoria", "e mostre os 3 maiores gastos.", "Responda numa tabela."]),
   "titulo": "Passo 2", "sub": "Envie o ficheiro e cole este prompt.",
   "bullets": ["Troque o que está entre colchetes", "Cole a lista de quem deve no fim do prompt", "Peça a resposta em tabela", "Salve a conversa com o nome do mês"], "link": "Prompt pronto para copiar"},
  {"tipo": "item", "card": T(["> quanto sobrou a cada 100 € que entraram?", "> que gasto cresceu desde o mês passado?", "> quem deve há mais de 30 dias?", "> quanto preciso faturar para sobrar 1.000 €?"]),
   "titulo": "Passo 3", "sub": "Faça estas 4 perguntas na mesma conversa.",
   "bullets": ["A margem real do mês", "O gasto que está crescendo calado", "Quem cobrar amanhã de manhã", "A meta do próximo mês em euros"], "link": "As respostas viram a sua meta"},
  {"tipo": "item", "card": T(["# EXEMPLO (números inventados)", "entrou:        2.800 €", "saiu:          1.900 €", "sobrou:          900 €", "falta receber:   350 €"]),
   "titulo": "Exemplo", "sub": "Um personal trainer no fim de outubro.",
   "bullets": ["Sobraram 32 € a cada 100 € que entraram", "Os 350 € a receber são 4 alunos atrasados", "Cobrar hoje sobe o sobrou para 1.250 €", "Depois disso, o foco volta a ser cliente novo"], "link": "Números de exemplo, faça com os seus"},
  {"tipo": "item", "card": T(["# confira as somas", "# a decisão é sua"]),
   "titulo": "Os limites", "sub": "A IA organiza. Quem decide é você.",
   "bullets": ["Confira os totais: a IA pode errar conta", "No gratuito, o envio de ficheiros tem limite", "Nada de dado pessoal de cliente", "Misturou conta pessoal? Os números saem errados"], "link": "Conferido na ajuda oficial em 09/11"},
  {"tipo": "cta", "palavra": "CLIENTES", "promessa": "O CONVITE PARA CONVERSAR",
   "itens": ["Como eu organizo os números da empresa", "O caminho para ter cliente todo mês", "Acesso direto comigo", "Para quem é e como começar"]},
]}

LEGENDA = """Se você só descobre se o mês deu lucro quando abre o extrato e sente o aperto, este post é para você.

Os 4 números do fim do mês: entrou, saiu, sobrou e falta receber. Dá para fazer isso hoje no ChatGPT, no plano gratuito (o envio de ficheiros tem limite de uso no gratuito, segundo a ajuda oficial da OpenAI, conferida em 09/11):
1. Exporte o extrato da conta da empresa e apague nomes de clientes e números de conta.
2. Envie o ficheiro e cole o prompt do slide 4.
3. Faça as 4 perguntas do slide 5 na mesma conversa.

No exemplo do slide 6 (números inventados), um personal trainer descobre que tem 350 € para receber de 4 alunos atrasados. Cobrar isso é dinheiro que já é dele.

Confira sempre as somas: a IA organiza, quem decide é você.

🔻 Salve para o dia 1. E se a sua empresa está parada no mesmo faturamento, comente CLIENTES que eu te chamo no direct. Siga @liurialves.

#inteligenciaartificial #chatgpt #donodenegocio #gestaofinanceira #personaltrainer"""


def run(cfg, out):
    p = f"{S}/cfg-{DIA}-{os.path.basename(out)}.json"
    json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=1)
    r = subprocess.run(["python3", f"{R}/scripts/render_clone.py", p, out], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit(1)


if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    run(tilli, f"{R}/posts/{DIA}/liurialves-4"); print("ok ia")
