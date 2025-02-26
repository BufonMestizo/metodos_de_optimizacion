import pandas as pd

df = pd.read_csv("ENAHO_P65_202306.csv", encoding="latin-1")  

for col in df.select_dtypes(include=['number']).columns:
    if df[col].isnull().sum() > 0:  # Solo si hay valores nulos
        df[col].fillna(df[col].median(), inplace=True)

for col in df.select_dtypes(include=['object']).columns:
    if df[col].isnull().sum() > 0:  # Solo si hay valores nulos
        df[col].fillna(df[col].mode()[0], inplace=True)

print(df.isnull().sum())


