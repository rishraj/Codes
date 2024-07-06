class BitManipulation:
    def getIthBit(self, n: int, i: int):
        return (n >> i) & 1
    
    def setIthBit(self, n: int, i: int):
        return (1<<i) | n
    
    def totalBits(self, n: int):
        res = 0
        while n:
            res += n&1
            n >>= 1
        return res