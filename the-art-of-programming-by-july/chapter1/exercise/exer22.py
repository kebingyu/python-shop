# -*- coding: utf-8 -*-
"""
22、字符串压缩

通过键盘输入一串小写字母(a~z)组成的字符串。请编写一个字符串压缩程序，将字符串中连续出席的重复字母进行压缩，并输出压缩后的字符串。
压缩规则：

仅压缩连续重复出现的字符。比如字符串"abcbc"由于无连续重复字符，压缩后的字符串还是"abcbc"。
压缩字段的格式为"字符重复的次数+字符"。例如：字符串"xxxyyyyyyz"压缩后就成为"3x6yz"。
要求实现函数： void stringZip(const char *pInputStr, long lInputLen, char *pOutputStr);

输入pInputStr： 输入字符串lInputLen： 输入字符串长度
输出 pOutputStr： 输出字符串，空间已经开辟好，与输入字符串等长；
注意：只需要完成该函数功能算法，中间不需要有任何IO的输入输出

示例

输入：“cccddecc” 输出：“3c2de2c”
输入：“adef” 输出：“adef”
输入：“pppppppp” 输出：“8p”
"""
def stringZip(pInputStr, lInputLen, pOutputStr):#{{{
    if lInputLen > 0:
        curr_char = None
        char_count = 0
        for _ in pInputStr:
            if curr_char == None:
                curr_char = _
                char_count = 1
            elif curr_char == _:
                char_count = char_count + 1
            else:
                if char_count == 1:
                    pOutputStr.append(curr_char)
                else:
                    pOutputStr.append(str(char_count) + curr_char)
                curr_char = _
                char_count = 1
        if char_count == 1:
            pOutputStr.append(curr_char)
        else:
            pOutputStr.append(str(char_count) + curr_char)
    return ''.join(pOutputStr)
#}}}

import sys
pInputStr = [_ for _ in sys.argv[1]]
lInputLen = len(pInputStr)
pOutputStr = [''] * lInputLen
print stringZip(pInputStr, lInputLen, pOutputStr)
