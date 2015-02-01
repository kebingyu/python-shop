"""
Difficulty: Easy

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Note: del, pop(), or remove() are not allowed.

"""
class Solution:#{{{
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length > 0:
            curr_idx = 1
            curr_num = A[0]
            for _ in range(1, length):
                if A[_] != curr_num:
                    curr_num = A[_]
                    A[curr_idx] = curr_num
                    curr_idx += 1
            
            A = A[:curr_idx]
        return len(A)
#}}}
