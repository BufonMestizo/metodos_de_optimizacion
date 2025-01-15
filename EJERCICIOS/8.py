# Ejercicio 8: Energía consumida
import numpy as np
import matplotlib.pyplot as plt

def energia_consumida(k, O, b):
    return k * O + b

O = np.linspace(0, 500, 100)  # Número de operaciones realizadas
E = energia_consumida(k=0.2, O=O, b=10)

plt.figure(8)
plt.plot(O, E, label="Energía consumida", color="magenta")
plt.title("Energía consumida")
plt.xlabel("Número de operaciones (O)")
plt.ylabel("Energía (E)")
plt.legend()
plt.grid()
plt.show()
