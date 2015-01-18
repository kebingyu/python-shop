# -*- coding: utf-8 -*-
"""
求有根树的任意两个节点的最近公共祖先
"""

"""
binary search tree
"""
def func1(root, node1, node2):#{{{
    if root and node1 and node2:
        while root:
            if node1.value > root.value and node2.value > root.value:
                root = root.right
            elif node1.value < root.value and node2.value < root.value:
                root = root.left
            else:
                return root
    return None
#}}}

"""
regular binary tree
"""
def func2(root, node1, node2):#{{{
    if root == None:
        return None
    if root == node1 or root == node2:
        return root

    left = func2(root.left, node1, node2)
    right = func2(root.right, node1, node2)

    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
    else:
        return None
#}}}

