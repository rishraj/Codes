from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.g = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.g[u].append(v)

    def is_cyclic(self):
        visited = [False for i in range(self.V)]
        stack  = [False for i in range(self.V)]
        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, stack):
                    return True
        return False

    def is_cyclic_util(self, v, visited, stack):
        visited[v] = True
        stack[v] = True
        for w in self.g[v]:
            if not visited[w]:
                if self.is_cyclic_util(w, visited, stack):
                    return True
            elif stack[w]:
                return True
        stack[v] = False
        return False


graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
if graph.is_cyclic():
    print('Cycle present.')
else:
    print('Cycle not present.')
