def my_func(arr, n):
    dp = [0 for x in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1]+arr[i])
    return max(dp)

for _ in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().split())
    print(my_func(arr, n))