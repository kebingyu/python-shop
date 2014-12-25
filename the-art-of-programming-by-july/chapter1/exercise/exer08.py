# -*- coding: utf-8 -*-
"""
8、字符串的匹配

在一篇英文文章中查找指定的人名，人名使用二十六个英文字母（可以是大写或小写）、空格以及两个通配符组成（、?），
通配符“”表示零个或多个任意字母，通配符“?”表示一个任意字母。如：“J* Smi??” 可以匹配“John Smith” .
"""
import sys
word = [_ for _ in sys.argv[1]]
print func1(word)
