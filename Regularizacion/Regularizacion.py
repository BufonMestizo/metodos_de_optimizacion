import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar la base de datos desde el archivo CSV
file_path = "datos_transporte_optim.csv"  # Cambia esto si el archivo está en otra ubicación
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta especificada: {file_path}")
    exit()

# Verificar si las columnas esperadas existen
if "Costo_total_dolares" not in data.columns:
    print("Error: La columna 'Costo_total_dolares' no existe en los datos.")
    exit()

# Separar las características (X) y la variable objetivo (y)
X = data.drop(columns=["Costo_total_dolares"], errors="ignore")  # Características
y = data["Costo_total_dolares"]  # Variable objetivo

# 2. Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Entrenar un modelo de Lasso para la regularización
alpha = 100  # Parámetro de regularización (ajustar según sea necesario)
lasso = Lasso(alpha=alpha, random_state=42, max_iter=10000)  # max_iter ajustado para evitar problemas de convergencia
lasso.fit(X_train, y_train)

# 4. Identificar las características seleccionadas
coef = lasso.coef_
selected_features = X.columns[coef != 0]

# 5. Evaluar el modelo
y_pred = lasso.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# 6. Imprimir los resultados
print("Regularización L1 (Navaja de Occam):")
print("Características seleccionadas por Lasso:", list(selected_features))
print("Coeficientes del modelo:", coef)
print("Error cuadrático medio (MSE):", mse)

# Opcional: Mostrar todas las características con sus coeficientes
coef_df = pd.DataFrame({"Característica": X.columns, "Coeficiente": coef})
print("\nCoeficientes de todas las características:")
print(coef_df)

# Crear un DataFrame para los coeficientes
coef_df = pd.DataFrame({"Característica": X.columns, "Coeficiente": coef})

# Ordenar por valor absoluto del coeficiente
coef_df = coef_df.sort_values(by="Coeficiente", key=abs, ascending=False)

# Configurar el tamaño y estilo de la gráfica
plt.figure(figsize=(10, 6))

# Usar hue explícito para evitar la advertencia
sns.barplot(data=coef_df, x="Coeficiente", y="Característica", dodge=False)

# Añadir etiquetas y título
plt.title("Importancia de las características tras la regularización L1", fontsize=14)
plt.xlabel("Valor del coeficiente", fontsize=12)
plt.ylabel("Características", fontsize=12)
plt.axvline(0, color="red", linestyle="--", linewidth=1)  # Línea vertical en 0 para referencia

# Mostrar la gráfica
plt.tight_layout()
plt.show()
