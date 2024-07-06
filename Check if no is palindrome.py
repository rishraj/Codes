from math import floor, log10, pow

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        
        digits = floor(log10(x)) + 1
        p = pow(10, digits-1)
        
        for i in range(digits // 2):
            if (x // p) != (x % 10):
                return False
            x = x % p
            x = x // 10
            p /= 100
            
        return True
        """ x = str(x)
        left, right = 0, len(x)-1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True """
        
    
x = int(input("Enter x: "))
sol = Solution()
print (sol.isPalindrome(x))
