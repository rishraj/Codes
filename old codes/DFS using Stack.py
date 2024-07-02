from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v):
        stack = list()
        stack.append(v)
        visited = [False for i in range(self.V)]
        visited[v] = True
        while stack:
            v = stack.pop()
            print(v, end=' ')
            for w in self.graph[v]:
                if not visited[w]:
                    visited[w] = True
                    stack.append(w)


g = Graph(5)
g.add_edge(1, 0)
g.add_edge(2, 1)
g.add_edge(4, 0)
g.add_edge(3, 4)
g.add_edge(0, 3)
g.add_edge(0, 2)
g.DFS(0)