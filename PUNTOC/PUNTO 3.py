import numpy as np
import matplotlib.pyplot as plt


V = float(input("Ingrese el voltaje (V): "))
R = float(input("Ingrese la resistencia (Ohmios): "))
C_micro = float(input("Ingrese la capacitancia (microFaradios µF): "))

# Convertir microFaradios a Faradios
C = C_micro * 1e-6


tau = R * C
print("Constante de tiempo (tau) =", tau, "segundos")


t = np.linspace(0, 5*tau, 1000)

Vc_carga = V * (1 - np.exp(-t/(R*C)))
Vc_descarga = V * np.exp(-t/(R*C))

#carga
plt.figure()
plt.plot(t, Vc_carga)
plt.title("Carga del Capacitor en Circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()
#descarga
plt.figure()
plt.plot(t, Vc_descarga)
plt.title("Descarga del Capacitor en Circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()