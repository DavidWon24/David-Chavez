# Video 2 — Buscamos vendedores

**Archivo:** `CH-Hats-vendedores.mp4` · 1080×1920 · 30 fps · **66.2 s** · **con voz incluida**

Este video **ya trae el audio**. No hay que grabar nada aparte. Solo falta que le
pongas la música inspiradora encima y los efectos de sonido que querías.

- **Voz:** `es-HN-CarlosNeural` (masculina hondureña), a velocidad −4 %
- **Nivel:** pico en −4.5 dB, promedio −24 dB → queda espacio de sobra para
  meterle música sin que se sature

## Guion con tiempos

| Desde | Hasta | Lo que dice | Imagen |
|---|---|---|---|
| 0.00 | 3.12 | Estamos buscando vendedores en Honduras. | cartel negro |
| 3.37 | 5.99 | Y no necesitás comprar nada. | cartel blanco |
| 6.34 | 9.10 | Ni tener el producto en tus manos. | video de gorras |
| 9.55 | 11.92 | Sí, parece raro. | cartel blanco |
| 12.32 | 14.29 | Pero funciona así. | cartel negro |
| 14.64 | 17.64 | Publicás los videos de nuestras gorras. | mockup de celular |
| 17.86 | 20.33 | En tu TikTok o en tu estado. | gorra sobre blanco |
| 20.59 | 23.52 | Alguien te escribe porque le gustó una. | mockup de chat |
| 23.82 | 25.98 | Nosotros la enviamos. | gorra sobre blanco |
| 26.18 | 28.27 | Nosotros cobramos. | gorra sobre blanco |
| 28.47 | 30.96 | Nosotros damos la garantía. | gorra sobre blanco |
| 31.36 | 34.17 | Y cuando el cliente recibe su gorra, | video de gorras |
| 34.47 | 36.87 | vos ganás cien lempiras. | **flecha → L.100** |
| 37.42 | 39.61 | Por cada gorra vendida. | cartel blanco |
| 39.96 | 43.10 | Diez gorras en un mes son mil lempiras. | **contador 10 → L.1,000** |
| 43.55 | 45.45 | Sin inventario. | cartel negro |
| 45.65 | 47.64 | Sin poner dinero. | cartel negro |
| 47.84 | 50.33 | Sin arriesgar nada tuyo. | cartel blanco |
| 50.78 | 54.60 | Vos publicás. Nosotros el resto. | los 3 pasos |
| 55.00 | 58.46 | Si querés entrar, escribinos al WhatsApp. | mockup de chat |
| 58.72 | 62.48 | 9804-9467 | número grande |
| 62.88 | 65.69 | Y te explicamos todo hoy mismo. | cierre blanco |

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

Las gorras de la web van **sobre fondo blanco y redondeadas**, como pediste, no
recortadas sobre negro.

## Sobre los efectos y el stock de video

Probé las páginas que mandaste y otras:

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
        "flecha", 0.55)               # visual y pausa después
```

Si cambiás un texto hay que regenerar la voz y volver a armar el video:

```bash
python3 build2.py            # render completo
python3 build2.py preview    # solo un PNG de cada tipo de visual, para revisar
```

Para cambiar de voz, editá `VOZ` en `guion2.py`. Hay otras hondureñas
(`es-HN-KarlaNeural`, femenina) y mexicanas, salvadoreñas, etc.

Requiere `ffmpeg` en `/projects/bin`, las fuentes Inter en `/projects/fonts` y los
paquetes `edge-tts`, `pillow` y `fonttools`.

## Pendiente

Sigue faltando material propio. Las gorras se ven, pero hay solo un video de 34 s
y las fotos de la web. Con clips de vos empacando, entregando, o mostrando gorras
puestas, el video se sentiría mucho más real y menos armado.
