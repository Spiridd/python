import re
import sys


def repl(match):
    return match.group(0)[0]


pattern = re.compile(r'(\w)\1+')
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, repl, line)
    print(line)
