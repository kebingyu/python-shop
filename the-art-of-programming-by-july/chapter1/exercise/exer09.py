# -*- coding: utf-8 -*-
"""
9、字符个数的统计

char *str = "AbcABca"; 写出一个函数，查找出每个字符的个数，区分大小写，要求时间复杂度是n
"""
def func1(word):#{{{
    if word:
        pool = [0] * 51
        # in ASCII, 'A' starts earlier than 'a'
        for _ in word:
            idx = ord(_) - ord('A')
            pool[idx] = pool[idx] + 1
        for _ in range(len(pool)):
            if pool[_] > 0:
                print chr(_ + ord('A')) + ': ' + str(pool[_])
    return
#}}}

import sys
word = sys.argv[1]
print func1(word)
