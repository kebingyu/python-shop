# -*- coding: utf-8 -*-
"""
编写程序，在原字符串中把字符串尾部的m个字符移动到字符串的头部，要求：长度为n的字符串操作时间复杂度为O(n)，空间复杂度为O(1)。
例如，原字符串为”Ilovebaofeng”，m=7，输出结果为：”baofengIlove”。
"""
def move(data, length):#{{{
    totalLength = len(data)
    if totalLength and length < totalLength:
        reverse(data, 0, totalLength - length - 1)
        reverse(data, totalLength - length, totalLength - 1)
        reverse(data, 0, totalLength - 1)
    return ''.join(data)

def reverse(data, fr, to):
    while fr < to:
        data[fr], data[to] = data[to], data[fr]
        fr = fr + 1
        to = to - 1
    return data
#}}}

import sys
data = [_ for _ in sys.argv[1]]
length = int(sys.argv[2])
print move(data, length)
