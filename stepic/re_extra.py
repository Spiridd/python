import re
import sys


pattern = re.compile(r'\b(0+|1(01*0)*1)+\b')
for line in sys.stdin:
    line = line.rstrip()
    if len(line.split()) > 1:
        continue
    if re.findall(pattern, line):
        print(line)

