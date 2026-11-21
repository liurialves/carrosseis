"""16/11/2026 · 6º post do dia (pedido do dono às 13:39): formato LEGENDA, molde @therealbrianmark (fala de palco em 8
slides, 2 frames por slide com legenda). Frames do vídeo do Liuri falando (Drive reels/meus-videos-falando,
VIDEO-2026-10-17-09-50-03.mov) em assets/frames-falando. 19:10 · conexão (bandeira/opinião) · pilar 2 · CTA comentário.
Sem fato da história: só opinião + exemplos ilustrativos do comprador ideal. toca_indicacao = false."""
import json, os, subprocess
R = "/home/claude/carrosseis"; DIA = "2026-11-16"
S = "/tmp/claude-0/-home-claude-carrosseis/d98bb076-8483-5c41-8cfe-e62d9469467b/scratchpad"
F = lambda n: f"{R}/assets/frames-falando/video-2026-10-17-a-{n}.jpg"
cfg = {"slides": [
 {"fotos": [F("44"), F("53")], "foco": [0.6, 0.6], "textos": ["Eu acho que todo dono de negócio", "devia ter um pouco de medo."]},
 {"fotos": [F("24"), F("49")], "foco": [0.5, 0.6], "textos": ["Não do concorrente.", "Do mesmo faturamento."]},
 {"fotos": [F("31"), F("45")], "foco": [0.5, 0.6], "textos": ["Se a sua empresa fatura igual há seis meses,", "ela não está estável. Está parada."]},
 {"fotos": [F("14"), F("55")], "foco": [0.5, 0.6], "textos": ["O personal com os mesmos 20 alunos", "desde o ano passado."]},
 {"fotos": [F("18"), F("50")], "foco": [0.5, 0.6], "textos": ["A barbearia que enche no sábado", "e fica vazia na terça."]},
 {"fotos": [F("27"), F("57")], "foco": [0.5, 0.6], "textos": ["Os dois chamam isso de segurança.", "Eu chamo de risco."]},
 {"fotos": [F("34"), F("54")], "foco": [0.5, 0.6], "textos": ["Todo mês, olhe esse número", "e mexa em alguma coisa antes que ele caia."]},
 {"fotos": [F("21"), F("58")], "foco": [0.5, 0.6], "textos": ["Está no mesmo faturamento há meses?", "Comente CLIENTES."]},
]}
LEGENDA = """Negócio parado não é estabilidade. É risco.

Se a sua empresa fatura igual há seis meses, ela não está segura. Está parada. O personal com os mesmos 20 alunos desde o ano passado e a barbearia que enche no sábado e fica vazia na terça chamam isso de segurança. Eu chamo de risco.

Faça hoje: abra os últimos 6 meses e anote o faturamento de cada um. Se a linha está reta, escolha uma coisa para mudar este mês: a oferta, o preço, o atendimento ou a forma de trazer cliente novo. Uma só, e meça no fim do mês.

🔻 Está no mesmo faturamento há meses? Comente CLIENTES que eu te chamo no direct e a gente vê o que mexer primeiro.

#donodenegocio #empreendedorismo #personaltrainer #barbearia #mentalidadeempresarial"""
if __name__ == "__main__":
    out = f"{R}/posts/{DIA}/liurialves-6"; os.makedirs(S, exist_ok=True)
    p = f"{S}/cfg-legenda.json"; json.dump(cfg, open(p, "w"), ensure_ascii=False)
    subprocess.run(["python3", f"{R}/scripts/render_legenda.py", p, out], check=True)
    json.dump({"6": LEGENDA}, open(f"{S}/legenda-6.json", "w"), ensure_ascii=False)
    print("ok")
