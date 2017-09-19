from heapq import heapify, heappop
from random import randrange
import copy
import time
from matplotlib import pyplot as plt


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
        j = left
        while x > v[j]:
            j += 1
        for k in range(i, j, -1):
            v[k] = v[k-1]
        v[j] = x


def simple_sort(v, left, right):
    # interval is [left; right]
    insertion_sort(v, left, right)
    # selection_sort(v, left, right)


def partition(v, left, right):
    # choose pivot as median of first, middle and last element
    middle = (left + right) // 2
    x = v[middle]
    first, last = v[0], v[-1]  # TODO 0 -> left, -1 -> right
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


def heap_sort(v):
    heap = copy.deepcopy(v)
    heapify(heap)
    index = 0
    size = len(v)
    while index < size:
        v[index] = heappop(heap)
        index += 1


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) \
               + [arr[0]] \
               + qsort([x for x in arr[1:] if x >= arr[0]])


def main(cutoff):
    size = 2000000
    vec = [randrange(0, size) for _ in range(size)]
    quick_sort(vec, 0, len(vec)-1, cutoff)
    # vec = qsort(vec)
    # heap_sort(vec)
    # vec.sort()


if __name__ == '__main__':
    main(12)
    # times = []
    # for cut in range(15, 25):
    #     start = time.time()
    #     main(cut)
    #     end = time.time()
    #     times.append(end-start)
    # plt.plot(range(15, 25), times)
    # plt.grid()
    # plt.show()

