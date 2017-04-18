import re
import sys


pattern = 'cat'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 1:
        print(line)
