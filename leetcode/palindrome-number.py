"""
Difficulty: Easy

Determine whether an integer is a palindrome. Do this without extra space.

"""
class Solution:
    # @return a boolean
    def isPalindrome(self, x):#{{{
        if x < 0:
            return False
        x = str(x)
        i = 0
        j = len(x) - 1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True
#}}}
