# Video 2 — Buscamos vendedores

**Archivo:** `CH-Hats-vendedores.mp4` · 1080×1920 · 30 fps · **55.3 s** · **con voz incluida**

Este video **ya trae el audio**. No hay que grabar nada aparte. Solo falta que le
pongas la música inspiradora encima y los efectos de sonido.

- **Voz:** `es-HN-CarlosNeural` (masculina hondureña), a velocidad **+8 %**
- **Ritmo:** 125 palabras por minuto, corrido y sin arrastrar
- **Nivel:** pico en −4.8 dB, promedio −24 dB → queda espacio de sobra para
  meterle música sin que se sature
- **Silencios:** 3.05 s en total repartidos en 22 cortes, o sea el aire mínimo
  para que se note el cambio de idea y nada más

## Guion con tiempos

| Desde | Hasta | Lo que dice | Imagen |
|---|---|---|---|
| 0.00 | 2.78 | Estamos buscando vendedores en Honduras. | cartel negro |
| 2.88 | 5.21 | Y no necesitás comprar nada. | cartel blanco |
| 5.33 | 7.78 | Ni tener el producto en tus manos. | video de gorras |
| 7.94 | 10.05 | Sí, parece raro. | cartel blanco |
| 10.19 | 11.94 | Pero funciona así. | cartel negro |
| 12.16 | 14.83 | Publicás los videos de nuestras gorras. | mockup de celular |
| 14.91 | 17.12 | En tu TikTok o en tu estado. | gorra sobre blanco |
| 17.22 | 19.83 | Alguien te escribe porque le gustó una. | mockup de chat |
| 19.93 | 21.88 | Nosotros la enviamos. | gorra sobre blanco |
| 21.95 | 23.82 | Nosotros cobramos. | gorra sobre blanco |
| 23.89 | 26.12 | Nosotros damos la garantía. | gorra sobre blanco |
| 26.26 | 28.76 | Y cuando el cliente recibe su gorra, | video de gorras |
| 28.84 | 30.97 | vos ganás cien lempiras. | **flecha → L.100** |
| 31.17 | 33.12 | Por cada gorra vendida. | cartel blanco |
| 33.26 | 36.04 | Diez gorras en un mes son mil lempiras. | **contador 10 → L.1,000** |
| 36.22 | 37.92 | Sin inventario. | cartel negro |
| 37.99 | 39.77 | Sin poner dinero. | cartel negro |
| 39.84 | 42.07 | Sin arriesgar nada tuyo. | cartel blanco |
| 42.23 | 45.62 | Vos publicás. Nosotros el resto. | los 3 pasos |
| 45.78 | 48.85 | Si querés entrar, escribinos al WhatsApp. | mockup de chat |
| 48.95 | 52.31 | 9804-9467 | número grande |
| 52.45 | 54.94 | Y te explicamos todo hoy mismo. | cierre blanco |

Los subtítulos van **palabra por palabra**, y los tiempos no son estimados: el
motor de voz devuelve el instante exacto en que arranca cada palabra, así que
están clavados al audio.

## Lo que afirma el video

- Se buscan vendedores en Honduras
- No hay que comprar nada ni tener el producto
- El vendedor solo publica los videos de las gorras
- CH Hats se encarga del envío, el cobro y la garantía
- **L.100 por cada gorra vendida**, cuando el cliente recibe el producto
- Referencia: 10 gorras al mes = L.1,000
- Contacto: **WhatsApp 9804-9467**

## Estilo copiado del video de referencia

Del video de `@venta.silenciosa` saqué:

- **Blanco y negro puro**, sin colores
- **Sans-serif** (Inter) en lugar de la serif del video anterior
- Los carteles alternan **negro con texto blanco** y **blanco con texto negro**
- Primera palabra en negrita y el resto normal: *"**Sí,** parece raro."*
- El b-roll va en **tarjetas de esquinas redondeadas** sobre negro, no a pantalla
  completa
- Aparece rápido y por partes, siguiendo lo que se está diciendo

Las gorras de la web van **sobre fondo blanco y redondeadas**, como se pidió, no
recortadas sobre negro.

## Sobre los efectos y el stock de video

Probé las páginas pedidas y otras:

| Fuente | Resultado |
|---|---|
| motionarray.com | 403, pide cuenta |
| vecteezy.com | 403, pide cuenta |
| mixkit | 403 |
| pixabay | pide llave de API |
| pexels | solo responde por caché de CDN en consultas populares, no es fiable |

Así que **las animaciones están generadas, no descargadas**. La flecha que revela
L.100, el contador de gorras, los 3 pasos, el mockup de celular con el contador de
vistas subiendo y el chat con los mensajes apareciendo: todo hecho a medida. Sale
mejor que stock genérico porque va al mensaje, y no hay problemas de licencia.

## Archivos

| Archivo | Qué es |
|---|---|
| `CH-Hats-vendedores.mp4` | el video final, con voz |
| `guion-vendedores.md` | este documento |
| `guion2.py` | el guion: texto, subtítulo y visual de cada línea |
| `build2.py` | el generador completo |
| `subtitulos-vendedores.ass` | los subtítulos, editables aparte |

## Cómo cambiarlo

El guion está en `guion2.py`, en la lista `SEGMENTOS`. Cada renglón es:

```python
("s13", "vos ganás cien lempiras.",   # lo que dice la voz
        "vos ganás L.100",            # lo que se lee en pantalla
        "flecha", 0.20)               # visual y pausa después
```

Si cambiás un texto hay que regenerar la voz y volver a armar el video:

```bash
python3 build2.py            # render completo
python3 build2.py preview    # solo un PNG de cada tipo de visual, para revisar
```

**Para cambiar el ritmo:** `RATE` en `guion2.py`. Está en `+8%`. Si se quiere más
lento, `+4%` o `0%`; más rápido, `+12%`. La última columna de cada segmento es la
pausa que va después, en segundos — bajarlas hace el video más corrido.

**Para cambiar de voz:** `VOZ` en `guion2.py`. Hay otra hondureña
(`es-HN-KarlaNeural`, femenina) y también mexicanas, salvadoreñas y demás.

Requiere `ffmpeg` en `/projects/bin`, las fuentes Inter en `/projects/fonts` y los
paquetes `edge-tts`, `pillow` y `fonttools`.

## Pendiente

Sigue faltando material propio. Las gorras se ven, pero hay solo un video de 34 s
y las fotos de la web. Con clips de vos empacando, entregando, o mostrando gorras
puestas, el video se sentiría mucho más real y menos armado.
