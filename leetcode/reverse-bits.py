"""
Difficulty: Easy

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):#{{{
        bin_str = self.int2bin(n)
        return self.bin2int(bin_str[::-1])
#}}}
        
    def int2bin(self, n):#{{{
        bin_str = ''
        while n > 0:
            bin_str = str(n % 2) + bin_str
            n = n / 2
        return '0' * (32 - len(bin_str)) + bin_str
#}}}
        
    def bin2int(self, bin_str):#{{{
        num = 0
        for i in range(32):
            rank = 32 - i - 1
            num += (1 << rank) * int(bin_str[i])
        return num
#}}}
