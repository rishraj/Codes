class Node:
    def __init__(self, data):
        self.data = data
        self.size = 1
        self.child = self


class UnionFind:
    def find(self, v):
        while v.child != v:
            v = v.child
        return v

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1.size > r2.size:
            r2.child = r1
            r1.size = r1.size+r2.size
            r2.size = 0
        else:
            r1.child = r2
            r2.size = r2.size+r1.size
            r1.size = 0

    def same_set(self, v1, v2):
        if self.find(v1) == self.find(v2):
            return True
        else:
            return False


v1 = Node(1)
v2 = Node(2)
v3 = Node(3)
v4 = Node(4)
v5 = Node(5)

union_find = UnionFind()
union_find.union(v1, v3)
union_find.union(v2, v5)
union_find.union(v3, v2)
print(union_find.same_set(v2, v1))
print(union_find.same_set(v1, v4))


