"""
Difficulty: Medium

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):#{{{
        self.pool = []
        temp = []
        while len(temp) > 0 or root != None:
            if root:
                temp.append(root)
                root = root.left
            else:
                root = temp.pop()
                self.pool.append(root.val)
                root = root.right#}}}
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):#{{{
        return len(self.pool) > 0#}}}

    # @return an integer, the next smallest number
    def next(self):#{{{
        if self.hasNext():
            return self.pool.pop(0)#}}}
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

