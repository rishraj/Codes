from collections import defaultdict
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottom_view(root):
    if root is None:
        return
    h_dict = defaultdict(deque)
    queue = deque()
    queue.append([root, 0])
    while queue:
        v, h = queue.popleft()
        h_dict[h].append(v.data)
        if v.left is not None:
            queue.append([v.left, h-1])
        if v.right is not None:
            queue.append([v.right, h+1])

    res = []
    for i in h_dict.keys():
        res.append([i, h_dict[i].pop()]) #res.append([i, h_dict[i].popleft()]) for Top View
    res = sorted(res, key = lambda x: x[0])
    for i in res:
        print(i[1], end=' ')


root = Node(20)
# root.left = Node(8)
# root.right = Node(22);
# root.left.left = Node(5);
# root.left.right = Node(3);
# root.right.left = Node(4);
# root.right.right = Node(25);
# root.left.right.left = Node(10);
# root.left.right.right = Node(14);
root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.left.right = Node(4);
root.left.right.right = Node(5);
root.left.right.right.right = Node(6);

bottom_view(root)