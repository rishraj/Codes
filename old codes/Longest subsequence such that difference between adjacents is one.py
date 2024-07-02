t = int(input())
final_res = []


def hi(arr, n):
    dp = [1 for x in range(n)]
    for i in range(n):
        for j in range(i):
            if (arr[i] == arr[j] + 1) or (arr[i] == arr[j] - 1):
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


for _ in range(t):
    n = int(input())
    arr = map(int, raw_input().split())
    final_res.append(hi(arr, n))
for i in range(len(final_res)):
    print(final_res[i])