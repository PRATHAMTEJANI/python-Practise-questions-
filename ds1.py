# x = []
# y = [1,2,3,45,5,6]
# z = [1 , "hello" , 3.14 , True]
# print(x)
# print(y)
# print(z)
# x.append(33)
# x.append(28)
# x.append(35)
# x.append(36)
# x.sort()
# print(x)

# arr  = [2,7,4,9,3,6 ,1]
# minval = arr[0]

# for i in arr:
#     if i < minval:
#         minval = i
# print('lowest value ' , minval)

stack = []
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('C')
stack.append('C')
stack.append('C')
print("stack 1:- " , stack)


topelement = stack[-1]
print("peek" , stack)


popelemt = stack.pop()
print("pop" , popelemt)

print(stack)

isempty =  not bool(stack)
print(isempty)

print(len(stack))