import sys # lee lo que se escribe en la terminal al ejecutar (la ruta de la imagen)
import os # trabaja con rutas y carpetas (nombre del archivo y crear "resultados")
import random # permide simular numeros pseudoaleatorios para el interferometro
from PIL import Image # Pillow: abre, crea, modifica y guarda imagenes
import matplotlib.pyplot as plt # dibuja la ventana con las imagenes

max_pruebas = 7 # numero maximo de pruebas por foton (constante ajustable)
umbral = 128 # umbral de una imagen (constante ajustable)

# simula el sistema sobre un pixel
# cada vuelta del for es un foton y el sorteo sigue el arbol de probabilidad
# un pixel blanco nunca entra al if, asi que siempre termina inconcluso
def probar_pixel(es_negro):
    for prueba in range(max_pruebas):
        if es_negro:
            sorteo = random.random()
            if sorteo < 0.5:
                return "explota"
            elif sorteo < 0.75:
                return "detecta"
    return "inconcluso"

# lee la ruta escrita en el terminal, saca el nombre del archivo sin carpeta ni extension
# abre la imagen a color, obtiene su resolucion y crea una copia en grises
ruta = sys.argv[1]
nombre = os.path.splitext(os.path.basename(ruta))[0]
original = Image.open(ruta).convert("RGB")
ancho, alto = original.size
grises = original.convert("L")

# pasa a blanco y negro: crea un lienzo en blanco y pinta de negro los pixeles mas oscuros que el umbral
# esto se hace para cada pixel
imagen = Image.new("L", (ancho, alto), 255)
for y in range(alto):
    for x in range(ancho):
        if grises.getpixel((x, y)) < umbral:
            imagen.putpixel((x, y), 0)

# muestra la resolucion: ancho * alto es la cantidad de pixeles (bombas) a probar
print("Ancho:", ancho)
print("Alto:", alto)
print("Total de pixeles:", ancho * alto)

# contadores de cada resultado
explotadas = 0
detectadas = 0
inconclusos = 0

# lienzo blanco donde se pintara el resultado
resultado_img = Image.new("L", (ancho, alto), 255)

# recorre cada pixel de la imagen en blanco y negro, verifica si es negro, los prueba con el interferometro y pinta los resultados en el lienzo
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

# explicar que, como y porque se esta imprimiento en pantalla
print("Explotadas:", explotadas)
print("Detectadas:", detectadas)
print("Inconclusos:", inconclusos)

# crea la carpeta resultados si no existe, y guarda la imagen con el nombre [nombre_original]_resultado.png
os.makedirs("resultados", exist_ok=True)
resultado_img.save("resultados/" + nombre + "_resultado.png")

# se crea una ventana de 1 fila * 3 columnas
figura, ejes = plt.subplots(1, 3)

ejes[0].imshow(original) # muestra la imagen
ejes[0].set_title("Original") # titulo del subplot
ejes[0].axis("off") # quita los numeros de los ejes

# cmap="gray" traduce los numeros a grises, vmin y vmax fijan los colores a los extremos (blanco o negro)
ejes[1].imshow(imagen, cmap="gray", vmin=0, vmax=255)
ejes[1].set_title("Blanco y negro")
ejes[1].axis("off")

ejes[2].imshow(resultado_img, cmap="gray", vmin=0, vmax=255)
ejes[2].set_title("Resultado")
ejes[2].axis("off")

plt.show()
