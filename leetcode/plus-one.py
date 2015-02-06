"""
Difficulty: Easy

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

"""
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):#{{{
        length = len(digits)
        if length > 0:
            idx = length - 1
            carry = 1
            while idx >= 0:
                if digits[idx] + carry <= 9:
                    digits[idx] += carry
                    carry = 0
                else:
                    digits[idx] = digits[idx] + carry - 10
                    carry = 1
                idx -= 1
            if carry == 1:
                digits.insert(0, 1)
        return digits
#}}}
