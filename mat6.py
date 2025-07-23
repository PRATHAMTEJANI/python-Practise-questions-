import matplotlib.pyplot as plt
import numpy as mk

# y = mk.array([6,3,1,2,5,6])
# x = mk.array(["A" , "B" , "C" , "D" , "E" , "F"])

# plt.bar(x,y)
# plt.show()  

# x = mk.array(["APPLES", "BANANAS"])
# y = mk.array([400, 350])

# x = mk.array(["A", "B", "C", "D"])
# y = mk.array([3, 8, 1, 10])


# #plt.bar(x,y , color="hotpink" , width=0.5) #( barh ) for making horizaotnal bar on graph
# plt.barh(x,y , color="hotpink" , height=0.5) #( barh ) for making horizaotnal bar on graph
# plt.show()

x = mk.random.normal(170 , 10 , 250)
plt.hist(x)
plt.show()
