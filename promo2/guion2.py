#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guion del video 2: reclutamiento de vendedores para CH Hats.
Cada segmento es una linea de voz. El audio manda: el video se construye
despues a partir de las duraciones REALES que devuelve el TTS.
"""

VOZ  = "es-HN-CarlosNeural"   # voz masculina hondureña
RATE = "+8%"                  # corrido y con energia, sin arrastrar las palabras

# (id, texto para la voz, subtitulo en pantalla, visual, pausa_despues)
#
# Las pausas van cortas a proposito: solo el aire minimo para que se note el
# corte entre ideas. Nada de silencios largos que frenen el video.
#
# visual:
#   negro            pantalla negra, solo texto
#   blanco           pantalla blanca, texto negro (los golpes del video de guia)
#   gorras:<n>       tarjeta redondeada con foto de gorra (fondo blanco)
#   footage:<seg>    tarjeta redondeada con el video de las gorras
#   flecha           animacion: flecha a la derecha revelando L.100
#   contador         animacion: 10 gorras -> L.1,000
#   celular          mockup de celular con un post de TikTok
#   chat             mockup de chat de WhatsApp
#   pasos            los 3 pasos apareciendo
#   negro_num        el numero de WhatsApp grande
#   cierre           cierre blanco con el numero
#
SEGMENTOS = [
    ("s01", "Estamos buscando vendedores en Honduras.",
            "Estamos buscando vendedores en Honduras.", "negro", 0.10),

    ("s02", "Y no necesitás comprar nada.",
            "Y no necesitás comprar nada.", "blanco", 0.12),

    ("s03", "Ni tener el producto en tus manos.",
            "Ni tener el producto en tus manos.", "footage:2.0", 0.16),

    ("s04", "Sí, parece raro.",
            "Sí, parece raro.", "blanco", 0.14),

    # unica pausa un poco mas marcada: cierra el gancho y abre la explicacion
    ("s05", "Pero funciona así.",
            "Pero funciona así.", "negro", 0.22),

    ("s06", "Publicás los videos de nuestras gorras.",
            "Publicás los videos de nuestras gorras.", "celular", 0.08),

    ("s07", "En tu TikTok o en tu estado.",
            "En tu TikTok o en tu estado.", "gorras:0", 0.10),

    ("s08", "Alguien te escribe porque le gustó una.",
            "Alguien te escribe porque le gustó una.", "chat", 0.10),

    ("s09", "Nosotros la enviamos.",
            "Nosotros la enviamos.", "gorras:1", 0.07),

    ("s10", "Nosotros cobramos.",
            "Nosotros cobramos.", "gorras:2", 0.07),

    ("s11", "Nosotros damos la garantía.",
            "Nosotros damos la garantía.", "gorras:3", 0.14),

    ("s12", "Y cuando el cliente recibe su gorra,",
            "Y cuando el cliente recibe su gorra…", "footage:9.0", 0.08),

    ("s13", "vos ganás cien lempiras.",
            "vos ganás L.100", "flecha", 0.20),

    ("s14", "Por cada gorra vendida.",
            "Por cada gorra vendida.", "blanco", 0.14),

    ("s15", "Diez gorras en un mes son mil lempiras.",
            "10 gorras = L.1,000", "contador", 0.18),

    ("s16", "Sin inventario.",
            "Sin inventario.", "negro", 0.07),

    ("s17", "Sin poner dinero.",
            "Sin poner dinero.", "negro", 0.07),

    ("s18", "Sin arriesgar nada tuyo.",
            "Sin arriesgar nada tuyo.", "blanco", 0.16),

    ("s19", "Vos publicás. Nosotros el resto.",
            "Vos publicás. Nosotros el resto.", "pasos", 0.16),

    ("s20", "Si querés entrar, escribinos al WhatsApp.",
            "Escribinos al WhatsApp", "chat", 0.10),

    # sin comas entre digitos: con comas el TTS mete pausas y se alarga muchisimo
    ("s21", "Nueve ocho cero cuatro, nueve cuatro seis siete.",
            "9804-9467", "negro_num", 0.14),

    # el cierre lleva el numero en pantalla: es el ultimo golpe del video
    ("s22", "Y te explicamos todo hoy mismo.",
            "Y te explicamos todo hoy mismo.", "cierre", 0.45),
]
