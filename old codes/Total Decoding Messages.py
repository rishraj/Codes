def my_func(arr, n):
    dp = [0 for x in range(n+1)]
    dp[0] = 1
    if arr[0] == 0:
        return 0
    dp[1] = 1
    for i in range(2, n+1):
        temp = arr[i-2]*10 + arr[i-1]
        if i<n and arr[i] == 0:
            dp[i] = dp[i-1]
        elif arr[i-1] == 0:
            if arr[i-2] == 1 or arr[i-2] == 2:
                dp[i] = dp[i-1]
            else:
                return 0
        else:
            if temp > 0 and temp<=26 and arr[i-2]!=0:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
    # print(dp)
    return dp[n]


for _ in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().strip())
    print(my_func(arr, n))