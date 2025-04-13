# ==========================================
# PROYECTO: MODELO SUPERVISADO - TRANSPORTE IA
# ==========================================
# Objetivo: Clasificar rutas de transporte como Rápida, Normal o Demorada
# basado en características como duración, congestión, tipo de ruta, clima y hora.

# Paso 1: Importar librerías necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import classification_report, accuracy_score

# Paso 2: Cargar el dataset desde archivo CSV
rutas = pd.read_csv("dataset_transporte.csv")

# Paso 3: Preprocesamiento
# Codificar variables categóricas
le = LabelEncoder()
for columna in ['origen', 'destino', 'congestion', 'tipo_ruta', 'clima', 'hora_dia', 'clasificacion']:
    rutas[columna] = le.fit_transform(rutas[columna])

# Separar variables predictoras y variable objetivo
X = rutas.drop('clasificacion', axis=1)
y = rutas['clasificacion']

# Paso 4: Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Paso 5: Entrenar el modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Paso 6: Hacer predicciones
y_pred = modelo.predict(X_test)

# Paso 7: Evaluación del modelo
print("\n=== REPORTE DE CLASIFICACIÓN ===")
print(classification_report(y_test, y_pred))
print("Precisión total del modelo:", accuracy_score(y_test, y_pred))

# Paso 8: Mostrar el árbol de decisión
print("\n=== ESTRUCTURA DEL ÁRBOL DE DECISIÓN ===")
arbol = export_text(modelo, feature_names=list(X.columns))
print(arbol)

# Paso 9: Guardar predicciones y pruebas
resultados = pd.DataFrame({
    'y_real': y_test,
    'y_predicho': y_pred
})
resultados.to_csv("resultados_modelo.csv", index=False)
print("\nResultados guardados en 'resultados_modelo.csv'")
