#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False

        totalBits = 0
        while n:
            totalBits += n&1
            n >>= 1
        if totalBits == 1: return True
        return False

        # a clever trick: n&(n-1) is always 0 for powers of 2
        """ if n >= 1 and (n & (n - 1)) == 0:
            return True
        return False """
        
# @lc code=end

