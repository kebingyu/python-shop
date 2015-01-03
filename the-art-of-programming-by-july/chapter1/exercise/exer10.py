# -*- coding: utf-8 -*-
"""
10、最小子串

给一篇文章，里面是由一个个单词组成，单词中间空格隔开，再给一个字符串指针数组，比如 char *str[]={"hello","world","good"};

求文章中包含这个字符串指针数组的最小子串。注意，只要包含即可，没有顺序要求。
"""
def func1(needle, haystack):#{{{
    ret = []
    min_length = len(haystack)
    if needle and haystack:
        for _ in range(len(haystack)):
            needle_copy = needle[:]
            matched_words = []
            idx_h = _
            while idx_h < len(haystack):
                if needle_copy:
                    if haystack[idx_h] in needle_copy:
                        matched_words.append(haystack[idx_h])
                        needle_copy.remove(haystack[idx_h])
                    elif len(matched_words) > 0:
                        matched_words.append(haystack[idx_h])
                    idx_h = idx_h + 1
                else:
                    break
            if len(matched_words) < min_length and len(needle_copy) == 0:
                ret = matched_words
    return ret
#}}}

import sys
needle   = [_ for _ in sys.argv[1].split()]
haystack = [_ for _ in sys.argv[2].split()]
print func1(needle, haystack)

# python exer10.py 'hello world good' 'this is good test world world bla hello bla good'
