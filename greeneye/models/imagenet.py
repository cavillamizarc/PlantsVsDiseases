# Import required libraries
import tensorflow as tf
import numpy as np
import os, random

class ModelBuilder:
    def __init__(self, retrainLayers = 8):
        self.retrainLayers = retrainLayers

    def build(self) -> "ModelBuilder":
        extractor = tf.keras.applications.MobileNet(weights='imagenet', include_top=False,
                                            input_shape=(224, 224, 3))
        
        # Fixing the training layers of the model
        for layer in extractor.layers:
            layer.trainable=False

        # Global Average Pooling
        pool = tf.keras.layers.GlobalAveragePooling2D()(extractor.output)
        # Dense 32 neurons - Relu activation
        dense1 = tf.keras.layers.Dense(32, activation="relu")(pool)
        # Dropout - 0.2
        drop1 = tf.keras.layers.Dropout(0.2)(dense1)
        # Dense Clasifitacion layer (15 categories) - Softmax
        dense2 = tf.keras.layers.Dense(38, activation="softmax")(drop1)

        self.model = tf.keras.models.Model(inputs=[extractor.input], outputs=[dense2])

        return self

##########################3
 #       self.model = models[self.model_type](self.n_clusters)
 #       return self

    # wulr = Learning rate for the warm-up stage
    # lr = Learning rate for the final learning

    def train(self, X: Array, wulr = 1e-3, lr = 1e-4) -> "ModelBuilder":

        self.model.compile(loss="categorical_crossentropy", optimizer=tf.optimizers.Adam(lr=wulr),
                 metrics=["accuracy"])        
        
        # Warm-up
        #validation_data=(X_val_p, Y_val)  #TODO
        self.model.fit_generator(X, epochs=5, steps_per_epoch=X.shape[0]//32)


        # Enable last layers for training
        for layer in model.layers[-4 - self.retrainLayers:]:
            layer.trainable = True

        # Recompiling of the model for final training
        self.model.compile(loss="categorical_crossentropy", optimizer=tf.optimizers.Adam(lr=lr),
                        metrics=["accuracy"])

        model.fit(x= X, epochs=7, steps_per_epoch=X_train.shape[0]//32)

        return self

    def predict(self, X: Array) -> Array: 
        y = self.model.predict(X)
        return y
