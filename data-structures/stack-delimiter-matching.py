"""
stack usage: check delimiter matching
"""
from stack import Stack
import sys
#equation = 'a=b+(c-d)*(e-f))'
equation = sys.argv[1]

s = Stack()
for _ in equation:
    if '(' == _:
        s.push(_)
    elif ')' == _:
        if '(' == s.topEl():
            s.top()
        else:
            s.push(_)

if s.isEmpty():
    print 'match equation\n'
else:
    print 'mismatch equation\n'
