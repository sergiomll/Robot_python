import os

# Ejemplo de uso de red pre-entrenada Inception v3 para
# Clasificacion binaria (perro o gato), podria ser gato si o no, o perro si o no
# Descargar imagenes: https://www.robots.ox.ac.uk/~vgg/data/pets/
# las imagenes son de distinto tamaño (se igualan antes a target_size=(256,256)
# que es el tamaño predeterminado en generador_entrenamiento.flow_from_directory("Imagenes/images/train"))

import os
from keras.preprocessing.image import ImageDataGenerator

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
algunas_imagenes = next(datos_test)


