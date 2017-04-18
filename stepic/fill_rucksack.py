n, w = [int(x) for x in input().split(' ')]
things = []
for _ in range(n):
    s = input().split(' ')
    cost = int(s[0])
    volume = int(s[1])
    things.append((cost, volume))

things.sort(key=lambda x: x[0]/x[1], reverse=True)
total_cost = 0
free_volume = w
for thing in things:
    part = min(thing[1], free_volume)
    if part > 0:
        free_volume -= part
        total_cost += part/thing[1]*thing[0]
    else:
        break
print(total_cost)
