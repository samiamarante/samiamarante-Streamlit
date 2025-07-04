import streamlit as st
import numpy as np
import joblib

# Cargar modelo
@st.cache_data
def cargar_modelo():
    return joblib.load('models/modelo_vino_5vars.pkl')

modelo = cargar_modelo()

# ======= Encabezado y bienvenida =======
st.title("🍷 Sistema de identificación de calidad del vino")
st.markdown("### Bienvenido a nuestro sistema de predicción de calidad del vino.")
st.write("Introduce las características químicas del vino para estimar su nivel de calidad.")

# Imagen decorativa 
st.image("vino.jpg", caption="¿De qué calidad será tu vino?", use_column_width=True)

# ======= Inputs del usuario =======
alcohol = st.number_input('Alcohol', 10.0, 15.0, 13.0, step=0.1)
malic_acid = st.number_input('Ácido málico', 0.5, 6.0, 2.0, step=0.1)
ash = st.number_input('Ceniza', 1.0, 3.5, 2.4, step=0.1)
magnesium = st.number_input('Magnesio', 70, 160, 100, step=1)
flavanoids = st.number_input('Flavonoides', 0.0, 5.0, 2.0, step=0.1)

# ======= Botón de predicción =======
if st.button("Predecir calidad del vino"):
    entrada = np.array([[alcohol, malic_acid, ash, magnesium, flavanoids]])
    clase = modelo.predict(entrada)[0]
    calidad = {
        0: "Alta calidad 🍷✨",
        1: "Calidad media 🍷",
        2: "Calidad baja 🍷⬇️"
    }.get(clase, "Desconocida")
    st.success(f"✅ Resultado: **{calidad}** (Clase {clase})")