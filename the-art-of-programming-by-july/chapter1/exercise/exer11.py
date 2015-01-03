# -*- coding: utf-8 -*-
"""
11、字符串的集合

给定一个字符串的集合，格式如：{aaa bbb ccc}， {bbb ddd}，{eee fff}，{ggg}，{ddd hhh}
要求将其中交集不为空的集合合并，要求合并完成后的集合之间无交集，例如上例应输出{aaa bbb ccc ddd hhh}，{eee fff}， {ggg}。
"""
def wordToBinary(word, table):
    return 1 << (table.index(word))

def binaryToWord(bi, table):
    word = []
    for _ in range(len(table)):
        if bi & (1 << _) > 0:
            word.append(table[_])
    return word

def merge(word, table, mark):
    length = len(word)
    if length == 1:
        print word[0]
        return
    else:
        # compare the first element with the rest
        merge_idx = None
        for _ in range(1, length):
            if mark[0] & mark[_] > 0:
                merge_idx = _
                break
        if merge_idx != None:
            merged_bi = mark[0] | mark[_]
            word[_] = binaryToWord(merged_bi, table)
            mark[_] = merged_bi
            merge(word[1:], table, mark[1:])
        else:
            # no common elements
            print word[0]
            merge(word[1:], table, mark[1:])

def func1(words):
    length = len(words)
    if length > 1:
        # create lookup table
        table = {}
        for word in words:
            for _ in word:
                if not table.has_key(_):
                    table[_] = True
        lookup_table = table.keys()
        lookup_table.sort()
        mark = []
        # create mark 
        for word in words:
            bi = 0
            for _ in word:
                bi = bi | wordToBinary(_, lookup_table)
            mark.append(bi)
        # start merging
        merge(words, lookup_table, mark)



import sys
temp = sys.argv[1].split(',')
temp2 = []
for _ in temp:
    temp2.append(_.split())
print func1(temp2)

# python exer11.py 'aaa bbb ccc,bbb ddd,eee fff,ggg,ddd hhh'
