"""
Difficulty: Easy

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

"""
class Solution:
    # @return an integer
    def reverse(self, x):#{{{
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
            
        ret = 0
        while x >= 10:
            mod = x % 10
            x = x / 10
            ret = ret * 10 + mod
        ret = ret * 10 + x
        if sign == 1 and ret > 2 ** 31 - 1:
            return 0
        elif sign == -1 and ret > 2 ** 31:
            return 0
        else:
            return sign * ret
#}}}
