"""28/11/2026, pedido do dono no chat: carrossel de prova com o total de 2026 (corrigido: 100.174,60 € = massagem 45.174,60 da planilha
+ 5.000 €/mês de marketing e 500 €/mês de plataformas, fev a nov), publicado na hora. Números da aba "Graficos " (outubro, fevereiro)."""
import json, subprocess
R="/home/claude/carrosseis"; FL=lambda x:f"{R}/assets/fotos-liuri/{x}.jpg"
cfg={"slides":[
 {"tipo":"foto","foto":FL("lagoa-biceps-de-frente"),"foco_y":0.3,"grande":True,"arraste":True,"faixa":"PROVA · 2026",
  "texto":"DE FEVEREIRO A NOVEMBRO DE 2026 EU FATUREI 100.174,60 €."},
 {"tipo":"foto","foto":FL("home-office-headset"),"foco_y":0.3,"faixa":"DE ONDE VEIO","texto":"45.174,60 € NA MASSAGEM.","destaque":"50.000 € EM MARKETING E 5.000 € DAS PLATAFORMAS."},
 {"tipo":"foto","foto":FL("dunas-punhos-camisa-preta-1"),"foco_y":0.2,"faixa":"O MELHOR MÊS NA MASSAGEM","texto":"OUTUBRO: 6.965 € DE RECEITA.","destaque":"6.804 € DE LUCRO, EM 39 MASSAGENS."},
 {"tipo":"foto","foto":FL("selfie-jaqueta-verde"),"foco_y":0.3,"faixa":"O QUE MAIS MUDOU","texto":"O VALOR MÉDIO POR CLIENTE.","destaque":"DE 90,67 € EM FEVEREIRO PARA 178,59 € EM OUTUBRO."},
 {"tipo":"foto","foto":FL("selfie-sem-camisa-serio"),"foco_y":0.3,"faixa":"E OS CUSTOS","texto":"CAÍRAM DE 428 € PARA 161 € POR MÊS.","destaque":"QUASE TUDO O QUE ENTRA, FICA."},
 {"tipo":"foto","foto":f"{R}/assets/foto-perfil-liuri.jpg","foco_y":0.3,"faixa":"COMO","texto":"SOZINHO: O CONTEÚDO, OS ANÚNCIOS E O ATENDIMENTO.","destaque":"A MINHA VIDA MUDOU ESTE ANO, COM A MINHA ATITUDE."},
 {"tipo":"branco","blocos":[["h","SUBA O SEU VALOR MÉDIO ANTES DE CORRER ATRÁS DE MAIS CLIENTE."],["esp",8],
  ["n","Some o que entrou no último mês e divida pelo número de clientes atendidos. Esse é o seu valor médio."],
  ["n","Exemplo ilustrativo de um personal: 3.000 € ÷ 30 alunos = 100 €. Se 10 desses alunos passarem para um plano de 8 treinos a 160 €, o mês vai para 3.600 € sem nenhum aluno novo."]]},
 {"tipo":"foto","foto":FL("dunas-punhos-camisa-preta-3"),"foco_y":0.2,"faixa":"ENVIE PARA QUEM ESTÁ NO MESMO FATURAMENTO",
  "texto":"E COMENTE CLIENTES. EU TE CHAMO NO DIRECT.","destaque":"QUAL É O SEU VALOR MÉDIO HOJE?"},
]}
p="/tmp/claude-0/cfg50.json"; json.dump(cfg,open(p,"w"),ensure_ascii=False)
subprocess.run(["python3",f"{R}/scripts/render_faixa.py",p,f"{R}/posts/2026-11-28/liurialves-prova100"],check=True)
