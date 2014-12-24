# -*- coding: utf-8 -*-
"""
已知字符串里的字符是互不相同的，现在任意组合，比如ab，则输出aa，ab，ba，bb，编程按照字典序输出所有的组合。
"""
def permutation1(word, length):#{{{
    if length == 0:
        return ['']
    else:
        word.sort()
        ret = []
        for str_i in word:
            perm = permutation1(word, length - 1)
            for str_j in perm:
                ret.append(str_i + str_j)
        return ret
#}}}

import sys
word = [_ for _ in sys.argv[1]]
print permutation1(word, len(word))
