"""
Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.

"""
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):#{{{
        length = len(strs)
        if length == 0:
            return ''
        elif length == 1:
            return strs[0]
        else:
            temp = self.getCommonPrefix(strs[0], strs[1])
            for _ in strs[2:]:
                temp = self.getCommonPrefix(temp, _)
            return temp
        
    def getCommonPrefix(self, str1, str2):
        i = 0
        j = 0
        common = ''
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                common += str1[i]
                i += 1
                j += 1
            else:
                break
        return common
 #}}}
