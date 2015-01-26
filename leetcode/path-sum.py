"""
Difficulty: Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

For example:
    Given the below binary tree and sum = 22,
5
/ \
4   8
/   / \
11  13  4
/  \      \
7    2      1
    
    return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):#{{{
        if root:
            temp = [(root, sum)]
            while len(temp) > 0:
                node, curr_sum = temp.pop()
                if node.val == curr_sum and node.left == None and node.right == None:
                    return True
                if node.left:
                    temp.append((node.left, curr_sum - node.val))
                if node.right:
                    temp.append((node.right, curr_sum - node.val))
        return False
#}}}
