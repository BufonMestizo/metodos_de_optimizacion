# Ejercicio 4: Costo total de almacenamiento
import numpy as np
import matplotlib.pyplot as plt

def costo_almacenamiento(p, D, f):
    return p * D + f

D = np.linspace(0, 1000, 100)  # Cantidad de datos almacenados
C = costo_almacenamiento(p=2, D=D, f=50)

plt.figure(4)
plt.plot(D, C, label="Costo de almacenamiento", color="red")
plt.title("Costo total de almacenamiento")
plt.xlabel("Cantidad de datos (D)")
plt.ylabel("Costo (C)")
plt.legend()
plt.grid()
plt.show()
