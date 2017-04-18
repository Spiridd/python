import re
import sys


def repl(match):
    string = match.group(0)
    return ''.join([string[1], string[0], string[2:]])


pattern = re.compile(r'\b\w{2,}?\b')
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, repl, line)
    print(line)
