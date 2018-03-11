"""
Даны число 1≤n≤102 ступенек лестницы и целые числа −10^4≤a1,…,an≤10^4,
которыми помечены ступеньки. Найдите максимальную сумму, которую можно получить,
идя по лестнице снизу вверх (от нулевой до nn-й ступеньки),
каждый раз поднимаясь на одну или две ступеньки.
"""
# Bottom Up


def max_sum(steps):
    if len(steps) == 1:
        return steps[0]
    elif len(steps) == 2:
        return max(steps[1], sum(steps))

    d = [-1e5] * len(steps)
    d[0] = steps[0]
    d[1] = max(steps[1], steps[1]+steps[0])
    for i in range(2, len(steps)):
        d[i] = steps[i] + max(d[i-1], d[i-2])
    return d[len(steps)-1]


def main():
    n = int(input())
    steps = tuple(map(int, input().split()))
    print(max_sum(steps))


if __name__ == '__main__':
    main()
