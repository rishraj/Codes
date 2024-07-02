def my_func(arr, n):
    dp = [0 for i in range(n+1)]
    dp[1] = arr[0]
    for i in range(2, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i-1])
    return dp[n]


for _ in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().split())
    print(my_func(arr, n))