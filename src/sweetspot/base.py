from abc import ABC, abstractmethod
import numpy as np
class Desirability(ABC):
    @abstractmethod
    def __call__(self,x):...
    def clip(self,y): return np.clip(y,0,1)
