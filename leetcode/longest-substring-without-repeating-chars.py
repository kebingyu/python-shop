"""
Difficulty: Medium

Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution:
    # @return an integer
    # O(n)
    def lengthOfLongestSubstring(self, s):#{{{
        length = len(s)
        max_length = 0
        lastRepeatIndex = -1
        table = {}
        for i in range(length):
            if table.has_key(s[i]) and table[s[i]] > lastRepeatIndex:
                lastRepeatIndex = table[s[i]]
            if i - lastRepeatIndex > max_length:
                max_length = i - lastRepeatIndex
            table[s[i]] = i
        return max_length#}}}

    # @return an integer
    # O(n^2)
    def lengthOfLongestSubstring2(self, s):#{{{
        length = len(s)
        max_length = 0
        for i in range(length):
            table = {}
            table[s[i]] = True
            while i + 1 < length and s[i] != s[i + 1] and (not table.has_key(s[i + 1])):
                table[s[i + 1]] = True
                i += 1
            if len(table) > max_length:
                max_length = len(table)
        return max_length
#}}}
