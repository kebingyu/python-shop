# -*- coding: utf-8 -*-
"""
给定一个字符串，求它的最长回文子串的长度
"""
def longest_palindrome1(word):#{{{
    length = len(word)
    if length < 2:
        return length

    longest = 1
    for idx_i in range(length):
        # odd length palindrome
        for idx_j in range(1, length + 1, 2):
            left = idx_i - idx_j / 2
            right = idx_i + idx_j / 2
            if left >= 0 and right < length and word[left] == word[right]:
                longest = max(longest, idx_j)
            else:
                break
        # even length palindrome
        for idx_j in range(2, length + 1, 2):
            left = idx_i - idx_j / 2 + 1
            right = idx_i + idx_j / 2
            if left >= 0 and right < length and word[left] == word[right]:
                longest = max(longest, idx_j)
            else:
                break
    return longest
#}}}

def longest_palindrome2(word):#{{{
    # Manacher algorithm
    pass
#}}}

import sys
word = sys.argv[1]
print longest_palindrome1(word)
print longest_palindrome2(word)
