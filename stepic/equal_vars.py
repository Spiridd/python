class DisjointSet(object):
    def __init__(self, size):
        self.vars = list(range(size))
        self.rank = [0] * size

    def find(self, index):
        root = index
        while root != self.vars[root]:
            root = self.vars[root]
        # do path compression
        while index != self.vars[index]:
            temp = self.vars[index]
            self.vars[index] = root
            index = temp
        return root

    def union(self, first, second):
        first = self.find(first)
        second = self.find(second)
        if first != second:
            if self.rank[first] > self.rank[second]:
                self.vars[second] = first
            else:
                self.vars[first] = second
                if self.rank[first] == self.rank[second]:
                    self.rank[second] += 1

    def are_equal(self, first, second):
        return self.find(first) == self.find(second)


def main():
    n, e, d = map(int, input().split())
    variables = DisjointSet(n)
    for _ in range(e):
        i, j = map(int, input().split())
        variables.union(i-1, j-1)
    for _ in range(d):
        i, j = map(int, input().split())
        if variables.are_equal(i-1, j-1):
            print(0)
            return
    print(1)


if __name__ == '__main__':
    main()
