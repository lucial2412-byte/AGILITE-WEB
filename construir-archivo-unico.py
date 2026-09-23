#!/usr/bin/env python3
"""Genera un HTML de un solo archivo, con las imágenes incrustadas.

    python3 construir-archivo-unico.py

Produce `agilite-pilates-completo.html`: no necesita la carpeta `assets`,
así que se puede enviar por correo o WhatsApp y abrir con doble clic.
El original (index.html + assets/) sigue siendo la versión de trabajo.
"""
import base64, pathlib, re, sys

RAIZ = pathlib.Path(__file__).parent
FUENTE = RAIZ / "index.html"
SALIDA = RAIZ / "agilite-pilates-completo.html"
TIPOS = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
         ".webp": "image/webp", ".svg": "image/svg+xml"}

html = FUENTE.read_text(encoding="utf-8")
referencias = sorted(set(re.findall(r"assets/[\w.-]+", html)), key=len, reverse=True)
if not referencias:
    sys.exit("No se encontró ninguna referencia a assets/ en index.html")

incrustadas = 0
for ref in referencias:
    archivo = RAIZ / ref
    if not archivo.exists():
        sys.exit(f"Falta el archivo {ref}")
    tipo = TIPOS.get(archivo.suffix.lower())
    if not tipo:
        sys.exit(f"Tipo de imagen no contemplado: {ref}")
    datos = base64.b64encode(archivo.read_bytes()).decode("ascii")
    html = html.replace(ref, f"data:{tipo};base64,{datos}")
    incrustadas += 1
    print(f"  incrustada  {ref:34} {archivo.stat().st_size/1024:7.1f} KB")

if "assets/" in html:
    sys.exit("Quedaron referencias a assets/ sin incrustar")

SALIDA.write_text(html, encoding="utf-8")
print(f"\n{incrustadas} imágenes incrustadas")
print(f"{SALIDA.name}: {SALIDA.stat().st_size/1024/1024:.2f} MB")
