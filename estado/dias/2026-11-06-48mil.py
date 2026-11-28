"""Extra de 06/11/2026 pedido pelo dono no chat: carrossel com a capa dele "48.000€ faturados este ano. Duas plataformas
construídas do zero." (Lisboa Massagem e MedPortugal). Fatias no formato escuro, pelos pilares do mapa da marca
(conteúdo, funil, controle financeiro + vida de quem empreende). Números só os da capa do dono (48.000€, +90 terapeutas).
CTA: CALL (call de diagnóstico gratuita, liurialves.com). Agendado às 22:15 de Lisboa.
"""
import json, os, subprocess
from PIL import Image
S = "/tmp/claude-0/-home-claude-carrosseis/3de97be0-9b10-54e4-a03c-47adc178e7b7/scratchpad"
R = "/home/claude/carrosseis"
OUT = f"{R}/posts/2026-11-06/liurialves-5"
CAPA = "/root/.claude/uploads/3de97be0-9b10-54e4-a03c-47adc178e7b7/b2fd41fe-image.png"

cfg = {"formato": "escuro", "slides": [
  {"etiqueta": "Antes do número", "frase": "Cheguei a Lisboa [[sem ninguém saber o meu nome]].",
   "texto": "Sem contato, sem sócio, sem investidor. O que está na capa foi feito com o que eu tinha na mão: dez anos de massagem, um computador e a disciplina que eu trouxe da Aeronáutica."},
  {"etiqueta": "Plataforma 1", "frase": "A Lisboa Massagem começou [[comigo atendendo cliente]].",
   "texto": "Eu via outros terapeutas com o mesmo problema que eu: agenda vazia e cliente sem saber onde procurar. Hoje a plataforma tem mais de 90 terapeutas em Portugal, com contacto direto pelo WhatsApp."},
  {"etiqueta": "Plataforma 2", "frase": "A MedPortugal levou [[o mesmo método]] para outra área.",
   "texto": "Osteopatia, fisioterapia, nutrição e personal trainer, com perfis verificados e contacto direto. Construí do zero de novo, só que dessa vez sabendo o que tinha funcionado na primeira."},
  {"etiqueta": "O que eu aplico · 1", "frase": "Conteúdo feito para [[o cliente encontrar]], e não para impressionar.",
   "texto": "Cada página e cada post respondem o que a pessoa quer saber antes de chamar: o que é, onde fica, em quem confiar e como falar com alguém."},
  {"etiqueta": "O que eu aplico · 2", "frase": "Todo caminho termina [[numa conversa no WhatsApp]].",
   "texto": "A pessoa procura, encontra o profissional e fala direto com ele. Sem formulário longo e sem intermediário no meio. Quanto menos passos, mais gente chega ao fim."},
  {"etiqueta": "O que eu aplico · 3", "frase": "Eu sei [[quanto entra e quanto sai]] todo mês.",
   "texto": "Tem mês bom e tem mês apertado, e eu vejo os dois na hora. Faturamento sem controle do dinheiro só aumenta o tamanho do problema."},
  {"etiqueta": "O que eu não vou te prometer", "frase": "Isto [[não é dinheiro fácil]].",
   "texto": "Foram anos de trabalho antes deste número. O caminho é simples e dá para começar de onde você está: conteúdo, funil e dinheiro no controle, todos os dias."},
  {"etiqueta": "Próximo passo", "frase": "Quer aplicar isso [[no seu negócio]]?",
   "texto": "Comente CALL ou acesse liurialves.com e marque a sua call de diagnóstico gratuita. Eu olho o seu conteúdo, o seu funil e os seus números com você."},
]}

if __name__ == "__main__":
    os.makedirs(S, exist_ok=True)
    tmp = f"{S}/escuro-48mil"
    p = f"{S}/cfg-48mil.json"
    json.dump({"formato": "escuro", "slides": [{"etiqueta": "x", "frase": "x", "texto": "x"}] + cfg["slides"]}, open(p, "w"), ensure_ascii=False)
    subprocess.run(["python3", f"{R}/scripts/render_formatos.py", p, tmp], check=True)
    os.makedirs(OUT, exist_ok=True)
    Image.open(CAPA).convert("RGB").resize((1080, 1350), Image.LANCZOS).save(f"{OUT}/CAPA.jpg", quality=93)
    for i in range(1, 9):
        os.replace(f"{tmp}/fatia-{i}.jpg", f"{OUT}/fatia-{i}.jpg")
    print("ok")
