from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Cargar dataset 
datos = load_wine()
X_full = datos.data
y = datos.target
feature_names = datos.feature_names

# Seleccionar 5 características para usar
features_seleccionadas = ['alcohol', 'malic_acid', 'ash', 'magnesium', 'flavanoids']
indices = [feature_names.index(feat) for feat in features_seleccionadas]
X = X_full[:, indices]

# Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Guardar el modelo
joblib.dump(modelo, 'models/modelo_vino_5vars.pkl')

# Opcional: imprimir precisión
print(f"Precisión train: {modelo.score(X_train, y_train):.3f}")
print(f"Precisión test: {modelo.score(X_test, y_test):.3f}")