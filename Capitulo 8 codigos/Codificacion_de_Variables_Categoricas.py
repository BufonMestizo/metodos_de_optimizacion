import pandas as pd

df = pd.read_csv("ENAHO_P65_202306.csv", encoding="latin-1")


df.fillna(df.mean(numeric_only=True), inplace=True)

categorical_cols = df.select_dtypes(include=['object']).columns
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

df.to_csv("ENAHO_P65_202306_clean.csv", index=False)

print("Preprocesamiento completado y guardado en 'ENAHO_P65_202306_clean.csv'")
