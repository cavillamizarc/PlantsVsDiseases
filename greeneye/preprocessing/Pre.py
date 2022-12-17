# Import required libraries
import tensorflow as tf
import numpy as np

class ImagenetPre():

    def dataAugmentation(X, Y, batch_size = 32):
        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=180,
                                                                        width_shift_range=0.2,
                                                                        height_shift_range=0.2,
                                                                        shear_range=0.2,
                                                                        brightness_range=[0.1, 0.5],
                                                                        zoom_range=0.2,
                                                                        horizontal_flip=True,
                                                                        fill_mode='constant')
        return train_datagen.flow(X, Y, batch_size=32)


    def imgPreprocess(path):
        img = [tf.keras.preprocessing.image.load_img(path, target_size=(224, 224, 3))]
        img = np.array(list(map(np.array, img)))

        return ImagenetPre.preprocess(img.copy())

    def preprocess(X):
        X_p = tf.keras.applications.mobilenet.preprocess_input(X)
        return X_p


    def prepAndAugment(X, Y):  
        X_p = preprocess(X)
        X_aug = dataAugmentation(X_p, Y)

        return X_aug