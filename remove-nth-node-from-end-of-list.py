"""
Difficulty: Easy

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):#{{{
        if head:
            curr = head
            prev = None
            tail = head
            while n > 0:
                tail = tail.next
                n -= 1
            while tail != None:
                tail = tail.next
                prev = curr
                curr = curr.next
            if curr == head:
                return head.next
            else:
                prev.next = curr.next
                curr = None
                return head
        return None
        #}}}
