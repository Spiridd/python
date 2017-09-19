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


class Deque(object):
    """
    it is actually NOT deque
    
    push_back: pushes to the front
    push_front: not implemented
    
    deque contains all the data pushed to it,
    it does not delete unnecessary elements
    """
    def __init__(self, maxsize):
        self.pusher = Stack()
        self.popper = Stack()
        self.size = 0
        self.maxsize = maxsize

    def move_to_popper(self):
        while self.pusher:
            self.popper.append(self.pusher.pop())

    def push_back(self, item):
        if self.size == self.maxsize:
            if not self.popper:
                self.move_to_popper()
            self.popper.pop()
            self.size -= 1
        self.pusher.append(item)
        self.size += 1

    def get_max(self):
        # incorrect, when one of two stacks is empty
        return max(self.popper.get_max(), self.pusher.get_max())


def main():
    n = int(input())
    gen = map(int, input().split())
    window_width = int(input())
    deque = Deque(window_width)
    for _ in range(window_width-1):
        deque.push_back(next(gen))
    for _ in range(n+1-window_width):
        deque.push_back(next(gen))
        print(deque.get_max(), end=' ')


if __name__ == '__main__':
    main()
