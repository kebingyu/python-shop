# -*- coding: utf-8 -*-
"""
1、第一个只出现一次的字符

在一个字符串中找到第一个只出现一次的字符。如输入abaccdeff，则输出b。
"""
def func1(word):#{{{
    pool = {}
    length = len(word)
    for _ in range(length):
        if not pool.has_key(word[_]):
            pool[word[_]] = _
        else:
            pool[word[_]] = length
    idx = length
    char = None
    for key, value in pool.items():
        if value < idx:
            idx = value
            char = key
    return char
#}}}

import sys
word = [_ for _ in sys.argv[1]]
print func1(word)
