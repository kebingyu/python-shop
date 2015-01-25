"""
Difficulty: Easy

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Example:

1 - 10: I, II, III, IV, V, VI, VII, VIII, IX, X

Symbol  Value
I   1
V   5
X   10
L   50
C   100
D   500
M   1,000

Symbols are placed from left to right in order of value, starting with the largest. However, in a few specific cases to avoid four characters being repeated in succession (such as IIII or XXXX) these can be reduced using subtractive
notation
"""
class Solution:
    # @return an integer
    def romanToInt(self, s):#{{{
        table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        number = 0
        length = len(s)
        if length > 0:
            for _ in range(length):
                if _ + 1 < length and table[s[_]] < table[s[_ + 1]]:
                    number += -table[s[_]]
                else:
                    number += table[s[_]]
        return number
#}}}
