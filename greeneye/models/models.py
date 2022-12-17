from typing import Protocol
from abc import abstractmethod
from numpy import ndarray as Array
from sklearn.cluster import (
        KMeans, SpectralClustering
        )
from sklearn.mixture import GaussianMixture
from enum import Enum
import imagenet.Imagenet

class GEModel(Protocol):
    labels_: Array

    @abstractmethod
    def fit(self, X: Array) -> "GEModel":
        ...

    @abstractmethod
    def predict(self, X: Array) -> Array:
        ...

class ModelBuilder:
    model: GEModel
    
    def __init__(self,):

    def build(self) -> "GEModel":
        self.model = Imagenet()
        return self

    def train(self, X: Array) -> "GEModel":
        self.model.fit(X)
        return self

    def predict(self, X: Array) -> Array: 
        if self.model_type in predict_models:
            y = self.model.predict(X)
        else:
            y = self.model.labels_
        return y



