"""
Difficulty: Medium

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

1
/ \
2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

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
    def sumNumbers(self, root):#{{{
        self.total = 0
        if root:
            self.helper(root, [])
        return self.total
            
    def helper(self, node, numbers):
        numbers.append(int(node.val))
        if node.left:
            self.helper(node.left, numbers[:]) # need to make a copy
        if node.right:
            self.helper(node.right, numbers[:]) # need to make a copy
        if (not node.left) and (not node.right):
            temp = 0
            for _ in numbers:
                temp = temp * 10 + _
            self.total += temp
#}}}
