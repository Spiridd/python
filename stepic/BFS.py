"""
The program implements breadth-first search in an undirected graph.
It is based on queue structure. Vertices are numbered from 0. 
Graph is represented with adjacency list.
"""


class Stack(list):
    def __init__(self):
        super(Stack, self).__init__()

    def push(self, item):
        super(Stack, self).append(item)


class Queue(object):
    def __init__(self):
        self.getter = Stack()
        self.popper = Stack()

    def push_back(self, item):
        self.getter.push(item)

    def pop(self):
        if not self.popper:
            while self.getter:
                self.popper.push(self.getter.pop())
        return self.popper.pop()

    def __bool__(self):
        return bool(self.getter) or bool(self.popper)


def add_edges(u, v, edges):
    edges[u].add(v)
    edges[v].add(u)


def read_graph():
    nv, ne = map(lambda x: int(x), input().split())
    edges = [set() for _ in range(nv)]
    for _ in range(ne):
        u, v = map(lambda x: int(x), input().split())
        add_edges(u, v, edges)
    return nv, edges


def explore(v, visited, distances, nv, edges):
    queue = Queue()
    visited[v] = True
    distances[v] = 0
    queue.push_back((v, 0))
    while queue:
        u, d = queue.pop()
        notvis_edges = (w for w in edges[u] if not visited[w])
        for w in notvis_edges:
            visited[w] = True
            distances[w] = d+1
            queue.push_back((w, d+1))


def BFS(nv, edges):
    visited = [False] * nv
    distances = [0] * nv
    for v in range(nv):
        if not visited[v]:
            explore(v, visited, distances, nv, edges)
    return distances


def main():
    nv, edges = read_graph()
    distances = BFS(nv, edges)
    [print(d, end=' ') for d in distances]


if __name__ == '__main__':
    main()

