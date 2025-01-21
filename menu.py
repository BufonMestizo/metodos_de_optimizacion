import streamlit as st
import numpy as np

def solve_by_substitution(a, b):
    try:
        steps = []
        result = np.linalg.solve(a, b)
        steps.append(f"Sistema reducido a ecuaciones independientes:")
        for i, eq in enumerate(result):
            steps.append(f"x[{i + 1}] = {eq}")
        return result, "\n".join(steps)
    except Exception as e:
        return None, f"Error: {e}"

def solve_by_gauss_jordan(a, b):
    try:
        steps = []
        aug_matrix = np.hstack((a, b.reshape(-1, 1)))
        rows, cols = aug_matrix.shape

        for i in range(rows):
            pivot = aug_matrix[i][i]
            aug_matrix[i] = aug_matrix[i] / pivot
            steps.append(f"Dividiendo la fila {i + 1} entre el pivote {pivot}:")
            steps.append(aug_matrix.copy())

            for j in range(rows):
                if i != j:
                    factor = aug_matrix[j][i]
                    aug_matrix[j] = aug_matrix[j] - factor * aug_matrix[i]
                    steps.append(f"Restando {factor} * fila {i + 1} a fila {j + 1}:")
                    steps.append(aug_matrix.copy())

        solution = aug_matrix[:, -1]
        steps.append(f"Solución final: {solution}")
        return solution, "\n".join(map(str, steps))
    except Exception as e:
        return None, f"Error: {e}"

def solve_by_cramers_rule(a, b):
    try:
        steps = []
        det_a = np.linalg.det(a)
        if det_a == 0:
            return None, "No solution (determinant is zero)."
        steps.append(f"Determinante de A: {det_a}")

        solutions = []
        for i in range(len(b)):
            modified_matrix = np.copy(a)
            modified_matrix[:, i] = b
            det_modified = np.linalg.det(modified_matrix)
            steps.append(f"Reemplazando la columna {i + 1} por el vector b:")
            steps.append(modified_matrix.copy())
            steps.append(f"Determinante del nuevo sistema: {det_modified}")
            solutions.append(det_modified / det_a)

        steps.append(f"Solución final: {solutions}")
        return np.array(solutions), "\n".join(map(str, steps))
    except Exception as e:
        return None, f"Error: {e}"

st.title("Solución de Sistemas de Ecuaciones")

menu = ["Sustitución", "Gauss-Jordan", "Regla de Cramer"]
choice = st.sidebar.selectbox("Selecciona el método para resolver", menu)

st.write("Proporciona el sistema de ecuaciones en forma de matriz (A) y vector (b):")
n = st.number_input("Número de ecuaciones (n):", min_value=2, step=1, value=2)

st.write("Ingresa los valores de la matriz A:")
matriz_a = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        matriz_a[i][j] = st.number_input(f"A[{i + 1}][{j + 1}]:", value=0.0)

st.write("Ingresa los valores del vector b:")
vector_b = np.zeros(n)
for i in range(n):
    vector_b[i] = st.number_input(f"b[{i + 1}]:", value=0.0)

if st.button("Resolver"):
    if choice == "Sustitución":
        resultado, pasos = solve_by_substitution(matriz_a, vector_b)
    elif choice == "Gauss-Jordan":
        resultado, pasos = solve_by_gauss_jordan(matriz_a, vector_b)
    elif choice == "Regla de Cramer":
        resultado, pasos = solve_by_cramers_rule(matriz_a, vector_b)

    st.write("Resultado:", resultado)
    st.write("Procedimiento:")
    st.text(pasos)
