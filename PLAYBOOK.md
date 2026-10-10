# Playbook — carrosséis diários (@liurialves e @spatherapieslisbon)

Rotina executada todo dia por uma tarefa agendada. Cada execução começa do zero,
então TUDO o que ela precisa está aqui. Siga na ordem.

## Meta do dia
3 carrosséis para **@liurialves** + 3 carrosséis para **@spatherapieslisbon**,
feitos com a skill **um-clique-darkgram**, imagens hospedadas neste repositório,
postados na **fila do Buffer** (o Buffer publica nos horários já configurados por canal).
Sem aprovação humana: o dono escolheu publicação direta. Por isso o controle de
qualidade da skill é obrigatório e não pode ser pulado.

## IDs fixos
- Buffer organização: `6a7f1a6904f03a7114bc637d`
- Buffer canal @liurialves: `6ac788306a5c39ccb6502999`
- Buffer canal @spatherapieslisbon: `6ac78c036a5c39ccb65050f9`
- Buffer canal TikTok @liurialves: `6ac7a3f36a5c39ccb65168cc`
- Drive pasta raiz "conteudo para o instagram" (pública): `1LfIV23SNjppw2eIuPcgyV8ZlAwV19qGE`
  - `fotos` (banco geral do Liuri): `1K4KOqLK6tOCobjrpUVqCEZ-v686CwSpz`
    - subpastas: `aeronautica`, `lisboa`, `familia`, `carro`, `outras`, `liurialves`, `spatherapieslisbon` (+ fotos soltas)
  - `fotos/spatherapieslisbon` (fotos do spa/massagem): `156fnNYTy3KCnjd7FMtPgyuoJ2wr62ncV`
  - `fotos/liurialves`: `1kvCsOBuSCutMeeQFnarul4olihTw9oGW`
  - `logos`: `1ggQNwpr9shcrdN63y0NGjDk819iDj8na` (PNG com "liuri" ou "spa" no nome)
  - `prints-site` (prints de lisboamassagem.pt): `1TveVh4LuBtAExDu1Dz5AqA-nIftx_SuA`
- URL pública das imagens: `https://raw.githubusercontent.com/liurialves/carrosseis/main/<caminho>`

## Logos (já no repositório, usar sempre)
- @liurialves: `"logo_png": "/home/claude/carrosseis/assets/logos/liuri-alves.png"`, `"logo_mode": "original"`
  (escudo laranja + LIURI ALVES; destaque amarelo `#F5C518` continua).
- @spatherapieslisbon: `"logo_png": "/home/claude/carrosseis/assets/logos/lisboa-massagem.png"`, `"logo_mode": "original"`
  (flor dourada + LISBOA MASSAGEM, versão escolhida pelo dono: 1a Flor). Destaque `#C9A486`.
- Outras versões no mesmo diretório (ícones, versão clara) só se fizer sentido; não troque o logo principal.

## Passo a passo
1. **Repo.** O repositório `liurialves/carrosseis` deve estar em `/home/claude/carrosseis`.
   Se não estiver, anexe com `add_repo` (owner `liurialves`, repo `carrosseis`, access `push`) e clone.
   `git pull` antes de começar. Instale `pip install pillow-heif --break-system-packages` se faltar.
2. **Ler a skill.** Leia `/mnt/skills/plugins/um-clique-darkgram/SKILL.md` e, nas references,
   `voz-e-doutrina.md`, `humanizer.md`, `filtro-editorial.md`, `banco-de-headlines.md`, `exemplos.md`.
   As regras de copy delas valem integralmente (densidade, sem travessão, sem paralelismo, sem jargão de marca).
   No modo automático, os checkpoints humanos da skill (origem, aprovação, estilo, fotos) são
   substituídos pelas decisões deste playbook.
3. **Histórico.** Leia `estado/historico.json`. Não repita capa, ângulo ou CTA dos últimos 14 dias
   do mesmo perfil. Dê preferência a fotos menos usadas.
4. **Fotos.** Liste as pastas do Drive com `search_files` (`parentId = '<id>'`, mimeType contém `image/`).
   Fotos novas (createdTime mais recente que o último post) têm prioridade.
   Baixe com `download_file_content`; o resultado grande é salvo num .txt em tool-results.
   Converta todos de uma vez: `python3 scripts/decodificar_drive.py /tmp/fotos <txt1> <txt2> ...`
   Abra uma prancha de miniaturas para VER as fotos antes de escolher (Read numa imagem montada com PIL).
   Baixe só o necessário (no máx. ~12 por perfil por dia).
5. **Escrever os 6 carrosséis** (ver pilares abaixo). Cada um: capa + 8 fatias, 40–80 palavras por fatia,
   último parágrafo com `<span class='hl'>…</span>`. Duas passadas: escreve, depois reescreve pelo humanizer.
6. **Casar foto com slide.** Foto que combina com o texto do slide. Lembre: o texto cobre a metade de baixo
   das fatias, então foto com o assunto no meio/alto. Capa usa a foto mais forte. Slide sem foto boa fica escuro.
7. **Renderizar.** Para cada carrossel, grave um JSON e rode
   `python3 scripts/render_carrossel.py cfg.json posts/AAAA-MM-DD/<perfil>-<n>`
   (perfil = `liurialves` ou `spatherapieslisbon`, n = 1..3). Use o logo do perfil (seção Logos).
   Confira visualmente pelo menos a capa e uma fatia de cada carrossel.
8. **Subir.** Atualize `estado/historico.json` e rode `bash scripts/publicar_github.sh`.
   Teste com curl que uma URL de cada carrossel responde 200.
9. **Buffer.** Antes, conte posts agendados (`list_posts` status scheduled): o plano aceita no máx. 10.
   Para cada carrossel, `create_post` com `mode: addToQueue`, `schedulingType: automatic`,
   `metadata.instagram = {type: "post", shouldShareToFeed: true}`, `assets` = as 9 imagens na ordem
   CAPA, fatia-1 … fatia-8 (cada uma com altText curto), `text` = legenda.
   Intercale perfis/pilares. Salve o `buffer_post_id` no histórico e faça novo commit+publicação.
9b. **TikTok (@liurialves).** Reaproveite os 3 carrosséis do @liurialves do dia no TikTok, com as MESMAS
   9 imagens (mesmas URLs). `create_post` no canal TikTok com `schedulingType: automatic`,
   `mode: customScheduled` e `dueAt` hoje às **13:05, 19:35 e 22:15** (hora de Lisboa, offset correto;
   se o horário já passou, use o próximo livre). A fila do TikTok no Buffer só tem 2 horários por dia,
   por isso NÃO use addToQueue aqui. `metadata.tiktok.title` = frase curta (até ~60 caracteres) que gere
   curiosidade. Legenda TikTok: 2 a 3 frases + CTA na mesma linha + 6 a 7 hashtags (inclua #fyp).
   Nada de "link na bio" sem link; prefira "comenta X" / "manda X no direct" / "salva".
   Antes de criar, confira o total de posts agendados no Buffer (limite 10 no plano). Instagram tem
   prioridade: se faltar vaga, deixe o TikTok de fora e diga no relatório.
   Guarde os ids em `historico.json` no campo `tiktok_post_id` de cada post do liurialves.
10. **Relatório.** Termine com um resumo curto: capas do dia, horário em que cada um entrou na fila,
    e qualquer problema (falta de fotos, erro no Buffer).

Se algo falhar no meio, publique o que ficou pronto e explique no relatório. Nunca use `shareNow`.

## @liurialves — marca pessoal
Público: brasileiro na Europa que trabalha pesado para outro e quer ter o próprio serviço com clientes.
Liuri: 28 anos, brasileiro em Lisboa, pai e marido, pratica MMA, entrou na Aeronáutica aos 19 por
necessidade financeira (lá ganhou disciplina), saiu por querer algo maior, ~10 anos em massagem,
hoje tem empresa (Lisboa Massagem: plataforma + anúncios para terapeutas), cria sites e faz tráfego pago.
Não pode parecer coach genérico, guru ou milionário de Instagram. Pode mostrar família, treino, Lisboa, rotina.
Voz: Darkgram, confronto em 2ª pessoa ("você"), PT-BR, agressiva para vendas, sem jargão de IA.

Pilares (3 por dia, sempre 3 diferentes):
1. **História** — Aeronáutica, chegada à Europa, massagem, virada, família.
2. **Cliente e marketing** — anúncio, página, WhatsApp, agenda cheia, erros de quem não tem cliente.
3. **Rotina de quem empreende** — conciliar trabalho, treino de MMA, família, cansaço, disciplina.
4. **Confronto do imigrante** — trabalhar no horário de outro, adiar o próprio negócio, medo de largar o salário.
5. **Bastidor da construção** — plataforma, serviço de marketing, sites para clientes, números reais só se o Liuri informou.

CTAs (rodar, nunca dois iguais seguidos): Comenta CLIENTE que eu te mando o checklist ·
Salva pra ler de novo amanhã · Manda pra aquele amigo que vive dizendo que vai abrir o próprio negócio ·
Link na bio · Me chama no direct.
Hashtags (escolha 8–10): #empreendedorismo #brasileirosemportugal #brasileirosemlisboa #brasileirosnaeuropa
#negocioproprio #trafegopago #marketingdigital #disciplina #lisboa #mma #empreendedorbrasileiro #metaads
#vidadeempreendedor #imigrantes

## @spatherapieslisbon — massagem / Lisboa Massagem
Objetivo: agendar massagens e levar terapeutas para a plataforma **lisboamassagem.pt**.
Idioma: português de Portugal, tratando o leitor por "tu" (passas, sentes, marca). Ecrã, telemóvel, marquesa, portátil.
Voz: Darkgram adaptado, direto e concreto, confronta o descuido com o corpo, nunca a pessoa.
Proibido: promessa médica, cura, "trata doença", números clínicos sem fonte. Nada sensual.
Categorias permitidas no conteúdo: relaxante, terapêutica, desportiva, drenagem linfática, reflexologia,
massagem a casal e ao domicílio. As categorias sensuais/tântricas do site NUNCA entram no Instagram
(risco de restrição da conta).

Identidade visual do spa (paleta do site lisboamassagem.pt, cor principal `#C9A486`):
- No JSON do render use `"accent": "#C9A486"` (destaque areia/dourado em vez do amarelo).
- Paleta de apoio: areia `#C9A486`, café `#1E1712`, creme `#F4EDE4`, oliva `#5E6B4A`, terra `#8A6448`.
- Fundos gerados com a paleta em `assets/spa-fundos/` (01-luz-quente, 02-linho, 03-ondas, 04-ripado,
  05-oliva, 06-vela). Use-os nos slides sem foto boa, no lugar do fundo preto. Dá para gerar novos com PIL
  na mesma paleta, se quiser variar.
- Vídeos (.mov/.mp4) da pasta do spa também servem: extraia frames com ffmpeg
  (`ffmpeg -ss <seg> -i video -frames:v 1 -q:v 2 frame.jpg`), em 3 a 4 momentos diferentes. Se o vídeo tiver
  texto sobreposto no topo (ex.: "Agende sua massagem"), corte os 16% de cima.
- Cards do site já prontos em `assets/spa-site/` (01-home, 02-busca, 03-como-funciona, 04-terapeutas):
  janela de navegador com os textos reais do site na paleta da marca. A janela fica na metade de cima,
  então funcionam bem como capa ou em fatias sobre a plataforma. Use 1 card por post no máximo e só nos
  posts que falam da plataforma (terapeutas, como marcar). Se o texto do site mudar, edite
  `scripts/gerar_cards_site.py` e rode de novo.
- Prints do site: pasta do Drive `prints-site` (id `1TveVh4LuBtAExDu1Dz5AqA-nIftx_SuA`). Quando houver prints, use-os nos
  posts sobre a plataforma (terapeutas e "como funciona").

Fatos do site que podem ser usados (são do próprio site): terapeutas verificados; contacto direto por WhatsApp;
terapeutas que vão ao domicílio; busca por distrito, categoria ou nome; registo e anúncio grátis para
terapeutas; plano Elite com destaque na busca; o site fala em 83+ terapeutas em 13 cidades (use só como
"mais de 80 terapeutas" e só se o site ainda disser isso). CTAs do site: "Pedir massagem agora",
"Anuncie-se grátis", "Cadastre-se grátis".

Pilares (3 por dia; trate a pasta `fotos/spatherapieslisbon` + vídeos + fundos da paleta como banco do spa; nunca use fotos pessoais do Liuri aqui):
1. **Corpo no dia a dia** — pescoço do computador, lombar do carro, tensão do stress, sono ruim. Cena concreta.
2. **Massagem explicada** — tipos (relaxante, desportiva, terapêutica, drenagem…), o que esperar, para quem.
3. **Mito ou verdade / erro comum** — dor depois da massagem, frequência, "só quando dói".
4. **Para terapeutas** (1 por dia) — agenda vazia, depender de espaço alheio, anunciar na plataforma
   lisboamassagem.pt.
5. **Agenda / convite** — chamar para marcar, sem soar desesperado.

CTAs: Marca a tua massagem pelo link na bio · Guarda este post · Envia a quem vive com o pescoço travado ·
Terapeuta? Anuncia em lisboamassagem.pt · Comenta MASSAGEM que respondemos no direct.
Hashtags (8–10): #massagemlisboa #lisboa #massagem #massagemrelaxante #massagemterapeutica #bemestar
#lisbon #massagelisbon #spalisboa #autocuidado #terapeutas #portugal

## Regras que valem para os dois
- Nunca escrever "bico"; use "extra".
- Nunca inventar números, depoimentos ou clientes.
- Legenda no formato da skill (ataque, desenvolvimento, virada, 🔻 CTA, hashtags), sem travessão.
- Fotos com marca d'água de fotógrafo (ex.: Roberto Castro Fotografia): evitar.
- Palavras sensíveis à moderação com # no meio (m#rte etc.), como na skill.
