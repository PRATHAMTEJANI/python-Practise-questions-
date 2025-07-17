from numpy import random
import numpy as mk

# x = random.rand()
# print(x)
# x = random.randint(100)
# print(x)
# x = random.randint(100 , size = 10)
# print(x)

# x = random.randint(100 , size = (10 , 3))
# print(x)

# x = random.choice([3, 5, 7, 9] , size=(3,5))
# print(x)  

# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# print(x)

arr = mk.array([1,2,3,4,5,6])
#random.shuffle(arr)
print(random.permutation(arr))
print(arr)