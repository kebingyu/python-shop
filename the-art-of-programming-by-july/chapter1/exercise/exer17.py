# -*- coding: utf-8 -*-
"""
17、字符串的移动

字符串为*号和26个字母的任意组合，把 *号都移动到最左侧，把字母移到最右侧并保持相对顺序不变，要求时间和空间复杂度最小。
"""
def func1(word):#{{{
    ret = ''
    length = len(word)
    if length > 0:
        star_sum = 0
        for _ in range(length):
            if word[_] == '*':
                star_sum = star_sum + 1
        temp = ['*'] * star_sum
        for _ in range(length):
            if word[_] != '*':
                temp.append(word[_])
        ret = ''.join(temp)
    return ret
#}}}

import sys
word = sys.argv[1]
print func1(word)
