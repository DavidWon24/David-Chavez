# Video promocional CH Hats — mayoristas

**Archivo:** `CH-Hats-mayoristas.mp4` · 1080×1920 · 30 fps · **50.7 s** · **sin pista de audio**

El video sale en silencio a propósito: la voz se le agrega después.
Los tiempos para grabar la locución están en **[`audio-elevenlabs.md`](audio-elevenlabs.md)**.

## Guion

Los subtítulos aparecen **palabra por palabra** en Playfair Display Bold.
Blanco = texto normal · **Dorado** = palabra con énfasis.

| Tiempo | Texto en pantalla | Imagen |
|---|---|---|
| 0.00–0.40 | — | negro |
| 0.40–3.30 | ¿Querés **emprender** en **Honduras** | gorras, acercamiento |
| 3.30–3.42 | — | flash azul |
| 3.42–5.82 | pero no sabés con **qué** | campo azul desenfocado |
| 5.82–8.72 | todos buscan una idea nueva | gorras, alejamiento |
| 8.72–8.82 | — | flash blanco |
| 8.82–11.92 | y la que ya **vende** la tenés **enfrente** | gorras, acercamiento |
| 11.92–12.04 | — | flash azul |
| 12.04–13.94 | gorras en **tendencia** | detalle de producto |
| 13.94–15.74 | a nivel **nacional** | detalle de producto |
| 15.74–17.24 | — | producto puro, sin texto |
| 17.24–19.54 | **CH HATS** | foto limpia de la gorra sobre negro |
| 19.54–19.64 | — | flash blanco |
| 19.64–22.74 | al público **L.950** | gorras |
| 22.74–25.44 | vos la llevás mucho **menos** | gorras |
| 25.44–25.56 | — | flash azul |
| 25.56–27.76 | desde **3** **unidades** | campo azul |
| 27.76–30.06 | precio de **mayorista** | gorras |
| 30.06–32.86 | la diferencia es tu **ganancia** | gorras negras con relieve |
| 32.86–35.36 | vendés en tu **zona** | gorra H rosada |
| 35.36–35.46 | — | flash blanco |
| 35.46–37.86 | mientras más **comprás** | gorras |
| 37.86–40.06 | **mejor** **precio** te damos | gorras |
| 40.06–42.16 | escribinos al **WhatsApp** | gorras |
| 42.16–45.76 | **9804-9467** | negro, número sostenido |
| 45.76–47.46 | y arrancás **hoy** | gorras |
| 47.46–50.66 | logo CH · gorrasch.shop · WhatsApp 9804-9467 | cierre |

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

Necesita `ffmpeg` en `/projects/bin` y las fuentes en `/projects/fonts`
(rutas absolutas al inicio del script, se cambian ahí si hace falta).

`Playfair Lining` es Playfair Display con las cifras *lining* activadas de fábrica,
para que el teléfono y el precio se lean derechos en vez de con cifras oldstyle,
que es como salen por defecto en esa tipografía.

El guion se edita en la lista `BEATS`: cada renglón es
`(imagen, duración, [(palabra, estilo)])`. Cambiar texto o tiempos es editar esa
lista y volver a correr el script — los subtítulos se recalculan solos.

## Pendiente

Solo hay 34 s de material y es una sola toma (gorras sobre la cama). Con clips de
empaque, gorras puestas, entregas o el local, el video puede quedar bastante mejor
y sin tanta repetición de encuadre.
