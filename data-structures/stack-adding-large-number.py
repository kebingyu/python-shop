"""
stack usage: adding two very large numbers
"""
from stack import Stack
import sys

n1 = str(sys.argv[1])
n2 = str(sys.argv[2])

s1 = Stack()
s2 = Stack()
result = Stack()

for _ in n1:
    s1.push(_)
for _ in n2:
    s2.push(_)

carry = 0
while not s1.isEmpty() and not s2.isEmpty():
    sum = str(int(s1.top()) + int(s2.top()) + carry)
    if len(sum) == 2:
        carry = int(sum[0])
        sum = sum[1]
    else:
        carry = 0
    result.push(sum)

if s1.isEmpty() and not s2.isEmpty():
    left = s2
elif s2.isEmpty() and not s1.isEmpty():
    left = s1
else:
    left = None

if left != None:
    while not left.isEmpty():
        sum = str(int(left.top()) + carry)
        if len(sum) == 2:
            carry = int(sum[0])
            sum = sum[1]
        else:
            carry = 0
        result.push(sum)

if carry != 0:
    result.push(str(carry))

answer = ''
while not result.isEmpty():
    answer = answer + result.top()
print answer
