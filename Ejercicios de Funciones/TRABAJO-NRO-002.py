# EJERCICIOS DE FUNCIONES
# 227522
import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1: Precio de una vivienda
def precio_vivienda(m, A, b):
    return m * A + b

A = np.linspace(0, 200, 100)  
P = precio_vivienda(m=1500, A=A, b=20000)

plt.figure(1)
plt.plot(A, P, label="Precio de la vivienda")
plt.title("Precio de una vivienda")
plt.xlabel("Área construida (A)")
plt.ylabel("Precio (P)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 2: Ganancia mensual
def ganancia_mensual(c, N, b):
    return c * N + b

N = np.linspace(0, 500, 100)  
G = ganancia_mensual(c=50, N=N, b=1000)

plt.figure(2)
plt.plot(N, G, label="Ganancia mensual", color="orange")
plt.title("Ganancia mensual")
plt.xlabel("Número de predicciones (N)")
plt.ylabel("Ganancia (G)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 3: Tiempo total de procesamiento
def tiempo_procesamiento(k, D, c):
    return k * D + c

D = np.linspace(0, 1000, 100)  
T = tiempo_procesamiento(k=0.5, D=D, c=10)

plt.figure(3)
plt.plot(D, T, label="Tiempo de procesamiento", color="green")
plt.title("Tiempo total de procesamiento")
plt.xlabel("Tamaño de los datos (D)")
plt.ylabel("Tiempo (T)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 4: Costo total de almacenamiento
def costo_almacenamiento(p, D, f):
    return p * D + f

D = np.linspace(0, 1000, 100)
C = costo_almacenamiento(p=2, D=D, f=50)

plt.figure(4)
plt.plot(D, C, label="Costo de almacenamiento", color="red")
plt.title("Costo total de almacenamiento")
plt.xlabel("Cantidad de datos (D)")
plt.ylabel("Costo (C)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 5: Medición calibrada
def medicion_calibrada(a, R, b):
    return a * R + b

R = np.linspace(0, 100, 100)
M = medicion_calibrada(a=1.5, R=R, b=5)

plt.figure(5)
plt.plot(R, M, label="Medición calibrada", color="purple")
plt.title("Medición calibrada")
plt.xlabel("Medición en crudo (R)")
plt.ylabel("Medición calibrada (M)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 6: Tiempo de respuesta promedio
def tiempo_respuesta(m, S, b):
    return m * S + b

S = np.linspace(0, 200, 100)
T = tiempo_respuesta(m=0.8, S=S, b=2)

plt.figure(6)
plt.plot(S, T, label="Tiempo de respuesta", color="brown")
plt.title("Tiempo de respuesta promedio")
plt.xlabel("Solicitudes simultáneas (S)")
plt.ylabel("Tiempo (T)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 7: Ingresos de la plataforma
def ingresos(p, S, b):
    return p * S + b

S = np.linspace(0, 1000, 100)
I = ingresos(p=10, S=S, b=500)

plt.figure(7)
plt.plot(S, I, label="Ingresos de la plataforma", color="cyan")
plt.title("Ingresos de la plataforma")
plt.xlabel("Número de suscriptores (S)")
plt.ylabel("Ingresos (I)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 8: Energía consumida
def energia_consumida(k, O, b):
    return k * O + b

O = np.linspace(0, 500, 100) 
E = energia_consumida(k=0.2, O=O, b=10)

plt.figure(8)
plt.plot(O, E, label="Energía consumida", color="magenta")
plt.title("Energía consumida")
plt.xlabel("Número de operaciones (O)")
plt.ylabel("Energía (E)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 9: Número de likes
def likes(m, F, b):
    return m * F + b

F = np.linspace(0, 1000, 100)
L = likes(m=0.05, F=F, b=10)

plt.figure(9)
plt.plot(F, L, label="Número de likes", color="teal")
plt.title("Número de likes")
plt.xlabel("Número de seguidores (F)")
plt.ylabel("Likes (L)")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 10: Costo total de entrenamiento
def costo_entrenamiento(p, I, c):
    return p * I + c

I = np.linspace(0, 1000, 100)
C = costo_entrenamiento(p=0.1, I=I, c=50)

plt.figure(10)
plt.plot(I, C, label="Costo total de entrenamiento", color="gray")
plt.title("Costo total de entrenamiento")
plt.xlabel("Número de iteraciones (I)")
plt.ylabel("Costo (C)")
plt.legend()
plt.grid()
plt.show()
