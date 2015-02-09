"""
Difficulty: Medium

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):#{{{
        table = {}
        for _ in A:
            if table.has_key(_):
                table.pop(_)
            else:
                table[_] = True
        keys = table.keys()
        return keys[0]

    def singleNumber(self, A):
        left = A[0]
        for _ in A[1:]:
            left = left ^ _
        return left
#}}}
