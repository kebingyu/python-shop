# -*- coding: utf-8 -*-
"""
输入一个字符串，打印出该字符串中字符的所有排列。

例如输入字符串abc，则输出由字符a、b、c 所能排列出来的所有字符串

abc、acb、bac、bca、cab 和 cba。
"""
def permutation1(word):#{{{
    length = len(word)
    if length == 1:
        return word[0]
    else:
        ret = []
        for _ in range(length):
            word_copy = word[:]
            word_copy.pop(_)
            combs = permutation1(word_copy)
            for comb in combs:
                ret.append(word[_] + comb)
        return ret
#}}}

def permutation2(word):#{{{
    length = len(word)
    if length == 1:
        return word[0]
    else:
        word.sort()
        ret = [''.join(word)]
        next_p = next_permutation(word)
        while next_p != None:
            ret.append(''.join(next_p))
            next_p = next_permutation(next_p)
        return ret
#}}}

def next_permutation(word):#{{{
    length = len(word)
    if length < 2:
        return None

    # find the right most element i that has a bigger neighbor
    idx_i = None
    for _ in range(length - 1):
        if word[_] < word[_ + 1]:
            idx_i = _
    if idx_i == None:
        return None

    # find the right most element j that is bigger than element i
    idx_j = None
    for _ in range(idx_i + 1, length):
        if word[_] >= word[idx_i]:
            idx_j = _

    # swap element i and j
    word[idx_i], word[idx_j] = word[idx_j], word[idx_i]

    # reverse the elements on the right of element i
    fr = idx_i + 1
    to = length - 1
    while fr < to:
        word[fr], word[to] = word[to], word[fr]
        fr = fr + 1
        to = to - 1
    return word
#}}}

import sys
word = [_ for _ in sys.argv[1]]
print permutation1(word)
print permutation2(word)
