"""
Difficulty: Easy

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

n = 4
P     I     N
A   L S   I G
Y A   H R
P     I

"""
class Solution:
    # @return a string
    def convert(self, s, nRows):#{{{
        if nRows <= 1:
            ret = s
        elif nRows == 2:
            ret = ''
            length = len(s)
            for _ in range(0, length, 2):
                ret += s[_]
            for _ in range(1, length, 2):
                ret += s[_]
        else:
            ret = ''
            length = len(s)
            total = 2 * nRows - 2
            for row in range(nRows):
                step = total - row * 2
                curr = row
                while curr < length:
                    ret += s[curr]
                    if step % total != 0 and curr + step < length:
                        ret += s[curr + step]
                    curr += total
        return ret
#}}}
