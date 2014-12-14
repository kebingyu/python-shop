# -*- coding: utf-8 -*-
"""
链表翻转。给出一个链表和一个数k，比如，链表为1→2→3→4→5→6，k=2，则翻转后2→1→6→5→4→3，若k=3，翻转后3→2→1→6→5→4，若k=4，翻转后4→3→2→1→6→5，用程序实现。
"""

def move(data, length):#{{{
    reverse(data, 0, length - 1)
    reverse(data, length, len(data) - 1)
    return data

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
