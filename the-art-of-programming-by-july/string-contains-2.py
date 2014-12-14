# -*- coding: utf-8 -*-
"""
如果两个字符串的字符一样，但是顺序不一样，被认为是兄弟字符串，比如bad和adb即为兄弟字符串，现提供一个字符串，如何在字典中迅速找到它的兄弟字符串，请描述数据结构和查询过程。
"""
def isBrother(word1, word2):#{{{
    if len(word1) != len(word2):
        return False

    pool = {}
    # scan word1 and store in hashtable
    for _ in word1:
        if pool.has_key(_):
            pool[_] = pool[_] + 1
        else:
            pool[_] = 1
    # scan word2
    for _ in word2:
        if pool.has_key(_):
            pool[_] = pool[_] - 1
        else:
            return False
        if pool[_] == 0:
            pool.pop(_)
    if len(pool) == 0:
        return True
    else:
        return False
#}}}

import sys
word1 = sys.argv[1]
word2 = sys.argv[2]
print isBrother(word1, word2)
