import numpy as np
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction

def gauss_jordan(x, y, verbose=0, step_output=None):
    m, n = x.shape
    augmented_mat = np.zeros(shape=(m, n + 1), dtype=object)  # Usar tipo 'object' para manejar fracciones
    augmented_mat[:m, :n] = x
    augmented_mat[:, m] = y
    np.set_printoptions(precision=2, suppress=True)

    step_output.insert(tk.END, "Matriz aumentada inicial:\n")
    step_output.insert(tk.END, imprimir_matriz_como_fracciones(augmented_mat) + "\n\n")
    
    for d in range(2):
        outer_loop = [[0, m - 1, 1], [m - 1, 0, -1]]
        for i in range(outer_loop[d][0], outer_loop[d][1], outer_loop[d][2]):
            inner_loop = [[i + 1, m, 1], [i - 1, -1, -1]]
            for j in range(inner_loop[d][0], inner_loop[d][1], inner_loop[d][2]):
                k = (-1) * augmented_mat[j, i] / augmented_mat[i, i]
                temp_row = augmented_mat[i, :] * k
                augmented_mat[j, :] = augmented_mat[j, :] + temp_row
                step_output.insert(tk.END, f"Paso {i}-{j}: \n")
                step_output.insert(tk.END, imprimir_matriz_como_fracciones(augmented_mat) + "\n\n")
                step_output.insert(tk.END, "-"*50 + "\n")  # Separador para cada paso
                
    for i in range(0, m):
        augmented_mat[i, :] = augmented_mat[i, :] / augmented_mat[i, i]
        step_output.insert(tk.END, f"Normalizar fila {i}: \n")
        step_output.insert(tk.END, imprimir_matriz_como_fracciones(augmented_mat) + "\n\n")
        step_output.insert(tk.END, "-"*50 + "\n")  # Separador para cada paso de normalización
    
    return augmented_mat[:, n]

def imprimir_matriz_como_fracciones(matriz):
    """Convierte cada elemento de la matriz en una fracción y la devuelve como una cadena."""
    matriz_como_fracciones = [[str(Fraction(matriz[i, j]).limit_denominator()) for j in range(matriz.shape[1])] for i in range(matriz.shape[0])]
    return "\n".join(["\t".join(fila) for fila in matriz_como_fracciones])

def create_entries():
    global entry_matrix, entry_rhs, step_output, result_label
    try:
        rows = int(entry_rows.get())
        cols = int(entry_cols.get())
        
        if rows <= 0 or cols <= 0:
            messagebox.showerror("Error", "Las dimensiones deben ser números enteros positivos.")
            return
        
        # Limpiar cualquier entrada anterior
        for widget in frame_matrix.winfo_children():
            widget.destroy()
        for widget in frame_rhs.winfo_children():
            widget.destroy()

        # Limpiar los pasos anteriores
        step_output.delete(1.0, tk.END)  # Limpiar pasos previos en el área de salida

        # Limpiar el resultado anterior
        result_label.config(text="")  # Limpiar el resultado anterior

        # Crear nuevas entradas basadas en las dimensiones
        entry_matrix = [[tk.Entry(frame_matrix, width=5) for _ in range(cols)] for _ in range(rows)]
        entry_rhs = [tk.Entry(frame_rhs, width=5) for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                entry_matrix[i][j].grid(row=i, column=j, padx=2, pady=2)  # Reducir padding
            entry_rhs[i].grid(row=i, column=0, padx=2, pady=2)  # Reducir padding

        button_solve.grid(row=rows+1, column=1, columnspan=2, pady=5)  # Ajustado pady

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese dimensiones válidas.")

def solve_system():
    try:
        rows = int(entry_rows.get())
        cols = int(entry_cols.get())

        # Verificar si algún campo está vacío
        for i in range(rows):
            for j in range(cols):
                if not entry_matrix[i][j].get():
                    raise ValueError("La entrada de la matriz no puede estar vacía.")
        for i in range(rows):
            if not entry_rhs[i].get():
                raise ValueError("La entrada del lado derecho no puede estar vacía.")
        
        # Convertir entradas a fracciones
        coefficients = np.array([[Fraction(entry_matrix[i][j].get()) for j in range(cols)] for i in range(rows)])
        right_hand_side = np.array([Fraction(entry_rhs[i].get()) for i in range(rows)])

        # Resolver el sistema usando Gauss-Jordan y mostrar los pasos
        solution = gauss_jordan(coefficients, right_hand_side, step_output=step_output)

        # Convertir la solución a cadenas de fracciones
        solution_fractions = [str(val) for val in solution]

        # Mostrar el resultado en la etiqueta como fracciones
        result_label.config(text=f"Solución: {', '.join(solution_fractions)}")  # Convertir a cadena para mostrar

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

app = tk.Tk()
app.title("Gauss-Jordan")

# Crear entrada para dimensiones de la matriz
frame_dimensions = tk.Frame(app)
frame_dimensions.grid(row=0, column=0, columnspan=3, pady=5)  # Reducir pady

tk.Label(frame_dimensions, text="Filas:").grid(row=0, column=0, padx=5)
entry_rows = tk.Entry(frame_dimensions, width=5)
entry_rows.grid(row=0, column=1, padx=5)

tk.Label(frame_dimensions, text="Columnas:").grid(row=0, column=2, padx=5)
entry_cols = tk.Entry(frame_dimensions, width=5)
entry_cols.grid(row=0, column=3, padx=5)

tk.Button(frame_dimensions, text="Crear Matriz", command=create_entries).grid(row=0, column=4, padx=5)

# Frames para la matriz y entradas RHS
frame_matrix = tk.Frame(app)
frame_matrix.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

frame_rhs = tk.Frame(app)
frame_rhs.grid(row=1, column=3, padx=5, pady=5)

# Frame para mostrar pasos
frame_steps = tk.Frame(app)
frame_steps.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

# Crear un widget de texto más grande para los pasos (aumentamos el tamaño)
step_output = tk.Text(frame_steps, width=80, height=20)  # Aumentar tamaño para mostrar más contenido
step_output.grid(row=0, column=0, padx=5, pady=5)

# Crear una etiqueta para mostrar el resultado en la parte inferior
result_label = tk.Label(app, text="Solución: ", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=5, pady=10)

# Botón para resolver (con texto actualizado)
button_solve = tk.Button(app, text="Resolver", command=solve_system)
button_solve.grid(row=4, column=0, columnspan=3, pady=5)

app.mainloop()
