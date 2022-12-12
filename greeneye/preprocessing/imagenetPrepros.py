# Import required libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os, random
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
%matplotlib inline
plt.style.use("ggplot")

class Preprocessor():

    

    def dataAugmentation(X, Y, batch_size = 32):
    # Creación de un generador de datos
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=180,
                                                                    width_shift_range=0.2,
                                                                    height_shift_range=0.2,
                                                                    shear_range=0.2,
                                                                    brightness_range=[0.1, 0.5],
                                                                    zoom_range=0.2,
                                                                    horizontal_flip=True,
                                                                    fill_mode='constant')
    return train_datagen.flow(X, Y, batch_size=32)

    def preprocess(X):  
    X_p = tf.keras.applications.mobilenet.preprocess_input(X)
    return X_p