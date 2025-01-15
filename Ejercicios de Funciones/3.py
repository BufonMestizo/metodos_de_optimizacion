# Ejercicio 3: Tiempo total de procesamiento
import numpy as np
import matplotlib.pyplot as plt

def tiempo_procesamiento(k, D, c):
    return k * D + c

D = np.linspace(0, 1000, 100)  # Tamaño de los datos
T = tiempo_procesamiento(k=0.5, D=D, c=10)

plt.figure(3)
plt.plot(D, T, label="Tiempo de procesamiento", color="green")
plt.title("Tiempo total de procesamiento")
plt.xlabel("Tamaño de los datos (D)")
plt.ylabel("Tiempo (T)")
plt.legend()
plt.grid()
plt.show()
