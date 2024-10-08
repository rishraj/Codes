#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0
        
        for i in range(32):
            x <<= 1
            x = x | (n & 1)
            n >>= 1
        # alternative soln is to get the i'th bit of n and set it to 32-i'th bit of x
        return x
# @lc code=end

