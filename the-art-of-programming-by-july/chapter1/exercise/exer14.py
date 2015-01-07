# -*- coding: utf-8 -*-
"""
14、字符串的压缩

一个字符串，压缩其中的连续空格为1个后，对其中的每个字串逆序打印出来。比如"abc efg hij"打印为"cba gfe jih"。
"""
def func1(word):#{{{
    temp = []
    space_idx = []
    length = len(word)
    if length > 0:
        idx = 0
        # left trim space
        while word[idx] == ' ':
            idx = idx + 1

        # store string into list
        for _ in range(idx, length):
            if word[_] != ' ':
                temp.append(word[_])
            elif temp[-1] != ' ':
                space_idx.append(len(temp))
                temp.append(word[_])

        # right trim space
        if temp[-1] == ' ':
            temp.pop()

        # swap
        for _ in range(len(space_idx)):
            if _ == 0:
                swap(temp, 0, space_idx[_] - 1)
            else:
                swap(temp, space_idx[_ - 1] + 1, space_idx[_] - 1)
        if (len(space_idx) > 0):
            swap(temp, space_idx[-1] + 1, len(temp) - 1)
        else:
            swap(temp, 0, len(temp) - 1)

    return ''.join(temp)

def swap(word, fr, to):
    while fr < to:
        word[fr], word[to] = word[to], word[fr]
        fr = fr + 1
        to = to - 1
#}}}

import sys
word = sys.argv[1]
print func1(word)

# python exer14.py 'abc efg   hijk'
