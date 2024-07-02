def my_func(t, n, val):
    dp = [[0 for x in range(val+1)] for y in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(val+1):
            if j < t[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-t[i-1]]
    return dp[n][val]


z = int(input())
res = []
for _ in range(z):
    n = int(input())
    t = list(map(int, input().split()))
    val = int(input())
    res.append(my_func(t, n, val))
for i in range(z):
    print(res[i])
