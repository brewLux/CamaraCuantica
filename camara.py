import sys
from PIL import Image
import random

max_pruebas = 7

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
imagen = Image.open(ruta).convert("L")
ancho, alto = imagen.size

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
resultado_img.save("resultados/resultado.png")
