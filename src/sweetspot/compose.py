import numpy as np
from dataclasses import dataclass
from .base import Desirability

def geometric_mean(*ds):
    arr=[np.asarray(d) for d in ds]; prod=np.ones_like(arr[0]);
    for d in arr: prod*=d
    return prod**(1/len(arr))

@dataclass
class MultiObjectiveDesirability:
    mapping: dict
    aggregator: callable = geometric_mean
    def __call__(self,**kwargs):
        vals=[self.mapping[k](kwargs[k]) for k in self.mapping]
        return self.aggregator(*vals)
