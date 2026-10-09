
from pathlib import Path
from textwrap import fill

archivo = Path("preguntas _analisis.txt")

if not archivo.exists():
    print(f"No se encontró el archivo: {archivo}")
    raise SystemExit(1)

texto = archivo.read_text(encoding="utf-8")
lineas = texto.splitlines()
resultado = []

for linea in lineas:
    if not linea.strip():
        resultado.append("")
    elif set(linea.strip()) in ({"="}, {"-"}):
        resultado.append(linea)
    else:
        resultado.extend(fill(linea, width=80).splitlines())

archivo.write_text(
    "\n".join(resultado) + "\n",
    encoding="utf-8"
)

print("¡Documento organizado correctamente!")