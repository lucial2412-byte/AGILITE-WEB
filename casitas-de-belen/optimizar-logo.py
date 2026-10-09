#!/usr/bin/env python3
"""Genera las versiones web del logo a partir de fuente/logo-original.jpg.

    python3 optimizar-logo.py

El original pesa ~500 KB y mide 1408x768 con mucho margen vacío. Aquí se
recorta al emblema y se exporta en AVIF, WebP y JPEG a varios anchos, para
que cada pantalla descargue sólo el tamaño que necesita (unos pocos KB).
También crea el favicon y los íconos para móviles a partir de la casita.
"""
import pathlib
from PIL import Image, ImageChops

RAIZ = pathlib.Path(__file__).parent
ORIGINAL = RAIZ / "fuente" / "logo-original.jpg"
SALIDA = RAIZ / "img"
ANCHOS = [96, 160, 240, 320, 480, 628]   # 628 = tamaño máximo real del emblema

SALIDA.mkdir(exist_ok=True)
im = Image.open(ORIGINAL).convert("RGB")

# Recorte cuadrado al emblema: se detecta todo lo que no es el fondo crema.
fondo = Image.new("RGB", im.size, im.getpixel((im.width // 2, 20)))
mascara = ImageChops.difference(im, fondo).convert("L").point(lambda p: 255 if p > 28 else 0)
l, t, r, b = mascara.getbbox()
lado = max(r - l, b - t) + 16
cx, cy = (l + r) // 2, (t + b) // 2
emblema = im.crop((cx - lado // 2, cy - lado // 2, cx + lado // 2, cy + lado // 2))
# Fondo plano: el crema del JPEG original tiene ruido y no coincide con el de
# la página, así que se ve un "cuadro". Todo lo que es casi fondo se pinta con
# el crema exacto de la página (--crema en index.html), con una rampa suave
# para no romper el antialias. Además el fondo plano comprime mucho mejor.
# #faf8eb se eligió porque AVIF, WebP y JPEG lo devuelven idéntico (otros
# cremas se corren 1–2 tonos al pasar a YUV y vuelve a notarse el cuadro).
# (Probamos con transparencia: el archivo pesa el doble y no se ve mejor.)
import numpy as np
PAGINA = np.array([250, 248, 235], dtype=np.float32)
px = np.asarray(emblema, dtype=np.float32)
bg = np.array(fondo.getpixel((0, 0)), dtype=np.float32)
dist = np.sqrt(((px - bg) ** 2).sum(-1))
alfa = np.clip((dist - 14) / 26, 0, 1)[..., None]
emblema = Image.fromarray((px * alfa + PAGINA * (1 - alfa)).round().astype(np.uint8), "RGB")

print(f"emblema {emblema.size[0]}x{emblema.size[1]}  fondo #{'%02x%02x%02x' % fondo.getpixel((0, 0))}")

def guardar(img, nombre, **kw):
    ruta = SALIDA / nombre
    img.save(ruta, **kw)
    print(f"  {nombre:28} {ruta.stat().st_size / 1024:6.1f} KB")

for ancho in ANCHOS:
    v = emblema.resize((ancho, ancho), Image.LANCZOS)
    guardar(v, f"logo-{ancho}.avif", quality=55, speed=4)
    guardar(v, f"logo-{ancho}.webp", quality=80, method=6)
    guardar(v, f"logo-{ancho}.jpg", quality=82, optimize=True, progressive=True)

# Ícono: la casita sola (el texto no se lee a 32 px).
e = emblema.width / 628
casita = emblema.crop((int(118 * e), int(30 * e), int(510 * e), int(422 * e)))
for ancho, nombre in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"),
                      (192, "icon-192.png"), (512, "icon-512.png")]:
    # PNG de 256 colores: pesa una fracción y no se nota la diferencia.
    v = casita.resize((ancho, ancho), Image.LANCZOS).quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
    guardar(v, nombre, optimize=True)
