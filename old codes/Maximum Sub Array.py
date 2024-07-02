from collections import defaultdict

def my_func(arr, n):
    ni = []
    for i in range(n):
        if arr[i] < 0:
            ni.append(i)
    if len(ni) == 0:
        print(*arr)
        return
    prev = -1
    curr = ni[0]
    ss = []
    c = 0
    while prev != ni[-1]:
        if arr[prev+1:curr] != []:
            ss.append(arr[prev+1:curr])
        prev = curr
        c += 1
        if c<len(ni):
            curr = ni[c]
    if ni[-1] != n-1:
        ss.append(arr[ni[-1]+1:n])
    print(ss)
    d = defaultdict(list)
    for s in ss:
        d[sum(s)].append(s)
    m = max(d.keys())
    m_len = len(d[m][0])
    m_len_i = 0
    for i in range(len(d[m])):
        if len(d[m][i]) > m_len:
            m_len = len(d[m][i])
            m_len_i = i
    print(*d[m][m_len_i])



for _ in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().split())
    my_func(arr, n)
