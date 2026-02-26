import matplotlib.pyplot as plt

# Valores del sensor PT100
R0 = 100.0
A = 0.0039083
B = -0.0000005775
C = -0.000000000004183

# Listas para guardar resultados
temperaturas = []
resistencias = []

# Recorrer temperaturas de -200 a 200 grados
for temperatura in range(-200, 200):
    temperaturas.append(temperatura)
    
    # Calcular resistencia según la temperatura
    if temperatura >= 0:
        resistencia = R0 * (1 + A*temperatura + B*(temperatura**2))
    else:
        resistencia = R0 * (1 + A*temperatura + B*(temperatura**2) + C*(temperatura - 100)*(temperatura**3))
    
    resistencias.append(resistencia)

# Dibujar la gráfica
plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, color='purple', linewidth=2)

plt.title("Sensor PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohmios)")
plt.grid(True)

plt.show()