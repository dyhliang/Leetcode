class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        while x <= 31:
            if 2 ** x == n:
                return True
            x += 1
        
        return False
    