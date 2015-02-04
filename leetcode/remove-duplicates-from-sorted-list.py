"""
Difficulty: Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):#{{{
        if head:
            curr = head
            prev = None
            curr_v = None
            while curr:
                if curr.val == curr_v:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    curr_v = curr.val
                    prev = curr
                    curr = curr.next
        return head
#}}}
