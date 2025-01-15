# Ejercicio 5: Medición calibrada
import numpy as np
import matplotlib.pyplot as plt

def medicion_calibrada(a, R, b):
    return a * R + b

R = np.linspace(0, 100, 100)  # Medición en crudo
M = medicion_calibrada(a=1.5, R=R, b=5)

plt.figure(5)
plt.plot(R, M, label="Medición calibrada", color="purple")
plt.title("Medición calibrada")
plt.xlabel("Medición en crudo (R)")
plt.ylabel("Medición calibrada (M)")
plt.legend()
plt.grid()
plt.show()
