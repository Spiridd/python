class TableList(object):
    """
    Based on disjoint set
    
    parent[item] is data xor index parent
    data is negative or zero
    reference is positive (that's why you see [source-1])
    """
    def __init__(self, parent):
        self.parent = parent
        self.max_size = -min(parent)

    def get_max_size(self):
        return self.max_size

    def find(self, index):
        root = index
        while self.parent[root-1] > 0:
            root = self.parent[root-1]
        # do path compression
        while self.parent[index-1] > 0:
            temp = self.parent[index-1]
            self.parent[index-1] = root
            index = temp
        return root

    def move_data(self, source, destination):
        source = self.find(source)
        destination = self.find(destination)
        if destination != source:
            self.parent[destination-1] += self.parent[source-1]
            self.max_size = max(self.max_size, -self.parent[destination-1])
            self.parent[source-1] = destination


def main():
    n, m = map(int, input().split())
    # initialize with minuses!
    records = list(map(lambda x: -int(x), input().split()))
    tables = TableList(records)
    for _ in range(m):
        source, destination = map(int, input().split())
        tables.move_data(source, destination)
        print(tables.get_max_size())


if __name__ == '__main__':
    main()
