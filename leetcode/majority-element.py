"""
Difficulty: Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):#{{{
        curr = num[0]
        count = 1
        for _ in num[1:]:
            if curr == _:
                count += 1
            else:
                count -= 1
            if count == 0:
                curr = _
                count = 1
        return curr
#}}}
