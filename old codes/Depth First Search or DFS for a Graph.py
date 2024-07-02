from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        if not visited[v]:
            visited[v] = True
            print(v, ' ', end='')
            for i in self.graph[v]:
                self.DFSUtil(i, visited)

    def DFS(self):
        visited = [False]*len(self.graph)
        for i in g.graph.keys():
            if not visited[i]:
                self.DFSUtil(i, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print(g.graph)
g.DFS()
