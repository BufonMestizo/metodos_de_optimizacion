# Ejercicio 10: Costo total de entrenamiento
import numpy as np
import matplotlib.pyplot as plt

def costo_entrenamiento(p, I, c):
    return p * I + c

I = np.linspace(0, 1000, 100)  # Número de iteraciones
C = costo_entrenamiento(p=0.1, I=I, c=50)

plt.figure(10)
plt.plot(I, C, label="Costo total de entrenamiento", color="gray")
plt.title("Costo total de entrenamiento")
plt.xlabel("Número de iteraciones (I)")
plt.ylabel("Costo (C)")
plt.legend()
plt.grid()
plt.show()
