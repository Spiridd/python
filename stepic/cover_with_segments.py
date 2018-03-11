from operator import itemgetter

from matplotlib import pyplot as plt


n = int(input())
segments = []
for _ in range(n):
    s = input().split(' ')
    left = int(s[0])
    right = int(s[1])
    segments.append((left, right))
print(segments)
segments.sort(key=itemgetter(1))
print(segments)

for k in range(n):
    plt.plot(segments[k], [k/n, k/n])
plt.show()

solution = []
solution.append(segments[0][1])
for k in range(1, n):
    if segments[k][0] > solution[-1]:
        solution.append(segments[k][1])
print(len(solution))
[print(point, end=' ') for point in solution]
