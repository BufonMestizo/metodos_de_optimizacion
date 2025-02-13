import optuna
import pandas as pd
import sklearn.ensemble
import sklearn.model_selection
import sklearn.svm
import optuna.visualization
from sklearn.preprocessing import LabelEncoder

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    X = df.iloc[:, :-1].values  # Todas las columnas excepto la última
    y = df.iloc[:, -1].values  # Última columna como variable objetivo
    
    # Si la variable objetivo es categórica, la convertimos a valores numéricos
    if y.dtype == 'object':
        y = LabelEncoder().fit_transform(y)
    
    return X, y

def objective(trial):
    X, y = load_data("uso_ia_data.csv")  # Usar la base de datos de uso de IA
    
    classifier = trial.suggest_categorical("classifier", ["RandomForest", "SVC"])
    
    if classifier == "RandomForest":
        n_estimators = trial.suggest_int("n_estimators", 2, 20)
        max_depth = int(trial.suggest_float("max_depth", 1, 32, log=True))
        
        clf = sklearn.ensemble.RandomForestClassifier(
            n_estimators=n_estimators, max_depth=max_depth
        )
    else:
        c = trial.suggest_float("svc_c", 1e-10, 1e10, log=True)
        
        clf = sklearn.svm.SVC(C=c, gamma="auto")
    
    return sklearn.model_selection.cross_val_score(
        clf, X, y, n_jobs=-1, cv=3
    ).mean()

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)

trial = study.best_trial

print("Accuracy: {}".format(trial.value))
print("Best hyperparameters: {}".format(trial.params))

# Graficar los resultados de la optimización
optuna.visualization.plot_optimization_history(study).show()
optuna.visualization.plot_slice(study).show()
optuna.visualization.plot_contour(study, params=["n_estimators", "max_depth"]).show()
