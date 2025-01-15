import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1: Precio de una vivienda
def precio_vivienda(m, A, b):
    return m * A + b

A = np.linspace(0, 200, 100)  # Área construida
P = precio_vivienda(m=1500, A=A, b=20000)

plt.figure(1)
plt.plot(A, P, label="Precio de la vivienda")
plt.title("Precio de una vivienda")
plt.xlabel("Área construida (A)")
plt.ylabel("Precio (P)")
plt.legend()
plt.grid()
plt.show()
