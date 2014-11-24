import sys
"""
sys.argv[0] is the file name if you run python <file>
"""
if len(sys.argv) > 1:
    word = sys.argv[1]
    for _ in range(len(word)):
        print word[_]

    print word.split(',')

    temp = [''] * len(word)
    i = 0
    j = len(word) - 1
    while i < j:
        temp[j] = word[i]
        temp[i] = word[j]
        i = i + 1
        j = j - 1
    if i == j:
        temp[i] = word[i]
    print temp

"""
line by line reading from stdin. ctrl-d for EOF
"""
for line in sys.stdin:
    print line
