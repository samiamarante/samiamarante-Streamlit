import streamlit as st
import pandas as pd
from utils import predict_flores

st.title('Predicción de flores en archivo CSV')
uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=['csv'])
if uploaded_file is not None:              
    df = pd.read_csv(uploaded_file)
    st.write('**Vista Previa del DataFrame:**')
    st.write(df.head())
    st.subheader('Realizar la predicción')
    st.write('**Selecciona las columnas para la predicción:**')
    feature_cols = st.multiselect('Selecciona las características', df.columns)
    if st.button('Realizar Predicción con CSV'):
        predicted_values = predict_flores(df[feature_cols])
        st.write('Los resultados de la predicción son:')
        st.write(predicted_values)