import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2

def main():
    # Bienvenida y selección del servicio
    st.title('Bienvenido al portal predictivo de la empresa XYZ')
    st.write('**Por favor seleccione el servicio predictivo que desea utilizar**')

    # Selección del servicio entre dos opciones
    opcion = st.radio('Seleccione el servicio:', ('Predicción del tipo de flor', 'Predicción de imagen'), index=None)

    # Redirección a la página del servicio seleccionado
    if opcion == 'Predicción del tipo de flor':
        way_to_pred = st.radio('¿Cómo desea realizar la predicción de la flor?', ('Ingresando datos manualmente', 'Subiendo un archivo CSV'), index=None)
        if way_to_pred == 'Ingresando datos manualmente':
            # Redirigir a la página de predicción de iris con datos manuales
            switch_page("pred_iris_man")
        elif way_to_pred == 'Subiendo un archivo CSV':
            # Redirigir a la página de predicción de iris con archivo CSV
            switch_page("pred_iris_csv")
    elif opcion == 'Predicción de imagen':
        # Redirigir a la página de predicción de imagen
        switch_page("pred_imagen")
    
if __name__ == "__main__":
    main()