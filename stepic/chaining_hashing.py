class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def set_next(self, n):
        self.next_node = n

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data


class LinkedList(object):
    def __init__(self):
        self.root = None

    def push_front(self, data):
        temp = self.root
        while temp:
            if temp.get_data() == data:
                return
            temp = temp.get_next()
        new_node = Node(data, self.root)
        self.root = new_node

    def remove(self, data):
        current = self.root
        if current:
            if current.get_data() == data:
                self.root = current.get_next()
            else:
                next_node = current.get_next()
                while next_node and next_node.get_data() != data:
                    current = next_node
                    next_node = current.get_next()
                if next_node:
                    current.set_next(next_node.get_next())

    def __contains__(self, data):
        current = self.root
        while current:
            if current.get_data() == data:
                return True
            current = current.get_next()
        return False

    def __str__(self):
        result = ''
        current = self.root
        while current:
            result = result + current.get_data() + ' '
            current = current.get_next()
        return result


def polynomial_hash(string):
    x = 263
    p = int(1e9+7)
    h = 0
    for char in reversed(string[1:]):
        h += ord(char)
        h *= x
    h += ord(string[0])
    return h % p


def main():
    m = int(input())
    n = int(input())
    hash_table = tuple(LinkedList() for _ in range(m))
    for _ in range(n):
        query = input().split()
        command = query[0]
        string = query[1]
        index = polynomial_hash(string) % m
        if command == 'add':
            hash_table[index].push_front(string)
        elif command == 'find':
            print('yes' if string in hash_table[index] else 'no')
        elif command == 'del':
            hash_table[index].remove(string)
        else:
            print(hash_table[int(string)])


if __name__ == '__main__':
    main()
