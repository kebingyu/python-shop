"""
Difficulty: Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

"""
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):#{{{
        len = 0
        last = 0
        for char in s:
            if char != ' ':
                len += 1
            else:
                if len > 0:
                    last = len
                len = 0
        if len > 0:
            return len
        else:
            return last
#}}}
