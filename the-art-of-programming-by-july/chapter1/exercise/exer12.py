# -*- coding: utf-8 -*-
"""
12、五笔编码

五笔的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把五笔的编码按字典序排序，形成一个数组如下： a, aa, aaa,
aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy
其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。

编写一个函数，输入是任意一个编码，比如baca，输出这个编码对应的Index；
编写一个函数，输入是任意一个Index，比如12345，输出这个Index对应的编码。
"""
def getIndex(code):#{{{
    """
    1. a => 0, aa => 1, aaa => 2, aaaa => 3, Index = len(code) - 1
    2. Index of b    = Index of a + 25 (aa to ay) + 25 ** 2 (aaa to ayy) + 25 ** 3 (aaaa to ayyy) + 1
    3. Index of ab   = Index of aa + 25 (aaa to aay) + 25 ** 2 (aaaa to aayy) + 1
    4. Index of aab  = Index of aaa + 25 (aaaa to aaay) + 1
    5. Index of aaab = Index of aaaa + 1
    """
    increment = [1+25+25**2+25**3, 1+25+25**2, 1+25, 1]
    length = len(code)
    index = length - 1
    for _ in range(length):
        index = index + (ord(code[_]) - ord('a')) * increment[_]
    return index
#}}}

def getCode(index):#{{{
    increment = [1+25+25**2+25**3, 1+25+25**2, 1+25, 1]
    idx = 0
    code = [''] * 4
    while index >= 0:
        mod = index / increment[idx]
        index = index % increment[idx]
        code[idx] = chr(mod + ord('a'))
        idx = idx + 1
        # go to the next code
        index = index - 1
    return ''.join(code)
#}}}

import sys
code = sys.argv[1]
index = int(sys.argv[2])
print getIndex(code)
print getCode(index)
