import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
plt.title("Integrantes: SERGIO, EDWAR, KERLON, JOHAN")

ANCHO = 2
ALTO = 4
ESPACIO_X = 0.5
ESPACIO_Y = 2.0


# funcion para la creacion de las curvas
def arco(x_cen, y_cen, radio_x, radio_y, ang_ini, ang_fin):
    t = np.linspace(np.radians(ang_ini), np.radians(ang_fin), 50)
    x = x_cen + radio_x * np.cos(t)
    y = y_cen + radio_y * np.sin(t)
    return x, y

# funciones para la creacion de letras
def letra_R(x, y):
    plt.plot([x, x], [y, y + ALTO], 'k-', linewidth=2) 
    ax, ay = arco(x, y + ALTO*0.75, ANCHO, ALTO*0.25, -90, 90)
    plt.plot(ax, ay, 'k-', linewidth=2)
    plt.plot([x, x + ANCHO], [y + ALTO/2, y], 'k-', linewidth=2)

def letra_S(x, y):
    ax, ay = arco(x + ANCHO/2, y + ALTO*0.75, ANCHO/2, ALTO/4, 45, 270)
    bx, by = arco(x + ANCHO/2, y + ALTO*0.25, ANCHO/2, ALTO/4, 90, -135)
    plt.plot(np.concatenate([ax, bx]), np.concatenate([ay, by]), 'k-', linewidth=2)

def letra_E(x, y):
    plt.plot([x+ANCHO, x, x, x+ANCHO], [y+ALTO, y+ALTO, y, y], 'k-', linewidth=2)
    plt.plot([x, x+ANCHO*0.8], [y+ALTO/2, y+ALTO/2], 'k-', linewidth=2)

def letra_G(x, y):
    ax, ay = arco(x + ANCHO/2, y + ALTO/2, ANCHO/2, ALTO/2, 45, 360)
    plt.plot(ax, ay, 'k-', linewidth=2)
    plt.plot([x+ANCHO/2, x+ANCHO], [y+ALTO/3, y+ALTO/3], 'k-', linewidth=2)
    plt.plot([x+ANCHO, x+ANCHO], [y+ALTO/3, y], 'k-', linewidth=2)

def letra_I(x, y):
    plt.plot([x+ANCHO/2, x+ANCHO/2], [y, y+ALTO], 'k-', linewidth=2)
    plt.plot([x, x+ANCHO], [y+ALTO, y+ALTO], 'k-', linewidth=2)
    plt.plot([x, x+ANCHO], [y, y], 'k-', linewidth=2)

def letra_O(x, y):
    ax, ay = arco(x+ANCHO/2, y+ALTO/2, ANCHO/2, ALTO/2, 0, 360)
    plt.plot(ax, ay, 'k-', linewidth=2)

def letra_D(x, y):
    plt.plot([x, x], [y, y+ALTO], 'k-', linewidth=2)
    ax, ay = arco(x, y+ALTO/2, ANCHO, ALTO/2, -90, 90)
    plt.plot(ax, ay, 'k-', linewidth=2)

def letra_W(x, y):
    px = [x, x+ANCHO*0.25, x+ANCHO*0.5, x+ANCHO*0.75, x+ANCHO]
    py = [y+ALTO, y, y+ALTO/2, y, y+ALTO]
    plt.plot(px, py, 'k-', linewidth=2)

def letra_A(x, y):
    plt.plot([x, x+ANCHO/2, x+ANCHO], [y, y+ALTO, y], 'k-', linewidth=2)
    plt.plot([x+ANCHO*0.25, x+ANCHO*0.75], [y+ALTO/2, y+ALTO/2], 'k-', linewidth=2)

def letra_K(x, y):
    plt.plot([x, x], [y, y+ALTO], 'k-', linewidth=2)
    plt.plot([x, x+ANCHO], [y+ALTO/2, y+ALTO], 'k-', linewidth=2)
    plt.plot([x, x+ANCHO], [y+ALTO/2, y], 'k-', linewidth=2)

def letra_L(x, y):
    plt.plot([x, x, x+ANCHO], [y+ALTO, y, y], 'k-', linewidth=2)

def letra_N(x, y):
    plt.plot([x, x, x+ANCHO, x+ANCHO], [y, y+ALTO, y, y+ALTO], 'k-', linewidth=2)

def letra_J(x, y):
    ax, ay = arco(x+ANCHO/2, y+ALTO*0.25, ANCHO/2, ALTO/4, 180, 360)
    plt.plot(ax, ay, 'k-', linewidth=2)
    plt.plot([x+ANCHO, x+ANCHO], [y+ALTO*0.25, y+ALTO], 'k-', linewidth=2)
    plt.plot([x, x+ANCHO], [y+ALTO, y+ALTO], 'k-', linewidth=2)

def letra_H(x, y):
    plt.plot([x, x], [y, y+ALTO], 'k-', linewidth=2)
    plt.plot([x+ANCHO, x+ANCHO], [y, y+ALTO], 'k-', linewidth=2)
    plt.plot([x, x+ANCHO], [y+ALTO/2, y+ALTO/2], 'k-', linewidth=2)


diccionario = {
    'S': letra_S, 'E': letra_E, 'R': letra_R, 'G': letra_G, 'I': letra_I, 'O': letra_O,
    'D': letra_D, 'W': letra_W, 'A': letra_A, 'K': letra_K, 'L': letra_L, 'N': letra_N,
    'J': letra_J, 'H': letra_H
}

nombres = ["SERGIO", "EDWAR", "KERLON", "JOHAN"]

pos_x = 0
pos_y = 12

# iteracion para la impresion de los nombre completos
for nombre in nombres:
    x_inicio = pos_x
    for letra in nombre:
        if letra in diccionario:
            diccionario[letra](pos_x, pos_y)
        pos_x += ANCHO + ESPACIO_X
    
    pos_y -= (ALTO + ESPACIO_Y)
    pos_x = 0

plt.axis('equal')
plt.axis('off')
plt.show()