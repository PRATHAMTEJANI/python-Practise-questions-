# from random import random
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# import numpy as mk
# # sns.displot([0,1,2,3,4,5,6] , kind = "kde")
# # sns.displot([0,1,2,3,4,5,6] , kind = "hist")
# # sns.displot([0,1,2,3,4,5,6] , kind = "ecdf")
# # plt.show()

# arr = mk.array([1,2,3,4,5,6])
# mk.random.shuffle(arr)
# print(arr)

# print(mk.random.permutation(arr))
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as mk
# import numpy as random
# mk.displot([0,1,2,3,43,5,6] , kind = 'ecdf')
# plt.show()

# x = random.normal(size = (2,3))
# print(x)

# mk.displot(random.normal(size=1000) , kind = "kde")


# mk.displot(random.binomial(n = 10 , p = 0.5 , size = 1000))
# plt.show()

# data = {
#     "normal" : random.normal(loc=50 , scale = 5 , size = 1000) , 
#     "binomial" :  random.binomial(n = 100 , p = 0.5 , size = 1000)

# }

# mk.displot(data , kind = "hist")
# plt.show()

# mk.displot(random.poisson(lam = 10 , size = 1000))
# plt.show()

# data = {
#     "normal" : random.normal(loc=50 , scale = 5 , size = 1000) , 
#     "binomial" :  random.binomial(n = 100 , p = 0.5 , size = 1000) , 
#     "poisson" : random.poisson(lam = 10 , size = 1000)

# }

# mk.displot(data , kind = "hist")
# plt.show()

# a = random.uniform(size = (2,3))
# print(a)

# mk.displot(random.uniform(size = 1000) , kind = "hist")
# plt.show()

# a = random.logistic(loc = 1 , scale=2 , size = (2,3))
# print(a)

# mk.displot(random.logistic(loc = 2 , scale = 2 , size = (2,6)))
# plt.show()


# data = {
#   "normal": random.normal(scale=2, size=1000),
#   "logistic": random.logistic(size=1000)
# }

# mk.displot(data , kind = "hist")
# plt.show()

# a = random.multinomial(n = 6 , pvals = [1/6 , 1/6 , 1/6 , 1/6 , 1/6 , 1/6 ])
# print(a)

# sam = mk.random.multinomial(1000 ,  [0.25, 0.25, 0.25, 0.25], size = 1000)
# count = sam[: , 0]
# plt.show()

from numpy import random
import matplotlib.pyplot as sns
import seaborn as plt

x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])

plt.show()