import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    line = re.sub('human', 'computer', line)
    print(line)
