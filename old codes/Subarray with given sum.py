from collections import defaultdict


def my_func(arr, n, k):
    d = defaultdict(int)
    s = 0
    d[0] = 0
    for i in range(n):
        s += arr[i]
        if (s-k) in d:
            return [d[s-k]+1, i+1]
        d[s] = i+1
    return [-1]


for _ in range(int(input())):
    n, k = (int(x) for x in input().split())
    arr = list(int(x) for x in input().split())
    print(*my_func(arr, n, k))