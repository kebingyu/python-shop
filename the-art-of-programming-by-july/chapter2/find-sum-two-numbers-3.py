# -*- coding: utf-8 -*-
"""
在二元树中找出和为某一值的所有路径

输入一个整数和一棵二元树，从树的根结点开始往下访问一直到叶结点所经过的所有结点形成一条路径，然后打印出和与输入整数相等的所有路径。

例如输入整数22和如下二元树

10  
/ \
5 12
/ \
4 7

则打印出两条路径：10, 12和10, 5, 7。 其中，二元树节点的数据结构定义为：

struct BinaryTreeNode // a node in the binary tree
{
    int m_nValue; // value of node
    BinaryTreeNode *m_pLeft; // left child of node
    BinaryTreeNode *m_pRight; // right child of node
};
"""
def func1(node, expected_sum):
    if node == None:
        return

    path = [node.value]
    current_sum = node.value
    while len(path) > 0:
        is_leaf = node.left == None and node.right == None
        if current_sum == expected_sum and is_leaf:
            print path
        print
    return

def func2(node, path, expected_sum, current_sum):
    if node == None:
        return

    current_sum += node.value
    path.append(node.value)
    is_leaf = node.left == None and node.right == None
    if current_sum == expected_sum and is_leaf:
        print path
    if node.left:
        func2(node.left, path, expected_sum, current_sum)
    if node.right:
        func2(node.right, path, expected_sum, current_sum)
    # when we finish visiting a node and return to its parent node
    current_sum = current_sum - node.value
    path.pop()
