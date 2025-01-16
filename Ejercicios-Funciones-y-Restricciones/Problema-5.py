import matplotlib.pyplot as plt
import numpy as np
import pulp

prob = pulp.LpProblem("Hardware", pulp.LpMaximize)

A = pulp.LpVariable('A', lowBound=0, cat='Continuous')
B = pulp.LpVariable('B', lowBound=0, cat='Continuous')

# Restricciones
prob += 5 * A + 10 * B <= 50
prob.solve()

print(f"Dispositivos tipo A ensamblados (A): {A.varValue}") 
print(f"Dispositivos tipo B ensamblados (B): {B.varValue}")


A_vals = np.linspace(0, 10, 100)
B_vals = (50 - 5 * A_vals) / 10  # Restricción 5A + 10B <= 50

plt.plot(A_vals, B_vals, label=r"$5A + 10B \leq 50$")
plt.fill_between(A_vals, 0, B_vals, where=(B_vals >= 0), color="lightblue", alpha=0.5, label="Región factible")
plt.scatter(10, 0, color='red', label="Solución óptima (A=10, B=0)")
plt.ylabel("B (Tipo B)")
plt.xlabel("A (Tipo A)")
plt.title("Región factible - Problema 5")
plt.legend()
plt.grid()
plt.show()
