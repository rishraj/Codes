import sys


class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for x in range(vertices)] for y in range(vertices)]
        self.V = vertices

    def min_key_index(self, included, key):
        temp = sys.maxsize
        for i in range(self.V):
            if key[i] < temp and not included[i]:
                temp = key[i]
                temp_index = i
        return temp_index

    def printMST(self, parent):
        for i in range(1, self.V):
            print(i, ' -- ', parent[i], ' == ', self.graph[i][parent[i]])

    def primMST(self):
        included = [False for _ in range(self.V)]
        key = [sys.maxsize for _ in range(self.V)]
        parent = [-1 for _ in range(self.V)]
        key[0] = 0
        for i in range(self.V):
            v = self.min_key_index(included, key)
            included[v] = True
            for j in range(self.V):
                if self.graph[i][j] > 0 and key[j] > self.graph[i][j] and not included[j]:
                    key[j] = self.graph[i][j]
                    parent[j] = i
        self.printMST(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0],
           ]

g.primMST()