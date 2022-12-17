from numpy import ndarray as Array
from abc import ABC, abstractmethod
from enum import Enum
from functools import partial
from typing import Callable, Dict


class AbstractDataset(ABC):
    n_samples: int # type hinting
    seed: int
    noise: float
    raw_f: Callable
    f: Callable

class DatasetBuilder:
    def __init__():
        ...
        
    """ def build(self) -> AbstractDataset:
        match self.dataset_kind:
            case ClusteringEnum.BLOBS:
                ds = BlobsDataset(
                        ClusteringEnum.BLOBS,
                        **self.params
                        )
            case ClusteringEnum.CIRCLES:
                ds = BiClusterDataset(
                        ClusteringEnum.CIRCLES,
                        **self.params
                        )
            case ClusteringEnum.MOONS:
                ds = BiClusterDataset(
                        ClusteringEnum.MOONS,
                        **self.params
                        )
        ds.init()
        return ds """