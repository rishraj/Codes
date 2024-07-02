from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.child = self
        self.size = 1


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)



class UnionFind:
    def find(self, v):
        while v.child != v:
            v = v.child
        return v

    def union(self, u, v):
        r1 = self.find(u)
        r2 = self.find(v)
        if r1.size > r2.size:
            r2.child = r1
            r1.size = r1.size+r2.size
            r2.size = 0
        else:
            r1.child = r2
            r2.size = r2.size+r1.size
            r1.size = 0

    def same_set(self, u, v):
        if self.find(u) == self.find(v):
            return True
        else:
            return False



def is_cyclic(l, g, uf):
    for v in l:
        for w in g.graph[v]:
            if uf.same_set(v, w):
                return True
            else:
                uf.union(v, w)
    return False


v0 = Node(0)
v1 = Node(1)
v2 = Node(2)
l = [v0, v1, v2]
uf = UnionFind()
g = Graph(3)
g.add_edge(v0, v1)
g.add_edge(v1, v2)
g.add_edge(v2, v0)
print(is_cyclic(l, g, uf))