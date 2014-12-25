# -*- coding: utf-8 -*-
"""
4、逆序输出链表

输入一个链表的头结点，从尾到头反过来输出每个结点的值。
"""
def rev_print(head):#{{{
    if head:
        rev_print(head.next)
        print head.data
#}}}

def rev_print2(head):#{{{
    pool = []
    while head:
        pool.append(head.data)
        head = head.next
    for _ in range(length - 1, -1, -1):
        print _
#}}}

def rev_print3(head):#{{{
    if head:
        # reverse list
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # prev is the new head
        while prev:
            print prev.data
            prev = prev.next
#}}}
