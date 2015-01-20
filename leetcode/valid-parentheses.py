"""
Difficulty: Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution:
    # @return a boolean
    def isValid(self, s):#{{{
        length = len(s)
        if length > 0:
            pool = []
            for _ in s:
                if _ =='(' or _ == '{' or _ == '[':
                    pool.append(_)
                elif _ == ')':
                    if len(pool) > 0 and pool[-1] == '(':
                        pool.pop()
                    else:
                        pool.append(_)
                elif _ == '}':
                    if len(pool) > 0 and pool[-1] == '{':
                        pool.pop()
                    else:
                        pool.append(_)
                else:
                    if len(pool) > 0 and pool[-1] == '[':
                        pool.pop()
                    else:
                        pool.append(_)
            if len(pool) > 0:
                return False
        return True #}}}
