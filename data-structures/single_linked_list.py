"""
single linked list 
"""

class SLLNode:
    def __init__(self, data, ptr):
        self.data = data
        self.next = ptr

    def __str__(self):
        return str(self.data)

class SLLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        ret = ''
        if not self.isEmpty():
            ptr = self.head
            while ptr != None:
                ret = ret + str(ptr) + ' '
                ptr = ptr.next
        return ret

    def isEmpty(self):
        return self.head == None

    def addToHead(self, data):
        self.head = SLLNode(data, self.head)
        if self.tail == None:
            self.tail = self.head
        return self

    def addToTail(self, data):
        node = SLLNode(data, None)
        if self.tail != None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        return self

    def deleteFromHead(self):
        if not self.isEmpty():
            temp = self.head
            self.head = temp.next
            temp.next = None
        return self

    def deleteFromTail(self):
        if not self.isEmpty():
            ptr = self.head
            while ptr.next != None:
                prev = ptr
                ptr = ptr.next
            prev.next = None
            self.tail = prev
        return self

    def deleteNode(self, data):
        if not self.isEmpty():
            ptr = self.head
            if ptr.data == data:
                self.deleteFromHead()
            prev = ptr
            ptr = ptr.next
            while ptr != None:
                if ptr.data == data:
                    prev.next = ptr.next
                    ptr.next = None
                    ptr = prev.next
                else:
                    prev = prev.next
                    ptr = ptr.next
            if prev.data == data:
                self.deleteFromTail()
        return self

    def isInList(self, data):
        ptr = self.head
        while ptr != None:
            if ptr.data == data:
                return True
            ptr = ptr.next
        return False

    def reverseList(self):
        if self.head == None or self.head.next == None:
            return self.head
        curr = self.head
        prev = None
        while curr.next != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr

"""
example 
"""

list = SLLList()
list.addToHead(1).addToTail(2).addToHead(3).addToHead(4).addToTail(5)
print list
node = list.reverseList()
while node != None:
    print node
    node = node.next
