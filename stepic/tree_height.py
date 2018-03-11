def get_height(parents, heights, index):
    if index == -1:
        return 0
    if heights[index] == -1:
        heights[index] = 1 + get_height(parents, heights, parents[index])
    return heights[index]


def get_tree_height(parents):
    heights = [-1] * len(parents)
    for index in range(len(parents)):
        get_height(parents, heights, index)
    return max(heights)


def main():
    _ = int(input())
    parents = tuple(map(int, input().split()))
    print(get_tree_height(parents))


if __name__ == '__main__':
    main()

