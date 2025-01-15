# Ejercicio 7: Ingresos de la plataforma
import numpy as np
import matplotlib.pyplot as plt

def ingresos(p, S, b):
    return p * S + b

S = np.linspace(0, 1000, 100)  # Número de suscriptores
I = ingresos(p=10, S=S, b=500)

plt.figure(7)
plt.plot(S, I, label="Ingresos de la plataforma", color="cyan")
plt.title("Ingresos de la plataforma")
plt.xlabel("Número de suscriptores (S)")
plt.ylabel("Ingresos (I)")
plt.legend()
plt.grid()
plt.show()
