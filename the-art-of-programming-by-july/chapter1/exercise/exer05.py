# -*- coding: utf-8 -*-
"""
5、在O(1)时间内删除单链表结点

给定单链表的一个结点的指针，同时该结点不是尾结点，此外没有指向其它任何结点的指针，请在O(1)时间内删除该结点。
"""
def func(node):#{{{
    if node:
        temp = node.next
        node.data = temp.data
        node.next = temp.next
        temp = None
#}}}
