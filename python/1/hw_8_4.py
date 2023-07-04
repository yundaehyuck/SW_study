
class Stack:

    def __init__(self):

        self.stack = []
    
    def empty(self):

        return not(self.stack)
    
    def top(self):

        try:

            return self.stack[-1]
        
        except:

            return None
    
    def pop(self):

        try:

            return self.stack.pop(-1)
        
        except:

            return None

    
    def push(self,value):

        self.stack.append(value)
    
    def __repr__(self):

        return repr(self.stack)

print('******case1******')
stack = Stack()
print(stack.empty())
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(4)
stack.pop()
stack.pop()
print(stack.top())
print(stack)

print('*******case2********')
stack = Stack()
stack.pop()
print(stack.top())
print(stack.empty())
print(stack)
