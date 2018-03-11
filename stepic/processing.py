class Node(object):
    def __init__(self, arrival, duration, num, next_node=None):
        self.arrival = arrival
        self.duration = duration
        self.num = num
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_arrival(self):
        return self.arrival

    def get_duration(self):
        return self.duration

    def __str__(self):
        return ' '.join([str(self.num), str(self.arrival), str(self.duration)])


class Processor(object):
    def __init__(self, maxsize=10, root=None):
        self.root = root
        self.last = root
        self.maxsize = maxsize
        self.size = 0
        self.time = 0
        self.process_time = 0
        self.iterated = root

    def pop(self):
        self.process_time -= self.root.get_duration()
        self.root = self.root.get_next()
        self.size -= 1

    def get_queue_time(self):
        return self.process_time-self.root.get_duration()

    def add(self, node):
        if self.size < self.maxsize:
            if self.size == 0:
                self.root = node
            else:
                self.last.set_next(node)
            self.last = node
            self.size += 1
            self.time = max(self.time, node.get_arrival())
            print(self.time)
            self.time += node.get_duration()
            self.process_time += node.get_duration()
        elif node.get_arrival() >= self.time-self.get_queue_time():
            self.pop()
            self.add(node)
        else:
            print(-1)

    def finish(self):
        while self.size > 0:
            self.pop()

    def __iter__(self):
        self.iterated = self.root
        return self

    def __next__(self):
        if self.iterated:
            current = self.iterated
            self.iterated = self.iterated.get_next()
            return current
        else:
            raise StopIteration


def main():
    maxsize, n = map(int, input().split())
    processor = Processor(maxsize)
    for num in range(n):
        arrival, duration = map(int, input().split())
        node = Node(arrival, duration, num)
        processor.add(node)


if __name__ == '__main__':
    main()

