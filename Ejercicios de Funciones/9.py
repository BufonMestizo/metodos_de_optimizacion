# Ejercicio 9: Número de likes
import numpy as np
import matplotlib.pyplot as plt

def likes(m, F, b):
    return m * F + b

F = np.linspace(0, 1000, 100)  # Número de seguidores
L = likes(m=0.05, F=F, b=10)

plt.figure(9)
plt.plot(F, L, label="Número de likes", color="teal")
plt.title("Número de likes")
plt.xlabel("Número de seguidores (F)")
plt.ylabel("Likes (L)")
plt.legend()
plt.grid()
plt.show()
