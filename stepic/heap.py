def parent_index(index):
    return (index-1)//2


def left_child_index(index):
    return 2*index+1


def right_child_index(index):
    return 2*index+2


def is_leaf(v, index):
    return True if left_child_index(index) >= len(v) else False


def sift_up(v, index):
    parent = parent_index(index)
    while index > 0 and v[index] < v[parent]:
        v[index], v[parent] = v[parent], v[index]
        index = parent


def sift_down(v, index, swaps):
    size = len(v)
    while True:
        largest = index
        left = left_child_index(index)
        if left < size and v[largest] < v[left]:
            largest = left
        right = right_child_index(index)
        if right < size and v[largest] < v[right]:
            largest = right
        if largest != index:
            v[largest], v[index] = v[index], v[largest]
            swaps.append((index, largest))
            index = largest
        else:
            break


def heapify(v, swaps):
    start = parent_index(len(v)-1)
    for index in range(start, -1, -1):
        sift_down(v, index, swaps)


def main():
    _ = int(input())
    v = list(map(lambda x: -int(x), input().split()))
    swaps = []
    heapify(v, swaps)
    print(len(swaps))
    [print(swap[0], swap[1]) for swap in swaps]


if __name__ == '__main__':
    main()
