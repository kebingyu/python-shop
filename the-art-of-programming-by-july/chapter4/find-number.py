# -*- coding: utf-8 -*-
"""
数组中有一个数字出现的次数超过了数组长度的一半，找出这个数字。
"""
def func1(numbers):#{{{
    # time O(n), space O(n)
    length = len(numbers)
    if length == 0:
        return None
    elif length == 1:
        return numbers[0]
    else:
        table = {}
        for _ in numbers:
            if table.has_key(_):
                table[_] += 1
            else:
                table[_] = 1
        for _ in table.keys():
            if table[_] > length / 2:
                return _
        return None
#}}}

def func2(numbers):#{{{
    # time O(n*lgn), space O(1)
    length = len(numbers)
    if length == 0:
        return None
    elif length == 1:
        return numbers[0]
    else:
        numbers.sort()
        count = 0 
        curr = numbers[0]
        for _ in numbers:
            if _ == curr:
                count += 1
            else:
                if count > length / 2:
                    return curr
                else:
                    count = 1
                    curr = _
        return None
#}}}

def func3(numbers):#{{{
    # time O(n), space O(1)
    length = len(numbers)
    if length == 0:
        return None
    elif length == 1:
        return numbers[0]
    else:
        curr = None
        count = 0
        for _ in numbers:
            if curr == None:
                curr = _
                count += 1
            elif curr == _:
                count += 1
            else:
                count -= 1
            if count == 0:
                curr = _

        if count > 0:
            return curr
        else:
            return None
#}}}

import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers)
print func2(numbers)
print func3(numbers)

#python find-number.py '1,2,3,1,2,2,4,2'
