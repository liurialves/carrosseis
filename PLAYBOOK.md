# Playbook — carrosséis diários (@liurialves e @spatherapieslisbon)

Rotina executada todo dia por uma tarefa agendada. Cada execução começa do zero,
então TUDO o que ela precisa está aqui. Siga na ordem.

## Meta do dia
3 carrosséis para **@liurialves** + 3 carrosséis para **@spatherapieslisbon** (agendados no Buffer) +
**1 a 2 Reels para @liurialves** que NÃO são publicados: ficam na pasta do Drive para o dono escolher a
música e postar (passos 9a e 9d),
feitos com a skill **um-clique-darkgram**, imagens hospedadas neste repositório,
agendados no **Buffer** com horário fixo por perfil (ver passo 9).
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
  - `fotos/pexels` (fotos de banco de imagem livres, para misturar no @liurialves): `1BDJzj3zYgQCR7v7fOZ4K2GyDinD8oRRe`
  - `logos`: `1ggQNwpr9shcrdN63y0NGjDk819iDj8na` (PNG com "liuri" ou "spa" no nome)
  - `tiktok-spa` (pacotes diários para repostar no TikTok da massagem): `1nbhLyU6A8MAHIeF6hsdEDuSfPV8kMzU6`
  - `prints-site` (prints de lisboamassagem.pt): `1TveVh4LuBtAExDu1Dz5AqA-nIftx_SuA`
- Drive `reels` (vídeos do dia para o dono editar): `1wqJjbKdmrlIroQ02CTcjMX3xfl6R6Mjs`
  - `reels/meus-videos-falando`: `1605m4VFoz-BKVgfAJ208onI6JxXuVvIW` · `reels/referencias`: `1y84a3PcRXrgmIJ0uUlJFfw36okChd9SV`
- Pexels API: chave como network secret do ambiente (host `api.pexels.com`) ou variável `PEXELS_API_KEY`;
  rede com `api.pexels.com` e `images.pexels.com` liberados. Script: `scripts/buscar_pexels.py`.
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
   No @liurialves vale a seção "Fase atual: FUNIL DE VENDAS" (que substituiu a fase CRESCIMENTO em 22/10/2026)
   e, no que não conflitar com ela, as regras da fase CRESCIMENTO: quando divergirem da skill (ex.: lista com
   promessa específica, pergunta fechada no fim, opinião impopular), ela prevalece. Densidade, humanizer,
   sem travessão e sem paralelismo continuam obrigatórios.
6. **Casar foto com slide.** Foto que combina com o texto do slide. Lembre: o texto cobre a metade de baixo
   das fatias, então foto com o assunto no meio/alto. Capa usa a foto mais forte. Slide sem foto boa fica escuro.
7. **Renderizar.** Para cada carrossel, grave um JSON e rode
   `python3 scripts/render_carrossel.py cfg.json posts/AAAA-MM-DD/<perfil>-<n>`
   (perfil = `liurialves` ou `spatherapieslisbon`, n = 1..3). Use o logo do perfil (seção Logos).
   Confira visualmente pelo menos a capa e uma fatia de cada carrossel.
8. **Subir.** Atualize `estado/historico.json` e rode `bash scripts/publicar_github.sh`.
   Teste com curl que uma URL de cada carrossel responde 200.
9. **Buffer.** Antes, conte posts agendados (`list_posts` status scheduled): o plano aceita no máx. 10.
   Horários do Instagram (definidos em 13/10/2026 a partir do alcance dos posts enviados pelo Buffer;
   a API do Buffer não deixa mudar a grade da fila, por isso usamos horário fixo):
   - @liurialves: **12:10, 14:20 e 17:40** (hora de Lisboa) → carrossel 1, 2 e 3.
   - @spatherapieslisbon: **08:25, 12:45 e 15:20** → carrossel 1, 2 e 3.
   Para cada carrossel, `create_post` com `mode: customScheduled`, `dueAt` = hoje no horário acima com o
   offset correto de Lisboa (se o horário já passou, use o mesmo horário no dia seguinte), `schedulingType: automatic`,
   `metadata.instagram = {type: "post", shouldShareToFeed: true}`, `assets` = as 9 imagens na ordem
   CAPA, fatia-1 … fatia-8 (cada uma com altText curto), `text` = legenda.
   Intercale perfis/pilares. Salve o `buffer_post_id` no histórico e faça novo commit+publicação.
9a. **Reels (@liurialves), 1 a 2 por dia NO TOTAL (contando os falados do 9d): NÃO publicar.** O dono edita o áudio à mão e publica ele mesmo.
   Regras de 17/10/2026 (análise de 39 Reels; ver "Aprendizados" abaixo). Elas valem sobre o resto deste passo:
   - **Prioridade:** se houver vídeo falado novo (9d), ele é o Reel do dia e entra no máximo mais 1 Reel de frases.
     Sem falado novo, faça 2 Reels de frases.
   - **Curto:** 4 a 5 frases, `"segundos_por_frase": 2.2`, total de 9 a 12 s. Nunca passar de 15 s.
   - **Gancho com conflito na 1ª frase:** comparação ou provocação ("Ringue e negócio cobram igual",
     "Seu salário depende de uma pessoa só"). Nada de frase só de ambientação ("Domingo, 21h", "Você chegou com duas malas").
   - **Série "Ringue e negócio #N"** (o tema do Reel campeão, 2.323 visualizações): pelo menos 3 vezes por semana,
     1 dos Reels do dia é dessa série (uma lição do MMA/tatame aplicada a cliente, venda ou empresa). Registrar o número
     da série no histórico e continuar a contagem.
   - **CTA:** pergunta que se responde com 1 palavra ligada ao tema ("Comenta RINGUE se você já apanhou no negócio") ou
     uma virada de humor. Evitar CTA genérico ("comenta EU", "comenta FANTASMA" tiveram zero comentários).
   Estilo visual: fotos escuras em preto e branco trocando a cada ~1,1 s, zoom lento, frase curta branca no centro e
   @liurialves pequeno embaixo.
   - **Texto:** frases curtas (2 a 7 palavras) que formam uma ideia só. Temas dos pilares de crescimento, com
     prioridade para MMA/treino ligado a negócio. Voz do Liuri, PT-BR, sem jargão de IA, sem travessão. Não repetir
     frases dos Reels dos últimos 14 dias.
   - **Imagens:** 2 por frase. PRIORIDADE para material do Liuri: fotos dele (Drive, pastas `fotos/*`), frames dos
     vídeos dele que caibam no limite de 10 MB do Drive (treino, MMA, atendimento, bastidor) e fotos novas que ele
     subir em `fotos/liurialves`. Pexels só para completar, no máximo metade das imagens, e sempre em cena de
     treino/luta/trabalho (termos tipo "boxing bag gym dark", "mma training dark", "dumbbells dark gym",
     "laptop desk dark night"). A 1ª e a última frase usam foto ou frame do Liuri. Fotos do Liuri no estande de tiro podem entrar (regra de 21/10/2026); nada de arma vinda do Pexels, marca d'água ou
     rosto de famoso.
   - **Áudio:** SEM música (o dono põe a música no Instagram/CapCut). Não passe `"musica"` no JSON.
   - **Render:** grave `reel.json` e rode `python3 scripts/render_reel.py reel.json reels/AAAA-MM-DD/reel-N.mp4`.
     Confira 2 frames (ffmpeg). Publique com `bash scripts/publicar_github.sh` e teste com curl que a URL
     responde 200 (os vídeos ficam 7 dias no repositório).
   - **Drive:** na pasta `reels` (id `1wqJjbKdmrlIroQ02CTcjMX3xfl6R6Mjs`) crie a subpasta do dia (`AAAA-MM-DD`)
     e dentro dela, com `create_file` (contentMimeType `text/html`, vira Google Doc), o documento
     `Reels - AAAA-MM-DD`: no topo "Baixe nos próximos 7 dias; os links expiram depois". Para cada
     Reel: título, link de download do MP4, as frases na ordem com o segundo em que entram (0,0 s; 2,4 s; ...),
     sugestão de clima de música (ex.: "piano escuro lento, 70–80 bpm") e legenda pronta para Instagram e
     TikTok. A legenda NUNCA pode ir vazia ou só com emoji: 1 linha com palavra-chave (MMA, empreender, Lisboa,
     brasileiro em Portugal) + pergunta + CTA + 3 a 5 hashtags. No topo do doc, lembrar: "Publique no máximo 1 a 2
     Reels por dia e nunca deixe a legenda vazia". Nunca envie o vídeo em si ao Drive.
   - **Não** criar posts de Reel no Buffer. Registrar no `historico.json` com `"tipo": "reel"`, frases e fotos.
   - No relatório: o link da pasta do dia em `reels`.
9d. **Reels falados e referências (pastas do Drive dentro de `reels`).**
   - `reels/meus-videos-falando` (id `1605m4VFoz-BKVgfAJ208onI6JxXuVvIW`): vídeos do Liuri falando para a câmera.
     Para cada vídeo novo (não listado em `historico.json` como `falado_origem`): baixe e edite no **estilo
     animado** (pedido do dono em 15/10/2026, referência: Reel do Matheus/FitFolio, ver `estado/referencias.md`):
     1. Transcreva: `python3 scripts/transcrever.py video.mp4 /tmp/t.json` (Whisper small offline; baixa o modelo
        do GitHub na 1ª vez, ~640 MB). Corrija à mão os erros óbvios. Ache as pausas pela energia do áudio para
        acertar o tempo de cada frase.
     2. Recorte 3 a 5 figurinhas dele (frames com gesto: dedo para cima, apontando, sorrindo) com `rembg`
        (modelo `u2net_human_seg` de github.com/danielgatis/rembg/releases, em `~/.u2net/`) e contorno branco.
     3. Monte o EDL e rode `python3 scripts/render_reel_animado.py edl.json reels/AAAA-MM-DD/falado-N.mp4`.
        Regras do estilo: corta o silêncio do início; a voz dele corre o vídeo todo (nunca música); alterna
        **rosto** (zoom lento, punch-in de 1.25 a 1.35 nas frases de impacto, legenda de no máximo 3 palavras por
        vez, palavra-chave em amarelo e "falência/perigo" em vermelho) com **tela preta** a cada 3 a 5 s nas
        frases com número, conceito ou virada: palavras a aparecer uma a uma, número gigante amarelo (Anton),
        palavra manuscrita (Caveat) com seta a desenhar-se, figurinha dele a balançar, carimbo vermelho na frase
        de corte ("ACABOU.") e, no CTA, botões "1 CONCORDO / 2 DISCORDO" (ou a palavra do CTA) + "comenta aqui".
        Nunca dois blocos de rosto seguidos com o mesmo zoom; nenhum bloco acima de 4,5 s.
     4. Confira 6 a 8 frames e a duração final. Link no doc do dia com legenda pronta. Conta como um dos 1 a 2
        Reels do dia (e tem prioridade sobre os de frases). Se o download falhar por tamanho, diga no relatório e peça o vídeo em 720p.
     Os vídeos que o dono mandar direto na conversa seguem o mesmo processo.
   - `reels/referencias` (id `1y84a3PcRXrgmIJ0uUlJFfw36okChd9SV`): Reels de outros perfis que o dono gostou. Para
     cada novo: baixe, faça uma prancha de frames e meça os cortes (ffmpeg scene detection). Anote em
     `estado/referencias.md` o estilo (ritmo, tipo de imagem, texto, gancho, duração) e aplique no máximo 2
     elementos novos nos Reels do dia. Nunca copie texto, imagem ou áudio da referência.
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
9c. **Pacote TikTok do spa (repost manual pelo Liuri).** Depois de os 3 carrosséis do @spatherapieslisbon
   estarem no Buffer:
   - Rode `python3 scripts/pacote_tiktok_spa.py AAAA-MM-DD` (cria `tiktok-spa/AAAA-MM-DD/` com as imagens
     numeradas 01-09 e um ZIP por carrossel, e imprime as URLs). Rode `bash scripts/publicar_github.sh` e
     confirme com curl que um ZIP responde 200.
   - No Drive, dentro da pasta `tiktok-spa`, crie uma subpasta com o nome do dia (`AAAA-MM-DD`).
   - Dentro dela, crie com `create_file` (contentMimeType `text/html`, vira Google Doc) o documento
     `TikTok spa - AAAA-MM-DD (3 posts)` no mesmo formato do de 2026-10-11: instrução curta de uso no topo e,
     para cada post: título da secção, `<img>` da capa (width 240), link do ZIP, links das 9 imagens soltas,
     **Título** TikTok (até ~60 caracteres, gera curiosidade) e **Legenda** TikTok em português de Portugal
     (2 a 3 frases + CTA + 6 a 7 hashtags com #fyp). Nunca coloque os ficheiros de imagem em si no Drive.
10. **Relatório.** Termine com um resumo curto: capas do dia, horário em que cada um entrou na fila,
    e qualquer problema (falta de fotos, erro no Buffer).

Se algo falhar no meio, publique o que ficou pronto e explique no relatório. Nunca use `shareNow`.

## Avisos pontuais (apague depois da data)
- **25/10/2026:** a rotina de 24/10 rodou tarde (12h) e já deixou o carrossel 1 do spa de 24/10 agendado para
  **25/10 às 08:25**. Nesse dia faça só **2** carrosséis do spa (12:45 e 15:20) e os 3 do @liurialves. Lembrete: em
  25/10 Portugal volta para a hora de inverno (offset `+00:00`).
- **21/10/2026 (permanente):** o dono liberou as fotos religiosas e as fotos dele no estande de tiro (ver "Liberado pelo dono em 21/10/2026" na seção do @liurialves). Se o texto da tarefa agendada ainda disser "nem fotos com arma", vale esta regra mais nova do dono: no @liurialves pode; no spa continua proibido.
- **16/10/2026:** o dono já agendou pelo chat 2 carrosséis do @liurialves em formato de frase (tweet às 10:30 e
  foto às 20:30; ver `historico.json`, `origem: chat`). Nesse dia faça só **2** carrosséis normais do
  @liurialves (12:10 e 17:40, sem formato de frase), os 3 do spa e o TikTok dos 2 carrosséis normais + o tweet
  (mesmas URLs de `posts/2026-10-15/liurialves-4`). Assim o Buffer fica em 2 + 2 + 3 + 3 = 10.
- Regra geral: antes de criar, some no limite de 10 os posts que já estiverem agendados no Buffer para o dia.

## Aprendizados da semana (atualizado toda segunda pela análise semanal)
Esta seção é reescrita pela tarefa "Análise semanal de crescimento". A rotina diária DEVE aplicá-la:
ela tem prioridade sobre escolhas de tema, gancho e formato (nunca sobre IDs, limites, horários fixos e
regras de segurança). Histórico completo em `estado/analises/`.
**Semana de 19/10/2026** (Buffer, 12–18/10 vs 21/09–11/10; completo em `estado/analises/2026-10-19.md`)
- **Funcionou:** gancho de história real em 1ª pessoa com foto própria: 125 de alcance médio, 8 curtidas e 7,3% de
  engajamento. Melhor carrossel: "Eu casei e segurei meu filho no colo vestindo a farda..." (216 de alcance, 16 curtidas,
  2 comentários). Em setembro, "Esse garoto na chuva sou eu" teve 14 comentários. Reels do Liuri em cena continuam no
  topo ("Ringue e negócio": 1.860 de alcance; "Be strong" de 18/10: 1.374). Capa com foto própria teve 97 de alcance,
  contra 48 com Pexels. Os horários das 20–22h renderam 110–126, contra 49 às 12h.
- **Cortar:** a capa começando por "Opinião impopular:" (57 de alcance, 0 comentários) e a série "Modo fantasma" (48 de
  alcance, 0 comentários; o #4 teve 27). Também os CTAs "Responda 1 ou 2", "SIM ou NÃO" e "Siga para a parte 2", que
  tiveram 0 comentários em 7 posts. Na mesma linha: Pexels na capa, Reel sem legenda (~30 de alcance) e mais de 2 Reels
  por dia. O alcance dos carrosséis caiu de 115 para 78 (−33%) quando o volume diário passou de ~2 para ~10 posts.
- **Ajustes desta semana (@liurialves):**
  1. Pilares prioritários: História do Liuri, Homem cru (com MMA) e confronto do imigrante com cena real. Cliente e
     negócio no máximo 1 por dia. Opinião impopular: a tese pode existir, mas a capa abre com uma cena vivida, nunca
     com a etiqueta "Opinião impopular:".
  2. 1 dos 3 carrosséis do dia é da série **"Ringue e negócio #N"** (uma lição de MMA aplicada a cliente ou empresa),
     com foto de treino do Liuri na capa. A numeração continua a mesma dos Reels.
  3. Capa sempre com foto própria. Pexels só nas fatias.
  4. CTA: um carrossel por dia com envio ("Envie para o amigo que chegou a Portugal este ano") e os outros com
     pergunta de experiência ("Comente qual foi a primeira coisa que você cortou"). No máximo 5 hashtags (limite do
     Instagram desde dez/2025), nos dois perfis.
  5. TikTok: o título e a 1ª linha da legenda trazem palavras de busca ("brasileiro em Portugal", "disciplina",
     "MMA", "empreender em Lisboa"). Em 4 semanas foram 0 comentários.
- **8 ganchos para testar (@liurialves):**
  "Eu dirigia Uber em Lisboa e foi no banco do carro que aprendi a primeira regra de vendas" ·
  "Ringue e negócio #2: o treinador que me corrigiu sem levantar a voz me ensinou a falar com cliente" ·
  "Aos 19 entrei na Aeronáutica por necessidade. O motivo pelo qual saí muita gente achou loucura" ·
  "Meu filho me viu sair para o treino de manhã cedo. Foi a conversa mais importante que tive com ele sobre disciplina" ·
  "Dez anos atendendo clientes de massagem me mostraram por que uns voltam e outros somem, e não é o preço" ·
  "Ringue e negócio #3: quem só bate no saco de pancada nunca aprende a apanhar, e na empresa acontece o mesmo" ·
  "O que eu faria diferente nos primeiros 90 dias em Portugal (envie para quem acabou de chegar)" ·
  "Na Aeronáutica eu tinha horário para tudo. Em Lisboa ninguém me dizia a hora de acordar, e foi aí que a disciplina foi testada"
- **Spa:** o alcance está estável (~127), mas o engajamento é de 0,7% e houve 0 partilhas em 4 semanas. Priorizar "corpo
  no dia a dia" (142) e "para terapeutas" (único pilar com comentários). Cortar "agenda/convite" (81). A 1ª linha da
  legenda leva "massagem + zona de Lisboa" (os posts entram no Google). O CTA de envio nomeia uma pessoa concreta.
  3 ganchos: "Envia isto a quem passa uma hora por dia no IC19 agarrado ao volante" · "Massagem ao domicílio em Lisboa:
  o que o terapeuta traz e o que tens de preparar" · "Terapeuta em Lisboa: o cliente procura massagem desportiva perto
  de casa e o teu perfil não diz a zona onde atendes".
- **Reels (dono):** no máximo 2 por dia e nunca sem legenda. Gravar "Ringue e negócio" em cena de treino real e usar
  trial reel para testar 1 gancho novo por semana.
- **Recomendação de horário (o dono decide; o passo 9 não mudou):** trocar o slot das 12:10 do @liurialves por ~20:30.
- **Teste A/B da semana:** alternar por dia o CTA do carrossel das 17:40. Dias pares usam A, de envio ("Envie para o
  amigo que..."); dias ímpares usam B, de comentário com palavra ligada ao tema. Registrar `"ab": "A"` ou `"B"` no
  histórico. Métrica: (partilhas + comentários) por 100 de alcance em 48 h. Vence quem tiver ≥30% a mais.
- Base de 17/10 (Reels) continua valendo: Liuri em cena ~800 views, contra ~160 de foto com frase. Humor puxa comentário.

## @liurialves — marca pessoal
### Fase atual: FUNIL DE VENDAS (desde 22/10/2026, substitui a fase CRESCIMENTO)
Pedido do dono em 22/10/2026: "não quero conteúdo por criar conteúdo; quero alcance, vendas e funil".
Referência: print do @alfredosoares "Seu conteúdo serve pra fechar negócio" (só a estrutura, nunca copiar
texto ou arte). Esta seção PREVALECE sobre tudo o que vem abaixo dela no @liurialves (fase CRESCIMENTO,
mecânica de engajamento, lista de CTAs) e sobre a regra "cliente e negócio no máximo 1 por dia" dos
Aprendizados. A análise semanal pode ajustar temas e ganchos dentro de cada etapa, mas não pode tirar o funil.

**O que o funil vende (ofertas reais do Liuri):** treinamento de marketing para empresas; site;
estratégia de marketing + tráfego pago (gestão de anúncios); kit digital para pequenas empresas.
Público comprador: dono de pequena empresa e profissional autônomo, com prioridade para estética, massagem,
beleza e serviços locais, brasileiros em Portugal e no Brasil. Nunca inventar preço, prazo, resultado de
cliente, depoimento ou número; se não houver dado real, fale do processo.

**As 5 etapas (da referência) e onde cada uma acontece:**
1. **Atrair o comprador** (topo, alcance): conteúdo polêmico que fala do problema que a oferta resolve.
   Tese forte contra práticas do mercado: "postar todo dia não vende", "impulsionar post é jogar dinheiro
   fora", "seu Instagram bonito não traz cliente", "agência que só entrega arte", "o sobrinho que faz o seu
   site", "curso de marketing que você nunca aplicou", "você depende de indicação e chama isso de
   negócio". Pode dividir opinião e gerar crítica: o dono pediu para NÃO evitar polêmica por medo de hate.
   Limites que continuam: nada contra mulheres, religião, política, raça, orientação ou nacionalidade;
   nada de humilhar pessoa (o alvo é a prática); nada de número inventado ou promessa de faturamento.
   CTA: comentar uma palavra, opinar, enviar para alguém, seguir.
2. **Ensinar e mostrar a dor** (meio): explicar por que o problema acontece, com cena concreta e um
   passo que a pessoa pode aplicar hoje (ex.: "3 coisas que o seu perfil precisa ter antes de você pagar
   anúncio", "por que o cliente pergunta o preço e some", "a página que eu monto antes de ligar o tráfego").
   Mostra autoridade pela vida real (empresa Lisboa Massagem, 10 anos atendendo, sites e anúncios que ele faz).
   CTA: salvar + "se quiser que eu olhe o seu caso, clique no link da bio e me chame no WhatsApp".
3. **Oferecer o próximo passo / mostrar como eu resolvo** (fundo): apresentar o método e a oferta com
   clareza: o que é, para quem é, o que a pessoa recebe e como começa. O próximo passo é sempre uma
   **conversa de diagnóstico grátis no WhatsApp** (análise do perfil/site/anúncio). Pode alternar a oferta
   em foco: treinamento, site, estratégia + tráfego, kit digital.
4. **Captar o contato:** o site do Liuri está no link da bio e tem o botão de WhatsApp. Todo CTA de
   venda é: "Clique no link da bio e me chame no WhatsApp com a palavra X" (X ligada ao tema: SITE,
   TRÁFEGO, KIT, TREINAMENTO, DIAGNÓSTICO). Use uma palavra diferente por oferta para o dono saber de qual
   post o lead veio. Não usar "comente que eu mando no direct" nos posts de fundo (o contato precisa
   chegar ao WhatsApp).
5. **Qualificar e iniciar a conversa comercial:** acontece no WhatsApp, com o roteiro do dono (ver
   `estado/funil-whatsapp.md`). O conteúdo prepara isso: no fundo de funil, diga para quem a oferta
   NÃO é (ex.: "se você ainda não tem um serviço definido, isto não é para você agora"), o que filtra curioso.

**Distribuição diária dos 3 carrosséis do @liurialves (ordem dos horários do passo 9):**
- 12:10 → etapa 1 (alcance/polêmica). O formato foto ou tweet do dia entra aqui.
- 14:20 → etapa 2 (ensinar e mostrar a dor).
- 17:40 → etapa 3 (como eu resolvo + oferta + CTA WhatsApp com palavra). O teste A/B de CTA de envio
  fica suspenso enquanto o funil estiver ativo.
- "Ringue e negócio" deixa de ser obrigatório todo dia: entra no máximo 3 vezes por semana, como etapa 1 ou 2,
  sempre com a ponte para cliente, venda ou anúncio. História do Liuri e homem cru entram como etapa 1
  quando a ponte para negócio for clara.
- Os 3 do dia falam do MESMO problema em profundidades diferentes (ex.: 12:10 "impulsionar post é jogar
  dinheiro fora", 14:20 "o que eu confiro antes de ligar um anúncio", 17:40 "como eu monto estratégia + tráfego
  para pequenas empresas: chame no WhatsApp com a palavra TRÁFEGO"). Assim quem chega pelo alcance encontra
  o resto do caminho no perfil no mesmo dia.
- Legenda do fundo de funil: 1ª linha com a dor + quem é o cliente ("Dono de clínica de estética em Lisboa..."),
  depois o que a pessoa recebe, para quem não é, e o CTA do WhatsApp com a palavra. Máximo 5 hashtags.
- TikTok: mesma lógica; no fundo de funil, "link no perfil" só se o site estiver na bio do TikTok; se não
  souber, use "manda DIAGNÓSTICO no direct".
- Tom: continua o de 17/10 (masculino, seguro, formal, sem gíria), só que mais direto na venda: afirmar,
  confrontar a prática errada e pedir a ação sem rodeio. Nada de "talvez", "se fizer sentido para você".
- Registrar no histórico o campo `"funil": "alcance" | "dor" | "oferta"` e a palavra do CTA em `"palavra_cta"`.

**Fase anterior (14/10 a 21/10/2026): CRESCIMENTO.** O objetivo nº 1 era comentário, curtida, salvamento e
SEGUIR a conta, com no máximo 1 CTA de venda por dia. As regras abaixo continuam valendo só no que não
conflitar com o funil acima.

Público: homem brasileiro (20–40) na Europa ou no Brasil que trabalha pesado, quer disciplina, dinheiro
e o próprio negócio. Liuri: 28 anos, brasileiro em Lisboa, pai e marido, pratica MMA, entrou na Aeronáutica
aos 19 por necessidade financeira (lá ganhou disciplina), saiu por querer algo maior, ~10 anos em massagem,
hoje tem empresa (Lisboa Massagem: plataforma + anúncios para terapeutas), cria sites e faz tráfego pago.
Não pode parecer guru ou milionário de Instagram: a autoridade vem de vida real (treino, família, empresa,
imigração). Voz: ver "Tom de voz (pedido do dono em 17/10/2026)" logo abaixo; ele prevalece sobre a skill.

**Tom de voz (pedido do dono em 17/10/2026, prevalece sobre o Darkgram e o humanizer em caso de conflito):**
o dono achou a linguagem "estranha". O texto do @liurialves passa a ser **masculino, seguro e mais formal**:
um empresário que já fez e fala com calma, sem gritar e sem gíria.
- Português correto: "para" (nunca "pra"), "está", "você está"; nada de "kkk", "mano", "cara", "bora", "tipo",
  "bué", "fixe", "galera". CTAs no imperativo formal: "Comente", "Salve", "Siga", "Envie" (nunca "Comenta", "Salva").
- Frases completas e naturais. Proibido o estilo telegráfico e os aforismos montados ("Ninguém perde o foco de uma
  vez. Perde uma resposta de cada vez.", "Quem conta os dias já está procurando a porta"). Se a frase soa como
  pôster ou como tradução, reescreva como um homem experiente falaria numa reunião.
- Mais primeira pessoa com experiência ("Eu aprendi", "Na minha empresa", "Quando eu dirigia Uber") e menos
  acusação em série contra o leitor. Confrontar pode, humilhar ou dar bronca não.
- Sem exclamação, sem emoji no texto dos slides; na legenda no máximo o 🔻 antes do CTA.
- Vocabulário de negócio sóbrio: cliente, agenda, preço, margem, decisão, responsabilidade. Evitar palavras
  dramáticas ("guerra", "fera", "monstro", "sangue") e palavras de coach.
- Exemplo. Antes: "Opinião impopular: mais um curso não vai te dar cliente. Responde só com o número, sem vergonha."
  Depois: "Mais um curso não vai trazer clientes para você. Comente quantos cursos você já comprou e ainda não
  colocou em prática."

Referências de estilo (o dono mandou prints em 13/10; NUNCA copiar texto ou imagem deles, só tema e formato):
@homemricooficial, @mentalidade_milionaria, @olobo_silencioso, @homemcru, @yearlikeaghost, @thetrillionairelife.
O que eles têm em comum e que vamos usar:
- **Lista com promessa e isca no número** (o formato mais forte do @homemricooficial): "Coisas que a vida
  militar ensina que a escola nunca ensinou", "7 lugares para onde o seu salário vai sem você perceber
  (o nº 4 quase todo mundo ignora)", "5 lições de homem para homem". Capa com contagem + "(a 5ª ...)".
- **História-parábola de abertura**: "Um jovem árabe rico foi estudar na Alemanha. Depois de um mês escreveu
  ao pai..." No nosso caso a história é do Liuri (verdadeira) ou é apresentada claramente como fábula
  ("conta-se que..."); nunca inventar fato real.
- **Comparação antes/depois em 2 imagens** na capa ("Doença aos 50 / começa aos 18", "farda / hoje").
- **Frase de impacto em fundo escuro com destaque dourado** (@olobo_silencioso): "Eu não confio em
  motivação. Confio no que continua de pé quando ela some." Ótima para salvar e compartilhar.
- **Regras / manual**: "Como ser um homem 10/10", "As regras de Maquiavel" (clássicos de domínio público,
  citados com fidelidade).
- **Curiosidade sobre dinheiro e gente rica**: só com fato verificável e fonte na legenda. Frase de
  famoso só se for citação real e conhecida; nada de "Elon Musk disse" inventado.
- **O que NÃO copiar**: teoria da conspiração, cura escondida, "a CIA documentou", sal ao lado da cama,
  demônio/superstição, luxo ostentação de bilionário (@thetrillionairelife) e citação falsa. Isso dá
  alcance mas destrói a credibilidade do Liuri, que vende serviço real.
Estética: foto forte ocupando a capa, texto em caixa alta com 1 ou 2 palavras em amarelo `#F5C518`,
clima escuro e cinematográfico. Nas fatias, preferir foto (Liuri ou Pexels) a fundo preto liso.
Sem foto boa para a fatia: usar um dos fundos de `assets/liuri-fundos/` (luz dourada, fumaça, persiana,
cidade à noite, holofote, brasa; gerados por `scripts/gerar_fundos_liuri.py`), nunca o preto liso.
Primeiro exemplo aprovado como modelo: "6 coisas que a Aeronáutica me ensinou aos 19 que nenhuma escola
teve coragem de ensinar (a 5ª eu uso até hoje)", com parte 2 prometida ("o que a vida de imigrante em
Lisboa me ensinou e a farda não"). Fazer essa parte 2 numa das próximas rotinas.

Formatos de frase (pedido do dono em 15/10/2026, referência @codiesanchez): **1 dos 3 carrosséis do dia**
usa um destes dois formatos, alternando dia sim, dia não, com `python3 scripts/render_frases.py cfg.json posts/...`
(ver o cabeçalho do script):
- **"tweet"**: fundo branco, avatar (`assets/avatar-liuri.jpg`, recorte da foto de perfil do Instagram `assets/foto-perfil-liuri.jpg`) + "Liuri Alves" + @liurialves, texto preto grande.
  9 slides, um pensamento curto por slide (1 a 3 frases, até ~45 palavras), todos sobre o mesmo tema, do
  gancho polêmico ao CTA no último. NUNCA colocar selo de verificado. Tom: frase de quem viveu, com cena real
  (agenda das 9h às 21h, WhatsApp às 23h, filho, MMA, empresa), sem jargão de coach.
- **"foto"**: 2 slides com foto dele (Drive ou frame de vídeo falado) e frase branca grossa embaixo. Slide 1 =
  situação que todo empreendedor reconhece, slide 2 = virada curta e engraçada ("Spoiler: é o chefe.").
  Humor seco, nada de indireta para pessoas.
Os dois formatos seguem as regras da fase de CRESCIMENTO (CTA de comentar/seguir/salvar) e entram no Buffer igual
aos outros (assets na ordem CAPA, fatia-1...).

Pilares (3 por dia, sempre 3 diferentes; pelo menos 1 polêmico por dia):
1. **Opinião impopular / polêmica** — tese forte que divide o público. Ex.: "Salário fixo é o vício mais
   caro do imigrante", "Fim de semana é invenção de quem não tem sonho", "Academia não te faz disciplinado".
   Defenda a tese com cena concreta e feche pedindo lado: "Concorda ou discorda? Responde com 1 ou 2."
2. **Modo fantasma** — sumir das festas, do scroll e da opinião dos outros para construir em silêncio.
   Desafios ("90 dias invisível"), regras, o que cortar. Tom escuro, quase manifesto. Série recorrente.
3. **Dinheiro e mentalidade** — hábitos e decisões sobre dinheiro, erro de quem ganha pouco e gasta igual
   a quem ganha muito, curiosidades sobre empresas e gente rica SÓ com fato verificável (cita a fonte na
   legenda; se não tiver fonte, não usa o número). Sempre com a ponte para a vida do Liuri/imigrante.
4. **Homem cru** — disciplina, MMA, ser pai, corpo, vício em tela, palavra dada, aguentar pressão.
   Confronto direto, sem coach.
5. **História do Liuri** — Aeronáutica, chegada a Lisboa, massagem, virada, família (prova de que é real).
6. **Cliente e negócio** — anúncio, página, WhatsApp, agenda cheia (1 por dia no máximo; é o único pilar
   que pode ter CTA de venda).

Ganchos que funcionam nesta fase (usar na capa, sempre com âncora concreta):
- Curiosidade com lacuna: "O que os homens que enriquecem fazem às 5h que você nunca vai fazer"
- Polêmica com lado: "Opinião impopular: ..." / "Ninguém tem coragem de dizer, mas..."
- Contraste de vida: "Aos 19 eu ganhava X na farda. Hoje..." (só número que o Liuri informou)
- Desafio: "Some por 90 dias e volta irreconhecível. As regras:"
- Lista com promessa específica (permitida nesta fase, mas cada item é cena, nunca tópico genérico):
  "4 coisas que eu cortei quando decidi parar de trabalhar para os outros"

Mecânica de engajamento (obrigatória em todo carrossel @liurialves):
- Slide 2 abre um loop ("e o terceiro item é o que ninguém faz") para segurar o arraste até o fim.
- Último slide: pergunta fechada que se responde com 1 palavra ou número ("1 ou 2", "SIM ou NÃO",
  "comenta FANTASMA se você topa"), MAIS "Segue @liurialves para a parte 2" quando for série.
- Legenda: 1ª linha repete a polêmica com outras palavras e termina numa pergunta; última linha antes das
  hashtags convida a marcar alguém ("Marca o amigo que precisa ouvir isso").
- Fixar a curiosidade: séries numeradas ("Modo fantasma #1, #2...") para gerar motivo de seguir.

Limites da polêmica (não negociáveis): nada contra mulheres, religião, política partidária, raça,
orientação ou nacionalidade; nada de humilhar quem trabalha de empregado (o alvo é o comportamento, não a
pessoa); nada de promessa de riqueza, renda garantida ou número inventado; nada de linguagem que a Meta
pune (palavras sensíveis com # no meio, como na skill). A polêmica é sobre escolhas e hábitos.

CTAs (rodar, nunca dois iguais seguidos):
Engajamento/seguir: Concorda ou discorda? Responde com 1 ou 2 · Comenta FANTASMA se você topa os 90 dias ·
Segue @liurialves para a parte 2 · Marca o amigo que precisa ouvir isso · Salva e lê de novo no domingo ·
Responde com SIM ou NÃO, sem desculpa.
Venda (só 1 por dia): Comenta CLIENTE que eu te mando o checklist · Me chama no direct com a palavra SITE.
Hashtags (escolha 8–10): #disciplina #mentalidade #homemdevalor #mentalidadeforte #empreendedorismo
#brasileirosemportugal #brasileirosnaeuropa #negocioproprio #mma #modofantasma #dinheiro #foco
#vidadeempreendedor #lisboa

**Liberado pelo dono em 21/10/2026:** as fotos religiosas do Drive (igrejas, altares, santuários das viagens) e as fotos do Liuri no estande de tiro podem ser usadas no @liurialves, inclusive na capa quando combinarem com o tema (disciplina, foco, viagem, fé, treino). No texto, a palavra continua censurada com # (a#ma), e a foto nunca acompanha copy agressiva ou de ameaça.

Fotos @liurialves: misture as fotos do Liuri (pastas `fotos/*`) com fotos do banco `fotos/pexels`
(id `1BDJzj3zYgQCR7v7fOZ4K2GyDinD8oRRe`), onde o dono guarda imagens baixadas do Pexels (licença livre).
Capa de preferência com foto do Liuri; fatias podem usar Pexels (homem sozinho, cidade à noite, treino,
estrada, sombra). A rede desta rotina não acessa Pexels/Pinterest diretamente, por isso só use imagens
dessa pasta ou do script abaixo. Nunca use imagens do Pinterest (direitos de terceiros).
Busca automática no Pexels (quando o ambiente tiver acesso, ver "Pexels" em IDs fixos): rode
`python3 scripts/buscar_pexels.py /tmp/pexels "termo 1" "termo 2" ... --n 4` com termos em inglês ligados ao
texto do slide (ex.: "man silhouette dark", "boxing gym", "city night rain", "lonely road", "wolf black and
white", "man suit shadow", "early morning run", "military parade"). Olhe a prancha antes de escolher.
Registre no histórico como `pexels:<id>`. Se o script falhar (rede ou chave), siga só com Drive + fundos e
diga no relatório. Para unificar a estética escura,
pode converter as fotos para preto e branco com contraste alto (PIL) antes do render.

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

Fotos do spa (regra do dono em 20/10/2026): o banco do spa é a pasta `fotos/spatherapieslisbon` + vídeos + fundos
da paleta, e AGORA também podem entrar as fotos do Liuri (pastas `fotos/*`, `fotos/liurialves` e frames dos vídeos
dele), sobretudo para variar o banco do spa, que é pequeno. Escolha as que combinam com o tema do slide (Lisboa,
corpo, treino, trabalho, o Liuri a atender). Fotos religiosas (igrejas, altares) podem entrar no spa quando combinarem com o tema (ex.: Lisboa, passeio, descanso). Continuam proibidas no spa: fotos do Pexels, fotos com arma (inclusive as do estande de tiro) e fotos com
marca d'água. Fotos da família só se fizerem sentido no tema (ex.: massagem a casal), nunca na capa.
Na capa do spa, prefira foto do spa ou do Liuri em contexto de massagem/Lisboa.

Pilares (3 por dia):
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
