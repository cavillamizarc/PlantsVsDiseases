from typing import Protocol
from abc import abstractmethod
from numpy import ndarray as Array
from enum import Enum
import tensorflow as tf

class GEModel(Protocol):
    labels_: Array

    @abstractmethod
    def fit(self, X: Array) -> "GEModel":
        ...

    @abstractmethod
    def predict(self, X: Array) -> Array:
        ...

class Imagenet(GEModel):
    
    def __init__(self, retrainLayers = 8):
        self.retrainLayers = retrainLayers

    def build(self) -> "Imagenet":
        extractor = tf.keras.applications.MobileNet(weights='imagenet', include_top=False,
                                            input_shape=(224, 224, 3))

        for layer in extractor.layers:
            layer.trainable=False

        pool = tf.keras.layers.GlobalAveragePooling2D()(extractor.output)
        
        dense1 = tf.keras.layers.Dense(256, activation="relu")(pool)
        drop1 = tf.keras.layers.Dropout(0.2)(dense1)

        dense2 = tf.keras.layers.Dense(128, activation="relu")(drop1)
        drop2 = tf.keras.layers.Dropout(0.2)(dense2)

        dense3 = tf.keras.layers.Dense(64, activation="relu")(drop2)
        drop3 = tf.keras.layers.Dropout(0.2)(dense3)
        
        dense4 = tf.keras.layers.Dense(38, activation="softmax")(drop3)

        self.model = tf.keras.models.Model(inputs=[extractor.input], outputs=[dense4])

        return self

    # wulr = Learning rate for the warm-up stage
    # lr = Learning rate for the final learning

    def train(self, X: Array, wulr = 1e-3, lr = 1e-4) -> "Imagenet":

        self.model.compile(loss="categorical_crossentropy", optimizer=tf.optimizers.Adam(lr=wulr),
                 metrics=["accuracy"])        
        
        # Warm-up
        #validation_data=(X_val_p, Y_val)  #TODO
        self.model.fit_generator(X, epochs=8, steps_per_epoch=X.shape[0]//32)


        # Enable last layers for training
        for layer in self.model.layers[-8 - self.retrainLayers:]:
            layer.trainable = True

        # Recompiling of the model for final training
        self.model.compile(loss="categorical_crossentropy", optimizer=tf.optimizers.Adam(lr=lr),
                        metrics=["accuracy"])

        if(self.best_callback != None):            
            self.model.fit(x= X,
                        epochs=10,
                        steps_per_epoch=X_train.shape[0]//32,
                        callbacks=[self.best_callback])
        else:
            self.model.fit(x= X,
                        epochs=10,
                        steps_per_epoch=X_train.shape[0]//32,)
        return self

    def predict(self, X: Array) -> Array: 
        y = self.model.predict(X)
        return y

    def setCallback(path):
        self.best_callback = tf.keras.callbacks.ModelCheckpoint(path, monitor="val_loss", 
                                                   verbose=True, save_best_only=True,
                                                   save_weights_only=True, mode="min")

    def load(path):
        model.load_weights(path)
        
