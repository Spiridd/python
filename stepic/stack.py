class Stack(list):
    """
    This Stack supports max operation with O(1) complexity
    """
    def __init__(self):
        super(Stack, self).__init__()
        self.max_list = [-1]

    def append(self, item):
        super(Stack, self).append(item)
        if len(self.max_list) == len(self):
            self.max_list.append(max(self.max_list[-1], item))
        else:
            self.max_list[len(self)] = max(self.max_list[len(self)-1], item)

    def get_max(self):
        return self.max_list[len(self)]


def main():
    s = Stack()
    q = int(input())
    for _ in range(q):
        query = input().split()
        if query[0] == 'push':
            s.append(int(query[1]))
        elif query[0] == 'pop':
            s.pop()
        else:
            print(s.get_max())


if __name__ == '__main__':
    main()

