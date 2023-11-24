import pickle
import streamlit as st
from keras.models import load_model
import tensorflow as tf

def predict_flores(data):
    # Cargar el modelo previamente entrenado para predecir el tipo de flor
    model = pickle.load(open('models/iris_model.pkl', "rb"))
    # Realizar la predicción con los datos proporcionados
    predictions = model.predict(data) 
    return predictions

def predict_imagen(imagen):
    # Añadir una dimensión extra (lote)
    imagen = imagen.reshape((1, 32, 32, 3))
    # Cargar el modelo desde el archivo
    model = load_model('models/modelo_cifar_10.h5')
    # Realizar la predicción
    predictions = model.predict(imagen)
    predicted_class = tf.argmax(predictions[0]).numpy()
    # Obtener el nombre de la clase predicha
    class_names = ['avión', 'automóvil', 'pájaro', 'gato', 'ciervo', 'perro', 'rana', 'caballo', 'barco', 'camión']
    return class_names[predicted_class]

def check_client_id(client_id):
    # Simulación
    # Cargar credenciales para la BBDD de la empresa y consultar si el identificador del cliente está activo 
    api_key = st.secrets["DB_USERNAME"]
    ls_ids = [123,12345,12345678]
    return True if client_id in ls_ids else False