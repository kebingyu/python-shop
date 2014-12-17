# -*- coding: utf-8 -*-
"""
判断一条单向链表是不是“回文”
"""

### idea#{{{
# find the middle point of the list
# reverse the second half
# scan both halves from their heads and compare
###

def findMiddle(head):#{{{
    if head == None or head.next == None:
        return head
    fast = head
    slow = head
    while fast.next != None:
        if fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        else:
            fast = fast.next
    return slow
#}}}

def reverseList(head):#{{{
    if head == None or head.next == None:
        return head
    curr = head
    prev = None
    while curr.next != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    curr.next = prev
    return curr
#}}}
#}}}
