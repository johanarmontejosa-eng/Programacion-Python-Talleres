import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer imagen
imagen = cv2.imread(r"c:\Users\57301\Desktop\PYTHON\mazda.png")

# Convertir a gris
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Binarización automática
_, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

binaria = binaria // 255

# Invertir
binaria = cv2.bitwise_not(binaria)

# Convertir a 0 y 1
binaria = binaria // 255

filas, columnas = binaria.shape
boundaries = []

# Recorrer píxel por píxel
for i in range(1, filas-1):
    for j in range(1, columnas-1):
        if binaria[i, j] == 1:

            # Verificar vecinos
            if (binaria[i-1, j] == 0 or
                binaria[i+1, j] == 0 or
                binaria[i, j-1] == 0 or
                binaria[i, j+1] == 0):

                boundaries.append((j, i))  # X=j, Y=i

# Separar coordenadas
coordenadas_X = [p[0] for p in boundaries]
coordenadas_Y = [p[1] for p in boundaries]

print("Primeras 20 coordenadas:")
for k in range(len(coordenadas_X)):
    print("X:", coordenadas_X[k], "Y:", coordenadas_Y[k])

# Graficar
plt.figure()
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))

for x, y in zip(coordenadas_X, coordenadas_Y):
    plt.plot(x, y, 'w.')

plt.title("Contorno")
plt.show()

plt.figure()

plt.plot(coordenadas_X, coordenadas_Y, 'k.')  # puntos negros
plt.gca().invert_yaxis()  # importante en imágenes (origen arriba)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Contorno en plano cartesiano")
plt.grid(True)

plt.show()