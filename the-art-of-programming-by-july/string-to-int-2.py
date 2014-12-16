"""
Integer to string
"""
def intToString(num):
    if num < 0:
        sign = '-'
        num = -num
    else:
        sign = ''
    string = ''
    while num > 10:
        string = str(num % 10) + string 
        num = num / 10
    return sign + str(num) + string

import sys
num = int(sys.argv[1])
print intToString(num)
