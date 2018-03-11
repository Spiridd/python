import re
import sys


pattern = re.compile(r'\bcat\b')
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line):
        print(line)
