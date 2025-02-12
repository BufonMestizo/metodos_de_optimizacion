import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import optuna

# Cargar datos desde el archivo CSV
data = pd.read_csv("house_prices.csv")

# Separar características (X) y etiquetas (y)
X = data.drop("Price", axis=1)
y = data["Price"]

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Función objetivo para Optuna
def objective(trial):
    # Seleccionar el modelo a optimizar
    model_type = trial.suggest_categorical("model", ["RandomForest", "SVR"])
    
    if model_type == "RandomForest":
        # Hiperparámetros para RandomForest
        n_estimators = trial.suggest_int("n_estimators", 10, 100)
        max_depth = trial.suggest_int("max_depth", 3, 20)
        model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    else:
        # Hiperparámetros para SVR
        c = trial.suggest_float("C", 1e-3, 1e3, log=True)
        epsilon = trial.suggest_float("epsilon", 1e-3, 1.0, log=True)
        model = SVR(C=c, epsilon=epsilon)
    
    # Entrenar el modelo
    model.fit(X_train, y_train)
    
    # Predecir en el conjunto de prueba
    y_pred = model.predict(X_test)
    
    # Retornar el error cuadrático medio (MSE)
    return mean_squared_error(y_test, y_pred)

# Crear un estudio y ejecutar la optimización
study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=50)

# Mostrar los mejores hiperparámetros
print("Mejor modelo:", study.best_params["model"])
print("Mejores hiperparámetros:", study.best_params)
