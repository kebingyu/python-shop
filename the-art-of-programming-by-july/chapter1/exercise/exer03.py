# -*- coding: utf-8 -*-
"""
3、编程判断俩个链表是否相交

给出俩个单向链表的头指针，比如h1，h2，判断这俩个链表是否相交。为了简化问题，我们假设俩个链表均不带环。

also find the intersection node
"""
def isIntersect(h1, h2):#{{{
    if h1 and h2:
        # traverse L1
        while h1.next != None:
            h1 = h1.next
        # traverse L2
        while h2.next != None:
            h2 = h2.next
        if h2 == h1:
            return True
    return False
#}}}

def find(h1, h2):#{{{
    if h1 and h2:
        count = 0
        # find the length difference
        curr = h1
        while curr != None:
            curr = curr.next
            count = count + 1
        curr = h2
        while curr != None:
            curr = curr.next
            count = count - 1
        # move h1 if L1 is longer, otherwise move h2
        if count >= 0:
            while count > 0:
                h1 = h1.next
                count = count - 1
        else:
            while count < 0:
                h2 = h2.next
                count = count + 1
        # compare
        while h1 != None:
            if h1 == h2:
                return True
            else:
                h1 = h1.next
                h2 = h2.next
    return False
#}}}
