import sys


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

    def insert_left(self, data):
        if self.left_child:
            self.left_child.insert_left(data)
        else:
            self.left_child = Node(data)

    def insert_right(self, data):
        if self.right_child:
            self.right_child.insert_right(data)
        else:
            self.right_child = Node(data)


def insert(node, v, index):
    # do iteratively
    left_index, right_index = v[index][1], v[index][2]
    if left_index >= 0:
        left_node = Node(v[left_index][0])
        insert(left_node, v, left_index)
        node.left_child = left_node
    if right_index >= 0:
        right_node = Node(v[right_index][0])
        insert(right_node, v, right_index)
        node.right_child = right_node


class Tree(object):
    def __init__(self, v):
        if v:
            self.root = Node(v[0][0])
            insert(self.root, v, 0)
        else:
            self.root = None

    def get_root(self):
        return self.root


def is_bst(node, minimum, maximum):
    if not node:
        return True
    result = True
    if node.left_child:
        if minimum < node.left_child.data < node.data:
            result = is_bst(node.left_child, minimum, min(maximum, node.data))
        else:
            return False
    if node.right_child:
        if node.data < node.right_child.data < maximum:
            result = is_bst(node.right_child, max(minimum, node.data), maximum)
        else:
            return False
    return result


def main():
    sys.setrecursionlimit(2000)
    n = int(input())
    vector = []
    for _ in range(n):
        vector.append(tuple(map(int, input().split())))
    tree = Tree(vector)
    big_number = int(1e100)
    print('CORRECT' if is_bst(tree.get_root(), -big_number, big_number) else 'INCORRECT')


if __name__ == '__main__':
    main()
