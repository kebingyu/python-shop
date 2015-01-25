"""
Difficulty: Easy

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Requirements for atoi:#{{{
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#}}}
"""
class Solution:
    # @return an integer
    def atoi(self, str):#{{{
        str = str.strip()
        length = len(str)
        if length > 0:
            if str[0] == '-':
                if length == 1 or self.isNaN(str[1]):
                    return 0
                sign = -1
                start = 1
            elif str[0] == '+':
                if length == 1 or self.isNaN(str[1]):
                    return 0
                sign = 1
                start = 1
            elif not self.isNaN(str[0]):
                sign = 1
                start = 0
            else:
                return 0
                
            number = 0
            for _ in str[start:]:
                if self.isNaN(_):
                    break
                else:
                    number = number * 10 + int(_)
                    
            if sign == 1 and number > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif sign == -1 and number > 2 ** 31:
                return -2 ** 31
            else:
                return sign * number
        return 0
                    
    def isNaN(self, char):
        if ord(char) < ord('0') or ord(char) > ord('9'):
            return True
        else:
            return False
#}}}
