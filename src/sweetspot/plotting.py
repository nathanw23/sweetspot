import matplotlib.pyplot as plt
import numpy as np

def plot_desirability(funcs,x,labels=None,title=None):
    x=np.asarray(x); labels=labels or [f.__class__.__name__ for f in funcs]
    for f,l in zip(funcs,labels): plt.plot(x,f(x),label=l)
    plt.ylim(-0.05,1.05); plt.legend();
    if title: plt.title(title)
    return plt.gca()
