# -*- coding: utf-8 -*-
"""
如果不是求字符的所有排列，而是求字符的所有组合，应该怎么办呢？
当输入的字符串中含有相同的字符串时，相同的字符交换位置是不同的排列，但是同一个组合。
举个例子，如果输入abc，它的组合有a、b、c、ab、ac、bc、abc。
"""
def combination1(word, length):#{{{
    if length == 1:
        return [word[0]]
    else:
        head = word.pop()
        ret = [head]
        comb = combination1(word, length - 1)
        for _ in comb:
            ret.extend([_, head + _])
        return ret
#}}}

import sys
word = [_ for _ in sys.argv[1]]
print combination1(word, len(word))
