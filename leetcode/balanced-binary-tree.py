"""
Difficulty: Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

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
    def isBalanced(self, root):#{{{
        if root:
            l_depth = self.getMaxDepth(root.left)
            r_depth = self.getMaxDepth(root.right)
            if l_depth - r_depth > 1 or l_depth - r_depth < -1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return True
        
    def getMaxDepth(self, node):
        if node == None:
            return 0
        l_depth = 1 + self.getMaxDepth(node.left)
        r_depth = 1 + self.getMaxDepth(node.right)
        return max(l_depth, r_depth)
#}}}
