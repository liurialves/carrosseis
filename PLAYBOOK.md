# Playbook — carrosséis diários (@liurialves e @spatherapieslisbon)

Rotina executada todo dia por uma tarefa agendada. Cada execução começa do zero,
então TUDO o que ela precisa está aqui. Siga na ordem.

## FASE ATUAL (desde 31/10/2026): PLANO 100 MIL, SÓ @liurialves — PREVALECE SOBRE TODO O RESTO
Pedido do dono em 31/10/2026: "dedicação total ao @liurialves". Base: o PDF "Do Zero aos 100 Mil Seguidores"
(plano de 8 semanas; o dono pediu para começar na **semana 2 em 31/10/2026**). Resumo do plano em `estado/plano-100k.md`.
**Suspenso até nova ordem do dono:** posts do @spatherapieslisbon, TikTok (Buffer e pacote do spa, passos 9b e 9c),
criação/render de Reels (passos 9a e 9d). Não agendar nada nesses canais. As seções sobre eles ficam só como arquivo.

**Entregas de TODOS os dias (rotina diária):**
1. **Pesquisa de 5 perfis de sucesso do nicho** (lista fixa e rotativa em `estado/perfis-referencia.md`) + o que está a
   funcionar agora: WebSearch/WebFetch (o Instagram bloqueia leitura direta; usar CreatorDB, matérias, YouTube, podcasts).
   Escolher os 3 melhores conteúdos/moldes e dizer como adaptar ao Liuri (copiar só o molde, nunca texto/arte).
2. **3 carrosséis publicados por dia** (quantidade do PDF: 21 posts por semana), agendados no Buffer às
   **14:20, 17:40 e 20:30** (Lisboa). Um por ângulo (ver `estado/plano-100k.md`): dinheiro e gestão · cliente e conteúdo ·
   vida de quem empreende. Formatos: tweet, quadro, branco, fotofrase, capa+escuro (render_formatos.py), variando.
   O 2º slide funciona como segunda capa (o Instagram reexibe o carrossel a partir do 2º slide para quem não deslizou).
3. **Teste de CTA:** cada um dos 3 posts do dia usa um tipo de CTA diferente e o tipo roda entre os horários:
   `comentario` (emoji 🔥 na legenda / "deixe o seu fogo" no slide, ou palavra/número), `envio` ("envie para o seu sócio /
   para quem precisa ouvir isto": envios por alcance é o sinal nº 1 para não seguidores, segundo Mosseri) e `salvar`
   ("salve para aplicar"). Registar `"cta_tipo"` no histórico. CALL só como linha extra na legenda (oferta forte só nas
   semanas 7 e 8 do plano).
4. **3 roteiros de Reels** (o dono grava; NÃO renderizar vídeo): gancho forte nos 3 primeiros segundos, ideia, cortes,
   texto na tela, CTA e "por que pode viralizar" (com base nos Reels de sucesso estudados no dia).
5. **Stories do dia:** sequência simples de 4 a 6 telas com bastidores (treino, família, empresa, cliente) + 1 enquete +
   1 caixa de pergunta, ligada ao tema dos carrosséis.
6. **10 perfis para interagir** (comentar com algo útil, não "top"): rodar a lista de `estado/perfis-interacao.md`,
   mistura de grandes do nicho (comentar cedo) e médios/pequenos (brasileiros empreendedores em Portugal), mais novos que a
   pesquisa encontrar (acrescentar ao ficheiro com a fonte).
7. **Tarefa do PDF do dia** (calendário em `estado/plano-100k.md`), com o material pronto para o dono executar.
8. **Remodelagem (pedido do dono em 31/10/2026): 1 dos 3 carrosséis do dia é sempre remodelado**, alternando por dia:
   - **Dia par: referência @99hud** (https://www.instagram.com/99hud). O Instagram não pode ser lido daqui, por isso a
     fonte são os prints/links que o dono põe na pasta do Drive `plano-100k/referencias-99hud`
     (id `1mLheLZjWvJwGDpzhK0Qu7Q6udLt2TUZp`). Usar o post mais recente ainda não usado (marcar no histórico
     `"remodelado_de": "99hud:<nome do ficheiro ou link>"`). Copiar só o molde: tema, estrutura do gancho, ordem dos
     slides e tipo de CTA. Texto, exemplos, fotos e desenho são 100% do Liuri, no nicho dele (dono de pequena empresa,
     Brasil/Portugal) e no design dele. Nunca copiar frase, arte, foto ou marca (o Instagram corta recomendação de
     conteúdo não original em fotos e carrosséis desde mai/2026). Se a pasta estiver vazia, usar a regra do dia ímpar.
   - **Dia ímpar: replicar um vencedor do próprio @liurialves** (regra do PDF: repetir o que funcionou). Buffer
     `list_posts` status sent com includeMetrics nos últimos 30 dias; escolher o post com maior alcance (desempate:
     guardados + envios por 100 de alcance) que não foi replicado nos últimos 14 dias. Refazer com alterações: gancho
     novo com o mesmo ângulo, exemplo atualizado, outro formato ou outro tipo de CTA, nunca as mesmas imagens.
     Registar `"remodelado_de": "liurialves:<buffer_post_id>"`.
Tudo isto vai num Google Doc por dia "Plano 100k - AAAA-MM-DD" na pasta do Drive `plano-100k`
(id `1g92VDiDlPbCW8_GSkd4jPLkq0f7SvzEN`), com as capas, horários e links. Depois, notificação push com o resumo e o link do doc.

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
9a. **Reels (@liurialves), SEMPRE 2 por dia NO TOTAL (1 de nicho + 1 de alcance; contando os falados do 9d; regra de 28/10/2026, ver "Plano 10K em 90 dias"): NÃO publicar.** O dono edita o áudio à mão e publica ele mesmo.
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
- **29/10/2026:** o dono pediu em 28/10 à noite mais posts no formato quadro. Já está agendado no Buffer um quadro extra do
  @liurialves para **29/10 às 20:30** (`posts/2026-10-29/liurialves-extra`, tema "as 5 portas da cliente: pesquisa, perfil,
  WhatsApp, preço, marcação", palavra DIAGNÓSTICO; id no histórico). Ele conta no limite de 10 do Buffer. No quadro das
  14:20 desse dia use OUTRO tema e outro desenho de capa (não o funil das 5 portas). Não apague a pasta liurialves-extra.
- **26/10/2026:** os 5 carrosséis do @liurialves desse dia (funil completo com os formatos novos) foram feitos no chat em
  25/10 e estão em `posts/2026-10-26/liurialves-1` a `-5`, com legendas em `estado/agendar-2026-10-26.json`. Os 5 JÁ
  FORAM AGENDADOS no Buffer na noite de 25/10 (ids em `historico.json`), às 10:30, 12:10, 14:20, 17:40 e 20:30
  (hora de Lisboa, +00:00). Nesse dia: confira no Buffer se estão lá; se faltar algum, agende-o a partir desse JSON
  (mesmos horários). NÃO faça carrosséis novos do @liurialves. Faça os 3 do spa (08:25, 12:45, 15:20) e o TikTok do
  @liurialves só com 2 deles: liurialves-1 às 13:05 e liurialves-5 às 19:35 (mesmas imagens; título e legenda no
  JSON). Total no Buffer: 5 + 3 + 2 = 10. Reel do dia: no máximo 1.
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
ela tem prioridade sobre escolhas de tema, gancho e formato (nunca sobre IDs, limites, horários fixos,
regras de segurança nem sobre a fase FUNIL DE VENDAS do @liurialves). Histórico completo em `estado/analises/`.
**Semana de 26/10/2026** (Buffer, 19–25/10 vs 28/09–18/10; completo em `estado/analises/2026-10-26.md`)
- **Funcionou:** Reels do Liuri com legenda e CTA. "A maioria dos homens não diz que está no limite" teve 1.441 de
  alcance e 109 curtidas. "Prometi à minha esposa... 10 mil por mês" teve 1.430 de alcance e **21 comentários** com o CTA
  "deixa um 🙏 se você também está construindo algo pela sua família". "Segue @liurialves" (25/10) teve 1.320 de
  alcance e 18 partilhas. Reel com legenda: 406 de alcance médio; sem legenda: 112. No total, o @liurialves teve
  13.130 de alcance na semana (antes ~4.800/sem.), 33 partilhas (antes ~5) e 42 guardados (antes ~13).
  Melhor carrossel: "Na Aeronáutica eu tinha horário para tudo..." (130 de alcance, 9 curtidas, 2 comentários).
  Pela 2ª semana, a capa de história em 1ª pessoa lidera, com 137 de alcance médio, contra 74–97 de lista e
  cliente/site. No TikTok, "Brasileiro em Portugal: 5 coisas que eu faria diferente" teve 417 views (média de 180).
- **Cortar:** posts manuais sem legenda: foram 44 no @liurialves (~112 de alcance) e 12 no spa em 24/10 (~28 cada).
  Também dias com 10 a 12 posts manuais. Nos carrosséis, cortar a capa de funil seca, sem cena:
  "5 testes no celular" teve 27 de alcance, "WhatsApp não toca" teve 34. "Ringue e negócio" em carrossel (89) fica
  só para Reel.
  O spa caiu de 156 para 78 de alcance por carrossel. A queda começou com o lote de posts sem legenda e o dia sem
  posts (23/10).
- **Ajustes desta semana (@liurialves, dentro do funil):**
  1. Capa de topo do funil (polêmica e inovador) abre com uma cena vivida pelo Liuri, a tese vem logo depois.
     Exemplo: "Ontem abri o site de uma clínica em Lisboa e em 5 segundos eu já sabia por que o WhatsApp não
     toca". Nada de lista seca na capa.
  2. CTA de topo e dos Reels: identidade com emoji ("deixa um 🙏/🔥 se você também..."). Educativo: salvar.
     Fundo: WhatsApp + palavra, sem mudança.
  3. Fotos: capa com foto própria (Liuri em cena: treino, carro, cliente, família). Pexels só nas fatias.
- **8 ganchos para testar (@liurialves):**
  "Prometi à minha esposa que a empresa ia bater a meta até dezembro. Este é o 1º número que eu passei a olhar todo dia" ·
  "Abri o Instagram de uma clínica de estética em Lisboa e em 5 segundos eu sabia por que a agenda está vazia" ·
  "Na Aeronáutica eu aprendi a fazer relatório. Hoje é o mesmo relatório que eu peço a todo cliente antes de ligar anúncio" ·
  "Eu dirigia Uber em Lisboa quando percebi que o cliente decide no 1º minuto, no carro e no seu perfil" ·
  "O sobrinho fez o site de graça. Eu abri no celular e mostro onde o cliente desiste e vai para o concorrente" ·
  "10 anos com as mãos nas costas de cliente: quem volta não é quem achou mais barato" ·
  "Meu filho perguntou por que eu trabalho até tarde. A resposta mudou como eu vendo" ·
  "Brasileiro em Portugal: 5 coisas que eu faria diferente se abrisse a empresa hoje"
- **Spa:** acabar com os lotes de fotos sem legenda (cada post leva legenda com "massagem + zona de Lisboa" na 1ª
  linha). Peso maior para "para terapeutas" (148–170 de alcance) e "corpo no dia a dia" com zona. 3 ganchos:
  "Terapeuta em Lisboa: o cliente de Benfica procura 'massagem perto de mim' e o teu perfil não diz onde atendes" ·
  "Massagem em Lisboa depois do treino: em que dia marcar para não chegares ao jogo dorido" ·
  "Envia isto a quem passa o dia no portátil em Alcântara e diz que a dor no pescoço é normal".
- **Reels (dono):** no máximo 2 por dia, sempre com legenda de 3 ou mais linhas e CTA. Repetir o formato "promessa à
  família + série até a meta" (a série dá motivo para seguir). Gravar 1 Reel por semana em cena de cliente/site
  (fundo do funil). Testar 1 gancho novo como trial reel.
- **TikTok:** título em lista ou história + "Brasileiro em Portugal"/"Empreender em Lisboa". Priorizar o carrossel de
  lista no slot das 19:35.
- **Recomendação de horário (o dono decide; o passo 9 não mudou):** 2ª semana em que as 12h são o pior horário (74 de
  média, contra 123–129 às 20–21h). Trocar o slot das 12:10 por ~20:30.
- **Teste A/B da semana:** o teste anterior não foi aplicado. Este substitui. No carrossel das 17:40 do @liurialves,
  dia par usa a capa A (cena em 1ª pessoa) e dia ímpar a capa B (tese/tweet sem cena), com o mesmo tema de funil e o
  mesmo CTA. Registrar `"ab": "A"` ou `"B"` no `historico.json`. Métrica: alcance e (comentários + partilhas +
  guardados) por 100 de alcance em 48 h. Vence quem tiver ≥30% a mais.

## Reposicionamento do @liurialves (pedido do dono em 28/10/2026, PREVALECE sobre tudo o que vem abaixo no @liurialves)
Documento completo: Claude Doc "Reposicionamento @liurialves + 10 roteiros" (https://claude.ai/artifact/RX9Fc5ZiH13FyTJeEQ14vw).
- **Deixa de ser "marketing para estética".** Público: donos de pequena e média empresa, autônomos e quem quer faturar
  com a internet usando as redes sociais, no Brasil e em Portugal. Estética, massagem e beleza viram só um exemplo
  entre vários (restaurante, loja, prestador de serviço, infoprodutor, profissional liberal).
- **O que vende:** mentoria e consultoria de crescimento: estratégia, funil, conteúdo e gestão/dinheiro da empresa
  (preço, margem, caixa, metas). Site e tráfego pago ficam como serviço complementar.
- **Próximo passo único:** call de diagnóstico gratuita de 30 min. Palavra única em todo CTA de venda: **CALL**
  ("Comente CALL" ou "Mande CALL no direct"; o ManyChat responde com o link de marcação). Substitui SITE, TRÁFEGO, KIT,
  TREINAMENTO e DIAGNÓSTICO, que não devem mais aparecer nos posts novos.
- **Prova real (correção do dono em 28/10/2026):** o Liuri JÁ atendeu empresas que estão no site dele, entre elas a
  **Carolwell** e a **empresa de limpeza LB**. Podem ser citadas pelo nome como casos ("o site que eu fiz para a
  Carolwell", "a estratégia da LB"), dizendo só o que foi feito. Número de resultado (clientes, faturamento, %),
  depoimento ou quantidade de empresas atendidas só quando o dono informar; nunca inventar. Somam-se à prova: a
  própria empresa (Lisboa Massagem), a trajetória (Aeronáutica, 10 anos de serviço, imigração) e o processo em público.
  Pelo menos 1 post por semana mostra um caso real (bastidor do que foi feito para um cliente).
- **4 frentes de conteúdo** (substituem os pilares antigos e alimentam as 5 etapas do funil): 1) estratégia e funil;
  2) conteúdo que vende; 3) gestão e dinheiro da empresa; 4) vida de quem empreende (Aeronáutica, família, MMA,
  imigração; é o conteúdo de alcance). Pelo menos 1 post por semana da frente 3.
- **Perfil (feito à mão pelo dono):** @ continua @liurialves; Nome "Liuri Alves | Mentor de negócios e marketing";
  bio "Ajudo empresários a crescer com estratégia, funil e conteúdo / Mande CALL no direct / Diagnóstico gratuito de
  30 min 👇"; link = página de marcação da call + WhatsApp.
- **Referências de Reels:** `estado/banco-de-ideias.md` (seção "Mentores", 10 Reels de Joel Jota, Caio Carneiro,
  Tallis Gomes, Alfredo Soares e Thiago Concer) e os 10 roteiros do doc. Copiar só o molde, nunca o texto.
- Hashtags passam a ser de negócio: #empreendedorismo #empresario #marketingdigital #gestao #vendas #funildevendas
  #negocioproprio #brasileirosemportugal (máx. 5 por post).

## Plano 10K em 90 dias (@liurialves, desde 29/10/2026 até 26/01/2027)
Pedido do dono em 28/10/2026: aplicar ao Instagram o PDF "10K Followers in 90 Days Game Plan" (@therealbrianmark).
Esta seção vale junto com a fase FUNIL DE VENDAS e PREVALECE sobre o "Prioridade" do passo 9a. Não muda IDs,
horários do passo 9, limite do Buffer, regras de copy nem o tom de 17/10.

**1. Perfil (feito à mão pelo dono, uma vez):** nome pesquisável "Liuri Alves | Marketing para estética"; bio em 3
linhas (quem eu ajudo + resultado sem promessa de número / palavra para mandar no direct / diagnóstico grátis + link);
Meta Verified é opcional. Texto sugerido em `estado/plano-10k.md`.

**2. Banco de ideias:** `estado/banco-de-ideias.md`. A análise semanal (segunda) acrescenta pelo menos 7 ideias
"outlier": posts próprios com 3x ou mais do alcance médio do formato e, quando houver acesso, vídeos de criadores do
nicho com 10x ou mais da média deles (Sandcastles.ai é feito à mão pelo dono). Para cada ideia: gancho, formato,
por que funcionou e "minha versão". A rotina diária tira daqui pelo menos 1 das ideias do dia e marca como usada.

**3. Roubar o molde, nunca o texto:** de cada outlier copia-se só a estrutura (gancho, formato de história, layout
visual). Palavras, exemplos e história são do Liuri e falam com o dono de estética, massagem, beleza e serviço local.

**4. 2 Reels por dia, todos os dias (passo 9a):**
- **Reel 1, nicho** (gera call): dor do dono de empresa ou empreendedor (cliente, venda, funil, conteúdo, dinheiro da
  empresa), no mesmo tema dos carrosséis do dia. CTA: "Comente CALL" / "Mande CALL no direct".
  Mede-se por mensagens no direct e no WhatsApp. Se houver vídeo falado novo (9d), ele é o Reel de nicho.
- **Reel 2, alcance** (busca viral): público amplo. Ringue e negócio (série numerada), brasileiro em Portugal,
  promessa à família + série até a meta, homem que trabalha pesado, a ideia outlier da semana. CTA de identidade com
  emoji ou "Siga @liurialves". Mede-se por visualizações, partilhas e seguidores.
- No doc do dia, cada Reel leva o rótulo NICHO ou ALCANCE e a legenda pronta (nunca vazia). No topo do doc:
  "Publique os 2 hoje: o de nicho de manhã/tarde, o de alcance à noite (20h–21h)".
- Dobrar o que funciona: se um Reel passar de 3x o alcance médio, fazer mais 2 versões na mesma semana.
- Registrar no histórico `"tipo": "reel"` com `"reel_tipo": "nicho" | "alcance"`.

**5. Mensagem automática para novos seguidores (ManyChat, configurado à mão pelo dono):** texto em
`estado/plano-10k.md`. As respostas seguem o roteiro de `estado/funil-whatsapp.md`.

**Métrica do plano:** a análise semanal registra os seguidores do @liurialves no início de cada semana em
`estado/plano-10k.md` (linha "Semana N: X seguidores") e compara com a meta linear até 10.000 em 26/01/2027.

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

**Os 5 tipos de conteúdo e os formatos (pedido do dono em 25/10/2026, referência @alfredosoares):**
O dono quer o funil montado com 5 tipos de post, com a estrutura dos formatos que o @alfredosoares usa, num visual
**premium, minimalista e profissional** (pedido do dono em 25/10/2026): papel claro quente, preto suave, um único
destaque laranja da marca, margens largas, cabeçalho discreto (ícone + LIURI ALVES + 01/09) e barra de progresso fina
embaixo. Nada de letra gritando, contorno, brilho ou várias cores. Prints do perfil dele em
`estado/referencias/alfredosoares/` e a análise dos formatos em `estado/referencias.md`. Sempre que houver print ou
link novo do Alfredo, olhe primeiro e tire dali ideia de tema e de formato. Pode partir de uma ideia dele e remodelar
para o nicho do Liuri (estética, massagem, beleza, serviço local, brasileiro empreendendo em Portugal), com texto 100%
próprio: nunca copiar frase, arte, foto, nome de produto ou marca dele.
1. **Polêmica (alcance)**: tese forte contra uma prática do mercado. Formato **tweet** (post estilo X sobre papel
   claro) ou **branco** com uma frase de impacto. CTA: comentar.
2. **Educativo (ensinar algo diferente)**: um método explicado num esquema. Formato **quadro** (etiqueta, título limpo,
   esquema desenhado à mão em traço fino laranja: número em círculo, funil, círculos, lista, "pular etapas"; texto de
   apoio e frase final com filete). CTA: salvar + WhatsApp com palavra.
3. **Intencional (levar o cliente a fazer algo)**: passo a passo curto para fazer hoje. Formato **branco** (etiqueta
   "Ajuste 1", frase grande com destaque laranja, texto de apoio). CTA: "Comente FEITO" + WhatsApp com palavra.
4. **Inovador (algo que faça diferença para quem aprende)**: ideia nova e aplicável que o mercado não mostra.
   Formato **fotofrase** (foto P&B escurecida, frase branca alinhada à esquerda com partes em negrito). 1ª e última
   foto do Liuri. CTA: comentar resultado / seguir.
5. **Venda (converter)**: oferta clara (para quem é, etapas do que recebe, para quem não é, primeiro passo).
   Capa **capa** (foto P&B do Liuri em cima, painel escuro com etiqueta "Oferta", título e subtítulo) + fatias
   **escuro** (uma etapa por slide). CTA: link da bio + WhatsApp com a palavra da oferta.
Como gerar: `python3 scripts/render_formatos.py cfg.json posts/AAAA-MM-DD/liurialves-N` (campos no cabeçalho do script;
`**negrito**` e `[[destaque]]`; cada slide pode ter `"formato"` próprio, por exemplo capa "capa" + fatias "escuro").
Exemplo completo: os 5 de `posts/2026-10-26/` (configuração em `estado/agendar-2026-10-26.json` e no histórico).
Nestes formatos o texto é curto por slide (frase + 1 a 3 frases de apoio): a regra de 40 a 80 palavras vale só para
as fatias Darkgram; o humanizer, o tom de 17/10, "sem travessão" e o controle de qualidade valem para todos.
Confira sempre a capa e 2 fatias em tamanho real antes de publicar (texto não pode cobrir o rosto).

**Distribuição diária dos 3 carrosséis do @liurialves (ordem dos horários do passo 9):**
- 12:10 → **Polêmica** (tweet ou branco, alternando dia sim, dia não).
- 14:20 → **SEMPRE no formato quadro** (pedido do dono em 28/10/2026: "quero mais posts como esse", sobre o quadro do
  funil de 26/10, que teve o melhor desempenho do funil). O tipo de conteúdo continua no rodízio, mas desenhado em quadro:
  seg, qui e dom **Educativo** (método em esquema); ter e sex **Intencional** (passo a passo em quadro: número em círculo
  por ajuste, lista com check no fim); qua e sáb **Inovador** (ideia nova em esquema: círculos, "pular etapas", funil).
  Estrutura que funcionou: capa com etiqueta "Método", título com número/promessa e um desenho que resume tudo (funil,
  círculos); fatias "Etapa N de 5" com número em círculo + nota manuscrita + texto + soco; uma fatia "O erro que eu mais
  vejo" (pular); uma "Na prática" (lista com check); a última "Próximo passo" (círculos) com WhatsApp + palavra e "Salve".
  Variar o desenho da capa de um dia para o outro e não repetir o tema de quadro dos últimos 14 dias.
  Fotofrase e branco continuam disponíveis para os outros horários quando fizer sentido.
- 17:40 → **Venda** (capa + fatias escuras, CTA WhatsApp com palavra). O teste A/B de CTA de envio
  fica suspenso enquanto o funil estiver ativo.
- Registrar no histórico `"tipo_conteudo": "polemica" | "educativo" | "intencional" | "inovador" | "venda"` e
  `"formato"`, além de `"funil"` e `"palavra_cta"`.
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
