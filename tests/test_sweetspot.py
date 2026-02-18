from sweetspot import LargerIsBetter
import numpy as np

def test_basic(): f=LargerIsBetter(0,10); assert f(5)>0
