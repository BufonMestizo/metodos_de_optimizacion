import matplotlib.pyplot as plt
import numpy as np
import pulp

prob = pulp.LpProblem("Videojuegos", pulp.LpMaximize)

P1 = pulp.LpVariable('P1', lowBound=0, cat='Continuous')
P2 = pulp.LpVariable('P2', lowBound=0, cat='Continuous')

# Restricciones
prob += 2 * P1 + 3 * P2 <= 18
prob.solve()

print(f"Modelos 3D producidos (P1): {P1.varValue}")
print(f"Texturas producidas (P2): {P2.varValue}")

P1_vals = np.linspace(0, 10, 100)
P2_vals = (18 - 2 * P1_vals) / 3  # Restricción 2P1 + 3P2 <= 18

plt.plot(P1_vals, P2_vals, label=r"$2P_1 + 3P_2 \leq 18$")
plt.fill_between(P1_vals, 0, P2_vals, where=(P2_vals >= 0), color="lightblue", alpha=0.5, label="Región factible")
plt.scatter(0, 6, color='red', label="Solución óptima (P1=0, P2=6)")
plt.xlabel("P1 (Modelos 3D)")
plt.ylabel("P2 (Texturas)")
plt.title("Región factible - Problema 4")
plt.legend()
plt.grid()
plt.show()
