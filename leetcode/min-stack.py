"""
Difficulty: Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""
class MinStack:
    # @param x, an integer
    # @return an integer
    def push(self, x):#{{{
        self.pool.append(x)
        if len(self.mini) == 0 or x <= self.mini[-1]:
            self.mini.append(x)
#}}}

    # @return nothing
    def pop(self):#{{{
        if len(self.pool) > 0:
            top = self.pool.pop()
            if len(self.mini) > 0 and top == self.mini[-1]:
                self.mini.pop()
        #}}}

    # @return an integer
    def top(self):#{{{
        if len(self.pool) > 0:
            return self.pool[-1]
        else:
            return None
        #}}}

    # @return an integer
    def getMin(self):#{{{
        if len(self.mini) > 0:
            return self.mini[-1]
        else:
            return None
#}}}
        
    def __init__(self):#{{{
        self.pool = []
        self.mini = []
#}}}
