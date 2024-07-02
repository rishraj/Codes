def my_func(t, n):
    dp = [0 for x in range(n+1)]
    for i in range(1, n+1):
        m = 0
        flag = False
        for j in range(len(t)):
            if t[j] <= i and dp[i-t[j]] != -1:
                m = max(m, dp[i-t[j]] + 1)
                flag = True
        if not flag:
            dp[i] = -1
        else:
            dp[i] = m
    return dp[n]

for _ in range(int(input())):
    n = int(input())
    t = list(int(x) for x in input().split())
    print(my_func(t, n))