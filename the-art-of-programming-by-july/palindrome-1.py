# -*- coding: utf-8 -*-
"""
回文，英文palindrome，指一个顺着读和反过来读都一样的字符串，比如madam、我爱我，这样的短句在智力性、趣味性和艺术性上都颇有特色，中国历史上还有很多有趣的回文诗。

那么，我们的第一个问题就是：判断一个字串是否是回文？
"""
def isPalindrome1(word):#{{{
    length = len(word)
    if length > 1:
        tmp = [_ for _ in word]
        fr = 0
        to = length - 1
        while fr < to:
            tmp[fr], tmp[to] = tmp[to], tmp[fr]
            fr = fr + 1
            to = to - 1
        reversedWord = ''.join(tmp)
        if word != reversedWord:
            return False
    return True
#}}}

def isPalindrome2(word):#{{{
    length = len(word)
    if length > 1:
        fr = 0
        to = length - 1
        # scan from head and tail
        while fr < to:
            if word[fr] == word[to]:
                fr = fr + 1
                to = to - 1
            else:
                return False
    return True
#}}}

def isPalindrome3(word):#{{{
    length = len(word)
    if length > 1:
        m = length / 2 - 1
        left = m
        right = length - m - 1
        # scan from middle
        while left >= 0:
            if word[left] == word[right]:
                left = left - 1
                right = right + 1
            else:
                return False
    return True
#}}}

import sys
word = sys.argv[1]
print isPalindrome1(word)
print isPalindrome2(word)
print isPalindrome3(word)
