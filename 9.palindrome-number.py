#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # div could also be found using 10^(digits-1) where digits = floor(log10(x))+1
        div = 1
        while x >= div * 10:
                div *= 10

        while x:
            if (x // div) != (x % 10):
                return False
            
            x = (x % div) // 10
            div /= 100
            
        return True
    
        # if we convert x to a string:
        
        """ x = str(x)
        left, right = 0, len(x)-1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True """
        
# @lc code=end

