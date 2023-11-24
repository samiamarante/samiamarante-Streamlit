from PIL import Image
import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model
import tensorflow as tf
print(tf.__version__)
print(np.__version__)

imagen = Image.open('iris.jpg').resize((32, 32))


# Convertir la imagen a una matriz de valores de píxeles
imagen = np.array(imagen) / 255.0

# Añadir una dimensión extra (lote)
imagen = imagen.reshape((1, 32, 32, 3))
# Cargar el modelo desde el archivo
model = load_model('models/modelo_cifar_10.h5')
# Realizar la predicción
predictions = model.predict(imagen)
predicted_class = tf.argmax(predictions[0]).numpy()
# Obtener el nombre de la clase predicha
class_names = ['avión', 'automóvil', 'pájaro', 'gato', 'ciervo', 'perro', 'rana', 'caballo', 'barco', 'camión']
print(class_names[predicted_class])