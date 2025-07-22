import matplotlib.pyplot as plt
import numpy as mk

#plot-1
x = mk.array([1,2,3,4,5,6,7])
y = mk.array([4,5,6,7,8,9,6])
plt.subplot(2,1,1)
plt.plot(x,y,linewidth=10 , color='r')
plt.grid()


#plot-2
x = mk.array([1,2,3,4,5,6,7])
y = mk.array([8,7,6,6,5,5,4])
plt.subplot(2,1,2)

plt.plot(x,y)


plt.tight_layout()
plt.show()
x = mk.array([0, 1, 2, 3])
y = mk.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = mk.array([0, 1, 2, 3])
y = mk.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = mk.array([0, 1, 2, 3])
y = mk.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = mk.array([0, 1, 2, 3])
y = mk.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = mk.array([0, 1, 2, 3])
y = mk.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = mk.array([0, 1, 2, 3])
y = mk.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.suptitle("MAFIA WORLD")
plt.scatter(x,y)
plt.show()

