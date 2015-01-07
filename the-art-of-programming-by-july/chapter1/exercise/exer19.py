# -*- coding: utf-8 -*-
"""
19、倒数第n个元素

链表倒数第n个元素。
"""
def func1(head):#{{{
    if head:
        first = head
        second = head
        count = n
        while count > 0:
            second = second.next
        while second != None:
            first = first.next
            second = second.next
        return first
    return None
#}}}
