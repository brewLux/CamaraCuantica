# Cámara Cuántica

Simulación en Python de una cámara basada en la medición libre de interacción. Cada píxel de una imagen en blanco y negro se trata como una bomba de Elitzur-Vaidman y se somete al interferómetro de Mach-Zehnder (simulado con números aleatorios), de modo que el resultado es una imagen parcial del objeto, obtenida sin "iluminarlo". El modelo y el análisis de resultados están en el informe (`docs/`).

## Estructura

```
├── camara.py          # Programa principal: conversión a blanco y negro, simulación y ventana de resultados
├── requirements.txt   # Dependencias (Pillow y matplotlib)
├── imagenes/          # Imágenes de entrada
├── resultados/        # Imágenes generadas (<nombre>_resultado.png)
└── docs/              # Informe en PDF y capturas de las pruebas
```

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
python camara.py imagenes/silueta.png
```

Se abre una ventana con la imagen original, su versión en blanco y negro y el resultado del protocolo. El resultado también se guarda en `resultados/`.
