from collections import defaultdict

def my_func(arr, n, k):
    s = [0 for x in range(n+1)]
    temp = arr[0]
    for i in range(n-1):
        s[i+1] = temp
        temp += arr[i+1]
    s[n] = temp
    # print(s)
    max_len = 0
    # for i in range(n+1):
    #     for j in range(i, n+1):
    #         if s[j] == s[i]+k:
    #             if j-i > max_len:
    #                 max_len = j-i
    d = defaultdict(int)
    for i in range(n+1):
        d[s[i]] = i
    # print(d)
    for i in range(n+1):
        if s[i]+k in d:
            if d[s[i]+k] - i > max_len:
                max_len = d[s[i]+k] - i
    return max_len


for _ in range(int(input())):
    n, k = (int(x) for  x in input().split())
    arr = list(int(x) for x in input().split())
    print(my_func(arr, n, k))