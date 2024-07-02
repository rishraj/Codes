from collections import defaultdict

class Graph():
    def __init__(self, V):
        self.vertices = V
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def hamUtil(self, v, stack):
        if len(stack) == self.vertices:
            return True
        if v not in stack:
            stack.append(v)
            for w in self.graph[v]:
                if self.hamUtil(w, stack):
                    return True
            stack.pop()
        else:
            return False

    def ham(self):
        for i in range(self.vertices):
            stack = []
            if self.hamUtil(i+1, stack):
                return 1
        return 0


for _ in range(int(input())):
    V, E = (int(x) for x in input().split())
    g = Graph(V)
    edges = list(int(x) for x in input().split())
    for i in range(0, 2*E-1, 2):
        g.add_edge(edges[i], edges[i+1])
    print(g.ham())
    # print(g.graph)
