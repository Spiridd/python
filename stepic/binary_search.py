def binary_search(v, x):
    # search in [left, right)
    left = 0
    right = len(v)
    while left < right-1:
        middle = (left + right) // 2
        if x >= v[middle]:
            left = middle
        else:
            right = middle
    return left+1 if v[left] == x else -1  # left+1 is for [1, ...]


fline = map(int, input().split())
n = next(fline)
vec = [num for num in fline]
sline = map(int, input().split())
k = next(sline)
keys = [num for num in sline]
for key in keys:
    print(binary_search(vec, key), end=' ')
