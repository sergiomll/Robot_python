import os

# Ejemplo de uso de red pre-entrenada Inception v3 para
# Clasificacion binaria (perro o gato), podria ser gato si o no, o perro si o no
# Descargar imagenes: https://www.robots.ox.ac.uk/~vgg/data/pets/
# las imagenes son de distinto tamaño (se igualan antes a target_size=(256,256)
# que es el tamaño predeterminado en generador_entrenamiento.flow_from_directory("Imagenes/images/train"))

import os
from keras.preprocessing.image import ImageDataGenerator
from keras import applications
from keras.layers import Flatten, Dense
from keras.models import Sequential
from matplotlib import pyplot as plt

# Carga de datos
# Habremos descargado el conjunto de datos Oxford pets del URL https://www.robots.ox.ac.uk/~vgg/data/pets/
# y extraído las imágenes a una carpeta images. La siguiente celda organiza los archivos en dos clases (perros y gatos)
# y en dos subconjuntos (entrenamiento y test) para facilitar las tareas posteriores:

images_path = "Imagenes/images"
annotations_path = "Imagenes/annotations"

trainval = open(os.path.join(annotations_path, "trainval.txt")).readlines()
test = open(os.path.join(annotations_path, "test.txt")).readlines()

os.makedirs(os.path.join(images_path, "train", "cats"), exist_ok=True)
os.makedirs(os.path.join(images_path, "train", "dogs"), exist_ok=True)
os.makedirs(os.path.join(images_path, "test", "cats"), exist_ok=True)
os.makedirs(os.path.join(images_path, "test", "dogs"), exist_ok=True)

def classify_image(line, subset):
    basename = line.split(" ")[0]
    species = line.split(" ")[2]
    subfolder = "cats" if species == "1" else "dogs"
    oldpath = os.path.join(images_path, f"{basename}.jpg")
    newpath = os.path.join(images_path, subset, subfolder, f"{basename}.jpg")
    if os.path.isfile(oldpath):
        os.rename(oldpath, newpath)

for line in trainval:
    classify_image(line, "train")

for line in test:
    classify_image(line, "test")

generador_entrenamiento = ImageDataGenerator()
datos_entrenamiento = generador_entrenamiento.flow_from_directory("Imagenes/images/train")
generador_test = ImageDataGenerator()
datos_test = generador_test.flow_from_directory("Imagenes/images/test", class_mode=None)

# Carga del modelo
# Nuestro objetivo será crear un modelo capaz de responder a la pregunta
# "¿Corresponde esta imagen a un gato o a un perro?".
# En lugar de diseñar una nueva red neuronal desde cero, podemos cargar una red ya construida y, mejor aún,
# los parámetros optimizados para el conjunto de datos Imagenet de todo tipo de imágenes,
# de forma que nuestra red viene ya "preparada" para reconocer imágenes y no partimos de cero al entrenar.
# Esta estrategia se conoce como transfer learning.

# Importaremos la red InceptionV3 desde la biblioteca de modelos ya entrenados de Tensorflow.
# Esta red se basa en un componente llamado "bloque Inception":
# encadena varios de estos bloques para extraer información de la imagen.

inception = applications.InceptionV3(include_top=False, input_shape=(256, 256, 3), weights="imagenet")
inception.trainable = False
# for i in inception.layers:
#     i.trainable = False

# Ajustes del modelo
# En la siguiente celda añadimos a la red InceptionV3 un par de capas que nos permiten obtener
# una predicción a partir de la información que haya inferido de la imagen.

predictor = Sequential()
predictor.add(Flatten())
predictor.add(Dense(128, activation="relu"))
predictor.add(Dense(2, activation="softmax"))

modelo = Sequential()
modelo.add(inception)
modelo.add(predictor)

# modelo.add(Flatten())
# modelo.add(Dense(128, activation="relu"))
# modelo.add(Dense(2, activation="softmax"))

modelo.compile(optimizer="adam", loss="categorical_crossentropy")
modelo.summary()

# Entrenamiento
# Una vez creado el modelo que ya tiene la estructura final para responder preguntas de "sí/no",
# ajustamos sus parámetros (que inicialmente son aleatorios) al conjunto de imágenes que vamos a utilizar para entrenar:
modelo.fit(datos_entrenamiento, epochs=50)

# Predicción
# Nuestro modelo ya está listo. En la siguiente celda tomamos algunas imágenes del subconjunto de test
# (imágenes que nunca han sido vistas por la red neuronal) y comprobamos cuáles son las predicciones del modelo:
# ¿acertará todos los perros y gatos?

lote_test = next(datos_test)

probs = modelo.predict(lote_test)
import numpy as np
clase = np.argmax(probs, -1)

mostrar_imagenes = 10

for i in range(mostrar_imagenes):
    plt.imshow(lote_test[i]/255.)
    plt.axis('off')
    prediccion = "perro" if clase[i] else "gato"
    plt.title(prediccion)
    plt.show()