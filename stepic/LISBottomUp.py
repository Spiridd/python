def largest_sequence(v):
    subsequence = [1] * len(v)
    for i, vi in enumerate(v):
        for j, vj in enumerate(v[:i]):
            if vi % vj == 0 and subsequence[i] < subsequence[j] + 1:
                subsequence[i] = subsequence[j] + 1
    ans = 0
    for sub in subsequence:
        ans = max(ans, sub)
    return ans


def main():
    n = int(input())
    vec = tuple(map(int, input().split()))
    k = largest_sequence(vec)
    print(k)


if __name__ == '__main__':
    main()
