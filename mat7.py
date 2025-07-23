import matplotlib.pyplot as plt
import numpy as mk

x = mk.array([1,2,34,4,54,5])
label1 = ["a1" , "a2" ,"a3" ,"a4" ,"a5" ,"a6" ]
myexplod = [0.2 , 0 , 0, 0 , 0.4 , 0.6]
mycolors = ["black", "hotpink", "b", "#4CAF50"]


plt.pie(x , labels=label1 , startangle=0 , explode=myexplod , shadow=True , colors=mycolors)
plt.legend(title = "MAFIA WORLD")
plt.show()

#explode inmclude upper program
#shadoe inlcude