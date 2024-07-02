import random


def my_func(arr, n):
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if dp[j]%2 == 0 and arr[i] < arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
            elif dp[j]%2 == 1 and arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


# n = int(input())
# arr = list(map(int, input().split()))
a = random.randint(1, 10)
arr = []
for i in range(a):
    arr.append(random.randint(1,100))
print(arr)
print(my_func(arr, len(arr)))