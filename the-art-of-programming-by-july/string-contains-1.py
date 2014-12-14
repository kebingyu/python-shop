# -*- coding: utf-8 -*-
"""
给定两个分别由字母组成的字符串A和字符串B，字符串B的长度比字符串A短。请问，如何最快地判断字符串B中所有字母是否都在字符串A里？

为了简单起见，我们规定输入的字符串只包含大写英文字母，请实现函数bool StringContains(string &A, string &B)

比如，如果是下面两个字符串：

String 1：ABCD

String 2：BAD

答案是true，即String2里的字母在String1里也都有，或者说String2是String1的真子集。

如果是下面两个字符串：

String 1：ABCD

String 2：BCE

答案是false，因为字符串String2里的E字母不在字符串String1里。

同时，如果string1：ABCD，string 2：AA，同样返回true。
"""
def StringContains1(string1, string2):#{{{
    def merge(word1, word2):#{{{
        idx1 = 0
        idx2 = 0
        word3 = ''
        while idx1 < len(word1) and idx2 < len(word2):
            if word1[idx1] < word2[idx2]:
                word3 = word3 + word1[idx1]
                idx1 = idx1 + 1
            else:
                word3 = word3 + word2[idx2]
                idx2 = idx2 + 1
        while idx1 < len(word1):
            word3 = word3 + word1[idx1]
            idx1 = idx1 + 1
        while idx2 < len(word2):
            word3 = word3 + word2[idx2]
            idx2 = idx2 + 1
        return word3
#}}}
    def mergeSort(word):#{{{
        if len(word) > 1:
            mid = len(word) / 2
            word1 = mergeSort(word[:mid])
            word2 = mergeSort(word[mid:])
            word = merge(word1, word2)
        return word
#}}}
    def search(needle, haystack):#{{{
        if len(needle) and len(haystack):
            mid = len(haystack) / 2
            if needle > haystack[mid]:
                return search(needle, haystack[mid + 1:])
            elif needle < haystack[mid]:
                return search(needle, haystack[:mid])
            else:
                return True
        return False
#}}}
    # merge sort string1
    string1 = mergeSort(string1)
    # binary search for each char
    for _ in string2:
        if search(_, string1) == False:
            return False
    return True
#}}}

def StringContains2(string1, string2):#{{{
    table = {}
    for _ in string1:
        if not table.has_key(_):
            table[_] = True
    for _ in string2:
        if not table.has_key(_):
            return False
    return True
#}}}

def StringContains3(string1, string2):#{{{
    mem = 0
    for _ in string1:
        shift = ord(_) - ord('A')
        mem = mem | (1 << shift)
    for _ in string2:
        shift = ord(_) - ord('A')
        if (mem & (1 << shift) == 0):
            return False
    return True
#}}}

import sys
string1 = sys.argv[1]
string2 = sys.argv[2]
print StringContains1(string1, string2)
print StringContains2(string1, string2)
print StringContains3(string1, string2)
