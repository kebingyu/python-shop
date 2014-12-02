"""
Implement max heap as a list
"""
class MaxHeap(object):
    def __init__(self):
        self.pool = []

    def __str__(self):
        print self.pool
        return ''

    def isEmpty(self):
        return len(self.pool) == 0

    """
    Swap two elements marked by index child and parent
    """
    def swap(self, child, parent):
        self.pool[child], self.pool[parent] \
                = self.pool[parent], self.pool[child]

    def getParentIndex(self, idx):
        if idx > 0:
            return (idx - 1) / 2
        else:
            return 0

    def getLeftChildIndex(self, idx):
        child = 2 * idx + 1
        if child < len(self.pool):
            return child
        else:
            return -1

    def getRightChildIndex(self, idx):
        child = 2 * idx + 2
        if child < len(self.pool):
            return child
        else:
            return -1

    def isLeaf(self, idx):
        return self.getLeftChildIndex(idx) == -1 \
                and self.getRightChildIndex(idx) == -1

    def enqueue(self, data):
        self.pool.append(data)
        child = len(self.pool) - 1 # Index of the new added element
        # Move up
        while child != 0 \
                and self.pool[child] > self.pool[self.getParentIndex(child)]:
            parent = self.getParentIndex(child)
            self.swap(child, parent)
            child = parent

    def bulkEnqueue(self, dataList):
        for _ in dataList:
            self.enqueue(_)

    def dequeue(self):
        if not self.isEmpty():
            ret = self.pool[0]
            numElem = len(self.pool)
            if numElem > 1:
                self.pool[0] = self.pool[numElem - 1]
                self.pool.pop()
                idx = 0
                while not self.isLeaf(idx):
                    left = self.getLeftChildIndex(idx)
                    right = self.getRightChildIndex(idx)
                    leftData = None
                    rightData = None
                    moveDown = False
                    if left != -1 and self.pool[idx] < self.pool[left]:
                        moveDown = True
                        leftData = self.pool[left]
                    if right != -1 and self.pool[idx] < self.pool[right]:
                        moveDown = True
                        rightData = self.pool[right]
                    if moveDown == True:
                        # Find the index of larger child
                        if leftData and rightData:
                            if leftData > rightData:
                                larger = left
                            else:
                                larger = right
                        elif leftData:
                            larger = left
                        else:
                            larger = right
                        self.swap(larger, idx)
                        idx = larger
                    else:
                        break
            else:
                self.pool.pop()
            return ret
        else:
            return None

