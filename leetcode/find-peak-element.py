"""
Difficulty: Medium

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):#{{{
        length = len(num)
        if length > 0:
            prev = float('-inf')
            for _ in range(length):
                if _ == length - 1:
                    next = float('-inf')
                else:
                    next = num[_ + 1]
                curr = num[_]
                if curr > prev and curr > next:
                    return _
                else:
                    prev = curr
#}}}
