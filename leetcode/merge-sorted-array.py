"""
Difficulty: Easy

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
    You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
    The number of elements initialized in A and B are m and n respectively.
"""
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):#{{{
        for _ in range(m, m + n):
            A.insert(_, 0)

        i = m - 1
        j = n - 1
        a = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[a] = A[i]
                i -= 1
            else:
                A[a] = B[j]
                j -= 1
            a -= 1
        while j >= 0:
            A[a] = B[j]
            j -= 1
            a -= 1#}}}
