# Video promocional CH Hats — mayoristas

**Archivo:** `CH-Hats-mayoristas.mp4` · 1080×1920 · 30 fps · **49.2 s** · **sin pista de audio**

El video sale en silencio a propósito: la voz se le agrega después. Los cortes están
en tiempos parejos para que calce una locución encima sin tener que reeditar.

## Guion

Los subtítulos aparecen **palabra por palabra** en Playfair Display Bold.
Blanco = texto normal · **Dorado** = palabra con énfasis.

| Tiempo | Texto en pantalla | Imagen |
|---|---|---|
| 0.0–0.4 | — | negro |
| 0.4–3.3 | ¿Querés **emprender** en **Honduras** | gorras, acercamiento |
| 3.3–3.4 | — | flash azul |
| 3.4–5.8 | pero no sabés con **qué** | campo azul desenfocado |
| 5.8–8.7 | todos buscan una idea nueva | gorras, alejamiento |
| 8.7–8.8 | — | flash blanco |
| 8.8–11.9 | y la que ya **vende** la tenés **enfrente** | gorras, acercamiento |
| 11.9–12.0 | — | flash azul |
| 12.0–13.9 | gorras en **tendencia** | detalle de producto |
| 13.9–15.7 | a nivel **nacional** | detalle de producto |
| 15.7–17.2 | — | producto puro, sin texto |
| 17.2–19.5 | **CH HATS** | foto limpia de la gorra sobre negro |
| 19.5–19.6 | — | flash blanco |
| 19.6–22.1 | al público **L.950** | gorras |
| 22.1–24.8 | vos la llevás mucho **menos** | gorras |
| 24.8–24.9 | — | flash azul |
| 24.9–27.1 | desde **3** **unidades** | campo azul |
| 27.1–29.4 | precio de **mayorista** | gorras |
| 29.4–32.2 | la diferencia es tu **ganancia** | gorras negras con relieve |
| 32.2–34.7 | vendés en tu **zona** | gorra H rosada |
| 34.7–34.8 | — | flash blanco |
| 34.8–37.2 | mientras más **comprás** | gorras |
| 37.2–39.4 | **mejor** **precio** te damos | gorras |
| 39.4–41.5 | escribinos al **WhatsApp** | gorras |
| 41.5–44.2 | **9804-9467** | negro, número sostenido |
| 44.2–45.9 | y arrancás **hoy** | gorras |
| 45.9–49.2 | logo CH · gorrasch.shop · WhatsApp 9804-9467 | cierre |

## Datos que afirma el video

- Precio al público: **L.950** por unidad
- Mayorista: **desde 3 unidades**, precio se pasa por privado
- A más volumen, mejor precio
- WhatsApp: **9804-9467**
- Web: **gorrasch.shop**

## Estilo copiado del video de referencia

- Subtítulos palabra por palabra, serif bold, centrados, con halo negro suave
- Dos colores: blanco y dorado `#F7C63E` (el dorado de la marca)
- Flashes de 3–4 fotogramas a azul `#02308d` y a blanco entre bloques
- Campos azules desenfocados con el producto insinuado detrás
- Grading oscuro con viñeta y encuadre cerrado

## Cómo regenerarlo

```bash
python3 build_video.py
```

Necesita `ffmpeg` y la fuente Playfair Display instalada en
`/usr/share/fonts/playfair` (la variante `Playfair Lining` es Playfair Display
con las cifras *lining* activadas de fábrica, para que el teléfono y el precio
se lean derechos en vez de con cifras oldstyle).

El guion se edita en la lista `BEATS` dentro de `build_video.py`: cada renglón es
`(imagen, duración, [(palabra, estilo)])`. Cambiar texto o tiempos es editar esa
lista y volver a correr el script.

## Pendiente

Solo hay 34 s de material y es una sola toma (gorras sobre la cama). Con clips de
empaque, gorras puestas, entregas o el local, el video puede quedar bastante mejor
y sin tanta repetición de encuadre.
