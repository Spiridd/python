def isancestor(ancestor, child):
    if ancestor == child:
        return True
    global parents
    current_ancestors = parents[child]
    for anc in current_ancestors:
        if isancestor(ancestor, anc):
            return True
    return False


n = int(input())
parents = {}
for _ in range(n):
    s = input().split(' : ')
    child = s[0]
    if len(s) == 1:
        parents[child] = set()
    else:
        straight_ancestors = s[1].split()
        parents[child] = set(straight_ancestors)
m = int(input())
exceptions = set()
for _ in range(m):
    cur_ex = input()
    catched = True
    for e in exceptions:
        if isancestor(e, cur_ex):
            catched = False
    if catched:
        exceptions.add(cur_ex)
    else:
        print(cur_ex)
