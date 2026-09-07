#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del video promocional de CH Hats.
Estilo copiado del video de guia: subtitulos serif palabra-por-palabra,
flashes a color solido, campos azules desenfocados, b-roll con grading.
Salida: 1080x1920, 30fps, SIN audio (el cliente le pone la voz despues).
"""
import os, subprocess, shutil

# ---------------------------------------------------------------- rutas
SRC     = "/projects/sandbox/David-Chavez/IMG_6373.MOV"
HERO    = "/projects/sandbox/assets/hero_gorra.png"   # gorra con fondo transparente
LOGO_CH = "/projects/sandbox/assets/logo_ch.png"      # icono "CH"
WORK    = "/projects/sandbox/work"
OUT     = "/projects/sandbox/out/CH-Hats-mayoristas.mp4"

W, H, FPS = 1080, 1920, 30

AZUL   = "0x02308d"   # azul sacado del video de guia
NEGRO  = "0x000000"
BLANCO = "0xffffff"

C_BLANCO = "&H00FFFFFF"
C_ORO    = "&H003EC6F7"   # #F7C63E

Y_TXT = 1150              # todas las palabras a la misma altura (sin saltos)

# ---------------------------------------------------------------- guion
# visual: black | flash:blue | flash:white | solid:black
#         clip:<seg>:<in|out>   b-roll con grading + zoom
#         tint:<seg>            b-roll desenfocado y teñido de azul
#         hero                  foto limpia de la gorra sobre negro
#         outro                 logo CH + datos
BEATS = [
    ("black",          0.40, None),

    # gancho
    ("clip:0.8:in",    2.90, [("¿Querés","W"),("emprender","G"),("en","W"),("Honduras","G")]),
    ("flash:blue",     0.12, None),
    ("tint:5.0",       2.40, [("pero","W"),("no","W"),("sabés","W"),("con","W"),("qué","G")]),

    # problema
    ("clip:5.2:out",   2.90, [("todos","W"),("buscan","W"),("una","W"),("idea","W"),("nueva","W")]),
    ("flash:white",    0.10, None),
    ("clip:9.6:in",    3.10, [("y","W"),("la","W"),("que","W"),("ya","W"),("vende","G"),
                              ("la","W"),("tenés","W"),("enfrente","G")]),

    # revelacion
    ("flash:blue",     0.12, None),
    ("clip:12.0:in",   1.90, [("gorras","W"),("en","W"),("tendencia","G")]),
    ("clip:14.2:in",   1.80, [("a","W"),("nivel","W"),("nacional","G")]),
    ("clip:23.8:out",  1.50, None),                       # respira: producto puro
    ("hero",           2.30, None),   # foto limpia del producto + marca completa

    # oferta
    ("flash:white",    0.10, None),
    ("clip:20.6:in",   2.50, [("al","W"),("público","W"),("L.950","B")]),
    ("clip:17.6:out",  2.70, [("vos","W"),("la","W"),("llevás","W"),("mucho","W"),("menos","G")]),
    ("flash:blue",     0.12, None),
    ("tint:27.6",      2.20, [("desde","W"),("3","B"),("unidades","G")]),
    ("clip:31.2:in",   2.30, [("precio","W"),("de","W"),("mayorista","G")]),

    # margen
    ("clip:23.8:in",   2.80, [("la","W"),("diferencia","W"),("es","W"),("tu","W"),("ganancia","G")]),
    ("clip:27.8:out",  2.50, [("vendés","W"),("en","W"),("tu","W"),("zona","G")]),

    # escala
    ("flash:white",    0.10, None),
    ("clip:9.6:out",   2.40, [("mientras","W"),("más","W"),("comprás","G")]),
    ("clip:16.2:out",  2.20, [("mejor","G"),("precio","G"),("te","W"),("damos","W")]),

    # llamado a la accion
    ("clip:5.2:in",    2.10, [("escribinos","W"),("al","W"),("WhatsApp","G")]),
    ("solid:black",    2.70, [("9804-9467","B")]),
    ("clip:0.8:out",   1.70, [("y","W"),("arrancás","W"),("hoy","G")]),
    ("outro",          3.20, None),
]

# ---------------------------------------------------------------- grading
# Version corregida: mucho mas claro que el primer intento para que
# SI se vean las gorras. Baja el rosado de la colcha sin matar el producto.
GRADE = (
    "eq=contrast=1.12:brightness=0.040:saturation=0.74,"
    "curves=all='0/0 0.18/0.17 0.55/0.60 1/1',"
    # NO usar selectivecolor aca: quitarle magenta a los neutros vuelve
    # verde oliva las gorras negras. El encuadre cerrado ya deja la colcha
    # casi fuera de cuadro, que era el problema real.
    "colorbalance=rs=-0.06:gs=-0.01:bs=0.06,"
    "vignette=PI/4.4,"
    "unsharp=5:5:0.90:5:5:0.0"
)

COMMON = f"-r {FPS} -c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p -an -y"


def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print("FALLO:", cmd[:400])
        print(r.stderr[-2500:])
        raise SystemExit(1)
    return r


def render_beat(i, visual, dur):
    out = f"{WORK}/{i:03d}.mp4"
    nf = max(1, int(round(dur * FPS)))

    if visual.startswith("clip:"):
        _, start, direction = visual.split(":")
        # encuadre mas cerrado que antes: deja la colcha de la cama fuera
        z = f"1.13+0.15*on/{nf}" if direction == "in" else f"1.28-0.15*on/{nf}"
        # y ademas baja el centro del recorte, donde estan las gorras
        ypos = f"min(ih-ih/zoom,ih/2-(ih/zoom/2)+ih*0.055)"
        vf = (f"scale={W*3//2}:{H*3//2}:flags=lanczos,{GRADE},"
              f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='{ypos}'"
              f":d=1:s={W}x{H}:fps={FPS},format=yuv420p")
        cmd = (f'ffmpeg -v error -ss {start} -t {dur} -i "{SRC}" '
               f'-vf "{vf}" -t {dur} {COMMON} "{out}"')

    elif visual.startswith("tint:"):
        # campo azul desenfocado con el producto apenas insinuado detras,
        # igual que los frames azules borrosos del video de guia
        start = visual.split(":")[1]
        # mas claro y menos opaco que antes, para que se vea el bokeh
        # del producto detras del azul (como los frames borrosos de la guia)
        fc = (f"[0:v]scale={W}:{H}:flags=lanczos,gblur=sigma=30,"
              f"eq=contrast=1.10:brightness=0.10:saturation=0.30,"
              f"zoompan=z='1.06+0.08*on/{nf}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d=1:s={W}x{H}:fps={FPS}[bg];"
              f"[1:v]format=rgba[bl];[bg][bl]overlay=0:0:format=auto,format=yuv420p")
        cmd = (f'ffmpeg -v error -ss {start} -t {dur} -i "{SRC}" '
               f'-f lavfi -i "color=c={AZUL}@0.55:s={W}x{H}:r={FPS}:d={dur}" '
               f'-filter_complex "{fc}" -t {dur} {COMMON} "{out}"')

    elif visual == "hero":
        # gorra recortada sobre negro, con leve empuje de camara
        fc = (f"[1:v]scale=1000:-1:flags=lanczos[cap];"
              f"[0:v][cap]overlay=(W-w)/2:530:format=auto,"
              f"zoompan=z='1.0+0.07*on/{nf}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d=1:s={W}x{H}:fps={FPS},format=yuv420p")
        cmd = (f'ffmpeg -v error -f lavfi -i "color=c={NEGRO}:s={W}x{H}:r={FPS}:d={dur}" '
               f'-i "{HERO}" -filter_complex "{fc}" -t {dur} {COMMON} "{out}"')

    elif visual == "outro":
        fc = (f"[1:v]scale=260:-1:flags=lanczos[lg];"
              f"[0:v][lg]overlay=(W-w)/2:700:format=auto,format=yuv420p")
        cmd = (f'ffmpeg -v error -f lavfi -i "color=c={NEGRO}:s={W}x{H}:r={FPS}:d={dur}" '
               f'-i "{LOGO_CH}" -filter_complex "{fc}" -t {dur} {COMMON} "{out}"')

    else:
        color = {"black": NEGRO, "flash:blue": AZUL,
                 "flash:white": BLANCO, "solid:black": NEGRO}[visual]
        cmd = (f'ffmpeg -v error -f lavfi -i "color=c={color}:s={W}x{H}:r={FPS}:d={dur}" '
               f'-vf format=yuv420p -t {dur} {COMMON} "{out}"')

    run(cmd)
    return out


def ts(t):
    cs = int(round(t * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def build_ass(events):
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: W,Playfair Lining,142,{C_BLANCO},{C_BLANCO},&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3,3,5,50,50,50,1
Style: G,Playfair Lining,142,{C_ORO},{C_ORO},&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3,3,5,50,50,50,1
Style: B,Playfair Lining,190,{C_ORO},{C_ORO},&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,5,5,5,50,50,50,1
Style: S,Playfair Lining,68,{C_BLANCO},{C_BLANCO},&H00000000,&H64000000,-1,0,0,0,100,100,3,0,1,3,3,5,50,50,50,1
Style: SG,Playfair Lining,76,{C_ORO},{C_ORO},&H00000000,&H64000000,-1,0,0,0,100,100,3,0,1,3,3,5,50,50,50,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
    lines = [head]
    for (t0, t1, style, text, y) in events:
        # \blur suaviza el contorno negro y lo vuelve un halo: garantiza
        # que la palabra se lea sobre las gorras sin verse como borde duro
        # blur bajo: el halo negro da legibilidad pero la serif queda nitida
        pop = "{\\blur2\\fscx86\\fscy86\\t(0,90,\\fscx100\\fscy100)\\fad(50,50)}"
        lines.append(f"Dialogue: 0,{ts(t0)},{ts(t1)},{style},,0,0,0,,"
                     f"{{\\an5\\pos({W//2},{y})}}{pop}{text}")
    return "\n".join(lines) + "\n"


def main():
    shutil.rmtree(WORK, ignore_errors=True)
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    clips, events = [], []
    t = 0.0

    for i, (visual, dur, words) in enumerate(BEATS):
        clips.append(render_beat(i, visual, dur))

        if words:
            peso = [1.35 if st in ("G", "B") else 1.0 for _, st in words]
            tot = sum(peso)
            ct = t
            for (word, st), p in zip(words, peso):
                d = dur * p / tot
                # el hero muestra la gorra: el texto sube para no taparla
                y = 1420 if visual == "hero" else Y_TXT
                events.append((ct + 0.05, ct + d - 0.03, st, word, y))
                ct += d

        if visual == "hero":
            # la marca se muestra COMPLETA y sostenida, no palabra por palabra
            events.append((t + 0.30, t + dur - 0.10, "B", "CH HATS", 1420))

        if visual == "outro":
            events.append((t + 0.45, t + dur - 0.15, "SG", "gorrasch.shop", 1180))
            events.append((t + 0.80, t + dur - 0.15, "S",  "WhatsApp  9804-9467", 1300))

        t += dur

    with open(f"{WORK}/lista.txt", "w") as f:
        for c in clips:
            f.write(f"file '{c}'\n")
    run(f'ffmpeg -v error -f concat -safe 0 -i "{WORK}/lista.txt" -c copy -an -y "{WORK}/base.mp4"')

    with open(f"{WORK}/subs.ass", "w", encoding="utf-8") as f:
        f.write(build_ass(events))

    run(f'ffmpeg -v error -i "{WORK}/base.mp4" '
        f'-vf "ass={WORK}/subs.ass:fontsdir=/usr/share/fonts/playfair" '
        f'-c:v libx264 -preset slow -crf 21 -pix_fmt yuv420p '
        f'-movflags +faststart -r {FPS} -an -y "{OUT}"')

    print(f"LISTO -> {OUT}")
    print(f"duracion: {t:.2f}s   beats: {len(BEATS)}   eventos de texto: {len(events)}")


if __name__ == "__main__":
    main()
