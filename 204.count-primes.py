#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        # handle 0 and 1 separately so that flag[1] later doesn't cause issues
        if not n or n == 1:
            return 0

        flag = [0]*(n+1)
        flag[0], flag[1], flag[n]= 1, 1, 1
        # since factors before sqrt(n) multiply with factors after that to give n
        for i in range(2, int(n ** 0.5) + 1):
            if not flag[i]:
                # leaving flag[prime] = 0 and converting flag of its multiples to 1
                cur = i + i
                while cur < n:
                    flag[cur] = 1
                    cur += i
        return n+1 - sum(flag)
        
# @lc code=end

