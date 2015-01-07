# -*- coding: utf-8 -*-
"""
20、回文字符串

将一个很长的字符串，分割成一段一段的子字符串，子字符串都是回文字符串。有回文字符串就输出最长的，没有回文就输出一个一个的字符。

例如：

habbafgh

输出h,abba,f,g,h。
"""
def func1(word):#{{{
    length = len(word)
    if length > 0:
        idx_fr = 0
        while idx_fr < length:
            idx_to = length - 1
            while idx_fr <= idx_to:
                if isPalindrome(word, idx_fr, idx_to):
                    print ''.join(word[idx_fr:idx_to+1])
                    break
                else:
                    idx_to = idx_to - 1
            idx_fr = idx_to + 1
    return

def isPalindrome(word, fr, to):
    if fr > to:
        return False
    else:
        while fr < to:
            if word[fr] != word[to]:
                return False
            fr = fr + 1
            to = to - 1
        return True
#}}}

import sys
word = sys.argv[1]
print func1(word)
