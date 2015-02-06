"""
Difficulty: Easy

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):#{{{
        len_i = len(a)
        len_j = len(b)
        i = len_i - 1
        j = len_j - 1
        carry = 0
        ret = ''
        while i >= 0 and j >= 0:
            sum = int(a[i]) + int(b[j]) + carry
            sum, carry = self.helper(sum, carry)
            ret = str(sum) + ret
            i -= 1
            j -= 1
            
        while i >= 0:
            sum = int(a[i]) + carry
            sum, carry = self.helper(sum, carry)
            ret = str(sum) + ret
            i -= 1
            
        while j >= 0:
            sum = int(b[j]) + carry
            sum, carry = self.helper(sum, carry)
            ret = str(sum) + ret
            j -= 1
            
        if carry > 0:
            ret = str(carry) + ret
        return ret
    
    def helper(self, sum, carry):
        if sum >= 2:
            sum = sum - 2
            carry = 1
        else:
            carry = 0
        return (sum, carry)
#}}}
