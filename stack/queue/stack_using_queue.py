"""
225. Implement Stack using Queues
"""
class MyStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]


    def empty(self) -> int:
        if self.stack:
            return False
        else:
            return True

myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.top() # return 2
myStack.pop() # return 2
myStack.empty() # return False