"""
Difficulty: Medium

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):#{{{
        curr1 = l1
        curr2 = l2
        temp = ListNode(0)
        carry = 0
        curr_sum = temp
        while curr1 and curr2:
            s = (curr1.val + curr2.val + carry) % 10
            carry = (curr1.val + curr2.val + carry) / 10
            curr_sum.next = ListNode(s)
            curr_sum = curr_sum.next
            curr1 = curr1.next
            curr2 = curr2.next
            
        while curr1:
            s = (curr1.val + carry) % 10
            carry = (curr1.val + carry) / 10
            curr_sum.next = ListNode(s)
            curr_sum = curr_sum.next
            curr1 = curr1.next
            
        while curr2:
            s = (curr2.val + carry) % 10
            carry = (curr2.val + carry) / 10
            curr_sum.next = ListNode(s)
            curr_sum = curr_sum.next
            curr2 = curr2.next
        
        if carry == 1:
            curr_sum.next = ListNode(1)
        
        return temp.next
#}}}
