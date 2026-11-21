"""Pedido do dono no chat em 12/11/2026 (16:10): post de motivação "quem não ligou no inverno, não atenda no verão",
criado e publicado na hora. Conexão, pilar 6 (lição para o dono estagnado: cuidar de quem ficou no mês fraco).
Itens usados: 4 e 5 (o sorvete dividido, a chacota "não casa"), 18 (900 € com 700 €, o gerente amigo), 20 (1.500 € → 7.000 €).
Fotos Drive 42 (capa, chuva; Robério Castro), 20, 73, 72, 71 + fotos-liuri video-rotina-17s."""
import json, os, subprocess
S = "/tmp/claude-0/-home-claude-carrosseis/55739fb9-38ed-5ace-8282-20b5171b290d/scratchpad"
R = "/home/claude/carrosseis"
HP = lambda x: f"/tmp/h12/{x}.jpg"
FL = lambda x: f"{R}/assets/fotos-liuri/{x}.jpg"
cfg = {"slides": [
  {"tipo": "foto", "foto": HP("42"), "foco_y": 0.45, "grande": True, "arraste": True, "faixa": "O QUE A VIDA ME ENSINOU",
   "texto": "QUEM NÃO LIGOU NO INVERNO, NÃO ATENDA NO VERÃO."},
  {"tipo": "foto", "foto": HP("20"), "foco_y": 0.3, "faixa": "O MEU PRIMEIRO INVERNO",
   "texto": "EU E A MINHA NAMORADA ÍAMOS AO SHOPPING SÓ PARA USAR O WI-FI. TÍNHAMOS DINHEIRO PARA UM SORVETE SÓ, E DIVIDÍAMOS.",
   "destaque": "QUANDO FALAMOS EM CASAR, TEVE GENTE QUE DISSE: NÃO CASA, NÃO VALE A PENA."},
  {"tipo": "foto", "foto": HP("73"), "foco_y": 0.4, "faixa": "O SEGUNDO INVERNO",
   "texto": "JÁ EM LISBOA, EU PRECISAVA DE 900 € POR MÊS E GANHAVA 700 €. TRABALHAVA 12 HORAS E NO FIM DE SEMANA IA PARA UM CLUBE ATÉ AS 8 DA MANHÃ."},
  {"tipo": "foto", "foto": HP("72"), "foco_y": 0.35, "faixa": "QUEM LIGOU",
   "texto": "UM EX-GERENTE ME EMPRESTOU DINHEIRO TODO MÊS. UM DIA ME DEU 100 € DE PRESENTE E EU CHOREI.",
   "destaque": "ESSE EU ATENDO A QUALQUER HORA."},
  {"tipo": "foto", "foto": HP("71"), "foco_y": 0.4, "faixa": "O VERÃO CHEGA",
   "texto": "EM 2026 A MINHA EMPRESA SAIU DE 1.500 € PARA 7.000 € POR MÊS. E O TELEFONE TOCA MAIS.",
   "destaque": "AGORA EU ESCOLHO QUEM ATENDO PRIMEIRO."},
  {"tipo": "branco", "blocos": [
   ["h", "NO SEU NEGÓCIO, O INVERNO É O MÊS FRACO."], ["esp", 8],
   ["n", "Quem pagou você no pior mês do ano merece ser o primeiro a ser atendido quando a agenda encher. Faça hoje:"],
   ["h", "1. ABRA OS SEUS 3 PIORES MESES"],
   ["n", "Liste quem pagou em todos eles."],
   ["h", "2. MANDE UMA MENSAGEM PESSOAL"],
   ["n", "\"[Nome], você ficou comigo quando o movimento estava fraco. Obrigado. Guardei o seu horário de sempre.\""],
   ["h", "3. PROTEJA ESSES CLIENTES"],
   ["n", "Quando subir o preço, eles são os últimos a pagar o novo."]]},
  {"tipo": "foto", "foto": FL("video-rotina-17s"), "foco_y": 0.3, "faixa": "ENVIE PARA QUEM LIGOU NO SEU INVERNO",
   "texto": "E COMENTE CLIENTES QUE EU TE CHAMO NO DIRECT.",
   "destaque": "O INVERNO PASSA. A MEMÓRIA FICA."},
]}
LEG = """Quem não ligou no inverno, não atenda no verão.

O meu primeiro inverno foi no Brasil: eu e a minha namorada íamos ao shopping só para usar o Wi-Fi e dividíamos um sorvete, porque o dinheiro só dava para um. Quando falamos em casar, teve gente que disse "não casa, não vale a pena". Casamos.

O segundo foi em Lisboa: eu precisava de 900 € por mês e ganhava 700 €. Trabalhava 12 horas e, no fim de semana, ia para um clube até as 8 da manhã. Um ex-gerente me emprestou dinheiro todo mês e um dia me deu 100 € de presente. Esse eu atendo a qualquer hora.

Em 2026 a minha empresa saiu de 1.500 € para 7.000 € por mês. O telefone toca mais, e agora eu escolho quem atendo primeiro.

No seu negócio, o inverno é o mês fraco. Abra hoje os seus 3 piores meses, liste quem pagou em todos eles e mande uma mensagem pessoal de agradecimento. Quando subir o preço, eles são os últimos a pagar o novo.

🔻 Envie para quem ligou no seu inverno. E comente CLIENTES que eu te chamo no direct.

Foto da capa: Robério Castro Fotografia.

#motivacao #empreendedorismo #donodenegocio #historiareal #brasileiroemportugal"""
if __name__ == "__main__":
    out = f"{R}/posts/2026-11-12/liurialves-extra"
    os.makedirs(S, exist_ok=True); os.makedirs(out, exist_ok=True)
    for f in os.listdir(out): os.remove(os.path.join(out, f))
    p = f"{S}/cfg-extra.json"; json.dump(cfg, open(p, "w"), ensure_ascii=False)
    subprocess.run(["python3", f"{R}/scripts/render_faixa.py", p, out], check=True)
    open(f"{S}/legenda-extra.txt", "w").write(LEG)
    print("ok")
