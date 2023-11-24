import streamlit as st
import pandas as pd
import pickle
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)','petal width (cm)']
def main():
    option = st.radio('Selecciona una opción:', ('Ingresar Datos', 'Usar Datos del CSV'))

    if option == 'Ingresar Datos':
        st.write('**Ingresa los datos para realizar la predicción:**')
        
        # Aquí puedes solicitar los datos para la predicción
        # Por ejemplo, si estás prediciendo con un modelo de regresión lineal:
        input_data = {}
        input_data['sepal length (cm)'] = [st.number_input('sepal length (cm)', value=0.0)]
        input_data['sepal width (cm)'] = [st.number_input('sepal width (cm)', value=0.0)]
        input_data['petal length (cm)'] = [st.number_input('petal length (cm)', value=0.0)]
        input_data['petal width (cm)'] = [st.number_input('petal width (cm)', value=0.0)]
        # Continúa con todas las características necesarias para la predicción
        
        if st.button('Realizar Predicción'):
            # Realiza la predicción con los datos ingresados
            predicted_value = make_prediction(pd.DataFrame(input_data))
            st.write('El resultado de la predicción es:', predicted_value)

    elif option == 'Usar Datos del CSV':
        st.title('Predicción con Archivo CSV')
        # Widget para subir archivos CSV
        uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=['csv'])
        if uploaded_file is not None:              
            # Lee el archivo CSV como un DataFrame
            df = pd.read_csv(uploaded_file)
            st.write('**Vista Previa del DataFrame:**')
            # Muestra el DataFrame
            st.write(df)
            st.subheader('Realizar Predicción')
            st.write('**Selecciona las columnas para la predicción:**')
            # Aquí el usuario elige qué columnas usar para la predicción
            # Por ejemplo, si se tienen columnas 'Feature_1', 'Feature_2', 'Target':
            feature_cols = st.multiselect('Selecciona las características', df.columns)
        if st.button('Realizar Predicción con CSV'):
            # Realiza la predicción con los datos del CSV seleccionados
            predicted_values = make_prediction(df[feature_cols])
            st.write('Los resultados de la predicción son:')
            st.write(predicted_values)

def make_prediction(data):
    # Aquí va tu lógica para realizar la predicción
    # Esto puede variar según el modelo que estés utilizando
    
    # Ejemplo con regresión lineal
    try:
        model = pickle.load(open('iris_model.pkl', "rb"))
    except Exception as e:
        st.write(e)
    else:
        predictions = model.predict(data)  # Realiza la predicción
        return predictions

if __name__ == "__main__":
    main()
