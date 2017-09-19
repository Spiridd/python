# replace a with b in s so that there is no a in s
# print minimal number of operations
# if impossible print impossible

# seems to be wrong (passes tests though)
import sys


s = input()
a = input()
b = input()
if a in b and a in s:
    print('Impossible')
    sys.exit(0)
new = s.replace(a, b)
n = 0
while new != s:
    n += 1
    new, s = new.replace(a, b), new
if a in s:
    print('Impossible')
else:
    print(n)
