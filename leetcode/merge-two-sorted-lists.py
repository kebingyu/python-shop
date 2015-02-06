"""
Difficulty: Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):#{{{
        head = ListNode(-1)
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                temp = l1.next
                l1.next = None
                curr.next = l1
                curr = curr.next
                l1 = temp
            else:
                temp = l2.next
                l2.next = None
                curr.next = l2
                curr = curr.next
                l2 = temp
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return head.next
#}}}
