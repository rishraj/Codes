from collections import defaultdict


def my_func(arr, n):
    s = [0 for x in range(n+1)]
    if arr[0] == 0:
        temp = -1
    else:
        temp = 1
    for i in range(n-1):
        if arr[i+1] == 0:
            s[i+1] = temp
            temp += -1
        else:
            s[i+1] = temp
            temp += 1
    s[n] = temp
    # print(s)
    d = defaultdict(list)
    max_len = 0
    for i in range(n+1):
        d[s[i]].append(i)
    for key in d:
        m = len(d[key])
        if d[key][m-1] - d[key][0] > max_len:
            max_len = d[key][m-1] - d[key][0]
    return max_len

for i in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().split())
    print(my_func(arr, n))