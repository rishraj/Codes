import math

def my_func(n):
    dp = [10000 for i in range(n+1)]
    dp[0] = 0
    for i in range(1, int(math.sqrt(n))):
        dp[i*i] = 1
    for i in range(1, n+1):
        for j in range(1, int(math.sqrt(i))+1):
            dp[i] = min(dp[i], dp[i-(j*j)]+1)
    return dp[n]


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    res.append(my_func(n))
for i in range(t):
    print(res[i])