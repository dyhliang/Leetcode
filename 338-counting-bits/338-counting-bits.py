class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [bin(n).count('1') for n in range(0, n+1)]
        return res
    