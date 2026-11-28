import json, subprocess
R="/home/claude/carrosseis"; FL=lambda x:f"{R}/assets/fotos-liuri/{x}.jpg"; HP=lambda x:f"/tmp/h26/{x}.jpg"
cfg={"slides":[
 {"tipo":"foto","foto":FL("dunas-punhos-camisa-preta-3"),"foco_y":0.2,"grande":True,"arraste":True,"faixa":"PROVA · 2026 EM REAIS",
  "texto":"COMECEI 2026 FATURANDO R$ 9.585 POR MÊS. ATÉ AQUI JÁ SÃO R$ 306.720."},
 {"tipo":"foto","foto":FL("home-office-headset"),"foco_y":0.3,"faixa":"NO COMEÇO DO ANO","texto":"R$ 9.585 POR MÊS.","destaque":"EU FAZIA TUDO SOZINHO."},
 {"tipo":"foto","foto":HP("72"),"foco_y":0.45,"faixa":"EM 5 MESES","texto":"R$ 35.145 POR MÊS.","destaque":"CONTEÚDO, ANÚNCIOS E ATENDIMENTO FEITOS POR MIM."},
 {"tipo":"foto","foto":FL("selfie-jaqueta-verde"),"foco_y":0.3,"faixa":"DEPOIS","texto":"R$ 44.730 POR MÊS.","destaque":"COM MASSAGEM E SITES PARA CLIENTES."},
 {"tipo":"foto","foto":HP("70"),"foco_y":0.3,"faixa":"AS DUAS PLATAFORMAS","texto":"LISBOA MASSAGEM E MEDPORTUGAL, CONSTRUÍDAS DO ZERO.","destaque":"A LISBOA MASSAGEM TEM MAIS DE 90 TERAPEUTAS."},
 {"tipo":"foto","foto":HP("73"),"foco_y":0.3,"faixa":"UM DOS ANÚNCIOS","texto":"R$ 1.610 EM ANÚNCIOS DE MENSAGEM.","destaque":"VOLTARAM R$ 11.214 EM ATENDIMENTOS, DE 15 A 31/10."},
 {"tipo":"branco","blocos":[["h","FAÇA A CONTA DO SEU ANO."],["esp",8],
  ["n","Faturamento médio dos últimos 3 meses × 12. Depois escreva quanto você quer faturar em 2027 e quantos clientes a mais isso exige."],
  ["n","Exemplo ilustrativo de uma barbearia: R$ 15 mil por mês = R$ 180 mil no ano. Para R$ 240 mil, são R$ 5 mil a mais por mês: 50 cortes de R$ 100 ou 25 planos mensais de R$ 200."],
  ["n","Valores do Liuri convertidos de euro pela cotação de 26/11/2026: 1 € = R$ 6,39."]]},
 {"tipo":"foto","foto":FL("lagoa-biceps-de-frente-editada"),"foco_y":0.3,"faixa":"ENVIE PARA QUEM ESTÁ NO MESMO FATURAMENTO",
  "texto":"E COMENTE CLIENTES. EU TE CHAMO NO DIRECT.","destaque":"QUANTO O SEU NEGÓCIO FATUROU EM 2026?"},
]}
p="/tmp/claude-0/cfg48.json"; json.dump(cfg,open(p,"w"),ensure_ascii=False)
subprocess.run(["python3",f"{R}/scripts/render_faixa.py",p,f"{R}/posts/2026-11-26/liurialves-8"],check=True)
