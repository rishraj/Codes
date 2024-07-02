from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, v):
        visited = [False]*len(self.graph)
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            i = queue.popleft()
            print(i, end=" ")
            for j in self.graph[i]:
                if not visited[j]:
                    visited[j] = True
                    queue.append(j)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.BFS(2)