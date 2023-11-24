import streamlit as st
import pandas as pd
from utils import *
from streamlit_extras.switch_page_button import switch_page

def main():
    # Bienvenida y selección del servicio
    st.title('Bienvendo al portal predictivo de la empresa XYZ')
    st.write('**Por favor seleccione es sistema predictivo que desea usar**')
    opcion = st.radio('Seleccione la página:', ('Predicción del tipo de flor', 'Predicción de imagen'), index=None)

    # Redirigir a la págna del servicio
    if opcion=='Predicción del tipo de flor':
        way_to_pred = st.radio('¿Cómo desea realizar la predicción de la flor?:', ('Ingresando datos manualmente', 'Subiendo un archivo CSV'), index=None)
        if way_to_pred == 'Ingresando datos manualmente':
            switch_page("pred_iris_man")
        elif way_to_pred == 'Subiendo un archivo CSV':
            switch_page("pred_iris_csv")
    elif opcion=='Predicción de imagen':
        switch_page("pred_imagen")
    
if __name__ == "__main__":
    main()

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2