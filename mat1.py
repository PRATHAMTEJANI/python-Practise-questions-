import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()  # Just view it in a window


x = np.array([1,5 , 7, 4, 3])     #horizaontal line
y = np.array([3,8 , 4, 5 ,6])     #vertical line

#The x-points in the example above are [0, 1, 2, 3, 4, 5]. default
# plt.plot( x , y , marker= '_' ) #change symbol also * o like this called as MARKER
# plt.show()

# plt.plot(x,y,'o:g' , ms=20)     #red dotted line coloue we can change as per requirement ms = size of dot symbol
# plt.show()

plt.plot(x,y, marker = 'o', ms = 20, mfc='hotpink' , mec='hotpink')
plt.show()
