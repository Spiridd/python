import re
import sys


pattern = re.compile(r'\b[aA]+\b')
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, 'argh', line, 1)
    print(line)
