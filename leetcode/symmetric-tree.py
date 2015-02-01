"""
Difficulty: Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

1
/ \
2   2
/ \ / \
3  4 4  3
But the following is not:
1
/ \
2   2
\   \
3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):#{{{
        if root:
            return self.check(root.left, root.right)
        return True
        
        
    def check(self, n1, n2):
        if n1 == None and n2 == None:
            return True
        elif n1 == None or n2 == None:
            return False
        else:
            return n1.val == n2.val and self.check(n1.left, n2.right) and self.check(n1.right, n2.left)
#}}}
