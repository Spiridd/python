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

    def preorder(self):
        print(str(self.data), end=' ')
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(str(self.data), end=' ')
        if self.right_child:
            self.right_child.inorder()
            
    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(str(self.data), end=' ')


def insert(node, v, index):
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
        self.root = Node(v[0][0])
        insert(self.root, v, 0)

    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder()

    def postorder(self):
        self.root.postorder()


def main():
    n = int(input())
    vector = []
    for _ in range(n):
        vector.append(tuple(map(int, input().split())))
    tree = Tree(vector)
    tree.inorder()
    print()
    tree.preorder()
    print()
    tree.postorder()
    print()


if __name__ == '__main__':
    main()
