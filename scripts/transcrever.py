"""
Transcreve a fala de um vídeo (PT) com Whisper small via sherpa-onnx, offline.

Uso:  python3 scripts/transcrever.py video.mp4 [saida.json]
Saída: JSON {"segmentos": [{"ini": s, "fim": s, "texto": "...", "palavras": [{"p": "...", "ini": s, "fim": s}]}]}
As palavras têm tempo aproximado (distribuído pelo tamanho da palavra dentro do trecho de fala).

Na primeira vez baixa o modelo (~640 MB) e o VAD dos releases do GitHub do sherpa-onnx
(o huggingface.co está bloqueado na rede da rotina) para ~/.cache/carrosseis-asr.
Requer: pip install sherpa-onnx --break-system-packages
"""
import json, os, subprocess, sys, tarfile, urllib.request
import numpy as np
import sherpa_onnx

CACHE = os.path.expanduser("~/.cache/carrosseis-asr")
REL = "https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/"
SR = 16000


def garantir_modelo():
    os.makedirs(CACHE, exist_ok=True)
    mdir = os.path.join(CACHE, "sherpa-onnx-whisper-small")
    for alt in ("/tmp/asr/sherpa-onnx-whisper-small",):
        if not os.path.isdir(mdir) and os.path.isdir(alt):
            mdir = alt
    if not os.path.isdir(mdir):
        tb = os.path.join(CACHE, "w.tar.bz2")
        urllib.request.urlretrieve(REL + "sherpa-onnx-whisper-small.tar.bz2", tb)
        with tarfile.open(tb) as t:
            t.extractall(CACHE)
        os.remove(tb)
    vad = os.path.join(CACHE, "silero_vad.onnx")
    if not os.path.exists(vad):
        if os.path.exists("/tmp/asr/silero_vad.onnx"):
            vad = "/tmp/asr/silero_vad.onnx"
        else:
            urllib.request.urlretrieve(REL + "silero_vad.onnx", vad)
    return mdir, vad


def audio(video):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", video, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def main(video, out=None):
    mdir, vadp = garantir_modelo()
    rec = sherpa_onnx.OfflineRecognizer.from_whisper(
        encoder=f"{mdir}/small-encoder.int8.onnx", decoder=f"{mdir}/small-decoder.int8.onnx",
        tokens=f"{mdir}/small-tokens.txt", language="pt", task="transcribe", num_threads=4)
    cfg = sherpa_onnx.VadModelConfig()
    cfg.silero_vad.model = vadp
    cfg.silero_vad.min_silence_duration = 0.25
    cfg.silero_vad.min_speech_duration = 0.2
    cfg.silero_vad.max_speech_duration = 8
    cfg.sample_rate = SR
    vad = sherpa_onnx.VoiceActivityDetector(cfg, buffer_size_in_seconds=120)
    x = audio(video)
    win = cfg.silero_vad.window_size
    segs = []
    i = 0
    while i < len(x):
        vad.accept_waveform(x[i:i + win]); i += win
        while not vad.empty():
            segs.append((vad.front.start / SR, np.array(vad.front.samples))); vad.pop()
    vad.flush()
    while not vad.empty():
        segs.append((vad.front.start / SR, np.array(vad.front.samples))); vad.pop()
    res = []
    for ini, s in segs:
        st = rec.create_stream(); st.accept_waveform(SR, s); rec.decode_stream(st)
        txt = st.result.text.strip()
        if not txt:
            continue
        fim = ini + len(s) / SR
        ws = txt.split(); tot = sum(len(w) + 1 for w in ws); t = ini; pal = []
        for w in ws:
            d = (fim - ini) * (len(w) + 1) / tot
            pal.append({"p": w, "ini": round(t, 2), "fim": round(t + d, 2)}); t += d
        res.append({"ini": round(ini, 2), "fim": round(fim, 2), "texto": txt, "palavras": pal})
    data = {"video": os.path.basename(video), "segmentos": res}
    if out:
        json.dump(data, open(out, "w"), ensure_ascii=False, indent=1)
    for s in res:
        print(f'{s["ini"]:6.2f}-{s["fim"]:6.2f} {s["texto"]}')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
