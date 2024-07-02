import sys


def func(p, n):
    dp = [[0 for x in range(n)] for y in range(n)]
    for l in range(1, n-1):
        for i in range(1, n-l):
            j = i+l
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                temp = dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j]
                if dp[i][j] > temp:
                    dp[i][j] = temp
    return dp[1][n-1]

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res.append(func(arr, n))

for i in range(t):
    print(res[i])
