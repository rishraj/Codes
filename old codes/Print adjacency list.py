from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

t = int(input())
for _ in range(t):
    vertices, edges = (int(x) for x in input().split())
    g = Graph(vertices)
    for i in range(edges):
        v1, v2 = (int(x) for x in input().split())
        g.add_edge(v1, v2)
    for i in range(g.V):
        print(i,*(g.graph[i]), sep='-> ')