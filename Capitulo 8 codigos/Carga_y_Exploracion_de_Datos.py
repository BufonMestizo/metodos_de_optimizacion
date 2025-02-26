import pandas as pd

df = pd.read_csv("ENAHO_P65_202306.csv", encoding="latin-1")

print(df.info())

print(df.head())

print(df.describe())

# Rellenar valores numéricos faltantes con la mediana
for col in df.select_dtypes(include=['number']).columns:
    df[col].fillna(df[col].median(), inplace=True)

# Rellenar valores categóricos faltantes con la moda
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)
