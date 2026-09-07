# Guion de voz para ElevenLabs

**El audio completo tiene que durar 50.66 segundos** (el video mide 50.7 s).

Hay **18 segmentos de voz** y **3 huecos de silencio** a propósito. Los silencios
no son relleno: uno deja respirar el producto y el otro cierra con el logo.

---

## Cómo armarlo (recomendado)

ElevenLabs **no garantiza duraciones exactas**, así que no generés todo de un tiro.
Generá **cada segmento por separado** (18 clips) y colocá cada uno en el segundo que
dice la tabla. Así queda clavado con los subtítulos aunque un clip salga un poco
más corto o más largo.

En el editor: importás el video, importás los 18 audios, y arrastrás cada uno a su
marca de tiempo. La columna **"aire"** es el margen que sobra en cada hueco — todos
tienen de sobra menos el 8, que va justo.

---

## Los 18 segmentos

| # | Poner en | Hasta | Hueco | Voz ≈ | Aire | Texto para ElevenLabs |
|---|---|---|---|---|---|---|
| — | 0.00 | 0.40 | 0.40 s | — | — | *(silencio)* |
| 1 | **0.40** | 3.30 | 2.90 s | 1.9 s | 1.0 s | ¿Querés emprender en Honduras? |
| 2 | **3.42** | 5.82 | 2.40 s | 1.5 s | 0.9 s | Pero no sabés con qué. |
| 3 | **5.82** | 8.72 | 2.90 s | 2.1 s | 0.8 s | Todos buscan una idea nueva. |
| 4 | **8.82** | 11.92 | 3.10 s | 2.6 s | 0.6 s | Y la que ya vende, la tenés enfrente. |
| 5 | **12.04** | 13.94 | 1.90 s | 1.3 s | 0.6 s | Gorras en tendencia, |
| 6 | **13.94** | 15.74 | 1.80 s | 1.3 s | 0.5 s | a nivel nacional. |
| — | 15.74 | 17.24 | 1.50 s | — | — | *(silencio — el producto respira)* |
| 7 | **17.24** | 19.54 | 2.30 s | 0.4 s | 1.9 s | CH Hats. |
| 8 | **19.64** | 22.74 | 3.10 s | 3.0 s | 0.1 s | Al público, novecientos cincuenta lempiras. ⚠️ |
| 9 | **22.74** | 25.44 | 2.70 s | 1.7 s | 1.0 s | Vos la llevás mucho menos. |
| 10 | **25.56** | 27.76 | 2.20 s | 1.5 s | 0.7 s | Desde tres unidades, |
| 11 | **27.76** | 30.06 | 2.30 s | 1.5 s | 0.8 s | precio de mayorista. |
| 12 | **30.06** | 32.86 | 2.80 s | 2.1 s | 0.7 s | La diferencia es tu ganancia. |
| 13 | **32.86** | 35.36 | 2.50 s | 1.3 s | 1.2 s | Vendés en tu zona. |
| 14 | **35.46** | 37.86 | 2.40 s | 1.1 s | 1.3 s | Mientras más comprás, |
| 15 | **37.86** | 40.06 | 2.20 s | 1.5 s | 0.7 s | mejor precio te damos. |
| 16 | **40.06** | 42.16 | 2.10 s | 1.5 s | 0.6 s | Escribinos al WhatsApp. |
| 17 | **42.16** | 45.76 | 3.60 s | 3.2 s | 0.4 s | Nueve, ocho, cero, cuatro. Nueve, cuatro, seis, siete. |
| 18 | **45.76** | 47.46 | 1.70 s | 1.1 s | 0.6 s | Y arrancás hoy. |
| — | 47.46 | 50.66 | 3.20 s | — | — | *(silencio — cierre con logo)* |

⚠️ **El 8 va justo.** Si el clip te sale más largo de 3.10 s, quitale la palabra
final y dejá **"Al público, novecientos cincuenta."** — el `L.950` ya está en
pantalla, no se pierde nada.

---

## Guion corrido (si preferís leerlo de una)

> ¿Querés emprender en Honduras? Pero no sabés con qué.
> Todos buscan una idea nueva. Y la que ya vende, la tenés enfrente.
> Gorras en tendencia, a nivel nacional.
> CH Hats.
> Al público, novecientos cincuenta lempiras. Vos la llevás mucho menos.
> Desde tres unidades, precio de mayorista.
> La diferencia es tu ganancia. Vendés en tu zona.
> Mientras más comprás, mejor precio te damos.
> Escribinos al WhatsApp. Nueve, ocho, cero, cuatro. Nueve, cuatro, seis, siete.
> Y arrancás hoy.

Son **68 palabras en 50.66 s**, o sea un ritmo de ~81 palabras por minuto contando
los silencios. Es lento a propósito: así suena a alguien seguro de lo que vende,
no a alguien apurado.

---

## Ajustes en ElevenLabs

**Modelo:** Multilingual v2 (o el más nuevo que tengas). Voz **masculina
latinoamericana**, tono grave y calmado.

| Control | Valor | Por qué |
|---|---|---|
| Stability | **0.50 – 0.60** | firme sin sonar robótico |
| Similarity | 0.75 | |
| Style | **0.15 – 0.30** | poca exageración: la confianza es sobria |
| Speaker boost | activado | |

Si te queda demasiado plano subí Style un poco. Si te queda actuado, bajalo.

---

## Tres cosas que te van a dar problema

**1. Los números.** Van escritos **con letras** a propósito. Si escribís `9804-9467`
te lo va a leer "nueve mil ochocientos cuatro guion...". Igual con `L.950`: por eso
dice "novecientos cincuenta lempiras" y no "L.950".

**2. "CH Hats".** En español lo puede leer como "che hats". Si querés que diga las
letras separadas, escribilo **"Ce Hache Hats"** en el prompt. Probá las dos y quedate
con la que suene a como lo decís vos.

**3. El voseo.** El guion está en voseo hondureño: *querés, sabés, vos, escribinos,
arrancás, vendés, comprás*. La mayoría de voces lo lee bien, pero **escuchá el
segmento 16** ("escribinos") porque es el que más se equivocan. Si te lo lee raro,
probá otra voz antes de cambiar la palabra.

---

## Si querés cambiar los tiempos

Los huecos salen de la lista `BEATS` en `build_video.py`. Cambiás la duración de un
beat, volvés a correr el script, y se regenera el video con los subtítulos ya
recalculados. No hay que reeditar nada a mano.
