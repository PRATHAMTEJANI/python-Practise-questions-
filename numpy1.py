import numpy as ml
arr = ml.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(ml.__version__)
print(ml.array(42))

arra = ml.array([[1,2,3] , [4,5,6]])

arr1 = ml.array([[[1,2,3] , [4,5,6] , [7,8,9]]])
print(arr1)

print(arr.ndim)
print(arra.ndim)
print(arr1.ndim)

arr2 = ml.array([[1,2,3] , [4,5,6]] , ndmin=5)
print(arr2)
print(arr2.dtype)

arr3 = ml.array(['apple', 'banana', 'cherry'])
print(arr3.dtype)

arr4 = ml.array(['apple', 'banana', 'cherry'] , dtype = 'S')
print(arr4)
print(arr4.dtype)

#casting in array

arr5 = ml.array([1.2 , 1.3 , 1.4 , 1.5])
array = arr5.astype(bool)#change here for see
array = arr5.astype('i')#change here for see
print(arr5)
print(array)
print(array.dtype)

ar6 = arr5.copy()
ar6[0] = 23
print(ar6)

ar6 = arr5.view()
print(ar6)
print(arr5.base)


arr = ml.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in ml.nditer(arr):
    print(x)

