from collections import defaultdict

def my_func(arr, n, k):
    s = [0 for x in range(n+1)]
    temp = arr[0]
    for i in range(n-1):
        s[i+1] = temp
        temp += arr[i+1]
    s[n] = temp
    for i in range(n+1):
        s[i] = s[i]%k
    d = defaultdict(list)
    for i in range(n+1):
        d[s[i]].append(i)
    max_len = 0
    for key in d:
        m = len(d[key])
        if d[key][m-1] - d[key][0] > max_len:
            max_len = d[key][m-1] - d[key][0]
    return max_len



for _ in range(int(input())):
    n, k = (int(x) for x in input().split())
    arr = list(int(x) for x in input().split())
    print(my_func(arr, n, k))