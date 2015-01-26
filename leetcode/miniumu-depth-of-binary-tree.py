"""
Difficulty: Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):#{{{
        depth = 0
        if root:
            depth = self.getMinDepth(root, depth)
        return depth
            
    def getMinDepth(self, node, depth):
        if node.left == None and node.right == None:
            return depth + 1
            
        left_depth = float('inf')
        right_depth = float('inf')
        if node.left:
            left_depth = self.getMinDepth(node.left, depth + 1)
        if node.right:
            right_depth = self.getMinDepth(node.right, depth + 1)
        return min(left_depth, right_depth)
#}}}
