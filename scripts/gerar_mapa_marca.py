"""
Gera o PDF preenchível "O mapa da sua marca" para os mentorados do Liuri Alves (pedido do dono em 06/11/2026).
Estrutura inspirada num exercício de marca em 4 partes (objetivo, pilares, teste, voz); texto e design são do Liuri:
papel claro quente, preto suave, laranja #D9541E, Inter + Caveat, cabeçalho com ícone + LIURI ALVES e barra de progresso.

Uso: python3 scripts/gerar_mapa_marca.py saida.pdf [pasta_fontes_estaticas]
As fontes do repositório são variáveis; o script gera instâncias estáticas (fontTools) se não existirem.
"""
import os, sys
from fontTools.ttLib import TTFont as FTFont
from fontTools.varLib.instancer import instantiateVariableFont
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FD = os.path.join(RAIZ, "assets", "fonts")
ICONE = os.path.join(RAIZ, "assets", "logos", "liuri-alves-icone-laranja.png")
OUT = sys.argv[1] if len(sys.argv) > 1 else "mapa-da-marca.pdf"
FX = sys.argv[2] if len(sys.argv) > 2 else "/tmp/fx"

PAPEL, TINTA, CINZA, LINHA = HexColor("#F4F1EB"), HexColor("#121212"), HexColor("#706B64"), HexColor("#D8D3CA")
ACC, CAMPO = HexColor("#D9541E"), HexColor("#FBFAF7")


def fontes():
    os.makedirs(FX, exist_ok=True)
    pesos = {"Regular": 400, "SemiBold": 600, "Bold": 700, "Black": 900}
    for n, w in pesos.items():
        p = f"{FX}/Inter-{n}.ttf"
        if not os.path.exists(p):
            f = FTFont(os.path.join(FD, "Inter.ttf")); loc = {"wght": w}
            if "opsz" in [a.axisTag for a in f["fvar"].axes]: loc["opsz"] = 14 if w < 700 else 32
            instantiateVariableFont(f, loc, inplace=True)
            for rec in f["name"].names:  # nome único por peso (senão o leitor de PDF mistura as instâncias)
                if rec.nameID in (1, 3, 4, 6): rec.string = f"LiuriInter{n}"
            f.save(p)
        pdfmetrics.registerFont(TTFont(f"I{n}", p))
    p = f"{FX}/Caveat-Bold.ttf"
    if not os.path.exists(p):
        f = FTFont(os.path.join(FD, "Caveat.ttf")); instantiateVariableFont(f, {"wght": 700}, inplace=True); f.save(p)
    pdfmetrics.registerFont(TTFont("Cav", p))


W, H = landscape(A4)
M = 56
TOTAL = 7


def quebra(c, txt, fonte, tam, maxw):
    ls, l = [], ""
    for w in txt.split():
        t = (l + " " + w).strip()
        if c.stringWidth(t, fonte, tam) <= maxw: l = t
        else: ls.append(l); l = w
    if l: ls.append(l)
    return ls


def texto(c, txt, x, y, fonte="IRegular", tam=11, cor=CINZA, maxw=600, lh=1.4):
    c.setFont(fonte, tam); c.setFillColor(cor)
    for l in quebra(c, txt, fonte, tam, maxw):
        c.drawString(x, y, l); y -= tam * lh
    return y


def base(c, n):
    c.setFillColor(PAPEL); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.drawImage(ICONE, M, H - 44, 14, 14, mask="auto")
    c.setFont("IBold", 8); c.setFillColor(TINTA)
    c.drawString(M + 20, H - 40, "L I U R I   A L V E S")
    c.setFont("IRegular", 8); c.setFillColor(CINZA)
    c.drawRightString(W - M, H - 40, f"{n:02d} / {TOTAL:02d}")
    # barra de progresso
    c.setStrokeColor(LINHA); c.setLineWidth(1); c.line(M, 34, W - M, 34)
    c.setStrokeColor(ACC); c.setLineWidth(2); c.line(M, 34, M + (W - 2 * M) * n / TOTAL, 34)
    c.setFont("IRegular", 7.5); c.setFillColor(CINZA)
    c.drawString(M, 20, "Mentoria Liuri Alves  ·  @liurialves  ·  material de uso individual do mentorado")


def etiqueta(c, txt, y):
    c.setStrokeColor(ACC); c.setLineWidth(1.2); c.line(M, y + 3, M + 18, y + 3)
    c.setFont("ISemiBold", 8.5); c.setFillColor(ACC)
    c.drawString(M + 26, y, "  ".join(txt.upper()))


def titulo(c, txt, y, tam=30):
    c.setFont("IBold", tam); c.setFillColor(TINTA); c.drawString(M, y, txt)


def nota(c, txt, x, y, tam=17, maxw=700):
    c.setFont("Cav", tam); c.setFillColor(ACC)
    for l in quebra(c, txt, "Cav", tam, maxw):
        c.drawString(x, y, l); y -= tam * 1.1
    return y


def campo(c, nome, x, y, w, h, dica=""):
    """Caixa preenchível (multilinha se h > 30). y = topo da caixa."""
    c.setFillColor(CAMPO); c.setStrokeColor(LINHA); c.setLineWidth(0.8)
    c.roundRect(x, y - h, w, h, 4, stroke=1, fill=1)
    c.acroForm.textfield(name=nome, x=x + 2, y=y - h + 2, width=w - 4, height=h - 4, borderWidth=0,
                         fillColor=CAMPO, textColor=TINTA, fontName="Helvetica", fontSize=10.5,
                         fieldFlags="multiline" if h > 30 else "", tooltip=dica or nome)


def pergunta(c, num, txt, apoio, y, maxw=W - 2 * M):
    c.setFillColor(ACC); c.circle(M + 11, y + 4, 11, stroke=0, fill=1)
    c.setFont("IBold", 11); c.setFillColor(white); c.drawCentredString(M + 11, y, str(num))
    c.setFont("IBold", 14); c.setFillColor(TINTA); c.drawString(M + 32, y, txt)
    return texto(c, apoio, M + 32, y - 18, tam=10, maxw=maxw - 32)


def gerar():
    fontes()
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle("O mapa da sua marca · Mentoria Liuri Alves"); c.setAuthor("Liuri Alves")

    # 1. Capa
    base(c, 1)
    etiqueta(c, "Exercício de mentoria", H - 150)
    c.setFont("IBlack", 52); c.setFillColor(TINTA); c.drawString(M, H - 215, "O mapa da")
    c.setFillColor(ACC); c.drawString(M, H - 272, "sua marca")
    nota(c, "Um exercício simples para saber o que postar, para quem e por quê.", M, H - 312, 21, maxw=330)
    texto(c, "Responda com calma e com honestidade. Ninguém além de você e de mim vai ler isto. "
             "Este mapa vira a base do seu perfil, dos seus posts e da forma como você vende.",
          M, H - 368, tam=11, maxw=330)
    for i, (rot, nome) in enumerate([("Nome", "nome"), ("Empresa", "empresa"), ("Data", "data")]):
        yy = H - 430 - i * 40
        c.setFont("ISemiBold", 9); c.setFillColor(TINTA); c.drawString(M, yy - 15, rot.upper())
        campo(c, nome, M + 80, yy, 300, 24)
    # bloco das 4 partes à direita
    x0 = W / 2 + 60
    c.setStrokeColor(LINHA); c.line(x0 - 30, H - 140, x0 - 30, 90)
    for i, (t, d) in enumerate([("A base", "o seu objetivo e pelo que quer ser lembrado"),
                                ("Os pilares", "os 3 a 5 assuntos que você vai dominar"),
                                ("O teste", "qual pilar fica e qual sai"),
                                ("A voz", "o que você defende e contra o que você está")]):
        yy = H - 175 - i * 82
        c.setFont("IBlack", 30); c.setFillColor(ACC); c.drawString(x0, yy - 8, f"{i + 1}")
        c.setFont("IBold", 15); c.setFillColor(TINTA); c.drawString(x0 + 36, yy, t)
        texto(c, d, x0 + 36, yy - 18, tam=10, maxw=260)
    c.showPage()

    # 2. Parte 1 · objetivo
    base(c, 2)
    etiqueta(c, "Parte 1 · A base", H - 90); titulo(c, "Por que você está nas redes sociais?", H - 128)
    nota(c, "Sem discurso bonito. Seja honesto: dinheiro, liberdade, reconhecimento, impacto?", M, H - 156)
    y = pergunta(c, 1, "Qual é o seu objetivo real com as redes sociais?",
                 "Escreva o que você quer de verdade e, se puder, com número e prazo. Exemplo: \"Fechar 4 clientes novos por "
                 "mês até março\" é melhor que \"crescer\".", H - 200)
    campo(c, "objetivo", M + 32, y - 6, W - 2 * M - 32, 110)
    y = pergunta(c, 2, "Se esse objetivo der certo, o que muda na sua vida?",
                 "Em casa, no seu tempo, no seu dinheiro. É esta resposta que vai te fazer postar no dia em que não tiver vontade.",
                 y - 140)
    campo(c, "o_que_muda", M + 32, y - 6, W - 2 * M - 32, 90)
    c.showPage()

    # 3. Parte 1 · pelo que quer ser conhecido
    base(c, 3)
    etiqueta(c, "Parte 1 · A base", H - 90); titulo(c, "Pelo que você quer ser lembrado?", H - 128)
    nota(c, "Se alguém descrevesse a sua marca em uma frase, o que diria?", M, H - 156)
    blocos = [("frase", "A frase da sua marca", "Como alguém te apresentaria a um amigo. Ex.: \"É o cara que ajuda dono de empresa a parar de depender de indicação.\""),
              ("problema", "O problema que você resolve", "Escreva a dor como o cliente fala, não como o mercado fala. Ex.: \"Só tenho cliente quando alguém me indica.\""),
              ("sentimento", "O sentimento que você cria", "Como o cliente se sente depois de passar por você. Prefira algo que ele sente logo no começo: controle, alívio, orgulho, tranquilidade.")]
    y = H - 200
    for i, (nome, t, d) in enumerate(blocos):
        y = pergunta(c, i + 3, t, d, y)
        campo(c, nome, M + 32, y - 4, W - 2 * M - 32, 58)
        y -= 92
    c.showPage()

    # 4. Parte 2 · pilares
    base(c, 4)
    etiqueta(c, "Parte 2 · Os pilares", H - 90); titulo(c, "Os assuntos que você vai dominar", H - 128)
    nota(c, "De 3 a 5 temas que sustentam aquilo pelo que você quer ser lembrado.", M, H - 156)
    texto(c, "Pense em temas largos o bastante para render posts durante anos e estreitos o bastante para o seu cliente "
             "se reconhecer neles. Pelo menos um pilar mostra a sua vida real: é ele que cria conexão e traz alcance.",
          M, H - 186, tam=10.5, maxw=W - 2 * M)
    exemplos = ["ex.: dinheiro e gestão da empresa", "ex.: cliente, conteúdo e vendas", "ex.: a minha rotina de quem empreende",
                "opcional", "opcional"]
    for i in range(5):
        yy = H - 238 - i * 58
        c.setFont("IBlack", 22); c.setFillColor(ACC if i < 3 else LINHA); c.drawString(M, yy - 26, f"{i + 1:02d}")
        c.setFont("ISemiBold", 8.5); c.setFillColor(TINTA); c.drawString(M + 48, yy - 4, f"PILAR {i + 1}")
        c.setFont("Cav", 13); c.setFillColor(CINZA); c.drawString(M + 105, yy - 4, exemplos[i])
        campo(c, f"pilar_{i + 1}", M + 48, yy - 10, W - 2 * M - 48, 32)
    c.showPage()

    # 5. Parte 3 · teste
    base(c, 5)
    etiqueta(c, "Parte 3 · O teste", H - 90); titulo(c, "Cada pilar precisa passar nas 4 perguntas", H - 128)
    nota(c, "Marque cada pergunta em que a resposta é SIM. Pilar sem as 4 marcas sai do mapa ou espera.", M, H - 156)
    crit = [("Credibilidade", "Eu tenho experiência própria ou resultado comprovado nisso?"),
            ("Paixão", "Eu falaria disto pelos próximos 10 anos sem me cansar?"),
            ("Conexão", "Este tema deixa eu mostrar quem eu sou, os meus valores e a minha história?"),
            ("Público", "Existe um grupo claro de pessoas que precisa muito de ajuda nisto?")]
    cw = (W - 2 * M - 150) / 4
    for j, (t, d) in enumerate(crit):
        x = M + 150 + j * cw
        c.setFont("IBold", 11); c.setFillColor(TINTA); c.drawString(x, H - 200, t)
        texto(c, d, x, H - 216, tam=8.5, maxw=cw - 14, lh=1.3)
    for i in range(5):
        yy = H - 290 - i * 46
        c.setStrokeColor(LINHA); c.setLineWidth(0.8); c.line(M, yy - 14, W - M, yy - 14)
        c.setFont("ISemiBold", 9); c.setFillColor(TINTA); c.drawString(M, yy, f"PILAR {i + 1}")
        for j in range(4):
            x = M + 150 + j * cw
            c.acroForm.checkbox(name=f"teste_p{i + 1}_{j + 1}", x=x, y=yy - 6, size=16, buttonStyle="check",
                                borderColor=ACC, fillColor=CAMPO, textColor=ACC, borderWidth=1,
                                tooltip=f"Pilar {i + 1}: {crit[j][0]}")
    texto(c, "Dica: credibilidade não precisa ser diploma. A sua história conta: anos de trabalho, a sua própria empresa, "
             "o que você já fez por um cliente real. O que não vale é número inventado.", M, 70, tam=9.5, maxw=W - 2 * M)
    c.showPage()

    # 6. Parte 4 · voz
    base(c, 6)
    etiqueta(c, "Parte 4 · A voz", H - 90); titulo(c, "O que você defende e contra o que você está", H - 128)
    nota(c, "Marca sem opinião vira só mais um perfil bonito.", M, H - 156)
    col = (W - 2 * M - 30) / 2
    for k, (nome, t, d) in enumerate([
            ("defendo", "Eu defendo", "De 3 a 5 crenças ou valores ligados aos seus pilares. Ex.: \"Empresa se gere com número, "
                                       "não com sensação.\" \"Trabalho feito vale mais que promessa.\""),
            ("sou_contra", "Eu sou contra", "Mitos, frustrações e maus conselhos do seu mercado com que você não concorda. "
                                            "Ex.: dinheiro fácil, resultado imediato, viver só de indicação.")]):
        x = M + k * (col + 30)
        c.setFillColor(ACC if k == 0 else TINTA); c.rect(x, H - 200, 4, 22, stroke=0, fill=1)
        c.setFont("IBold", 16); c.setFillColor(TINTA); c.drawString(x + 14, H - 194, t)
        yy = texto(c, d, x, H - 222, tam=9.5, maxw=col)
        campo(c, nome, x, yy - 6, col, yy - 6 - 60)
    c.showPage()

    # 7. Fechamento
    base(c, 7)
    etiqueta(c, "Fechamento", H - 90); titulo(c, "A sua mensagem em uma frase", H - 128)
    nota(c, "Junte tudo. Se couber numa frase, cabe na sua bio e na sua cabeça.", M, H - 156)
    partes = [("Eu ajudo", "msg_quem", "quem é o seu cliente"),
              ("a", "msg_resultado", "o resultado que ele quer"),
              ("sem", "msg_sem", "o que ele odeia ou teme"),
              ("para que ele sinta", "msg_sentimento", "o sentimento que você cria")]
    for i, (rot, nome, d) in enumerate(partes):
        yy = H - 210 - i * 52
        c.setFont("IBold", 15); c.setFillColor(TINTA); c.drawRightString(M + 140, yy - 20, rot)
        campo(c, nome, M + 155, yy, W - 2 * M - 155, 28)
        c.setFont("Cav", 12); c.setFillColor(CINZA); c.drawString(M + 160, yy - 40, d)
    c.setFillColor(TINTA); c.roundRect(M, 58, W - 2 * M, 66, 6, stroke=0, fill=1)
    c.setFont("IBold", 14); c.setFillColor(white); c.drawString(M + 24, 98, "Próximo passo")
    c.setFont("IRegular", 10.5); c.setFillColor(HexColor("#D8D3CA"))
    c.drawString(M + 24, 78, "Salve este PDF preenchido e traga para a nossa próxima sessão. Vamos transformar este mapa no seu perfil e nos seus posts.")
    c.setFillColor(ACC); c.rect(W - M - 6, 58, 6, 66, stroke=0, fill=1)
    c.showPage()
    c.save()


if __name__ == "__main__":
    gerar(); print(OUT)
