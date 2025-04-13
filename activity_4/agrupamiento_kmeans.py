
# ==============================================
# PROYECTO: AGRUPAMIENTO DE RUTAS (KMEANS)
# Actividad 4 - Inteligencia Artificial (No Supervisado)
# ==============================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Paso 1: Cargar el dataset
df = pd.read_csv("dataset_transporte_no_supervisado.csv")

# Paso 2: Codificar variables categóricas
le = LabelEncoder()
for col in ['origen', 'destino', 'congestion', 'tipo_ruta', 'clima', 'hora_dia']:
    df[col] = le.fit_transform(df[col])

# Paso 3: Aplicar KMeans
X = df.copy()
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X)

# Paso 4: Reducción a 2 dimensiones para graficar
pca = PCA(n_components=2)
componentes = pca.fit_transform(X)
df['PCA1'] = componentes[:, 0]
df['PCA2'] = componentes[:, 1]

# Paso 5: Graficar clusters
plt.figure(figsize=(8, 6))
for cluster in df['cluster'].unique():
    subset = df[df['cluster'] == cluster]
    plt.scatter(subset['PCA1'], subset['PCA2'], label=f'Cluster {cluster}')
plt.title("Agrupamiento de rutas de transporte (KMeans + PCA)")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.legend()
plt.grid(True)
plt.savefig("cluster_rutas.png")
plt.show()

# Paso 6: Guardar resultados
df.to_csv("rutas_agrupadas.csv", index=False)
print("✅ Archivo 'rutas_agrupadas.csv' generado correctamente.")
