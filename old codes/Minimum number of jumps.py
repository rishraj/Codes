def my_func(arr, n):
    dp = [0 for x in range(n+1)]
    if arr[0] == 0:
        dp[1] = -1
    else:
        dp[1] = 0
    for i in range(2, n+1):
        minimum = float('inf')
        flag = False
        for k in range(1, i):
            if arr[k-1] >= i-k and dp[k] != -1:
                flag = True
                minimum = min(minimum, dp[k]+1)
        if flag:
            dp[i] = minimum
        else:
            dp[i] = -1
    return dp[n]

for _ in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().split())
    print(my_func(arr, n))