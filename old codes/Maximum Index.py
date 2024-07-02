def my_func(arr, n):
    s = []
    for i in range(n):
        s.append([arr[i], i])
    s = sorted(s, key=lambda x: x[0])
    # print(s)
    max_diff = -1
    minimum = s[0][1]
    for i in range(len(s)):
        if s[i][1] < minimum:
            minimum = s[i][1]
            continue
        if s[i][1]-minimum > max_diff:
            max_diff = s[i][1]-minimum
    print(max_diff)

for _ in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().split())
    my_func(arr, n)