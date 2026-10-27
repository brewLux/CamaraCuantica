import sys
import os
import random
from PIL import Image
import matplotlib.pyplot as plt

max_pruebas = 7
umbral = 114

def probar_pixel(es_negro):
    for prueba in range(max_pruebas):
        if es_negro:
            sorteo = random.random()
            if sorteo < 0.5:
                return "explota"
            elif sorteo < 0.75:
                return "detecta"
    return "inconcluso"

ruta = sys.argv[1]
nombre = os.path.splitext(os.path.basename(ruta))[0]
original = Image.open(ruta).convert("RGB")
ancho, alto = original.size
grises = original.convert("L")

imagen = Image.new("L", (ancho, alto), 255)
for y in range(alto):
    for x in range(ancho):
        if grises.getpixel((x, y)) < umbral:
            imagen.putpixel((x, y), 0)

print("Ancho:", ancho)
print("Alto:", alto)
print("Total de pixeles:", ancho * alto)

explotadas = 0
detectadas = 0
inconclusos = 0

resultado_img = Image.new("L", (ancho, alto), 255)

for y in range(alto):
    for x in range(ancho):
        valor = imagen.getpixel((x, y))
        es_negro = (valor == 0)
        resultado = probar_pixel(es_negro)
        if resultado == "explota":
            explotadas += 1
        elif resultado == "detecta":
            detectadas += 1
            resultado_img.putpixel((x, y), 0)
        else:
            inconclusos += 1

print("Explotadas:", explotadas)
print("Detectadas:", detectadas)
print("Inconclusos:", inconclusos)
os.makedirs("resultados", exist_ok=True)
resultado_img.save("resultados/" + nombre + "_resultado.png")

figura, ejes = plt.subplots(1, 3)

ejes[0].imshow(original)
ejes[0].set_title("Original")
ejes[0].axis("off")

ejes[1].imshow(imagen, cmap="gray", vmin=0, vmax=255)
ejes[1].set_title("Blanco y negro")
ejes[1].axis("off")

ejes[2].imshow(resultado_img, cmap="gray", vmin=0, vmax=255)
ejes[2].set_title("Resultado")
ejes[2].axis("off")

plt.show()
