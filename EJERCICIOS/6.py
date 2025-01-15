# Ejercicio 6: Tiempo de respuesta promedio
import numpy as np
import matplotlib.pyplot as plt

def tiempo_respuesta(m, S, b):
    return m * S + b

S = np.linspace(0, 200, 100)  # Número de solicitudes simultáneas
T = tiempo_respuesta(m=0.8, S=S, b=2)

plt.figure(6)
plt.plot(S, T, label="Tiempo de respuesta", color="brown")
plt.title("Tiempo de respuesta promedio")
plt.xlabel("Solicitudes simultáneas (S)")
plt.ylabel("Tiempo (T)")
plt.legend()
plt.grid()
plt.show()
