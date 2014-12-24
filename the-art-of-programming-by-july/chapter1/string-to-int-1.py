# -*- coding: utf-8 -*-
"""
输入一个由数字组成的字符串，把它转换成整数并输出。例如：输入字符串"123"，输出整数123。

给定函数原型int StrToInt(const char *str) ，实现字符串转换成整数的功能，不能使用库函数atoi。
"""
def StrToInt(string):
    num = 0
    if len(string) > 0:
        length = len(string)
        # check sign
        if string[0] == '-':
            sign = -1
            idx = 1
        elif string[0] == '+':
            sign = 1
            idx = 1
        elif isInteger(string[0]):
            sign = 1
            idx = 0
        else:
            return 0
        # convert
        while idx < length and isInteger(string[idx]):
            # not considering int overflow
            num = 10 * num + (ord(string[idx]) - ord('0'))
            idx = idx + 1
    return num * sign

def isInteger(string):
    return string == '1' or string == '2' or string == '3' or string == '4'\
        or string == '5' or string == '6' or string == '7' or string == '8'\
        or string == '9' or string == '0'

import sys
string = sys.argv[1]
print StrToInt(string)
