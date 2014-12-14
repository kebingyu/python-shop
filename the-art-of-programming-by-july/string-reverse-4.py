# -*- coding: utf-8 -*-
"""
单词翻转。输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变，句子中单词以空格符隔开。为简单起见，标点符号和普通字母一样处理。例如，输入“I am a student.”，则输出“student. a am I”
"""
def reverse(word):#{{{
    data = word.split(' ')
    ret = ''
    for _ in range(len(data) - 1, -1, -1):
        ret = ret + ' ' + data[_]
    return ret

def flip(word):
    data = [_ for _ in word]
    fr = 0
    to = len(word) - 1
    while fr < to:
        data[fr], data[to] = data[to], data[fr]
        fr = fr + 1
        to = to - 1
    return ''.join(data)#}}}

import sys
word = sys.argv[1]
print reverse(word)
