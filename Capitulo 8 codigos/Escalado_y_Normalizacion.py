import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("ENAHO_P65_202306.csv", encoding="latin-1")

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.fillna(df.mean(numeric_only=True), inplace=True)

num_cols = df.select_dtypes(include=['number']).columns

if len(num_cols) == 0:
    print("❌ No hay columnas numéricas para escalar. Revisa el contenido del DataFrame con df.info()")
else:
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    df.to_csv("ENAHO_P65_202306_scaled.csv", index=False)
    print("✅ Escalado completado y guardado en 'ENAHO_P65_202306_scaled.csv'")
