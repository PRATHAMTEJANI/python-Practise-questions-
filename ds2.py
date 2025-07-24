# class stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self , x):
#         self.stack.append(x)
    
#     def pop(self):
#         if self.isempty():
#             return "stack is empty"
#         return self.stack.pop()
    
#     def peek(self):
#         if self.isempty():
#             return "stack is empty"
#         return self.stack[-1]
    
#     def isempty(self):
#         return len(self.stack) == 0     #length of non element having stack is zero
    
#     def size(self):
#         return len(self.stack)

# mystack = stack()

# mystack.push('A')
# mystack.push('B')
# mystack.push('C')
# mystack.push('D')
# mystack.push('E')
# mystack.push('F')

# print(mystack.stack)
# print("pop" , mystack.pop())
# print(mystack.stack)
# print(mystack.isempty())    #false
# print(mystack.size())

class node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __init__(self , value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size  += 1

    