"""Gera trilhas originais (sem direitos de terceiros) para os Reels: escuras, lentas, cinematográficas.
Uso: python3 scripts/gerar_trilha.py  -> assets/musicas/trilha-0N.mp3 (35 s cada)"""
import numpy as np, subprocess, os, wave
SR = 44100; DUR = 35
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "musicas")
def note(f): return 440 * 2 ** ((f - 69) / 12)
def env(n, a, r):
    e = np.ones(n); a = int(a * SR); r = int(r * SR)
    e[:a] = np.linspace(0, 1, a); e[-r:] *= np.linspace(1, 0, r); return e
def pad(freqs, dur):
    t = np.arange(int(dur * SR)) / SR; s = 0
    for f in freqs:
        for det in (-0.15, 0, 0.15):
            s = s + np.sin(2 * np.pi * (f + det) * t) + 0.3 * np.sin(2 * np.pi * 2 * (f + det) * t)
    return s / (len(freqs) * 3) * env(len(t), dur * 0.3, dur * 0.3)
def piano(f, dur=2.5):
    t = np.arange(int(dur * SR)) / SR
    s = sum(np.sin(2 * np.pi * f * k * t) / k ** 1.6 for k in range(1, 6))
    return s * np.exp(-t * 2.2) * env(len(t), 0.005, 0.2)
def kick():
    t = np.arange(int(0.5 * SR)) / SR
    return np.sin(2 * np.pi * (50 + 90 * np.exp(-t * 30)) * t) * np.exp(-t * 7)
def hat():
    t = np.arange(int(0.08 * SR)) / SR
    return np.random.default_rng(1).normal(0, 1, len(t)) * np.exp(-t * 60) * 0.15
def faixa(nome, bpm, prog, mel, seed):
    rng = np.random.default_rng(seed); n = DUR * SR; mix = np.zeros(n + SR * 12)
    beat = 60 / bpm; bar = beat * 4; i = 0; t0 = 0
    while t0 < DUR:
        ch = prog[i % len(prog)]
        p = pad([note(m) for m in ch], bar * 1.05); s = int(t0 * SR); mix[s:s + len(p)] += 0.35 * p
        b = pad([note(ch[0] - 12)], bar); mix[s:s + len(b)] += 0.25 * b
        for k in range(8):
            if t0 > bar * 2 and rng.random() < 0.7:
                m = mel[(i * 8 + k) % len(mel)]; pn = piano(note(m)); ss = int((t0 + k * beat / 2) * SR)
                mix[ss:ss + len(pn)] += 0.22 * pn
        if t0 >= bar * 4:
            for k in range(4):
                ss = int((t0 + k * beat) * SR)
                if k in (0, 2): kk = kick(); mix[ss:ss + len(kk)] += 0.7 * kk
                hh = hat(); hs = int((t0 + k * beat + beat / 2) * SR); mix[hs:hs + len(hh)] += hh
        t0 += bar; i += 1
    mix = mix[:n]; mix *= env(n, 1.0, 2.5); mix /= np.abs(mix).max() * 1.12
    wav = os.path.join(OUT, nome + ".wav")
    with wave.open(wav, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-af", "aecho=0.8:0.6:120|260:0.35|0.2,loudnorm=I=-15:TP=-1.5",
                    "-ac", "2", "-b:a", "192k", os.path.join(OUT, nome + ".mp3")], check=True)
    os.remove(wav)
os.makedirs(OUT, exist_ok=True)
# A menor: Am F C G / D menor: Dm Bb F C / E menor lenta
faixa("trilha-01-am", 75, [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]], [69, 72, 76, 72, 69, 67, 64, 67], 1)
faixa("trilha-02-dm", 70, [[50, 53, 57], [46, 50, 53], [53, 57, 60], [48, 52, 55]], [74, 72, 69, 65, 69, 72, 74, 77], 2)
faixa("trilha-03-em", 80, [[52, 55, 59], [48, 52, 55], [55, 59, 62], [50, 54, 57]], [71, 67, 64, 67, 71, 74, 71, 67], 3)
print(sorted(os.listdir(OUT)))
