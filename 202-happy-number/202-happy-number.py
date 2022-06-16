class Solution:
    def isHappy(self, n: int) -> bool:
        
        occ = {}
        while n != 1:
            n = sum([int(x) ** 2 for x in str(n)])
            
            if n not in occ:
                occ[n] = n
            else:
                break
            
        if n == 1:
            return True
        else:
            return False