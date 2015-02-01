"""
Difficulty: Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by
level from leaf to root).

For example:
    Given binary tree {3,9,20,#,#,15,7},
3
/ \
9  20
/  \
15   7

return its bottom-up level order traversal as:
[
    [15,7],
    [9,20],
    [3]
]

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        ret = []#{{{
        if root:
            queue = [root]
            while len(queue) > 0:
                curr_len = len(queue)
                curr_list = []
                while curr_len > 0:
                    node = queue.pop(0)
                    curr_list.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    curr_len -= 1
                ret.append(curr_list)
            ret.reverse()
        return ret
#}}}
