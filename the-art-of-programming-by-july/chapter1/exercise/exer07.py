# -*- coding: utf-8 -*-
"""
7、在字符串中删除特定的字符

输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。

例如，输入”They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”。
"""
def func1(haystack, needle):#{{{
    # O(m + n)
    if needle:
        # create lookup table
        table = {}
        for _ in needle:
            table[_] = True
        # scan haystack
        for _ in range(len(haystack)):
            if table.has_key(haystack[_]):
                haystack[_] = ''
    return ''.join(haystack)
#}}}

def func2(haystack, needle):#{{{
    # sort needle
    # scan haystack, binary search in needle
    # O(m * lgn)
    pass
    #}}}

import sys
haystack = [_ for _ in sys.argv[1]]
needle = [_ for _ in sys.argv[2]]
print func1(haystack, needle)
