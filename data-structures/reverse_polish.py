from stack import Stack

exp = '645+*5-23+/'
stack = Stack()
for _ in exp:
    if _ == '+':
        stack.push(int(stack.top()) + int(stack.top()))
    elif _ == '-':
        second = int(stack.top())
        stack.push(int(stack.top()) - second)
    elif _ == '*':
        stack.push(int(stack.top()) * int(stack.top()))
    elif _ == '/':
        second = int(stack.top())
        stack.push(int(stack.top()) / second)
    else:
        stack.push(_)

print stack
