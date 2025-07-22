import matplotlib.pyplot as plt
import numpy as mk

x = mk.random.randint(100 , size =(100))
y = mk.random.randint(100 , size =(100))

colors = mk.random.randint(100,size=(100))
size = mk.random.randint(100 , size=(100))

plt.scatter(x,y, c=colors , s = size , alpha=1 , cmap='nipy_spectral')
plt.colorbar()
plt.show() 





