"""
Дано целое число 1≤n≤10^5 и массив A[1…n],
содержащий неотрицательные целые числа, не превосходящие 10^9.
Найдите наибольшую невозрастающую подпоследовательность в A.
В первой строке выведите её длину k, во второй — её индексы
1≤i1<i2<…<ik≤n1≤i1<i2<…<ik≤n
(таким образом, A[i1]≥A[i2]≥…≥A[in]A[i1]≥A[i2]≥…≥A[in]).
"""
# it fucking works!
# O(n log n)
from bisect import bisect_right


def non_increasing_sub(vec):
    # O(n log n) complexity
    # 1 >= 2 >= 3 >= ...
    ancestors = [-1] * len(vec)
    original_numbers = [-1] * len(vec)
    subsequence = [vec[0]]
    original_numbers[0] = 0
    for i, v in enumerate(vec[1:], 1):
        if v >= subsequence[-1]:
            subsequence.append(v)
            original_numbers[len(subsequence)-1] = i
            ancestors[i] = original_numbers[len(subsequence)-2]
        else:
            # bisect_left ?
            pos = bisect_right(subsequence, v)
            subsequence[pos] = v
            original_numbers[pos] = i
            try:
                ancestors[i] = original_numbers[pos-1]
            except IndexError:
                pass
    answer = []
    index = original_numbers[len(subsequence)-1]
    for _ in range(len(subsequence)):
        answer.append(index)
        index = ancestors[index]
    return tuple(reversed(answer))


def main():
    n = int(input())
    # save -x to keep list sorted (we use builtin bisect)
    vec = tuple(map(lambda x: -int(x), input().split()))
    indexes = non_increasing_sub(vec)
    print(len(indexes))
    [print(index+1, end=' ') for index in indexes]


if __name__ == '__main__':
    main()
