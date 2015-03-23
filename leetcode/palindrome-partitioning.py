"""
Difficulty: Medium

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
["aa","b"],
["a","a","b"]
]

"""
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):#{{{
        length = len(s)
        result = []
        if length == 0:
            return result
        output = []
        self.helper(s, 0, output, result)
        return result
        
    def helper(self, str, start, output, result):
        if start == len(str):
            result.append(output[:])
            return
        
        for i in range(start, len(str)):
            if self.isPalindrome(str[start:i + 1]):
                output.append(str[start:i + 1])
                self.helper(str, i + 1, output, result)
                output.pop()
        
    def isPalindrome(self, str):
        length = len(str)
        if length > 0:
            i = 0
            j = length - 1
            while i < j:
                if str[i] == str[j]:
                    i += 1
                    j -= 1
                else:
                    return False
        return True#}}}

    # Time limit exceeded
    def partition(self, s):#{{{
        length = len(s)
        if length == 0:
            return []
        return self.helper(s)
        
    def helper(self, str):
        if len(str) == 1:
            return [[str]]
        else:
            temp = self.helper(str[1:])
            result = []
            for _ in temp:
                i = 0
                while i < len(_):
                    curr_str = str[0]
                    for j in range(0, i + 1):
                        curr_str += _[j]
                    if self.isPalindrome(curr_str):
                        _copy = _[i + 1:]
                        _copy.insert(0, curr_str)
                        result.append(_copy)
                    i += 1
                _.insert(0, str[0])
                result.append(_)
            import itertools
            result.sort()
            return list(result for result,_r in itertools.groupby(result))
        
    def isPalindrome(self, str):
        length = len(str)
        if length > 0:
            i = 0
            j = length - 1
            while i < j:
                if str[i] == str[j]:
                    i += 1
                    j -= 1
                else:
                    return False
        return True
#}}}
