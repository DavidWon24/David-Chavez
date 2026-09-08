#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guion del video 2: reclutamiento de vendedores para CH Hats.
Cada segmento es una linea de voz. El audio manda: el video se construye
despues a partir de las duraciones REALES que devuelve el TTS.
"""

VOZ  = "es-HN-CarlosNeural"   # voz masculina hondureña
RATE = "-4%"                  # un poco mas pausado = mas confiable

# (id, texto para la voz, subtitulo en pantalla, visual, pausa_despues)
#
# visual:
#   negro            pantalla negra, solo texto
#   blanco           pantalla blanca, texto negro (los golpes del video de guia)
#   card:<archivo>   tarjeta redondeada con imagen/video sobre negro
#   gorras:<n>       tarjeta con foto de gorra n (fondo blanco)
#   footage:<seg>    tarjeta redondeada con el video de las gorras
#   flecha           animacion: flecha a la derecha revelando L.100
#   contador         animacion: 10 gorras -> L.1,000
#   celular          mockup de celular con un post de TikTok
#   chat             mockup de chat de WhatsApp
#   pasos            los 3 pasos apareciendo
#
SEGMENTOS = [
    ("s01", "Estamos buscando vendedores en Honduras.",
            "Estamos buscando vendedores en Honduras.", "negro", 0.25),

    ("s02", "Y no necesitás comprar nada.",
            "Y no necesitás comprar nada.", "blanco", 0.35),

    ("s03", "Ni tener el producto en tus manos.",
            "Ni tener el producto en tus manos.", "footage:2.0", 0.45),

    ("s04", "Sí, parece raro.",
            "Sí, parece raro.", "blanco", 0.40),

    ("s05", "Pero funciona así.",
            "Pero funciona así.", "negro", 0.35),

    ("s06", "Publicás los videos de nuestras gorras.",
            "Publicás los videos de nuestras gorras.", "celular", 0.22),

    ("s07", "En tu TikTok o en tu estado.",
            "En tu TikTok o en tu estado.", "gorras:0", 0.26),

    ("s08", "Alguien te escribe porque le gustó una.",
            "Alguien te escribe porque le gustó una.", "chat", 0.30),

    ("s09", "Nosotros la enviamos.",
            "Nosotros la enviamos.", "gorras:1", 0.20),

    ("s10", "Nosotros cobramos.",
            "Nosotros cobramos.", "gorras:2", 0.20),

    ("s11", "Nosotros damos la garantía.",
            "Nosotros damos la garantía.", "gorras:3", 0.40),

    ("s12", "Y cuando el cliente recibe su gorra,",
            "Y cuando el cliente recibe su gorra…", "footage:9.0", 0.30),

    ("s13", "vos ganás cien lempiras.",
            "vos ganás L.100", "flecha", 0.55),

    ("s14", "Por cada gorra vendida.",
            "Por cada gorra vendida.", "blanco", 0.35),

    ("s15", "Diez gorras en un mes son mil lempiras.",
            "10 gorras = L.1,000", "contador", 0.45),

    ("s16", "Sin inventario.",
            "Sin inventario.", "negro", 0.20),

    ("s17", "Sin poner dinero.",
            "Sin poner dinero.", "negro", 0.20),

    ("s18", "Sin arriesgar nada tuyo.",
            "Sin arriesgar nada tuyo.", "blanco", 0.45),

    ("s19", "Vos publicás. Nosotros el resto.",
            "Vos publicás. Nosotros el resto.", "pasos", 0.40),

    ("s20", "Si querés entrar, escribinos al WhatsApp.",
            "Escribinos al WhatsApp", "chat", 0.26),

    # sin comas entre digitos: con comas el TTS mete pausas y se va a 6.7s
    ("s21", "Nueve ocho cero cuatro, nueve cuatro seis siete.",
            "9804-9467", "negro_num", 0.40),

    # el cierre lleva el numero en pantalla: es el ultimo golpe del video
    ("s22", "Y te explicamos todo hoy mismo.",
            "Y te explicamos todo hoy mismo.", "cierre", 0.55),
]
