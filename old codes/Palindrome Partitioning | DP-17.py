import sys


def is_palindrome(str):
    l = 0
    r = len(str)-1
    while l<r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1
    return True

def palindrome_partition(s):
    n = len(s)
    dp = [[0 for x in range(n)] for y in range(n)]
    for l in range(1, n):
        for i in range(0, n-l):
            j = i+l
            if (is_palindrome(s[i:j+1])):
                dp[i][j] = 0
            else:
                dp[i][j] = sys.maxsize
                for k in range(i, j):
                    temp = dp[i][k] + dp[k+1][j] + 1
                    if temp < dp[i][j]:
                        dp[i][j] = temp
    return dp[0][n-1]


t = int(input())
res = []
for _ in range(t):
    my_str = input()
    res.append(palindrome_partition(my_str))
for i in range(t):
    print(res[i])

