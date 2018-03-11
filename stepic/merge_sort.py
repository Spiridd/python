counter = 0


def merge(v, l, m, r):
    global counter
    i, j = l, m+1
    ret = []
    while i <= m and j <= r:
        if v[i] <= v[j]:
            ret.append(v[i])
            i += 1
        else:
            ret.append(v[j])
            j += 1
            counter += m - i + 1
    while i <= m:
        ret.append(v[i])
        i += 1
        # counter += 1
    while j <= r:
        ret.append(v[j])
        j += 1
    fuck = ret.__iter__()
    for i in range(l, r+1):
        v[i] = next(fuck)


def merge_sort(v, l, r):
    if l < r:
        m = (l+r)//2
        merge_sort(v, l, m)
        merge_sort(v, m+1, r)
        merge(v, l, m, r)


n = int(input())
vec = list(map(int, input().split()))
merge_sort(vec, 0, len(vec)-1)
print(counter)
