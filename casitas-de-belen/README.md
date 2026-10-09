# Casitas de Belén · Tienda online

Sitio de la tienda de accesorios y decoraciones para pesebres. HTML, CSS y
JavaScript puros, sin librerías ni compilación: se publica tal cual en
cualquier hosting y se abre con doble clic en `index.html`.

```
index.html             la tienda (estructura, estilos y lógica en un archivo)
img/                   logo optimizado en AVIF / WebP / JPEG + íconos
fuente/                logo original (1408×768, 500 KB) — NO se publica
optimizar-logo.py      regenera img/ a partir del original
manifest.webmanifest   ícono y colores al "agregar a la pantalla de inicio"
.htaccess              caché y compresión para Apache / hosting compartido
_headers               caché para Netlify / Cloudflare Pages
```

## Velocidad: objetivo < 3 s

Medido con Chromium simulando un celular (sin caché):

| Red                                | LCP      | Transferido |
|------------------------------------|----------|-------------|
| 4G lento (perfil Lighthouse móvil) | ~0,5 s   | 58 KB       |
| 3G rápido                          | ~1,4 s   | 58 KB       |
| 3G lento (400 kbps, CPU ×6)        | ~1,6 s   | 58 KB       |
| Escritorio                         | ~0,1 s   | 38 KB       |

CLS (saltos de la página al cargar): 0.

### Qué se hizo con el logo

1. **Recorte al emblema.** El original tiene mucho margen vacío; se recorta
   a un cuadrado de 628 px.
2. **Formatos modernos con respaldo.** `<picture>` sirve AVIF (el más
   liviano), luego WebP y por último JPEG para navegadores viejos.
3. **Un tamaño por pantalla.** `srcset` + `sizes` con 6 anchos (96 a 628 px):
   el header descarga ~2–5 KB y el logo grande ~10–25 KB, en lugar de 500 KB.
4. **Prioridad.** `preload` + `fetchpriority="high"`: el logo se pide antes
   que cualquier otra cosa.
5. **Sin saltos.** `width` y `height` fijos reservan su espacio.
6. **Fondo que no se nota.** El crema del original tiene ruido y no
   coincide con la página; se reemplaza por `#faf8eb`, un crema que AVIF,
   WebP y JPEG devuelven idéntico, el mismo de `--crema` en la página.
7. **Favicon e íconos** a partir de la casita (el texto no se lee a 32 px).

### Qué se hizo con la página

- CSS en línea (cero archivos que bloqueen el pintado).
- Sin fuentes web: tipografías del sistema, se ven al instante.
- Íconos e ilustraciones en SVG en línea (0 peticiones).
- JavaScript propio de ~3 KB, al final del documento, sin librerías.
- Caché de un año para imágenes y compresión del HTML (`.htaccess`, `_headers`).

### Para mantenerlo bajo 3 s al crecer

- **Fotos de productos:** cuando reemplaces las ilustraciones por fotos,
  expórtalas en WebP/AVIF a ~600 px, ponles `width`/`height` y
  `loading="lazy"` (todas menos las que se ven sin hacer scroll).
- **No agregues** sliders, fuentes de Google o widgets de chat pesados
  arriba de la página; si los necesitas, que carguen al final.
- Si cambias el logo, reemplaza `fuente/logo-original.jpg` y corre:

  ```bash
  python3 optimizar-logo.py    # requiere Pillow y numpy
  ```

## Antes de publicar

- Cambia `WHATSAPP` en `index.html` por el número real (código de país +
  número, sin espacios). Los pedidos del carrito llegan ahí ya escritos.
- Ajusta productos y precios en la lista `PRODUCTOS` del mismo archivo.
- Cambia el correo del pie de página.
- No subas la carpeta `fuente/` al hosting.
