#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video 2 de CH Hats: reclutamiento de vendedores.
Estilo tomado de @venta.silenciosa (IMG_6394.MP4): blanco y negro puro,
sans-serif, b-roll en tarjetas de esquinas redondeadas sobre fondo negro.

El AUDIO manda: los tiempos salen de voz/tiempos.json, que trae la duracion
real de cada linea y el instante exacto de cada palabra.

Uso:
    python3 build2.py preview     -> saca un PNG de cada tipo de visual
    python3 build2.py             -> render completo con audio
"""
import json, os, subprocess, shutil, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ----------------------------------------------------------------- rutas
FFMPEG = "/projects/bin/ffmpeg"
FONTS  = "/projects/fonts"
SRC_V  = "/projects/sandbox/source/IMG_6373.MOV"     # footage de las gorras
WEBIMG = "/projects/sandbox/webimg"                  # fotos de producto de la web
TIEMPOS = "/projects/sandbox/voz/tiempos.json"
VOZ_DIR = "/projects/sandbox/voz"
WORK   = "/projects/sandbox/work2"
PREV   = "/projects/sandbox/preview2"
OUT    = "/projects/sandbox/out/CH-Hats-vendedores.mp4"

W, H, FPS = 1080, 1920, 30

# ----------------------------------------------------------------- estilo
NEGRO  = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS   = (140, 140, 140)
GRIS_O = (32, 32, 32)      # gris muy oscuro para superficies sobre negro
GRIS_C = (228, 228, 228)   # gris muy claro para superficies sobre blanco

CARD_M = 96                # margen lateral de las tarjetas
CARD_R = 46                # radio de las esquinas redondeadas

F_BLACK = f"{FONTS}/Inter-Black.ttf"
F_XBOLD = f"{FONTS}/Inter-ExtraBold.ttf"
F_SEMI  = f"{FONTS}/Inter-SemiBold.ttf"
F_REG   = f"{FONTS}/Inter-Regular.ttf"

# fotos de producto con fondo blanco (las que el cliente pidio)
GORRAS_BLANCO = ["w01", "w07", "w04"]


def fuente(path, size):
    return ImageFont.truetype(path, size)


def lienzo(color=NEGRO):
    return Image.new("RGB", (W, H), color)


def centrar(d, y, texto, font, fill, maxw=None):
    """dibuja texto centrado horizontalmente; devuelve el alto usado"""
    b = d.textbbox((0, 0), texto, font=font)
    d.text(((W - (b[2] - b[0])) / 2 - b[0], y), texto, font=font, fill=fill)
    return b[3] - b[1]


def tarjeta_redondeada(img, size, radio=CARD_R):
    """recorta una imagen a un rectangulo de esquinas redondeadas"""
    img = img.convert("RGB").resize(size, Image.LANCZOS)
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size[0]-1, size[1]-1],
                                           radius=radio, fill=255)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def gris(img):
    """a blanco y negro, con un poco de contraste"""
    g = img.convert("L")
    return g.point(lambda v: max(0, min(255, int((v - 128) * 1.18 + 128)))).convert("RGB")


# ================================================================= visuales
# Cada funcion devuelve una lista de frames PIL (o 1 frame si es estatico).

def v_negro(dur, **kw):
    return [lienzo(NEGRO)]


def v_blanco(dur, **kw):
    return [lienzo(BLANCO)]


def v_gorra_card(dur, idx=0, **kw):
    """foto de producto sobre FONDO BLANCO, en tarjeta redondeada"""
    base = lienzo(NEGRO)
    nombre = GORRAS_BLANCO[idx % len(GORRAS_BLANCO)]
    p = os.path.join(WEBIMG, nombre)
    im = Image.open(p).convert("RGB")

    cw = W - CARD_M * 2
    ch = cw                      # cuadrada: llena mucho mejor el cuadro
    fondo = Image.new("RGB", (cw, ch), BLANCO)
    foto = gris(im)
    foto.thumbnail((cw - 56, ch - 56), Image.LANCZOS)
    fondo.paste(foto, ((cw - foto.width) // 2, (ch - foto.height) // 2))

    card = tarjeta_redondeada(fondo, (cw, ch))
    base.paste(card, (CARD_M, 470), card)
    return [base]


def v_footage(dur, t0=0.0, **kw):
    """el video de las gorras, en gris, dentro de una tarjeta redondeada"""
    n = max(1, int(dur * FPS))
    cw = W - CARD_M * 2
    ch = int(cw * 1.22)
    tmp = f"{WORK}/_foot_{t0}"
    os.makedirs(tmp, exist_ok=True)
    # el footage de gorras negras en gris queda casi negro: hay que levantarlo
    # bastante o no se distingue el producto dentro de la tarjeta
    subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", str(t0), "-t", str(dur + 0.2),
                    "-i", SRC_V, "-vf",
                    f"fps={FPS},scale={cw}:{ch}:force_original_aspect_ratio=increase,"
                    f"crop={cw}:{ch},format=gray,"
                    f"eq=brightness=0.14:contrast=1.22,"
                    f"curves=all='0/0.06 0.3/0.42 0.7/0.82 1/1'",
                    f"{tmp}/%04d.png"], capture_output=True)
    archivos = sorted(os.listdir(tmp))[:n]
    frames = []
    for i, f in enumerate(archivos):
        base = lienzo(NEGRO)
        im = Image.open(os.path.join(tmp, f)).convert("RGB")
        # zoom lento para que no se sienta congelado
        z = 1.0 + 0.05 * i / max(1, n)
        zw, zh = int(cw * z), int(ch * z)
        im = im.resize((zw, zh), Image.LANCZOS).crop(
            ((zw - cw) // 2, (zh - ch) // 2, (zw - cw) // 2 + cw, (zh - ch) // 2 + ch))
        card = tarjeta_redondeada(im, (cw, ch))
        base.paste(card, (CARD_M, 350), card)
        frames.append(base)
    shutil.rmtree(tmp, ignore_errors=True)
    return frames or [lienzo(NEGRO)]


def v_celular(dur, **kw):
    """mockup de celular con un post estilo TikTok mostrando una gorra"""
    n = max(1, int(dur * FPS))
    # el alto termina en 1430 para no chocar con el subtitulo, que va en 1545
    pw, ph = 720, 1180
    px, py = (W - pw) // 2, 250

    foto = gris(Image.open(os.path.join(WEBIMG, "w03")).convert("RGB"))
    frames = []
    for i in range(n):
        base = lienzo(NEGRO)
        d = ImageDraw.Draw(base)
        # cuerpo del telefono
        d.rounded_rectangle([px, py, px + pw, py + ph], radius=54,
                            fill=GRIS_O, outline=BLANCO, width=5)
        # pantalla con la gorra
        sw, sh = pw - 28, ph - 28
        pant = Image.new("RGB", (sw, sh), (12, 12, 12))
        # recorte "cover": la gorra llena la pantalla del telefono
        f2 = foto.copy()
        esc = max(sw / f2.width, sh / f2.height)
        f2 = f2.resize((int(f2.width * esc) + 1, int(f2.height * esc) + 1), Image.LANCZOS)
        ox, oy = (f2.width - sw) // 2, (f2.height - sh) // 2
        pant.paste(f2.crop((ox, oy, ox + sw, oy + sh)), (0, 0))
        base.paste(tarjeta_redondeada(pant, (sw, sh), 44), (px + 14, py + 14),
                   tarjeta_redondeada(pant, (sw, sh), 44))
        d = ImageDraw.Draw(base)
        # barra de progreso que avanza: da sensacion de video reproduciendose
        avance = int((sw - 80) * (i / max(1, n - 1)))
        d.rounded_rectangle([px + 54, py + ph - 58, px + 14 + sw - 40, py + ph - 52],
                            radius=3, fill=(70, 70, 70))
        d.rounded_rectangle([px + 54, py + ph - 58, px + 54 + avance, py + ph - 52],
                            radius=3, fill=BLANCO)
        # contador de vistas que sube
        vistas = 1200 + int(i * 47)
        fs = fuente(F_SEMI, 34)
        d.text((px + 54, py + ph - 132), f"{vistas:,} vistas".replace(",", ","),
               font=fs, fill=BLANCO)
        frames.append(base)
    return frames


def v_chat(dur, **kw):
    """mockup de chat: los mensajes van apareciendo uno por uno"""
    n = max(1, int(dur * FPS))
    msgs = [
        ("in",  "Hola! Vi tu video"),
        ("in",  "Cuánto vale la gorra?"),
        ("out", "L.950, te llega a tu casa"),
        ("in",  "La quiero!"),
    ]
    fm = fuente(F_SEMI, 54)
    frames = []
    for i in range(n):
        base = lienzo(NEGRO)
        d = ImageDraw.Draw(base)
        prog = i / max(1, n - 1)
        visibles = max(1, min(len(msgs), int(prog * len(msgs)) + 1))
        y = 520
        for k in range(visibles):
            lado, txt = msgs[k]
            b = d.textbbox((0, 0), txt, font=fm)
            tw, th = b[2] - b[0], b[3] - b[1]
            bw, bh = tw + 76, th + 66
            bx = CARD_M + 20 if lado == "in" else W - CARD_M - 20 - bw
            col = GRIS_C if lado == "in" else BLANCO
            tcol = NEGRO
            r = [bx, y, bx + bw, y + bh]
            d.rounded_rectangle(r, radius=36, fill=col)
            d.text((bx + 38 - b[0], y + 33 - b[1]), txt, font=fm, fill=tcol)
            y += bh + 32
        frames.append(base)
    return frames


def v_flecha(dur, **kw):
    """flecha que crece hacia la derecha y revela L.100 (lo que pidio el cliente)"""
    n = max(1, int(dur * FPS))
    y = 800
    x0, x1 = 130, W - 290
    fnum = fuente(F_BLACK, 230)
    frames = []
    for i in range(n):
        base = lienzo(NEGRO)
        d = ImageDraw.Draw(base)
        p = min(1.0, (i / max(1, n - 1)) * 1.35)         # llega al final antes del corte
        e = 1 - (1 - p) ** 3                              # desaceleracion
        xf = x0 + (x1 - x0) * e
        d.line([x0, y, xf, y], fill=BLANCO, width=20)
        if e > 0.04:                                       # punta
            s = 54
            d.polygon([(xf + s, y), (xf - 8, y - s), (xf - 8, y + s)], fill=BLANCO)
        if e > 0.50:                                       # el numero aparece al final
            a = min(1.0, (e - 0.50) / 0.32)
            cap = Image.new("RGB", (W, 340), NEGRO)
            dc = ImageDraw.Draw(cap)
            b = dc.textbbox((0, 0), "L.100", font=fnum)
            dc.text(((W - (b[2] - b[0])) / 2 - b[0], 40 - b[1]), "L.100",
                    font=fnum, fill=tuple(int(255 * a) for _ in range(3)))
            base.paste(cap, (0, y + 130))
        frames.append(base)
    return frames


def v_contador(dur, **kw):
    """10 gorras -> L.1,000: cuadritos que se llenan y el numero subiendo"""
    n = max(1, int(dur * FPS))
    fnum = fuente(F_BLACK, 168)
    flab = fuente(F_SEMI, 46)
    cols, filas = 5, 2
    s, gap = 118, 26
    gw = cols * s + (cols - 1) * gap
    gx, gy = (W - gw) // 2, 620
    frames = []
    for i in range(n):
        base = lienzo(NEGRO)
        d = ImageDraw.Draw(base)
        p = min(1.0, (i / max(1, n - 1)) * 1.25)
        llenos = int(round(p * 10))
        for k in range(10):
            cx = gx + (k % cols) * (s + gap)
            cy = gy + (k // cols) * (s + gap)
            if k < llenos:
                d.rounded_rectangle([cx, cy, cx + s, cy + s], radius=22, fill=BLANCO)
            else:
                d.rounded_rectangle([cx, cy, cx + s, cy + s], radius=22,
                                    outline=(90, 90, 90), width=4)
        centrar(d, gy - 96, f"{llenos} gorras", flab, GRIS)
        monto = llenos * 100
        centrar(d, gy + filas * (s + gap) + 54, f"L.{monto:,}", fnum, BLANCO)
        frames.append(base)
    return frames


def v_pasos(dur, **kw):
    """los 3 pasos apareciendo en orden"""
    n = max(1, int(dur * FPS))
    fn = fuente(F_BLACK, 78)
    ft = fuente(F_SEMI, 62)
    pasos = [("1", "Publicás"), ("2", "Te compran"), ("3", "Cobrás")]
    frames = []
    for i in range(n):
        base = lienzo(NEGRO)
        d = ImageDraw.Draw(base)
        p = i / max(1, n - 1)
        vis = max(1, min(3, int(p * 3) + 1))
        y = 700
        for k in range(vis):
            num, txt = pasos[k]
            d.text((160, y), num, font=fn, fill=GRIS)
            d.text((300, y + 10), txt, font=ft, fill=BLANCO)
            y += 190
        frames.append(base)
    return frames


def v_negro_num(dur, **kw):
    return [lienzo(NEGRO)]


def v_cierre(dur, **kw):
    """cierre: fondo blanco con el numero de WhatsApp"""
    return [lienzo(BLANCO)]


VISUALES = {
    "negro": v_negro, "blanco": v_blanco, "negro_num": v_negro_num,
    "cierre": v_cierre, "celular": v_celular, "chat": v_chat,
    "flecha": v_flecha, "contador": v_contador, "pasos": v_pasos,
}


def frames_de(visual, dur):
    if visual.startswith("gorras:"):
        return v_gorra_card(dur, idx=int(visual.split(":")[1]))
    if visual.startswith("footage:"):
        return v_footage(dur, t0=float(visual.split(":")[1]))
    return VISUALES[visual](dur)


# ================================================================= preview
def preview():
    os.makedirs(PREV, exist_ok=True)
    os.makedirs(WORK, exist_ok=True)
    casos = ["negro", "blanco", "gorras:0", "gorras:1", "gorras:2",
             "footage:2.0", "celular", "chat", "flecha", "contador", "pasos", "cierre"]
    hoja = []
    for c in casos:
        fr = frames_de(c, 2.5)
        im = fr[int(len(fr) * 0.8)] if len(fr) > 1 else fr[0]
        nombre = c.replace(":", "_")
        im.save(f"{PREV}/{nombre}.png")
        hoja.append((nombre, im))
        print("preview:", nombre, f"({len(fr)} frames)")

    # hoja de contactos para revisar todo de un golpe
    cols = 6
    tw, th = 300, 533
    filas = (len(hoja) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, filas * (th + 34)), (18, 18, 18))
    d = ImageDraw.Draw(sheet)
    f = fuente(F_SEMI, 22)
    for i, (nombre, im) in enumerate(hoja):
        t = im.resize((tw - 10, th - 10), Image.LANCZOS)
        cx, cy = (i % cols) * tw, (i // cols) * (th + 34)
        sheet.paste(t, (cx + 5, cy + 5))
        d.text((cx + 6, cy + th + 4), nombre, font=f, fill=(255, 210, 0))
    sheet.save(f"{PREV}/hoja.png")
    print("\nhoja de contactos:", f"{PREV}/hoja.png")


# ================================================================= render
def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print("FALLO:", cmd[:300]); print(r.stderr[-2000:]); raise SystemExit(1)
    return r


def clip_de_frames(frames, dur, dst):
    """codifica una lista de frames PIL a un mp4 de duracion exacta"""
    n = max(1, int(round(dur * FPS)))
    tmp = dst + "_f"
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    if len(frames) == 1:
        frames[0].save(f"{tmp}/0001.png")
        run(f'{FFMPEG} -v error -loop 1 -framerate {FPS} -i "{tmp}/0001.png" '
            f'-t {dur} -r {FPS} -c:v libx264 -preset medium -crf 18 '
            f'-pix_fmt yuv420p -an -y "{dst}"')
    else:
        for i in range(n):
            frames[min(i, len(frames)-1)].save(f"{tmp}/{i+1:04d}.png")
        run(f'{FFMPEG} -v error -framerate {FPS} -i "{tmp}/%04d.png" '
            f'-t {dur} -r {FPS} -c:v libx264 -preset medium -crf 18 '
            f'-pix_fmt yuv420p -an -y "{dst}"')
    shutil.rmtree(tmp, ignore_errors=True)


def ts(t):
    cs = int(round(t * 100))
    h, cs = divmod(cs, 360000); m, cs = divmod(cs, 6000); s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


CARTELES = {"negro", "blanco", "negro_num", "cierre"}


def construir_ass(segs):
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: FRASE,InterPromo ExtraBold,94,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,110,110,60,1
Style: FRASEN,InterPromo ExtraBold,94,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,0,0,0,0,100,100,0,0,1,0,0,5,110,110,60,1
Style: NUM,InterPromo Black,168,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,0,5,60,60,60,1
Style: NUMN,InterPromo Black,150,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,0,0,0,0,100,100,2,0,1,0,0,5,60,60,60,1
Style: SUB,InterPromo SemiBold,82,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,0,0,1,0,3,5,90,90,60,1
Style: CHICO,InterPromo SemiBold,54,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,0,0,0,0,100,100,1,0,1,0,0,5,90,90,60,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
    L = [cab]

    def ev(t0, t1, estilo, y, txt, extra="", fade=70):
        # las palabras sueltas duran ~300ms: con fade de 70+70 se pasan medio
        # tiempo translucidas y se ven grises. Para esas el fade va corto.
        pop = f"{{\\fad({fade},{fade})}}"
        L.append(f"Dialogue: 0,{ts(t0)},{ts(t1)},{estilo},,0,0,0,,"
                 f"{{\\an5\\pos({W//2},{y})}}{extra}{pop}{txt}")

    for s in segs:
        ini = s["inicio"]; fin = ini + s["voz"] + s["pausa"]
        vis = s["visual"]; sub = s["sub"]

        if vis == "negro":
            ev(ini + 0.04, fin - 0.05, "FRASE", 940, sub)

        elif vis == "blanco":
            # primera palabra en negrita, el resto normal (como el video de guia)
            partes = sub.split(" ", 1)
            if len(partes) == 2:
                txt = (partes[0] + " {\\fnInterPromo Regular}" + partes[1])
            else:
                txt = sub
            ev(ini + 0.04, fin - 0.05, "FRASEN", 940, txt)

        elif vis == "negro_num":
            ev(ini + 0.04, fin - 0.05, "NUM", 900, sub)

        elif vis == "cierre":
            ev(ini + 0.04, fin - 0.05, "FRASEN", 760, sub)
            ev(ini + 0.30, fin - 0.05, "NUMN", 1010, "9804-9467")
            ev(ini + 0.55, fin - 0.05, "CHICO", 1170, "WhatsApp")

        else:
            # sobre los visuales: palabra por palabra, sincronizado al audio real
            pals = s["palabras"]
            if pals:
                for i, p in enumerate(pals):
                    t0 = ini + p["t"]
                    t1 = ini + (pals[i+1]["t"] if i+1 < len(pals) else p["t"] + p["d"] + 0.22)
                    ev(t0, min(t1, fin), "SUB", 1545, p["w"], fade=25)
            else:
                ev(ini + 0.04, fin - 0.05, "SUB", 1545, sub, fade=25)

    return "\n".join(L) + "\n"


def construir_audio(segs, dst):
    """une las lineas de voz con los silencios exactos entre ellas"""
    partes = []
    for i, s in enumerate(segs):
        wav = f"{WORK}/a{i:03d}.wav"
        run(f'{FFMPEG} -v error -i "{VOZ_DIR}/{s["id"]}.mp3" '
            f'-ar 48000 -ac 2 -y "{wav}"')
        partes.append(wav)
        if s["pausa"] > 0.001:
            sil = f"{WORK}/s{i:03d}.wav"
            run(f'{FFMPEG} -v error -f lavfi -i anullsrc=r=48000:cl=stereo '
                f'-t {s["pausa"]} -y "{sil}"')
            partes.append(sil)
    lista = f"{WORK}/audio.txt"
    with open(lista, "w") as f:
        for p in partes:
            f.write(f"file '{p}'\n")
    run(f'{FFMPEG} -v error -f concat -safe 0 -i "{lista}" -c copy -y "{dst}"')


def render():
    datos = json.load(open(TIEMPOS))
    segs = datos["segmentos"]
    shutil.rmtree(WORK, ignore_errors=True); os.makedirs(WORK)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    print("1/5 visuales...")
    clips = []
    for i, s in enumerate(segs):
        dur = s["voz"] + s["pausa"]
        fr = frames_de(s["visual"], dur)
        dst = f"{WORK}/v{i:03d}.mp4"
        clip_de_frames(fr, dur, dst)
        clips.append(dst)
        print(f"   {s['id']} {s['visual']:13} {dur:5.2f}s")

    print("2/5 uniendo video...")
    lista = f"{WORK}/video.txt"
    with open(lista, "w") as f:
        for c in clips:
            f.write(f"file '{c}'\n")
    run(f'{FFMPEG} -v error -f concat -safe 0 -i "{lista}" -c copy -an -y "{WORK}/base.mp4"')

    print("3/5 audio...")
    construir_audio(segs, f"{WORK}/voz.wav")

    print("4/5 subtitulos...")
    with open(f"{WORK}/subs.ass", "w", encoding="utf-8") as f:
        f.write(construir_ass(segs))

    print("5/5 render final...")
    run(f'{FFMPEG} -v error -i "{WORK}/base.mp4" -i "{WORK}/voz.wav" '
        f'-vf "ass={WORK}/subs.ass:fontsdir={FONTS}" '
        f'-map 0:v -map 1:a '
        f'-c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p '
        f'-c:a aac -b:a 160k -shortest -movflags +faststart -r {FPS} -y "{OUT}"')

    d = subprocess.run(["/projects/bin/ffprobe","-v","error","-show_entries",
                        "format=duration","-of","csv=p=0",OUT],
                       capture_output=True, text=True).stdout.strip()
    print(f"\nLISTO -> {OUT}")
    print(f"duracion: {d} s   (guion: {datos['total']} s)")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "preview":
        preview()
    else:
        render()
