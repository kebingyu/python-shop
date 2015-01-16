# -*- coding: utf-8 -*-
"""
we have 100 people and 5 gold mines
1st gold mine needs 77 people and can get 92 gold
2nd gold mine needs 22 people and can get 22 gold
3rd gold mine needs 29 people and can get 87 gold
4th gold mine needs 50 people and can get 46 gold
5th gold mine needs 99 people and can get 90 gold

one person can only dig one gold mine
each gold mine needs the exact amount of people to dig

question: to get the most gold with given people

answer: 133
"""
def maxGold(num_people, idx_mine, list_man, list_gold):#{{{
    # performance can be improved by caching the sub-problems
    # read/write cache[num_people][idx_mine]
    # boundary
    if idx_mine == 0:
        if num_people >= list_man[idx_mine]:
            getGold = list_gold[idx_mine]
        else:
            getGold = 0
    # dp
    elif num_people >= list_man[idx_mine]:
        # if dig this mine
        gold_dig = maxGold(num_people - list_man[idx_mine], idx_mine - 1,\
                list_man, list_gold) + list_gold[idx_mine]
        # if not dig this mine
        gold_not_dig = maxGold(num_people, idx_mine - 1, list_man, list_gold)
        getGold = max(gold_dig, gold_not_dig)
    else:
        getGold = maxGold(num_people, idx_mine - 1, list_man, list_gold)
    return getGold
#}}}

import sys
numbers = sys.stdin.readlines()
# process data
list_man = []
list_gold = []
temp = numbers[0].split(' ')
total_people = int(temp[0])
num_gold_mine = int(temp[1])
for _ in range(1, len(numbers)):
    temp = numbers[_].rstrip().split(' ')
    list_man.append(int(temp[0]))
    list_gold.append(int(temp[1]))
print maxGold(total_people, num_gold_mine - 1, list_man, list_gold)

#python gold-mine.py
#100 5
#77 92
#22 22
#29 87
#50 46
#99 90
# ctrl+d
