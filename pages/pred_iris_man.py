import streamlit as st
from utils import predict_flores
import pandas as pd

st.write('**Ingresa los datos manualmente para realizar la predicción de la flor:**')

input_data = {}
columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

for col in columns:
    input_data[col] = st.number_input(col, value=0.0)

if st.button('Realizar Predicción'):
    predicted_value = predict_flores(pd.DataFrame(input_data))
    st.write('El resultado de la predicción es:', predicted_value)