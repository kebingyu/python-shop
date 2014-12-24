# -*- coding: utf-8 -*-
"""
写一个程序，打印出以下的序列。

(a),(b),(c),(d),(e)........(z)

(a,b),(a,c),(a,d),(a,e)......(a,z),(b,c),(b,d).....(b,z),(c,d).....(y,z)

(a,b,c),(a,b,d)....(a,b,z),(a,c,d)....(x,y,z)

....

(a,b,c,d,.....x,y,z)
"""
def combination1(word, length):#{{{
    if length == 1:
        return [word[0]]
    else:
        head = word.pop(0)
        ret = [head]
        comb = combination1(word, length - 1)
        for _ in comb:
            ret.append(_)
        for _ in comb:
            ret.append(head + _)
        return ret
#}}}

word = [_ for _ in 'abcd']
print combination1(word, len(word))
