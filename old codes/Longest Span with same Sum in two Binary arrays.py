from collections import defaultdict

def my_func(arr1, arr2, n):
    s1 = [0 for x in range(n+1)]
    s2 = [0 for x in range(n+1)]
    temp1 = 0
    temp2 = 0
    for i in range(n):
        temp1 += arr1[i]
        temp2 += arr2[i]
        s1[i+1] = temp1
        s2[i+1] = temp2
    s = []
    for i in range(n+1):
        s.append(s1[i]-s2[i])
    # print(s)
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
    n = int(input())
    arr1 = list(int(x) for x in input().split())
    arr2 = list(int(x) for x in input().split())
    print(my_func(arr1, arr2, n))