import re
import sys


pattern = re.compile(r'z.{3}z')
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line):
        print(line)