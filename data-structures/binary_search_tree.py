from stack import Stack
from queue import Queue

class BSTNode:#{{{
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
#}}}

class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        self.traversal(self.bft)
        return ''

    """
    Call different tree traversal methods
    """
    def traversal(self, func):
        func()

    def clear(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def insert(self, data):#{{{
        node = BSTNode(data)
        if self.isEmpty():
            self.root = node
        else:
            curr = self.root
            while curr:
                if data < curr.data:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        break
                elif data > curr.data:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        break
#}}}

    """
    Bulk insert a list of data
    """
    def bulkInsert(self, dataList):#{{{
        for _ in dataList:
            self.insert(_)
#}}}

    def search(self, data):#{{{
        if not self.isEmpty():
            curr = self.root
            while curr:
                if data == curr.data:
                    return True
                elif data < curr.data:
                    curr = curr.left
                else:
                    curr = curr.right
        return False
#}}}

    def bft(self):#{{{
        if not self.isEmpty():
            pool = Queue()
            pool.enqueue(self.root)
            while not pool.isEmpty():
                curr = pool.dequeue()
                print curr
                if curr.left:
                    pool.enqueue(curr.left)
                if curr.right:
                    pool.enqueue(curr.right)
#}}}

    def inorder_nonrecursive(self):#{{{
        if not self.isEmpty():
            pool = Stack()
            curr = self.root
            while not pool.isEmpty():
                if curr.left:
                    pool.push(curr)
                    curr = curr.left
                else:
                    print curr
                    if curr.right:
                        curr = curr.right
                    else:
                        curr = pool.top()
                    #}}}

    def inorder_recursive(self):
        if not self.isEmpty():
            self.inorder(self.root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print node
            self.inorder(node.right)

    def preorder_nonrecursive(self):#{{{
        pass
#}}}

    def preorder_recursive(self):
        if not self.isEmpty():
            self.preorder(self.root)

    def preorder(self, node):
        if node:
            print node
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder_nonrecursive(self):#{{{
        pass
#}}}

    def postorder_recursive(self):
        if not self.isEmpty():
            self.postorder(self.root)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print node
