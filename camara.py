import sys
from PIL import Image

ruta = sys.argv[1]
imagen = Image.open(ruta).convert("L")
ancho, alto = imagen.size

print("Ancho:", ancho)
print("Alto:", alto)
print("Total de pixeles:", ancho * alto)

negros = 0
blancos = 0

for y in range(alto):
    for x in range(ancho):
        valor = imagen.getpixel((x, y))
        if valor == 0:
            negros += 1
        else:
            blancos += 1

print("Negros:", negros)
print("Blancos:", blancos)
