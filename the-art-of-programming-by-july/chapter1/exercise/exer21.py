# -*- coding: utf-8 -*-
"""
21、最长连续字符

用递归算法写一个函数，求字符串最长连续字符的长度，比如aaaabbcc的长度为4，aabb的长度为2，ab的长度为1。
"""
def func1(word):#{{{
    length = len(word)
    if length:
        curr_char = None
        max_length = 1
        curr_length = 1
        for _ in word:
            if curr_char == None:
                curr_char = _
            elif curr_char == _:
                curr_length = curr_length + 1
            else:
                curr_char = _
                if curr_length > max_length:
                    max_length = curr_length
                curr_length = 1
        return max(max_length, curr_length)
    return 0
#}}}

def func2(word):#{{{
    length = len(word)
    if length < 2:
        return length
    if word[0] == word[1]:
        return 1 + func2(word[1:])
    return func2(word[1:])
#}}}

import sys
word = [_ for _ in sys.argv[1]]
print func1(word)
print func2(word)
