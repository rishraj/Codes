def my_func(n, k):
    res = [0 for x in range(k)]
    if k%2 == 0:
        for i in range(k-1):
            if i%2 == 0:
                res[i] = 0
            elif n > 0:
                res[i] = 1
                n -= 1
            else:
                res[i] = 0
        res[k-1] = n
    else:
        for i in range(k-1):
            if i%2 == 1:
                res[i] = 0
            elif n > 0:
                res[i] = 1
                n -= 1
            else:
                res[i] = 0
        res[k-1] = n
    new_res = []
    for i in range(k-1, -1, -1):
        new_res.append(res[i])
    print(*new_res)


for _ in range(int(input())):
    n, k = (int(x) for x in input().split())
    my_func(n, k)
# n = coins         k = people