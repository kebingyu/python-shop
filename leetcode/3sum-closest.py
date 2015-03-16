"""
Difficulty: Medium

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""
class Solution:
    # @return an integer
    def threeSumClosest(self, numbers, target):#{{{
        closest_sum = float('inf')
        length = len(numbers)
        if length > 0:
            numbers.sort()
            for _ in range(length):
                idx_i = 0
                idx_j = length - 1
                while idx_i < idx_j:
                    if idx_i == _:
                        idx_i = idx_i + 1
                    elif idx_j == _:
                        idx_j = idx_j - 1
                    else:
                        curr_sum = numbers[idx_i] + numbers[idx_j] + numbers[_]
                        if curr_sum == target:
                            return curr_sum
                        else:
                            if abs(curr_sum - target) < abs(closest_sum - target):
                                closest_sum = curr_sum
                            if curr_sum > target: 
                                idx_j = idx_j - 1
                            else:
                                idx_i = idx_i + 1
        return closest_sum
#}}}
