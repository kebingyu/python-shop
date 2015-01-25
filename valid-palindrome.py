"""
Difficulty: Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):#{{{
        self.ord_a = ord('a')
        self.ord_z = ord('z')
        self.ord_0 = ord('0')
        self.ord_9 = ord('9')
        length = len(s)
        i = 0
        j = length - 1
        while i < j:
            if not self.isValidChar(s[i].lower()):
                i += 1
            elif not self.isValidChar(s[j].lower()):
                j -= 1
            else:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
        return True
        
    def isValidChar(self, char):
        if (ord(char) >= self.ord_a and ord(char) <= self.ord_z) or\
                (ord(char) >= self.ord_0 and ord(char) <= self.ord_9):
            return True
        else:
            return False
#}}}
