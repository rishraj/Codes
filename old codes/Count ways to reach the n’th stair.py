dp = [0, 1, 2]
m = 1000000007
for i in range(3, 100001):
    dp.append((dp[i-1]%m+dp[i-2]%m)%m)

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
