import sys


def paired_bracket(b):
    return '{' if b == '}' \
        else '[' if b == ']' \
        else '(' if b == ')' \
        else None


text = input()
n = len(text)

open_brackets = {'{', '[', '('}
close_brackets = {'}', ']', ')'}
stack = []

for i, s in enumerate(text):
    if s in open_brackets:
        stack.append(tuple([i, s]))
    elif s in close_brackets:
        if stack:
            if stack[-1][1] == paired_bracket(s):
                stack.pop()
            else:
                print(i + 1)
                sys.exit(0)
        else:
            print(i + 1)
            sys.exit(0)
if stack:
    print(stack[0][0]+1)
else:
    print('Success')
