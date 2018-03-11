class Node(object):
    def __init__(self, data, c1=None, c2=None):
        self.data = data
        self.left_child = c1
        self.right_child = c2

    def insert(self, data):
        if data == self.data:
            return False
        elif data > self.data:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True
        else:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True

    def find(self, data):
        if data == self.data:
            return True
        elif data > self.data:
            return self.right_child.find(data) if self.right_child else False
        else:
            return self.left_child.find(data) if self.left_child else False

    def preorder(self):
        print(str(self.data))
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(str(self.data))
        if self.right_child:
            self.right_child.inorder()
            
    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(str(self.data))


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root:
            self.root.preorder()

    def inorder(self):
        if self.root:
            self.root.inorder()

    def postorder(self):
        if self.root:
            self.root.posrorder()


def main():
    bst = Tree()
    bst.insert(10)
    bst.insert(1)
    bst.insert(15)
    bst.preorder()


if __name__ == '__main__':
    main()
