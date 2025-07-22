import matplotlib.pyplot as plt
import numpy as mk

# x = mk.array([1,2,3,4,5,6])
# y = mk.array([7,8,9,11,12,12])

#plt.plot(x, y , linestyle='dotted')
# plt.plot(x, y , linestyle='dashed' , color='r' , linewidth=20)
# plt.show()

# plt.plot(x , ls=':' , linewidth=20)
# plt.plot(y , ls=':' , linewidth=20)
# plt.show()

y1 = mk.array([3, 8, 1, 10])
x2 = mk.array([0, 1, 2, 3])
x1 = mk.array([0, 1, 2, 3])
y2 = mk.array([6, 2, 7, 11])

plt.plot(x1,y1,x1,y2)
plt.show()



