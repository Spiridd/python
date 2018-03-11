"""
Get the number of connected components of a undirected graph.
The program uses depth-first search. Graph is represented with
adjacency list. Vertices are numbered from 1
"""


def add_edge(v1, v2, edges):
    edges[v1].append(v2)
    edges[v2].append(v1)


def read_graph():
    nvertices, nedges = tuple(map(lambda x: int(x), input().split()))
    # if edges[k] contains m then there is edge {k, m}
    edges = [list() for _ in range(nvertices+1)]
    for _ in range(nedges):
        # get pair of adjacent vertices
        v1, v2 = tuple(map(lambda x: int(x), input().split()))
        add_edge(v1, v2, edges)
    return nvertices, edges


def explore(v, visited, nvertices, edges):
    # stack stores tuples (vertex, index to check)
    stack = [(v, 0)]
    visited[v] = True
    while len(stack) > 0:
        # get upper element
        u, index = stack[-1]
        if index >= len(edges[u]):
            # no more neighbours are left unvisited
            stack.pop()
        else:
            w = edges[u][index]
            stack[-1] = (u, index+1)
            if not visited[w]:
                stack.append((w, 0))
                visited[w] = True


def DFS(nvertices, edges):
    ncomponents = 0
    visited = [False] * (nvertices+1)
    for v in range(1, nvertices+1):
        if not visited[v]:
            ncomponents += 1
            explore(v, visited, nvertices, edges)
    return ncomponents


def main():
    nvertices, adj_matrix = read_graph()
    ncomponents = DFS(nvertices, adj_matrix)
    print(ncomponents)


if __name__ == '__main__':
    main()

