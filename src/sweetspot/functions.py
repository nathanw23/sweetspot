import numpy as np
from .base import Desirability
class LargerIsBetter(Desirability):
    def __init__(self,y_min,y_max,s=1): self.y_min=y_min; self.y_max=y_max; self.s=s
    def __call__(self,x): d=(np.asarray(x)-self.y_min)/(self.y_max-self.y_min);return self.clip(d**self.s)
class SmallerIsBetter(Desirability):
    def __init__(self,y_min,y_max,s=1): self.y_min=y_min; self.y_max=y_max; self.s=s
    def __call__(self,x): d=(self.y_max-np.asarray(x))/(self.y_max-self.y_min);return self.clip(d**self.s)
class TargetIsBest(Desirability):
    def __init__(self,target,k=0.3): self.target=target; self.k=k
    def __call__(self,x): return self.clip(np.exp(-self.k*np.abs(np.asarray(x)-self.target)))
class RangeIsBest(Desirability):
    def __init__(self,lo,hi): self.lo=lo; self.hi=hi
    def __call__(self,x): x=np.asarray(x); return self.clip((x>=self.lo)&(x<=self.hi))
