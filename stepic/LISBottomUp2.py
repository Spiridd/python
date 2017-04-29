from bisect import bisect_right


def largest_sequence(v):
    # O(n^2) complexity
    # 1 >= 2 >= 3 >= ...
    subsequence = [1] * len(v)
    for i, vi in enumerate(v):
        for j, vj in enumerate(v[:i]):
            if vj >= vi and subsequence[i] < subsequence[j] + 1:
                subsequence[i] = subsequence[j] + 1
    print(v)
    print(subsequence)
    largest_sub_len = 1
    index_of_largest_sub = 0
    for k, sub in enumerate(subsequence):
        if sub > largest_sub_len:
            largest_sub_len = sub
            index_of_largest_sub = k

    indexes = [0] * largest_sub_len
    for i in reversed(range(len(indexes))):
        indexes[i] = index_of_largest_sub
        # find prev index_of_largest_sub that satisfies condition
        largest_sub_len -= 1
        while index_of_largest_sub > 0 and (subsequence[index_of_largest_sub] != largest_sub_len
                                            or v[index_of_largest_sub] < v[indexes[i]]):
            index_of_largest_sub -= 1
    print(indexes)
    return indexes


def fast_largest_sequence(vec):
    # O(n log n) complexity
    # 1 < 2 < 3 < ...
    ancestors = [-1] * len(vec)
    subsequence = [(vec[0], 0)]
    for i, v in enumerate(vec):
        if v > subsequence[-1][0]:
            subsequence.append((v, i))
            ancestors[i] = subsequence[-2][1]
        else:
            # if it works incorrect we have to keep
            # vector of indexes [i] separately
            pos = bisect_right(subsequence, (v, ))
            subsequence[pos] = (v, i)
            try:
                ancestors[i] = subsequence[-2][1]
            except IndexError:
                pass
    index = subsequence[-1][1]
    answer = []
    for _ in range(len(subsequence)):
        answer.append(index)
        index = ancestors[index]
    return tuple(reversed(answer))


def non_increasing_sub(vec):
    # O(n log n) complexity
    # 1 >= 2 >= 3 >= ...
    ancestors = [-1] * len(vec)
    subsequence = [(vec[0], 0)]
    for i, v in enumerate(vec):
        if v <= subsequence[-1][0]:
            subsequence.append((v, i))
            ancestors[i] = subsequence[-2][1]
        else:
            # if it works incorrect we have to keep
            # vector of indexes [i] separately
            pos = bisect_right(subsequence, (v, ))
            subsequence[pos] = (v, i)
            try:
                ancestors[i] = subsequence[-2][1]
            except IndexError:
                pass
    index = subsequence[-1][1]
    answer = []
    for _ in range(len(subsequence)):
        answer.append(index)
        index = ancestors[index]
    return tuple(reversed(answer))


def main():
    n = int(input())
    vec = tuple(map(int, input().split()))
    # indexes = largest_sequence(vec)
    # indexes = fast_largest_sequence(vec)
    indexes = non_increasing_sub(vec)
    print(len(indexes))
    [print(index+1, end=' ') for index in indexes]


if __name__ == '__main__':
    main()
