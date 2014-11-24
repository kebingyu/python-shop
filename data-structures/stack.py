class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return ' '.join(str(_) for _ in self.stack)

    def clear(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def topEl(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()

    def push(self, data):
        self.stack.append(data)
