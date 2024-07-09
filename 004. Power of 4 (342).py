class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        if not n&(n-1):
            # checked if n is a power of 2
            while n:
                if n&1:
                    return True
                n >>= 2
        return False

        # clever trick to use 32-bit hexadecimal mask to check 1 at odd places
        """ if n <= 0: return False
        if not n&(n-1):
            if n&0x55555555:
                return True
        return False """
        
print (Solution().isPowerOfFour(int(input("Enter n: "))))
