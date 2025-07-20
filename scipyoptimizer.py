from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)

var = root(eqn , 0)
print(var.x)