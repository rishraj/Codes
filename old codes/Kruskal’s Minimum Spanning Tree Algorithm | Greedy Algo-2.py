from collections import defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.child = self
        self.size = 1


class Graph:
    def __init__(self, vertices):
        self.graph = []
        self.V = vertices

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, v):
        while v.child != v:
            v = v.child
        return v

    def union(self, u, v):
        r1 = self.find(u)
        r2 = self.find(v)
        if r1.size > r2.size:
            r2.child = r1
            r1.size = r1.size + r2.size
            r2.size = 0
        else:
            r1.child = r2
            r2.size = r2.size + r1.size
            r1.size = 0

    def same_set(self, u, v):
        if self.find(u) == self.find(v):
            return True
        else:
            return False

    def kruskalMST(self):
        res = []
        f = 0
        e = 0
        self.graph = sorted(self.graph, key = lambda x: x[2])
        node = []
        for i in range(self.V):
            node.append(Node(i))
        while e < self.V-1:
            u, v, w = self.graph[f]
            f += 1
            if not self.same_set(node[u], node[v]):
                res.append([u, v, w])
                e += 1
                self.union(node[u], node[v])
        for u,v,w in res:
            print(u ,' -- ', v, ' == ', w)


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.kruskalMST()
