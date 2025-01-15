# Ejercicio 2: Ganancia mensual
import numpy as np
import matplotlib.pyplot as plt

def ganancia_mensual(c, N, b):
    return c * N + b

N = np.linspace(0, 500, 100)  # Número de predicciones
G = ganancia_mensual(c=50, N=N, b=1000)

plt.figure(2)
plt.plot(N, G, label="Ganancia mensual", color="orange")
plt.title("Ganancia mensual")
plt.xlabel("Número de predicciones (N)")
plt.ylabel("Ganancia (G)")
plt.legend()
plt.grid()
plt.show()
