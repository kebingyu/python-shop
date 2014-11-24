class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join(str(_) for _ in self.queue)

    def clear(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None

    def topEl(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return None
