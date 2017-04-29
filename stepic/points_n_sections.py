# given n sections and m points
# for each point find number of segments
# this point lies on

# complexity: O((m+n) log n)

from bisect import bisect_left, bisect_right


def selection_sort(v, left, right):
    # interval is [left; right]
    # traverse through all elements but last
    for i in range(left, right):
        # find index of the smallest element in the right part
        index = i
        for j in range(i + 1, right + 1):
            if v[j] < v[index]:
                index = j
        # put smallest to its position
        v[i], v[index] = v[index], v[i]


def insertion_sort(v, left, right):
    # interval is [left; right]
    for i in range(left+1, right+1):
        x = v[i]
        j = 0
        while x > v[j]:
            j += 1
        for k in range(i, j, -1):
            v[k] = v[k-1]
        v[j] = x


def simple_sort(v, left, right):
    insertion_sort(v, left, right)


def partition(v, left, right):
    # choose pivot as median of first, middle and last element
    middle = (left + right) // 2
    x = v[middle]
    first, last = v[0], v[-1]
    if first <= last <= x:
        v[middle], v[-1] = v[-1], v[middle]
        x = last
    elif last <= first <= x:
        v[0], v[middle] = v[middle], v[0]
        x = first

    # do swaps
    i, j = left, right
    while i <= j:
        while v[i] < x:
            i += 1
        while x < v[j]:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
    return i - 1


def quick_sort(v, left, right, cutoff):
    # interval is [left; right]
    if right - left > cutoff:
        m = partition(v, left, right)
        quick_sort(v, left, m, cutoff)
        quick_sort(v, m+1, right, cutoff)
    else:
        simple_sort(v, left, right)


def main():
    n, m = map(int, input().split())

    sections_left = []
    sections_right = []
    for _ in range(n):
        left, right = map(int, input().split())
        sections_left.append(left)
        sections_right.append(right)
    # sections_left.sort()
    # sections_right.sort()
    cut = 14
    quick_sort(sections_left, 0, len(sections_left)-1, cut)
    quick_sort(sections_right, 0, len(sections_right)-1, cut)

    points = map(int, input().split())
    for point in points:
        left_good = bisect_right(sections_left, point)
        right_bad = bisect_left(sections_right, point)
        print(left_good - right_bad, end=' ')


if __name__ == '__main__':
    main()
