"""
Первая строка входа содержит целые числа 1≤W≤10^4 и 1≤n≤300 —
вместимость рюкзака и число золотых слитков. Следующая строка
содержит n целых чисел 0≤w1,…,wn≤10^5, задающих веса слитков.
Найдите максимальный вес золота, который можно унести в рюкзаке.
"""
# dynamic programming BottomUp


def max_cost(capacity, weights, costs):
    d = [[0] * (capacity+1) for _ in range(len(weights)+1)]
    for i in range(1, len(weights)+1):
        wi = weights[i - 1]
        ci = costs[i - 1]
        for w in range(1, capacity+1):
            d[i][w] = d[i-1][w]
            if wi <= w:
                d[i][w] = max(d[i][w], d[i-1][w-wi]+ci)
    return d[len(weights)][capacity]


def main():
    capacity, n = map(int, input().split())
    weights = tuple(map(int, input().split()))
    print(max_cost(capacity, weights, weights))


if __name__ == '__main__':
    main()
