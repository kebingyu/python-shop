"""
Difficulty: Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
"""
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):#{{{
        length = len(s)
        number = 0
        i = length - 1
        rank = 0
        while i >= 0:
            number += (ord(s[i]) - ord('A') + 1) * (26 ** rank)
            i -= 1
            rank += 1
        return number#}}}
