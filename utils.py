import pickle
import streamlit as st

def check_client_id(client_id):
    # Cargar credenciales para la BBDD de la empresa y consultar si el identificador del cliente está activo 
    api_key = st.secrets["DB_USERNAME"]
    ls_ids = [123,12345,12345678]
    return True if client_id in ls_ids else False

def predict_flores(data):
    model = pickle.load(open('iris_model.pkl', "rb"))
    predictions = model.predict(data) 
    return predictions