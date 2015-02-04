"""
Difficulty: Easy

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

"""
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):#{{{
        length = len(A)
        i = 0
        if length > 0:
            j = length - 1
            while i <= j:
                if A[i] == elem:
                    A[i], A[j] = A[j], A[i]
                    j -= 1
                else:
                    i += 1
        return i
#}}}
