def my_func(A, B):
    n = len(A)
    m = len(B)
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[j-1] == B[i-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]


t = int(input())
res = []
for _ in range(t):
    n, m = list(map(int, input().split()))
    str1 = input()
    str2 = input()
    res.append(my_func(list(str1), list(str2)))
for i in range(t):
    print(res[i])
