import numpy as np
import matplotlib.pyplot as plt
from scipy import signal  # Libreria para la funcion de transferencia 

print("Forma del denominador: a*s^2 + b*s + c")

a = float(input("Ingrese el coeficiente 'a' (termino s^2): "))
b = float(input("Ingrese el coeficiente 'b' (termino s): "))
c = float(input("Ingrese el coeficiente 'c' (termino independiente): "))

# Se asume ganancia unitaria
num = [c]       
den = [a, b, c] 

# Creacion de la funcion de transferencia 
sistema = signal.TransferFunction(num, den)

wn = np.sqrt(c / a)
zeta = (b / a) / (2 * wn)
tipo_sistema = ""

if zeta > 1:
    tipo_sistema = "SOBREAMORTIGUADO"
elif zeta == 1:
    tipo_sistema = "CRITICAMENTE AMORTIGUADO"
elif 0 < zeta < 1:
    tipo_sistema = "SUBAMORTIGUADO"
elif zeta == 0:
    tipo_sistema = "OSCILATORIO PURO"
else:
    tipo_sistema = "INESTABLE"

print("\n" + "="*40)
print(f"RESULTADOS DEL ANÁLISIS:")
print(f"-> Frecuencia Natural (Wn): {wn:.2f} rad/s")
print(f"-> Factor de Amortiguamiento (Zeta): {zeta:.4f}")
print(f"-> CLASIFICACIÓN: {tipo_sistema}")
print("="*40)

tiempo, amplitud = signal.step(sistema)

plt.figure(figsize=(8, 5)) 
plt.plot(tiempo, amplitud, label='Respuesta del sistema', color='blue', linewidth=2)

plt.title(f"Respuesta al escalon - {tipo_sistema}")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")    
plt.axhline(1, color='red', linestyle='--', label='Referencia (Set Point)')
plt.legend()
plt.show()