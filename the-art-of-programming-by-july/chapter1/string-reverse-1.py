# -*- coding: utf-8 -*-
"""
给定一个字符串，要求把字符串前面的若干个字符移动到字符串的尾部，如把字符串“abcdef”前面的2个字符'a'和'b'移动到字符串的尾部，使得原字符串变成字符串“cdefab”。请写一个函数完成此功能，要求对长度为n的字符串操作的时间复杂度为 O(n)，空间复杂度为 O(1)。

input: python 1.py 'abcdef' 2
output: 'cdefab'
"""

def move(word, length):#{{{
    data = [_ for _ in word]
    totalLength = len(data)
    if totalLength and length < totalLength:
        reverse(data, 0, length - 1)
        reverse(data, length, totalLength - 1)
        reverse(data, 0, totalLength - 1)
    return ''.join(data)

def reverse(data, fr, to):
    while fr < to:
        data[fr], data[to] = data[to], data[fr]
        fr = fr + 1
        to = to -1
    return data
#}}}

import sys
word = sys.argv[1]
length = int(sys.argv[2])
print move(word, length)
