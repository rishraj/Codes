def my_func(A, n, B, m):
    dp = [[0 for x in range(m+1)] for y in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[n][m]


t = int(input())
res = []
for _ in range(t):
    n, m = map(int, input().split())
    A, B = input().split()
    res.append(my_func(A, n, B, m))
for i in range(t):
    print(res[i])
