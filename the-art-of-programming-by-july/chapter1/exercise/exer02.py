# -*- coding: utf-8 -*-
"""
2、对称子字符串的最大长度

输入一个字符串，输出该字符串中对称的子字符串的最大长度。比如输入字符串“google”，由于该字符串里最长的对称子字符串是“goog”，因此输出4。
"""
def func1(word):#{{{
    length = len(word)
    if length < 2:
        return length
    else:
        max_length = 0
        for idx_i in range(length):
            if (min(idx_i, length - 1 - idx_i) + 1) * 2 > max_length:
                # odd length palindrome
                for idx_j in range(1, length + 1, 2):
                    left  = idx_i - idx_j / 2
                    right = idx_i + idx_j / 2
                    if left >= 0 and right < length and word[left] == word[right]:
                        max_length = max(max_length, idx_j)
                    else:
                        break
                # even length palindrome
                for idx_j in range(2, length + 1, 2):
                    left  = idx_i - idx_j / 2 + 1
                    right = idx_i + idx_j / 2
                    if left >= 0 and right < length and word[left] == word[right]:
                        max_length = max(max_length, idx_j)
                    else:
                        break
        return max_length
#}}}

import sys
word = [_ for _ in sys.argv[1]]
print func1(word)
