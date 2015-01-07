# -*- coding: utf-8 -*-
"""
23、集合的差集

已知集合A和B的元素分别用不含头结点的单链表存储，请求集合A与B的差集，并将结果保存在集合A的单链表中。例如，若集合A={5,10,20,15,25,30}，集合B={5,15,35,25}，完成计算后A={10,20,30}。
"""
def merge1(head_a, head_b):#{{{
    if head_a and head_b:
        # prepare lookup table
        pool = {}
        curr = head_a
        while curr:
            pool[curr.data] = False
            curr = curr.next
        curr = head_b
        while curr:
            if pool.has_key(curr.data):
                pool[curr.data] = True
            curr = curr.next

        # merge
        curr = head_a
        prev = None
        while curr:
            if pool[curr.data] == True:
                if prev == None:
                    head_a = curr.next
                else:
                    prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
#}}}
