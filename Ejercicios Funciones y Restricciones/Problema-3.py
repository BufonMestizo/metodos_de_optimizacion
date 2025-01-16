import matplotlib.pyplot as plt
import numpy as np
import pulp

prob = pulp.LpProblem("Administrador_de_proyectos", pulp.LpMaximize)

x = pulp.LpVariable('x', lowBound=4, cat='Continuous')
y = pulp.LpVariable('y', lowBound=6, cat='Continuous')

# Restricciones
prob += x + y <= 12 
prob.solve()

print(f"Horas con stakeholders (x): {x.varValue}") 
print(f"Horas de documentación técnica (y): {y.varValue}")


x_vals = np.linspace(4, 12, 100)
y1 = 12 - x_vals  # Restricción x + y <= 12

plt.plot(x_vals, y1, label=r"$x + y \leq 12$")
plt.axvline(4, color='red', linestyle='--', label=r"$x \geq 4$")
plt.axhline(6, color='green', linestyle='--', label=r"$y \geq 6$")
plt.fill_between(x_vals, 6, y1, where=(x_vals >= 4) & (y1 >= 6), color="lightblue", alpha=0.5, label="Región factible")
plt.scatter(x.varValue, y.varValue, color='red', label=f"Solución óptima (x={x.varValue}, y={y.varValue})")  # Solución óptima
plt.xlim(3, 13)
plt.ylim(5, 13)
plt.xlabel("x (Reuniones con stakeholders)")
plt.ylabel("y (Trabajo en documentación)")
plt.title("Región factible - Problema 3")
plt.legend()
plt.grid()
plt.show()
